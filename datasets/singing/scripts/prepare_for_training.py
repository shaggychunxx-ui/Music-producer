#!/usr/bin/env python3
"""Prepare raw singing corpora for RVC-style or DiffSinger-style training.

RVC: copy/export mono WAVs under prepared/rvc/<source>/, optional silence trim + resample.
DiffSinger: write a CSV manifest (path, duration_sec, source, relative_path).

Does not invent phoneme/MIDI labels — only collects audio for clone / further labeling.
"""
from __future__ import annotations

import argparse
import csv
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
PREP = ROOT / "prepared"

VOCALSET_ROOT = RAW / "vocalset"
GTSINGER_EN = RAW / "gtsinger" / "English"


def _need_audio_libs():
    try:
        import numpy  # noqa: F401
        import soundfile  # noqa: F401
    except ImportError:
        import subprocess

        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "numpy", "soundfile", "-q"]
        )


def _is_real_wav(p: Path) -> bool:
    name = p.name
    if name.startswith("._"):
        return False
    if "__MACOSX" in p.parts:
        return False
    return p.suffix.lower() == ".wav"


def find_wavs(source: str) -> list[Path]:
    if source == "vocalset":
        if not VOCALSET_ROOT.exists():
            return []
        wavs = [p for p in VOCALSET_ROOT.rglob("*.wav") if _is_real_wav(p)]
        wavs += [p for p in VOCALSET_ROOT.rglob("*.WAV") if _is_real_wav(p)]
        return sorted(set(wavs))
    if source == "gtsinger-en":
        if not GTSINGER_EN.exists():
            return []
        # Prefer singing groups over paired speech for primary RVC set
        wavs = []
        for p in GTSINGER_EN.rglob("*.wav"):
            if not _is_real_wav(p):
                continue
            if "Paired_Speech" in p.parts:
                continue
            wavs.append(p)
        return sorted(wavs)
    if source == "all":
        return find_wavs("vocalset") + find_wavs("gtsinger-en")
    raise ValueError(f"Unknown source: {source}")


def duration_sec(path: Path) -> float:
    import soundfile as sf

    try:
        info = sf.info(str(path))
        return float(info.frames) / float(info.samplerate) if info.samplerate else 0.0
    except Exception:
        return 0.0


def load_mono(path: Path, target_sr: int | None):
    import numpy as np
    import soundfile as sf

    data, sr = sf.read(str(path), always_2d=True)
    mono = data.mean(axis=1).astype(np.float32)
    if target_sr and sr != target_sr:
        # linear resample (good enough for prep; use librosa/soxr later if needed)
        n_out = int(round(len(mono) * target_sr / sr))
        if n_out > 1 and len(mono) > 1:
            x_old = np.linspace(0.0, 1.0, num=len(mono), endpoint=False)
            x_new = np.linspace(0.0, 1.0, num=n_out, endpoint=False)
            mono = np.interp(x_new, x_old, mono).astype(np.float32)
            sr = target_sr
    return mono, sr


def trim_silence(mono, sr: int, thresh_db: float = -40.0, pad_ms: int = 50):
    import numpy as np

    if mono.size == 0:
        return mono
    thr = 10 ** (thresh_db / 20.0)
    mask = np.abs(mono) > thr
    if not mask.any():
        return mono
    idx = np.where(mask)[0]
    pad = int(sr * pad_ms / 1000)
    start = max(0, int(idx[0]) - pad)
    end = min(len(mono), int(idx[-1]) + pad + 1)
    return mono[start:end]


def safe_name(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    return str(rel).replace("\\", "__").replace("/", "__").replace(" ", "_")


def prepare_rvc(
    source: str,
    *,
    sample_rate: int,
    trim: bool,
    max_files: int | None,
    min_sec: float,
    copy_only: bool,
) -> None:
    _need_audio_libs()
    import soundfile as sf

    out_dir = PREP / "rvc" / source.replace("-", "_")
    out_dir.mkdir(parents=True, exist_ok=True)

    wavs = find_wavs(source)
    if not wavs:
        print(f"No WAVs found for source={source}. Run download_datasets.py first.")
        return

    if max_files:
        wavs = wavs[:max_files]

    roots = {
        "vocalset": VOCALSET_ROOT,
        "gtsinger-en": GTSINGER_EN,
    }
    # for "all", name from parent marker
    total_sec = 0.0
    n_ok = 0
    n_skip = 0

    for i, wav in enumerate(wavs, 1):
        if source == "all":
            if VOCALSET_ROOT in wav.parents or str(wav).startswith(str(VOCALSET_ROOT)):
                root = VOCALSET_ROOT
                tag = "vs"
            else:
                root = GTSINGER_EN
                tag = "gt"
            name = f"{tag}__{safe_name(wav, root)}"
        else:
            root = roots[source]
            # VocalSet zip may nest under VocalSet11/ etc.
            try:
                name = safe_name(wav, root)
            except ValueError:
                name = safe_name(wav, wav.parents[min(3, len(wav.parts) - 1)])
            tag = source

        out = out_dir / name
        if not out.suffix.lower() == ".wav":
            out = out.with_suffix(".wav")

        try:
            if copy_only and not trim and sample_rate <= 0:
                if not out.exists():
                    shutil.copy2(wav, out)
                dur = duration_sec(out if out.exists() else wav)
            else:
                sr_target = sample_rate if sample_rate > 0 else None
                mono, sr = load_mono(wav, sr_target)
                if trim:
                    mono = trim_silence(mono, sr)
                dur = len(mono) / float(sr) if sr else 0.0
                if dur < min_sec:
                    n_skip += 1
                    continue
                sf.write(str(out), mono, sr, subtype="PCM_16")

            total_sec += dur
            n_ok += 1
            if i % 50 == 0 or i == len(wavs):
                print(f"[{i}/{len(wavs)}] ok={n_ok} skip={n_skip} hours={total_sec/3600:.2f}")
        except Exception as e:
            n_skip += 1
            print(f"skip {wav}: {e}")

    summary = out_dir / "SUMMARY.txt"
    summary.write_text(
        f"source={source}\nfiles={n_ok}\nskipped={n_skip}\n"
        f"total_sec={total_sec:.1f}\ntotal_hours={total_sec/3600:.3f}\n"
        f"sample_rate={sample_rate}\ntrim={trim}\n",
        encoding="utf-8",
    )
    print(f"RVC prep done -> {out_dir}")
    print(f"  {n_ok} files, {total_sec/3600:.2f} h (skipped {n_skip})")


def prepare_diffsinger(source: str, max_files: int | None, min_sec: float) -> None:
    _need_audio_libs()
    out_dir = PREP / "diffsinger"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / f"manifest_{source.replace('-', '_')}.csv"

    wavs = find_wavs(source)
    if not wavs:
        print(f"No WAVs found for source={source}. Run download_datasets.py first.")
        return
    if max_files:
        wavs = wavs[:max_files]

    rows = []
    total = 0.0
    for wav in wavs:
        d = duration_sec(wav)
        if d < min_sec:
            continue
        rows.append(
            {
                "path": str(wav.resolve()),
                "duration_sec": f"{d:.3f}",
                "source": source,
                "name": wav.name,
            }
        )
        total += d

    with open(manifest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["path", "duration_sec", "source", "name"])
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {manifest} ({len(rows)} clips, {total/3600:.2f} h)")
    print("Note: phoneme/MIDI labels must come from GTSinger TextGrid/json or your own aligner.")


def main() -> int:
    p = argparse.ArgumentParser(description="Prepare singing data for training")
    p.add_argument("--format", choices=["rvc", "diffsinger"], required=True)
    p.add_argument(
        "--source",
        choices=["vocalset", "gtsinger-en", "all"],
        default="all",
    )
    p.add_argument("--sample-rate", type=int, default=40000, help="RVC target SR (0=keep original)")
    p.add_argument("--no-trim", action="store_true", help="Skip silence trim")
    p.add_argument("--copy-only", action="store_true", help="Copy WAVs without re-encode")
    p.add_argument("--max-files", type=int, default=None, help="Limit for smoke tests")
    p.add_argument("--min-sec", type=float, default=0.5, help="Drop clips shorter than this")
    args = p.parse_args()

    print(f"Root: {ROOT}")
    if args.format == "rvc":
        prepare_rvc(
            args.source,
            sample_rate=args.sample_rate,
            trim=not args.no_trim,
            max_files=args.max_files,
            min_sec=args.min_sec,
            copy_only=args.copy_only,
        )
    else:
        prepare_diffsinger(args.source, args.max_files, args.min_sec)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
