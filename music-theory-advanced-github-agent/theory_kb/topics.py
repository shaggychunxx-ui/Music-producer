from __future__ import annotations

from typing import Any

TOPICS: dict[str, dict[str, Any]] = {
    "defining_modes": {
        "name": "Defining modes",
        "pages": "4–8",
        "summary": (
            "Definition by intervals from 1 or by step pattern (W/H). Mode ≠ scale. "
            "History: Gregorian names mixed vs ancient Greek. Tables for Groups I–III."
        ),
    },
    "improvisation": {
        "name": "Using modes for improvisation",
        "pages": "9–15",
        "summary": (
            "Monody→polyphony shifted power to chords. Lead pattern rarely changes mode. "
            "Choose modes that fit chord tones; extract implied scale from progression; "
            "vamps allow static-chord mode colors."
        ),
        "method": [
            "List chord tones forced by harmony",
            "Fill remaining degrees consistently",
            "Match resulting signature to a mode",
            "Improvise diatonically emphasizing characteristic notes",
        ],
    },
    "composition": {
        "name": "Using modes for composition",
        "pages": "16–18",
        "summary": (
            "Scale pattern alone does not make a modal piece. Establish finalis + "
            "characteristic modal note; favor chords containing that note; diatonic melodies; "
            "avoid stock major/minor tonal cadences that kill modality."
        ),
    },
    "dorian": {
        "name": "The Dorian mode",
        "pages": "19–21",
        "summary": "Ancient/church pedigree; minor with natural 6; harmony vs major on same root; Scarborough Fair example.",
    },
    "phrygian": {
        "name": "The Phrygian mode",
        "pages": "22–23",
        "summary": "b2 color; Spanish/Arabic flavor; cadences with bII, i, iv patterns.",
    },
    "lydian_mixolydian": {
        "name": "Lydian and Mixolydian",
        "pages": "24–26",
        "summary": "Other major modes: Lydian #4 brightness; Mixolydian b7 dominant flavor; cadences and chord tables.",
    },
    "locrian": {
        "name": "The Locrian mode",
        "pages": "27–28",
        "summary": "Unstable b5 tonic; rare as home mode; specialized cadences on m7b5.",
    },
    "modulation": {
        "name": "Modulation",
        "pages": "29–33",
        "summary": (
            "Parent key, adjacent keys, remote keys via V/V7 of destination, "
            "inter-tonal exchanges between distant diatonic collections; relative major/minor ease."
        ),
    },
}


def list_topics() -> list[str]:
    return list(TOPICS.keys())


def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "modes": "defining_modes",
        "define": "defining_modes",
        "improv": "improvisation",
        "compose": "composition",
        "composition": "composition",
        "lydian": "lydian_mixolydian",
        "mixolydian": "lydian_mixolydian",
        "modulate": "modulation",
    }
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic '{name}'. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
