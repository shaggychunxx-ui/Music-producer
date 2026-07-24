"""Action recipes for the song creation pipeline."""

from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "start_song": {
        "title": "Start a new original song",
        "steps": [
            "Scaffold song folder (VOICE_BRIEF, GATES, NOTES, PARTS, STRUCTURE).",
            "Ask for reference track (or explicit waive).",
            "Capture + fingerprint; fill mood lock + kick/bass voice brief.",
            "Light form sketch only.",
            "Build MVP drums+bass; STOP for pocket approval.",
        ],
    },
    "mvp_pocket": {
        "title": "MVP drums + bass pocket",
        "steps": [
            "Compose only kit + bass (temp 6–7).",
            "Dry peak-safe; mono below ~80–100 Hz.",
            "Carve kick vs bass ownership (50–80 Hz).",
            "Simple faders/EQ/dyn; light master.",
            "Desktop MVP master → ask: drums? bass? pocket? WAIT.",
        ],
    },
    "add_lead": {
        "title": "Add lead only",
        "steps": [
            "Lock approved drums/bass stems.",
            "Timbre brief; pick sample/synth family; solo A/B.",
            "HPF mud; own presence 1–5 kHz.",
            "One master; STOP for user OK before bed.",
        ],
    },
    "add_bed": {
        "title": "Add one bed (pad or pluck)",
        "steps": [
            "Lock prior stems.",
            "HPF; sit under lead/bass; optional light duck under kick.",
            "Do not hard-pan/widen unless asked.",
            "One master; STOP.",
        ],
    },
    "duck_mild_short": {
        "title": "Mild short-release kick→bass duck",
        "params": {
            "amount": 0.30,
            "floor": 0.74,
            "attack_ms": 3,
            "release_ms": 40,
            "key_lp_hz": 120,
        },
        "steps": [
            "Key = low-passed kick/drum energy.",
            "Duck bass with mild amount + high floor.",
            "Keep release short (40–60 ms) to avoid pump tail.",
            "Add light kick presence EQ (body + click) rather than max duck.",
            "If still pumps → shorten release; if hollow → lower amount/raise floor.",
        ],
    },
    "duck_dial": {
        "title": "Dial sidechain from user feedback",
        "steps": [
            "Too aggressive → lower amount, raise floor.",
            "Still pumps → shorten release (primary).",
            "Clicks → slightly longer release or softer amount.",
            "Beds fighting kick → duck pads harder than bass.",
            "One bounce per change; keep last good master.",
        ],
    },
    "lead_send_dial": {
        "title": "Lead dry vs aux (air)",
        "steps": [
            "Keep dry lead; put plate/delay on shared sends.",
            "Less airy → cut send first, then dry level.",
            "dry −3 dB / aux +3 dB is a valid single move; repeat only if asked.",
            "Pre-HPF wet returns so mud doesn't fill verb.",
        ],
    },
    "pad_hardpan_wide": {
        "title": "Hard-pan wide pad with presence",
        "steps": [
            "HPF ≥150–200 Hz (no sub on sides).",
            "Hard L + Haas R (~10–18 ms); slight HF tilt on one side.",
            "Presence peaks ~2.5–4.5 kHz + mild air.",
            "Optional M/S side boost; check mono fold.",
            "Light-duck pad under kick so width doesn't mask punch.",
        ],
    },
    "late_arrange": {
        "title": "Late form on locked stems",
        "steps": [
            "Confirm user wants form/length/start/tempo — not part rename.",
            "Freeze approved stems; do not re-voice.",
            "Detect lead/hook bar; cut pre-hook if start-on-lead.",
            "± few BPM if asked; section map from existing blocks only.",
            "Loop/reorder with contrast (breaks, pull-downs).",
            "Re-apply duck/pad/sends; write STRUCTURE + arrange stems.",
            "One master; STOP.",
        ],
    },
    "parts_not_form": {
        "title": "Organize parts without rewriting the song",
        "steps": [
            "Update PARTS_STRUCTURE role hierarchy.",
            "Export/rename Stems_Parts role stems.",
            "Do NOT change bar order, MIDI form, or section map.",
            "If form was already rewritten by mistake: restore last full mix master.",
        ],
    },
    "focus_one_part": {
        "title": "One-focus re-voice",
        "steps": [
            "User names one problem part.",
            "Lock all other dry stems.",
            "Fix source (patch/sample/envelope) before heavy FX.",
            "Re-run mix stages 2–8; one Desktop master.",
            "Ask better / worse / next?",
        ],
    },
    "final_lock": {
        "title": "Final lock and stop",
        "steps": [
            "User done language (e.g. as good as we'll get).",
            "NOTES: FINAL LOCK + master path + tempo/length summary.",
            "GATES: tick final; status FINAL LOCK.",
            "Do not rework unless user reopens.",
        ],
    },
    "shelf_track": {
        "title": "Shelf when concept fails",
        "steps": [
            "Stop creative thrash.",
            "Mark SHELVED in NOTES.",
            "New brief or different project — not the same dense stack rewritten silently.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    if key in ("list", "all", ""):
        return {"available": list(RECIPES.keys())}
    if key not in RECIPES:
        # fuzzy contains
        hits = [k for k in RECIPES if key in k]
        if len(hits) == 1:
            key = hits[0]
        else:
            return {"error": f"unknown recipe: {name}", "available": list(RECIPES.keys())}
    out = dict(RECIPES[key])
    out["key"] = key
    return out
