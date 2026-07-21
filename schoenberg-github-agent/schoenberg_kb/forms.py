"""Formal types and analysis templates."""

from __future__ import annotations

from typing import Any

FORMS: dict[str, dict[str, Any]] = {
    "phrase": {
        "name": "Phrase",
        "level": "micro",
        "schema": "integrated events → comma-like close",
        "typical_length": "~1 breath; often ~4 bars simple metre",
    },
    "sentence": {
        "name": "Sentence",
        "level": "theme",
        "schema": "presentation (statement + immediate continuation) → development/continuation → cadence",
        "notes": "Higher than period; starts development at once; leading themes of sonatas/symphonies",
        "practice": "Tonic form then dominant form openings; complete with developmental continuation",
    },
    "period": {
        "name": "Period",
        "level": "theme",
        "schema": "antecedent (phrase + remote forms) | caesura | consequent (repetition-like)",
        "practice_form": "8 bars = 4 + 4",
        "notes": "Postpones repetition; rarer as pure type in literature but excellent drill",
    },
    "small_ternary": {
        "name": "Small Ternary (A–B–A¹)",
        "level": "small form",
        "schema": "A (tonic statement) – B (contrast, often new region) – A¹ (return, often varied)",
        "notes": "Also called three-part song form historically; foundation of many larger forms",
    },
    "minuet": {
        "name": "Minuet",
        "level": "small form / movement",
        "schema": "Minuet (ternary-like) + Trio + (da capo) Minuet",
        "notes": "Dance metre/tempo/rhythm identify character; independent or cyclic middle movement",
    },
    "scherzo": {
        "name": "Scherzo",
        "level": "small form / movement",
        "schema": "A – modulatory contrasting middle – A¹ (+ extensions/codettas/coda) + Trio",
        "notes": "Playful; commonly 3/4; more developmental middle than simple minuet",
    },
    "theme_and_variations": {
        "name": "Theme and Variations",
        "level": "set form",
        "schema": "Theme (binary/ternary skeleton) + Variation1…n (each with motive of variation)",
        "notes": "Preserve structural skeleton; modify melody/rhythm/harmony/texture; organize set for contrast",
    },
    "rondo_simple": {
        "name": "Simple Rondo / Andante forms",
        "level": "large-ish",
        "schemas": ["ABA", "ABAB", "other simple refrain patterns"],
        "notes": "Repetition of principal theme(s) separated by contrasts",
    },
    "rondo_large": {
        "name": "Large Rondo",
        "level": "large",
        "schema": "ABA – C – ABA",
        "notes": "C-section longer/elaborate—like trio or sonata elaboration",
    },
    "sonata_rondo": {
        "name": "Sonata-Rondo",
        "level": "large",
        "schema": "rondo returns + developmental / sonata-like procedures",
        "notes": "Hybrid of refrain structure and sonata developmental logic",
    },
    "sonata_allegro": {
        "name": "Sonata-Allegro (first-movement form)",
        "level": "large",
        "schema": {
            "exposition": ["Principal theme/group", "Transition", "Subordinate group"],
            "elaboration": ["Durchfuhrung / development", "Retransition"],
            "recapitulation": ["Principal material", "Adapted subordinate group (tonic)", "Coda"],
        },
        "notes": "Essentially ternary at the large scale; tonal contrast then resolution",
        "subsidiary": ["independent transition theme", "transition evolving from previous", "lyric theme", "coda"],
    },
}


def get_form(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "ternary": "small_ternary",
        "aba": "small_ternary",
        "three_part": "small_ternary",
        "song_form": "small_ternary",
        "variations": "theme_and_variations",
        "theme_variations": "theme_and_variations",
        "rondo": "rondo_simple",
        "andante": "rondo_simple",
        "sonata": "sonata_allegro",
        "sonata_form": "sonata_allegro",
        "first_movement": "sonata_allegro",
        "durchfuhrung": "sonata_allegro",
        "development": "sonata_allegro",
    }
    key = aliases.get(key, key)
    if key not in FORMS:
        for k, v in FORMS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown form '{name}'. Try: {', '.join(FORMS)}")
    return FORMS[key]


def analysis_plan(context: str) -> dict[str, Any]:
    """Generic analysis plan for a passage or movement description."""
    return {
        "context": context,
        "steps": [
            "1. Locate phrases and caesuras; estimate phrase lengths.",
            "2. Extract the basic motive (interval set + rhythm + implied harmony).",
            "3. List motive-forms and name variation operations (rhythm/interval/harmony).",
            "4. Decide sentence vs period vs freer theme construction.",
            "5. Identify form level: small ternary / dance form / rondo / sonata-allegro.",
            "6. Chart harmonic regions (tonic establishment vs contrasting region).",
            "7. Mark functional sections: transition, retransition, codetta, coda, liquidation.",
            "8. Evaluate coherence of contrasts and balance of repetition vs variety.",
            "9. Self-criticism: listen to melody alone and harmony alone.",
        ],
        "form_candidates": list(FORMS.keys()),
    }
