"""
Per-song production state: GATES, NOTES, scaffold.

Song-agnostic process lives in pipeline.py; this module only reads/writes
the song folder the producer owns (creative + approval status).

Studio One must not interpret these files for creative policy — it only
executes job JSON produced by plan_job / write_job.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json
import re

from song_pipeline_kb.pipeline import GATES as GATE_DEFS
from song_pipeline_kb.pipeline import SCAFFOLD

# Machine-parseable gate ids used in GATES.txt (map to workflow stops)
GATE_KEYS: List[str] = [
    "brief",
    "pocket",
    "lead",
    "bed",
    "color",
    "mix",
    "qc",
    "late_form",
    "final",
]

GATE_HELP: Dict[str, str] = {
    "brief": "Reference + mood lock confirmed or waived (A)",
    "pocket": "USER approved MVP pocket drums+bass (C2)",
    "lead": "USER approved lead (D1)",
    "bed": "USER approved bed (D2)",
    "color": "USER approved color if used (D3)",
    "mix": "Full mix signal-flow accepted (F)",
    "qc": "QC A/B + mono (H)",
    "late_form": "Late form on locked stems if asked (I)",
    "final": "FINAL LOCK — stop rework (K)",
}

DEFAULT_NOTES = """# Song notes (production — Music-producer)

## Brief
- Reference (title + artist) or WAIVED:
- Mood lock:
- Complexity budget: S
- Target length:
- Taste profile: (optional — python -m song_pipeline_kb taste apply-brief --song-dir .)

## Pocket
- Approved: no

## Parts
- Lead / bed / color:

## Mix
- Local master paths only (never commit audio):

## Log
"""


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def default_gates() -> Dict[str, str]:
    return {k: "open" for k in GATE_KEYS}


def parse_gates(text: str) -> Dict[str, str]:
    out = default_gates()
    for line in text.splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_]+)\s*[=:]\s*(\S+)", raw)
        if not m:
            continue
        key, val = m.group(1).lower(), m.group(2).lower()
        if val in ("yes", "y", "true", "done", "ok", "approved"):
            val = "locked"
        if val in ("no", "n", "false", "todo", "pending"):
            val = "open"
        if val not in ("open", "locked", "skipped"):
            val = "open"
        out[key] = val
    return out


def format_gates(gates: Dict[str, str]) -> str:
    lines = [
        "# GATES — production approvals (Music-producer)",
        "# status: open | locked | skipped",
        "# Lock only after user approval. Studio One does not write these.",
        "",
    ]
    for g in GATE_KEYS:
        lines.append(f"{g}={gates.get(g, 'open')}  # {GATE_HELP.get(g, '')}")
    for k, v in gates.items():
        if k not in GATE_KEYS:
            lines.append(f"{k}={v}")
    lines.append("")
    return "\n".join(lines)


def gates_path(song_dir: Path) -> Path:
    return Path(song_dir) / "GATES.txt"


def notes_path(song_dir: Path) -> Path:
    return Path(song_dir) / "NOTES.txt"


def load_gates(song_dir: Path) -> Dict[str, str]:
    p = gates_path(song_dir)
    if not p.is_file():
        return default_gates()
    return parse_gates(p.read_text(encoding="utf-8", errors="replace"))


def save_gates(song_dir: Path, gates: Dict[str, str]) -> Path:
    p = gates_path(song_dir)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(format_gates(gates), encoding="utf-8")
    return p


def set_gate(song_dir: Path, gate: str, status: str) -> Dict[str, str]:
    gate = gate.lower().strip()
    status = status.lower().strip()
    if status in ("yes", "y", "true", "done", "ok", "approved"):
        status = "locked"
    if status not in ("open", "locked", "skipped"):
        raise ValueError(f"invalid status: {status}")
    gates = load_gates(song_dir)
    gates[gate] = status
    save_gates(song_dir, gates)
    append_notes(song_dir, f"Gate `{gate}` → {status}")
    return gates


def is_locked(song_dir: Path, gate: str) -> bool:
    return load_gates(song_dir).get(gate.lower(), "open") == "locked"


def require_gates(song_dir: Path, needed: List[str]) -> List[str]:
    gates = load_gates(song_dir)
    return [g for g in needed if gates.get(g, "open") != "locked"]


def append_notes(song_dir: Path, line: str) -> None:
    p = notes_path(song_dir)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.is_file():
        p.write_text(DEFAULT_NOTES, encoding="utf-8")
    with p.open("a", encoding="utf-8") as f:
        f.write(f"\n- [{_utc()}] {line}\n")


def init_song(song_dir: Path, *, name: Optional[str] = None) -> Dict[str, Any]:
    """Create producer-owned song docs + dirs for execution handoff."""
    song = Path(song_dir)
    song.mkdir(parents=True, exist_ok=True)

    for d in SCAFFOLD.get("dirs") or []:
        (song / d).mkdir(parents=True, exist_ok=True)
    # Always ensure MIDI + s1_jobs for Studio-One executor
    (song / "MIDI").mkdir(parents=True, exist_ok=True)
    (song / "s1_jobs").mkdir(parents=True, exist_ok=True)
    (song / "_vision" / "arm_watch").mkdir(parents=True, exist_ok=True)

    if not gates_path(song).is_file():
        save_gates(song, default_gates())
    if not notes_path(song).is_file():
        header = DEFAULT_NOTES
        if name:
            header = f"# Song: {name}\n\n" + DEFAULT_NOTES
        notes_path(song).write_text(header, encoding="utf-8")

    # Optional empty scaffold files
    for f in SCAFFOLD.get("files") or []:
        if f in ("GATES.txt", "NOTES.txt"):
            continue
        fp = song / f
        if not fp.is_file():
            fp.write_text(f"# {f}\n", encoding="utf-8")

    return {
        "song_dir": str(song.resolve()),
        "gates": load_gates(song),
        "scaffold_dirs": SCAFFOLD.get("dirs"),
        "gate_defs": GATE_DEFS,
    }


def summary(song_dir: Path) -> Dict[str, Any]:
    song = Path(song_dir)
    midi = song / "MIDI"
    files = {}
    if midi.is_dir():
        for n in ("drums.mid", "bass.mid", "lead.mid", "bed.mid", "color.mid"):
            files[n] = (midi / n).is_file()
    return {
        "song_dir": str(song.resolve()),
        "gates": load_gates(song),
        "midi": files,
        "job_path": str(song / "s1_jobs" / "current.json"),
        "result_path": str(song / "s1_jobs" / "last_result.json"),
        "has_current_job": (song / "s1_jobs" / "current.json").is_file(),
        "has_last_result": (song / "s1_jobs" / "last_result.json").is_file(),
    }
