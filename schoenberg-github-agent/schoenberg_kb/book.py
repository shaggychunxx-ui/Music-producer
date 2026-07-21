"""Book metadata, glossary, pedagogical framing."""

from __future__ import annotations

BOOK = {
    "title": "Fundamentals of Musical Composition",
    "author": "Arnold Schoenberg",
    "editors": ["Gerald Strang", "Leonard Stein (collaboration)"],
    "first_published": 1967,
    "edition_note": "Faber paperback edition 1970; ISBN 0 571 09276 4",
    "copyright": "Estate of Gertrude Schoenberg, 1967",
    "publisher": "Faber and Faber Limited, London / Boston",
    "origin": (
        "Grew from Schoenberg’s analysis and composition teaching at USC and UCLA; "
        "work intermittent 1937–1948; text largely through four revisions by his death; "
        "Strang reconciled versions for publication."
    ),
    "related_works": [
        {
            "title": "Structural Functions of Harmony",
            "role": "Companion theory; amplifies progression purposes for composition",
        },
        {
            "title": "Preliminary Exercises in Counterpoint",
            "role": "Parallel large textbook on counterpoint practice",
        },
        {
            "title": "Models for Beginners in Composition",
            "year": 1942,
            "role": "Syllabus enlarged by Fundamentals",
        },
        {
            "title": "Harmonielehre / Theory of Harmony",
            "role": "Earlier harmony pedagogy (1911 / English abridgment)",
        },
    ],
    "method": [
        "Analysis of masterworks (special emphasis: Beethoven piano sonatas)",
        "Practice writing musical forms, small and large",
    ],
    "audience": (
        "Average university student and the talented student who might become a composer; "
        "technical matters discussed in a very fundamental way."
    ),
    "aesthetic_essentials": [
        "clarity of statement",
        "contrast",
        "repetition",
        "balance",
        "variation",
        "elaboration",
        "proportion",
        "connexion",
        "transition",
    ],
    "historical_scope": (
        "Little reference to music after 1900; student encouraged to use resources available "
        "up to that time; principles apply across styles and contemporary materials."
    ),
    "source_urls": [
        "https://monoskop.org/images/d/da/Schoenberg_Arnold_Fundamentals_of_Musical_Composition_no_OCR.pdf",
    ],
    "parts": [
        {"id": "I", "title": "Construction of Themes", "chapters": list(range(1, 13))},
        {"id": "II", "title": "Small Forms", "chapters": list(range(13, 18))},
        {"id": "III", "title": "Large Forms", "chapters": list(range(18, 21))},
    ],
}

GLOSSARY = {
    # Book’s own US ↔ British glossary (p. glossary)
    "whole note": "semibreve",
    "half note": "minim",
    "quarter note": "crotchet",
    "eighth note": "quaver",
    "tone": "note (pitch)",
    "tonality": "key",
    "degree": "scale degree / chord built on a degree (e.g. V, vii)",
    "measure": "bar",
    "voice-leading": "part-writing",
    "authentic cadence": "perfect cadence",
    "deceptive cadence": "interrupted cadence",
    # Schoenberg compositional terms
    "motive": "Intervals + rhythms forming a memorable contour; germ of the idea",
    "motive-form": "A varied form of the basic motive",
    "phrase": "Smallest structural unit; ~single breath; comma-like close",
    "sentence": "Theme type that states and immediately develops",
    "period": "Antecedent + consequent; repetition postponed after contrast",
    "liquidation": "Reducing characteristic features toward generic cadential material",
    "Durchfuhrung": "Elaboration / development section (sonata)",
    "practice form": "Simplified pedagogical form for student writing",
    "codetta": "Small closing unit; often liquidates motives",
    "retransition": "Return path to recapitulation / principal theme",
}

PEDAGOGY = {
    "order": [
        "Concept of form & musical blocks",
        "Phrase sketches on fixed harmony",
        "Motive invention & variation",
        "Connecting motive-forms",
        "Sentence openings (tonic/dominant forms)",
        "Period (antecedent → consequent)",
        "Complete sentence",
        "Accompaniment as function",
        "Character, mood, melody vs theme",
        "Self-criticism",
        "Small ternary → minuet → scherzo → variations",
        "Transitions, rondo types, sonata-allegro",
    ],
    "analysis_checklist": [
        "Identify basic motive (intervals + rhythm + implied harmony)",
        "Catalog motive-forms and variation techniques used",
        "Map phrases and caesuras",
        "Classify theme as sentence, period, or freer construction",
        "Name form (ternary, minuet, scherzo, rondo type, sonata…)",
        "Track harmonic regions (tonic vs contrasting region)",
        "Locate transition / retransition / coda functions",
        "Note liquidation near cadences and section ends",
    ],
    "practice_principles": [
        "Intelligibility requires repetition; monotony requires variation",
        "Variety must never endanger comprehensibility",
        "Rapid tempo ⇒ less rapid variety",
        "Control variety via delimitation, subdivision, simple repetition",
        "Beginning construction determines continuation",
        "Contrast must remain coherent (same connecting processes as motive-forms)",
    ],
}
