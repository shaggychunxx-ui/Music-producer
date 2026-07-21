from __future__ import annotations
from typing import Any

INSTRUMENT = {
    "name": "Korg monologue",
    "type": "Monophonic analog synthesizer",
    "manual": "monologue Owner's Manual (English)",
    "source_url": "https://cdn.korg.com/us/support/download/files/d05d6cb06052aed2b067eea2dfa4f7cd.pdf",
    "pages": 59,
    "lineage": "Analog circuit based on minilogue design; VCF tuned for mono; drive circuit for aggressive tones",
    "features": [
        "Battery powered (6x AA) or DC 9V adapter",
        "80 factory + 20 user programs",
        "Real-time oscilloscope display",
        "16-step sequencer with up to 4 motion parameters",
        "Sync In/Out for volca/DAW expansion",
        "USB and 5-pin MIDI",
    ],
    "signal_path": [
        "VCO1 (SAW/SQR, SHAPE)",
        "VCO2 (SAW/TRI, OCTAVE, PITCH, SYNC/RING, SHAPE)",
        "NOISE",
        "MIXER (VCO1/VCO2 levels)",
        "VCF (CUTOFF, RESONANCE)",
        "DRIVE",
        "VCA / OUTPUT (+ AUDIO IN path)",
    ],
    "front_panel": [
        "MASTER", "DRIVE", "OCTAVE (±2)", "Slider (program-assignable)",
        "VCO1 WAVE/SHAPE", "VCO2 OCTAVE/PITCH/WAVE/SYNC-RING/SHAPE",
        "MIXER VCO1/VCO2", "FILTER CUTOFF/RESONANCE",
        "EG TYPE/ATTACK/DECAY/INT/TARGET",
        "LFO WAVE/MODE/RATE/INT/TARGET",
        "SEQUENCER TEMPO, KEY TRG/HOLD, MOTION/SLIDE/NOTE, PLAY/REC/REST/SHIFT, steps 1-8 (+shift 9-16)",
        "PROGRAM/VALUE", "Display (scope)", "EDIT MODE / WRITE / EXIT",
    ],
    "rear": ["USB B", "Power", "MIDI IN/OUT", "SYNC IN/OUT", "AUDIO IN", "OUTPUT", "Headphones", "DC 9V"],
    "toc": [
        "Introduction & features", "Block diagram", "Controls & connections",
        "Power on/off, batteries, auto power off",
        "Play programs & sequencer", "Program architecture & editing",
        "Sequencer & motion sequence",
        "Edit mode: PROGRAM / SEQ / GLOBAL",
        "Tuning, factory restore, SHIFT shortcuts",
        "MIDI/USB", "Program list", "Specifications", "MIDI implementation chart",
    ],
    "program_memory": {"factory": "001-080", "user": "081-100", "includes": "sound + sequence"},
    "sync_out": "5 V pulse, 15 ms at beginning of each step",
}

TOPICS: dict[str, dict[str, Any]] = {
    "overview": {"name": "Overview & features", "summary": "Mono analog (minilogue lineage), drive, portable, 100 programs, scope, 16-step + motion, sync I/O."},
    "panel": {"name": "Controls & connections", "summary": "Front synth voice + sequencer; rear MIDI/USB/sync/audio/power."},
    "power": {"name": "Power", "summary": "6x AA or 9V adapter; hold power switch; save programs before off; auto power off 4h default; battery type in GLOBAL."},
    "programs": {"name": "Programs", "summary": "Select with PROGRAM/VALUE; SHIFT+knob skips 10; save via WRITE; architecture VCO/mixer/filter/EG/LFO/seq."},
    "sound": {"name": "Sound design", "summary": "VCO1/2 waves & shape; sync/ring; filter; drive; EG targets; LFO targets; AUDIO IN."},
    "sequencer": {"name": "Sequencer", "summary": "16 steps; PLAY/REC; KEY TRG/HOLD transpose/latch; MOTION/SLIDE/NOTE; tempo 56-240; rests, active steps."},
    "motion": {"name": "Motion sequence", "summary": "Automate up to 4 synth parameters per program; enable/smooth in SEQ EDIT."},
    "edit": {"name": "Edit modes", "summary": "EDIT MODE button; PROGRAM EDIT, SEQ EDIT, GLOBAL EDIT parameter lists."},
    "midi": {"name": "MIDI & USB", "summary": "DIN + USB; local/MIDI channel/filter settings in GLOBAL; control external or be controlled."},
    "sync": {"name": "Sync I/O", "summary": "Pulse sync with volca etc.; SYNC OUT 5V 15ms/step; GLOBAL settings for sync behavior."},
    "maintenance": {"name": "Tuning / factory / shortcuts", "summary": "Tuning function; restore factory; SHIFT button shortcuts table."},
}

def list_topics():
    return list(TOPICS.keys())

def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {"seq": "sequencer", "voice": "sound", "filter": "sound", "vco": "sound", "global": "edit", "usb": "midi"}
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic {name}. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
