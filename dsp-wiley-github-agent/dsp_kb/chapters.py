"""Chapter map from Contents (2nd edition)."""

from __future__ import annotations

from typing import Any

CHAPTERS: dict[int, dict[str, Any]] = {
    1: {
        "number": 1,
        "title": "Introduction",
        "book_pages": "1–19",
        "pdf_start_approx": 15,
        "sections": {
            "1.1": "Studio Technology",
            "1.2": "Digital Transmission Systems (incl. OFDM/DAB/DRM, Internet audio)",
            "1.3": "Storage Media (CD, R-DAT, SACD, DVD-era specs)",
            "1.4": "Audio Components at Home (EQ, amps, Class-D, etc.)",
        },
        "key_points": [
            "Traces audio from studio recording through transmission/storage to home playback",
            "Digital mixing, multitrack, room simulators, broadcast (DAB OFDM)",
            "Optical/magnetic storage specs as historical benchmarks",
            "Sets context for why quantization, conversion, and coding matter",
        ],
    },
    2: {
        "number": 2,
        "title": "Quantization",
        "book_pages": "21–61",
        "pdf_start_approx": 35,
        "sections": {
            "2.1": "Signal Quantization (classical model, quantization theorem, error statistics)",
            "2.2": "Dither (basics, implementation, examples)",
            "2.3": "Spectrum Shaping of Quantization – Noise Shaping",
            "2.4": "Number Representation (fixed-point, floating-point, format conversion effects)",
            "2.5": "Java Applet – Quantization, Dither, and Noise Shaping",
            "2.6": "Exercises",
        },
        "key_points": [
            "Quantized signal = original + error; PDF and spectrum of error under model assumptions",
            "Uniform quantization noise power ~ Q²/12 for full-scale random model",
            "Dither randomizes/linearizes requantization; reduces correlated distortion",
            "Noise shaping moves error energy toward less audible bands",
            "Fixed-point vs floating-point: range, SNR behavior, algorithm sensitivity",
        ],
    },
    3: {
        "number": 3,
        "title": "AD/DA Conversion",
        "book_pages": "63–95",
        "pdf_start_approx": 77,
        "sections": {
            "3.1": "Methods (Nyquist sampling, oversampling, delta-sigma modulation)",
            "3.2": "AD Converters (specs, parallel, successive approx, counter, ΔΣ ADC)",
            "3.3": "DA Converters (specs, current/voltage sources, weighted R/C, R-2R, ΔΣ DAC)",
            "3.4": "Java Applet – Oversampling and Quantization",
            "3.5": "Exercises",
        },
        "key_points": [
            "Nyquist sampling needs anti-alias filtering; practical ADCs use oversampling",
            "ΔΣ: high sample rate, low bits, aggressive digital noise shaping + decimation",
            "Converter specs: linearity, SNR, THD, aperture, settling, etc.",
            "DAC architectures trade accuracy, matching, and speed",
        ],
    },
    4: {
        "number": 4,
        "title": "Audio Processing Systems",
        "book_pages": "97–113",
        "pdf_start_approx": 111,
        "sections": {
            "4.1": "Digital Signal Processors (fixed-point, floating-point)",
            "4.2": "Digital Audio Interfaces (two-channel AES/EBU, MADI)",
            "4.3": "Single-processor Systems (peripherals, control)",
            "4.4": "Multi-processor Systems (serial/parallel links, buses, scalable systems)",
        },
        "key_points": [
            "Real-time DASP runs on specialized DSP silicon with MAC-centric ISAs",
            "Professional interconnect: AES/EBU (stereo), MADI (multichannel)",
            "Scaling: multi-DSP topologies for large mixers/processors",
            "Later algorithm chapters assume such platforms for real-time demos",
        ],
    },
    5: {
        "number": 5,
        "title": "Equalizers",
        "book_pages": "115–189",
        "pdf_start_approx": 129,
        "sections": {
            "5.1": "Basics",
            "5.2": "Recursive Audio Filters (design, parametric structures, quantization effects)",
            "5.3": "Nonrecursive Audio Filters (fast convolution, long sequences, frequency sampling design)",
            "5.4": "Multi-complementary Filter Bank (principles; 8-band example)",
            "5.5": "Java Applet – Audio Filters",
            "5.6": "Exercises",
        },
        "key_points": [
            "IIR parametric EQ: efficient real-time boost/cut with controllable bandwidth",
            "Coefficient quantization and structure choice affect stability/noise",
            "FIR via FFT convolution for linear phase / long responses",
            "Partitioned/fast convolution manages latency for long filters",
            "Multi-complementary banks split spectrum for multi-band processing",
        ],
    },
    6: {
        "number": 6,
        "title": "Room Simulation",
        "book_pages": "191–223",
        "pdf_start_approx": 205,
        "sections": {
            "6.1": "Basics (room acoustics, model-based RIR, measurement, simulation)",
            "6.2": "Early Reflections (Ando, Gerzon algorithm)",
            "6.3": "Subsequent Reverberation (Schroeder, general feedback, feedback all-pass)",
            "6.4": "Approximation of Room Impulse Responses",
            "6.5": "Java Applet – Fast Convolution",
            "6.6": "Exercises",
        },
        "key_points": [
            "Perceptual split: early discrete reflections + dense late reverb tail",
            "Schroeder: comb filters + allpasses for dense exponential decay",
            "Feedback delay networks / allpass feedback for improved density/coloration control",
            "Measured RIRs rendered with (partitioned) fast convolution",
        ],
    },
    7: {
        "number": 7,
        "title": "Dynamic Range Control",
        "book_pages": "225–239",
        "pdf_start_approx": 239,
        "sections": {
            "7.1": "Basics",
            "7.2": "Static Curve",
            "7.3": "Dynamic Behavior (level measurement, gain smoothing, time constants)",
            "7.4": "Implementation (limiter; compressor/expander/noise gate; combinations)",
            "7.5": "Realization Aspects (sample-rate reduction, curve approximation, stereo)",
            "7.6": "Java Applet – Dynamic Range Control",
            "7.7": "Exercises",
        },
        "key_points": [
            "Used along mic→loudspeaker chain to fit recording/transmission/listening dynamics",
            "Static I/O curve defines ratio knees (comp/limit/expand/gate)",
            "Level detector (peak/RMS-like) + attack/release smoothing of gain",
            "Stereo linking avoids image shifts; efficiency tricks for real-time DSP",
        ],
    },
    8: {
        "number": 8,
        "title": "Sampling Rate Conversion",
        "book_pages": "241–271",
        "pdf_start_approx": 255,
        "sections": {
            "8.1": "Basics (upsample+anti-image; downsample+anti-alias)",
            "8.2": "Synchronous Conversion",
            "8.3": "Asynchronous Conversion (single-stage, multistage, control of interpolation filters)",
            "8.4": "Interpolation Methods (polynomial, Lagrange, spline)",
            "8.5": "Exercises",
        },
        "key_points": [
            "Integer-ratio SRC via expand/decimate + lowpass",
            "Async SRC for unlocked clocks / arbitrary rate ratios",
            "Multistage designs reduce filter cost at extreme ratios",
            "Polynomial/Lagrange/spline interpolators for continuous-time reconstruction viewpoint",
        ],
    },
    9: {
        "number": 9,
        "title": "Audio Coding",
        "book_pages": "273–315",
        "pdf_start_approx": 287,
        "sections": {
            "9.1": "Lossless Audio Coding",
            "9.2": "Lossy Audio Coding",
            "9.3": "Psychoacoustics (critical bands, absolute threshold, masking)",
            "9.4": "ISO-MPEG-1 Audio Coding (filter banks, psychoacoustic models, bit allocation)",
            "9.5": "MPEG-2 Audio Coding",
            "9.6": "MPEG-2 Advanced Audio Coding",
            "9.7": "MPEG-4 Audio Coding",
            "9.8": "Spectral Band Replication",
            "9.9": "Java Applet – Psychoacoustics",
            "9.10": "Exercises",
        },
        "key_points": [
            "Lossless: perfect reconstruction, used for high word-length archival/transport",
            "Lossy: remove perceptually irrelevant energy via masking models",
            "Critical bands / simultaneous & temporal masking drive bit allocation",
            "MPEG family evolution: Layer coding → AAC → MPEG-4 tools; SBR extends HF",
        ],
    },
}


def list_chapters() -> list[str]:
    return [f"{c['number']}. {c['title']}" for c in CHAPTERS.values()]


def get_chapter(ref: str | int) -> dict[str, Any]:
    if isinstance(ref, int) or (isinstance(ref, str) and str(ref).isdigit()):
        n = int(ref)
        if n not in CHAPTERS:
            raise KeyError(f"Chapter {n} not in 1–9")
        return CHAPTERS[n]
    q = str(ref).strip().lower()
    for c in CHAPTERS.values():
        if q in c["title"].lower():
            return c
    for c in CHAPTERS.values():
        if any(q in s.lower() for s in c["sections"].values()):
            return c
    raise KeyError(f"No chapter match for '{ref}'")
