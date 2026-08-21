#!/usr/bin/env python3
"""Download free singing datasets: VocalSet (Zenodo) + GTSinger (Hugging Face).

Default: VocalSet full zip + GTSinger English only (~11 GB total).
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
VOCALSET_DIR = RAW / "vocalset"
GTSINGER_DIR = RAW / "gtsinger"

VOCALSET_URL = "https://zenodo.org/api/records/1193957/files/VocalSet.zip/content"
VOCALSET_ZIP = VOCALSET_DIR / "VocalSet.zip"
# Zenodo file size from API (bytes)
VOCALSET_EXPECTED_SIZE = 2_077_087_366

GTSINGER_REPO = "AaronZ345/GTSinger"


def _progress(done: int, total: int | None, label: str) -> None:
    if total and total > 0:
        pct = 100.0 * done / total
        mb = done / 1e6
        tm = total / 1e6
        print(f"\r{label}: {mb:.1f}/{tm:.1f} MB ({pct:.1f}%)", end="", flush=True)
    else:
        print(f"\r{label}: {done / 1e6:.1f} MB", end="", flush=True)


def download_url(url: str, dest: Path, expected_size: int | None = None) -> Path:
    import urllib.request

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and expected_size and dest.stat().st_size == expected_size:
        print(f"Already complete: {dest} ({dest.stat().st_size} bytes)")
        return dest
    if dest.exists() and expected_size and dest.stat().st_size > 0:
        print(f"Partial/mismatch size {dest.stat().st_size} (want {expected_size}); re-downloading")
        dest.unlink()

    tmp = dest.with_suffix(dest.suffix + ".part")
    if tmp.exists():
        # resume not implemented for simplicity; restart
        tmp.unlink()

    print(f"Downloading {url}")
    print(f"  -> {dest}")

    req = urllib.request.Request(url, headers={"User-Agent": "singing-dataset-downloader/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        total = resp.headers.get("Content-Length")
        total_i = int(total) if total else expected_size
        done = 0
        with open(tmp, "wb") as f:
            while True:
                chunk = resp.read(1024 * 1024)
                if not chunk:
                    break
                f.write(chunk)
                done += len(chunk)
                if done % (8 * 1024 * 1024) < 1024 * 1024:
                    _progress(done, total_i, "VocalSet")
    print()
    tmp.replace(dest)
    print(f"Saved {dest} ({dest.stat().st_size} bytes)")
    return dest


def extract_vocalset(zip_path: Path) -> None:
    marker = VOCALSET_DIR / ".extracted_ok"
    if marker.exists():
        print(f"VocalSet already extracted ({marker})")
        return
    print(f"Extracting {zip_path} ...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(VOCALSET_DIR)
    marker.write_text("ok\n", encoding="utf-8")
    print(f"Extracted under {VOCALSET_DIR}")


def download_vocalset() -> None:
    VOCALSET_DIR.mkdir(parents=True, exist_ok=True)
    download_url(VOCALSET_URL, VOCALSET_ZIP, VOCALSET_EXPECTED_SIZE)
    extract_vocalset(VOCALSET_ZIP)
    (VOCALSET_DIR / "LICENSE.txt").write_text(
        "VocalSet: A Singing Voice Dataset\n"
        "License: Creative Commons Attribution 4.0 International (CC BY 4.0)\n"
        "Source: https://zenodo.org/records/1193957\n"
        "Cite Wilkins et al., ISMIR 2018.\n",
        encoding="utf-8",
    )


def download_gtsinger(english_only: bool = True) -> None:
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub", "-q"])
        from huggingface_hub import snapshot_download

    GTSINGER_DIR.mkdir(parents=True, exist_ok=True)
    allow = None
    if english_only:
        allow = [
            "English/**",
            "processed/English/**",
            "README.md",
            "dataset_license.md",
            ".gitattributes",
        ]
        print("Downloading GTSinger English subset (~8.7 GB audio + labels)...")
    else:
        print("Downloading FULL GTSinger (all languages — very large)...")

    # Keep workers low to reduce anonymous HF 429 rate limits (raise if HF_TOKEN set).
    import os

    workers = 8 if os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") else 2
    path = snapshot_download(
        repo_id=GTSINGER_REPO,
        repo_type="dataset",
        local_dir=str(GTSINGER_DIR),
        allow_patterns=allow,
        max_workers=workers,
    )
    print(f"GTSinger at {path}")
    lic = GTSINGER_DIR / "LICENSE_NOTE.txt"
    if not lic.exists():
        lic.write_text(
            "GTSinger — CC BY-NC-SA 4.0 (non-commercial, share-alike).\n"
            "Source: https://huggingface.co/datasets/AaronZ345/GTSinger\n"
            "https://github.com/AaronZ345/GTSinger\n"
            "Using this data means you accept their dataset_license.md terms.\n",
            encoding="utf-8",
        )


def main() -> int:
    p = argparse.ArgumentParser(description="Download singing training datasets")
    p.add_argument("--vocalset-only", action="store_true")
    p.add_argument("--gtsinger-only", action="store_true")
    p.add_argument(
        "--all-gtsinger",
        action="store_true",
        help="Download all GTSinger languages (default is English only)",
    )
    args = p.parse_args()

    do_vs = not args.gtsinger_only
    do_gt = not args.vocalset_only
    if args.vocalset_only:
        do_gt = False
    if args.gtsinger_only:
        do_vs = False

    RAW.mkdir(parents=True, exist_ok=True)
    print(f"Root: {ROOT}")

    if do_vs:
        download_vocalset()
    if do_gt:
        download_gtsinger(english_only=not args.all_gtsinger)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
