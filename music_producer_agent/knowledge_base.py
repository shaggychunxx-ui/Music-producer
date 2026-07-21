"""Domain knowledge base backing the Music Producer Agent's responses.

Each entry maps a topic to a list of keywords used for matching plus the
expert advice text returned when the topic is triggered.
"""

from typing import Dict, List, TypedDict


class Topic(TypedDict):
    keywords: List[str]
    advice: str


KNOWLEDGE_BASE: Dict[str, Topic] = {
    "chord_progression": {
        "keywords": ["chord", "chords", "progression", "harmony"],
        "advice": (
            "For a solid chord progression, start with a strong tonal center "
            "and lean on functional harmony: try I-V-vi-IV for an uplifting pop "
            "feel, or vi-IV-I-V for something more introspective. In minor keys, "
            "i-VI-III-VII gives a cinematic, emotional pull. Add tension with "
            "secondary dominants or borrowed chords (e.g. a bVII or iv) right "
            "before a chorus to make the release feel bigger."
        ),
    },
    "melody": {
        "keywords": ["melody", "melodies", "hook", "topline"],
        "advice": (
            "Great melodies balance repetition and surprise. Anchor your hook "
            "around a memorable rhythmic motif, repeat it with small variations, "
            "and reserve your widest interval leap for the emotional peak of the "
            "phrase. Keep verse melodies narrower in range than the chorus so "
            "the chorus feels like a lift."
        ),
    },
    "arrangement": {
        "keywords": ["arrangement", "arrange", "structure", "song structure", "instrumentation"],
        "advice": (
            "Think of arrangement as controlling energy over time. A common pop "
            "structure is Intro-Verse-PreChorus-Chorus-Verse-PreChorus-Chorus-"
            "Bridge-Chorus. Strip elements out at the start of each section and "
            "reintroduce them to create movement, and always leave one element "
            "in reserve so the final chorus can go bigger than the rest."
        ),
    },
    "mixing": {
        "keywords": ["mix", "mixing", "eq", "compression", "compressor", "balance"],
        "advice": (
            "Start a mix with levels and panning before touching EQ or "
            "compression. Carve space with subtractive EQ to avoid frequency "
            "masking (e.g. cut mud around 200-400 Hz on competing elements), "
            "use compression to control dynamics rather than just add loudness, "
            "and reference your mix against a commercial track in the same "
            "genre at matched volume."
        ),
    },
    "mastering": {
        "keywords": ["master", "mastering", "loudness", "lufs"],
        "advice": (
            "Mastering should enhance, not fix, a mix. Aim for a target loudness "
            "appropriate to the platform (around -14 LUFS integrated for "
            "streaming), use gentle multiband compression and a limiter for "
            "peak control, and always A/B against reference tracks at matched "
            "loudness so you're judging tone, not volume."
        ),
    },
    "genre": {
        "keywords": ["genre", "style", "hip-hop", "hip hop", "edm", "electronic", "rock", "pop", "film score", "orchestral"],
        "advice": (
            "Every genre has its own sonic fingerprint: hip-hop leans on punchy "
            "drums and sub-heavy 808s, EDM thrives on build-drop tension and "
            "sidechained pads, rock favors live-feeling drums and guitar "
            "layering, and film scoring is about serving the picture with "
            "thematic motifs and dynamic range. Tell me the genre you're "
            "targeting and I can get more specific."
        ),
    },
    "collaboration": {
        "keywords": ["collaborate", "collaboration", "feedback", "artist", "session"],
        "advice": (
            "When collaborating, set a clear creative direction before the "
            "session starts (references, tempo, key, mood), keep sessions "
            "organized so ideas aren't lost, and give feedback on the artist's "
            "performance in terms of feel and emotion first, technical details "
            "second."
        ),
    },
}


def find_topic(message: str) -> str | None:
    """Return the first topic key whose keywords appear in the message."""
    lowered = message.lower()
    for topic, data in KNOWLEDGE_BASE.items():
        if any(keyword in lowered for keyword in data["keywords"]):
            return topic
    return None
