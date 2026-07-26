"""
Technical QC scoring from S1 last_result + optional ref fingerprint JSON.

Does not claim artistic taste — crest/signal/clip evidence only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from song_pipeline_kb.s1_jobs import load_last_result


def _load_ref(song_dir: Path) -> Optional[Dict[str, Any]]:
    for rel in ("ref_fingerprint.json", "MIDI/ref_fingerprint.json", "_vision/ref_fingerprint.json"):
        p = Path(song_dir) / rel
        if p.is_file():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                return None
    return None


def score_execution(result: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not result:
        return {"overall": 0.0, "notes": ["no_result"], "pass": False}
    notes: List[str] = []
    scores: Dict[str, float] = {}
    scores["job_ok"] = 1.0 if result.get("ok") else 0.0
    stream = [s for s in (result.get("steps") or []) if s.get("op") == "stream_record"]
    if stream:
        clip = sum(1 for s in stream if s.get("clip_growth") or (s.get("lane") or {}).get("growth"))
        audio = sum(1 for s in stream if (s.get("audio") or {}).get("has_signal"))
        notes_ok = sum(1 for s in stream if (s.get("note_ons") or 0) > 0 or s.get("imported"))
        scores["clip"] = clip / len(stream)
        scores["audio"] = audio / len(stream)
        scores["material"] = notes_ok / len(stream)
    else:
        scores["clip"] = 0.0
        scores["audio"] = 0.0
        scores["material"] = 0.0
        notes.append("no_stream_steps")

    audio_list = result.get("audio") or []
    if audio_list:
        peaks = [a.get("peak_db", -120) for a in audio_list if a.get("peak_db") is not None]
        if peaks:
            # Prefer not clipped (peak < -0.5) and not silent
            clipped = sum(1 for p in peaks if p > -0.3)
            silent = sum(1 for p in peaks if p < -50)
            scores["headroom"] = 1.0 - min(1.0, clipped / len(peaks))
            scores["not_silent"] = 1.0 - min(1.0, silent / len(peaks))
            avg_peak = sum(peaks) / len(peaks)
            scores["avg_peak_norm"] = max(0.0, min(1.0, (avg_peak + 40) / 35.0))
    else:
        scores["headroom"] = 0.5
        scores["not_silent"] = 0.3
        notes.append("no_audio_list")

    weights = {
        "job_ok": 0.2,
        "clip": 0.25,
        "audio": 0.2,
        "material": 0.15,
        "headroom": 0.1,
        "not_silent": 0.1,
    }
    overall = sum(scores.get(k, 0) * w for k, w in weights.items())
    return {
        "overall": round(overall, 3),
        "scores": {k: round(v, 3) for k, v in scores.items()},
        "notes": notes,
        "pass": overall >= 0.62 and bool(result.get("ok")),
    }


def score_vs_ref(song_dir: Path, result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    song = Path(song_dir)
    result = result if result is not None else load_last_result(song)
    base = score_execution(result)
    ref = _load_ref(song)
    if not ref:
        base["ref"] = None
        base["ref_match"] = None
        return base
    # Compare average peak/rms if present on both
    notes = list(base.get("notes") or [])
    ref_peak = ref.get("peak_db") or ref.get("peak")
    audio_list = (result or {}).get("audio") or []
    if ref_peak is not None and audio_list:
        peaks = [a.get("peak_db") for a in audio_list if a.get("peak_db") is not None]
        if peaks:
            avg = sum(peaks) / len(peaks)
            delta = abs(float(avg) - float(ref_peak))
            # Within 12 dB counts as usable match
            match = max(0.0, 1.0 - delta / 12.0)
            base["ref_match"] = round(match, 3)
            base["ref_peak_db"] = ref_peak
            base["song_avg_peak_db"] = round(avg, 2)
            base["overall"] = round(min(1.0, base["overall"] * 0.75 + match * 0.25), 3)
            base["pass"] = base["overall"] >= 0.62 and bool((result or {}).get("ok"))
            notes.append(f"ref_peak_delta_db={delta:.1f}")
    base["ref"] = {"path_keys": list(ref.keys())[:12]}
    base["notes"] = notes
    return base


def qc_report(song_dir: Path) -> Dict[str, Any]:
    song = Path(song_dir)
    result = load_last_result(song)
    scored = score_vs_ref(song, result)
    return {
        "song_dir": str(song.resolve()),
        "job_id": None if not result else result.get("job_id"),
        "qc": scored,
        "recommendation": (
            "pass_technical"
            if scored.get("pass")
            else "retry_or_inspect"
        ),
    }
