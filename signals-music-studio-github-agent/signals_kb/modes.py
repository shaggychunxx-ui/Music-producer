from __future__ import annotations

MODES: dict[str, dict] = {
    "ionian": {
        "aka": ["major"],
        "degrees": "1 2 3 4 5 6 7",
        "tonic": "major",
        "feel": "Default bright / catchy / radio.",
        "write": [
            "Do not skip it because it is 'simple' — it is still the hook factory.",
            "Start loops on I; close on IV or V.",
            "Signature pop loop: I–V–vi–IV.",
        ],
        "avoid": "Nothing required. Know its habits so you can leave them when writing other modes.",
        "lessons": ["writing-chord-progressions", "riffing-modes-ionian"],
    },
    "dorian": {
        "aka": ["2nd mode"],
        "degrees": "1 2 b3 4 5 6 b7",
        "tonic": "minor",
        "characteristic": "natural 6 (vs Aeolian b6)",
        "feel": "Wistful, smoky, slightly optimistic minor. Santana / jazz-funk / dad-rock.",
        "write": [
            "Signature move: i–IV (Am–D). The major IV proves Dorian.",
            "Sustain i so A (or your finalis) feels like home before other chords.",
            "Leads: bend to / land on the natural 6.",
            "Allowed break: raise 7 for V (Am–D–E) — leaves Dorian toward melodic/harmonic minor.",
        ],
        "avoid": "Aeolian b6 (minor iv / bVI) if you want the Dorian color to stay.",
        "lessons": ["dorian-scale-intro", "riffing-modes-dorian", "jam-track-funk-dorian"],
    },
    "phrygian": {
        "aka": ["3rd mode"],
        "degrees": "1 b2 b3 4 5 b6 b7",
        "tonic": "minor",
        "characteristic": "b2",
        "feel": "Dark / evil / Jaws half-step. Flamenco, metal, some rap/EDM.",
        "write": [
            "Pedal the tonic; snake melody around b2 and b7.",
            "Useful chords: bII and bvii (both contain b2), resolve to i.",
            "Most songs only dip into Phrygian for a riff, then leave.",
        ],
        "avoid": "Confusing with Phrygian Dominant (major 3rd; 5th mode of harmonic minor).",
        "lessons": ["phrygian-scale-intro", "riffing-modes-phrygian", "harmonic-minor-phrygian-dominant"],
    },
    "lydian": {
        "aka": ["4th mode"],
        "degrees": "1 2 3 #4 5 6 7",
        "tonic": "major",
        "characteristic": "#4",
        "feel": "Dreamy, floaty, film-wonder, fragile prog.",
        "write": [
            "Identity tetrachord: 1 3 #4 5.",
            "Stay on I as long as possible. Dip to II or vii only.",
            "If you camp on V, the ear resets to that major key and Lydian dies.",
        ],
        "avoid": "Natural 4, and long V chords.",
        "lessons": ["lydian-scale-intro", "riffing-modes-lydian"],
    },
    "mixolydian": {
        "aka": ["5th mode"],
        "degrees": "1 2 3 4 5 6 b7",
        "tonic": "major",
        "characteristic": "b7",
        "feel": "Major's cooler sibling — bold, bouncy rock. AC/DC, bagpipes, many 80s hooks.",
        "write": [
            "Signature: I–bVII–IV.",
            "Also I–v (minor v) for a bittersweet hover.",
            "Leads: Mixolydian pentatonic + chord-tone accents, slides, hammers.",
        ],
        "avoid": "Treating I7 as a V7 that must resolve away — I7 is home.",
        "lessons": ["mixolydian-improv-intro", "riffing-modes-mixolydian", "jam-track-classic-rock"],
    },
    "aeolian": {
        "aka": ["natural minor", "minor", "6th mode"],
        "degrees": "1 2 b3 4 5 b6 b7",
        "tonic": "minor",
        "characteristic": "b6 (vs Dorian nat6)",
        "feel": "Default sad/serious minor.",
        "write": [
            "Starter palette: i, iv, bVI, bVII.",
            "Real 'minor key' writing usually adds V via harmonic minor (raised 7).",
            "Andalusian: i–bVII–bVI–V.",
        ],
        "avoid": "Calling every minor vamp Aeolian if the 6th is major (that's Dorian).",
        "lessons": ["writing-in-minor", "andalusian-cadence", "riffing-modes-aeolian"],
    },
    "locrian": {
        "aka": ["7th mode"],
        "degrees": "1 b2 b3 4 b5 b6 b7",
        "tonic": "diminished",
        "characteristic": "b5",
        "feel": "Awkward leftover. Unstable home.",
        "write": [
            "Know why it fails: diminished tonic will not rest.",
            "Useful as a color over diminished chords, not as a default key.",
            "If you want weird, you do not have to stay inside Locrian rules.",
        ],
        "avoid": "Sustaining i° as if it were a major/minor home.",
        "lessons": ["riffing-modes-locrian"],
    },
}

ALIASES = {
    "major": "ionian",
    "minor": "aeolian",
    "natural-minor": "aeolian",
    "nat-minor": "aeolian",
}


def list_modes() -> list[str]:
    return [
        f"{name}: {m['degrees']}  ({m['tonic']} tonic) — {m['feel']}"
        for name, m in MODES.items()
    ]


def get_mode(name: str) -> dict:
    key = name.strip().lower().replace(" ", "-")
    key = ALIASES.get(key, key)
    if key in MODES:
        out = {"name": key, **MODES[key]}
        return out
    hits = [k for k, m in MODES.items() if key in k or key in " ".join(m.get("aka", [])).lower()]
    if len(hits) == 1:
        return get_mode(hits[0])
    return {"error": f"unknown mode {name!r}", "available": list(MODES)}
