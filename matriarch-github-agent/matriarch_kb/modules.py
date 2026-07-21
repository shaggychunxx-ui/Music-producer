"""Front/rear modules: controls, patch points, behavior."""

from __future__ import annotations

from typing import Any

MODULES: dict[str, dict[str, Any]] = {
    "keyboard": {
        "id": "keyboard",
        "name": "Keyboard",
        "summary": "49-note Fatar keyboard with velocity and channel aftertouch.",
        "controls": [],
        "notes": [
            "Velocity and aftertouch are not hardwired to the synth engine.",
            "Access via rear KB VEL OUT / KB AT OUT and MIDI.",
            "Use Utilities Mults + Attenuators to fan out KB CV / Vel / AT.",
        ],
        "patch_points": [],
    },
    "lhc": {
        "id": "lhc",
        "name": "Left-Hand Controller",
        "summary": "Pitch bend, mod wheel, glide, arp/seq transport.",
        "controls": [
            {"name": "PLAY", "type": "button", "color": "green", "function": "Arm/disarm Arp or Sequencer"},
            {"name": "HOLD", "type": "button", "color": "blue", "function": "Latch Arp/Seq; acts as sustain when Arp/Seq idle"},
            {"name": "TAP", "type": "button", "color": "yellow", "function": "Tap tempo for Arp/Seq; hold to exit tap mode"},
            {"name": "PITCH", "type": "wheel", "function": "Spring-loaded pitch bend"},
            {"name": "MOD", "type": "wheel", "function": "0–max of PITCH/CUTOFF/PULSE WIDTH AMT"},
            {"name": "GLIDE", "type": "knob", "range": "0 ~ 10 s", "function": "Portamento time"},
        ],
        "shortcuts": [
            "SHIFT + <KB / KB> : octave transpose ±2",
            "HOLD+PLAY+TAP : reset default octave",
            "HOLD+PLAY+TAP hold 1s : MIDI panic",
            "SHIFT + GLIDE right/left : Legato Glide On/Off (default Off)",
            "When TAP lit, RATE selects clock divisions of tap tempo",
        ],
        "patch_points": [],
    },
    "oscillators": {
        "id": "oscillators",
        "name": "Oscillators",
        "summary": "Four nearly identical analog VCOs; OSC2–4 have FREQUENCY and SYNC.",
        "provenance": "Minimoog Voyager / 921",
        "controls": [
            {"name": "OCTAVE", "per": "each OSC", "positions": ["16'", "8'", "4'", "2'"]},
            {"name": "FREQUENCY", "per": "OSC 2/3/4", "default_range": "±7 semitones (global 0–24)"},
            {"name": "WAVEFORM", "per": "each", "positions": ["Triangle", "Sawtooth", "Square", "Narrow Pulse"]},
            {"name": "SYNC ENABLE", "type": "button", "color": "red", "function": "Master enable for individual sync buttons"},
            {"name": "1→2 SYNC", "type": "button", "function": "OSC2 hard-synced to OSC1; expands FREQUENCY range"},
            {"name": "2→3 SYNC", "type": "button", "function": "OSC3 hard-synced to OSC2"},
            {"name": "3→4 SYNC", "type": "button", "function": "OSC4 hard-synced to OSC3"},
            {"name": "FINE TUNE", "location": "rear", "range": "±1 semitone global"},
        ],
        "waveforms": {
            "Triangle": "Strong fundamental, odd harmonics low — flutes, soft tones",
            "Sawtooth": "All natural harmonics strong — brass, leads, bass",
            "Square": "50% pulse, hollow — clarinet/bass",
            "Narrow Pulse": "Reedy/nasal — oboe, clav; PWM for chorus",
        },
        "sync_notes": [
            "Hard sync resets slave phase to master each cycle → complex harmonics.",
            "If slave frequency is below master, slave may not complete a cycle (little/no sound).",
            "Modulating slave pitch enhances sync effect.",
        ],
        "patch_points": [
            {"jack": "PITCH IN", "dir": "in", "range": "−5 to +5 V (1 V/Oct)", "notes": "Cascades to subsequent OSCs unless they have their own PITCH IN; dead-patch breaks chain"},
            {"jack": "LIN FM IN", "dir": "in", "range": "−5 to +5 V AC-coupled", "notes": "Linear FM — metallic/bell tones"},
            {"jack": "PWM IN", "dir": "in", "range": "−5 to +5 V", "notes": "Affects Square/Narrow Pulse only"},
            {"jack": "WAVE OUT", "dir": "out", "range": "10 V p-p", "notes": "Per oscillator audio"},
        ],
    },
    "mixer": {
        "id": "mixer",
        "name": "Mixer",
        "summary": "Blends OSC1–4 + Noise (and rear Instrument In) into the filter.",
        "provenance": "Moog CP3",
        "controls": [
            {"name": "NOISE", "type": "knob", "notes": ">11 o'clock gentle drive; higher = overdrive"},
            {"name": "OSCILLATOR 1–4", "type": "knob", "notes": "Same drive behavior as Noise"},
        ],
        "notes": [
            "DC-coupled — can sum CVs as well as audio.",
            "Paraphonic modes: mix gates mute unused OSC channels (external sources muted similarly).",
            "Noise HPF color via Global Settings.",
        ],
        "patch_points": [
            {"jack": "NOISE IN", "dir": "in", "range": "10 V p-p", "notes": "Replaces noise generator"},
            {"jack": "OSC 1–4 IN", "dir": "in", "range": "10 V p-p", "notes": "Replaces that oscillator into mixer"},
            {"jack": "OUTPUT", "dir": "out", "range": "10 V p-p", "notes": "Sum of mixer sources"},
        ],
    },
    "filters": {
        "id": "filters",
        "name": "Filters",
        "summary": "Dual ladder VCFs with linked CUTOFF and bipolar SPACING.",
        "provenance": "Moog 904A",
        "controls": [
            {"name": "CUTOFF", "type": "knob", "range": "~20 Hz–20 kHz", "notes": "Linked for both VCFs"},
            {"name": "SPACING", "type": "knob", "bipolar": True, "notes": "Offsets VCF1 only vs VCF2"},
            {"name": "FILTER MODE", "type": "switch", "positions": ["HP/LP SERIES", "LP/LP STEREO", "HP/LP PARALLEL"]},
            {"name": "RESONANCE 1", "type": "knob", "notes": "~3 o'clock+ self-oscillates"},
            {"name": "RESONANCE 2", "type": "knob"},
            {"name": "ENVELOPE AMT", "type": "knob", "bipolar": True, "notes": "Filter EG → cutoff; inverse when CCW"},
            {"name": "KB TRACKING", "type": "knob", "notes": "Max = 1 V/Oct tracking"},
        ],
        "modes": {
            "HP/LP SERIES": "Band-pass foundation; mono to both VCAs",
            "LP/LP STEREO": "True stereo dual LP",
            "HP/LP PARALLEL": "Notch foundation; summed mono",
        },
        "patch_points": [
            {"jack": "VCF 1 IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "VCF 2 IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "VCF 1 OUT", "dir": "out", "range": "10 V p-p"},
            {"jack": "VCF 2 OUT", "dir": "out", "range": "10 V p-p"},
            {"jack": "CUTOFF 1 IN", "dir": "in", "range": "−5 to +5 V", "notes": "Normalled to CUTOFF 2; dead-patch isolates VCF2"},
            {"jack": "CUTOFF 2 IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "ENV AMT IN", "dir": "in", "range": "−5 to +5 V"},
        ],
    },
    "envelopes": {
        "id": "envelopes",
        "name": "Envelope Generators (ADSR)",
        "summary": "Filter EG + Amplitude EG, identical stage controls.",
        "provenance": "Moog 911",
        "controls": [
            {"name": "ATTACK", "range": "2 ms – 10 s"},
            {"name": "DECAY", "range": "2 ms – 10 s"},
            {"name": "SUSTAIN", "type": "slider", "notes": "Level, not time"},
            {"name": "RELEASE", "range": "2 ms – 10 s"},
        ],
        "patch_points": [
            {"jack": "ENV OUT (Filter)", "dir": "out", "range": "0 to +8 V"},
            {"jack": "ENV END OUT (Filter)", "dir": "out", "range": "0 to +5 V", "notes": "Gate after envelope completes; loop via TRIGGER IN"},
            {"jack": "TRIGGER IN (Filter)", "dir": "in", "range": "0 to +8 V", "threshold": ">2.3 V", "notes": "Overrides keyboard gate"},
            {"jack": "ENV OUT (Amp)", "dir": "out", "range": "0 to +8 V"},
            {"jack": "ENV END OUT (Amp)", "dir": "out", "range": "0 to +8 V"},
            {"jack": "TRIGGER IN (Amp)", "dir": "in", "range": "0 to +8 V", "threshold": ">2.3 V"},
        ],
        "tips": [
            "Invert EG: ENV OUT → Attenuator INPUT, ATTENUATOR fully CCW, take OUTPUT.",
            "Looping EG: ENV END OUT → same EG TRIGGER IN.",
        ],
    },
    "output": {
        "id": "output",
        "name": "Output / VCAs",
        "summary": "Dual VCAs before delay; MAIN VOLUME and VCA MODE.",
        "provenance": "Moog 902",
        "controls": [
            {"name": "MAIN VOLUME", "notes": "Affects MAIN OUT only (not Euro/Headphones)"},
            {
                "name": "VCA MODE",
                "positions": {
                    "AMP ENV": "Both VCAs from Amplitude EG",
                    "SPLIT": "VCA1 = Filter EG; VCA2 = Amp EG",
                    "DRONE": "Constant level (keys optional); CV 0–+8 V sets level",
                },
            },
        ],
        "patch_points": [
            {"jack": "VCA 1 IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "VCA 2 IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "VCA 1 CV IN", "dir": "in", "range": "−8 to +8 V (ENV/SPLIT); 0 to +8 V (DRONE)"},
            {"jack": "VCA 2 CV IN", "dir": "in", "range": "−8 to +8 V (ENV/SPLIT); 0 to +8 V (DRONE)"},
        ],
    },
    "stereo_delay": {
        "id": "stereo_delay",
        "name": "Stereo Delay",
        "summary": "Two BBD analog delays after the VCAs.",
        "provenance": "Moog 500 Series Analog Delay",
        "controls": [
            {"name": "TIME", "range": "35–780 ms (longer via tap/patch, lo-fi)"},
            {"name": "SPACING", "bipolar": True, "notes": "Offsets Delay1 vs Delay2; clock divisions when synced"},
            {"name": "FEEDBACK", "notes": "~2 o'clock+ self-oscillation"},
            {"name": "MIX", "notes": "CCW dry, CW 100% wet delay"},
            {"name": "SYNC/TAP", "type": "button", "notes": "Tap = hold to enter; Sync = press; green LED = arp/seq clock, yellow = external"},
            {"name": "PING PONG", "type": "button", "color": "blue", "notes": "Delay1↔Delay2 feedback cross"},
        ],
        "patch_points_front": [
            {"jack": "INPUT 1", "dir": "in", "range": "10 V p-p", "notes": "Replaces VCA1 → Delay1 (L)"},
            {"jack": "INPUT 2", "dir": "in", "range": "10 V p-p", "notes": "Replaces VCA2 → Delay2 (R)"},
            {"jack": "FB CV IN", "dir": "in", "range": "−5 to +5 V", "notes": "Both delays unless rear FB2 used"},
            {"jack": "MIX IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "TIME 1 IN", "dir": "in", "range": "−5 to +5 V", "notes": "Bend vs divisions depends on DELAY CV SYNC BEND global"},
            {"jack": "TIME 2 IN", "dir": "in", "range": "−5 to +5 V"},
        ],
        "patch_points_rear": [
            {"jack": "DELAY OUT L/R", "dir": "out", "range": "10 V p-p wet"},
            {"jack": "SYNC IN", "dir": "in", "threshold": ">3.6 V rising"},
            {"jack": "DELAY FB 2 CV IN", "dir": "in", "range": "0 to +8 V", "notes": "Independent Delay2 feedback"},
        ],
    },
    "modulation": {
        "id": "modulation",
        "name": "Modulation",
        "summary": "Primary analog LFO / mod oscillator with hardwired destinations.",
        "controls": [
            {"name": "RATE", "range": "0.07 Hz – 1.3 kHz", "notes": "SHIFT for fine tune"},
            {"name": "WAVEFORM", "positions": ["Sine", "Sawtooth", "Ramp", "Square", "Staircase", "Smooth Random"]},
            {"name": "PITCH AMT", "notes": "Max pitch mod when MOD wheel full up"},
            {"name": "PITCH MOD ASSIGN", "positions": ["1&3", "All", "2&4"]},
            {"name": "CUTOFF AMT"},
            {"name": "PULSE WIDTH AMT", "notes": "Only when OSC wave is Square/Narrow Pulse"},
        ],
        "notes": [
            "Staircase = stepped triangle; steps held on ARP/SEQ clock rises.",
            "Square polarity bipolar/unipolar via Global Settings.",
        ],
        "patch_points": [
            {"jack": "RATE IN", "dir": "in", "range": "−5 to +5 V (1 V/Oct)"},
            {"jack": "SYNC IN", "dir": "in", "threshold": "rising >2.5 V (0–10 V)", "notes": "Resets wave / steps S/H"},
            {"jack": "NOISE OUT", "dir": "out", "range": "−8 to +8 V"},
            {"jack": "S/H OUT", "dir": "out", "range": "−8 to +8 V", "notes": "Must be patched; no internal route"},
            {"jack": "WAVE OUT", "dir": "out", "range": "10 V p-p"},
        ],
    },
    "utilities_1": {
        "id": "utilities_1",
        "name": "Utilities (1)",
        "summary": "4-jack unbuffered Mult + two bipolar voltage-controlled attenuators.",
        "patch_points": [
            {"jack": "MULT ×4", "dir": "io", "notes": "Passive split or passive mix of outputs"},
            {"jack": "ATTEN INPUT", "dir": "in", "range": "±8 V", "notes": "Normalled +8 V DC if unpatched"},
            {"jack": "ATTEN OUTPUT", "dir": "out", "range": "±8 V", "notes": "If ATT1 OUT free, sums into ATT2 OUT"},
            {"jack": "ATTEN CV IN", "dir": "in", "range": "±8 V"},
        ],
        "tips": [
            "Ring mod: OSC1 WAVE → INPUT, OSC2 WAVE → CV IN, take OUTPUT; center knob for classic RM.",
            "Center = full attenuate; CW = dry positive; CCW = inverted dry.",
        ],
    },
    "utilities_2": {
        "id": "utilities_2",
        "name": "Utilities (2)",
        "summary": "Mult + one attenuator + patchable LFO (Triangle & Square outs).",
        "controls": [
            {"name": "LFO RATE", "range": "0.07–520 Hz (up to ~620 Hz with CV)"},
        ],
        "patch_points": [
            {"jack": "MULT ×4", "dir": "io"},
            {"jack": "ATTEN INPUT/OUTPUT/CV IN", "dir": "io", "range": "±8 V"},
            {"jack": "RATE IN", "dir": "in", "range": "±8 V"},
            {"jack": "TRI OUT", "dir": "out", "range": "10 V p-p"},
            {"jack": "SQUARE OUT", "dir": "out", "range": "10 V p-p"},
        ],
    },
    "arp_seq": {
        "id": "arp_seq",
        "name": "Arpeggiator / Sequencer",
        "summary": "Arp + step sequencer (12 banks × 256 steps) with ties/rests/ratchets.",
        "controls": [
            {"name": "RATE", "range": "20–280 BPM", "notes": "Divisions when MIDI/ext/tap sync; SHIFT = triplets"},
            {"name": "MODE", "positions": ["ARP", "SEQ", "REC"]},
            {"name": "DIRECTION", "positions": ["ORD", "FW/BW", "RND"]},
            {"name": "OCT/BANK", "positions": ["1", "2", "3"], "notes": "Arp octaves or sequence banks"},
            {"name": "SEQUENCE", "type": "knob", "notes": "Select sequence within bank"},
            {"name": "REST / TIE / RATCHET", "type": "buttons", "notes": "Step entry; up to 8 ratchets/step"},
        ],
        "warnings": [
            "Entering REC with sequencer stopped and adding notes overwrites saved sequence permanently.",
            "Live REC while running can rewrite the current step in real time.",
        ],
        "patch_points": [
            {"jack": "ARP RATE/DIV IN", "dir": "in", "range": "−5 to +5 V"},
            {"jack": "VELOCITY OUT", "dir": "out", "range": "0–5 V (0–10 global)"},
            {"jack": "CV OUT", "dir": "out", "range": "−5–+5 V (0–10 global)"},
            {"jack": "GATE OUT", "dir": "out", "range": "+5 V (+10 global)"},
        ],
        "rear_jacks": [
            {"jack": "CLOCK IN", "threshold": ">3.6 V rising", "modes": ["Clock", "Step-advance (global)"]},
            {"jack": "ON/OFF IN", "notes": "<1 V stop; >3.6 V start/arm"},
            {"jack": "RESET IN", "threshold": ">2.5 V rising"},
            {"jack": "CLOCK OUT", "range": "0–10 V", "notes": "PPQN via globals"},
        ],
    },
    "paraphony": {
        "id": "paraphony",
        "name": "Paraphony / Voice Mode",
        "summary": "Independent OSC pitch assignment with shared post-mixer path.",
        "controls": [
            {
                "name": "VOICE MODE",
                "positions": {
                    "1": "Mono — all 4 OSCs from one key",
                    "2": "Duo — key1: OSC1+2; key2: OSC3+4",
                    "4": "Quad — one OSC per key",
                },
            },
            {
                "name": "MULTI TRIG",
                "type": "button",
                "on": "EG retriggers every new key",
                "off": "Legato — no retrig until all keys released",
            },
        ],
        "notes": [
            "Each OSC has a pre-mixer gate muting unused voices.",
            "Round-robin / stolen-voice / paraphonic unison via Global Settings group 4.",
        ],
    },
    "rear_panel": {
        "id": "rear_panel",
        "name": "Rear Panel",
        "summary": "Power, fine tune, audio, delay, keyboard CV, arp/seq clock, MIDI.",
        "sections": {
            "power": ["12V DC tip-positive", "POWER switch", "Kensington slot", "FINE TUNE ±1 st"],
            "audio": ["MAIN OUT L/R", "HEADPHONE + volume", "INSTRUMENT IN", "EURO OUT L/R"],
            "delay": ["DELAY OUT L/R", "SYNC IN", "DELAY FB 2 CV IN"],
            "keyboard": [
                "SUS PEDAL IN",
                "EXP PEDAL IN / EXP CV OUT (0–+8 V)",
                "KB VEL OUT",
                "KB AT OUT",
                "MOD WHL OUT",
                "KB CV OUT",
                "KB GATE OUT",
            ],
            "arp_seq": ["CLOCK IN", "ON/OFF IN", "RESET IN", "CLOCK OUT"],
            "midi": ["DIN IN", "THRU", "OUT", "USB", "MIDI LED"],
        },
    },
}


def list_modules() -> list[str]:
    return list(MODULES.keys())


def get_module(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "osc": "oscillators",
        "oscs": "oscillators",
        "vcf": "filters",
        "filter": "filters",
        "eg": "envelopes",
        "adsr": "envelopes",
        "vca": "output",
        "delay": "stereo_delay",
        "lfo": "modulation",
        "mod": "modulation",
        "util": "utilities_1",
        "utilities": "utilities_1",
        "arp": "arp_seq",
        "seq": "arp_seq",
        "sequencer": "arp_seq",
        "voice": "paraphony",
        "rear": "rear_panel",
    }
    key = aliases.get(key, key)
    if key not in MODULES:
        raise KeyError(f"Unknown module '{name}'. Try: {', '.join(list_modules())}")
    return MODULES[key]
