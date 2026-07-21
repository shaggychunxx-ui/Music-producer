"""Starter patch / performance recipes from manual principles."""

from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "setup": {
        "title": "First power-up & monitoring",
        "steps": [
            "Connect 12 V tip-positive adapter; power on.",
            "Warm up 10–15 minutes (longer if cold-stored).",
            "MAIN VOLUME fully down; cable MAIN OUT L (mono) or L+R stereo to amp/interface.",
            "Raise MAIN VOLUME past 12 o'clock; set amp gain.",
            "Optional: headphones use rear HEADPHONE VOLUME (independent of MAIN).",
        ],
    },
    "bass": {
        "title": "Thick monophonic bass",
        "steps": [
            "VOICE MODE = 1; MULTI TRIG as preferred.",
            "OSC1 Saw 8'; OSC2 Saw slightly detuned; levels just into gentle drive (~11–1 o'clock).",
            "Filter LP-friendly mode (LP/LP STEREO or Series with spacing for thickness).",
            "CUTOFF mid-low; RES modest; ENVELOPE AMT + some; Amp EG short attack, medium decay, low-mid sustain.",
            "Glide low for funk slides; optional PWM on one pulse OSC with MOD wheel.",
            "Delay MIX low or off for dry punch.",
        ],
    },
    "sync_lead": {
        "title": "Hard-sync lead",
        "steps": [
            "SYNC ENABLE on; 1→2 SYNC on.",
            "OSC1 carrier (Saw/Square); sweep OSC2 FREQUENCY for harmonic motion.",
            "Pitch-mod OSC2 via PITCH IN or MOD assign that includes OSC2; raise MOD wheel.",
            "Filter bright with resonance; Amp EG snappy attack.",
        ],
    },
    "paraphonic_pluck": {
        "title": "2-note paraphonic plucks into delay",
        "steps": [
            "VOICE MODE = 2; MULTI TRIG on for independent attacks.",
            "Sync pairs: 1→2 and 3→4; PITCH MOD ASSIGN = 2&4 so carriers stay in tune.",
            "Short Amp Attack/Decay, low Sustain; Filter EG short for pluck.",
            "Stereo Delay MIX ~10–2 o'clock; moderate feedback; optional PING PONG.",
            "TAP or SYNC delay to tempo.",
        ],
    },
    "bandpass": {
        "title": "Band-pass (Series HP/LP)",
        "steps": [
            "FILTER MODE = HP/LP SERIES.",
            "Use CUTOFF + SPACING so HP and LP edges form a band.",
            "Resonance on one or both for formant peaks.",
        ],
    },
    "notch": {
        "title": "Notch (Parallel HP+LP)",
        "steps": [
            "FILTER MODE = HP/LP PARALLEL.",
            "Offset with SPACING; resonate carefully.",
            "Useful for thinning midrange or phaser-like motion with LFO→CUTOFF.",
        ],
    },
    "ring_mod": {
        "title": "Attenuator ring modulation",
        "steps": [
            "Patch OSC1 WAVE OUT → Attenuator INPUT.",
            "Patch OSC2 WAVE OUT → same Attenuator CV IN.",
            "Take Attenuator OUTPUT to Mixer OSC IN (or VCF IN).",
            "ATTENUATOR at 12 o'clock for classic RM; offset for asymmetry.",
        ],
    },
    "sample_hold": {
        "title": "Keyboard-stepped Sample & Hold",
        "steps": [
            "Patch ARP/SEQ GATE OUT (or KB GATE) → MOD SYNC IN.",
            "Set Modulation RATE to minimum.",
            "Patch S/H OUT → CUTOFF 1 IN (or dead-patch CUTOFF 2 if mono control desired).",
            "Each key / step advances a new random voltage.",
        ],
    },
    "looping_eg": {
        "title": "Looping envelope LFO",
        "steps": [
            "Patch Filter ENV END OUT → Filter TRIGGER IN.",
            "Short Attack + Release for rhythmic pulses; longer for pads.",
            "Use ENV OUT to modulate cutoff, pitch, or delay time.",
        ],
    },
    "drone": {
        "title": "Drone pad",
        "steps": [
            "VCA MODE = DRONE; set levels carefully.",
            "Slow Amp/Filter EGs if returning to ENV mode later.",
            "High Delay FEEDBACK just below self-oscillation for wash.",
            "Mod LFO slow Sine to CUTOFF AMT with MOD wheel raised slightly.",
        ],
    },
    "external_fx": {
        "title": "Process external instrument",
        "steps": [
            "Plug source into rear INSTRUMENT IN (line/instrument; +20 dB).",
            "Raise a free Mixer channel or use level via noise/OSC IN if patched.",
            "Use filters, VCAs, delay as analog FX processor.",
            "Or break filter path: VCF INs as insert processors.",
        ],
    },
    "modular_front_end": {
        "title": "Keyboard front-end for Eurorack / Mother-32 / DFAM",
        "steps": [
            "KB CV / GATE / VEL / AT outs to modules (set voltage ranges in globals).",
            "CLOCK OUT / IN for analog sync; MIDI for DAW.",
            "EURO OUT for modular-level stereo returns.",
            "Local Control off if Matriarch is only a controller.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "mono_bass": "bass",
        "sync": "sync_lead",
        "para": "paraphonic_pluck",
        "duo": "paraphonic_pluck",
        "rm": "ring_mod",
        "s_h": "sample_hold",
        "sh": "sample_hold",
        "ext": "external_fx",
        "euro": "modular_front_end",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
