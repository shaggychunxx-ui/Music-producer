"""Chapter map of Fundamentals of Musical Composition."""

from __future__ import annotations

from typing import Any

CHAPTERS: dict[int, dict[str, Any]] = {
    1: {
        "number": 1,
        "roman": "I",
        "title": "The Concept of Form",
        "part": "I Construction of Themes",
        "topics": ["meanings of form", "logic and coherence", "subdivision", "practice forms", "musical blocks"],
        "key_points": [
            "Form as number of parts vs size/complexity vs dance character vs organic organization",
            "Logic, coherence, relationship; differentiate ideas by importance/function",
            "Memory limits → subdivision determines form",
            "Beginners: simple to complex; build phrases and motives first",
        ],
    },
    2: {
        "number": 2,
        "roman": "II",
        "title": "The Phrase",
        "part": "I",
        "topics": ["phrase as molecule", "breath length", "metrical flexibility", "harmony-based sketches"],
        "key_points": [
            "Ending like a comma; may contain motivic features",
            "Homophonic-harmonic music concentrates essential content in one voice",
            "Four-bar norm in simple metres; tempo alters phrase span",
            "Drill: many phrases over fixed harmony (e.g. tonic of F major)",
        ],
    },
    3: {
        "number": 3,
        "roman": "III",
        "title": "The Motive",
        "part": "I",
        "topics": ["germ of the idea", "intervals and rhythms", "variation required", "variation techniques"],
        "key_points": [
            "Memorable contour + inherent harmony",
            "Final impression depends on treatment/development, not primary form alone",
            "Repetition + variation overcomes monotony",
            "Systematic variation of rhythm, intervals, harmony; adapt melody",
        ],
    },
    4: {
        "number": 4,
        "roman": "IV",
        "title": "Connecting Motive-Forms",
        "part": "I",
        "topics": ["common content", "rhythmic similarity", "coherent harmony", "cadential analogy"],
        "key_points": [
            "Piece resembles a cadence; phrases are parts of it",
            "I–V–I can establish tonality; elaborate cadence often closes",
            "Harmony usually slower than melody",
        ],
    },
    5: {
        "number": 5,
        "roman": "V",
        "title": "Construction of Simple Themes (1) — Beginning the Sentence",
        "part": "I",
        "topics": ["parts of a piece", "variety vs comprehensibility", "repetition", "tonic/dominant forms"],
        "key_points": [
            "Parts differ in content, character, tonality, size, structure",
            "Control rapid variety via delimitation, subdivision, simple repetition",
            "Intelligibility needs repetition; pure repetition risks monotony",
            "Practice tonic form / dominant form harmonic schemes for sentence openings",
        ],
    },
    6: {
        "number": 6,
        "roman": "VI",
        "title": "Construction of Simple Themes (2) — Antecedent of the Period",
        "part": "I",
        "topics": ["period vs sentence", "antecedent", "caesura", "Beethoven period analysis"],
        "key_points": [
            "Period postpones immediate repetition",
            "Antecedent = phrase + more remote motive-forms",
            "Practice: 8 bars with caesura at m.4",
            "Beginning determines continuation",
        ],
    },
    7: {
        "number": 7,
        "roman": "VII",
        "title": "Construction of Simple Themes (3) — Consequent of the Period",
        "part": "I",
        "topics": ["consequent as repetition", "cadence contour", "rhythm", "Romantic periods"],
        "key_points": [
            "Consequent restores comprehensibility after contrast",
            "Melodic cadence contour and rhythmic design critical",
            "Examples 42–51",
        ],
    },
    8: {
        "number": 8,
        "roman": "VIII",
        "title": "Construction of Simple Themes (4) — Completion of the Sentence",
        "part": "I",
        "topics": ["development as driving force", "continuation patterns", "literature examples"],
        "key_points": [
            "Sentence higher than period: statement + immediate development",
            "Photograph-album metaphor of basic motive under changing circumstances",
            "Examples 52–61",
        ],
    },
    9: {
        "number": 9,
        "roman": "IX",
        "title": "The Accompaniment",
        "part": "I",
        "topics": [
            "functional accompaniment",
            "omissibility",
            "motive of accompaniment",
            "types",
            "voice leading",
            "bass",
            "instruments",
        ],
        "key_points": [
            "Complement not decoration",
            "Unaccompanied segments for contrast/transparency",
            "Examples 62–67",
        ],
    },
    10: {
        "number": 10,
        "roman": "X",
        "title": "Character and Mood",
        "part": "I",
        "topics": ["genre character", "dance distinctions"],
        "key_points": ["Means beyond formal labels (e.g. mazurka vs gavotte vs polka)"],
    },
    11: {
        "number": 11,
        "roman": "XI",
        "title": "Melody and Theme",
        "part": "I",
        "topics": ["vocal melody", "instrumental melody", "melody versus theme"],
        "key_points": [
            "Vocal singability as foundation of melodiousness",
            "Instrumental freer under control",
            "Examples 69–100",
        ],
    },
    12: {
        "number": 12,
        "roman": "XII",
        "title": "Advice for Self-Criticism",
        "part": "I",
        "topics": ["listen separately", "analyse motive features", "tentative drafts"],
        "key_points": ["Ear first; separate melody and harmony; know the basic motive"],
    },
    13: {
        "number": 13,
        "roman": "XIII",
        "title": "The Small Ternary Form",
        "part": "II Small Forms",
        "topics": ["A–B–A¹", "contrasting middle", "upbeat chord", "recapitulation"],
        "key_points": [
            "Overwhelming proportion of forms are three-part",
            "B contrasts (esp. harmonic region) but must cohere",
            "A¹ true or modified return",
            "Examples 101–107",
        ],
    },
    14: {
        "number": 14,
        "roman": "XIV",
        "title": "Uneven, Irregular and Asymmetrical Construction",
        "part": "II",
        "topics": ["irregular phrase lengths", "asymmetry consequences"],
        "key_points": ["Literature often departs from even norms; Examples 108–112"],
    },
    15: {
        "number": 15,
        "roman": "XV",
        "title": "The Minuet",
        "part": "II",
        "topics": ["minuet form", "trio", "recapitulation habits"],
        "key_points": [
            "Independent or middle movement of cyclic forms",
            "Recapitulation seldom far-reaching in contour change",
            "Examples 113–119",
        ],
    },
    16: {
        "number": 16,
        "roman": "XVI",
        "title": "The Scherzo",
        "part": "II",
        "topics": [
            "A-section",
            "modulatory contrasting middle",
            "practice form",
            "extensions/episodes/codettas",
            "coda",
            "trio",
        ],
        "key_points": [
            "Playful/humorous; commonly 3/4; post-Beethoven replaces/alongside minuet",
            "More elaborate middle and codettas/liquidation than simple ternary",
            "Examples 120–123",
        ],
    },
    17: {
        "number": 17,
        "roman": "XVII",
        "title": "Theme and Variations",
        "part": "II",
        "topics": [
            "theme constitution",
            "theme–variation relation",
            "motive of variation",
            "elaboration",
            "counterpoint",
            "set organization",
        ],
        "key_points": [
            "Theme usually binary or ternary skeleton",
            "Each variation has a motive of variation applied to the theme’s structure",
            "Far-reaching modification allowed if coherence and style consistency hold",
            "Examples 124–127",
        ],
    },
    18: {
        "number": 18,
        "roman": "XVIII",
        "title": "The Parts of Larger Forms (Subsidiary Formulations)",
        "part": "III Large Forms",
        "topics": [
            "transition (independent vs evolving)",
            "retransition",
            "subordinate theme group",
            "lyric theme",
            "coda",
        ],
        "key_points": [
            "Transitions connect principal and subordinate material",
            "Retransition prepares return",
            "Subordinate group may include lyric theme",
            "Coda liquidates obligations / re-establishes tonic region",
        ],
    },
    19: {
        "number": 19,
        "roman": "XIX",
        "title": "The Rondo Forms",
        "part": "III",
        "topics": [
            "Andante forms ABA / ABAB",
            "simple rondos",
            "recap changes",
            "large rondo ABA–C–ABA",
            "sonata-rondo",
        ],
        "key_points": [
            "Repetition of theme(s) separated by intervening contrasts",
            "Large C-section may resemble trio or sonata elaboration",
            "Sonata-rondo blends rondo returns with developmental procedures",
        ],
    },
    20: {
        "number": 20,
        "roman": "XX",
        "title": "The Sonata-Allegro (First-Movement Form)",
        "part": "III",
        "topics": [
            "exposition",
            "principal theme/group",
            "transition",
            "subordinate group",
            "elaboration (Durchfuhrung)",
            "retransition",
            "recapitulation",
            "coda",
        ],
        "key_points": [
            "Essentially ternary at large scale: exposition – elaboration – recapitulation",
            "Exposition: principal group, transition, subordinate group (tonal contrast)",
            "Elaboration develops motives; retransition prepares return",
            "Recapitulation adapts material for new formal function (esp. subordinate group in tonic)",
            "Coda closes; literature illustrations throughout Beethoven",
        ],
    },
}


def list_chapters() -> list[str]:
    return [f"{c['number']}. {c['title']}" for c in CHAPTERS.values()]


def get_chapter(ref: str | int) -> dict[str, Any]:
    if isinstance(ref, int) or (isinstance(ref, str) and ref.isdigit()):
        n = int(ref)
        if n not in CHAPTERS:
            raise KeyError(f"Chapter {n} not found (1–20)")
        return CHAPTERS[n]
    q = str(ref).strip().lower()
    for c in CHAPTERS.values():
        if q in c["title"].lower() or q == c["roman"].lower():
            return c
    # keyword
    for c in CHAPTERS.values():
        if any(q in t for t in c["topics"]) or q in c["title"].lower():
            return c
    raise KeyError(f"No chapter match for '{ref}'. Try 1–20 or a title keyword.")
