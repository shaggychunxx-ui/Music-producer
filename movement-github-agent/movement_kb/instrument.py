"""Structured transcription of Output MOVEMENT Owner's Manual."""

from __future__ import annotations

from typing import Any

INSTRUMENT = {
    "name": "Output MOVEMENT",
    "manufacturer": "Output",
    "type": "Dual-engine rhythmic multi-effects processor (plugin)",
    "manual": "Owner's Manual (Movement_User_Guide.pdf)",
    "website": "https://www.output.com",
    "source": "https://drive.google.com/file/d/10rxiXHuJ9Oz89ByD5pEcgMr2Ax8E8y5z/view",
    "pages": 17,
    "overview": (
        "Effects processor designed to add rhythmic, textural motion to audio. "
        "Modulates up to 38 parameters at once from four independent rhythm sources "
        "(LFO, step sequence, or sidechain envelope). Input is duplicated into two "
        "identical engines (A/B), each with four FX slots; engines sum to stereo out."
    ),
    "toc": [
        "1. Overview & Getting Started",
        "2. Engines",
        "3. FX Modules",
        "4. Rhythms",
        "5. Flux",
        "6. X-Y Pad & Macros",
        "7. Presets",
        "8. Additional Info (Low CPU, on-screen help)",
    ],
    "architecture": {
        "engines": 2,
        "fx_slots_per_engine": 4,
        "rhythms": {
            "1": "Engine A",
            "2": "Engine A",
            "3": "Engine B",
            "4": "Engine B",
        },
        "cross_engine_modulation": False,
        "max_modulated_params": 38,
        "per_engine_controls": ["volume", "pan", "mute", "VU meter", "4 FX slots", "2 rhythms"],
    },
    "fx_types": ["delay", "filter", "reverb", "eq", "distortion", "compression"],
    "rhythm_types": ["LFO", "step sequencer", "sidechain"],
    "preset_paths": {
        "mac": "/Users/Shared/Output/Movement/Presets",
        "pc": "C:/Users/Public/Documents/Output/Movement/Presets",
        "format": "XML",
    },
    "install": [
        "Receive serial after purchase",
        "Install Output Connect; paste serial; download installer",
        "Run installer; load plugin in DAW; activate with serial",
    ],
    "global_rules": [
        "FX module output gain knobs are unipolar (no modulation past current setting)",
        "Mute unused engine when designing so dry path does not mask wet path",
        "Assign rhythm by dragging numbered circle onto a knob; depth via under-knob slider",
        "Low CPU mode only freezes GUI animation, not audio",
    ],
}

FX_MODULES: dict[str, dict[str, Any]] = {
    "delay": {
        "time": "1/256 bar to 1 bar; straight, dotted, or triplet",
        "params": ["Type (feedback character)", "Time", "Feedback", "HP/LP", "Wet/Dry", "Output"],
    },
    "filter": {
        "params": ["Type (2/4 pole HP, LP, BP)", "Cutoff", "Resonance", "Wet/Dry", "Output"],
        "ui": "Drag graph: L/R = cutoff, U/D = resonance",
    },
    "reverb": {
        "type": "Room modeled",
        "params": ["Predelay (ms)", "Size", "HP/LP", "Wet/Dry", "Output"],
    },
    "eq": {
        "type": "Two-band; parametric or shelving",
        "params": ["Width (parametric)", "Frequency", "Level", "Wet/Dry", "Output"],
        "ui": "Drag graph: L/R = freq, U/D = boost/cut",
    },
    "distortion": {
        "params": ["Crunch (intensity + HF accent)", "Drive", "HP/LP", "Wet/Dry", "Output"],
    },
    "compression": {
        "params": ["Warmth (tube-style input drive)", "Threshold", "Ratio", "Attack", "Release", "Wet/Dry", "Output"],
    },
}

LFO_SHAPES = [
    "Sine",
    "Trapezoid",
    "Triangle",
    "Quad Stepped Sawtooth",
    "Sawtooth Up",
    "Pulse",
    "Notch",
    "Wide Pulse",
    "Sawtooth Down",
    "Tri Stepped Sawtooth",
    "Random",
    "Narrow Pulse",
]

TOPICS: dict[str, dict[str, Any]] = {
    "overview": {
        "name": "Overview",
        "summary": INSTRUMENT["overview"],
        "assign_modulation": (
            "Drag numbered rhythm icon onto a knob; edit rhythm via darkened circular area; "
            "set amount with colored slider under the knob."
        ),
    },
    "getting_started": {
        "name": "Getting started / install",
        "summary": "Connect utility + serial download; install; activate in DAW with product key.",
        "steps": INSTRUMENT["install"],
    },
    "engines": {
        "name": "Engines A & B",
        "summary": (
            "Two parallel rhythm/FX units. Each: 4 FX slots, 2 rhythms, volume, pan, mute, VU. "
            "Rhythms 1–2 → A only; 3–4 → B only. Mute alternate engine while designing chains."
        ),
    },
    "fx": {
        "name": "FX modules",
        "summary": "Six types per slot via +. Output knobs unipolar. See FX_MODULES.",
        "modules": FX_MODULES,
    },
    "rhythms": {
        "name": "Rhythms (LFO / step / sidechain)",
        "summary": (
            "Three rhythm kinds modulate FX params + engine volume/pan on the owning engine."
        ),
        "lfo": {
            "shapes": LFO_SHAPES,
            "controls": ["Shape", "Rate (host tempo division)", "Phase", "Chaos (random amp per cycle)"],
            "note": "LFO modulates above/below knob position except unipolar output gains.",
        },
        "step_sequencer": {
            "steps": "1–32",
            "rate": "8 bars down to 1/64 triplet (host tempo divisions)",
            "controls": ["Swing", "Pattern menu (36 presets)", "Random", "Clear"],
            "step_shapes": (
                "Four shapes; each step generally rises from 0 to value then back to 0 "
                "(attack/release-like) except square which holds between step values like a classic sequencer."
            ),
        },
        "sidechain": {
            "behavior": "Envelope follower from DAW sidechain input; boost or duck",
            "full_range": "On = bipolar recovery can overshoot original; Off = unipolar",
            "params": ["Gain", "Attack", "Release", "Offset (ms delay for syncopation)"],
            "tip": "Best with transient sources (kick); full mixes with slow silence return are less useful",
        },
    },
    "flux": {
        "name": "Flux",
        "summary": (
            "Modulate one rhythm's rate with the other rhythm on the same engine. "
            "Enable Flux On, or drag rhythm circle onto the other rate knob; scale with slider."
        ),
    },
    "xy_pad": {
        "name": "XY pad & macros",
        "summary": (
            "Y/orange = Engine A advancement (up); X/blue = Engine B advancement (right). "
            "Right-click knob → Assign to XY Control; edit knob range and rhythm amount range; "
            "power toggles per axis; XY icon reopens editor."
        ),
        "gotcha": "Rhythm amount range scales relative to current rhythm slider (already max = no further increase).",
    },
    "presets": {
        "name": "Presets",
        "summary": "XML user presets; save icon + tags; browser tags/search/favorites; folder paths on Mac/PC.",
        "paths": INSTRUMENT["preset_paths"],
    },
    "cpu_help": {
        "name": "Low CPU & help",
        "summary": "Low CPU freezes graphics only; ? opens on-screen help for UI elements.",
    },
}


def list_topics() -> list[str]:
    return list(TOPICS.keys())


def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "engine": "engines",
        "effects": "fx",
        "effect": "fx",
        "lfo": "rhythms",
        "sequencer": "rhythms",
        "step": "rhythms",
        "sidechain": "rhythms",
        "macro": "xy_pad",
        "xy": "xy_pad",
        "macros": "xy_pad",
        "install": "getting_started",
        "activate": "getting_started",
        "cpu": "cpu_help",
        "help": "cpu_help",
        "preset": "presets",
    }
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic '{name}'. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
