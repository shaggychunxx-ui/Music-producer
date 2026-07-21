"""Composition practice exercises derived from the book’s method."""

from __future__ import annotations

from typing import Any

EXERCISES: dict[str, dict[str, Any]] = {
    "phrase_sketches": {
        "title": "Phrase sketches on fixed harmony",
        "chapter": 2,
        "goal": "Coordinate melody, rhythm, and harmony until invention becomes fluent.",
        "steps": [
            "Choose a single harmony (e.g. F major tonic triad) as in Schoenberg’s early drills.",
            "Invent many different contours using only chord tones (then add passing tones).",
            "Aim for phrase endings that feel like commas—not full stops every time.",
            "Vary length slightly around ~4 bars without losing breath-unit completeness.",
            "Play melodies without accompaniment to check smoothness and balance.",
        ],
    },
    "motive_variations": {
        "title": "Build a catalog of motive-forms",
        "chapter": 3,
        "goal": "Keep basic shape while varying rhythm, intervals, and harmony.",
        "steps": [
            "Invent a short basic motive (2–4 notes) with clear rhythm and contour.",
            "Produce at least 8 motive-forms using the variation lists (rhythm / interval / harmony).",
            "Reject variants that change everything (foreign shapes).",
            "Label each variant with the technique used.",
        ],
    },
    "connect_forms": {
        "title": "Connect motive-forms into phrases",
        "chapter": 4,
        "goal": "Common content + rhythmic similarity + coherent harmony.",
        "steps": [
            "Select 3–4 motive-forms from one basic motive.",
            "Combine into a phrase over a simple I–V–I or expanded cadence.",
            "Keep harmony slower than melody (several notes per chord).",
            "Check that the phrase feels like a part of a larger cadence.",
        ],
    },
    "sentence": {
        "title": "Write a sentence opening + completion",
        "chapters": [5, 8],
        "goal": "Statement that immediately begins development.",
        "steps": [
            "Compose a presentation phrase on tonic form harmony (e.g. I then V, or I–V–I).",
            "Answer with dominant form (e.g. V–I or V–I–V), adjusting melody only as needed.",
            "Continue with developmental combination of prior motive-forms.",
            "Cadence clearly; optionally liquidate near the end.",
            "Compare with leading themes of Beethoven sonatas for pacing.",
        ],
    },
    "period": {
        "title": "Practice-form period (8 bars)",
        "chapters": [6, 7],
        "goal": "Antecedent contrast then consequent as repetition-type response.",
        "steps": [
            "Write a 4-bar antecedent: opening motive + more remote forms; caesura at m.4.",
            "Write a 4-bar consequent that restates/repeats the antecedent’s structure with variation.",
            "Make the final cadence more conclusive than the mid-caesura.",
            "Analyse a Beethoven period afterward to compare.",
        ],
    },
    "accompaniment": {
        "title": "Functional accompaniment",
        "chapter": 9,
        "goal": "Complement, not decorate.",
        "steps": [
            "Take a melody that implies clear harmony.",
            "Write an accompaniment that clarifies tonality, supports rhythm, and matches character.",
            "Design a short ‘motive of the accompaniment’ that can be varied.",
            "Leave one phrase unaccompanied for transparency; compare effect.",
            "Check voice leading and bass as a coherent line.",
        ],
    },
    "small_ternary": {
        "title": "Small ternary A–B–A¹",
        "chapter": 13,
        "goal": "Coherent harmonic contrast + return.",
        "steps": [
            "A: 8–16 bars establishing tonic (sentence or period).",
            "B: contrast primarily by region (closely related); keep motive kinship.",
            "A¹: return with controlled variation; prepare with an upbeat chord if useful.",
            "Ensure contrast is not incoherent collage.",
        ],
    },
    "minuet": {
        "title": "Minuet + trio sketch",
        "chapter": 15,
        "goal": "Dance character + balanced return.",
        "steps": [
            "Write a minuet A–B–A¹ with clear metre/tempo character.",
            "Trio in contrasting but related region/texture.",
            "Da capo (or written return) of minuet; avoid extreme contour rewriting of A¹.",
        ],
    },
    "scherzo": {
        "title": "Scherzo practice form",
        "chapter": 16,
        "goal": "Modulatory middle + codettas/liquidation.",
        "steps": [
            "Energetic A-section in scherzo character.",
            "Modulatory contrasting middle with clear segments and return path to tonic.",
            "Recapitulation; add extension/codetta that liquidates motive features.",
            "Optional short coda and trio.",
        ],
    },
    "variations": {
        "title": "Theme and three variations",
        "chapter": 17,
        "goal": "One theme skeleton; distinct motive of variation each time.",
        "steps": [
            "Compose a clear binary or ternary theme with simple harmonic plan.",
            "Variation 1: rhythmic motive of variation.",
            "Variation 2: figuration / register / texture change.",
            "Variation 3: mode or character change while skeleton remains audible.",
            "Keep piano (or chosen medium) style consistent inside each variation.",
        ],
    },
    "sonata_exposition": {
        "title": "Sonata exposition sketch",
        "chapters": [18, 20],
        "goal": "Principal group – transition – subordinate group.",
        "steps": [
            "Principal theme (sentence preferred) in tonic.",
            "Transition: either independent theme or evolving from principal material; prepare new key.",
            "Subordinate group with character contrast (optional lyric theme).",
            "Close exposition with cadence/codetta in the new region.",
            "Outline only the Durchfuhrung plan: which motives, which regions, retransition to V.",
        ],
    },
    "self_criticism": {
        "title": "Self-criticism protocol",
        "chapter": 12,
        "goal": "Diagnose weak melody vs weak harmony.",
        "steps": [
            "Play/read melody alone; mark unsingable leaps or unbalanced contour.",
            "Play/read harmony alone; check progression logic and cadences.",
            "Name the basic motive and list which features survived in weak bars.",
            "Rewrite only the failing factor first, then recombine.",
        ],
    },
}


def get_exercise(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "phrases": "phrase_sketches",
        "phrase": "phrase_sketches",
        "motive": "motive_variations",
        "motives": "motive_variations",
        "connect": "connect_forms",
        "ternary": "small_ternary",
        "aba": "small_ternary",
        "theme_variations": "variations",
        "variation": "variations",
        "exposition": "sonata_exposition",
        "sonata": "sonata_exposition",
        "critique": "self_criticism",
        "criticism": "self_criticism",
    }
    key = aliases.get(key, key)
    if key not in EXERCISES:
        raise KeyError(f"Unknown exercise '{name}'. Try: {', '.join(EXERCISES)}")
    return EXERCISES[key]
