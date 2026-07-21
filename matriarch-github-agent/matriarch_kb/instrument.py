"""Instrument overview, signal flow, and specifications."""

from __future__ import annotations

INSTRUMENT = {
    "name": "Moog Matriarch",
    "type": "Semi-Modular Analog Synthesizer",
    "manual": "Matriarch_Manual_012023",
    "family": "Moog semi-modular (pairs with Mother-32, DFAM, Grandmother, Eurorack)",
    "summary": (
        "Four analog VCOs with Hard Sync and Linear FM; dual ladder filters "
        "(series / parallel / stereo); dual ADSR; stereo VCAs; stereo analog BBD delay; "
        "dual LFO-class modulation; arp + 256-step × 12-bank sequencer; 90 patch points; "
        "mono / 2-note / 4-note paraphony. 100% analog audio path; works unpatched."
    ),
    "provenance": {
        "oscillators": "Minimoog Voyager / Moog 921 lineage",
        "mixer": "Moog CP3",
        "filters": "Moog 904A ladder",
        "envelopes": "Moog 911",
        "vcas": "Moog 902",
        "stereo_delay": "Moog 500 Series Analog Delay",
    },
    "features": [
        "49 velocity + aftertouch keys (Fatar)",
        "Pitch bend + mod wheels, variable glide",
        "4 VCOs: Triangle / Saw / Square / Narrow Pulse; octaves 16'–2'",
        "Hard Sync chain OSC1→2, 2→3, 3→4 via SYNC ENABLE",
        "Dual ladder VCF modes: HP/LP Series, LP/LP Stereo, HP/LP Parallel",
        "Stereo analog delay with ping-pong, tap, MIDI/internal sync",
        "Arpeggiator + 12 sequences of up to 256 steps (ties, rests, ratchets)",
        "90 modular patch points; DIN + USB MIDI",
        "Instrument input for external processing",
    ],
    "warmup_minutes": {"typical": 10, "cold": 25},
    "safety_notes": [
        "Do not operate in direct sunlight.",
        "No user-serviceable parts inside.",
        "High volumes can cause hearing damage.",
        "Use soft dry cloth only for cleaning.",
    ],
}

SIGNAL_FLOW = {
    "default_audio": [
        "OSC 1–4 WAVE OUT (hardwired)",
        "NOISE",
        "Mixer (levels; optional INSTRUMENT IN on rear)",
        "VCF 1 / VCF 2 (mode-dependent routing)",
        "VCA 1 (L) / VCA 2 (R)",
        "Stereo Delay (Delay 1 L / Delay 2 R)",
        "MAIN OUT L/R, EURO OUT L/R, DELAY OUT L/R, Headphones",
    ],
    "filter_modes": {
        "HP_LP_SERIES": {
            "description": "Mixer → VCF1 (HP) → VCF2 (LP) mono → both VCAs",
            "use": "Band-pass foundation",
        },
        "LP_LP_STEREO": {
            "description": "Mixer → VCF1 LP → VCA1; Mixer → VCF2 LP → VCA2",
            "use": "True stereo path from filters onward",
        },
        "HP_LP_PARALLEL": {
            "description": "Mixer → VCF1 HP + VCF2 LP summed mono → both VCAs",
            "use": "Notch foundation",
        },
    },
    "modulation_hardwired": {
        "mod_wheel_scales": ["PITCH AMT", "CUTOFF AMT", "PULSE WIDTH AMT"],
        "note": "AMT knobs set maximum; MOD wheel applies 0–100% of those amounts.",
    },
    "keyboard_cv": {
        "hardwired_pitch": True,
        "hardwired_velocity": False,
        "hardwired_aftertouch": False,
        "rear_outs": [
            "KB CV OUT",
            "KB GATE OUT",
            "KB VEL OUT",
            "KB AT OUT",
            "MOD WHL OUT",
            "EXP CV OUT",
        ],
    },
}

SPECS = {
    "keys": {"count": 49, "type": "Full-size Fatar", "velocity": True, "aftertouch": "channel"},
    "polyphony": ["1-note monophonic", "2-note paraphonic", "4-note paraphonic"],
    "sound_sources": [
        "4 oscillators (Linear FM; OSC2–4 Hard Sync)",
        "White noise generator",
        "External instrument input",
    ],
    "filters": {
        "count": 2,
        "type": "Moog analog ladder",
        "slope": "-24 dB/octave",
        "resonance": "self-oscillating",
        "modes": ["Series HP/LP", "Stereo LP/LP", "Parallel HP/LP"],
    },
    "envelopes": "2 × ADSR (Attack/Decay/Release 2 ms–10 s)",
    "mod_sources": [
        "Main modulation oscillator: Sine, Saw, Ramp, Square, Staircase, Smooth Random; Noise; S/H",
        "Utilities LFO: Triangle + Square simultaneous",
    ],
    "attenuators": 3,
    "mults": "2 sets of 4 parallel unbuffered jacks",
    "effects": "Stereo analog delay, ping-pong, MIDI sync, tap tempo",
    "arp_seq": {"sequences": 12, "max_steps": 256},
    "patch_points": {
        "total": 90,
        "inputs": 49,
        "outputs": 33,
        "mults": "8 (4×2)",
        "size_mm": 3.5,
    },
    "audio_io": {
        "main_out": "1/4\" TRS impedance-balanced L/R @ +4 dBu (L mono-normalled)",
        "headphones": "1/4\" TRS, independent volume (~1.1 V into 16 Ω)",
        "instrument_in": "1/4\" TS, +20 dB gain",
        "euro_out": "3.5 mm L/R 10 V p-p (not MAIN VOLUME)",
        "delay_out": "3.5 mm L/R wet 10 V p-p",
    },
    "midi": ["DIN In", "DIN Out", "DIN Thru", "USB MIDI"],
    "pedals": ["Sustain (TS, normally open)", "Expression (TRS, +5 V on ring)"],
    "dimensions": {
        "width": "32 in / 81.28 cm",
        "depth": "14.25 in / 36.19 cm",
        "height": "5.5 in / 13.97 cm",
        "weight": "30 lb / 13.61 kg",
    },
    "power": {
        "adapter": "12 V DC tip-positive, 2 A",
        "mains": "100–240 V AC, 50/60 Hz",
    },
}
