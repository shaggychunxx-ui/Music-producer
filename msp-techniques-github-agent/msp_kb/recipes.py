from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "study_path": {
        "title": "Study path with Pd open",
        "steps": [
            "Install Pure Data; locate book examples in the Pd distribution.",
            "Ch.1: sine, dB, envelopes, additive triad.",
            "Ch.2: wavetable osc + simple sampler loop.",
            "Ch.3: control vs audio; tiny MIDI-style monophonic synth.",
            "Ch.4: ADSR + voice allocation sketch.",
            "Ch.5–6: ring mod, waveshaping, FM, then PAF/formants.",
            "Ch.7–8: comb/reverb, pitch shift; elementary filters.",
            "Ch.9–10: FFT FX; band-limited saw strategies.",
        ],
    },
    "sine_pd": {
        "title": "Basic Pd sine (Ch.1 mindset)",
        "steps": [
            "osc~ frequency → *~ amplitude → dac~.",
            "Use dbtorms for dB amplitude control.",
            "Smooth amplitude with line~/envelope to avoid clicks.",
            "Turn DSP on; watch levels.",
        ],
    },
    "wavetable_osc": {
        "title": "Wavetable oscillator",
        "steps": [
            "Fill table with one period (or load sample).",
            "phasor~ * table size → tabread4~ (or tabosc4~).",
            "Frequency sets phasor rate; interpolate reads.",
            "Optional cross-fade two tables for morphing.",
        ],
    },
    "risset_bell": {
        "title": "Risset-style additive bell (Ch.4 example family)",
        "steps": [
            "Several partials with inharmonic frequency ratios.",
            "Independent amplitude envelopes (longer for lower partials often).",
            "Sum partials; careful peak gain.",
            "Compare to pure harmonic additive.",
        ],
    },
    "ring_mod": {
        "title": "Ring modulation experiment",
        "steps": [
            "Two osc~ (or audio inputs) into *~.",
            "Listen for sum/difference; try harmonic vs inharmonic ratios.",
            "Optional filter after multiply.",
        ],
    },
    "fm_basic": {
        "title": "Simple FM/PM",
        "steps": [
            "Modulator osc → scale by modulation index → add to carrier phase/freq path.",
            "Sweep index; observe sideband richness.",
            "Keep carrier/modulator ratio rational for harmonic stacks, irrational for bell-like.",
        ],
    },
    "comb_reverb": {
        "title": "Delay network starter reverb",
        "steps": [
            "Parallel recirculating combs with coprime delay times.",
            "Series allpasses for echo density.",
            "Control feedback < 1 for stability; damp high frequencies if available.",
            "Mind Pd delwrite~/delread~ order and minimum delay.",
        ],
    },
    "pitch_shift_delay": {
        "title": "Pitch shift with variable delay",
        "steps": [
            "Write input to delay line; read with time-varying delay.",
            "Triangle/saw modulation of delay for pitch; overlap two readers to reduce dropouts.",
            "Expect artifacts; compare to phase-vocoder method (Ch.9).",
        ],
    },
    "fft_noise_gate": {
        "title": "Narrow-band companding / noise suppress idea",
        "steps": [
            "rfft~ analysis frames.",
            "Attenuate low-magnitude bins (noise floor).",
            "rifft~ resynthesize; window/overlap correctly.",
        ],
    },
    "bandlimit_saw": {
        "title": "Avoid sawtooth foldover",
        "steps": [
            "Do not naive wrap phasor as audio at high pitches.",
            "Use oversampling, additive band-limited construction, or transition splicing (Ch.10).",
            "Verify at high MIDI notes for aliasing grit.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "study": "study_path",
        "sine": "sine_pd",
        "pd": "sine_pd",
        "wavetable": "wavetable_osc",
        "bell": "risset_bell",
        "risset": "risset_bell",
        "rm": "ring_mod",
        "ring": "ring_mod",
        "fm": "fm_basic",
        "reverb": "comb_reverb",
        "delay": "comb_reverb",
        "pitch": "pitch_shift_delay",
        "pitchshift": "pitch_shift_delay",
        "fft": "fft_noise_gate",
        "vocoder": "fft_noise_gate",
        "saw": "bandlimit_saw",
        "aliasing": "bandlimit_saw",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
