"""Core concepts transcribed from the manual."""

from __future__ import annotations

from typing import Any

CONCEPTS: dict[str, dict[str, Any]] = {
    "form": {
        "name": "Form (concept)",
        "chapter": 1,
        "summary": (
            "Form is used for number of parts (binary/ternary/rondo), size/complexity "
            "(sonata), dance character (minuet/scherzo), and aesthetically as organization "
            "like a living organism."
        ),
        "requirements": ["logic", "coherence", "relationship", "differentiation by function", "comprehensible subdivision"],
        "practice": (
            "Beginners cannot see the whole like Michelangelo’s Moses; build blocks "
            "(phrases, motives) and connect them with simplified practice forms."
        ),
        "quotes_paraphrase": [
            "Without organization music would be an amorphous mass, as unintelligible as an essay without punctuation.",
            "One can comprehend only what one can keep in mind.",
        ],
    },
    "phrase": {
        "name": "Phrase",
        "chapter": 2,
        "summary": (
            "Smallest structural unit: a musical molecule of integrated events with "
            "completeness, combinable with similar units. Ending suggests a comma. "
            "Approximates what one could sing in a single breath."
        ),
        "length": (
            "In simple metres, four measures is normal; slow tempos may shrink to half a "
            "measure; rapid tempos may need eight or more. Seldom exact multiple of bar; "
            "usually crosses metric subdivisions."
        ),
        "practice": (
            "Sketch many phrases on a predetermined harmony (e.g. tonic of F major) to "
            "coordinate melody, rhythm, and harmony until fluency appears."
        ),
        "related": ["motive", "sentence", "period"],
    },
    "motive": {
        "name": "Motive",
        "chapter": 3,
        "summary": (
            "Features are intervals and rhythms combined into a memorable contour that "
            "usually implies inherent harmony. Basic motive is the germ of the idea; "
            "appears characteristically at the opening; related to almost every figure."
        ),
        "metaphors": [
            "smallest common multiple (elements of later figures)",
            "greatest common factor (included in every subsequent figure)",
        ],
        "central_rule": (
            "Use of the motive requires variation. Changing every feature produces the "
            "foreign and incoherent; change some features while preserving the basic shape."
        ),
        "variation_rhythm": [
            "modify note lengths",
            "note repetitions",
            "repetition of certain rhythms",
            "shift rhythms to different beats",
            "addition of upbeats",
            "change of metre (seldom within a piece)",
        ],
        "variation_intervals": [
            "change order or direction of notes",
            "addition or omission of intervals",
            "fill intervals with ancillary notes",
            "reduction through omission or condensation",
            "repetition of features",
            "shift features to other beats",
        ],
        "variation_harmony": [
            "inversions",
            "additions at the end",
            "insertions in the middle",
            "substitute different chord or succession",
        ],
        "melody_adaptation": ["transposition", "addition of passage-work", "contour adjusted to new harmony"],
        "related": ["motive-form", "phrase", "liquidation"],
    },
    "motive-form": {
        "name": "Motive-form",
        "chapter": 3,
        "summary": "A derived shape produced by controlled variation of the basic motive.",
        "related": ["motive", "sentence", "period"],
    },
    "connecting_motive_forms": {
        "name": "Connecting motive-forms",
        "chapter": 4,
        "summary": (
            "Mechanics of combination: common content (shared basic motive), rhythmic "
            "similarities, coherent harmony. A piece generally resembles a cadence of which "
            "each phrase is a part."
        ),
        "harmony_notes": [
            "Simple I–V–I can express tonality if not contradicted",
            "Usually concluded with more elaborate cadence in traditional music",
            "Harmony ordinarily moves more slowly than melody",
        ],
    },
    "sentence": {
        "name": "Sentence",
        "chapters": [5, 8],
        "summary": (
            "Higher form of construction than the period: states an idea and at once starts "
            "a kind of development—showing forethought. Much used in leading themes of "
            "sonatas/symphonies; also applicable to smaller forms."
        ),
        "opening": (
            "Begin with a phrase and its immediate continuation/repetition (often tonic form "
            "then dominant form), then complete with continuation that develops motive-forms."
        ),
        "harmonic_practice_forms": {
            "tonic_form_examples": ["I only then V only", "I–V", "I–V–I", "I–IV"],
            "dominant_form_examples": ["V only then I only", "V–I", "V–I–V"],
            "note": "V–I ending preferred for clear tonality; useful even when tonic form used III, I–VI, I–III.",
        },
        "album_metaphor": (
            "A piece resembles a photograph album of the basic idea under changing "
            "circumstances; order of motive-forms is conditioned by comprehensibility and logic."
        ),
        "related": ["period", "motive", "tonic_form", "dominant_form"],
    },
    "period": {
        "name": "Period",
        "chapters": [6, 7],
        "summary": (
            "Differs from the sentence by postponing repetition. First phrase is not repeated "
            "immediately but united with more remote (contrasting) motive-forms to form the "
            "antecedent; consequent is a kind of repetition of the antecedent."
        ),
        "practice_form": "Eight measures: 4-bar antecedent + 4-bar consequent; caesura in m.4 (comma/semicolon).",
        "usage_note": (
            "Only a small percentage of classical themes are periods; Romantic composers use "
            "them still less—but writing periods trains many techniques."
        ),
        "antecedent": "Construction of beginning determines continuation; analysis of Beethoven periods recommended.",
        "consequent": "Melodic cadence contour + rhythmic considerations; often fuller close than antecedent.",
        "related": ["sentence", "phrase", "caesura"],
    },
    "accompaniment": {
        "name": "Accompaniment",
        "chapter": 9,
        "summary": (
            "Should not be mere addition; functional complement to tonality, rhythm, phrasing, "
            "contour, character, mood; reveals inherent harmony; unifies motion; fits the instrument."
        ),
        "when_needed": "Imperative if harmony or rhythm is complicated; powerful in descriptive music.",
        "omissibility": (
            "Unaccompanied music exists (folk, church, solo sonatas); unaccompanied segments "
            "can supply contrast and transparency even inside accompanied works."
        ),
        "topics": [
            "motive of the accompaniment",
            "types of accompaniment",
            "voice leading",
            "bass line treatment",
            "instrument requirements",
        ],
    },
    "character_mood": {
        "name": "Character and mood",
        "chapter": 10,
        "summary": (
            "Character/mood distinguish genres (e.g. mazurka vs gavotte vs polka) via metre, "
            "tempo, rhythm, articulation, harmony, and motive types—not only formal schema."
        ),
    },
    "melody": {
        "name": "Melody and theme",
        "chapter": 11,
        "summary": (
            "Concentrating the main idea in one line needs special balance. Vocal limits "
            "define ‘singable/melodious’; instrumental melody freer but should still be controlled. "
            "Theme is a formal unit; not every melody is a theme."
        ),
        "vocal": "Start from vocal restrictions for sounder melodiousness.",
        "instrumental": "More freedom; still organized by motive, contour, and harmonic implication.",
    },
    "self_criticism": {
        "name": "Self-criticism",
        "chapter": 12,
        "summary": "Even masters stray; ear is the best tool; technical advice often negative (what to avoid).",
        "steps": [
            "LISTEN: play/read harmony and melody separately several times",
            "ANALYSE: be conscious of significant features of the basic motive",
            "Treat drafts as tentative until mature technique",
            "Find where/why the error and which track is right",
        ],
    },
    "liquidation": {
        "name": "Liquidation",
        "summary": (
            "Progressive reduction of distinctive motive features toward simpler, more generic "
            "material (scales, repeated notes, cadential formulas)—used near section ends, "
            "codettas, transitions, and before structural arrivals."
        ),
        "related": ["codetta", "transition", "coda", "scherzo"],
    },
    "contrast": {
        "name": "Contrast",
        "summary": (
            "Contrast produces variety and avoids monotony of pure repetition, but must remain "
            "coherent—using the same connecting processes as motive-forms. Incoherent contrast "
            "tolerated only in some descriptive music."
        ),
        "harmonic": "Most effective middle-section contrast is often a new closely related region.",
    },
    "repetition": {
        "name": "Repetition",
        "summary": (
            "Intelligibility seems impossible without repetition; pure unvaried repetition risks "
            "monotony—hence variation. Recapitulation satisfies desire to hear again what pleased."
        ),
    },
}


def define(term: str) -> dict[str, Any]:
    key = term.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "form": "form",
        "phrase": "phrase",
        "motive": "motive",
        "motif": "motive",
        "motive_form": "motive-form",
        "motiveform": "motive-form",
        "sentence": "sentence",
        "period": "period",
        "antecedent": "period",
        "consequent": "period",
        "accompaniment": "accompaniment",
        "melody": "melody",
        "theme": "melody",
        "self_criticism": "self_criticism",
        "criticism": "self_criticism",
        "liquidation": "liquidation",
        "contrast": "contrast",
        "repetition": "repetition",
        "connecting": "connecting_motive_forms",
        "connexion": "connecting_motive_forms",
        "character": "character_mood",
        "mood": "character_mood",
    }
    key = aliases.get(key, key)
    if key not in CONCEPTS:
        # fuzzy
        for k, v in CONCEPTS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown concept '{term}'. Try: {', '.join(CONCEPTS)}")
    return CONCEPTS[key]
