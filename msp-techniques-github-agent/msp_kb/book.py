BOOK = {
    "title": "The Theory and Technique of Electronic Music",
    "author": "Miller Puckette",
    "affiliation": "University of California, San Diego (UCSD)",
    "publisher": "World Scientific Publishing Co. Pte. Ltd.",
    "copyright_year": 2007,
    "draft_date": "December 30, 2006",
    "source_url": "https://msp.ucsd.edu/techniques/latest/book.pdf",
    "pdf_pages": 337,
    "foreword": "Max Mathews",
    "software": {
        "primary": "Pure Data (Pd) — open source, Puckette",
        "related": ["Max (1988)", "Max/MSP (with Zicarelli)", "Csound (techniques transfer)"],
        "examples": "Included in Pd distribution; figures also as Pd patches in electronic supplement",
    },
    "audience": (
        "Anyone who likes electronic music, is computer-fluent, and wants synthesis "
        "from oscillators through sampling, FM, filtering, waveshaping, delays, FFT, etc. "
        "No staff notation required; intermediate algebra/trig; complex numbers from Ch.7."
    ),
    "math_topics_encountered": [
        "Bessel functions (FM)",
        "Chebyshev polynomials (waveshaping)",
        "Central Limit Theorem (mentions)",
        "Fourier analysis",
    ],
    "structure": "Each chapter: theory (implementation-agnostic) then Pd examples + exercises",
}

GLOSSARY = {
    "sinusoid": "Pure tone x[n]=A cos(ωn+φ); building block of additive synthesis",
    "RMS": "Root-mean-square amplitude measure (vs peak)",
    "dB": "Logarithmic amplitude; book uses dbtorms-style conversion in Pd",
    "wavetable": "Stored period (or sample) looked up by phase index",
    "phasor": "Ramp phase generator 0…1 (or 0…N) driving table lookup",
    "control stream": "Sparse timed numeric events vs continuous audio rate",
    "foldover": "Aliasing when partials exceed Nyquist",
    "ring modulation": "Multiply two audio signals → sum/difference spectra",
    "waveshaping": "Instantaneous nonlinearity y=f(x) generating harmonics",
    "FM/PM": "Frequency/phase modulation for sideband spectra",
    "PAF": "Phase-aligned formant generator",
    "comb filter": "Delay + feedforward/feedback spectral peaks/notches",
    "allpass": "Flat magnitude, frequency-dependent phase (reverb density)",
    "phase vocoder": "STFT analysis/resynthesis with phase for time/pitch transforms",
    "timbre stamp": "Classical vocoder-style spectral envelope transfer",
    "switch-and-ramp": "Click-free discontinuous control change technique",
}

PEDAGOGY = {
    "order": [f"Chapter {i}" for i in range(1, 11)],
    "study_tips": [
        "Run Pd examples while reading theory sections",
        "Build each technique yourself in a general environment (not only presets)",
        "Always track sample rate R and Nyquist R/2 for spectral claims",
        "Separate control-rate zipper risks from audio-rate modulation",
        "Do chapter exercises",
    ],
}
