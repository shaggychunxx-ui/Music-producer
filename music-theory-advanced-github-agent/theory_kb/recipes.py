from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "mode_from_chords": {
        "title": "Identify mode from a short progression",
        "steps": [
            "Write all chord tones forced by the harmony (e.g. C: C-E-G, F: F-A-C).",
            "Fill unspecified degrees consistently without accidental clashes.",
            "Compare resulting interval signature to mode tables (1 2 b3 …).",
            "Name mode from the tone center (finalis), not from a random fingering box.",
            "Improvise emphasizing characteristic modal notes.",
        ],
    },
    "vamp": {
        "title": "Modal colors over a vamp",
        "steps": [
            "Band holds one chord type for a long time.",
            "Match pool of modes compatible with that triad/7th quality.",
            "For minor triad: try Dorian (nat6), Aeolian (b6), Phrygian (b2) carefully.",
            "For major/7: try Ionian, Lydian (#4), Mixolydian (b7) by desired color.",
            "Stay diatonic; land phrases on characteristic notes and chord tones.",
        ],
    },
    "dorian_jam": {
        "title": "Write a Dorian groove",
        "steps": [
            "Pick finalis (e.g. D); use notes of parent major starting on degree 2 (C major → D Dorian).",
            "Feature natural 6 (B in D Dorian) vs Aeolian’s b6.",
            "Use i and IV7 (or bVII) colors from document harmony comparison.",
            "Avoid classical V7→i minor-key habits that force harmonic minor unless intended.",
            "Reference: Scarborough Fair Dorian sound.",
        ],
    },
    "phrygian_color": {
        "title": "Phrygian color phrases",
        "steps": [
            "Center on i; stress b2 neighbor tones.",
            "Try cadences revolving around bIImaj7 against i.",
            "Keep Spanish/Arabic flavor by oscillating b2–1 and b7–1 gestures.",
        ],
    },
    "lydian_bright": {
        "title": "Lydian major brightness",
        "steps": [
            "Major tonic with #4 instead of 4.",
            "Highlight #4 in melody; cadences using Imaj7 and vii7 (of Lydian set).",
            "Avoid flattening to Ionian by landing on natural 4 by accident.",
        ],
    },
    "mixo_dominant": {
        "title": "Mixolydian rock dominant",
        "steps": [
            "Major tonic with b7; treat I7 as home, not V7 needing resolution.",
            "Compare diatonic 7th chords to Ionian table (document C major vs C Mixolydian).",
            "Jam over static I7 or I–bVII–IV rock loops.",
        ],
    },
    "compose_modal": {
        "title": "Compose a short modal section",
        "steps": [
            "Choose mode + finalis.",
            "Identify characteristic modal note; prefer chords containing it.",
            "Write diatonic melody ending on finalis.",
            "Ban stock major perfect authentic cadences unless leaving the mode on purpose.",
            "Check that harmony does not force another mode’s signature notes.",
        ],
    },
    "modulate_remote": {
        "title": "Modulate to a remote key",
        "steps": [
            "Target new key’s V or V7 as pivot goal.",
            "May need secondary dominants / stepwise preparation of that V7.",
            "Resolve V7→I of destination; establish with melodic finalis.",
            "For relatives: shared notes make pivot easy—still assert new center clearly.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "identify": "mode_from_chords",
        "chords": "mode_from_chords",
        "dorian": "dorian_jam",
        "phrygian": "phrygian_color",
        "lydian": "lydian_bright",
        "mixolydian": "mixo_dominant",
        "mixo": "mixo_dominant",
        "compose": "compose_modal",
        "composition": "compose_modal",
        "modulation": "modulate_remote",
        "modulate": "modulate_remote",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
