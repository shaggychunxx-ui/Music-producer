from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "start_track": {
        "title": "Start any genre track (Part I workflow)",
        "steps": [
            "Import 2–4 commercial references in target genre; match rough loudness.",
            "Set BPM and swing/groove template before writing.",
            "Build a 4–8 bar core loop: drums + bass + one harmonic/melodic hook that already feels like the genre.",
            "Map form (song sections or dance intro–build–drop–outro).",
            "Sound design pass; intentional layering only.",
            "If vocals: carve space early; everything serves the lead.",
            "Mix in context; export, rest, revise vs references.",
        ],
    },
    "kick_bass": {
        "title": "Solve kick–bass (universal mix tip)",
        "steps": [
            "Identify who owns sub on hits (often kick).",
            "Complementary EQ carve (e.g. 100–200 Hz fight zone in metal/rock; 808 vs vocal mid-low in trap).",
            "Sidechain or volume duck competing lows.",
            "Frequency split: short kick click + long bass body.",
            "Check mono and small speakers before stacking more low layers.",
        ],
    },
    "trap_beat": {
        "title": "Trap beat starter",
        "steps": [
            "Set ~140 BPM; snare/clap on beat 3 (half-time).",
            "Program 808 bassline with glide; layer short kick if needed.",
            "Hi-hats 1/8–1/16 + rolls into downbeats with pitch automation.",
            "Dark simple motif; keep verse sparse, hook fuller + ad-libs.",
            "Mono sub; saturate 808; vocal-forward chain.",
        ],
    },
    "house_dj": {
        "title": "DJ-friendly house sketch",
        "steps": [
            "118–128 BPM; kick every beat; clap 2/4; open hats on offbeats.",
            "Syncopated bass sidechained to kick.",
            "16–32 bar intro percussion+kick for mixing in.",
            "Groove → bass → hook → breakdown → build → drop → outro.",
            "Phrase in 8/16/32 bars.",
        ],
    },
    "boom_bap": {
        "title": "Boom bap loop",
        "steps": [
            "90–94 BPM; hard snare 2 and 4; swung hats.",
            "Chop soul/jazz loop; filter and saturate; re-chop after print through console/tape emu.",
            "Simple bass; leave vocal space.",
            "Parallel drum compression; don't smash limiter.",
        ],
    },
    "pop_vocal": {
        "title": "Pop vocal production pass",
        "steps": [
            "Comp best syllables; transparent tuning (or hard tune if style).",
            "Align doubles; chorus triples/octaves/harmonies on key words.",
            "De-ess before brightening; slap + tempo delay throws.",
            "If chorus not bigger, remove verse layers first.",
        ],
    },
    "dnb_bass": {
        "title": "DnB sub + mid bass split",
        "steps": [
            "170–178 BPM; arrange break phrases in 8/16 bars.",
            "Clean mono sub fundamental separate from reese/neuro mid bass.",
            "Process bands separately; automate mid-bass movement.",
            "Parallel compress breaks for glue/aggression.",
        ],
    },
    "metal_guitars": {
        "title": "Modern metal rhythm guitars",
        "steps": [
            "DI record; amp sim or reamp; tight edit chugs to grid if modern.",
            "Quad-track L/R carefully phase-aligned.",
            "EQ carve vs kick 100–200 Hz; bass follows with click + sub.",
            "Sample-reinforce kick/snare for modern impact.",
        ],
    },
    "finish": {
        "title": "Finishing checklist (any genre)",
        "steps": [
            "A/B vs references on multiple systems (monitors, phones, car).",
            "Mono check lows and core elements.",
            "Automation rides complete; no masking on lead.",
            "Export with ~−1 dBTP headroom for streaming.",
            "Rest ears; final pass next day.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "start": "start_track",
        "workflow": "start_track",
        "kick": "kick_bass",
        "bass": "kick_bass",
        "808": "trap_beat",
        "trap": "trap_beat",
        "house": "house_dj",
        "boom": "boom_bap",
        "hiphop": "boom_bap",
        "vocal": "pop_vocal",
        "pop": "pop_vocal",
        "dnb": "dnb_bass",
        "jungle": "dnb_bass",
        "metal": "metal_guitars",
        "checklist": "finish",
        "master": "finish",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
