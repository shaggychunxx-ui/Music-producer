"""Chapter map from book Contents."""

from __future__ import annotations

from typing import Any

CHAPTERS: dict[int, dict[str, Any]] = {
    1: {
        "number": 1,
        "title": "Sinusoids, amplitude and frequency",
        "book_pages": "1–25",
        "pdf_start_approx": 13,
        "sections": [
            "Measures of amplitude (peak, RMS)",
            "Units of amplitude (decibels)",
            "Controlling amplitude",
            "Frequency (angular ω, Hz, pitch)",
            "Synthesizing a sinusoid",
            "Superposing signals",
            "Periodic signals / Fourier series intro",
            "About software examples / quick Pd intro",
            "Examples: dB amp, envelopes, triad, mtof, additive",
        ],
        "key_points": [
            "Digital audio = sequences x[n] at sample rate R",
            "Additive synthesis stacks sinusoids",
            "Envelope generators smooth amplitude without clicks",
            "Pd audio on/off; osc~, *~, dac~, message vs signal cords",
        ],
    },
    2: {
        "number": 2,
        "title": "Wavetables and samplers",
        "book_pages": "27–57",
        "pdf_start_approx": 39,
        "sections": [
            "Wavetable oscillator",
            "Sampling",
            "Enveloping samplers",
            "Timbre stretching",
            "Interpolation",
            "Examples: tabosc, looping/overlapping loopers, precession",
        ],
        "key_points": [
            "Lookup table driven by phase/phasor",
            "Transposition stretches spectrum (timbre change)",
            "Interpolation quality affects fidelity (e.g. tabread4~)",
            "Looping and cross-fades for sustained samples",
        ],
    },
    3: {
        "number": 3,
        "title": "Audio and control computations",
        "book_pages": "59–87",
        "pdf_start_approx": 71,
        "sections": [
            "Sampling theorem",
            "Control / control streams",
            "Audio↔control conversion",
            "Event detection",
            "Audio as control",
            "Control operations in Pd",
            "Examples: foldover, line~ players, sequencer, MIDI-style synth",
        ],
        "key_points": [
            "Nyquist limit and foldover demos",
            "Control streams are sparse timed numbers",
            "Event detection turns audio into triggers",
            "MIDI-style note handling is a control architecture problem",
        ],
    },
    4: {
        "number": 4,
        "title": "Automation and voice management",
        "book_pages": "89–117",
        "pdf_start_approx": 101,
        "sections": [
            "Envelope generators",
            "Linear and curved amplitude shapes",
            "Continuous vs discontinuous control (muting, switch-and-ramp)",
            "Polyphony, voice allocation, voice tags",
            "Encapsulation in Pd",
            "Examples: ADSR, transfer functions, Risset bell, spectral envelopes, poly sampler",
        ],
        "key_points": [
            "Polyphony needs voice allocation policies",
            "Clicks from discontinuous gain/phase must be managed",
            "Classic additive instruments (Risset bell) as case studies",
        ],
    },
    5: {
        "number": 5,
        "title": "Modulation",
        "book_pages": "119–146",
        "pdf_start_approx": 131,
        "sections": [
            "Taxonomy of spectra",
            "Multiplying audio signals (ring mod)",
            "Waveshaping",
            "Frequency and phase modulation",
            "Examples: RM, formant adder, Chebyshev, exp waveshaping, FM/PM",
        ],
        "key_points": [
            "Multiplication creates sum/difference frequencies",
            "Waveshaping maps instantaneous amplitude → harmonics (Chebyshev basis)",
            "FM/PM generate Bessel-related sideband families",
        ],
    },
    6: {
        "number": 6,
        "title": "Designer spectra",
        "book_pages": "147–173",
        "pdf_start_approx": 159,
        "sections": [
            "Carrier/modulator model",
            "Pulse trains (waveshaping / wavetable stretch)",
            "Movable ring modulation",
            "Phase-aligned formant (PAF) generator",
            "Examples: pulse train, formants, two-cosine carrier, PAF, stretched tables",
        ],
        "key_points": [
            "Intentional spectral design beyond raw FM",
            "PAF: controlled formant peaks with phase alignment",
            "Pulse trains as harmonic-rich sources",
        ],
    },
    7: {
        "number": 7,
        "title": "Time shifts and delays",
        "book_pages": "175–221",
        "pdf_start_approx": 187,
        "sections": [
            "Complex numbers & complex sinusoids",
            "Time shifts and phase",
            "Delay networks / recirculating networks",
            "Power conservation; artificial reverberation",
            "Variable/fractional delays; interpolation fidelity",
            "Pitch shifting",
            "Examples: comb, variable delay, execution order, reverb, pitch shifter",
        ],
        "key_points": [
            "Complex representation unifies delay phase analysis",
            "Recirculating combs/allpasses → reverb building blocks",
            "Variable delay enables Doppler/pitch effects",
            "Pd delay writer/reader order imposes minimum delay constraints",
        ],
    },
    8: {
        "number": 8,
        "title": "Filters",
        "book_pages": "223–262",
        "pdf_start_approx": 235,
        "sections": [
            "Taxonomy: LP/HP/BP/stop, equalizing",
            "Elementary non-recirculating and recirculating filters",
            "Compound filters; complex→real",
            "One-pole/one-zero, peaking/shelving, allpass",
            "Examples in Pd (bp~, etc.)",
        ],
        "key_points": [
            "Filters as delay networks with gains",
            "Poles (recirculating) vs zeros (non-recirculating)",
            "Allpass for phase/reverb density without magnitude EQ",
        ],
    },
    9: {
        "number": 9,
        "title": "Fourier analysis and resynthesis",
        "book_pages": "263–294",
        "pdf_start_approx": 275,
        "sections": [
            "Fourier of periodic signals; properties",
            "Non-periodic signals / STFT-style analysis",
            "Reconstruction; narrow-band companding; timbre stamp vocoder",
            "Phase; phase bashing",
            "Examples: rfft~/rifft~, noise suppression, vocoder, phase-vocoder time bender",
        ],
        "key_points": [
            "FFT frames enable spectral FX",
            "Vocoder = envelope transfer between spectra",
            "Phase vocoder for time stretch / pitch-ish transforms",
            "Phase handling is as important as magnitude",
        ],
    },
    10: {
        "number": 10,
        "title": "Classical waveforms",
        "book_pages": "295–317",
        "pdf_start_approx": 307,
        "sections": [
            "Symmetries and Fourier series",
            "Saw, parabolic, square, triangle series",
            "Predicting/controlling foldover (oversampling, sneaky triangles, transition splicing)",
            "Examples: combining saws, band-limiting strategies",
        ],
        "key_points": [
            "Analytic spectra of classic synth waveforms",
            "Naive digital saws alias; need band-limited techniques",
            "Oversampling and splicing as practical remedies",
        ],
    },
}


def list_chapters() -> list[str]:
    return [f"{c['number']}. {c['title']}" for c in CHAPTERS.values()]


def get_chapter(ref: str | int) -> dict[str, Any]:
    if isinstance(ref, int) or (isinstance(ref, str) and str(ref).isdigit()):
        n = int(ref)
        if n not in CHAPTERS:
            raise KeyError("Chapters are 1–10")
        return CHAPTERS[n]
    q = str(ref).strip().lower()
    for c in CHAPTERS.values():
        if q in c["title"].lower():
            return c
    for c in CHAPTERS.values():
        if any(q in s.lower() for s in c["sections"]):
            return c
    raise KeyError(f"No chapter match for '{ref}'")
