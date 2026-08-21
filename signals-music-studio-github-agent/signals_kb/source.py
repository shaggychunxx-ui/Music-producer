from __future__ import annotations

from pathlib import Path
import json

_KNOWLEDGE = Path(__file__).resolve().parent.parent / "knowledge"
_CATALOG_PATH = _KNOWLEDGE / "catalog.json"


def _load_catalog() -> dict:
    return json.loads(_CATALOG_PATH.read_text(encoding="utf-8"))


CATALOG = _load_catalog()

SOURCE = {
    "title": "Signals Music Studio",
    "teacher": "Jake Lizzio",
    "youtube": "https://www.youtube.com/@SignalsMusicStudio/videos",
    "lessons": "https://signalsmusic.studio/lessons",
    "about": CATALOG["channel"]["about"],
    "lesson_count": len(CATALOG["lessons"]),
    "series_count": len(CATALOG["series"]),
    "role": (
        "Practical songwriting/harmony/mode/rhythm techniques for a modern producer. "
        "Use this KB to study and apply Jake's methods — not as a DAW or mix agent."
    ),
    "copyright": (
        "Videos and lesson text © Jake Lizzio / Signals Music Studio. "
        "This package restates operational techniques for local study only."
    ),
    "do_not": [
        "Copy transcripts, PDFs, or paid Codex/course material into git",
        "Treat modes as 'start on a different degree' without a tonal center",
        "Switch parent scales on every chord of a diatonic loop",
        "Confuse THE dominant (V) with A dominant (dom7 quality)",
        "Camp on V while trying to stay Lydian",
    ],
    "study_paths": list(CATALOG["study_paths"].keys()),
    "cli": [
        "python -m signals_kb info",
        "python -m signals_kb series",
        "python -m signals_kb study harmony_writer",
        "python -m signals_kb mode dorian",
        "python -m signals_kb recipe four_bar_loop",
        "python -m signals_kb search tresillo",
        "python -m signals_kb watch writing-chord-progressions",
    ],
}
