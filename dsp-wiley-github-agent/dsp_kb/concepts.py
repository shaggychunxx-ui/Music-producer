"""Core DASP concepts from Zölzer 2e."""

from __future__ import annotations

from typing import Any

CONCEPTS: dict[str, dict[str, Any]] = {
    "quantization": {
        "name": "Signal quantization",
        "chapter": 2,
        "summary": (
            "AD path samples continuous x(t) then quantizes amplitudes to finite levels. "
            "Model often writes x_Q(n)=x(n)+e(n). Under suitable conditions error is "
            "approximately white with variance Q²/12 for step size Q."
        ),
        "related": ["dither", "noise_shaping", "fixed_point", "floating_point"],
    },
    "dither": {
        "name": "Dither",
        "chapter": 2,
        "summary": (
            "Noise added before (re)quantization to decorrelate error from signal, "
            "suppressing harmonic distortion and improving low-level linearity. "
            "Implementation choices trade noise floor vs. residual correlation."
        ),
        "related": ["quantization", "noise_shaping"],
    },
    "noise_shaping": {
        "name": "Noise shaping",
        "chapter": 2,
        "summary": (
            "Error feedback filter reshapes the spectrum of quantization noise, typically "
            "pushing energy out of sensitive bands (and often toward higher frequencies "
            "where hearing is less sensitive after oversampling)."
        ),
        "related": ["dither", "delta_sigma", "oversampling"],
    },
    "fixed_point": {
        "name": "Fixed-point arithmetic",
        "chapter": 2,
        "summary": (
            "Integer fractional representation with fixed scale. Predictable, efficient on "
            "fixed-point DSPs; careful scaling required to avoid overflow and limit roundoff noise."
        ),
        "related": ["floating_point", "quantization"],
    },
    "floating_point": {
        "name": "Floating-point arithmetic",
        "chapter": 2,
        "summary": (
            "Mantissa+exponent representation widens dynamic range; relative precision "
            "roughly constant. Simplifies some algorithms; format conversions still need care."
        ),
        "related": ["fixed_point"],
    },
    "oversampling": {
        "name": "Oversampling",
        "chapter": 3,
        "summary": (
            "Sample well above 2B to relax analog anti-alias/image filters and spread "
            "quantization noise over wider bandwidth before digital filtering/decimation."
        ),
        "related": ["delta_sigma", "nyquist"],
    },
    "delta_sigma": {
        "name": "Delta-sigma (ΔΣ) conversion",
        "chapter": 3,
        "summary": (
            "High-rate 1-bit (or few-bit) conversion with loop filter noise shaping; "
            "digital decimation/interpolation completes AD/DA. Dominant in modern audio converters."
        ),
        "related": ["oversampling", "noise_shaping"],
    },
    "nyquist": {
        "name": "Nyquist sampling",
        "chapter": 3,
        "summary": "Bandlimited sampling at ≥2B; ideal reconstruction with sinc; practical systems need anti-alias filters.",
        "related": ["oversampling", "src"],
    },
    "aes_ebu": {
        "name": "AES/EBU interface",
        "chapter": 4,
        "summary": "Professional two-channel digital audio interconnect used in studio systems.",
        "related": ["madi", "dsp_systems"],
    },
    "madi": {
        "name": "MADI",
        "chapter": 4,
        "summary": "Multichannel Audio Digital Interface for high channel-count digital links.",
        "related": ["aes_ebu"],
    },
    "parametric_eq": {
        "name": "Parametric / recursive equalizers",
        "chapter": 5,
        "summary": (
            "IIR structures realizing peaking/shelving filters with continuous control of "
            "frequency, gain, and bandwidth. Efficient for real-time multi-band EQ; "
            "must manage coefficient quantization and stability."
        ),
        "related": ["fir_eq", "filter_quantization"],
    },
    "fir_eq": {
        "name": "Nonrecursive (FIR) equalizers / fast convolution",
        "chapter": 5,
        "summary": (
            "FIR filters enable linear phase; long FIRs implemented via FFT-based fast "
            "convolution (overlap methods). Frequency sampling designs and partitioned "
            "convolution control latency."
        ),
        "related": ["parametric_eq", "room_ir"],
    },
    "filter_quantization": {
        "name": "Filter coefficient quantization effects",
        "chapter": 5,
        "summary": "Finite word-length poles/zeros shift response; structure choice (e.g. biquad forms) mitigates noise and sensitivity.",
        "related": ["parametric_eq", "fixed_point"],
    },
    "room_simulation": {
        "name": "Room simulation / artificial reverb",
        "chapter": 6,
        "summary": (
            "Combine early reflections (geometry/perception-motivated delays/gains/panning) "
            "with late reverberation algorithms (Schroeder combs/allpasses, feedback systems) "
            "or convolve measured room impulse responses."
        ),
        "related": ["schroeder", "fir_eq"],
    },
    "schroeder": {
        "name": "Schroeder reverberator",
        "chapter": 6,
        "summary": "Classic structure: parallel comb filters feeding series allpasses to increase echo density with exponential decay.",
        "related": ["room_simulation"],
    },
    "dynamics": {
        "name": "Dynamic range control",
        "chapter": 7,
        "summary": (
            "Time-varying gain from level measurement mapped through a static curve "
            "(compress, limit, expand, gate) with attack/release smoothing. Applied "
            "throughout the production/transmission chain."
        ),
        "related": ["limiter", "compressor"],
    },
    "limiter": {
        "name": "Limiter",
        "chapter": 7,
        "summary": "High-ratio/ceiling dynamics processor preventing peaks above a threshold; special case of DRC implementation.",
        "related": ["dynamics", "compressor"],
    },
    "compressor": {
        "name": "Compressor / expander / gate",
        "chapter": 7,
        "summary": "Ratio-based gain reduction above threshold (comp) or expansion/gating below; combined systems cascade behaviors.",
        "related": ["dynamics"],
    },
    "src": {
        "name": "Sampling rate conversion",
        "chapter": 8,
        "summary": (
            "Change fs: upsample with anti-imaging LPF; downsample with anti-alias LPF. "
            "Synchronous (rational ratios) vs asynchronous (arbitrary/unlocked clocks). "
            "Interpolation via polyphase filters or polynomial/Lagrange/spline methods."
        ),
        "related": ["oversampling", "nyquist"],
    },
    "psychoacoustics": {
        "name": "Psychoacoustics for coding",
        "chapter": 9,
        "summary": (
            "Critical bands, absolute threshold of hearing, simultaneous and temporal masking "
            "determine which spectral components can be quantized coarsely or discarded."
        ),
        "related": ["lossy_coding", "mpeg"],
    },
    "lossless_coding": {
        "name": "Lossless audio coding",
        "chapter": 9,
        "summary": "Perfect reconstruction coding for storage/transport of high word-lengths without perceptual loss.",
        "related": ["lossy_coding"],
    },
    "lossy_coding": {
        "name": "Lossy perceptual audio coding",
        "chapter": 9,
        "summary": (
            "Analysis filter bank + psychoacoustic model + dynamic bit allocation + entropy coding. "
            "Trades irrelevance/redundancy for bitrate."
        ),
        "related": ["psychoacoustics", "mpeg", "sbr"],
    },
    "mpeg": {
        "name": "MPEG audio coding family",
        "chapter": 9,
        "summary": (
            "ISO MPEG-1 Layers; MPEG-2; AAC; MPEG-4 audio tools—evolution of filter banks, "
            "prediction, stereo coding, and efficiency."
        ),
        "related": ["lossy_coding", "sbr"],
    },
    "sbr": {
        "name": "Spectral Band Replication",
        "chapter": 9,
        "summary": "Parametric extension reconstructing high-frequency content from lower band, improving coding efficiency.",
        "related": ["lossy_coding", "mpeg"],
    },
}


def define(term: str) -> dict[str, Any]:
    key = term.strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")
    aliases = {
        "noise_shape": "noise_shaping",
        "dithering": "dither",
        "delta-sigma": "delta_sigma",
        "deltasigma": "delta_sigma",
        "sigma_delta": "delta_sigma",
        "eq": "parametric_eq",
        "equalizer": "parametric_eq",
        "reverb": "room_simulation",
        "reverberation": "room_simulation",
        "drc": "dynamics",
        "compression": "compressor",
        "sample_rate_conversion": "src",
        "resampling": "src",
        "aac": "mpeg",
        "mp3": "mpeg",
        "masking": "psychoacoustics",
        "aes": "aes_ebu",
        "float": "floating_point",
        "fixed": "fixed_point",
        "fir": "fir_eq",
        "iir": "parametric_eq",
        "convolution": "fir_eq",
    }
    key = aliases.get(key, key)
    if key not in CONCEPTS:
        for k, v in CONCEPTS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown concept '{term}'. Try: {', '.join(list(CONCEPTS)[:20])}…")
    return CONCEPTS[key]
