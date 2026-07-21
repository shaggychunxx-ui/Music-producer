from __future__ import annotations

from typing import Any

CONCEPTS: dict[str, dict[str, Any]] = {
    "mode": {
        "name": "Mode",
        "summary": (
            "An ordered series of intervals with respect to a starting note whose absolute "
            "pitch is not specified. Abstract relative pitch pattern (e.g. 1 2 b3 4 5 6 b7)."
        ),
    },
    "scale": {
        "name": "Scale",
        "summary": (
            "A mode realized from a named absolute starting pitch. Same mode + different "
            "starts = different scales (e.g. C Dorian vs A Dorian)."
        ),
    },
    "mode_vs_scale": {
        "name": "Mode vs scale",
        "summary": "Mode abstract; scale concrete. Confusing them is the #1 source of modal confusion.",
    },
    "modal_vs_tonal": {
        "name": "Modal vs tonal music",
        "summary": (
            "Modal traditions emphasize monody/finalis and modal cadences. Western polyphony "
            "shifted to tonal harmony; kept Ionian/Aeolian → major/minor (plus harmonic/melodic minor)."
        ),
    },
    "finalis": {
        "name": "Finalis / tone center",
        "summary": "Tonal centre; modal songs classically terminate on the finalis.",
    },
    "characteristic_modal_note": {
        "name": "Characteristic modal note",
        "summary": (
            "Second defining color tone (beyond maj/min third) that distinguishes modes "
            "within a quality group—critical for modal composition and chord choice."
        ),
        "examples": {
            "Dorian": "natural 6",
            "Phrygian": "b2",
            "Lydian": "#4",
            "Mixolydian": "b7",
            "Locrian": "b5",
        },
    },
    "improvisation_rule": {
        "name": "Improvisation rule (harmony first)",
        "summary": (
            "Over a chord progression, the progression—not the lead guitar fingering—"
            "primarily determines the mode/tonality. Mode is chosen largely at composition time."
        ),
    },
    "vamp": {
        "name": "Vamp",
        "summary": "Long static/repeated chord; freer modal color choices constrained by chord type.",
    },
    "group_i": {
        "name": "Group I modes",
        "summary": "Seven modes derived as rotations of the major scale (Ionian…Locrian).",
    },
    "group_ii": {
        "name": "Group II modes",
        "summary": "Modes related to harmonic minor (starting on successive degrees).",
    },
    "group_iii": {
        "name": "Group III / Bartók",
        "summary": "Melodic-minor-derived; document highlights Bartók mode (4th of melodic minor).",
    },
    "modulation": {
        "name": "Modulation",
        "summary": (
            "Change of key/tonality mid-piece. Document covers parent-key, adjacent-key, "
            "remote-key (via V/V7 of target), and inter-tonal exchanges."
        ),
    },
    "leading_tone": {
        "name": "Leading tone & tritone pull",
        "summary": (
            "In tonal major, degree 7 (leading tone) and 4 (subdominant) form a tritone "
            "driving V7→I resolution—central to remote modulation strategy."
        ),
    },
}


def define(term: str) -> dict[str, Any]:
    key = term.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "modes": "mode",
        "scales": "scale",
        "characteristic": "characteristic_modal_note",
        "character_note": "characteristic_modal_note",
        "tonal": "modal_vs_tonal",
        "modal": "modal_vs_tonal",
        "improv": "improvisation_rule",
        "improvisation": "improvisation_rule",
        "modulate": "modulation",
        "bartok": "group_iii",
    }
    key = aliases.get(key, key)
    if key not in CONCEPTS:
        for k, v in CONCEPTS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown concept '{term}'. Try: {', '.join(CONCEPTS)}")
    return CONCEPTS[key]
