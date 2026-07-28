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
    import_ok = 0
    clip_ok = 0
    for s in stream_steps:
        if (s.get("note_ons") or 0) > 0:
            notes_ok += 1
        if s.get("armed_confirmed"):
            armed_ok += 1
        if s.get("method") == "import_fallback" and s.get("imported"):
            import_ok += 1
            notes_ok += 1  # import counts as delivered material
            clip_ok += 1
        if s.get("clip_growth"):
            notes.append("clip_growth_seen")
            clip_ok += 1
        lane = s.get("lane") or {}
        if lane.get("growth"):
            notes.append(f"lane_growth delta={lane.get('delta')}")
            clip_ok += 1
        # Per-step audio
        a = s.get("audio") or {}
        if a.get("has_signal"):
            scores["audio_signal"] = max(scores.get("audio_signal", 0.0), 0.8)
        if (s.get("live_shots") or 0) > 0:
            notes.append(f"live_vision_frames={s.get('live_shots')}")
    if stream_steps:
        scores["stream_notes"] = min(1.0, notes_ok / len(stream_steps))
        scores["stream_armed"] = armed_ok / len(stream_steps)
        scores["clip_evidence"] = min(1.0, clip_ok / len(stream_steps))
        if import_ok:
            notes.append(f"import_fallback_used={import_ok}")
            # Import path doesn't need rec arm
            scores["stream_armed"] = max(scores["stream_armed"], 0.5)
        if scores.get("clip_evidence", 0) < 0.5 and notes_ok > 0:
            notes.append("notes_without_clip_growth — do not treat as recorded")
    else:
        scores["stream_notes"] = 0.0
        scores["stream_armed"] = 0.0
        scores["clip_evidence"] = 0.0
        if ok:
            notes.append("no_stream_steps")

    # Require eyes artifacts when job claimed stream
    shot_count = vision.get("shot_count") or result.get("shot_count") or 0
    if stream_steps and shot_count < 2:
        notes.append("insufficient_eyes_shots — observe refuses high confidence")
        scores["shots"] = 0.0

    # Weighted overall (execution health, not "sounds good")
    weights = {
        "job_ok": 0.2,
        "stream_notes": 0.1,
        "stream_armed": 0.15,
        "clip_evidence": 0.25,
        "any_rec_red": 0.1,
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

    # Surface structured arm failure causes (fix root cause, do not thrash)
    for s in stream_steps:
        ad = s.get("arm_diagnosis") or {}
        if ad.get("primary_cause"):
            notes.append(f"arm_cause={ad.get('primary_cause')}")
            if ad.get("next_action"):
                notes.append(f"arm_next={ad.get('next_action')}")
            for rem in (ad.get("remediations") or [])[:2]:
                notes.append(f"arm_fix: {rem}")

    return {
        "overall": round(overall, 3),
        "scores": {k: round(v, 3) for k, v in scores.items()},
        "notes": notes,
        "stream_step_count": len(stream_steps),
    }


def _load_last_failure(song: Path) -> Optional[Dict[str, Any]]:
    p = Path(song) / "s1_jobs" / "last_failure.json"
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def observe(song_dir: Path) -> Dict[str, Any]:
    """Read last_result + gates + inventory; produce decision recommendation."""
    song = Path(song_dir)
    result = load_last_result(song)
    gates = load_gates(song)
    inv = summary(song)
    conf = _confidence_from_cues(result or {})
    nxt = next_action(song)
    last_failure = _load_last_failure(song)
    if last_failure and not last_failure.get("ok", True):
        conf.setdefault("notes", []).append(
            f"last_failure={last_failure.get('primary_cause')} domain={last_failure.get('domain')}"
        )
        for rem in (last_failure.get("remediations") or [])[:3]:
            conf["notes"].append(f"fix: {rem}")
        if last_failure.get("next_action"):
            conf["notes"].append(f"next_action={last_failure.get('next_action')}")

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
            auto_gate = None
        else:
            recommendation = "next_after_pocket"
            detail = nxt.get("message") or "Pocket locked — plan next part"
    elif conf["overall"] >= 0.72 and str(result.get("job_id", "")).startswith("lead"):
        if gates.get("lead") != "locked":
            recommendation = "user_listen_lead"
            detail = (
                "Lead stream cues look healthy (notes + audio/clips). "
                "USER should listen to lead. "
                "If approved: gate lead locked — then bed."
            )
        else:
            recommendation = "next_after_lead"
            detail = nxt.get("message") or "Lead locked — plan bed or skip"
    elif conf["overall"] >= 0.55 and result.get("ok"):
        recommendation = "verify_with_ears_eyes"
        detail = (
            "Useful confidence. Review _vision screenshots + ears WAVs, "
            "then lock the phase gate or re-run."
        )
    elif conf["overall"] >= 0.45 and result.get("ok"):
        recommendation = "verify_with_ears_eyes"
        detail = (
            "Partial confidence. Review _vision/arm_watch screenshots and "
            "_vision/ears WAVs, then decide gate or re-run job."
        )
    elif not result.get("ok"):
        recommendation = "fix_and_retry"
        lf = last_failure or (result or {}).get("failure") or {}
        cause = lf.get("primary_cause") or result.get("error") or "unknown"
        detail = (
            f"Job failed primary_cause={cause}. "
            f"See s1_jobs/last_failure.json remediations. "
            f"Cues: {', '.join(conf['notes'][:5]) or 'see scores'}. "
            "Fix root cause (not thrash), re-plan, re-execute."
        )
        if lf.get("next_action"):
            detail += f" next_action={lf.get('next_action')}"
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
        "last_failure": last_failure,
        "eyes_dir": None if result is None else result.get("eyes_dir"),
        "audio_captures": len((result or {}).get("audio") or []),
        "vision_summary": (result or {}).get("vision"),
    }


def _default_s1_remote() -> Path:
    """Resolve Studio-One hands repo: env → GitHub Desktop → legacy s1-remote."""
    import os

    env = (os.environ.get("S1_REMOTE") or "").strip()
    if env:
        return Path(env)
    candidates = [
        Path.home() / "Documents" / "GitHub" / "Studio-One",
        Path.home() / "s1-remote",
    ]
    for c in candidates:
        if (c / "tools" / "execute_job.py").is_file():
            return c
    return candidates[0]


def decide(
    song_dir: Path,
    *,
    auto_approve_technical: bool = False,
    min_confidence: float = 0.85,
    policy: str = "taste",
    unattended_min: float = 0.62,
) -> Dict[str, Any]:
    """
    Apply producer policy after observe.

    policy:
      - taste (default): never auto-lock artistic gates
      - unattended: auto-lock capture gates when confidence/QC pass
        (brief/pocket/lead/bed technical capture only — not final taste claim)
    """
    song = Path(song_dir)
    obs = observe(song)
    actions: List[str] = []
    gates_locked: List[str] = []
    conf = float(obs.get("confidence", {}).get("overall") or 0.0)
    rec = obs.get("recommendation") or ""
    job_id = str(obs.get("job_id") or "")

    if policy == "unattended" and conf >= unattended_min and obs.get("last_result_ok"):
        # Capture gates only — mark as metric-approved, not human taste
        try:
            from song_pipeline_kb.qc import score_vs_ref

            qc = score_vs_ref(song)
            obs["qc"] = qc.get("qc")
            qc_pass = bool((qc.get("qc") or {}).get("pass"))
        except Exception:
            qc_pass = conf >= unattended_min

        if qc_pass or conf >= max(unattended_min, 0.72):
            gates = obs.get("gates") or {}
            if job_id.startswith("mvp") and gates.get("pocket") != "locked":
                set_gate(song, "pocket", "locked")
                gates_locked.append("pocket")
                actions.append("unattended_lock_pocket")
            elif job_id.startswith("lead") and gates.get("lead") != "locked":
                set_gate(song, "lead", "locked")
                gates_locked.append("lead")
                actions.append("unattended_lock_lead")
            elif "bed" in job_id and gates.get("bed") != "locked":
                set_gate(song, "bed", "locked")
                gates_locked.append("bed")
                actions.append("unattended_lock_bed")
            append_notes(
                song,
                f"UNATTENDED metric gate lock conf={conf} rec={rec} locked={gates_locked}",
            )
        else:
            append_notes(song, f"unattended hold conf={conf} qc_fail rec={rec}")
            actions.append("unattended_hold")
    elif auto_approve_technical and conf >= min_confidence:
        append_notes(
            song,
            f"observe auto-tech conf={conf} rec={rec} (no artistic gate change)",
        )
        actions.append("logged_high_confidence_no_gate_change")
    else:
        append_notes(song, f"observe rec={rec} conf={conf}")
        actions.append("logged_observation")

    return {
        **obs,
        "actions_taken": actions,
        "gates_locked": gates_locked,
        "policy": {
            "mode": policy,
            "artistic_gates_auto": policy == "unattended",
            "auto_approve_technical": auto_approve_technical,
            "min_confidence": min_confidence,
            "unattended_min": unattended_min,
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
    policy: str = "taste",
    compose_if_missing: bool = False,
    genre: str = "dark_pulse",
) -> Dict[str, Any]:
    """
    One autonomous cycle:
      next → optionally compose → plan mvp → execute_job → observe/decide

    execute=True requires Studio One open and S1 Notes wired.
    """
    import os
    import subprocess
    import sys

    song = Path(song_dir)
    out: Dict[str, Any] = {"song_dir": str(song.resolve()), "phases": []}

    nxt = next_action(song)
    out["phases"].append({"stage": "next", "data": nxt})

    if compose_if_missing and nxt.get("action") == "compose_mvp_midi":
        from song_pipeline_kb.compose import compose_song

        comp = compose_song(song, genre=genre)
        out["phases"].append({"stage": "compose", "data": comp})
        nxt = next_action(song)
        out["phases"].append({"stage": "next_after_compose", "data": nxt})

    if plan_if_ready and nxt.get("action") == "plan_mvp":
        planned = plan_mvp(song, max_sec=max_sec)
        # Unattended: no_prompt on job options
        if planned.get("ok") and policy == "unattended":
            job = planned.get("job") or {}
            opts = job.setdefault("options", {})
            opts["no_prompt"] = True
            opts["import_on_arm_fail"] = True
            from song_pipeline_kb.s1_jobs import write_job

            write_job(song, job)
        out["phases"].append({"stage": "plan_mvp", "data": planned})
        if not planned.get("ok"):
            out["ok"] = False
            out["observe"] = observe(song)
            return out
    elif nxt.get("status") in ("need_brief", "need_mvp_midi", "final_locked", "awaiting_pocket_approval"):
        if policy == "unattended" and nxt.get("status") == "awaiting_pocket_approval":
            # Fall through to decide for metric lock
            pass
        elif nxt.get("status") == "need_mvp_midi" and compose_if_missing:
            pass
        else:
            out["ok"] = True
            out["blocked"] = nxt.get("status")
            out["observe"] = observe(song)
            return out

    if execute:
        remote = Path(s1_remote) if s1_remote else _default_s1_remote()
        exe = remote / "tools" / "execute_job.py"
        if not exe.is_file():
            out["ok"] = False
            out["error"] = f"execute_job.py missing at {exe}"
            out["s1_remote"] = str(remote)
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
        env["PYTHONPATH"] = str(remote) + os.pathsep + str(remote / "tools") + os.pathsep + env.get(
            "PYTHONPATH", ""
        )
        env["S1_SONG_DIR"] = str(song)
        env["S1_REMOTE"] = str(remote)
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=str(remote))
        out["phases"].append(
            {
                "stage": "execute",
                "s1_remote": str(remote),
                "returncode": proc.returncode,
                "stdout_tail": (proc.stdout or "")[-2000:],
                "stderr_tail": (proc.stderr or "")[-1000:],
            }
        )

    obs = decide(song, policy=policy)
    out["observe"] = obs
    out["ok"] = True
    return out


def run_full_unattended(
    song_dir: Path,
    *,
    s1_remote: Optional[Path] = None,
    name: Optional[str] = None,
    genre: str = "dark_pulse",
    max_sec: float = 40.0,
    parts: str = "drums,bass,lead",
    prefer_import: bool = False,
    skip_s1_hands: bool = False,
) -> Dict[str, Any]:
    """
    Full unattended path:
      init + brief lock → compose → call Studio-One autonomous_run (or cycle)

    skip_s1_hands=True only does brain-side compose + plan (for dry tests).
    """
    import os
    import subprocess
    import sys

    song = Path(song_dir)
    from song_pipeline_kb.song_state import init_song, set_gate, is_locked
    from song_pipeline_kb.compose import compose_song

    init_song(song, name=name or song.name)
    if not is_locked(song, "brief"):
        set_gate(song, "brief", "locked")
    comp = compose_song(song, genre=genre)
    out: Dict[str, Any] = {
        "song_dir": str(song.resolve()),
        "policy": "unattended",
        "compose": comp,
        "phases": [],
    }

    if skip_s1_hands:
        planned = plan_mvp(song, max_sec=max_sec)
        out["phases"].append({"stage": "plan_mvp", "data": planned})
        out["ok"] = bool(planned.get("ok"))
        return out

    remote = Path(s1_remote) if s1_remote else _default_s1_remote()
    auto = remote / "tools" / "autonomous_run.py"
    if auto.is_file():
        cmd = [
            sys.executable,
            str(auto),
            "--resume",
            "--song-dir",
            str(song),
            "--parts",
            parts,
            "--max-sec",
            str(max_sec),
        ]
        if prefer_import:
            cmd.append("--prefer-import")
        env = os.environ.copy()
        env["PYTHONPATH"] = str(remote) + os.pathsep + str(remote / "tools") + os.pathsep + env.get(
            "PYTHONPATH", ""
        )
        env["S1_SONG_DIR"] = str(song)
        env["S1_REMOTE"] = str(remote)
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=str(remote))
        out["phases"].append(
            {
                "stage": "autonomous_run",
                "returncode": proc.returncode,
                "stdout_tail": (proc.stdout or "")[-2500:],
                "stderr_tail": (proc.stderr or "")[-1000:],
            }
        )
        out["ok"] = proc.returncode == 0
    else:
        # Fallback: plan + execute cycle
        cyc = run_cycle(
            song,
            s1_remote=remote,
            execute=True,
            max_sec=max_sec,
            policy="unattended",
            compose_if_missing=False,
            genre=genre,
        )
        out["phases"].append({"stage": "cycle_fallback", "data": cyc})
        out["ok"] = bool(cyc.get("ok"))

    out["observe"] = decide(song, policy="unattended")
    return out
