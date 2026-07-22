#!/usr/bin/env python3
"""Smoke-test every CLI knowledge package in the Music-producer monorepo."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (folder, module, args for a cheap "info-like" call)
AGENTS: list[tuple[str, str, list[str]]] = [
    ("producers-genre-guide-github-agent", "producers_kb", ["info"]),
    ("genre-mixing-github-agent", "genre_mix_kb", ["info"]),
    ("matriarch-github-agent", "matriarch_kb", ["info"]),
    ("monologue-github-agent", "monologue_kb", ["info"]),
    ("tr8s-github-agent", "tr8s_kb", ["info"]),
    ("movement-github-agent", "movement_kb", ["info"]),
    ("studiolive-github-agent", "studiolive_kb", ["info"]),
    ("music-theory-advanced-github-agent", "theory_kb", ["info"]),
    ("schoenberg-github-agent", "schoenberg_kb", ["info"]),
    ("msp-techniques-github-agent", "msp_kb", ["info"]),
    ("dsp-wiley-github-agent", "dsp_kb", ["info"]),
]

STUDIO_ONE = ROOT / "studio-one-6.6-agent-knowledge"


def run_cli(folder: str, module: str, args: list[str]) -> tuple[bool, str]:
    cwd = ROOT / folder
    if not cwd.is_dir():
        return False, f"missing folder: {folder}"
    try:
        proc = subprocess.run(
            [sys.executable, "-m", module, *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()
        return False, err[:500] or f"exit {proc.returncode}"
    out = (proc.stdout or "").strip()
    return True, out[:200].replace("\n", " ")


def check_studio_one() -> tuple[bool, str]:
    if not STUDIO_ONE.is_dir():
        return False, "missing studio-one-6.6-agent-knowledge"
    required = [
        STUDIO_ONE / "AGENTS.md",
        STUDIO_ONE / "INDEX.md",
        STUDIO_ONE / "manifest.json",
        STUDIO_ONE / "chapters",
    ]
    missing = [str(p.name) for p in required if not p.exists()]
    if missing:
        return False, f"missing: {', '.join(missing)}"
    chapters = list((STUDIO_ONE / "chapters").glob("*.md"))
    if len(chapters) < 5:
        return False, f"too few chapters: {len(chapters)}"
    try:
        manifest = json.loads((STUDIO_ONE / "manifest.json").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return False, f"manifest.json: {exc}"
    n = len(manifest) if isinstance(manifest, list) else len(manifest.keys())
    return True, f"chapters={len(chapters)} manifest_entries={n}"


def main() -> int:
    print(f"Music-producer verify — root: {ROOT}\n")
    failed = 0

    ok, msg = check_studio_one()
    status = "OK " if ok else "FAIL"
    print(f"[{status}] studio-one-6.6-agent-knowledge  {msg}")
    if not ok:
        failed += 1

    for folder, module, args in AGENTS:
        ok, msg = run_cli(folder, module, args)
        status = "OK " if ok else "FAIL"
        print(f"[{status}] {folder}  ({module} {' '.join(args)})  {msg}")
        if not ok:
            failed += 1

    print()
    if failed:
        print(f"FAILED: {failed} check(s)")
        return 1
    print(f"All {1 + len(AGENTS)} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
