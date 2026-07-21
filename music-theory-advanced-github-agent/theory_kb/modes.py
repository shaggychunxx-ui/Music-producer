"""Mode formulas from the Advanced document."""

from __future__ import annotations

from typing import Any

MODES: dict[str, dict[str, Any]] = {
    "ionian": {
        "name": "Ionian",
        "group": "I",
        "parent": "major scale degree 1",
        "degrees": ["1", "2", "3", "4", "5", "6", "7"],
        "quality": "major",
        "equals": "major scale",
        "character_notes": ["natural 4 (vs Lydian)", "major 7 (vs Mixolydian)"],
    },
    "dorian": {
        "name": "Dorian",
        "group": "I",
        "parent": "major scale degree 2",
        "degrees": ["1", "2", "b3", "4", "5", "6", "b7"],
        "quality": "minor",
        "character_notes": ["natural 6 (vs Aeolian b6)", "b7"],
        "examples": ["Scarborough Fair (Simon & Garfunkel) cited as typical Dorian sound"],
        "harmony_hint": (
            "Vs major on same root: i7, ii7, bIIImaj7, IV7, v7, vi7(b5), bVIImaj7 "
            "(document comparison table for D Dorian vs D major degrees)."
        ),
    },
    "phrygian": {
        "name": "Phrygian",
        "group": "I",
        "parent": "major scale degree 3",
        "degrees": ["1", "b2", "b3", "4", "5", "b6", "b7"],
        "quality": "minor",
        "character_notes": ["b2 (Arabic/Spanish-like color)"],
        "usage": "Colorful melodic mode; frequent cadences involving bII and i",
        "cadence_ideas": [
            "i / i / bIImaj7 / bIImaj7",
            "i / i / iv / bIImaj7",
            "i7 / bvii … (see document patterns)",
        ],
    },
    "lydian": {
        "name": "Lydian",
        "group": "I",
        "parent": "major scale degree 4",
        "degrees": ["1", "2", "3", "#4", "5", "6", "7"],
        "quality": "major",
        "character_notes": ["#4 (raised fourth)"],
        "cadence_ideas": [
            "Imaj7 (long) / vii7",
            "Imaj7 / iii7 / vii7",
        ],
    },
    "mixolydian": {
        "name": "Mixolydian",
        "group": "I",
        "parent": "major scale degree 5",
        "degrees": ["1", "2", "3", "4", "5", "6", "b7"],
        "quality": "major",
        "character_notes": ["b7 (dominant quality without full major leading tone)"],
        "harmony_hint": "C Mixolydian vs C major: tonic becomes C7-type world; compare diatonic 7th chords in document table.",
    },
    "aeolian": {
        "name": "Aeolian",
        "group": "I",
        "parent": "major scale degree 6",
        "degrees": ["1", "2", "b3", "4", "5", "b6", "b7"],
        "quality": "minor",
        "equals": "natural minor",
        "character_notes": ["b6 (vs Dorian natural 6)"],
    },
    "locrian": {
        "name": "Locrian",
        "group": "I",
        "parent": "major scale degree 7",
        "degrees": ["1", "b2", "b3", "4", "b5", "b6", "b7"],
        "quality": "minor / unstable (b5)",
        "character_notes": ["b5", "b2"],
        "usage": (
            "Darkest/strangest of Group I; absent from classical repertoire as home mode; "
            "handle carefully as tonic."
        ),
        "cadence_ideas": [
            "im7(b5) / bV5",
            "im7(b5) / biii7",
            "i(b5)5 / bii5 / bV5",
        ],
    },
    "harmonic_minor": {
        "name": "Harmonic minor (Group II parent)",
        "group": "II",
        "parent": "self",
        "degrees": ["1", "2", "b3", "4", "5", "b6", "7"],
        "quality": "minor with leading tone",
        "character_notes": ["raised 7 vs Aeolian"],
    },
    "altered_locrian": {
        "name": "Altered Locrian",
        "group": "II",
        "parent": "harmonic minor degree 2",
        "degrees": ["1", "b2", "b3", "4", "b5", "6", "b7"],
    },
    "altered_ionian": {
        "name": "Altered Ionian",
        "group": "II",
        "parent": "harmonic minor degree 3",
        "degrees": ["1", "2", "3", "4", "#5", "6", "7"],
    },
    "altered_dorian": {
        "name": "Altered Dorian",
        "group": "II",
        "parent": "harmonic minor degree 4",
        "degrees": ["1", "2", "b3", "#4", "5", "6", "b7"],
    },
    "altered_phrygian": {
        "name": "Altered Phrygian (Major Dominant Phrygian)",
        "group": "II",
        "parent": "harmonic minor degree 5",
        "degrees": ["1", "b2", "3", "4", "5", "b6", "b7"],
        "aliases": ["Major Dominant Phrygian"],
    },
    "altered_lydian": {
        "name": "Altered Lydian",
        "group": "II",
        "parent": "harmonic minor degree 6",
        "degrees": ["1", "#2", "3", "#4", "5", "6", "7"],
    },
    "altered_mixolydian": {
        "name": "Altered Mixolydian",
        "group": "II",
        "parent": "harmonic minor degree 7",
        "degrees": ["1", "b2", "b3", "b4", "b5", "b6", "bb7"],
        "note": "Spelling as in document table (highly altered).",
    },
    "bartok": {
        "name": "Bartók mode",
        "group": "III",
        "parent": "melodic minor degree 4",
        "degrees": ["1", "2", "3", "#4", "5", "6", "b7"],
        "usage": "East-European music; named after Béla Bartók; most notable melodic-minor mode in this doc.",
    },
}


def list_modes() -> list[str]:
    return list(MODES.keys())


def get_mode(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "major": "ionian",
        "natural_minor": "aeolian",
        "minor": "aeolian",
        "mixo": "mixolydian",
        "myxolydian": "mixolydian",
        "myxolyian": "altered_mixolydian",  # doc typo path
        "dominant_phrygian": "altered_phrygian",
        "major_dominant_phrygian": "altered_phrygian",
        "bartók": "bartok",
        "bela_bartok": "bartok",
        "harmonic": "harmonic_minor",
    }
    key = aliases.get(key, key)
    if key not in MODES:
        for k, v in MODES.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown mode '{name}'. Try: {', '.join(list_modes())}")
    return MODES[key]
