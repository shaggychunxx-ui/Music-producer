"""
Original multi-part MIDI composition (brain side).

Studio One only streams/imports files; composition lives here so genre/theory
knowledge can drive material without hands thrash.
"""

from __future__ import annotations

import json
import random
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

try:
    import mido
except ImportError:  # pragma: no cover
    mido = None  # type: ignore

from song_pipeline_kb.song_state import append_notes, init_song

TPB = 480

# Pitch-class → MIDI note for bass octave ~F1–A1 (C1=24 … B1=35)
_PC = {
    "c": 0,
    "c#": 1,
    "db": 1,
    "d": 2,
    "d#": 3,
    "eb": 3,
    "e": 4,
    "e#": 5,  # enharmonic F
    "f": 5,
    "f#": 6,
    "gb": 6,
    "g": 7,
    "g#": 8,
    "ab": 8,
    "a": 9,
    "a#": 10,
    "bb": 10,
    "b": 11,
    "cb": 11,
    "b#": 0,
}

# Genre profiles → BPM, energy, progression roots (MIDI bass), scale for lead
# Default roots/scales are A minor dark-pulse; transposed via --key.
GENRE_PROFILES: Dict[str, Dict[str, Any]] = {
    "dark_pulse": {
        "bpm": 92,
        "bars": 32,
        "mood": "dark minor",
        "mode": "minor",
        "base_tonic_pc": 9,  # A
        "roots": [33, 33, 29, 29, 36, 36, 31, 31],  # A F C G (i–VI–III–VII)
        "scale": [57, 60, 62, 64, 67, 69, 72, 74],
        "kick_pattern": "four",
    },
    "trap": {
        "bpm": 140,
        "bars": 32,
        "mood": "dark minor trap",
        "mode": "minor",
        "base_tonic_pc": 9,
        "roots": [33, 33, 33, 36, 29, 29, 31, 31],
        "scale": [57, 60, 62, 63, 67, 69, 72],
        "kick_pattern": "trap",
    },
    "house": {
        "bpm": 124,
        "bars": 32,
        "mood": "minor house pulse",
        "mode": "minor",
        "base_tonic_pc": 9,
        "roots": [36, 36, 33, 33, 31, 31, 29, 29],
        "scale": [60, 62, 63, 65, 67, 70, 72],
        "kick_pattern": "four",
    },
    "ambient": {
        "bpm": 80,
        "bars": 32,
        "mood": "sparse ambient minor",
        "mode": "minor",
        "base_tonic_pc": 9,
        "roots": [33, 33, 36, 36, 31, 31, 29, 29],
        "scale": [57, 60, 64, 67, 69, 72],
        "kick_pattern": "sparse",
    },
}


def parse_key(key: Optional[str]) -> Tuple[Optional[int], str]:
    """
    Parse a key string into pitch-class 0–11 and a display label.
    E# → F (pc 5). Returns (None, 'default') if unset/invalid.
    """
    if not key or not str(key).strip():
        return None, "default"
    raw = str(key).strip()
    # strip mode words if present
    core = re.sub(
        r"\b(major|minor|maj|min|m)\b",
        "",
        raw,
        flags=re.I,
    ).strip()
    core = core.replace(" ", "").replace("♯", "#").replace("♭", "b")
    # unicode sharp/flat already handled; normalize
    low = core.lower()
    if low in _PC:
        pc = _PC[low]
        # Prefer user's spelling when enharmonic
        label = raw if len(raw) <= 8 else core
        return pc, label
    # single letter + accidental
    m = re.match(r"^([a-gA-G])([#b♯♭]?)$", core)
    if m:
        token = (m.group(1) + (m.group(2) or "")).lower().replace("♯", "#").replace("♭", "b")
        if token in _PC:
            return _PC[token], core
    return None, raw


def _transpose_profile(profile: Dict[str, Any], tonic_pc: Optional[int]) -> Dict[str, Any]:
    if tonic_pc is None:
        return profile
    base = int(profile.get("base_tonic_pc", 9))
    shift = (tonic_pc - base) % 12
    # Prefer downward/near bass octave shift for roots near A1
    if shift > 6:
        shift = shift - 12
    out = dict(profile)
    out["roots"] = [max(24, min(48, r + shift)) for r in profile["roots"]]
    out["scale"] = [max(36, min(96, p + shift)) for p in profile["scale"]]
    out["transpose_semitones"] = shift
    out["tonic_pc"] = tonic_pc
    return out


def _form_energy(bar: int, bars: int) -> float:
    """
    Professional long-form energy curve (0–1+).
    Scales to total length so 4+ minute songs get real intro/build/drop/bridge/outro.
    """
    if bars <= 0:
        return 1.0
    t = bar / bars
    # intro
    if t < 0.08:
        return 0.45 + 0.2 * (t / 0.08)
    # verse pocket
    if t < 0.22:
        return 0.75
    # build
    if t < 0.30:
        return 0.85 + 0.2 * ((t - 0.22) / 0.08)
    # chorus / main
    if t < 0.48:
        return 1.08
    # break / half
    if t < 0.55:
        return 0.55
    # build 2
    if t < 0.62:
        return 0.8 + 0.35 * ((t - 0.55) / 0.07)
    # final lift
    if t < 0.88:
        return 1.15
    # outro
    return 0.55 + 0.15 * (1.0 - (t - 0.88) / 0.12)


def _section(bar: int, bars: int) -> str:
    t = bar / max(1, bars)
    if t < 0.08:
        return "intro"
    if t < 0.22:
        return "verse"
    if t < 0.30:
        return "build"
    if t < 0.48:
        return "chorus"
    if t < 0.55:
        return "break"
    if t < 0.62:
        return "build2"
    if t < 0.88:
        return "final"
    return "outro"


def duration_sec(bpm: int, bars: int) -> float:
    return bars * 4.0 * 60.0 / float(bpm)


def bars_for_minutes(minutes: float, bpm: int) -> int:
    """Minimum whole bars for at least `minutes` at `bpm` (4/4)."""
    need = float(minutes) * float(bpm) / 4.0
    return max(16, int(need + 0.999))


def _write(path: Path, builder: Callable, *, bpm: int, bars: int, seed: int) -> float:
    if mido is None:
        raise RuntimeError("mido is required for compose — pip install mido")
    rng = random.Random(seed)
    mid = mido.MidiFile(ticks_per_beat=TPB)
    tr = mido.MidiTrack()
    mid.tracks.append(tr)
    tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm)))
    # optional key signature (fifths); F major = -1, F minor ~ -4; skip exact for E#
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
    bars = int(profile.get("bars") or 32)

    def drums(bar: int, rng: random.Random):
        out = []
        energy = _form_energy(bar, bars)
        sec = _section(bar, bars)
        kick_v = int(108 * min(1.12, energy))
        sn_v = int(92 * min(1.12, energy))
        if pattern == "sparse":
            out.append({"t": 0.0, "d": 0.12, "p": 36, "v": kick_v})
            if bar % 2 == 0:
                out.append({"t": 2.0, "d": 0.12, "p": 36, "v": kick_v - 10})
            out.append({"t": 1.0, "d": 0.1, "p": 38, "v": int(sn_v * 0.7)})
        elif pattern == "trap":
            for beat in (0.0, 1.5, 2.0, 3.25):
                out.append(
                    {
                        "t": beat,
                        "d": 0.1,
                        "p": 36,
                        "v": kick_v - (0 if beat < 1 else 6),
                    }
                )
            out.append({"t": 1.0, "d": 0.12, "p": 38, "v": sn_v})
            out.append({"t": 3.0, "d": 0.12, "p": 38, "v": sn_v - 4})
            dens = 16 if sec in ("chorus", "final", "build", "build2") else 8
            step = 0.25 if dens == 16 else 0.5
            for i in range(dens):
                t = i * step
                if sec == "intro" and i % 2:
                    continue
                out.append(
                    {
                        "t": t + rng.uniform(-0.005, 0.005),
                        "d": 0.05,
                        "p": 42,
                        "v": int(40 + (12 if i % 4 == 0 else 0) * energy),
                    }
                )
        else:  # four-on-floor professional
            if sec == "break":
                # half-time feel
                out.append({"t": 0.0, "d": 0.14, "p": 36, "v": kick_v})
                out.append({"t": 2.0, "d": 0.14, "p": 36, "v": kick_v - 6})
                out.append({"t": 1.0, "d": 0.12, "p": 38, "v": int(sn_v * 0.85)})
                out.append({"t": 3.0, "d": 0.12, "p": 38, "v": int(sn_v * 0.8)})
            else:
                kicks = (0.0, 1.0, 2.0, 3.0)
                if sec == "intro":
                    kicks = (0.0, 2.0)
                for beat in kicks:
                    out.append(
                        {
                            "t": beat,
                            "d": 0.12,
                            "p": 36,
                            "v": kick_v - (0 if beat in (0, 2) else 8),
                        }
                    )
                if bar % 2 == 1 and sec not in ("intro", "outro"):
                    out.append({"t": 2.5, "d": 0.08, "p": 36, "v": int(70 * energy)})
                out.append({"t": 1.0, "d": 0.12, "p": 38, "v": sn_v})
                out.append({"t": 3.0, "d": 0.12, "p": 38, "v": sn_v - 4})
                # phrase fills
                if bar % 8 == 7 and sec not in ("intro",):
                    out.append({"t": 3.5, "d": 0.08, "p": 39, "v": 100})
                    out.append({"t": 3.75, "d": 0.06, "p": 38, "v": 80})
                if bar % 16 == 15 and sec in ("chorus", "final", "build2"):
                    for t in (3.0, 3.25, 3.5, 3.75):
                        out.append({"t": t, "d": 0.06, "p": 38, "v": 88})
            hat_n = 8 if sec != "break" else 4
            for i in range(hat_n):
                t = i * (0.5 if hat_n == 8 else 1.0)
                v = int((52 + (10 if i % 2 == 0 else 0)) * min(1.15, energy))
                if sec == "intro" and i % 2:
                    continue
                if sec == "outro" and i % 2:
                    continue
                out.append(
                    {
                        "t": t + rng.uniform(-0.008, 0.008),
                        "d": 0.07,
                        "p": 42,
                        "v": v,
                    }
                )
            if sec in ("chorus", "final", "build2"):
                for i in range(4):
                    out.append({"t": 0.25 + i, "d": 0.05, "p": 44, "v": 48})
        return out

    return drums


def _bass_builder(profile: Dict[str, Any]):
    roots = profile.get("roots") or [33, 33, 29, 29, 36, 36, 31, 31]
    bars = int(profile.get("bars") or 32)

    def bass(bar: int, rng: random.Random):
        r = roots[bar % len(roots)]
        sec = _section(bar, bars)
        energy = _form_energy(bar, bars)
        if sec == "intro":
            return [
                {"t": 0.0, "d": 1.8, "p": r, "v": 88},
                {"t": 2.0, "d": 1.6, "p": r, "v": 78},
            ]
        if sec == "outro":
            return [{"t": 0.0, "d": 3.5, "p": r, "v": 70}]
        if sec == "break":
            return [
                {"t": 0.0, "d": 1.5, "p": r, "v": 80},
                {"t": 2.0, "d": 1.5, "p": r - 5, "v": 74},
            ]
        # tight pocket for verse/chorus
        fifth = r + 7 if bar % 4 < 2 else r + 5
        approach = r - 5 if bar % 2 else r
        notes = [
            {"t": 0.0, "d": 0.7, "p": r, "v": int(102 * min(1.05, energy))},
            {"t": 0.75, "d": 0.2, "p": r, "v": 70},
            {"t": 1.5, "d": 0.4, "p": r, "v": 88},
            {"t": 2.0, "d": 0.7, "p": fifth, "v": 94},
            {"t": 2.75, "d": 0.2, "p": r, "v": 68},
            {"t": 3.25, "d": 0.45, "p": approach, "v": 86},
        ]
        if bar % 8 == 7 and sec in ("chorus", "final", "build", "build2"):
            notes.append({"t": 3.75, "d": 0.2, "p": r + 12, "v": 75})
        return notes

    return bass


def _lead_builder(profile: Dict[str, Any]):
    scale = profile.get("scale") or [57, 60, 62, 64, 67, 69, 72, 74]
    bars = int(profile.get("bars") or 32)

    def lead(bar: int, rng: random.Random):
        sec = _section(bar, bars)
        if sec in ("intro", "verse"):
            # leave pocket space early
            if sec == "intro" or (sec == "verse" and bar % 4 != 0):
                return []
        if sec == "outro":
            return [{"t": 0.0, "d": 3.2, "p": scale[min(5, len(scale) - 1)], "v": 62}]
        if sec == "break":
            # sparse motif
            p0 = scale[0]
            return [
                {"t": 0.0, "d": 1.2, "p": p0, "v": 70},
                {"t": 2.0, "d": 1.5, "p": scale[min(2, len(scale) - 1)], "v": 64},
            ]
        degs = [
            [0, 2, 4, 2],
            [4, 3, 2, 0],
            [2, 4, 5, 4],
            [5, 4, 2, 0],
        ][bar % 4]
        # longer melodic phrases in final
        if sec == "final" and bar % 2 == 0:
            degs = [0, 2, 4, 5, 4, 2]
        out = []
        step = 0.95 if len(degs) <= 4 else 0.62
        for i, d in enumerate(degs):
            if bar % 8 == 7 and i >= 2 and sec not in ("final", "chorus"):
                break
            oct = 12 if sec in ("chorus", "final") and i == 0 and bar % 8 < 4 else 0
            pitch = scale[d % len(scale)] + oct
            out.append(
                {
                    "t": i * step + rng.uniform(-0.015, 0.015),
                    "d": 0.55 + (0.25 if i == 0 else 0),
                    "p": pitch,
                    "v": 92 if i == 0 else 68 + rng.randint(0, 8),
                }
            )
        return out

    return lead


def _bed_builder(profile: Dict[str, Any]):
    roots = profile.get("roots") or [33, 33, 29, 29, 36, 36, 31, 31]
    bars = int(profile.get("bars") or 32)

    def bed(bar: int, rng: random.Random):
        r = roots[bar % len(roots)]
        sec = _section(bar, bars)
        # minor triad mid register (root + m3 + P5)
        ch = [r + 12, r + 15, r + 19]
        if sec == "intro":
            v = 42
        elif sec == "break":
            v = 38
            ch = [r + 12, r + 19]  # open fifths
        elif sec in ("chorus", "final"):
            v = 60
            # add optional 7th color
            if bar % 2 == 0:
                ch = [r + 12, r + 15, r + 19, r + 22]
        elif sec == "outro":
            v = 36
        else:
            v = 52
        return [{"t": 0.0, "d": 3.85, "p": p, "v": v} for p in ch]

    return bed


def _color_builder(profile: Dict[str, Any]):
    scale = profile.get("scale") or [57, 60, 62, 64, 67, 69, 72, 74]
    bars = int(profile.get("bars") or 32)

    def color(bar: int, rng: random.Random):
        sec = _section(bar, bars)
        if sec in ("intro", "outro", "break"):
            return []
        if sec == "verse" and bar % 8 != 7:
            return []
        if bar % 4 != 3 and sec not in ("chorus", "final", "build2"):
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
    key: Optional[str] = None,
    min_minutes: Optional[float] = None,
    parts: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Write MIDI/{drums,bass,lead,bed,color}.mid under song_dir.

    key: e.g. E#, F, Am — E# is enharmonic F (pc 5).
    min_minutes: if set, raise bars so duration is at least this long.
    """
    song = Path(song_dir)
    init_song(song)
    gkey = (genre or "dark_pulse").lower().replace(" ", "_").replace("-", "_")
    if gkey not in GENRE_PROFILES:
        for k in GENRE_PROFILES:
            if gkey in k or k in gkey:
                gkey = k
                break
        else:
            gkey = "dark_pulse"
    profile = dict(GENRE_PROFILES[gkey])
    if bpm is not None:
        profile["bpm"] = int(bpm)
    if bars is not None:
        profile["bars"] = int(bars)

    tonic_pc, key_label = parse_key(key)
    profile = _transpose_profile(profile, tonic_pc)

    if min_minutes is not None and float(min_minutes) > 0:
        need = bars_for_minutes(float(min_minutes), int(profile["bpm"]))
        if int(profile["bars"]) < need:
            profile["bars"] = need

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
    dur = duration_sec(int(profile["bpm"]), int(profile["bars"]))
    meta: Dict[str, Any] = {
        "ok": True,
        "genre": gkey,
        "bpm": profile["bpm"],
        "bars": profile["bars"],
        "duration_sec": round(dur, 2),
        "duration_min": round(dur / 60.0, 3),
        "key": key_label,
        "tonic_pc": profile.get("tonic_pc"),
        "transpose_semitones": profile.get("transpose_semitones", 0),
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
        (
            f"compose genre={gkey} key={key_label} bpm={profile['bpm']} "
            f"bars={profile['bars']} ~{meta['duration_min']}min seed={seed_v}"
        ),
    )
    return meta


def list_genres() -> List[str]:
    return sorted(GENRE_PROFILES.keys())
