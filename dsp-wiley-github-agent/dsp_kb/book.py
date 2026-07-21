"""Book metadata and pedagogy."""

BOOK = {
    "title": "Digital Audio Signal Processing",
    "edition": "Second Edition",
    "year": 2008,
    "author": "Udo Zölzer",
    "affiliation": "Helmut Schmidt University, Hamburg, Germany",
    "publisher": "John Wiley & Sons, Ltd",
    "isbn_note": "A John Wiley & Sons, Ltd, Publication",
    "prior": "First German edition Digitale Audiosignalverarbeitung (B. G. Teubner)",
    "source_url": (
        "https://shop.pearlacoustics.com/wp-content/uploads/woocommerce_uploads/"
        "2023/01/Wiley-Digital-Audio-Signal-Processing-2nd-Edition-82cqs3.pdf"
    ),
    "pdf_pages": 334,
    "course_sites": [
        "http://ant.hsu-hh.de/dasp/  (demos, exercises, Matlab)",
        "http://www.dafx.de  (DAFX – Digital Audio Effects companion book)",
    ],
    "audience": (
        "Engineering, CS, physics students; professionals in studio engineering, "
        "consumer electronics, multimedia. Assumes systems theory, DSP, multirate DSP."
    ),
    "parts": [
        {
            "id": "A",
            "title": "Hardware systems basis",
            "chapters": [1, 2, 3, 4],
            "summary": "Studio chain, quantization, converters, DSP platforms and interfaces",
        },
        {
            "id": "B",
            "title": "Algorithms for digital audio",
            "chapters": [5, 6, 7, 8, 9],
            "summary": "EQ, room simulation, dynamics, SRC, audio coding",
        },
    ],
    "preface_2e_notes": [
        "Revised/extended second edition (June 2008)",
        "Basis of lectures at TU Hamburg-Harburg and Helmut Schmidt University",
        "Interactive demos and Matlab examples online",
    ],
}

GLOSSARY = {
    "quantization": "Mapping continuous amplitude to discrete levels; introduces error e(n)",
    "dither": "Added noise before (re)quantization to linearize and decorrelate error",
    "noise shaping": "Feedback filter that spectrally shapes quantization error",
    "oversampling": "Sampling above Nyquist rate to ease filtering and noise distribution",
    "delta-sigma": "ΔΣ modulation: high-rate low-bit conversion with noise shaping",
    "AES/EBU": "Professional two-channel digital audio interface",
    "MADI": "Multichannel Audio Digital Interface",
    "parametric EQ": "Recursively realized boost/cut with Fc, gain, Q/bandwidth",
    "fast convolution": "FFT-based FIR filtering (overlap-add/save) for long IRs",
    "RIR": "Room impulse response",
    "Schroeder reverb": "Parallel comb + series allpass artificial reverb structure",
    "static curve": "Input–output level mapping of compressor/limiter/expander/gate",
    "SRC": "Sampling rate conversion",
    "psychoacoustics": "Hearing models (masking, critical bands) used in lossy coding",
    "SBR": "Spectral Band Replication (high-frequency reconstruction in coding)",
    "MPEG Audio": "ISO perceptual coding family (Layers, AAC, MPEG-4 audio tools)",
}

PEDAGOGY = {
    "order": [
        "Studio/digital audio landscape (Ch.1)",
        "Quantization physics & number formats (Ch.2)",
        "AD/DA methods (Ch.3)",
        "DSP systems & digital interfaces (Ch.4)",
        "Equalizers IIR/FIR (Ch.5)",
        "Room simulation (Ch.6)",
        "Dynamic range control (Ch.7)",
        "Sample-rate conversion (Ch.8)",
        "Audio coding & psychoacoustics (Ch.9)",
    ],
    "study_tips": [
        "Work chapter exercises; use course Java applets / Matlab demos where available",
        "Always state fs and word-length when discussing SNR and filters",
        "Separate perceptual (coding/dynamics) from objective (quantization formulas)",
        "Implement small prototypes: dither, biquad EQ, compressor, polyphase SRC",
    ],
}
