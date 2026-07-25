"""
Plan Studio One *execution jobs* from production phase decisions.

Music-producer = brain (what/when/gates).
Studio-One = hands (execute_job.py runs the JSON only).

Job schema must stay compatible with Studio-One tools/s1_tools/job_schema.py.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from song_pipeline_kb.pipeline import get_phase
from song_pipeline_kb.song_state import (
    GATE_HELP,
    init_song,
    is_locked,
    load_gates,
    require_gates,
    summary,
    append_notes,
)

JOB_VERSION = 1


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def job_path(song_dir: Path) -> Path:
    return Path(song_dir) / "s1_jobs" / "current.json"


def result_path(song_dir: Path) -> Path:
    return Path(song_dir) / "s1_jobs" / "last_result.json"


def write_job(song_dir: Path, job: Dict[str, Any]) -> Path:
    path = job_path(song_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(job, indent=2), encoding="utf-8")
    return path


def load_last_result(song_dir: Path) -> Optional[Dict[str, Any]]:
    p = result_path(song_dir)
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _base_job(
    song_dir: Path,
    *,
    job_id: str,
    notes: str,
    steps: List[Dict[str, Any]],
    options: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return {
        "version": JOB_VERSION,
        "id": job_id,
        "source": "music-producer",
        "song_dir": str(Path(song_dir).resolve()),
        "created_at": _utc(),
        "notes": notes,
        "options": options
        or {
            "user_armed": False,
            "no_prompt": False,
            "no_eyes": False,
            "max_sec": None,
            "save_after": True,
        },
        "steps": steps,
    }


def plan_mvp(
    song_dir: Path,
    *,
    create_tracks: bool = True,
    track_count: int = 2,
    drums_track: int = 1,
    bass_track: int = 2,
    drums_midi: str = "MIDI/drums.mid",
    bass_midi: str = "MIDI/bass.mid",
    browser_loads: Optional[List[str]] = None,
    skip_brief_gate: bool = False,
    max_sec: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Production choice: run MVP capture (drums + bass) in Studio One, then stop
    for pocket approval (producer gate — not S1 logic).
    """
    song = Path(song_dir)
    init_song(song)

    blocked = [] if skip_brief_gate else require_gates(song, ["brief"])
    phase = get_phase("mvp")

    if blocked:
        return {
            "ok": False,
            "error": "gates_blocked",
            "missing_gates": blocked,
            "hint": "Lock brief first: python -m song_pipeline_kb gate brief locked",
            "phase": phase,
        }

    # MIDI presence is a producer responsibility before issuing the job
    missing = []
    for rel in (drums_midi, bass_midi):
        p = song / rel
        if not p.is_file() and not (song / "MIDI" / Path(rel).name).is_file():
            missing.append(rel)
    if missing:
        return {
            "ok": False,
            "error": "midi_missing",
            "missing_midi": missing,
            "hint": "Place MIDI under song/MIDI/ then re-run plan mvp",
            "phase": phase,
        }

    steps: List[Dict[str, Any]] = [
        {"op": "check_setup"},
        {"op": "ensure_workspace"},
    ]
    if create_tracks:
        steps.append({"op": "create_tracks", "count": track_count})
    for name in browser_loads or []:
        steps.append({"op": "browser_load", "name": name, "optional": True})

    steps.append(
        {
            "op": "stream_record",
            "midi": drums_midi,
            "track": drums_track,
            "label": "DRUMS",
        }
    )
    steps.append(
        {
            "op": "stream_record",
            "midi": bass_midi,
            "track": bass_track,
            "label": "BASS",
        }
    )
    steps.append({"op": "save"})
    steps.append(
        {
            "op": "report",
            "message": (
                "MVP stream attempted. Producer: verify eyes + clips, "
                "then lock pocket gate only after USER approves."
            ),
        }
    )

    opts: Dict[str, Any] = {
        "user_armed": False,
        "no_prompt": False,
        "no_eyes": False,
        "max_sec": max_sec,
        "save_after": True,
    }
    job = _base_job(
        song,
        job_id=f"mvp-{_utc().replace(':', '')}",
        notes="MVP drums+bass capture; stop for pocket approval",
        steps=steps,
        options=opts,
    )
    path = write_job(song, job)
    append_notes(song, f"Planned S1 job {job['id']} → {path.name}")
    return {
        "ok": True,
        "job_path": str(path),
        "job": job,
        "phase": phase,
        "next_producer_step": (
            "Run Studio-One: py -3.12 tools/execute_job.py --song-dir <song>. "
            "After success + user pocket OK: gate pocket locked"
        ),
        "execute_hint": f'py -3.12 tools/execute_job.py --song-dir "{song}"',
    }


def plan_stream_part(
    song_dir: Path,
    *,
    part: str,
    track: int,
    midi: Optional[str] = None,
    require_pocket: bool = True,
) -> Dict[str, Any]:
    """Plan a single-part stream (lead/bed/color) after pocket lock."""
    song = Path(song_dir)
    init_song(song)
    part = part.lower().strip()
    midi = midi or f"MIDI/{part}.mid"

    needed = ["pocket"] if require_pocket else []
    if part == "lead":
        phase_key = "lead"
    elif part == "bed":
        phase_key = "bed"
        needed = ["pocket", "lead"]
    elif part in ("color", "fx"):
        phase_key = "color"
        needed = ["pocket"]
    else:
        phase_key = part

    blocked = require_gates(song, needed) if needed else []
    phase = get_phase(phase_key)
    if blocked:
        return {
            "ok": False,
            "error": "gates_blocked",
            "missing_gates": blocked,
            "phase": phase,
        }

    p = song / midi
    if not p.is_file() and not (song / "MIDI" / Path(midi).name).is_file():
        return {"ok": False, "error": "midi_missing", "missing_midi": [midi], "phase": phase}

    steps = [
        {"op": "check_setup"},
        {"op": "ensure_workspace"},
        {
            "op": "stream_record",
            "midi": midi,
            "track": track,
            "label": part.upper(),
        },
        {"op": "save"},
        {
            "op": "report",
            "message": f"{part} stream attempted. Producer: user gate for {part} after listen.",
        },
    ]
    job = _base_job(
        song,
        job_id=f"{part}-{_utc().replace(':', '')}",
        notes=f"Stream {part} to track {track}",
        steps=steps,
    )
    path = write_job(song, job)
    append_notes(song, f"Planned S1 job {job['id']} for part={part}")
    return {
        "ok": True,
        "job_path": str(path),
        "job": job,
        "phase": phase,
        "execute_hint": f'py -3.12 tools/execute_job.py --song-dir "{song}"',
    }


def next_action(song_dir: Path) -> Dict[str, Any]:
    """
    Production router: what should the producer do next?
    Does not execute Studio One — only recommends + can emit job plans.
    """
    song = Path(song_dir)
    init_song(song)
    gates = load_gates(song)
    inv = summary(song)
    last = load_last_result(song)

    def phase_blob(key: str) -> Dict[str, Any]:
        return get_phase(key)

    if gates.get("final") == "locked":
        return {
            "status": "final_locked",
            "action": "stop",
            "message": "FINAL lock set — no rework unless user reopens",
            "gates": gates,
            "phase": phase_blob("final"),
        }

    if gates.get("brief") != "locked":
        return {
            "status": "need_brief",
            "action": "lock_brief",
            "message": (
                "Confirm reference (or waive) + mood lock, then: "
                "python -m song_pipeline_kb gate brief locked"
            ),
            "gates": gates,
            "phase": phase_blob("brief"),
            "gate_help": GATE_HELP["brief"],
        }

    if gates.get("pocket") != "locked":
        midi = inv.get("midi") or {}
        if not (midi.get("drums.mid") and midi.get("bass.mid")):
            return {
                "status": "need_mvp_midi",
                "action": "compose_mvp_midi",
                "message": "Add MIDI/drums.mid and MIDI/bass.mid, then plan mvp",
                "gates": gates,
                "phase": phase_blob("mvp"),
                "midi": midi,
            }
        # Ignore dry-run results — they are not real captures
        real_last = None
        if last and not last.get("dry_run"):
            real_last = last
        if (
            real_last
            and real_last.get("ok")
            and str(real_last.get("job_id", "")).startswith("mvp")
        ):
            return {
                "status": "awaiting_pocket_approval",
                "action": "user_listen",
                "message": (
                    "Last MVP job ok. User listens for pocket (use observe for cues). "
                    "If approved: python -m song_pipeline_kb gate pocket locked"
                ),
                "gates": gates,
                "phase": phase_blob("mvp"),
                "last_result": real_last,
            }
        if inv.get("has_current_job") and (
            not real_last
            or not real_last.get("ok")
            or not str(real_last.get("job_id", "")).startswith("mvp")
        ):
            return {
                "status": "ready_execute_mvp",
                "action": "execute_job",
                "message": (
                    "Job planned. Run Studio-One: "
                    f'py -3.12 tools/execute_job.py --song-dir "{song}" '
                    "then: python -m song_pipeline_kb observe --song-dir <song>"
                ),
                "gates": gates,
                "phase": phase_blob("mvp"),
                "execute_hint": f'py -3.12 tools/execute_job.py --song-dir "{song}"',
                "last_result": real_last,
            }
        return {
            "status": "ready_plan_mvp",
            "action": "plan_mvp",
            "message": "Run: python -m song_pipeline_kb plan mvp --song-dir <song>",
            "gates": gates,
            "phase": phase_blob("mvp"),
            "command": "plan mvp",
        }

    # After pocket: one part at a time
    if gates.get("lead") != "locked":
        return {
            "status": "need_lead",
            "action": "plan_lead_or_compose",
            "message": "Pocket locked. Compose lead MIDI then plan stream lead --track 3",
            "gates": gates,
            "phase": phase_blob("lead"),
        }
    if gates.get("bed") != "locked":
        return {
            "status": "need_bed",
            "action": "plan_bed_or_skip",
            "message": "Lead locked. Plan bed stream or gate bed skipped",
            "gates": gates,
            "phase": phase_blob("bed"),
        }
    if gates.get("mix") != "locked":
        return {
            "status": "need_mix",
            "action": "mix_guidance",
            "message": "Parts far enough — follow full_mix phase (S1 mix is mostly manual/MCU)",
            "gates": gates,
            "phase": phase_blob("full_mix"),
        }

    return {
        "status": "advanced",
        "action": "see_phase",
        "message": "Use phases/gates CLI for mix/qc/late_form/final",
        "gates": gates,
        "inventory": inv,
        "last_result": last,
    }
