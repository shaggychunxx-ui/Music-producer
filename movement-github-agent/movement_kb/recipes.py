"""Practical MOVEMENT design recipes."""

from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "install_activate": {
        "title": "Install & activate",
        "steps": [
            "Get serial from purchase email.",
            "Install Output Connect; paste serial; download MOVEMENT installer.",
            "Run installer; insert plugin on an audio or instrument track in your DAW.",
            "Paste serial when prompted and click Activate.",
        ],
    },
    "first_rhythm": {
        "title": "First rhythmic filter",
        "steps": [
            "Mute Engine B (or A) so only one path is audible.",
            "On active engine: add Filter via +; set type LP 4-pole.",
            "Open Rhythm 1 (or 3 if on B); choose LFO pulse or sine; set musical rate.",
            "Drag rhythm number onto Cutoff; raise rhythm slider under the knob.",
            "Optional: add slight Drive or Compression for movement to feel stronger.",
        ],
    },
    "pump": {
        "title": "Sidechain-style pump (internal or external)",
        "steps": [
            "Route a kick to MOVEMENT sidechain (DAW-specific; use link under Full Range).",
            "Set rhythm mode to Sidechain; choose Duck on level or filter cutoff.",
            "Tune Attack/Release/Gain; try Full Range off for unipolar ducking.",
            "Or: use step sequencer square pattern on volume for fixed pump without sidechain.",
        ],
    },
    "dual_engine": {
        "title": "Dual-engine stereo interest",
        "steps": [
            "Engine A: delay + LFO on feedback or wet; pan slightly L.",
            "Engine B: filter or distortion; different rate/phase; pan slightly R.",
            "Ensure both engines unmuted with complementary wet/dry so neither masks the other.",
            "Assign macros on XY: Y controls A intensity, X controls B intensity.",
        ],
    },
    "flux_chaos": {
        "title": "Flux rate warping",
        "steps": [
            "On one engine set two rhythms (e.g. LFO + step).",
            "Enable Flux On (or drag rhythm circle onto the other rate).",
            "Set slider so rate swings between slow and fast divisions.",
            "Assign resulting rhythm to filter or delay time for evolving grooves.",
        ],
    },
    "step_gate": {
        "title": "32-step trance gate",
        "steps": [
            "Rhythm = Step Sequencer; raise step count; pick rate (e.g. 1/16).",
            "Use square step shape for classic gates; or shaped steps for softer envelopes.",
            "Pattern preset or Random; Swing for humanize.",
            "Assign to Engine volume and/or distortion Drive; set amount slider.",
        ],
    },
    "xy_performance": {
        "title": "XY performance macro",
        "steps": [
            "Dial knobs and rhythm sliders to a starting sound.",
            "Right-click key knobs → Assign to XY Control.",
            "Set knob range above/below midpoint for direction; set rhythm amount range.",
            "Enable power on axes; perform with pad (Y=A, X=B).",
        ],
    },
    "save_preset": {
        "title": "Save and find presets",
        "steps": [
            "Click save icon top-left; name + tags; save (XML).",
            "Open browser via preset name; search/tag/favorite.",
            "Folders: Mac /Users/Shared/Output/Movement/Presets ; "
            "PC C:/Users/Public/Documents/Output/Movement/Presets",
        ],
    },
    "low_cpu": {
        "title": "Reduce GUI CPU",
        "steps": [
            "Enable Low CPU mode to freeze motion graphics.",
            "Audio processing is unchanged — only animation stops.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "install": "install_activate",
        "activate": "install_activate",
        "sidechain": "pump",
        "gate": "step_gate",
        "xy": "xy_performance",
        "macro": "xy_performance",
        "preset": "save_preset",
        "cpu": "low_cpu",
        "filter": "first_rhythm",
    }
    key = aliases.get(key, key)
    if key not in RECIPES:
        raise KeyError(f"Unknown recipe '{name}'. Try: {', '.join(RECIPES)}")
    return RECIPES[key]
