#!/usr/bin/env python3
"""Capture short WASAPI loopback clips while Spotify is playing on this PC.

Writes the same taste_data shape as GitStatus phone clips:
  source=spotify_pc
  taste_data/clips/YYYY/MM/clip_*.wav
  taste_data/listen_log.jsonl

Only records when Spotify is actually playing. Silent clips are discarded.
"""

from __future__ import annotations

import argparse
import json
import logging
import random
import secrets
import sys
import time
import wave
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

TOOLS = Path(__file__).resolve().parent
PKG_ROOT = TOOLS.parent
TASTE = PKG_ROOT / "taste_data"
LOG_PATH = TASTE / "pc_capture.log"

SAMPLE_RATE = 16000
MIN_SEC = 8
MAX_SEC = 25
GAP_MIN = 20
GAP_MAX = 119
MAX_WAV_BYTES = 900_000
PEAK_DB_MIN = -45.0
ACTIVITY_MIN = 0.05

SPOTIFY_APP_HINTS = (
    "spotify",
    "spotify.exe",
    "spotifyab.exe",
)
BROWSER_APP_HINTS = ("chrome", "msedge", "edge", "firefox", "brave", "opera")
NOT_SPOTIFY_HINTS = (
    "youtube",
    "netflix",
    "twitch",
    "disney",
    "prime video",
    "hulu",
    "soundcloud",
    "apple music",
    "amazon music",
)


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def setup_log(verbose: bool = False) -> None:
    TASTE.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


# --- now playing -----------------------------------------------------------


def _smtc_sessions() -> list[dict[str, str]]:
    """Windows System Media Transport Controls via winrt."""
    try:
        import asyncio

        import winrt.windows.foundation.collections  # noqa: F401 — required by get_sessions()
        from winrt.windows.media.control import (
            GlobalSystemMediaTransportControlsSessionManager as MediaManager,
            GlobalSystemMediaTransportControlsSessionPlaybackStatus as Status,
        )
    except Exception:
        return []

    async def _go() -> list[dict[str, str]]:
        mgr = await MediaManager.request_async()
        out: list[dict[str, str]] = []
        for s in mgr.get_sessions():
            info = s.get_playback_info()
            props = await s.try_get_media_properties_async()
            playing = bool(
                info
                and info.playback_status == Status.PLAYING
            )
            out.append(
                {
                    "app": (s.source_app_user_model_id or "").lower(),
                    "artist": (props.artist if props else "") or "",
                    "title": (props.title if props else "") or "",
                    "album": (props.album_title if props else "") or "",
                    "playing": playing,
                }
            )
        return out

    try:
        return asyncio.run(_go())
    except Exception as exc:
        logging.debug("SMTC failed: %s", exc)
        return []


def _window_process_name(hwnd: int) -> str:
    import ctypes
    from ctypes import wintypes

    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    if not pid.value:
        return ""
    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid.value)
    if not handle:
        return ""
    try:
        size = wintypes.DWORD(32768)
        buf = ctypes.create_unicode_buffer(size.value)
        if kernel32.QueryFullProcessImageNameW(handle, 0, buf, ctypes.byref(size)):
            return Path(buf.value).name.lower()
    finally:
        kernel32.CloseHandle(handle)
    return ""


def _spotify_window_track() -> dict[str, str] | None:
    """Parse the Spotify desktop window title: 'Song - Artist'."""
    if sys.platform != "win32":
        return None
    import ctypes
    from ctypes import wintypes

    user32 = ctypes.windll.user32
    titles: list[str] = []

    @ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    def _enum(hwnd, _lp):
        if not user32.IsWindowVisible(hwnd):
            return True
        if _window_process_name(hwnd) != "spotify.exe":
            return True
        n = user32.GetWindowTextLengthW(hwnd)
        if n <= 0:
            return True
        buf = ctypes.create_unicode_buffer(n + 1)
        user32.GetWindowTextW(hwnd, buf, n + 1)
        title = buf.value.strip()
        if title:
            titles.append(title)
        return True

    user32.EnumWindows(_enum, 0)
    for title in titles:
        low = title.lower()
        if low in {"spotify", "spotify premium", "spotify free"}:
            return {"artist": "", "title": "", "album": "", "playing": False, "app": "spotify"}
        # Desktop: "Track - Artist"
        if " - " in title:
            left, right = title.rsplit(" - ", 1)
            if right.lower().startswith("spotify"):
                # "Track - Artist - Spotify"
                parts = title.split(" - ")
                if len(parts) >= 3:
                    return {
                        "artist": parts[1].strip(),
                        "title": parts[0].strip(),
                        "album": "",
                        "playing": True,
                        "app": "spotify",
                    }
            return {
                "artist": right.strip(),
                "title": left.strip(),
                "album": "",
                "playing": True,
                "app": "spotify",
            }
    return None


def _spotify_process_running() -> bool:
    if sys.platform != "win32":
        return False
    import subprocess

    r = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq Spotify.exe", "/NH"],
        capture_output=True,
        text=True,
        timeout=8,
    )
    return "Spotify.exe" in (r.stdout or "")


def _looks_like_other_service(text: str) -> bool:
    low = text.lower()
    return any(h in low for h in NOT_SPOTIFY_HINTS)


def _is_spotify_session(s: dict[str, Any]) -> bool:
    if not s.get("playing"):
        return False
    app = (s.get("app") or "").lower()
    blob = " ".join(
        str(s.get(k) or "") for k in ("app", "artist", "title", "album")
    )
    if _looks_like_other_service(blob):
        return False
    if any(h in app for h in SPOTIFY_APP_HINTS):
        return True
    if "spotify" in blob.lower():
        return True
    # Web player: Chrome/Edge SMTC with artist+title and no other-service markers.
    if any(h in app for h in BROWSER_APP_HINTS) and (s.get("title") or s.get("artist")):
        return True
    return False


def now_playing() -> dict[str, Any] | None:
    sessions = _smtc_sessions()
    for s in sessions:
        if _is_spotify_session(s):
            s = dict(s)
            s.setdefault("app", "spotify.web")
            return s
    win = _spotify_window_track()
    if win and win.get("playing"):
        return win
    return None


# --- fingerprint (same math as GitStatus ClipFingerprint) -----------------


def _db(x: float) -> float:
    return max(-120.0, 20.0 * np.log10(max(x, 1e-12)))


def _one_pole_split(x: np.ndarray, cutoff_hz: float, sr: int) -> tuple[np.ndarray, np.ndarray]:
    rc = 1.0 / (2.0 * np.pi * max(cutoff_hz, 1.0))
    dt = 1.0 / sr
    a = dt / (rc + dt)
    y = 0.0
    low = np.empty_like(x)
    high = np.empty_like(x)
    for i, v in enumerate(x):
        y += a * (float(v) - y)
        low[i] = y
        high[i] = float(v) - y
    return low, high


def fingerprint(samples: np.ndarray, sr: int) -> dict[str, Any]:
    if samples.size == 0:
        return {
            "peak_db": -120.0,
            "rms_db": -120.0,
            "crest_db": 0.0,
            "activity_ratio": 0.0,
            "duration_sec": 0.0,
            "sample_rate": sr,
            "has_signal": False,
            "bands": {},
        }
    x = samples.astype(np.float64)
    peak = float(np.max(np.abs(x)))
    rms = float(np.sqrt(np.mean(x * x)))
    peak_db = _db(peak)
    rms_db = _db(rms)
    frame = max(1, sr // 50)
    frames = 0
    active = 0
    i = 0
    while i + frame <= x.size:
        e = float(np.sqrt(np.mean(x[i : i + frame] ** 2)))
        if e > 0.008:
            active += 1
        frames += 1
        i += frame
    activity = active / frames if frames else 0.0

    names = ["sub", "low", "lowmid", "mid", "himid", "high", "air"]
    cuts = [80.0, 200.0, 500.0, 2000.0, 5000.0, 10000.0, sr / 2.0]
    residual = x.astype(np.float32)
    energies: list[float] = []
    for b, cut in enumerate(cuts):
        low, high = _one_pole_split(residual, cut, sr)
        band = residual if b == len(names) - 1 else low
        energies.append(float(np.sum(band.astype(np.float64) ** 2)))
        residual = high
    total = max(sum(energies), 1e-12)
    bands = {n: round(e / total, 4) for n, e in zip(names, energies)}
    return {
        "peak_db": round(peak_db, 2),
        "rms_db": round(rms_db, 2),
        "crest_db": round(peak_db - rms_db, 2),
        "activity_ratio": round(activity, 3),
        "duration_sec": round(samples.size / sr, 2),
        "sample_rate": sr,
        "has_signal": peak_db > PEAK_DB_MIN and activity > ACTIVITY_MIN,
        "bands": bands,
    }


# --- loopback --------------------------------------------------------------


def _device_score(name: str) -> int:
    n = name.lower()
    if any(bad in n for bad in ("nvidia", "hdmi", "display", "mnn")):
        return 0
    if "realtek" in n and "speaker" in n:
        return 50
    if "realtek" in n:
        return 40
    if "stereo mix" in n:
        return 30
    if "speaker" in n:
        return 20
    return 10


def _resample_mono(samples: np.ndarray, src_sr: int, dst_sr: int) -> np.ndarray:
    if src_sr == dst_sr or samples.size == 0:
        return samples.astype(np.float32)
    n_dst = max(1, int(round(samples.size * dst_sr / src_sr)))
    x = np.linspace(0.0, 1.0, samples.size, endpoint=False)
    xi = np.linspace(0.0, 1.0, n_dst, endpoint=False)
    return np.interp(xi, x, samples.astype(np.float64)).astype(np.float32)


def _record_device(seconds: float, sr: int, device: int, loopback: bool) -> np.ndarray:
    import sounddevice as sd

    info = sd.query_devices(device)
    native = int(info.get("default_samplerate") or 48000)
    ch = 2 if loopback else min(2, int(info.get("max_input_channels") or 1) or 1)
    if loopback:
        ch = min(2, int(info.get("max_output_channels") or 2) or 2)
    extra = sd.WasapiSettings(loopback=True) if loopback else None
    frames = max(1, int(seconds * native))
    rec = sd.rec(
        frames,
        samplerate=native,
        channels=ch,
        dtype="float32",
        device=device,
        extra_settings=extra,
        blocking=True,
    )
    mono = rec.mean(axis=1) if rec.ndim == 2 else rec.reshape(-1)
    return _resample_mono(mono, native, sr)


def _record_soundcard(seconds: float, sr: int) -> tuple[np.ndarray, str]:
    import os

    import soundcard as sc

    override = os.environ.get("SPOTIFY_PC_DEVICE", "").strip().lower()
    speakers = list(sc.all_speakers())
    if override:
        speakers = [s for s in speakers if override in s.name.lower()] + speakers
    else:
        try:
            speakers = [sc.default_speaker()] + [s for s in speakers if s.name != sc.default_speaker().name]
        except Exception:
            pass
    last_err: Exception | None = None
    silent: list[str] = []
    native = 48000
    frames = max(1, int(seconds * native))
    for spk in speakers:
        try:
            mic = sc.get_microphone(id=spk.id, include_loopback=True)
            rec = mic.record(numframes=frames, samplerate=native)
        except Exception as exc:
            last_err = exc
            logging.warning("soundcard %s failed: %s", spk.name, exc)
            continue
        mono = rec.mean(axis=1) if getattr(rec, "ndim", 1) == 2 else np.asarray(rec).reshape(-1)
        peak = float(np.max(np.abs(mono))) if mono.size else 0.0
        if peak < 0.004:
            silent.append(f"{spk.name} peak={peak:.5f}")
            logging.info("soundcard %s silent (peak=%.5f)", spk.name, peak)
            continue
        logging.info("using soundcard loopback %s (peak=%.3f)", spk.name, peak)
        return _resample_mono(mono, native, sr), f"wasapi_loopback:{spk.name}"
    if silent:
        raise RuntimeError("soundcard loopbacks silent: " + "; ".join(silent))
    if last_err:
        raise last_err
    raise RuntimeError("no soundcard loopback device")


def record_loopback(seconds: float, sr: int = SAMPLE_RATE) -> tuple[np.ndarray, str]:
    try:
        return _record_soundcard(seconds, sr)
    except Exception as exc:
        logging.warning("soundcard loopback failed (%s); trying sounddevice", exc)
    return _record_sounddevice(seconds, sr)


def _record_sounddevice(seconds: float, sr: int) -> tuple[np.ndarray, str]:
    import os

    import sounddevice as sd

    override = os.environ.get("SPOTIFY_PC_DEVICE", "").strip()
    candidates: list[tuple[int, bool, str, int]] = []
    for i, d in enumerate(sd.query_devices()):
        name = str(d.get("name", ""))
        host = str(sd.query_hostapis(d["hostapi"]).get("name", ""))
        wasapi = "WASAPI" in host
        if override and override.lower() in name.lower():
            lb = wasapi and d.get("max_output_channels", 0) > 0
            candidates.append((i, lb, name, 100))
            continue
        if wasapi and d.get("max_output_channels", 0) > 0:
            candidates.append((i, True, name, _device_score(name)))
        elif "stereo mix" in name.lower() and d.get("max_input_channels", 0) > 0:
            candidates.append((i, False, name, _device_score(name)))
    candidates.sort(key=lambda r: r[3], reverse=True)
    if not candidates:
        raise RuntimeError("no loopback or Stereo Mix device found")

    last_err: Exception | None = None
    silent: list[str] = []
    for idx, loopback, name, score in candidates:
        try:
            samples = _record_device(seconds, sr, idx, loopback)
        except Exception as exc:
            last_err = exc
            logging.warning("device %s failed: %s", name, exc)
            continue
        peak = float(np.max(np.abs(samples))) if samples.size else 0.0
        backend = f"{'wasapi_loopback' if loopback else 'stereo_mix'}:{name}"
        if peak < 0.004:
            silent.append(f"{name} peak={peak:.5f}")
            logging.info("device %s opened but silent (peak=%.5f)", name, peak)
            continue
        logging.info("using %s (peak=%.3f)", backend, peak)
        return samples, backend
    if silent:
        raise RuntimeError("open devices were silent: " + "; ".join(silent))
    if last_err:
        raise last_err
    raise RuntimeError("all capture devices failed")


def write_wav_mono16(path: Path, samples: np.ndarray, sr: int) -> None:
    clipped = np.clip(samples, -1.0, 1.0)
    pcm = (clipped * 32767.0).astype(np.int16)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


def media_volume_percent() -> int:
    try:
        from ctypes import POINTER, cast

        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        level = float(volume.GetMasterVolumeLevelScalar())
        return int(round(level * 100))
    except Exception:
        return -1


# --- persist ---------------------------------------------------------------


def append_listen(entry: dict[str, Any]) -> None:
    log = TASTE / "listen_log.jsonl"
    TASTE.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def save_clip(samples: np.ndarray, sr: int, track: dict[str, Any], backend: str) -> dict[str, Any] | None:
    fp = fingerprint(samples, sr)
    if not fp["has_signal"]:
        logging.info("silent clip skipped (%s — %s)", track.get("artist"), track.get("title"))
        return None

    duration = int(round(fp["duration_sec"]))
    stamp = _stamp()
    day = datetime.now(timezone.utc).strftime("%Y/%m")
    rel = Path("clips") / day / f"clip_{stamp}_{duration}s.wav"
    wav_path = TASTE / rel
    write_wav_mono16(wav_path, samples, sr)
    if wav_path.stat().st_size > MAX_WAV_BYTES:
        logging.warning("wav %s too large (%s) — keeping listen only", wav_path.name, wav_path.stat().st_size)

    vol = media_volume_percent()
    meta = {
        "pc_volume_percent": vol,
        "stream": "WASAPI_loopback",
        "audio_file": wav_path.name,
        "backend": backend,
        "host": "pc",
    }
    meta_rel = rel.with_suffix(".meta.json")
    (TASTE / meta_rel).write_text(json.dumps(meta) + "\n", encoding="utf-8")

    entry = {
        "id": f"{stamp}-{secrets.token_hex(4)}",
        "ts": _utc(),
        "artist": (track.get("artist") or "").strip(),
        "title": (track.get("title") or "").strip(),
        "source": "spotify_pc",
        "url": None,
        "rating": "unrated",
        "tags": ["spotify", "auto-clip", "pc", "wasapi"],
        "notes": (
            f"album={track.get('album') or ''}; clip={duration}s; "
            f"backend={backend}; pc_volume_percent={vol}"
        ),
        "mood": None,
        "genre_hint": None,
        "fingerprint": fp,
        "audio_path": f"song-creation-pipeline-github-agent/taste_data/{rel.as_posix()}",
        "phone_volume_percent": vol,
        "volume_meta_path": f"song-creation-pipeline-github-agent/taste_data/{meta_rel.as_posix()}",
        "capture_backend": backend,
        "package": (track.get("app") or "spotify.web"),
        "host": "pc",
    }
    append_listen(entry)
    logging.info(
        "saved %s / %s  %ss  peak=%s  %s",
        entry["artist"],
        entry["title"],
        duration,
        fp["peak_db"],
        wav_path.name,
    )
    return entry


# --- loop ------------------------------------------------------------------


def tick_once() -> str:
    track = now_playing()
    if not track:
        if _spotify_process_running():
            return "spotify_idle"
        return "spotify_idle"
    seconds = MIN_SEC + random.randint(0, MAX_SEC - MIN_SEC)
    logging.info("capturing %ss · %s — %s", seconds, track.get("artist"), track.get("title"))
    samples, backend = record_loopback(seconds)
    saved = save_clip(samples, SAMPLE_RATE, track, backend)
    return "saved" if saved else "silent"


def run_loop() -> int:
    logging.info("Spotify PC capture started (WASAPI loopback)")
    logging.info("taste dir %s", TASTE)
    while True:
        try:
            status = tick_once()
        except KeyboardInterrupt:
            logging.info("stopped")
            return 0
        except Exception:
            logging.exception("tick failed")
            status = "error"
        if status == "saved":
            gap = GAP_MIN + random.randint(0, GAP_MAX - GAP_MIN)
        elif status == "silent":
            gap = GAP_MIN
        elif status == "error":
            gap = 8
        else:
            gap = 5
        logging.debug("status=%s sleep=%ss", status, gap)
        time.sleep(gap)


def cmd_status() -> int:
    running = _spotify_process_running()
    track = now_playing()
    print(
        json.dumps(
            {
                "spotify_process": running,
                "browser_ok": True,
                "now_playing": track,
                "sessions": _smtc_sessions(),
                "taste_dir": str(TASTE),
                "log": str(LOG_PATH),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


def cmd_once() -> int:
    status = tick_once()
    print(json.dumps({"status": status}, indent=2))
    return 0 if status in {"saved", "silent", "spotify_idle", "spotify_not_running"} else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="PC Spotify loopback clips → taste_data")
    p.add_argument("cmd", nargs="?", default="loop", choices=["loop", "once", "status"])
    p.add_argument("-v", "--verbose", action="store_true")
    a = p.parse_args(argv)
    setup_log(a.verbose)
    if a.cmd == "status":
        return cmd_status()
    if a.cmd == "once":
        return cmd_once()
    return run_loop()


if __name__ == "__main__":
    raise SystemExit(main())
