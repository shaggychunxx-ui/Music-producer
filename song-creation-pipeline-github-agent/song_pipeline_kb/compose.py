"""
Original multi-part MIDI composition (brain side).

Studio One only streams/imports files; composition lives here so genre/theory
knowledge can drive material without hands thrash.
"""

from __future__ import annotations

import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

try:
    import mido
except ImportError:  # pragma: no cover
    mido = None  # type: ignore

from song_pipeline_kb.song_state import append_notes, init_song

TPB = 480

# Genre profiles → BPM, energy, progression roots (MIDI bass), scale for lead
GENRE_PROFILES: Dict[str, Dict[str, Any]] = {
    "dark_pulse": {
        "bpm": 92,
        "bars": 32,
        "mood": "dark minor",
        "roots": [33, 33, 29, 29, 36, 36, 31, 31],  # A F C G
        "scale": [57, 60, 62, 64, 67, 69, 72, 74],
        "kick_pattern": "four",
    },
    "trap": {
        "bpm": 140,
        "bars": 32,
        "mood": "dark minor trap",
        "roots": [33, 33, 33, 36, 29, 29, 31, 31],
        "scale": [57, 60, 62, 63, 67, 69, 72],
        "kick_pattern": "trap",
    },
    "house": {
        "bpm": 124,
        "bars": 32,
        "mood": "minor house pulse",
        "roots": [36, 36, 33, 33, 31, 31, 29, 29],
        "scale": [60, 62, 63, 65, 67, 70, 72],
        "kick_pattern": "four",
    },
    "ambient": {
        "bpm": 80,
        "bars": 32,
        "mood": "sparse ambient minor",
        "roots": [33, 33, 36, 36, 31, 31, 29, 29],
        "scale": [57, 60, 64, 67, 69, 72],
        "kick_pattern": "sparse",
    },
}


def _write(path: Path, builder: Callable, *, bpm: int, bars: int, seed: int) -> float:
    if mido is None:
        raise RuntimeError("mido is required for compose — pip install mido")
    rng = random.Random(seed)
    mid = mido.MidiFile(ticks_per_beat=TPB)
    tr = mido.MidiTrack()
    mid.tracks.append(tr)
    tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm)))
    events: List[tuple] = []
    for bar in range(bars):
        for n in builder(bar, rng):
            t0 = max(0, int((bar * 4 + n["t"]) * TPB))
            t1 = t0 + max(1, int(n["d"] * TPB))
            events.append((t0, 1, int(n["p"]), int(n["v"])))
            events.append((t1, 0, int(n["p"]), 0))
    events.sort(key=lambda e: (e[0], e[1]))
    abs_t = 0
    for t, on, p, v in events:
        dt = max(0, t - abs_t)
        abs_t = t
        tr.append(
            mido.Message(
                "note_on" if on else "note_off",
                note=max(0, min(127, p)),
                velocity=max(0, min(127, v)) if on else 0,
                time=dt,
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    mid.save(str(path))
    return float(mido.MidiFile(str(path)).length)


def _drums_builder(profile: Dict[str, Any]):
    pattern = profile.get("kick_pattern") or "four"

    def drums(bar: int, rng: random.Random):
        out = []
        energy = 1.0
        if bar < 4:
            energy = 0.55
        elif bar >= 24:
            energy = 1.15
        if bar >= 28:
            energy = 0.7
        kick_v = int(108 * min(1.0, energy))
        sn_v = int(92 * min(1.0, energy))
        if pattern == "sparse":
            out.append({"t": 0.0, "d": 0.12, "p": 36, "v": kick_v})
            if bar % 2 == 0:
                out.append({"t": 2.0, "d": 0.12, "p": 36, "v": kick_v - 10})
            out.append({"t": 1.0, "d": 0.1, "p": 38, "v": int(sn_v * 0.7)})
        elif pattern == "trap":
            for beat in (0.0, 1.5, 2.0, 3.25):
                out.append({"t": beat, "d": 0.1, "p": 36, "v": kick_v - (0 if beat < 1 else 6)})
            out.append({"t": 1.0, "d": 0.12, "p": 38, "v": sn_v})
            out.append({"t": 3.0, "d": 0.12, "p": 38, "v": sn_v - 4})
            for i in range(16):
                t = i * 0.25
                if bar < 4 and i % 2:
                    continue
                out.append(
                    {
                        "t": t + rng.uniform(-0.005, 0.005),
                        "d": 0.05,
                        "p": 42,
                        "v": int(40 + (12 if i % 4 == 0 else 0)),
                    }
                )
        else:  # four
            for beat in (0.0, 1.0, 2.0, 3.0):
                out.append(
                    {
                        "t": beat,
                        "d": 0.12,
                        "p": 36,
                        "v": kick_v - (0 if beat in (0, 2) else 8),
                    }
                )
            if bar % 2 == 1 and bar >= 4:
                out.append({"t": 2.5, "d": 0.08, "p": 36, "v": int(70 * energy)})
            out.append({"t": 1.0, "d": 0.12, "p": 38, "v": sn_v})
            out.append({"t": 3.0, "d": 0.12, "p": 38, "v": sn_v - 4})
            if bar % 4 == 3 and bar >= 7:
                out.append({"t": 3.5, "d": 0.08, "p": 39, "v": 100})
                out.append({"t": 3.75, "d": 0.06, "p": 38, "v": 80})
            for i in range(8):
                t = i * 0.5
                v = int((52 + (10 if i % 2 == 0 else 0)) * min(1.1, energy))
                if bar < 4 and i % 2:
                    continue
                out.append(
                    {
                        "t": t + rng.uniform(-0.008, 0.008),
                        "d": 0.07,
                        "p": 42,
                        "v": v,
                    }
                )
        return out

    return drums


def _bass_builder(profile: Dict[str, Any]):
    roots = profile.get("roots") or [33, 33, 29, 29, 36, 36, 31, 31]

    def bass(bar: int, rng: random.Random):
        r = roots[bar % len(roots)]
        if bar < 4:
            return [
                {"t": 0.0, "d": 1.8, "p": r, "v": 88},
                {"t": 2.0, "d": 1.6, "p": r, "v": 78},
            ]
        if bar >= 28:
            return [{"t": 0.0, "d": 3.5, "p": r, "v": 70}]
        return [
            {"t": 0.0, "d": 0.7, "p": r, "v": 102},
            {"t": 0.75, "d": 0.2, "p": r, "v": 70},
            {"t": 1.5, "d": 0.4, "p": r, "v": 88},
            {"t": 2.0, "d": 0.7, "p": r + 7 if bar % 4 < 2 else r + 5, "v": 94},
            {"t": 2.75, "d": 0.2, "p": r, "v": 68},
            {"t": 3.25, "d": 0.45, "p": r - 5 if bar % 2 else r, "v": 86},
        ]

    return bass


def _lead_builder(profile: Dict[str, Any]):
    scale = profile.get("scale") or [57, 60, 62, 64, 67, 69, 72, 74]

    def lead(bar: int, rng: random.Random):
        if bar < 8:
            return []
        if bar >= 28:
            return [{"t": 0.0, "d": 3.2, "p": scale[min(5, len(scale) - 1)], "v": 62}]
        degs = [
            [0, 2, 4, 2],
            [4, 3, 2, 0],
            [2, 4, 5, 4],
            [5, 4, 2, 0],
        ][bar % 4]
        out = []
        for i, d in enumerate(degs):
            if bar % 8 == 7 and i >= 2:
                break
            pitch = scale[d % len(scale)] + (12 if 16 <= bar < 24 and i == 0 else 0)
            out.append(
                {
                    "t": i * 0.95 + rng.uniform(-0.015, 0.015),
                    "d": 0.55 + (0.2 if i == 0 else 0),
                    "p": pitch,
                    "v": 92 if i == 0 else 68 + rng.randint(0, 8),
                }
            )
        return out

    return lead


def _bed_builder(profile: Dict[str, Any]):
    roots = profile.get("roots") or [33, 33, 29, 29, 36, 36, 31, 31]

    def bed(bar: int, rng: random.Random):
        r = roots[bar % len(roots)]
        # triad mid register
        ch = [r + 12, r + 15, r + 19]
        v = 48 if bar < 4 else (58 if bar < 24 else 50)
        if bar >= 28:
            v = 40
        return [{"t": 0.0, "d": 3.85, "p": p, "v": v} for p in ch]

    return bed


def _color_builder(profile: Dict[str, Any]):
    scale = profile.get("scale") or [57, 60, 62, 64, 67, 69, 72, 74]

    def color(bar: int, rng: random.Random):
        if bar < 12 or bar >= 28:
            return []
        if bar % 4 != 3:
            return []
        top = scale[-1] if scale else 84
        return [
            {"t": 3.0, "d": 0.25, "p": min(100, top + 12), "v": 55},
            {"t": 3.5, "d": 0.2, "p": min(100, top + 7), "v": 48},
        ]

    return color


def compose_song(
    song_dir: Path,
    *,
    genre: str = "dark_pulse",
    seed: Optional[int] = None,
    bpm: Optional[int] = None,
    bars: Optional[int] = None,
    parts: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Write MIDI/{drums,bass,lead,bed,color}.mid under song_dir.
    """
    song = Path(song_dir)
    init_song(song)
    key = (genre or "dark_pulse").lower().replace(" ", "_").replace("-", "_")
    if key not in GENRE_PROFILES:
        # fuzzy
        for k in GENRE_PROFILES:
            if key in k or k in key:
                key = k
                break
        else:
            key = "dark_pulse"
    profile = dict(GENRE_PROFILES[key])
    if bpm is not None:
        profile["bpm"] = int(bpm)
    if bars is not None:
        profile["bars"] = int(bars)
    seed_v = int(seed if seed is not None else 92026)
    midi_dir = song / "MIDI"
    midi_dir.mkdir(parents=True, exist_ok=True)

    builders = {
        "drums.mid": _drums_builder(profile),
        "bass.mid": _bass_builder(profile),
        "lead.mid": _lead_builder(profile),
        "bed.mid": _bed_builder(profile),
        "color.mid": _color_builder(profile),
    }
    want = parts or list(builders.keys())
    meta: Dict[str, Any] = {
        "ok": True,
        "genre": key,
        "bpm": profile["bpm"],
        "bars": profile["bars"],
        "seed": seed_v,
        "mood": profile.get("mood"),
        "parts": {},
        "composed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    for name in want:
        if name not in builders and not name.endswith(".mid"):
            name = f"{name}.mid"
        if name not in builders:
            continue
        length = _write(
            midi_dir / name,
            builders[name],
            bpm=int(profile["bpm"]),
            bars=int(profile["bars"]),
            seed=seed_v + hash(name) % 1000,
        )
        meta["parts"][name] = {"length_sec": round(length, 2)}

    (midi_dir / "compose_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    append_notes(
        song,
        f"compose genre={key} bpm={profile['bpm']} bars={profile['bars']} seed={seed_v}",
    )
    return meta


def list_genres() -> List[str]:
    return sorted(GENRE_PROFILES.keys())
