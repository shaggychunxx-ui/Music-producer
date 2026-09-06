"""ffmpeg ops ported from Mira-Soline Edit-Video.py, adapted for music.

Mira loop/stitch strips audio (-an) so reverse does not rewind a soundtrack.
That is still correct for visualizers. Extract / mux / prepare-s1 are the
music-specific additions (48 kHz).
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

COMFY = "http://127.0.0.1:8189"
SHARED = Path.home() / "AppData/Local/Comfy-Desktop/ComfyUI-Shared"
INSTALL_IO = Path.home() / "AppData/Local/Comfy-Desktop/ComfyUI-Installs/ComfyUI/ComfyUI"
INPUT_DIRS = [SHARED / "input", INSTALL_IO / "input"]
OUTPUT_DIRS = [SHARED / "output", INSTALL_IO / "output"]
DAW_SR = 48000


def get_ffmpeg() -> str:
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    raise SystemExit("ffmpeg not found. pip install imageio-ffmpeg or add ffmpeg to PATH.")


def run_ffmpeg(args: list[str]) -> subprocess.CompletedProcess[str]:
    cmd = [get_ffmpeg(), "-hide_banner", "-y", *args]
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(path: Path) -> dict:
    p = subprocess.run(
        [get_ffmpeg(), "-hide_banner", "-i", str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    err = p.stderr or ""
    dur = 0.0
    fps = 0.0
    w = h = 0
    has_audio = "Audio:" in err
    if "Duration:" in err:
        t = err.split("Duration:")[1].split(",")[0].strip()
        hh, mm, ss = t.split(":")
        dur = int(hh) * 3600 + int(mm) * 60 + float(ss)
    for tok in err.replace(",", " ").split():
        if "x" in tok and tok[0].isdigit():
            a, b = tok.split("x", 1)
            if a.isdigit() and b.split("[")[0].isdigit():
                w, h = int(a), int(b.split("[")[0])
                break
    if " fps" in err:
        try:
            fps = float(err.split(" fps")[0].split()[-1])
        except ValueError:
            pass
    return {"dur": round(dur, 3), "fps": fps, "w": w, "h": h, "audio": has_audio}


def dump_frames(src: Path, dest_dir: Path, times: list[float], prefix: str, dur: float | None = None) -> list[Path]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    info_dur = dur if dur is not None else probe(src)["dur"]
    outs: list[Path] = []
    for t in times:
        name = f"{prefix}-{t:.2f}s.png".replace(".", "p", 1)
        out = dest_dir / name
        if info_dur > 0 and t >= info_dur - 0.08:
            r = run_ffmpeg(["-sseof", "-0.04", "-i", str(src), "-frames:v", "1", "-q:v", "3", str(out)])
        else:
            r = run_ffmpeg(["-ss", f"{max(0.0, t):.3f}", "-i", str(src), "-frames:v", "1", "-q:v", "3", str(out)])
        if r.returncode != 0 or not out.exists() or out.stat().st_size < 1000:
            print("frame fail", t, (r.stderr or "")[-400:])
            continue
        outs.append(out)
        print("qc", out.name, out.stat().st_size)
    return outs


def cmd_loop(src: Path, dest: Path, fade: float) -> int:
    info = probe(src)
    d = info["dur"]
    if d < 0.4:
        print("too short", d)
        return 1
    fade = min(fade, max(0.0, d * 0.2))
    dest.parent.mkdir(parents=True, exist_ok=True)
    if fade >= 0.08:
        offset = max(0.05, d - fade)
        filt = (
            f"[0:v]split[f][t];[t]reverse[r];"
            f"[f][r]xfade=transition=fade:duration={fade:.3f}:offset={offset:.3f},format=yuv420p[v]"
        )
        print("loop xfade", fade, "offset", round(offset, 3), "durA", d)
    else:
        filt = (
            "[0:v]split[f][t];[t]reverse,select='not(eq(n,0))',setpts=PTS-STARTPTS[r];"
            "[f][r]concat=n=2:v=1,format=yuv420p[v]"
        )
        print("loop concat no-freeze durA", d)
    r = run_ffmpeg(
        [
            "-i", str(src),
            "-filter_complex", filt,
            "-map", "[v]", "-an",
            "-c:v", "libx264", "-crf", "18", "-preset", "fast",
            "-movflags", "+faststart",
            str(dest),
        ]
    )
    if r.returncode != 0:
        print((r.stderr or "")[-2500:])
        return r.returncode
    out_info = probe(dest)
    print("ok", dest, dest.stat().st_size, "dur", out_info["dur"])
    mid = d - (fade * 0.5 if fade >= 0.08 else 0.0)
    end = max(0.05, out_info["dur"] - 0.05)
    dump_frames(
        dest,
        dest.parent / f"{dest.stem}-qc",
        [0.05, max(0.1, mid - 0.15), mid, min(end, mid + 0.15), end],
        dest.stem,
        dur=out_info["dur"],
    )
    return 0


def cmd_stitch(a: Path, b: Path, dest: Path, skip_b: float, fade: float) -> int:
    da = probe(a)["dur"]
    if da <= fade + 0.05:
        print("A too short", da)
        return 1
    offset = max(0.05, da - fade)
    dest.parent.mkdir(parents=True, exist_ok=True)
    print("stitch skip_b", skip_b, "fade", fade, "offset", round(offset, 3), "durA", da)
    r = run_ffmpeg(
        [
            "-i", str(a),
            "-ss", f"{skip_b:.3f}", "-i", str(b),
            "-filter_complex",
            f"[0:v][1:v]xfade=transition=fade:duration={fade:.3f}:offset={offset:.3f},format=yuv420p",
            "-an", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
            "-movflags", "+faststart",
            str(dest),
        ]
    )
    if r.returncode != 0:
        print((r.stderr or "")[-2500:])
        return r.returncode
    print("ok", dest, dest.stat().st_size, "dur", probe(dest)["dur"])
    dump_frames(dest, dest.parent / f"{dest.stem}-qc", [offset - 0.15, offset, offset + 0.15], dest.stem)
    return 0


def cmd_qc(src: Path, dest_dir: Path | None) -> int:
    info = probe(src)
    d = info["dur"]
    dest_dir = dest_dir or (src.parent / f"{src.stem}-qc")
    times = [0.05, d * 0.25, d * 0.5, d * 0.75, max(0.05, d - 0.05)]
    dump_frames(src, dest_dir, times, src.stem)
    print("probe", info)
    return 0


def cmd_grain(src: Path, dest: Path, strength: int = 8) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    filt = f"gblur=sigma=0.4,noise=alls={strength}:allf=t,format=yuv420p"
    print("grain", strength, src.name)
    r = run_ffmpeg(
        [
            "-i", str(src), "-vf", filt, "-an",
            "-c:v", "libx264", "-crf", "18", "-preset", "fast",
            "-movflags", "+faststart", str(dest),
        ]
    )
    if r.returncode != 0:
        print((r.stderr or "")[-2000:])
        return 1
    print("ok", dest, dest.stat().st_size)
    return 0


def cmd_extract_audio(src: Path, dest: Path, sr: int = DAW_SR) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print("extract-audio", sr, src.name)
    r = run_ffmpeg(
        [
            "-i", str(src),
            "-vn", "-acodec", "pcm_s16le", "-ar", str(sr), "-ac", "2",
            str(dest),
        ]
    )
    if r.returncode != 0:
        print((r.stderr or "")[-2000:])
        return r.returncode
    print("ok", dest, dest.stat().st_size, probe(dest))
    return 0


def cmd_mux(video: Path, audio: Path, dest: Path) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print("mux", video.name, "+", audio.name)
    r = run_ffmpeg(
        [
            "-i", str(video), "-i", str(audio),
            "-map", "0:v:0", "-map", "1:a:0",
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "320k", "-ar", str(DAW_SR),
            "-shortest",
            "-movflags", "+faststart",
            str(dest),
        ]
    )
    if r.returncode != 0:
        print((r.stderr or "")[-2000:])
        return r.returncode
    print("ok", dest, dest.stat().st_size, probe(dest))
    return 0


def cmd_remux(src: Path, dest: Path) -> int:
    """Copy remux, strip metadata / C2PA-style boxes (Mira Post-ToX.drop_c2pa)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    common = ["-map_metadata", "-1", "-movflags", "+faststart", "-fflags", "+bitexact", str(dest)]
    attempts = [
        ["-i", str(src), "-map", "0:v:0", "-map", "0:a:0?", "-c", "copy", *common],
        ["-i", str(src), "-map", "0:v:0", "-c:v", "copy", *common],
    ]
    last = None
    for args in attempts:
        last = run_ffmpeg(args)
        if last.returncode == 0 and dest.exists() and dest.stat().st_size > 1000:
            print("ok remux", dest, dest.stat().st_size)
            return 0
    print((last.stderr if last else "")[-2000:])
    return last.returncode if last else 1


def cmd_prepare_s1(src: Path, dest_dir: Path, fps: float | None = None) -> int:
    """Constant-fps yuv420p mp4 + 48 kHz wav sidecar for Studio One import."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    info = probe(src)
    use_fps = fps or (info["fps"] if info["fps"] >= 1 else 30.0)
    mp4 = dest_dir / f"{src.stem}.s1.mp4"
    wav = dest_dir / f"{src.stem}.48k.wav"
    print("prepare-s1 fps", use_fps, src.name)
    r = run_ffmpeg(
        [
            "-i", str(src),
            "-an",
            "-vf", f"fps={use_fps:.3f},format=yuv420p",
            "-c:v", "libx264", "-crf", "18", "-preset", "fast",
            "-movflags", "+faststart",
            str(mp4),
        ]
    )
    if r.returncode != 0:
        print((r.stderr or "")[-2000:])
        return r.returncode
    rc = 0
    if info.get("audio"):
        rc = cmd_extract_audio(src, wav)
    else:
        print("no audio in source; wav sidecar skipped")
        wav = None
    report = {
        "src": str(src),
        "mp4": str(mp4),
        "wav": str(wav) if wav else None,
        "fps": use_fps,
        "probe_in": info,
        "probe_mp4": probe(mp4),
        "studio_one_artist": "Import wav as Audio Track. Video Track is Professional-only.",
        "sample_rate": DAW_SR,
    }
    rep = dest_dir / f"{src.stem}.s1.json"
    rep.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("report", rep)
    return rc


def _post(path: str, data: dict | None = None):
    body = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(
        COMFY + path,
        data=body,
        headers={"Content-Type": "application/json"} if data else {},
        method="GET" if data is None else "POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def _find_output(name: str) -> Path | None:
    for root in OUTPUT_DIRS:
        for p in (root / name, root / "xclipslearn" / name, root / "video" / name):
            if p.exists():
                return p
        hits = list(root.rglob(name))
        if hits:
            return max(hits, key=lambda x: x.stat().st_mtime)
    return None


def cmd_rife(src: Path, dest: Path) -> int:
    staged_dir = next((d for d in INPUT_DIRS if d.is_dir()), INPUT_DIRS[0])
    staged_dir.mkdir(parents=True, exist_ok=True)
    staged = staged_dir / "src_rife.mp4"
    shutil.copy2(src, staged)
    g = {
        "1": {"class_type": "LoadVideo", "inputs": {"file": "src_rife.mp4"}},
        "2": {"class_type": "GetVideoComponents", "inputs": {"video": ["1", 0]}},
        "3": {
            "class_type": "RIFE VFI",
            "inputs": {
                "ckpt_name": "rife49.pth",
                "frames": ["2", 0],
                "clear_cache_after_n_frames": 5,
                "multiplier": 4,
                "fast_mode": True,
                "ensemble": True,
                "scale_factor": 1.0,
                "dtype": "float16",
                "torch_compile": False,
                "batch_size": 1,
            },
        },
        "4": {"class_type": "CreateVideo", "inputs": {"images": ["3", 0], "fps": 60}},
        "5": {
            "class_type": "SaveVideo",
            "inputs": {
                "video": ["4", 0],
                "filename_prefix": "xclipslearn/rife",
                "format": "auto",
                "codec": "auto",
            },
        },
    }
    print("RIFE 4x", src.name, "via", COMFY)
    try:
        res = _post("/prompt", {"prompt": g})
    except OSError as e:
        print("comfy down", e)
        return 6
    if res.get("node_errors"):
        print("node_errors", res["node_errors"])
        return 2
    pid = res["prompt_id"]
    t0 = time.time()
    while time.time() - t0 < 400:
        h = _post("/history/" + pid)
        if pid in h:
            item = h[pid]
            if (item.get("status") or {}).get("status_str") == "error":
                print("error", json.dumps(item.get("status"))[:2000])
                return 3
            for node in (item.get("outputs") or {}).values():
                for im in (node.get("images") or []) + (node.get("videos") or []):
                    name = im.get("filename") or ""
                    p = _find_output(name)
                    if p and p.exists():
                        shutil.copy2(p, dest)
                        print("ok", dest, dest.stat().st_size)
                        return 0
            print("no output")
            return 4
        time.sleep(2)
    print("timeout")
    return 5


def _need(path: Path) -> Path:
    p = Path(path)
    if not p.is_file():
        print("missing", p, file=sys.stderr)
        raise SystemExit(1)
    return p
