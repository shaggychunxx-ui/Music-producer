from __future__ import annotations
from typing import Any

RECIPES = {
    "first_boot": {"title": "Power on & firmware check", "steps": [
        "Power on; insert SD if needed.",
        "UTILITY → INFORMATION:Version (manual is for v1.02+).",
        "Update from roland.com/support only if not current.",
    ]},
    "step_record": {"title": "TR-REC a beat", "steps": [
        "Select pattern + kit; set tempo.",
        "TR-REC; choose instrument; enter steps; optional flam/weak/ALT/accent.",
        "WRITE pattern.",
    ]},
    "motion": {"title": "Record motion", "steps": [
        "Play pattern; enable motion record.",
        "Move knobs; verify playback; WRITE pattern.",
    ]},
    "sample_inst": {"title": "Import sample to instrument", "steps": [
        "SAMPLE Import from SD; edit; assign to INST; OPTIMIZE if needed; WRITE kit.",
    ]},
    "daw_sync": {"title": "USB slave to DAW", "steps": [
        "USB connect; set sync/MIDI to follow USB clock; start DAW transport.",
    ]},
    "backup": {"title": "Backup to SD", "steps": [
        "UTILITY BACKUP; restore via RESTORE; factory reset only after backup.",
    ]},
}

def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {"tr_rec": "step_record", "record": "step_record", "sync": "daw_sync"}
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe {name}. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
