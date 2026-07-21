from __future__ import annotations
from typing import Any

INSTRUMENT = {
    "name": "Roland TR-8S Rhythm Performer",
    "manual": "TR-8S Reference Manual eng01_W (program v1.02+)",
    "copyright": "© 2018 ROLAND CORPORATION",
    "source_url": "https://static.roland.com/assets/media/pdf/TR-8S_Reference_eng01_W.pdf",
    "update_url": "https://www.roland.com/support/",
    "pages": 50,
    "overview": "Rhythm performer with TR-style instruments, sample import, pattern variations, motion automation, FX, assignable/trigger outs, EXT IN, USB, SD.",
    "toc": [
        "Panel Descriptions", "Power / SD format", "Pattern / Kit / Motion overview",
        "Playing patterns (last step, fill, mute, solo, FX, tempo, nudge)",
        "Motion recording", "Pattern settings / WRITE / COPY / CLEAR",
        "TR-REC, INST REC, INST PLAY",
        "KIT Edit (REVERB, DELAY, MASTER FX, EXT IN, LFO, OUTPUT, MUTE, CTRL, COLOR, NAME)",
        "INST Edit / INST FX", "Import/export pattern & kit",
        "User samples (import/edit/delete/optimize)",
        "UTILITY menus", "Factory reset / backup / restore",
        "DAW/TB-3 sync, MIDI controller, trigger outs", "Error messages, audio diagram",
    ],
    "rear_io": ["MIX OUT", "PHONES", "EXT IN", "ASSIGNABLE/TRIGGER OUT", "MIDI", "USB", "SD", "DC IN"],
}

TOPICS: dict[str, dict[str, Any]] = {
    "panel": {"name": "Panel & connections", "summary": "VOLUME/EXT IN/SHIFT; instrument section; step pads; mode buttons; rear I/O. VOLUME does not control ASSIGNABLE OUT."},
    "pattern": {"name": "Patterns & variations", "summary": "Select/play; last step; fill manual/auto; random/copy/delete; mute/solo; tempo/tap/nudge."},
    "motion": {"name": "Motion", "summary": "Record/play/clear knob automation at steps."},
    "recording": {"name": "TR-REC / INST REC / INST PLAY", "summary": "Step record with sub-steps, flam, weak beats, ALT INST, accents, dynamics; realtime rec; live rolls."},
    "kit": {"name": "KIT Edit", "summary": "Reverb, delay, master FX, EXT IN, LFO, output, mute, CTRL assign, color, name; WRITE to save."},
    "inst": {"name": "INST Edit & INST FX", "summary": "Per-instrument tone and insert FX."},
    "samples": {"name": "User samples", "summary": "Import from SD, edit, assign to instruments, optimize area."},
    "utility": {"name": "UTILITY & system", "summary": "GENERAL, RELOAD, SAMPLE, LED, SYNC/TEMPO, MIDI, SOUND, MIX OUT, ASSIGN OUT, EXT IN, SD, INFORMATION; factory reset; backup/restore."},
    "sync": {"name": "Sync / MIDI / USB", "summary": "DAW slave, TB-3 master, MIDI controller mode, trigger outs, STORAGE MODE."},
    "fx": {"name": "Reverb / Delay / Master FX", "summary": "Per-inst sends and kit master FX with CTRL knob assignment."},
}

def list_topics():
    return list(TOPICS.keys())

def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {"patterns": "pattern", "kits": "kit", "sample": "samples", "midi": "sync", "usb": "sync", "rec": "recording", "tr_rec": "recording"}
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic {name}. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
