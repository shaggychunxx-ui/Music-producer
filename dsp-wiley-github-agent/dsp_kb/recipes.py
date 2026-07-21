"""Study / engineering recipes aligned with the book."""

from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "study_path": {
        "title": "Recommended study path",
        "steps": [
            "Skim Ch.1 for the digital audio ecosystem.",
            "Master Ch.2 quantization + dither + noise shaping (do exercises/applet).",
            "Ch.3 AD/DA and oversampling/ΔΣ intuition.",
            "Ch.4 platforms/interfaces enough to know real-time constraints.",
            "Algorithms: EQ (5) → reverb (6) → dynamics (7) → SRC (8) → coding (9).",
            "Use http://ant.hsu-hh.de/dasp/ demos and Matlab examples.",
            "For effects beyond basics, continue with DAFX (dafx.de).",
        ],
    },
    "dither_workflow": {
        "title": "Word-length reduction with dither",
        "steps": [
            "Identify target word-length (e.g. 24→16 bit).",
            "Choose dither PDF/amplitude per Ch.2 guidance.",
            "Add dither, then requantize.",
            "Optional: apply noise shaping for psychoacoustic noise placement.",
            "Verify absence of harmonic distortion at low levels; check noise floor.",
        ],
    },
    "design_eq": {
        "title": "Real-time parametric EQ design checklist",
        "steps": [
            "Specify fs, band type (peak/shelf), Fc, gain dB, Q/BW.",
            "Use recursive parametric structure from Ch.5 (biquad cascade).",
            "Check pole radii under coefficient quantization (fixed-point if applicable).",
            "Listen/measure magnitude response; watch for zipper noise when automating coeffs.",
            "For linear-phase graphic/long FIR needs, switch to FIR + fast convolution.",
        ],
    },
    "reverb_layers": {
        "title": "Build a layered artificial reverb",
        "steps": [
            "Early reflections: sparse tapped delays (Gerzon/Ando-style ideas) with gains/pans.",
            "Late reverb: Schroeder parallel combs + allpasses or feedback allpass/FDN-style nets.",
            "Set decay times vs frequency (damping) to avoid metallic ringing.",
            "Optional wet path: convolve measured RIR with partitioned fast convolution.",
            "Mix dry/wet; mono/stereo compatibility check.",
        ],
    },
    "compressor": {
        "title": "Implement a basic compressor",
        "steps": [
            "Level detector: peak or smoothed RMS-like envelope (Ch.7).",
            "Static curve: threshold, ratio, knee; compute desired gain.",
            "Smooth gain with attack/release time constants.",
            "Apply gain; add makeup; stereo-link detectors for L/R.",
            "Test with speech/music; avoid pumping via timing/tweak curve.",
        ],
    },
    "src_rational": {
        "title": "Synchronous (rational) sample-rate convert",
        "steps": [
            "Factor ratio L/M; upsample by L (zero-insert) + anti-image LPF.",
            "Downsample by M after anti-alias LPF (combine filters when possible).",
            "Prefer multistage for large L or M (Ch.8).",
            "Polyphase implementation for efficiency.",
        ],
    },
    "src_async": {
        "title": "Asynchronous SRC sketch",
        "steps": [
            "Track fractional read pointer between input clock domain samples.",
            "Interpolate (polyphase FIR or polynomial/Lagrange/spline).",
            "Control filter set / phase from timing estimator (Ch.8.3).",
            "Validate image/alias rejection and jitter sensitivity.",
        ],
    },
    "perceptual_coding": {
        "title": "Lossy coding pipeline map (MPEG-style)",
        "steps": [
            "Time→frequency via analysis filter bank / MDCT-style transforms (Ch.9).",
            "Psychoacoustic model: thresholds from masking + absolute threshold.",
            "Dynamic bit allocation: quantize bands to hide noise under mask.",
            "Entropy code side info + residual; pack bitstream.",
            "Optional tools: joint stereo, prediction, SBR for HF extension.",
        ],
    },
    "fixed_vs_float": {
        "title": "Choose fixed- vs floating-point for an algorithm",
        "steps": [
            "Estimate dynamic range and headroom needs (Ch.2.4).",
            "Fixed-point: plan scaling at each node; analyze roundoff noise growth.",
            "Float: simpler scaling; watch denormals and conversion to integer I/O.",
            "Benchmark on target DSP class from Ch.4.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "study": "study_path",
        "dither": "dither_workflow",
        "eq": "design_eq",
        "equalizer": "design_eq",
        "reverb": "reverb_layers",
        "dynamics": "compressor",
        "comp": "compressor",
        "src": "src_rational",
        "resample": "src_rational",
        "async": "src_async",
        "coding": "perceptual_coding",
        "mpeg": "perceptual_coding",
        "float": "fixed_vs_float",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
