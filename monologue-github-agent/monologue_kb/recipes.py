from __future__ import annotations
from typing import Any

RECIPES = {
    "first_boot": {"title": "Power on & pick a program", "steps": [
        "Connect headphones/speakers; volume down.",
        "Hold rear power until logo; raise MASTER.",
        "Ensure EDIT MODE unlit (Play mode); turn PROGRAM/VALUE to browse 001-080.",
        "Play keys; try OCTAVE, DRIVE, Slider.",
    ]},
    "create_sound": {"title": "Design a mono lead/bass", "steps": [
        "VCO1 saw/sqr + shape; VCO2 detune or interval; optional SYNC/RING.",
        "Mixer levels; filter cutoff/res; add DRIVE carefully.",
        "EG type/attack/decay to amp or filter; LFO to pitch/cutoff.",
        "WRITE to a user slot 081-100.",
    ]},
    "sequence": {"title": "Record a 16-step sequence", "steps": [
        "Select program; REC; enter notes/rests on steps; set slides.",
        "MOTION mode: record up to 4 parameter motions.",
        "Adjust TEMPO/swing/gate in SEQ EDIT; WRITE program.",
    ]},
    "sync_volca": {"title": "Sync with volca", "steps": [
        "Patch SYNC cables (watch master/slave GLOBAL settings).",
        "Align tempos; use monologue as master or slave per setup.",
    ]},
    "disable_auto_off": {"title": "Disable Auto Power Off", "steps": [
        "EDIT MODE → GLOBAL EDIT → button 8 twice → Auto Power Off → Off → EXIT.",
    ]},
    "midi_usb": {"title": "USB MIDI with DAW", "steps": [
        "USB B to computer; set GLOBAL MIDI params; verify channels.",
        "Save programs before powering off.",
    ]},
}

def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {"sound": "create_sound", "seq": "sequence", "sync": "sync_volca", "auto_off": "disable_auto_off"}
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe {name}. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
