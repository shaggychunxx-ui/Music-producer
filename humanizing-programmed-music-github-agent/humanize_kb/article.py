"""Structured transcription of the 'Humanizing Programmed Music' deep-dive article."""

from __future__ import annotations

from typing import Any

ARTICLE = {
    "title": "Deep Dive: Advanced Techniques for Humanizing Programmed Music",
    "author": None,
    "date": None,
    "site": "Internal knowledge base",
    "url": None,
    "thesis": (
        "To successfully humanize digital music, you must dismantle the absolute "
        "perfection of the digital domain. Computers excel at repeating identical "
        "tasks flawlessly; humans excel at expressive variations. Achieving a "
        "realistic, emotive feel requires a systematic approach to five core "
        "elements: micro-timing deviations, micro-dynamic shaping, tonal "
        "variations, arrangement imperfections, and spatial acoustics."
    ),
    "core_elements": [
        "micro_timing",
        "micro_dynamics",
        "tonal_expression",
        "arrangement_imperfections",
        "spatial_realism",
    ],
}

CATEGORIES: dict[str, dict[str, Any]] = {
    "micro_timing": {
        "name": "Advanced Micro-Timing Deviations",
        "summary": (
            "A professional human musician plays around the beat to create a "
            "specific 'feel' or pocket, rarely hitting the mathematical center of "
            "a transient."
        ),
        "techniques": {
            "pocketing": {
                "name": "Pocketing: Rushing vs. Dragging",
                "concept": (
                    "Rushing (slightly ahead of the grid) creates urgency, energy, "
                    "and drive. Dragging (slightly behind the grid) creates a "
                    "laid-back, relaxed, or heavy groove."
                ),
                "applications": [
                    "Snare drum: hip-hop/neo-soul/lo-fi -> nudge 5-15ms late (dragging) "
                    "for a relaxed, human pocket.",
                    "Snare drum: aggressive rock/electronic -> nudge 2-5ms early for "
                    "forward momentum.",
                    "Bassline: keep the kick locked tightly to the grid, shift bass "
                    "guitar/synth bass 3-10ms late so the kick hits first, followed by "
                    "the bass, mimicking a live rhythm section.",
                ],
            },
            "chord_flamming": {
                "name": "Chord Flamming and Strumming",
                "concept": (
                    "A human pianist's fingers do not strike a chord at the exact same "
                    "millisecond; a guitarist strokes strings sequentially."
                ),
                "applications": [
                    "Drag the start times of individual chord notes to cascade upward "
                    "or downward over a window of 5-25 milliseconds.",
                    "Use a DAW's Quantize Flam (Q-Flam) or Strum tool to automate "
                    "staggered note starts via a percentage slider.",
                ],
            },
            "groove_extraction": {
                "name": "Grid Loosening and Groove Extraction",
                "concept": "Use organic groove templates instead of a rigid 16th-note grid.",
                "applications": [
                    "Extract timing and velocity data from a real audio recording "
                    "(e.g. a classic James Brown drum break) and apply it as a groove "
                    "template to MIDI.",
                    "Apply a global 'Humanize' timing randomization of roughly 3% to "
                    "7% to break up strict quantization without destroying the rhythm.",
                ],
            },
        },
    },
    "micro_dynamics": {
        "name": "Micro-Dynamic Shaping (Velocity Control)",
        "summary": (
            "Velocity dictates the volume and intensity of a MIDI note. Flat "
            "velocities (e.g. every note at a default of 100) are the primary "
            "cause of the 'machine-gun effect.'"
        ),
        "techniques": {
            "accents": {
                "name": "Accents and Downbeat Hierarchies",
                "concept": "Human players naturally emphasize structural beats.",
                "velocity_hierarchy": {
                    "beat_1_downbeat": "110-115 (strongest)",
                    "beat_3_backbeat": "100-105 (strong)",
                    "beats_2_and_4": "90-95 (medium)",
                    "off_beats_subdivisions": "75-85 (weakest)",
                },
            },
            "physiological_modeling": {
                "name": "Physiological Velocity Modeling",
                "concept": (
                    "Human hands have fingers of varying strength (thumb strikes "
                    "harder than pinky); a drummer's dominant hand hits harder on a "
                    "downward motion than an upward motion."
                ),
                "applications": [
                    "Alternate hi-hat eighth/sixteenth-note velocities in a "
                    "'strong-weak-strong-weak' pattern (e.g. 95, 75, 90, 70) to "
                    "simulate the natural up-and-down motion of a drumstick."
                ],
            },
            "ghost_notes": {
                "name": "Ghost Notes and Transitions",
                "concept": (
                    "Drummers rest sticks lightly on the snare head between main hits, "
                    "creating tiny, subconscious intermediate strokes called ghost "
                    "notes."
                ),
                "applications": [
                    "Program tiny, low-velocity hits (velocities 15-35) right before a "
                    "major snare or kick hit to bridge gaps between major transients."
                ],
            },
        },
    },
    "tonal_expression": {
        "name": "Tonal and Expression Modulation",
        "summary": (
            "A real instrument changes its physical frequency response based on how "
            "hard it is played. A hard strike produces more high-frequency "
            "harmonics; a soft strike sounds darker and warmer."
        ),
        "techniques": {
            "velocity_to_filter": {
                "name": "Velocity-to-Filter Mapping",
                "concept": (
                    "If a synth/sampler plays the same waveform at low velocity as it "
                    "does at high velocity, the illusion breaks."
                ),
                "applications": [
                    "Route MIDI Velocity to the Low-Pass Filter Cutoff so lower "
                    "velocities slightly close the filter (darker) and higher "
                    "velocities fully open it (brighter), mimicking physical "
                    "instrument acoustics."
                ],
            },
            "round_robin": {
                "name": "Round Robin and Sample Start Offset",
                "concept": (
                    "High-end drum samplers cycle through 5-10 recordings of the same "
                    "hit (Round Robin) so no two consecutive hits sound identical."
                ),
                "applications": [
                    "Without Round Robin, map MIDI Velocity to Sample Start Offset so a "
                    "slightly lower velocity plays the audio a few milliseconds after "
                    "the initial transient, introducing attack-phase variation."
                ],
            },
            "cc_automation": {
                "name": "Continuous Controller (CC) Automation",
                "concept": (
                    "Instruments like violins, trumpets, and vocal chords constantly "
                    "change volume, timbre, and vibrato after the note has started."
                ),
                "applications": [
                    "Use CC#11 (Expression) or CC#1 (Modulation Wheel) to draw "
                    "continuous wave-like curves instead of flat, straight lines.",
                    "String section automation should swell up into notes and decay "
                    "softly out of them.",
                ],
            },
        },
    },
    "arrangement_imperfections": {
        "name": "Arrangement and Performance Imperfections",
        "summary": (
            "Humans make mistakes, change their minds mid-phrase, and get tired "
            "over the course of a long song."
        ),
        "techniques": {
            "avoid_loop_trap": {
                "name": "Avoiding the Loop Trap",
                "concept": (
                    "Copy-pasting a perfect 4-bar or 8-bar MIDI loop across a "
                    "4-minute track instantly screams 'programmed.'"
                ),
                "applications": [
                    "Write the main loop, copy it across the song, then manually "
                    "alter every iteration.",
                    "Delete a note in the second verse.",
                    "Add an extra decorative fill at the end of the second chorus.",
                    "Slightly lower the overall velocity of the instruments during the "
                    "bridge to simulate the band pulling back.",
                ],
            },
            "tempo_tracking": {
                "name": "Structural Climaxing (Tempo Tracking)",
                "concept": (
                    "Live bands naturally speed up by 1 to 3 BPM during high-energy "
                    "choruses and slow down slightly during intimate verses or "
                    "emotional transitions."
                ),
                "applications": [
                    "Automate the master tempo track instead of a flat tempo, e.g. "
                    "verses at 119.5 BPM, ramping up to 121.5 BPM over a pre-chorus "
                    "build-up."
                ],
            },
        },
    },
    "spatial_realism": {
        "name": "Spatial Realism and Acoustic Environment",
        "summary": (
            "In the real world, music is played in physical spaces where sounds "
            "bleed into one another and bounce off walls."
        ),
        "techniques": {
            "bleed": {
                "name": "The Magic of Bleed (Cross-Talk)",
                "concept": (
                    "In a real studio, a tom-tom hit bleeds slightly into the snare "
                    "microphone and the overhead microphones."
                ),
                "applications": [
                    "Use a dedicated drum suite (Superior Drummer, Addictive Drums) "
                    "and turn up the 'Acoustic Leakage' or 'Bleed' faders.",
                    "Route a tiny amount of dry kick and snare tracks to a shared "
                    "stereo room reverb bus to glue them into the same virtual space.",
                ],
            },
            "analog_drift": {
                "name": "Analog Nonlinearity and Pitch Drift",
                "concept": (
                    "Vintage analog hardware components warp, heat up, and cool down, "
                    "causing microscopic tuning instabilities."
                ),
                "applications": [
                    "Use a 'wow and flutter' or tape emulation plugin on instrument "
                    "busses.",
                    "Map a subtle, slow LFO to the global pitch fine-tuning of synths "
                    "(depth of 2-5 cents) so instruments drift marginally out of tune "
                    "over time, like real strings or analog circuits.",
                ],
            },
        },
    },
}


def list_categories() -> list[str]:
    return list(CATEGORIES.keys())


def get_category(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "timing": "micro_timing",
        "micro_timing_deviations": "micro_timing",
        "pocket": "micro_timing",
        "dynamics": "micro_dynamics",
        "velocity": "micro_dynamics",
        "tonal": "tonal_expression",
        "tone": "tonal_expression",
        "expression": "tonal_expression",
        "arrangement": "arrangement_imperfections",
        "imperfections": "arrangement_imperfections",
        "spatial": "spatial_realism",
        "space": "spatial_realism",
        "acoustics": "spatial_realism",
    }
    key = aliases.get(key, key)
    if key not in CATEGORIES:
        for k, v in CATEGORIES.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown category '{name}'. Try: {', '.join(list_categories())}")
    return CATEGORIES[key]


def list_techniques(category: str | None = None) -> list[str]:
    if category is None:
        techs = []
        for cat in CATEGORIES.values():
            techs.extend(cat["techniques"].keys())
        return techs
    return list(get_category(category)["techniques"].keys())


def get_technique(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "rushing": "pocketing",
        "dragging": "pocketing",
        "flam": "chord_flamming",
        "strum": "chord_flamming",
        "groove": "groove_extraction",
        "humanize": "groove_extraction",
        "accent": "accents",
        "hierarchy": "accents",
        "physiological": "physiological_modeling",
        "ghost_note": "ghost_notes",
        "filter": "velocity_to_filter",
        "round_robin": "round_robin",
        "sample_offset": "round_robin",
        "cc": "cc_automation",
        "expression_automation": "cc_automation",
        "loop_trap": "avoid_loop_trap",
        "tempo": "tempo_tracking",
        "climax": "tempo_tracking",
        "cross_talk": "bleed",
        "crosstalk": "bleed",
        "leakage": "bleed",
        "drift": "analog_drift",
        "wow_and_flutter": "analog_drift",
        "pitch_drift": "analog_drift",
    }
    key = aliases.get(key, key)
    for cat in CATEGORIES.values():
        if key in cat["techniques"]:
            return cat["techniques"][key]
    raise KeyError(f"Unknown technique '{name}'. Try: {', '.join(list_techniques())}")
