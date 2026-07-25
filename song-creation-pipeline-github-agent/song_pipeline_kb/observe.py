"""
Observe Studio-One execution results (visual + audio cues) and decide next moves.

Music-producer is the brain: never trusts note_ons alone.
Uses last_result.json written by Studio-One execute_job.py.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from song_pipeline_kb.song_state import (
    append_notes,
    is_locked,
    load_gates,
    set_gate,
    summary,
)
from song_pipeline_kb.s1_jobs import load_last_result, next_action, plan_mvp


def _confidence_from_cues(result: Dict[str, Any]) -> Dict[str, Any]:
    """Score execution evidence without artistic judgment."""
    scores: Dict[str, float] = {}
    notes: List[str] = []

    if not result:
        return {"overall": 0.0, "scores": {}, "notes": ["no_result"]}

    ok = bool(result.get("ok"))
    scores["job_ok"] = 1.0 if ok else 0.0

    vision = result.get("vision") or {}
    if vision.get("any_safety_dialog"):
        notes.append("safety_dialog_was_present — ensure S1 fully started")
    scores["any_rec_red"] = 1.0 if vision.get("any_rec_red") else 0.0
    scores["blue_clip_hint"] = 1.0 if vision.get("blue_clip_hint") else 0.0
    scores["shots"] = min(1.0, (vision.get("shot_count") or 0) / 4.0)

    audio_list = result.get("audio") or []
    signal_hits = sum(1 for a in audio_list if a.get("has_signal"))
    scores["audio_signal"] = min(1.0, signal_hits / max(1, len(audio_list))) if audio_list else 0.0
    if not audio_list:
        notes.append("no_audio_captures")

    stream_steps = [s for s in (result.get("steps") or []) if s.get("op") == "stream_record"]
    notes_ok = 0
    armed_ok = 0
    for s in stream_steps:
        if (s.get("note_ons") or 0) > 0:
            notes_ok += 1
        if s.get("armed_confirmed"):
            armed_ok += 1
        # Per-step audio
        a = s.get("audio") or {}
        if a.get("has_signal"):
            scores["audio_signal"] = max(scores.get("audio_signal", 0.0), 0.8)
    if stream_steps:
        scores["stream_notes"] = notes_ok / len(stream_steps)
        scores["stream_armed"] = armed_ok / len(stream_steps)
    else:
        scores["stream_notes"] = 0.0
        scores["stream_armed"] = 0.0
        if ok:
            notes.append("no_stream_steps")

    # Weighted overall (execution health, not "sounds good")
    weights = {
        "job_ok": 0.25,
        "stream_notes": 0.2,
        "stream_armed": 0.2,
        "any_rec_red": 0.15,
        "audio_signal": 0.15,
        "blue_clip_hint": 0.05,
    }
    overall = sum(scores.get(k, 0.0) * w for k, w in weights.items())
    if not ok:
        overall = min(overall, 0.35)
        notes.append("job_reported_failure")
    if scores.get("audio_signal", 0) < 0.3 and stream_steps:
        notes.append("weak_or_missing_audio — check loopback/levels")
    if scores.get("stream_armed", 0) < 0.5 and stream_steps:
        notes.append("rec_arm not confirmed in screenshots")

    return {
        "overall": round(overall, 3),
        "scores": {k: round(v, 3) for k, v in scores.items()},
        "notes": notes,
        "stream_step_count": len(stream_steps),
    }


def observe(song_dir: Path) -> Dict[str, Any]:
    """Read last_result + gates + inventory; produce decision recommendation."""
    song = Path(song_dir)
    result = load_last_result(song)
    gates = load_gates(song)
    inv = summary(song)
    conf = _confidence_from_cues(result or {})
    nxt = next_action(song)

    recommendation = "continue"
    detail = nxt.get("message") or ""
    auto_gate: Optional[Dict[str, str]] = None

    if not result:
        recommendation = "no_result"
        detail = "No s1_jobs/last_result.json — run Studio-One execute_job.py after plan"
    elif conf["overall"] >= 0.72 and str(result.get("job_id", "")).startswith("mvp"):
        if gates.get("pocket") != "locked":
            recommendation = "user_listen_pocket"
            detail = (
                "MVP execution cues look healthy (vision/audio/notes). "
                "USER should listen for pocket feel. "
                "If approved: gate pocket locked. "
                "Do NOT auto-lock artistic pocket from metrics alone."
            )
            # Soft suggestion only — still user gate
            auto_gate = None
        else:
            recommendation = "next_after_pocket"
            detail = nxt.get("message") or "Pocket locked — plan next part"
    elif conf["overall"] >= 0.45 and result.get("ok"):
        recommendation = "verify_with_ears_eyes"
        detail = (
            "Partial confidence. Review _vision/arm_watch screenshots and "
            "_vision/ears WAVs, then decide gate or re-run job."
        )
    elif not result.get("ok"):
        recommendation = "fix_and_retry"
        detail = (
            f"Job failed: {result.get('error')}. "
            f"Cues: {', '.join(conf['notes']) or 'see scores'}. "
            "Fix MIDI ports / arm / instruments, re-plan, re-execute."
        )
    else:
        recommendation = "investigate"
        detail = "Low cue confidence. Inspect eyes + ears before advancing."

    return {
        "song_dir": str(song.resolve()),
        "gates": gates,
        "inventory": inv,
        "last_result_ok": None if result is None else bool(result.get("ok")),
        "job_id": None if result is None else result.get("job_id"),
        "confidence": conf,
        "recommendation": recommendation,
        "detail": detail,
        "next_action": nxt,
        "eyes_dir": None if result is None else result.get("eyes_dir"),
        "audio_captures": len((result or {}).get("audio") or []),
        "vision_summary": (result or {}).get("vision"),
    }


def decide(
    song_dir: Path,
    *,
    auto_approve_technical: bool = False,
    min_confidence: float = 0.85,
) -> Dict[str, Any]:
    """
    Apply producer policy after observe.

    Artistic gates (pocket/lead/...) never auto-lock unless user passes
    auto_approve_technical AND confidence is very high AND only for
    non-taste technical acknowledgements. Default: no gate writes.
    """
    song = Path(song_dir)
    obs = observe(song)
    actions: List[str] = []

    # Technical: if brief open and job planned, do not touch
    # Only optional auto: skip nothing artistic
    if auto_approve_technical and obs["confidence"]["overall"] >= min_confidence:
        # Still never lock pocket/lead from metrics — log only
        append_notes(
            song,
            f"observe auto-tech conf={obs['confidence']['overall']} "
            f"rec={obs['recommendation']} (no artistic gate change)",
        )
        actions.append("logged_high_confidence_no_gate_change")
    else:
        append_notes(
            song,
            f"observe rec={obs['recommendation']} conf={obs['confidence']['overall']}",
        )
        actions.append("logged_observation")

    return {
        **obs,
        "actions_taken": actions,
        "policy": {
            "artistic_gates_auto": False,
            "auto_approve_technical": auto_approve_technical,
            "min_confidence": min_confidence,
        },
    }


def run_cycle(
    song_dir: Path,
    *,
    s1_remote: Optional[Path] = None,
    execute: bool = False,
    max_sec: Optional[float] = None,
    no_prompt: bool = True,
    plan_if_ready: bool = True,
) -> Dict[str, Any]:
    """
    One autonomous cycle:
      next → optionally plan mvp → optionally shell out to execute_job → observe

    execute=True requires Studio One open and S1 Notes wired.
    """
    import os
    import subprocess
    import sys

    song = Path(song_dir)
    out: Dict[str, Any] = {"song_dir": str(song.resolve()), "phases": []}

    nxt = next_action(song)
    out["phases"].append({"stage": "next", "data": nxt})

    if plan_if_ready and nxt.get("action") == "plan_mvp":
        planned = plan_mvp(song, max_sec=max_sec)
        out["phases"].append({"stage": "plan_mvp", "data": planned})
        if not planned.get("ok"):
            out["ok"] = False
            out["observe"] = observe(song)
            return out
    elif nxt.get("status") in ("need_brief", "need_mvp_midi", "final_locked", "awaiting_pocket_approval"):
        out["ok"] = True
        out["blocked"] = nxt.get("status")
        out["observe"] = observe(song)
        return out

    if execute:
        remote = Path(s1_remote) if s1_remote else Path(
            os.environ.get("S1_REMOTE", r"C:\Users\Box One\s1-remote")
        )
        exe = remote / "tools" / "execute_job.py"
        if not exe.is_file():
            out["ok"] = False
            out["error"] = f"execute_job.py missing at {exe}"
            out["observe"] = observe(song)
            return out
        cmd = [
            sys.executable,
            str(exe),
            "--song-dir",
            str(song),
        ]
        if no_prompt:
            cmd.append("--no-prompt")
        if max_sec is not None:
            cmd.extend(["--max-sec", str(max_sec)])
        env = os.environ.copy()
        env["PYTHONPATH"] = str(remote) + os.pathsep + env.get("PYTHONPATH", "")
        env["S1_SONG_DIR"] = str(song)
        env["S1_REMOTE"] = str(remote)
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=str(remote))
        out["phases"].append(
            {
                "stage": "execute",
                "returncode": proc.returncode,
                "stdout_tail": (proc.stdout or "")[-2000:],
                "stderr_tail": (proc.stderr or "")[-1000:],
            }
        )

    obs = decide(song)
    out["observe"] = obs
    out["ok"] = True
    return out
