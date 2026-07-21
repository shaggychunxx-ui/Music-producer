from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "folk_vocal": {
        "title": "Intimate folk vocal + guitar",
        "genre": "folk_acoustic",
        "steps": [
            "Record for natural voice and guitar; good mic/room first.",
            "Keep processing light; preserve dynamics for home listening.",
            "Optional light room noise/atmosphere if it serves intimacy.",
            "Mix: balance, gentle EQ, minimal compression, natural reverb only if needed.",
        ],
    },
    "rock_drums_punch": {
        "title": "Rock drums with parallel compression",
        "genre": "rock",
        "steps": [
            "Get solid drum recording/levels.",
            "Send drums to parallel bus; compress heavily.",
            "Blend compressed bus under dry drums for punch without full squash.",
            "EQ carve vs guitars; optional plate/room for kit depth.",
        ],
    },
    "rock_guitars": {
        "title": "Thick rock guitars",
        "genre": "rock",
        "steps": [
            "Commit tone at amp/mic stage (distortion culture).",
            "Double/layer riffs with different FX.",
            "Pan layers for width; EQ so they don't mask vocals/kick.",
            "Add plate or hall reverb to taste.",
        ],
    },
    "pop_vocal": {
        "title": "Polished pop vocal stack",
        "genre": "pop",
        "steps": [
            "Lead vocal: surgical EQ for clarity; controlled compression.",
            "Optional creative Autotune as effect, not only correction.",
            "Record/process quieter harmony layers heavily for lushness.",
            "Consider top-down mix bus glue early for cohesive polish.",
        ],
    },
    "hiphop_808": {
        "title": "Hip-hop punch with 808",
        "genre": "hip_hop",
        "steps": [
            "Design/select 808 that supports kick relationship.",
            "Use compression for upfront punch on drums/bass.",
            "EQ carve kick vs 808 vs sample midrange.",
            "If sample-based: chop/transform source; leave headroom for mix bus.",
        ],
    },
    "dance_low_end": {
        "title": "Club-ready dance low end",
        "genre": "dance",
        "steps": [
            "Split sub-bass and mid-bass duties.",
            "Sidechain bass (and often other elements) to kick for pump/clarity.",
            "Check mix in mono; fix phase so kick/bass stay solid.",
            "Automate energy into drops.",
        ],
    },
    "jazz_natural": {
        "title": "Natural jazz quartet capture",
        "genre": "jazz",
        "steps": [
            "Spend time on room and mic placement (ribbon options for warmth).",
            "Capture interplay; avoid over-isolating if bleed serves glue.",
            "Minimal compression/EQ; preserve dynamics.",
            "Natural or convolution hall reverb if space needs help.",
        ],
    },
    "classical_dynamics": {
        "title": "Classical dynamics-first mix",
        "genre": "classical",
        "steps": [
            "Record for hall/instrument balance.",
            "Avoid heavy compression that kills emotional range.",
            "Minimal FX; realistic stage panning.",
            "Convolution reverb only as needed for venue image.",
        ],
    },
    "bottom_up": {
        "title": "Bottom-up mix session",
        "steps": [
            "Solo/priority: foundation (kick, bass) then vocal/lead.",
            "Balance each track before heavy bus processing.",
            "Resolve conflicts early with EQ/pan.",
            "Add bus glue last.",
        ],
    },
    "top_down": {
        "title": "Top-down mix session",
        "steps": [
            "Put rough levels up; insert mix-bus EQ/comp/sat.",
            "Set overall vibe and loudness target feel.",
            "Then open individual tracks that fight the bus.",
            "Common for pop/electronic cohesion.",
        ],
    },
    "reverse_engineer": {
        "title": "Copy a favorite record's production",
        "steps": [
            "Identify genre intent and listening context.",
            "Research artist/producer gear (article tip).",
            "Map to EQ/comp/FX/pan conventions in this knowledge base.",
            "Emulate one signature tool (pedal/plugin) at a time.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "folk": "folk_vocal",
        "drums": "rock_drums_punch",
        "parallel": "rock_drums_punch",
        "guitars": "rock_guitars",
        "vocal": "pop_vocal",
        "808": "hiphop_808",
        "hiphop": "hiphop_808",
        "dance": "dance_low_end",
        "sidechain": "dance_low_end",
        "club": "dance_low_end",
        "jazz": "jazz_natural",
        "classical": "classical_dynamics",
        "reference": "reverse_engineer",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
