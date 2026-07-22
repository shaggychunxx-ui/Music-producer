from __future__ import annotations
from typing import Any

RECIPES = {
    "gain_structure": {"title": "Input gain structure", "steps": [
        "Follow manual Level Setting Procedure (ch.2).",
        "Set preamp gain for healthy meters without clipping Fat Channel.",
        "Balance channel faders near unity; use DCAs for group rides.",
    ]},
    "monitor_mix": {"title": "Create aux / FlexMix monitors", "steps": [
        "Configure FlexMix as aux; set pre/post sends as needed.",
        "Build per-musician mixes; link aux mutes if desired in system settings.",
        "Optional: GEQ + RTA to ring out wedges.",
    ]},
    "fat_vocal": {"title": "Fat Channel vocal chain", "steps": [
        "Select channel; set gate lightly if needed.",
        "Choose compressor model (Standard/Tube/FET) with gentle ratio.",
        "EQ (cut mud, presence boost carefully); A/B compare; save preset.",
    ]},
    "subgroup": {"title": "Instrument subgroup", "steps": [
        "Create FlexMix or fixed subgroup (model-dependent).",
        "Assign drums/keys/etc.; process bus as needed; send to main.",
    ]},
    "virtual_soundcheck": {"title": "Virtual soundcheck from SD", "steps": [
        "Record multitrack session to SD.",
        "Load session for playback; route tracks to channels.",
        "Adjust mix offline from stage levels.",
    ]},
    "scene_show": {"title": "Show scenes workflow", "steps": [
        "Create project; store scenes for songs/set changes.",
        "Use Scene Safe for critical channels; enable AutoStore carefully.",
        "Null motorized faders when recalling if needed.",
    ]},
    "patch_usb": {"title": "USB recording routing", "steps": [
        "Open Digital Patching; map channels to USB sends.",
        "Verify DAW inputs; use DAW button/transport integration as configured.",
    ]},
    "network_control": {"title": "UCNET control setup", "steps": [
        "Wired Ethernet control per networking overview.",
        "Set mixer nickname/IP; configure user permissions/profiles.",
        "Connect PreSonus control software/apps.",
    ]},
}

def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {"gain": "gain_structure", "aux": "monitor_mix", "monitors": "monitor_mix", "vocal": "fat_vocal", "vsc": "virtual_soundcheck", "scene": "scene_show"}
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe {name}. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
