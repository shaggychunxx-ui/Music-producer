from __future__ import annotations

RECIPES: dict[str, dict] = {
    "four_bar_loop": {
        "title": "Study drill — write a 4-bar major loop",
        "watch": "https://www.youtube.com/watch?v=M8eItITv8QA",
        "steps": [
            "Pick a key (not C if you already live there).",
            "Write the six beginner triads: I ii iii IV V vi.",
            "Bar 1 = I. Bar 4 = IV or V. Bars 2–3 = anything from the six.",
            "Loop it 8 times. Hum only parent-scale notes on top.",
            "Rewrite once ending IV, once ending V. Name plagal vs authentic.",
            "Optional upgrade: same numerals as 7ths, then as C–G/B–Am–F-style inversions.",
        ],
    },
    "minor_then_v": {
        "title": "Study drill — minor palette, then add V",
        "watch": "https://www.youtube.com/watch?v=j-j4g0ktPGw",
        "steps": [
            "Write i – bVII – bVI – iv (all natural minor).",
            "Replace the last chord with V. Hear the leading-tone snap.",
            "Over V only, raise 7 (harmonic minor). Over the rest, stay Aeolian.",
            "Restyle the same numerals as Andalusian metal (power chords) and as a pedal-tone pad version.",
        ],
    },
    "dorian_vamp": {
        "title": "Study drill — prove Dorian",
        "watch": "https://www.youtube.com/watch?v=hyZPcYf1Pe4",
        "steps": [
            "Two bars of i, one bar IV, one bar bIII.",
            "Melody must hit the natural 6 on purpose.",
            "Take 2: break it — last bar becomes V, melody uses the leading tone.",
            "Jam: funk track in A Dorian (jam-track-funk-dorian).",
        ],
    },
    "lydian_fragile": {
        "title": "Study drill — keep Lydian alive",
        "watch": "https://www.youtube.com/watch?v=Ou_Z9ol8r0I",
        "steps": [
            "Pedal I for 8 bars. Lead uses 1 3 #4 5 only for 4 bars, then full Lydian.",
            "Add II for one bar. Do not add V.",
            "If it suddenly feels like a normal major key, you overplayed 4 or V — reset to I + #4.",
        ],
    },
    "mixo_rock": {
        "title": "Study drill — Mixolydian rock loop",
        "watch": "https://www.youtube.com/watch?v=vPIebPDBizs",
        "steps": [
            "I – bVII – IV – I.",
            "Treat I7 as home.",
            "Solo with Mixolydian, then Mixolydian pentatonic, landing on 1, 3, and b7.",
        ],
    },
    "phrygian_dip": {
        "title": "Study drill — Phrygian riff, then leave",
        "watch": "https://www.youtube.com/watch?v=ZnoKgWnMEq8",
        "steps": [
            "Pedal i. Riff uses 1–b2–1 and 1–b7–1.",
            "Optional bII back to i.",
            "After 8 bars, modulate relatively to Aeolian (same notes, new home) for relief.",
        ],
    },
    "relative_flip": {
        "title": "Study drill — Comfortably Numb move",
        "watch": "https://www.youtube.com/watch?v=sC2qXLnVU3A",
        "steps": [
            "Write a verse that hammers vi (or i of the relative minor).",
            "Chorus uses the same seven notes but lands on I.",
            "Do not add accidentals. The flip is the arrangement.",
        ],
    },
    "mixture_poke": {
        "title": "Study drill — one poked degree",
        "watch": "https://www.youtube.com/watch?v=TZtc_gWnMa0",
        "steps": [
            "Major I–IV–V loop.",
            "Add bVII. Over I–IV–V play major; over bVII play Mixolydian (flat the 7).",
            "Rewrite as Imaj7–bVIImaj7. Confirm you are not playing the wrong 7th.",
            "Separate take: I–vi–I–iv. Try harmonic major (only 6 lowered) over iv, not full minor.",
        ],
    },
    "secondary_to_vi": {
        "title": "Study drill — V7/vi",
        "watch": "https://www.youtube.com/watch?v=py4HaueW50Q",
        "steps": [
            "I – V7/vi – vi – V.",
            "Circle the foreign note (G# in C when E7 appears).",
            "Melody uses that foreign note only on the E7 bar.",
        ],
    },
    "voice_lead_three": {
        "title": "Study drill — 3-voice IV–V–I",
        "watch": "https://www.youtube.com/watch?v=UkatcvIuF4U",
        "steps": [
            "Bass: roots F G C.",
            "Inner: A B C.",
            "Top: C D E.",
            "Label motions (parallel / contrary / oblique).",
            "Repeat dropping the 5ths — ask if color changed.",
        ],
    },
    "tresillo_steal": {
        "title": "Study drill — new song, stolen rhythm",
        "watch": "https://www.youtube.com/watch?v=na-W43-6JUc",
        "steps": [
            "Grid: 3+3+3+3+4 in one bar of 16ths (or two bars of 8ths).",
            "Write a riff that hits only those attacks.",
            "Harmonize with a 4-bar Signals loop (major or Andalusian).",
            "Do not copy anyone's pitches.",
        ],
    },
    "pulse_gym": {
        "title": "Study drill — body first, metronome later",
        "watch": "https://www.youtube.com/watch?v=CoBTWll93yE",
        "steps": [
            "Six even notes: foot 3s then 2s. Count out loud.",
            "Twelve even notes: foot 3s then 4s.",
            "Same grouping with one rest (Dream Theater 'Mirror' idea).",
            "Only then put a click on the foot pulse.",
        ],
    },
    "motif_reharm": {
        "title": "Study drill — motif + reharmonize",
        "watch": "https://www.youtube.com/watch?v=z3Dy6Mnp5Og",
        "steps": [
            "Write a 3-note motif.",
            "Harmonize statement A with a diatonic loop.",
            "Statement B: same motif, one borrowed or secondary-dominant chord.",
            "Statement C: invert the bass under the same motif.",
        ],
    },
    "daily_key": {
        "title": "Daily producer habit",
        "steps": [
            "Watch one Signals lesson from the active study path.",
            "Write 8 bars using only that technique (Studio One or paper).",
            "Label numerals + characteristic notes in the song notes.",
            "Do not start a new original song from this KB — pull the GitStatus Spotify ref first (taste pick / apply-brief).",
        ],
    },
}


def get_recipe(name: str) -> dict:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    if key in RECIPES:
        return {"id": key, **RECIPES[key]}
    hits = [k for k, v in RECIPES.items() if key in k or key in v["title"].lower().replace(" ", "_")]
    if len(hits) == 1:
        return get_recipe(hits[0])
    if hits:
        return {"matches": hits}
    return {"error": f"unknown recipe {name!r}", "available": list(RECIPES)}
