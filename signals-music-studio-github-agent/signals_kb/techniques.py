from __future__ import annotations

TECHNIQUES: dict[str, dict] = {
    "four_bar_diatonic_loop": {
        "title": "Four-bar diatonic loop (3 rules)",
        "source": "writing-chord-progressions",
        "youtube": "https://www.youtube.com/watch?v=M8eItITv8QA",
        "do": [
            "Four measures.",
            "Start on I (or i in minor).",
            "End the loop on IV or V (major) so it wants to repeat.",
            "Fill the middle from the remaining diatonic triads (skip vii° at first).",
        ],
        "why": "Removes mystery. Guessing in the middle still sounds like a song.",
    },
    "plagal_vs_authentic": {
        "title": "Close the loop: IV vs V",
        "source": "writing-chord-progressions",
        "do": [
            "IV→I = plagal, soft landing (amen).",
            "V→I = authentic, decisive arrival.",
            "Write the same middle twice; swap only the last chord and hear the cadence.",
        ],
    },
    "pop_axis": {
        "title": "I–V–vi–IV (axis / 'four chords')",
        "source": "writing-chord-progressions",
        "example": "G D Em C  /  C G Am F",
        "do": ["Learn it in every key.", "Then invert the bass, add 7ths, or borrow one chord so it is yours."],
    },
    "minor_starter": {
        "title": "Minor starter palette",
        "source": "writing-in-minor",
        "chords": "i, iv, bVI, bVII",
        "do": [
            "Any combination works as a first minor loop.",
            "Then add V (major) via raised 7 / harmonic minor over that chord only.",
        ],
    },
    "andalusian": {
        "title": "Andalusian cadence i–bVII–bVI–V",
        "source": "andalusian-cadence",
        "youtube": "https://www.youtube.com/watch?v=qbeRVJMT5CY",
        "do": [
            "Write the numerals once.",
            "Restyle without changing numerals: flamenco ornaments, metal power chords, or tonic pedal + pads.",
            "Minor/Aeolian over first three; harmonic minor over V.",
        ],
        "lesson": "Originality is arrangement, not a secret new progression.",
    },
    "mario_cadence": {
        "title": "Mario cadence I–bVI–bVII–I",
        "source": "mario-cadence",
        "do": ["Borrow bVI and bVII in a major key for a majestic lift.", "Keep I as home so it stays a cadence, not a new key."],
    },
    "inversions_for_bass": {
        "title": "Inversions / slash chords free the bass",
        "source": "inversions-slash-chords",
        "youtube": "https://www.youtube.com/watch?v=LFN-eKved_8",
        "do": [
            "Stop letting bass jump with every root.",
            "First inversion = 6/3 = C/E; second = 6/4 = C/G.",
            "Classic smoother pop: C – G/B – Am – F (bass C–B–A–F).",
        ],
    },
    "diatonic_sevenths": {
        "title": "Upgrade triads to diatonic 7ths",
        "source": "seventh-chord-progressions",
        "map": "I/IV=maj7  V=7  ii/iii/vi=m7",
        "example": "Cmaj7 G7 Am7 Fmaj7",
    },
    "sus_stretch": {
        "title": "Sus2 / sus4 to delay or neutralize",
        "source": "writing-chord-progressions series (sus section)",
        "do": [
            "No third → not major or minor.",
            "Isus / Vsus delays resolution.",
            "Use beside the unsuspended chord to get more mileage from one harmony.",
            "iii usually sus2 only; IV usually sus4 not sus2 (diatonic).",
        ],
    },
    "secondary_dominant": {
        "title": "Secondary dominant (V/x)",
        "source": "secondary-dominants",
        "youtube": "https://www.youtube.com/watch?v=py4HaueW50Q",
        "do": [
            "Pick a diatonic target (vi, ii, V, IV…).",
            "Play that target's V or V7 just before it.",
            "C example: C – E7 – Am – G  (E7 = V7/vi).",
            "Treat it as a mini-modulation that snaps back.",
        ],
        "note": "V7/vi is the modern-pop workhorse.",
    },
    "passing_dim7": {
        "title": "Passing dim7 between a whole step",
        "source": "diminished-chords-five-ways",
        "example": "C – F – F#dim7 – G",
        "do": ["Find two diatonic chords a whole step apart.", "Plug the chromatic gap with dim7.", "This is a secondary leading-tone chord."],
    },
    "borrowed_from_minor": {
        "title": "Borrow from parallel minor",
        "source": "borrowed-chords",
        "youtube": "https://www.youtube.com/watch?v=7IdttvJSedg",
        "starters": ["iv (Fm in C)", "bVI (Ab in C)", "bVII (Bb in C)"],
        "do": ["Write a major loop.", "Swap one chord for its parallel-minor cousin.", "Melody can stay mostly major except over the borrowed chord."],
    },
    "flexible_degree": {
        "title": "Poke one scale degree (modal mixture)",
        "source": "modal-mixture-major-keys",
        "youtube": "https://www.youtube.com/watch?v=TZtc_gWnMa0",
        "do": [
            "Key of A major = A major triad is home, not 'only A major notes'.",
            "Lower 7 → Mixolydian color / bVII.",
            "Raise 4 → Lydian color / II7.",
            "Lower 6 only for iv → harmonic major (do not auto-jump to full minor).",
            "Prove a chord's 'origin' by the scale you play on top.",
            "Avoid sounding both 3rds of a chord unless you want blues clash.",
        ],
    },
    "stay_in_mode": {
        "title": "Stay inside one mode",
        "source": "seven-ways-to-use-modes",
        "youtube": "https://www.youtube.com/watch?v=sC2qXLnVU3A",
        "do": [
            "Use only that mode's notes and its diatonic triads.",
            "Promote tonic pitch + tonic triad (two bars of i is an easy cheat).",
            "A Dorian demo: Am Am D Cmaj7.",
        ],
    },
    "break_the_mode": {
        "title": "Write in a mode, then break it",
        "source": "seven-ways-to-use-modes",
        "do": [
            "Establish Dorian (or any mode) first.",
            "Then allow one desirable outsider (Dorian + V with leading tone).",
            "Match the melody to the break (G# over E, not G).",
        ],
    },
    "relative_modulation": {
        "title": "Relative modulation (same notes, new home)",
        "source": "seven-ways-to-use-modes",
        "example": "Comfortably Numb: verse B minor, chorus D major",
        "do": [
            "Keep the pitch set.",
            "Change which triad is home between sections.",
            "Unstable mode (Phrygian) resolving to Aeolian is a relief move.",
        ],
    },
    "voice_leading": {
        "title": "Voice-lead the insides",
        "source": "voice-leading",
        "youtube": "https://www.youtube.com/watch?v=UkatcvIuF4U",
        "do": [
            "Track each voice: parallel / similar / contrary / oblique.",
            "Approach arrivals with neighbor tones.",
            "Drop the 5th if you need a free voice.",
            "Arrange IV–V–I as three smooth lines, not three block shapes.",
        ],
    },
    "double_tresillo": {
        "title": "Steal double tresillo (3+3+3+3+4)",
        "source": "stealing-musical-ideas",
        "youtube": "https://www.youtube.com/watch?v=na-W43-6JUc",
        "do": ["Keep the rhythm grid.", "Write new pitches, harmony, and arrangement.", "Do not copy the source melody."],
    },
    "pulse_switch": {
        "title": "6/8 vs 3/4 and 12/8 dual pulse",
        "source": "7-simple-rhythm-exercises",
        "youtube": "https://www.youtube.com/watch?v=CoBTWll93yE",
        "do": [
            "Same even notes; change foot grouping (2 vs 3, then 3 vs 4).",
            "Count and clap against the foot.",
            "Then add a rest so the grouping is musical, not a click.",
            "Gateway to polymeter and metric modulation.",
        ],
    },
    "motif_then_chords": {
        "title": "Motif first, then chords, then reharmonize",
        "source": "motifs-and-chords",
        "youtube": "https://www.youtube.com/watch?v=z3Dy6Mnp5Og",
        "do": ["Write a 2–4 note motif.", "Harmonize it.", "Keep the motif, change the chords under later statements."],
    },
    "one_shape_all_modes": {
        "title": "One shape, change the home note",
        "source": "one-scale-shape-all-modes",
        "youtube": "https://www.youtube.com/watch?v=96cydVB4w-A",
        "do": [
            "Stop hoarding boxes.",
            "Reuse one major or minor-pentatonic shape.",
            "Change which pitch is treated as 1 / tonic.",
        ],
    },
    "power_chord_ambiguity": {
        "title": "Power chords (no 3rd)",
        "source": "power-chords",
        "do": ["Root+5 sits under major or minor.", "Useful when the riff must not lock a 3rd before the vocal/lead does."],
    },
    "named_color_chords": {
        "title": "Named color chords",
        "source": "famous-chords-nicknames",
        "youtube": "https://www.youtube.com/watch?v=BHwYlzpdsRI",
        "chords": ["Neapolitan bII", "augmented sixth", "backdoor bVII7→I", "cadential 6/4"],
        "do": ["Write an 8-bar phrase that uses one named chord as the event."],
    },
    "methodical_writing": {
        "title": "95% methodical writing",
        "source": "writing-chord-progressions + songwriting-concepts",
        "do": [
            "Do not wait for inspiration.",
            "Run a technique (loop rules, stolen rhythm, motif+reharm) until something clicks.",
            "Then arrange: inversions, rhythm, orchestration — that is where it stops sounding generic.",
        ],
    },
}


def list_techniques() -> list[str]:
    return [f"{k}: {v['title']}" for k, v in TECHNIQUES.items()]


def get_technique(name: str) -> dict:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    if key in TECHNIQUES:
        return {"id": key, **TECHNIQUES[key]}
    hits = [
        k
        for k, v in TECHNIQUES.items()
        if key in k or key in v["title"].lower().replace(" ", "_").replace("-", "_")
    ]
    if len(hits) == 1:
        return get_technique(hits[0])
    if hits:
        return {"matches": hits}
    return {"error": f"unknown technique {name!r}", "available": list(TECHNIQUES)}
