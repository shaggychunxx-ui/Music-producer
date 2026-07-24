"""Pipeline phases, gates, and meta info — song-agnostic."""

from __future__ import annotations

from typing import Any

META: dict[str, Any] = {
    "name": "song-creation-pipeline",
    "version": "1.0.0",
    "title": "Song Creation Pipeline",
    "summary": (
        "Gated original song process: reference-first MVP, one part at a time, "
        "signal-flow mix, optional late form on locked stems, final lock."
    ),
    "song_agnostic": True,
    "source": "Standing production workflow (studio process extract)",
    "hard_rules": [
        "Reference first (or explicit waive) before compose",
        "MVP drums+bass until pocket approved",
        "One part at a time; lock stems",
        "Parts hierarchy ≠ song form",
        "Stop on user lock / done language",
        "No audio in git",
    ],
}

PHASES: dict[str, dict[str, Any]] = {
    "brief": {
        "id": "A",
        "name": "Brief & reference",
        "temp": "2–4",
        "do": [
            "Name reference (title+artist) or get explicit waive",
            "Capture + fingerprint (peak/RMS/crest/bands/tempo)",
            "Mood lock (dark/bright, lead limits)",
            "Fill VOICE_BRIEF for kick+bass before patches",
            "Complexity budget S default; note target length if known",
        ],
        "stop": "User confirms brief or says proceed",
    },
    "sketch": {
        "id": "B",
        "name": "Arrangement sketch",
        "temp": "3–5",
        "do": [
            "Light form + mute map (STRUCTURE lightweight)",
            "Frequency owners (PARTS_STRUCTURE)",
            "Contrast plan — what drops out where",
        ],
        "stop": "Sketch is enough for MVP; no heavy poly maps yet",
    },
    "mvp": {
        "id": "C",
        "name": "MVP drums + bass",
        "temp": "compose 6–7; mix 2–3",
        "do": [
            "MIDI drums+bass only",
            "Dry peak-safe stems; mono low",
            "Solo A/B bass and kick vs ref family",
            "Simple mix → Desktop *_MVP_Master",
        ],
        "stop": "USER APPROVES pocket (drums? bass? groove?) — do not add lead yet",
        "forbidden": ["lead", "pad", "poly", "stabs", "FX", "heavy automation"],
    },
    "lead": {
        "id": "D1",
        "name": "Lead only",
        "temp": "compose ~6–7; mix 2–3",
        "do": [
            "Lock drums/bass dry stems",
            "Timbre brief + source; own 1–5 kHz; HPF mud",
            "One master; wait for approval",
        ],
        "stop": "USER OK on lead before bed",
    },
    "bed": {
        "id": "D2",
        "name": "One bed",
        "temp": "5–6 compose; 2–3 mix",
        "do": [
            "Pad OR pluck only",
            "HPF; low level; duck under kick/bass if competing",
            "Wide/hard-pan only if asked",
        ],
        "stop": "USER OK on bed before color/full polish",
    },
    "color": {
        "id": "D3",
        "name": "Color (optional)",
        "temp": "4–6",
        "do": ["Sparse stabs/FX", "Not continuous mid wash"],
        "stop": "USER OK if used",
    },
    "full_mix": {
        "id": "F",
        "name": "Full mix signal flow 1–8",
        "temp": "2–3",
        "do": [
            "1 dry locked → 2 faders → 3 EQ → 4 dyn → 5 sends → 6 groups → 7 bus → 8 master",
            "Kick cut-through: mild duck + kick presence",
            "Lead air on sends; mono check low end",
        ],
        "stop": "User feedback; one-focus fixes only",
    },
    "automation": {
        "id": "G",
        "name": "Automation",
        "temp": "3–5",
        "do": ["Only after static mix works", "Mutes, filter opens, send throws"],
        "stop": "Do not use automation to fix bad faders",
    },
    "qc": {
        "id": "H",
        "name": "QC / A-B",
        "temp": "1–2",
        "do": [
            "Level-matched A/B vs ref",
            "Mono fold",
            "Crest not crushed vs ref",
            "Tick GATES + NOTES",
        ],
        "stop": "Ready for optional late form or FINAL",
    },
    "late_form": {
        "id": "I",
        "name": "Late form on locked stems",
        "temp": "2–4",
        "do": [
            "Only if user asks length/start/tempo/section map",
            "Freeze stems; loop/reorder; no new melodies",
            "Re-apply duck/pad/presence/sends",
            "Write STRUCTURE + arrange stems",
        ],
        "stop": "User approves form; do not recompose",
    },
    "final": {
        "id": "K",
        "name": "Final lock",
        "temp": "1",
        "do": [
            "Log FINAL in NOTES + GATES",
            "Desktop master path recorded",
            "Stop rework unless user reopens",
        ],
        "stop": "Done",
    },
}

# aliases for lookup
_PHASE_ALIASES = {
    "a": "brief",
    "b": "sketch",
    "c": "mvp",
    "d": "lead",
    "d1": "lead",
    "d2": "bed",
    "d3": "color",
    "e": "lead",
    "f": "full_mix",
    "mix": "full_mix",
    "g": "automation",
    "h": "qc",
    "i": "late_form",
    "arrange": "late_form",
    "form": "late_form",
    "j": "final",
    "k": "final",
    "done": "final",
    "pocket": "mvp",
    "drums": "mvp",
    "bass": "mvp",
}

GATES: list[dict[str, str]] = [
    {"id": "A1", "text": "Reference captured + fingerprint logged"},
    {"id": "A2", "text": "Mood lock + VOICE_BRIEF kick/bass filled"},
    {"id": "B1", "text": "Light STRUCTURE + PARTS owners noted"},
    {"id": "C1", "text": "MVP drums+bass rendered"},
    {"id": "C2", "text": "USER APPROVED pocket — STOP"},
    {"id": "D1", "text": "Lead approved — STOP"},
    {"id": "D2", "text": "Bed approved — STOP"},
    {"id": "D3", "text": "Color approved if used"},
    {"id": "F1", "text": "Signal flow 1–8 full mix"},
    {"id": "H1", "text": "QC A/B + mono"},
    {"id": "I1", "text": "Late form only if asked (locked stems)"},
    {"id": "K1", "text": "FINAL LOCK language logged — stop rework"},
]

TEMP_TABLE: dict[str, str] = {
    "mvp_compose": "6–7",
    "mix_qc": "2–3",
    "voice_focus": "3–5",
    "humanize_after_lock": "8–10 only if asked",
    "shelf_rebrief": "1–2",
}

SCAFFOLD: dict[str, Any] = {
    "files": [
        "VOICE_BRIEF.txt",
        "GATES.txt",
        "NOTES.txt",
        "PARTS_STRUCTURE.txt",
        "STRUCTURE.txt",
        "README.txt",
    ],
    "dirs": [
        "_reference_captures",
        "MIDI",
        "MIDI_Parts",
        "Stems_Dry",
        "Stems_MVP",
        "Stems_Parts",
        "Stems_Arrange",
        "Audio",
        "Voice_AB",
        "DRAG_THESE_INTO_STUDIO_ONE",
    ],
    "notes": [
        "PARTS_STRUCTURE = roles/stems only",
        "STRUCTURE = form/tempo/length only",
        "Tick GATES + one NOTES line on every user lock",
        "Status values: ACTIVE | SHELVED | FINAL LOCK | ARCHIVED",
    ],
    "cli_hint": "Local studio: python new_song_scaffold.py --name Song_Name (under songs/_studio_lib when present)",
}


def list_phases() -> list[str]:
    return list(PHASES.keys())


def get_phase(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    key = _PHASE_ALIASES.get(key, key)
    if key not in PHASES:
        return {"error": f"unknown phase: {name}", "available": list_phases()}
    out = dict(PHASES[key])
    out["key"] = key
    return out
