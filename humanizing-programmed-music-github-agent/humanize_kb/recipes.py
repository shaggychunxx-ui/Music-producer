"""Practical, actionable checklists distilled from the humanizing-music categories."""

from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "hiphop_drums": {
        "title": "Humanize a hip-hop/neo-soul drum groove",
        "category": "micro_timing",
        "steps": [
            "Keep the kick locked tightly to the grid.",
            "Nudge the snare 5-15ms late (dragging) for a relaxed pocket.",
            "Shift bass guitar/synth bass notes 3-10ms late so the kick leads.",
            "Program tiny ghost notes (velocity 15-35) before major snare hits.",
        ],
    },
    "rock_electronic_drums": {
        "title": "Humanize an aggressive rock/electronic drum groove",
        "category": "micro_timing",
        "steps": [
            "Nudge the snare 2-5ms early (rushing) for forward momentum.",
            "Keep the kick locked to the grid as the rhythmic anchor.",
            "Apply a 3-7% global timing randomization to break up strict quantization.",
        ],
    },
    "piano_chord_humanization": {
        "title": "Humanize a programmed piano/guitar chord",
        "category": "micro_timing",
        "steps": [
            "Select the chord's individual notes.",
            "Stagger note start times over a 5-25ms window (cascade up or down).",
            "Or use the DAW's Quantize Flam (Q-Flam)/Strum tool with a percentage slider.",
        ],
    },
    "hihat_velocity": {
        "title": "Humanize a programmed hi-hat pattern",
        "category": "micro_dynamics",
        "steps": [
            "Set a velocity hierarchy: beat 1 strongest (110-115), beat 3 strong "
            "(100-105), beats 2/4 medium (90-95), off-beats weakest (75-85).",
            "Alternate eighth/sixteenth-note velocities strong-weak-strong-weak "
            "(e.g. 95, 75, 90, 70) to mimic drumstick motion.",
        ],
    },
    "synth_acoustics": {
        "title": "Make a sampled/synth instrument respond like a real one",
        "category": "tonal_expression",
        "steps": [
            "Route MIDI Velocity to Low-Pass Filter Cutoff (low velocity = darker, "
            "high velocity = brighter).",
            "If no Round Robin, map Velocity to Sample Start Offset for attack "
            "variation.",
            "Draw CC#11 (Expression) or CC#1 (Modulation) curves that swell into and "
            "decay out of notes instead of flat automation lines.",
        ],
    },
    "avoid_repetition": {
        "title": "Break the copy-paste loop trap across a full song",
        "category": "arrangement_imperfections",
        "steps": [
            "Write the main loop and copy it across the song as a starting point.",
            "Delete a note in the second verse.",
            "Add a decorative fill at the end of the second chorus.",
            "Lower overall velocity slightly during the bridge to simulate pulling back.",
            "Automate master tempo: slightly slower verses, ramp up 1-3 BPM into choruses.",
        ],
    },
    "acoustic_glue": {
        "title": "Glue programmed drums into one virtual space",
        "category": "spatial_realism",
        "steps": [
            "Turn up 'Acoustic Leakage'/'Bleed' faders in a drum suite if available.",
            "Or route a small amount of dry kick/snare to a shared stereo room reverb "
            "bus.",
            "Add subtle wow-and-flutter/tape emulation on instrument busses.",
            "Optionally map a slow LFO (2-5 cents depth) to global pitch fine-tuning "
            "for analog-style drift.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "hiphop": "hiphop_drums",
        "neo_soul": "hiphop_drums",
        "rock": "rock_electronic_drums",
        "electronic": "rock_electronic_drums",
        "chords": "piano_chord_humanization",
        "flam": "piano_chord_humanization",
        "hihat": "hihat_velocity",
        "hi_hat": "hihat_velocity",
        "synth": "synth_acoustics",
        "filter": "synth_acoustics",
        "loop": "avoid_repetition",
        "loop_trap": "avoid_repetition",
        "bleed": "acoustic_glue",
        "reverb_bus": "acoustic_glue",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
