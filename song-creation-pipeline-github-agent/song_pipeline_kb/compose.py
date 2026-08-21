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

# Genre profiles → BPM, progression roots (MIDI bass), scale, and *style* knobs.
# Styles force different bass/lead/drum languages so songs don't become
# "same progression, different key". Roots/scales default in A; --key transposes.
#
# bass_style:   pocket | pump | offbeat | walk | pedal | syncop | arpeg | drone
# lead_style:   motif | hook | call | sparse | run | folk | pluck | longline
# harmony:      minor_triad | major_triad | sus | open5 | cluster | add9
# kick_pattern: four | trap | sparse | breakbeat | half | latin | disco | rock
GENRE_PROFILES: Dict[str, Dict[str, Any]] = {
    "dark_pulse": {
        "bpm": 92,
        "bars": 32,
        "mood": "dark minor pulse",
        "mode": "minor",
        "base_tonic_pc": 9,  # A
        "roots": [33, 33, 29, 29, 36, 36, 31, 31],  # i–VI–III–VII
        "scale": [57, 60, 62, 64, 67, 69, 72, 74],
        "kick_pattern": "four",
        "bass_style": "pocket",
        "lead_style": "motif",
        "harmony": "minor_triad",
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
        "bass_style": "syncop",
        "lead_style": "hook",
        "harmony": "open5",
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
        "bass_style": "pump",
        "lead_style": "pluck",
        "harmony": "minor_triad",
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
        "bass_style": "drone",
        "lead_style": "sparse",
        "harmony": "cluster",
    },
    # --- high-diversity set (batch 20260810) ---
    "bright_pop": {
        "bpm": 118,
        "bars": 40,
        "mood": "bright major pop",
        "mode": "major",
        "base_tonic_pc": 0,  # C
        "roots": [36, 36, 41, 41, 43, 43, 38, 38],  # C F G D (I–IV–V–ii)
        "scale": [60, 62, 64, 65, 67, 69, 71, 72],  # C major
        "kick_pattern": "rock",
        "bass_style": "walk",
        "lead_style": "hook",
        "harmony": "major_triad",
    },
    "funk_groove": {
        "bpm": 102,
        "bars": 40,
        "mood": "syncopated funk major",
        "mode": "major",
        "base_tonic_pc": 7,  # G
        "roots": [31, 31, 31, 34, 36, 36, 29, 29],  # G Bb C F (I–bIII–IV–bVII)
        "scale": [55, 57, 59, 60, 62, 64, 66, 67],  # G mixolydish
        "kick_pattern": "breakbeat",
        "bass_style": "syncop",
        "lead_style": "call",
        "harmony": "add9",
    },
    "dnb_rush": {
        "bpm": 174,
        "bars": 48,
        "mood": "drum and bass rush minor",
        "mode": "minor",
        "base_tonic_pc": 2,  # D
        "roots": [26, 26, 26, 29, 33, 33, 24, 24],  # D F A C
        "scale": [50, 53, 55, 57, 60, 62, 65],
        "kick_pattern": "breakbeat",
        "bass_style": "offbeat",
        "lead_style": "run",
        "harmony": "open5",
    },
    "latin_heat": {
        "bpm": 108,
        "bars": 40,
        "mood": "latin clave major",
        "mode": "major",
        "base_tonic_pc": 5,  # F
        "roots": [29, 29, 36, 36, 33, 33, 31, 31],  # F C A G
        "scale": [53, 55, 57, 58, 60, 62, 64, 65],
        "kick_pattern": "latin",
        "bass_style": "arpeg",
        "lead_style": "folk",
        "harmony": "major_triad",
    },
    "jazz_night": {
        "bpm": 88,
        "bars": 40,
        "mood": "late jazz ii-V-I",
        "mode": "major",
        "base_tonic_pc": 10,  # Bb
        "roots": [36, 36, 41, 41, 34, 34, 34, 34],  # Cm7 F7 Bb (ii–V–I feel)
        "scale": [58, 60, 62, 63, 65, 67, 69, 70],  # Bb major-ish
        "kick_pattern": "half",
        "bass_style": "walk",
        "lead_style": "longline",
        "harmony": "add9",
    },
    "synthwave": {
        "bpm": 96,
        "bars": 40,
        "mood": "retro synthwave minor",
        "mode": "minor",
        "base_tonic_pc": 4,  # E
        "roots": [28, 28, 35, 35, 31, 31, 26, 26],  # E B G D (i–V–III–VII)
        "scale": [52, 55, 57, 59, 62, 64, 67],
        "kick_pattern": "disco",
        "bass_style": "pump",
        "lead_style": "longline",
        "harmony": "sus",
    },
    "folk_story": {
        "bpm": 84,
        "bars": 36,
        "mood": "acoustic folk major story",
        "mode": "major",
        "base_tonic_pc": 2,  # D
        "roots": [26, 26, 33, 33, 31, 31, 28, 28],  # D A G E (I–V–IV–ii)
        "scale": [50, 52, 54, 55, 57, 59, 61, 62],
        "kick_pattern": "sparse",
        "bass_style": "pedal",
        "lead_style": "folk",
        "harmony": "sus",
    },
    "metal_drive": {
        "bpm": 148,
        "bars": 40,
        "mood": "driven metal minor riff",
        "mode": "minor",
        "base_tonic_pc": 4,  # E
        "roots": [28, 28, 28, 28, 31, 31, 26, 26],  # E E G D
        "scale": [52, 55, 57, 58, 59, 62, 64],
        "kick_pattern": "rock",
        "bass_style": "pedal",
        "lead_style": "run",
        "harmony": "open5",
    },
    "lofi_haze": {
        "bpm": 76,
        "bars": 36,
        "mood": "lofi dusty major7 haze",
        "mode": "major",
        "base_tonic_pc": 9,  # A
        "roots": [33, 33, 40, 40, 38, 38, 36, 36],  # A E D C
        "scale": [57, 59, 61, 64, 66, 68, 69],
        "kick_pattern": "half",
        "bass_style": "drone",
        "lead_style": "sparse",
        "harmony": "add9",
    },
    "techno_grid": {
        "bpm": 130,
        "bars": 48,
        "mood": "hypnotic techno minor grid",
        "mode": "minor",
        "base_tonic_pc": 1,  # C#
        "roots": [25, 25, 25, 25, 32, 32, 28, 28],  # C# G# E
        "scale": [49, 52, 54, 56, 59, 61, 64],
        "kick_pattern": "four",
        "bass_style": "offbeat",
        "lead_style": "pluck",
        "harmony": "open5",
    },
    "reggae_sun": {
        "bpm": 74,
        "bars": 36,
        "mood": "sunny reggae skank major",
        "mode": "major",
        "base_tonic_pc": 7,  # G
        "roots": [31, 31, 36, 36, 38, 38, 33, 33],  # G C D A
        "scale": [55, 57, 59, 60, 62, 64, 66, 67],
        "kick_pattern": "half",
        "bass_style": "offbeat",
        "lead_style": "call",
        "harmony": "major_triad",
    },
    "phrygian_fire": {
        "bpm": 112,
        "bars": 40,
        "mood": "spanish phrygian fire",
        "mode": "phrygian",
        "base_tonic_pc": 4,  # E phrygian
        "roots": [28, 28, 29, 29, 31, 31, 26, 26],  # E F G D
        "scale": [52, 53, 55, 57, 59, 60, 62, 64],  # E phrygian
        "kick_pattern": "latin",
        "bass_style": "arpeg",
        "lead_style": "folk",
        "harmony": "sus",
    },
}


def parse_key(key: Optional[str]) -> Tuple[Optional[int], str]:
    """
    Parse a key string into pitch-class 0–11 and a display label.
    E# → F (pc 5). Am/Fm/F#m accepted (trailing m|min|minor|maj|major stripped).
    Returns (None, 'default') if unset/invalid.
    """
    if not key or not str(key).strip():
        return None, "default"
    raw = str(key).strip()
    # Normalize then strip trailing mode suffixes (Am, F#m, C minor, Bb maj)
    core = raw.replace(" ", "").replace("♯", "#").replace("♭", "b")
    core = re.sub(
        r"(?i)(major|minor|maj|min|m)$",
        "",
        core,
    ).strip()
    low = core.lower()
    if low in _PC:
        pc = _PC[low]
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
        human = 0.012 if pattern in ("rock", "latin", "breakbeat", "half") else 0.006

        def kick(t, v=None):
            out.append(
                {
                    "t": t + rng.uniform(-human, human),
                    "d": 0.12,
                    "p": 36,
                    "v": int(v if v is not None else kick_v),
                }
            )

        def snare(t, v=None):
            out.append(
                {
                    "t": t + rng.uniform(-human * 0.5, human * 0.5),
                    "d": 0.11,
                    "p": 38,
                    "v": int(v if v is not None else sn_v),
                }
            )

        def hat(t, v=50, open_hat=False):
            out.append(
                {
                    "t": t + rng.uniform(-human, human),
                    "d": 0.06 if not open_hat else 0.18,
                    "p": 46 if open_hat else 42,
                    "v": int(v * min(1.15, energy)),
                }
            )

        if pattern == "sparse":
            kick(0.0)
            if bar % 2 == 0:
                kick(2.0, kick_v - 10)
            snare(1.0, int(sn_v * 0.7))
            if sec not in ("intro", "outro"):
                hat(2.0, 38)
        elif pattern == "trap":
            for beat in (0.0, 1.5, 2.0, 3.25):
                kick(beat, kick_v - (0 if beat < 1 else 6))
            snare(1.0)
            snare(3.0, sn_v - 4)
            dens = 16 if sec in ("chorus", "final", "build", "build2") else 8
            step = 0.25 if dens == 16 else 0.5
            for i in range(dens):
                if sec == "intro" and i % 2:
                    continue
                hat(i * step, 40 + (12 if i % 4 == 0 else 0))
        elif pattern == "breakbeat":
            # amen-ish / dnb skeleton
            kicks = (0.0, 0.75, 2.25) if bar % 2 == 0 else (0.0, 1.5, 2.5)
            if sec == "intro":
                kicks = (0.0, 2.0)
            for b in kicks:
                kick(b)
            snare(1.0)
            snare(2.75, sn_v - 8)
            if sec in ("chorus", "final", "build2"):
                snare(3.5, int(sn_v * 0.75))
            dens = 16 if sec not in ("intro", "break") else 8
            for i in range(dens):
                hat(i * (4.0 / dens), 48 if i % 2 == 0 else 36)
            if bar % 4 == 3 and sec not in ("intro", "outro"):
                out.append({"t": 3.25, "d": 0.06, "p": 39, "v": 95})
                out.append({"t": 3.5, "d": 0.06, "p": 38, "v": 88})
                out.append({"t": 3.75, "d": 0.05, "p": 38, "v": 80})
        elif pattern == "half":
            kick(0.0)
            if sec not in ("intro", "break"):
                kick(2.5, kick_v - 12)
            snare(2.0)
            if sec in ("chorus", "final"):
                snare(3.5, int(sn_v * 0.65))
            for i in range(4):
                hat(i * 1.0, 44 if i % 2 == 0 else 34)
            if bar % 2 == 1:
                hat(1.5, 40, open_hat=True)
        elif pattern == "latin":
            # tumbao-ish kick + clave snare accents
            for b in (0.0, 1.5, 2.5):
                kick(b, kick_v - (0 if b == 0 else 10))
            snare(1.0, int(sn_v * 0.85))
            snare(2.75, int(sn_v * 0.7))
            for i, t in enumerate((0.0, 0.75, 1.5, 2.0, 2.75, 3.5)):
                hat(t, 55 if i % 2 == 0 else 40)
            if sec in ("chorus", "final"):
                out.append({"t": 3.0, "d": 0.08, "p": 39, "v": 78})
        elif pattern == "disco":
            for b in (0.0, 1.0, 2.0, 3.0):
                kick(b)
            snare(1.0)
            snare(3.0)
            for i in range(8):
                hat(i * 0.5, 58 if i % 2 else 46, open_hat=(i % 4 == 3))
            if bar % 8 == 7:
                out.append({"t": 3.5, "d": 0.08, "p": 39, "v": 100})
        elif pattern == "rock":
            kick(0.0)
            if sec not in ("intro", "break"):
                kick(2.5 if bar % 2 else 2.0, kick_v - 8)
            snare(1.0)
            snare(3.0)
            dens = 8 if sec not in ("intro", "outro") else 4
            for i in range(dens):
                hat(i * (4.0 / dens), 50 if i % 2 == 0 else 38)
            if bar % 8 == 7 and sec not in ("intro",):
                for t in (3.0, 3.25, 3.5, 3.75):
                    snare(t, 80)
        else:  # four-on-floor
            if sec == "break":
                kick(0.0)
                kick(2.0, kick_v - 6)
                snare(1.0, int(sn_v * 0.85))
                snare(3.0, int(sn_v * 0.8))
            else:
                kicks = (0.0, 2.0) if sec == "intro" else (0.0, 1.0, 2.0, 3.0)
                for beat in kicks:
                    kick(beat, kick_v - (0 if beat in (0, 2) else 8))
                if bar % 2 == 1 and sec not in ("intro", "outro"):
                    kick(2.5, int(70 * energy))
                snare(1.0)
                snare(3.0, sn_v - 4)
                if bar % 8 == 7 and sec not in ("intro",):
                    out.append({"t": 3.5, "d": 0.08, "p": 39, "v": 100})
                    out.append({"t": 3.75, "d": 0.06, "p": 38, "v": 80})
                if bar % 16 == 15 and sec in ("chorus", "final", "build2"):
                    for t in (3.0, 3.25, 3.5, 3.75):
                        snare(t, 88)
            hat_n = 8 if sec != "break" else 4
            for i in range(hat_n):
                t = i * (0.5 if hat_n == 8 else 1.0)
                if sec in ("intro", "outro") and i % 2:
                    continue
                hat(t, 52 + (10 if i % 2 == 0 else 0))
            if sec in ("chorus", "final", "build2"):
                for i in range(4):
                    out.append({"t": 0.25 + i, "d": 0.05, "p": 44, "v": 48})
        return out

    return drums


def _bass_builder(profile: Dict[str, Any]):
    roots = profile.get("roots") or [33, 33, 29, 29, 36, 36, 31, 31]
    bars = int(profile.get("bars") or 32)
    style = (profile.get("bass_style") or "pocket").lower()

    def bass(bar: int, rng: random.Random):
        r = roots[bar % len(roots)]
        sec = _section(bar, bars)
        energy = _form_energy(bar, bars)
        v0 = int(102 * min(1.05, energy))

        if style == "drone":
            if sec == "outro":
                return [{"t": 0.0, "d": 3.8, "p": r, "v": 62}]
            return [
                {"t": 0.0, "d": 3.9, "p": r, "v": int(78 + 10 * energy)},
            ]

        if style == "pedal":
            notes = [{"t": 0.0, "d": 0.45, "p": r, "v": v0}]
            for t in (1.0, 2.0, 3.0):
                notes.append({"t": t, "d": 0.4, "p": r, "v": v0 - 12})
            if sec in ("chorus", "final") and bar % 2 == 0:
                notes.append({"t": 3.5, "d": 0.35, "p": r + 12, "v": v0 - 20})
            return notes

        if style == "pump":
            # four-on-floor bass hits with octave jump
            notes = []
            for i, t in enumerate((0.0, 1.0, 2.0, 3.0)):
                p = r + (12 if i % 2 and sec in ("chorus", "final") else 0)
                notes.append({"t": t, "d": 0.55, "p": p, "v": v0 - i * 2})
                notes.append({"t": t + 0.5, "d": 0.2, "p": r, "v": 60})
            return notes

        if style == "offbeat":
            # reggae / techno offbeats
            notes = []
            for t in (0.5, 1.5, 2.5, 3.5):
                notes.append({"t": t, "d": 0.35, "p": r, "v": v0 - 6})
            if sec not in ("intro", "break"):
                notes.append({"t": 0.0, "d": 0.25, "p": r - 12 if r > 30 else r, "v": v0})
            if bar % 4 == 3:
                notes.append({"t": 3.75, "d": 0.2, "p": r + 7, "v": 80})
            return notes

        if style == "walk":
            # walking line through chord tones
            steps = [0, 2, 4, 5, 7, 5, 4, 2]
            if bar % 2:
                steps = [0, -2, 0, 3, 5, 3, 2, 0]
            notes = []
            for i, s in enumerate(steps):
                notes.append(
                    {
                        "t": i * 0.5,
                        "d": 0.42,
                        "p": max(24, min(48, r + s)),
                        "v": v0 - (4 if i % 2 else 0) + rng.randint(-3, 3),
                    }
                )
            return notes

        if style == "syncop":
            # funk / trap syncopation
            hits = [
                (0.0, 0.35, 0),
                (0.75, 0.2, 0),
                (1.5, 0.3, 7),
                (2.25, 0.25, 0),
                (3.0, 0.35, 5 if bar % 2 else 0),
                (3.5, 0.2, -5 if bar % 2 else 12),
            ]
            if sec == "intro":
                hits = [(0.0, 1.5, 0), (2.0, 1.5, 0)]
            return [
                {
                    "t": t,
                    "d": d,
                    "p": max(24, min(52, r + off)),
                    "v": v0 - abs(off),
                }
                for t, d, off in hits
            ]

        if style == "arpeg":
            arps = [0, 7, 12, 7, 0, 5, 12, 5]
            return [
                {
                    "t": i * 0.5,
                    "d": 0.38,
                    "p": max(24, min(55, r + a)),
                    "v": v0 - 8 + (i % 2) * 4,
                }
                for i, a in enumerate(arps)
            ]

        # pocket (default)
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
        fifth = r + 7 if bar % 4 < 2 else r + 5
        approach = r - 5 if bar % 2 else r
        notes = [
            {"t": 0.0, "d": 0.7, "p": r, "v": v0},
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
    style = (profile.get("lead_style") or "motif").lower()
    # Seed motif tables from profile seed-ish content so styles differ hard
    motif_sets = {
        "motif": [[0, 2, 4, 2], [4, 3, 2, 0], [2, 4, 5, 4], [5, 4, 2, 0]],
        "hook": [[0, 0, 4, 2, 0], [4, 4, 2, 0], [2, 4, 7 % len(scale), 4], [0, 2, 0, 4]],
        "call": [[0, 4], [2, 5], [4, 2], [5, 0]],
        "sparse": [[0], [4], [2], [0]],
        "run": [
            [0, 1, 2, 3, 4, 5, 4, 2],
            [5, 4, 3, 2, 1, 0, 2, 4],
            [2, 3, 4, 5, 4, 3, 2, 0],
            [4, 5, 4, 2, 0, 2, 4, 5],
        ],
        "folk": [[0, 2, 4, 5, 4], [4, 2, 0, 2], [2, 4, 5, 7 % len(scale), 5], [0, 2, 0]],
        "pluck": [[0, 2], [4], [2, 0], [5, 4, 2]],
        "longline": [
            [0, 2, 4, 5, 4, 2, 0, 2],
            [4, 5, 4, 2, 0, 2, 4, 5],
            [2, 0, 2, 4, 5, 4, 2, 0],
            [5, 4, 2, 0, 2, 4, 2, 0],
        ],
    }
    table = motif_sets.get(style, motif_sets["motif"])

    def lead(bar: int, rng: random.Random):
        sec = _section(bar, bars)
        nscale = len(scale)

        if style == "sparse":
            if sec in ("intro", "break", "outro"):
                return [{"t": 0.0, "d": 2.8, "p": scale[0], "v": 58}]
            if bar % 2:
                return []
            return [
                {
                    "t": float(rng.choice([0.0, 1.0, 2.0])),
                    "d": 1.8,
                    "p": scale[(bar * 2) % nscale],
                    "v": 64,
                }
            ]

        if style == "call":
            if sec == "intro":
                return []
            # short call every other bar, answer next
            degs = table[bar % len(table)]
            t0 = 0.0 if bar % 2 == 0 else 2.0
            return [
                {
                    "t": t0 + i * 0.45,
                    "d": 0.35,
                    "p": scale[d % nscale] + (12 if sec in ("chorus", "final") else 0),
                    "v": 90 if i == 0 else 70,
                }
                for i, d in enumerate(degs)
            ]

        if sec in ("intro",) and style not in ("longline", "folk"):
            return []
        if sec == "verse" and style in ("motif", "pluck") and bar % 4 != 0:
            return []
        if sec == "outro":
            return [{"t": 0.0, "d": 3.2, "p": scale[min(nscale - 1, 5)], "v": 62}]
        if sec == "break" and style not in ("longline", "run"):
            return [
                {"t": 0.0, "d": 1.2, "p": scale[0], "v": 70},
                {"t": 2.0, "d": 1.5, "p": scale[min(2, nscale - 1)], "v": 64},
            ]

        degs = table[bar % len(table)]
        if style == "run":
            step = 0.22
            dur = 0.18
            jitter = 0.008
            vel0 = 86
        elif style == "pluck":
            step = 0.5
            dur = 0.22
            jitter = 0.01
            vel0 = 88
        elif style == "longline":
            step = 0.48
            dur = 0.42
            jitter = 0.005
            vel0 = 80
        elif style == "folk":
            step = 0.55
            dur = 0.4
            jitter = 0.02
            vel0 = 84
        elif style == "hook":
            step = 0.5
            dur = 0.35
            jitter = 0.01
            vel0 = 96
        else:
            step = 0.95 if len(degs) <= 4 else 0.62
            dur = 0.55
            jitter = 0.015
            vel0 = 92

        if sec == "final" and style in ("motif", "hook", "longline") and bar % 2 == 0:
            degs = degs + [degs[0]] if len(degs) < 6 else degs

        out = []
        for i, d in enumerate(degs):
            if bar % 8 == 7 and i >= 3 and style not in ("run", "longline", "hook"):
                break
            oct = 0
            if sec in ("chorus", "final") and i == 0 and style in ("hook", "motif", "call"):
                oct = 12
            if style == "run" and sec in ("final", "chorus"):
                oct = 12 if i < 2 else 0
            pitch = scale[d % nscale] + oct
            out.append(
                {
                    "t": i * step + rng.uniform(-jitter, jitter),
                    "d": dur + (0.2 if i == 0 and style != "pluck" else 0),
                    "p": pitch,
                    "v": vel0 if i == 0 else 68 + rng.randint(0, 10),
                }
            )
        return out

    return lead


def _bed_builder(profile: Dict[str, Any]):
    roots = profile.get("roots") or [33, 33, 29, 29, 36, 36, 31, 31]
    bars = int(profile.get("bars") or 32)
    harm = (profile.get("harmony") or "minor_triad").lower()
    mode = (profile.get("mode") or "minor").lower()

    def chord_from_root(r: int) -> List[int]:
        if harm == "open5":
            return [r + 12, r + 19]
        if harm == "sus":
            return [r + 12, r + 17, r + 19]  # sus4
        if harm == "cluster":
            return [r + 12, r + 14, r + 15, r + 19]
        if harm == "add9":
            third = 16 if mode == "major" else 15
            return [r + 12, r + third, r + 19, r + 26]
        if harm == "major_triad" or mode == "major":
            return [r + 12, r + 16, r + 19]
        # minor_triad default
        return [r + 12, r + 15, r + 19]

    def bed(bar: int, rng: random.Random):
        r = roots[bar % len(roots)]
        sec = _section(bar, bars)
        ch = chord_from_root(r)
        if sec == "intro":
            v = 38 if harm in ("cluster", "open5") else 42
            if harm != "open5":
                ch = ch[:2]
        elif sec == "break":
            v = 36
            ch = [r + 12, r + 19]
        elif sec in ("chorus", "final"):
            v = 58 if harm == "cluster" else 60
            if harm in ("minor_triad", "major_triad") and bar % 2 == 0:
                ch = ch + [r + 22]
        elif sec == "outro":
            v = 34
        else:
            v = 50
        # staccato beds for plucky pop vs pads
        dur = 1.8 if harm in ("sus",) and sec == "verse" else 3.85
        if harm == "cluster":
            dur = 3.95
        return [{"t": 0.0, "d": dur, "p": p, "v": v} for p in ch]

    return bed


def _color_builder(profile: Dict[str, Any]):
    scale = profile.get("scale") or [57, 60, 62, 64, 67, 69, 72, 74]
    bars = int(profile.get("bars") or 32)
    style = (profile.get("lead_style") or "motif").lower()

    def color(bar: int, rng: random.Random):
        sec = _section(bar, bars)
        if sec in ("intro", "outro"):
            return []
        if style in ("sparse", "folk") and sec == "break":
            return []
        if sec == "verse" and bar % 8 != 7 and style not in ("pluck", "run"):
            return []
        if bar % 4 != 3 and sec not in ("chorus", "final", "build2") and style != "run":
            return []
        top = scale[-1] if scale else 84
        if style == "run":
            return [
                {"t": 0.5 + i * 0.25, "d": 0.12, "p": min(100, top + (i % 3) * 2), "v": 48}
                for i in range(6)
            ]
        if style == "folk":
            return [
                {"t": 2.0, "d": 0.4, "p": min(96, top), "v": 50},
                {"t": 3.0, "d": 0.5, "p": min(96, top - 5), "v": 46},
            ]
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
        "mode": profile.get("mode"),
        "bass_style": profile.get("bass_style"),
        "lead_style": profile.get("lead_style"),
        "harmony": profile.get("harmony"),
        "kick_pattern": profile.get("kick_pattern"),
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
