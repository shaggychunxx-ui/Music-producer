from __future__ import annotations

from typing import Any

CONCEPTS: dict[str, dict[str, Any]] = {
    "sinusoid": {
        "name": "Sinusoid",
        "chapter": 1,
        "summary": "Pure tone with amplitude, frequency, phase; basis of additive synthesis and Fourier thinking.",
    },
    "amplitude": {
        "name": "Amplitude measures",
        "chapter": 1,
        "summary": "Peak vs RMS; dB units for perceptual/level control; envelope generators shape amplitude over time.",
    },
    "additive_synthesis": {
        "name": "Additive synthesis",
        "chapter": 1,
        "summary": "Sum of sinusoids (possibly time-varying amps/freqs) to build spectra; e.g. major triad, Risset constructions.",
    },
    "wavetable": {
        "name": "Wavetable oscillator",
        "chapter": 2,
        "summary": "Cycle through a stored table with a phase index; frequency = table speed. Cross-fade tables for morphing.",
    },
    "sampling": {
        "name": "Sampling / sample playback",
        "chapter": 2,
        "summary": "Read recorded audio with variable rate; transpose stretches spectrum; envelopes and loops sustain.",
    },
    "interpolation": {
        "name": "Interpolation",
        "chapter": 2,
        "summary": "Fractional table/delay reads need interpolation (linear, 4-point, etc.) for fidelity.",
    },
    "sampling_theorem": {
        "name": "Sampling theorem",
        "chapter": 3,
        "summary": "Bandlimited signals require fs > 2B; violations cause foldover/aliasing.",
    },
    "control_vs_audio": {
        "name": "Control vs audio computation",
        "chapter": 3,
        "summary": "Audio: dense sample streams. Control: sparse timed numbers/events. Conversion needs smoothing.",
    },
    "envelope": {
        "name": "Envelope generator",
        "chapter": 4,
        "summary": "Time functions (ADSR, line segments, curves) controlling amplitude or other params.",
    },
    "polyphony": {
        "name": "Polyphony / voice management",
        "chapter": 4,
        "summary": "Allocate limited voices to notes; tags track which voice is which; steal/release policies.",
    },
    "ring_modulation": {
        "name": "Ring modulation",
        "chapter": 5,
        "summary": "Multiply two audio signals; produces sum and difference frequencies; no original carriers if pure RM.",
    },
    "waveshaping": {
        "name": "Waveshaping",
        "chapter": 5,
        "summary": "Nonlinear map f(x) applied sample-wise; Chebyshev polynomials give controlled harmonic spectra.",
    },
    "fm": {
        "name": "Frequency / phase modulation",
        "chapter": 5,
        "summary": "Modulate carrier phase/frequency with modulator; rich sidebands related to Bessel functions of modulation index.",
    },
    "paf": {
        "name": "Phase-aligned formant (PAF)",
        "chapter": 6,
        "summary": "Designer-spectrum technique for movable formant peaks with coherent phase.",
    },
    "pulse_train": {
        "name": "Pulse trains",
        "chapter": 6,
        "summary": "Periodic impulses/pulses as harmonic-rich sources via waveshaping or wavetable methods.",
    },
    "delay_network": {
        "name": "Delay networks",
        "chapter": 7,
        "summary": "Combinations of delays and gains; feedforward/feedback combs; recirculation for resonance/reverb.",
    },
    "reverb": {
        "name": "Artificial reverberation",
        "chapter": 7,
        "summary": "Networks of delays/allpasses/combs approximating room energy decay; control density and color.",
    },
    "pitch_shift": {
        "name": "Pitch shifting via variable delay",
        "chapter": 7,
        "summary": "Time-varying delay read pointer changes instantaneous pitch (with artifacts to manage).",
    },
    "filter": {
        "name": "Digital filters",
        "chapter": 8,
        "summary": "Frequency-dependent gain/phase via elementary recirculating/non-recirculating delay structures.",
    },
    "allpass": {
        "name": "All-pass filter",
        "chapter": 8,
        "summary": "Approximately flat magnitude, useful phase response for reverb and dispersion.",
    },
    "fft_resynthesis": {
        "name": "Fourier analysis and resynthesis",
        "chapter": 9,
        "summary": "Frame-based spectral analysis (rfft) and reconstruction (rifft) for processing magnitudes/phases.",
    },
    "vocoder": {
        "name": "Timbre stamp / classical vocoder",
        "chapter": 9,
        "summary": "Impose spectral envelope of one sound onto another (carrier/modulator in channel vocoder spirit).",
    },
    "phase_vocoder": {
        "name": "Phase vocoder time bender",
        "chapter": 9,
        "summary": "Use phase derivatives across frames to time-stretch/compress without crude resampling.",
    },
    "foldover": {
        "name": "Foldover / aliasing of classical waves",
        "chapter": 10,
        "summary": "High harmonics of saw/square reflect below Nyquist; band-limit via oversampling or construction tricks.",
    },
    "classical_waveforms": {
        "name": "Classical waveforms",
        "chapter": 10,
        "summary": "Saw, square, triangle, parabolic—known Fourier series and symmetry properties.",
    },
}


def define(term: str) -> dict[str, Any]:
    key = term.strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")
    aliases = {
        "sine": "sinusoid",
        "rms": "amplitude",
        "db": "amplitude",
        "additive": "additive_synthesis",
        "sampler": "sampling",
        "sample": "sampling",
        "nyquist": "sampling_theorem",
        "control": "control_vs_audio",
        "adsr": "envelope",
        "voice": "polyphony",
        "ring": "ring_modulation",
        "rm": "ring_modulation",
        "waveshape": "waveshaping",
        "chebyshev": "waveshaping",
        "chebychev": "waveshaping",
        "phase_modulation": "fm",
        "pm": "fm",
        "formant": "paf",
        "delay": "delay_network",
        "comb": "delay_network",
        "reverberation": "reverb",
        "pitchshift": "pitch_shift",
        "lp": "filter",
        "hp": "filter",
        "bp": "filter",
        "fft": "fft_resynthesis",
        "stft": "fft_resynthesis",
        "phasevocoder": "phase_vocoder",
        "aliasing": "foldover",
        "saw": "classical_waveforms",
        "square": "classical_waveforms",
        "triangle": "classical_waveforms",
    }
    key = aliases.get(key, key)
    if key not in CONCEPTS:
        for k, v in CONCEPTS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown concept '{term}'. Try: {', '.join(list(CONCEPTS)[:15])}…")
    return CONCEPTS[key]
