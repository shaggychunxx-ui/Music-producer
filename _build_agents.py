#!/usr/bin/env python3
"""Generate separate GitHub agent packages for TR-8S, monologue, StudioLive."""
from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent


def w(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  {path.relative_to(BASE)} ({path.stat().st_size} bytes)")


def package_common(
    root: Path,
    pkg: str,
    title: str,
    agents_md: str,
    instrument_py: str,
    recipes_py: str,
    readme: str,
    cli_name: str,
) -> None:
    print(f"=== {title} ===")
    w(root / "AGENTS.md", agents_md)
    w(root / pkg / "__init__.py", f'''from {pkg}.instrument import INSTRUMENT, TOPICS, get_topic, list_topics
from {pkg}.recipes import RECIPES, get_recipe
from {pkg}.search import search_kb
__all__ = ["INSTRUMENT", "TOPICS", "get_topic", "list_topics", "RECIPES", "get_recipe", "search_kb"]
__version__ = "1.0.0"
''')
    w(root / pkg / "instrument.py", instrument_py)
    w(root / pkg / "recipes.py", recipes_py)
    w(
        root / pkg / "search.py",
        f'''from __future__ import annotations
from pathlib import Path
from {pkg} import instrument, recipes

_EXTRACT = Path(__file__).resolve().parent.parent / "knowledge" / "manual_extract.txt"

def _walk(obj, path=""):
    rows = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            rows += _walk(v, f"{{path}}.{{k}}" if path else str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            rows += _walk(v, f"{{path}}[{{i}}]")
    else:
        rows.append((path, str(obj)))
    return rows

def search_kb(query: str, limit: int = 20):
    terms = query.lower().split()
    hits = []
    corpus = {{"instrument": instrument.INSTRUMENT, "topics": instrument.TOPICS, "recipes": recipes.RECIPES}}
    for path, text in _walk(corpus):
        blob = f"{{path}} {{text}}".lower()
        if all(t in blob for t in terms):
            hits.append({{"source": "kb", "path": path, "text": text[:400]}})
            if len(hits) >= limit:
                return hits
    if _EXTRACT.exists() and len(hits) < limit:
        raw = _EXTRACT.read_text(encoding="utf-8", errors="ignore")
        for block in raw.split("---PAGE "):
            if not block.strip():
                continue
            head, _, body = block.partition("---")
            page = head.strip().split()[0] if head.strip() else "?"
            low = body.lower()
            if all(t in low for t in terms):
                i = low.find(terms[0])
                sn = body[max(0, i - 60) : i + 280].replace("\\n", " ")
                hits.append({{"source": "extract", "path": f"page {{page}}", "text": sn.strip()}})
                if len(hits) >= limit:
                    break
    return hits
''',
    )
    w(
        root / pkg / "__main__.py",
        f'''import argparse, json
from {pkg} import INSTRUMENT, get_topic, list_topics, get_recipe, search_kb
from {pkg}.recipes import RECIPES

def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)

def main(argv=None):
    p = argparse.ArgumentParser(prog="{cli_name}")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("topics")
    t = s.add_parser("topic"); t.add_argument("name")
    r = s.add_parser("recipe"); r.add_argument("name", nargs="?", default="")
    q = s.add_parser("search"); q.add_argument("query"); q.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    if a.cmd == "info":
        _p(INSTRUMENT)
    elif a.cmd == "topics":
        print("\\n".join(list_topics()))
    elif a.cmd == "topic":
        _p(get_topic(a.name))
    elif a.cmd == "recipe":
        if not a.name:
            print("Available:", ", ".join(RECIPES))
        else:
            _p(get_recipe(a.name))
    elif a.cmd == "search":
        _p(search_kb(a.query, a.limit))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
''',
    )
    w(root / "README.md", readme)
    w(
        root / ".github" / "copilot-instructions.md",
        f"# {title}\n\nFollow `AGENTS.md`. Prefer `{pkg}/` and `knowledge/manual_extract.txt`.\n",
    )
    w(
        root / "pyproject.toml",
        f'''[project]
name = "{cli_name}"
version = "1.0.0"
requires-python = ">=3.10"
[project.scripts]
{cli_name} = "{pkg}.__main__:main"
''',
    )
    w(
        root / "LICENSE",
        "MIT for agent scaffolding only. Manufacturer manuals remain copyright of their owners.\n",
    )


def build_tr8s() -> None:
    root = BASE / "tr8s-github-agent"
    agents = """# Roland TR-8S Agent

You are an expert on the **Roland TR-8S Rhythm Performer** from the *TR-8S Reference Manual* (program **v1.02+**, © 2018 Roland).
Ground answers in `tr8s_kb/` and `knowledge/manual_extract.txt`.

## Role
Explain panel, Pattern/Kit/Motion, TR-REC / INST REC / INST PLAY, kit & instrument edit, samples, UTILITY, sync/MIDI/USB, I/O. Use exact button names.

## Core terms
- **PATTERN** — sequence (variations, tracks, last step, fills, motion, kit assignment)
- **KIT** — sounds + reverb/delay/master FX + EXT IN + LFO + outputs + mute/CTRL/color/name
- **MOTION** — step automation of knob moves
- **TR-REC** — classic step recording; **INST REC** realtime; **INST PLAY** live performance

## I/O notes
VOLUME affects MIX OUT / PHONES only (not ASSIGNABLE OUT). EXT IN for external audio. SD for samples/backup. USB for DAW + STORAGE MODE.

## CLI
```bash
python -m tr8s_kb info
python -m tr8s_kb topic motion
python -m tr8s_kb search "fill in"
python -m tr8s_kb recipe step_record
```
"""
    instrument = '''from __future__ import annotations
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
'''
    recipes = '''from __future__ import annotations
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
'''
    readme = """# Roland TR-8S GitHub Agent

From [TR-8S Reference Manual](https://static.roland.com/assets/media/pdf/TR-8S_Reference_eng01_W.pdf) (v1.02+).

```bash
python -m tr8s_kb info
python -m tr8s_kb topic motion
python -m tr8s_kb search "MASTER FX"
```

Manual © Roland. Scaffolding for local agent use.
"""
    package_common(root, "tr8s_kb", "Roland TR-8S", agents, instrument, recipes, readme, "tr8s-kb")


def build_monologue() -> None:
    root = BASE / "monologue-github-agent"
    agents = """# Korg monologue Agent

You are an expert on the **Korg monologue** monophonic analog synthesizer (Owner’s Manual).
Ground answers in `monologue_kb/` and `knowledge/manual_extract.txt`.

## Role
Explain architecture, panel, programs, sound design (VCO/mixer/filter/EG/LFO/drive), 16-step sequencer + motion sequence, PROGRAM/SEQ/GLOBAL edit, MIDI/USB/Sync, battery power.

## Architecture (block diagram)
VCO1 (SAW/SQR + shape) + VCO2 (SAW/TRI + pitch/octave + SYNC/RING + shape) + NOISE → MIXER → VCF → DRIVE → VCA/OUT
Modulation: EG (type/attack/decay/int/target), LFO (wave/mode/rate/int/target), velocity, keytrack.

## Programs
100 programs: **001–080 factory**, **081–100 user**. Each program stores sound **and** sequence data. Unsaved edits lost on power-off.

## Sequencer
16-step mono sequencer; up to **4 motion** parameters; slide/note/motion modes; KEY TRG/HOLD; tempo 56–240 BPM; swing, gate, active steps.

## Edit modes
- **PROGRAM EDIT** — slider assign, sound params, etc.
- **SEQ EDIT** — step length/resolution/swing/BPM/motion enable-smooth
- **GLOBAL EDIT** — MIDI, sync, battery type, auto power off, etc. (saved automatically)

## Power
6× AA or optional 9V DC adapter. Hold power switch on rear. Auto Power Off default 4 hours (disable in GLOBAL). Wait ~10s before re-power.

## CLI
```bash
python -m monologue_kb info
python -m monologue_kb topic sequencer
python -m monologue_kb search "SYNC"
python -m monologue_kb recipe create_sound
```
"""
    instrument = '''from __future__ import annotations
from typing import Any

INSTRUMENT = {
    "name": "Korg monologue",
    "type": "Monophonic analog synthesizer",
    "manual": "monologue Owner's Manual (English)",
    "source_url": "https://cdn.korg.com/us/support/download/files/d05d6cb06052aed2b067eea2dfa4f7cd.pdf",
    "pages": 59,
    "lineage": "Analog circuit based on minilogue design; VCF tuned for mono; drive circuit for aggressive tones",
    "features": [
        "Battery powered (6x AA) or DC 9V adapter",
        "80 factory + 20 user programs",
        "Real-time oscilloscope display",
        "16-step sequencer with up to 4 motion parameters",
        "Sync In/Out for volca/DAW expansion",
        "USB and 5-pin MIDI",
    ],
    "signal_path": [
        "VCO1 (SAW/SQR, SHAPE)",
        "VCO2 (SAW/TRI, OCTAVE, PITCH, SYNC/RING, SHAPE)",
        "NOISE",
        "MIXER (VCO1/VCO2 levels)",
        "VCF (CUTOFF, RESONANCE)",
        "DRIVE",
        "VCA / OUTPUT (+ AUDIO IN path)",
    ],
    "front_panel": [
        "MASTER", "DRIVE", "OCTAVE (±2)", "Slider (program-assignable)",
        "VCO1 WAVE/SHAPE", "VCO2 OCTAVE/PITCH/WAVE/SYNC-RING/SHAPE",
        "MIXER VCO1/VCO2", "FILTER CUTOFF/RESONANCE",
        "EG TYPE/ATTACK/DECAY/INT/TARGET",
        "LFO WAVE/MODE/RATE/INT/TARGET",
        "SEQUENCER TEMPO, KEY TRG/HOLD, MOTION/SLIDE/NOTE, PLAY/REC/REST/SHIFT, steps 1-8 (+shift 9-16)",
        "PROGRAM/VALUE", "Display (scope)", "EDIT MODE / WRITE / EXIT",
    ],
    "rear": ["USB B", "Power", "MIDI IN/OUT", "SYNC IN/OUT", "AUDIO IN", "OUTPUT", "Headphones", "DC 9V"],
    "toc": [
        "Introduction & features", "Block diagram", "Controls & connections",
        "Power on/off, batteries, auto power off",
        "Play programs & sequencer", "Program architecture & editing",
        "Sequencer & motion sequence",
        "Edit mode: PROGRAM / SEQ / GLOBAL",
        "Tuning, factory restore, SHIFT shortcuts",
        "MIDI/USB", "Program list", "Specifications", "MIDI implementation chart",
    ],
    "program_memory": {"factory": "001-080", "user": "081-100", "includes": "sound + sequence"},
    "sync_out": "5 V pulse, 15 ms at beginning of each step",
}

TOPICS: dict[str, dict[str, Any]] = {
    "overview": {"name": "Overview & features", "summary": "Mono analog (minilogue lineage), drive, portable, 100 programs, scope, 16-step + motion, sync I/O."},
    "panel": {"name": "Controls & connections", "summary": "Front synth voice + sequencer; rear MIDI/USB/sync/audio/power."},
    "power": {"name": "Power", "summary": "6x AA or 9V adapter; hold power switch; save programs before off; auto power off 4h default; battery type in GLOBAL."},
    "programs": {"name": "Programs", "summary": "Select with PROGRAM/VALUE; SHIFT+knob skips 10; save via WRITE; architecture VCO/mixer/filter/EG/LFO/seq."},
    "sound": {"name": "Sound design", "summary": "VCO1/2 waves & shape; sync/ring; filter; drive; EG targets; LFO targets; AUDIO IN."},
    "sequencer": {"name": "Sequencer", "summary": "16 steps; PLAY/REC; KEY TRG/HOLD transpose/latch; MOTION/SLIDE/NOTE; tempo 56-240; rests, active steps."},
    "motion": {"name": "Motion sequence", "summary": "Automate up to 4 synth parameters per program; enable/smooth in SEQ EDIT."},
    "edit": {"name": "Edit modes", "summary": "EDIT MODE button; PROGRAM EDIT, SEQ EDIT, GLOBAL EDIT parameter lists."},
    "midi": {"name": "MIDI & USB", "summary": "DIN + USB; local/MIDI channel/filter settings in GLOBAL; control external or be controlled."},
    "sync": {"name": "Sync I/O", "summary": "Pulse sync with volca etc.; SYNC OUT 5V 15ms/step; GLOBAL settings for sync behavior."},
    "maintenance": {"name": "Tuning / factory / shortcuts", "summary": "Tuning function; restore factory; SHIFT button shortcuts table."},
}

def list_topics():
    return list(TOPICS.keys())

def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {"seq": "sequencer", "voice": "sound", "filter": "sound", "vco": "sound", "global": "edit", "usb": "midi"}
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic {name}. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
'''
    recipes = '''from __future__ import annotations
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
'''
    readme = """# Korg monologue GitHub Agent

From Korg monologue owner’s manual PDF.

```bash
python -m monologue_kb info
python -m monologue_kb topic sequencer
python -m monologue_kb recipe create_sound
```

Manual © Korg. Scaffolding for local agent use.
"""
    package_common(root, "monologue_kb", "Korg monologue", agents, instrument, recipes, readme, "monologue-kb")
    # keep original pdf name; also copy-friendly alias note
    pdf = root / "knowledge" / "korg_manual.pdf"
    if pdf.exists():
        alias = root / "knowledge" / "monologue_Owners_Manual.pdf"
        if not alias.exists():
            alias.write_bytes(pdf.read_bytes())
            print("  duplicated monologue_Owners_Manual.pdf")


def build_studiolive() -> None:
    root = BASE / "studiolive-github-agent"
    agents = """# PreSonus StudioLive Series III Agent

You are an expert on **PreSonus StudioLive Series III** digital mixers from the *Owner’s Manual V6 EN* (2019).
Models: **64S, 32S, 32SX, 32SC** (S) and Blue **32/24/16** (need firmware v2.0+). Shared features illustrated primarily on **64S**.
Ground answers in `studiolive_kb/` and `knowledge/manual_extract.txt`.

## Role
Guide live/studio mixing: levels, Fat Channel, FlexMixes, DCAs, digital patching, SD capture, UCNET, scenes/projects, monitoring, GEQ/RTA, networking.

## Core concepts
| Concept | Meaning |
|---------|---------|
| **Fat Channel** | Per-channel dynamics/EQ/plugins (gate, compressors, EQs), A/B compare, copy/paste presets |
| **FlexMixes** | Configurable buses (aux / subgroup / matrix) |
| **Fader layers** | Banked fader views + User layer |
| **Filter DCA** | DCA-style group control with filtering options |
| **Digital patching** | Route input sources, analog/AVB/USB/SD/AES sends |
| **Projects / Scenes / Presets** | Show file hierarchy; AutoStore; Scene Safe; nulling |
| **UCNET** | Network control, permissions, software control |
| **Capture / SD** | Multitrack record/playback; virtual soundcheck |
| **FLEX DSP FX** | Internal bus effects rack |

## Manual map
1 Overview · 2 Getting Started (gain) · 3 Hookup · 4 Basic mix · 5 Buses · 6 Fat Channel · 7 Tape/BT · 8 SD Recording · 9 Master/UCNET/Scenes · 10 Solo · 11 GEQ · 12 Home/patching/profiles · 13 Resources (mics, comp/EQ recipes, delays, sidechain) · 14 Specs/routing/troubleshoot

## Answering style
- Call out **model differences** (64S mono/LCR, 32-ch fixed subgroups, Blue vs S).
- Prefer gain-structure first, then bus/FX, then show scenes.
- Use Power User Tips mindset from manual.

## CLI
```bash
python -m studiolive_kb info
python -m studiolive_kb topic fat_channel
python -m studiolive_kb search "FlexMix"
python -m studiolive_kb recipe gain_structure
```
"""
    instrument = '''from __future__ import annotations
from typing import Any

INSTRUMENT = {
    "name": "PreSonus StudioLive Series III",
    "type": "Digital mix console / recorder with motorized faders",
    "manual": "StudioLive Series III Owner's Manual V6 EN (2019-10-06)",
    "source_url": "https://pae-web.presonusmusic.com/downloads/products/pdf/StudioLive_Series_III_OwnersManual_V6_EN_10062019.pdf",
    "pages": 157,
    "models": {
        "S": ["StudioLive 64S", "StudioLive 32S", "StudioLive 32SX", "StudioLive 32SC"],
        "Blue": ["StudioLive 32", "StudioLive 24", "StudioLive 16"],
        "blue_firmware": "v2.0 or later required for Blue models in this manual family",
        "illustration_default": "StudioLive 64S for shared features",
    },
    "toc": [
        "1 Overview",
        "2 Getting Started (level setting, useful concepts)",
        "3 Hookup (rear configs, I/O, band/church diagrams)",
        "4 Basic mix (channel strip, fader layers, Filter DCA, meters, talkback)",
        "5 Buses (FlexMixes, aux, subgroups, matrix, FX, mono/LCR on 64S)",
        "6 Fat Channel (gate/comp/EQ plugins, navigation, input, assignments)",
        "7 Tape / Bluetooth",
        "8 SD Recording & virtual soundcheck",
        "9 Master Control (FLEX DSP FX, UCNET, DAW, scenes/projects)",
        "10 Monitoring / Solo",
        "11 Graphic EQ & RTA ring-out",
        "12 Home (system, user profiles, digital patching, soft power)",
        "13 Resources (networking, mic placement, compression/EQ guides, delays, sidechain, FX types)",
        "14 Technical (specs, default routing, block diagrams, troubleshooting)",
    ],
    "key_concepts": [
        "Select buttons + Fat Channel",
        "Fat Channel plugins",
        "FlexMixes",
        "Fader layers / User layer",
        "DCA / Filter DCA groups",
        "Recording & playback (USB/SD)",
        "Digital patching",
        "Projects, scenes, presets",
        "User profiles & permissions",
    ],
}

TOPICS: dict[str, dict[str, Any]] = {
    "overview": {"name": "Overview & models", "summary": "Series III S and Blue models; shared workflows; 64S used in illustrations; companion PreSonus ecosystem."},
    "getting_started": {"name": "Getting started / gain", "summary": "Level setting procedure; useful concepts for first session."},
    "hookup": {"name": "Hookup & I/O", "summary": "Model rear panels; analog I/O; digital/networking; power; band/church setup diagrams."},
    "mix_basics": {"name": "Basic mix functions", "summary": "Channel strip; fader layers/banks; User layer; Filter DCA create/edit; main meters; talkback."},
    "buses": {"name": "Buses & routing", "summary": "FlexMixes; aux pre/post; external FX; subgroups (fixed on some 32-ch); matrix/front fill; FX buses; 64S mono/LCR."},
    "fat_channel": {"name": "Fat Channel", "summary": "Gate; Standard/Tube/FET compressors; Standard/Passive/Vintage EQ; A/B compare; copy/paste/presets; aux sends mode; input polarity/phantom/stereo link; bus assigns."},
    "sd_recording": {"name": "SD recording", "summary": "New session; load playback; Capture screen; transport; virtual soundcheck."},
    "scenes": {"name": "Scenes & projects", "summary": "Create/recall projects & scenes; filters; list editor; scene safe; AutoStore; reset; nulling parameters."},
    "ucnet": {"name": "UCNET & control", "summary": "Mixer nickname; permissions; software control; control network IP; transport; DAW button."},
    "fx": {"name": "FLEX DSP effects", "summary": "Effects editor; types; presets for internal bus FX."},
    "monitoring": {"name": "Solo / monitoring", "summary": "Solo modes; solo bus; solo-in-place for mix setup."},
    "geq": {"name": "Graphic EQ & RTA", "summary": "Assign GEQs; presets; use RTA to ring out monitors."},
    "patching": {"name": "Digital patching", "summary": "Input sources; analog/AVB/USB/SD/AES sends; default routing tables in tech chapter."},
    "profiles": {"name": "User profiles", "summary": "Administrator; create profiles; edit permissions."},
    "resources": {"name": "Mixing resources", "summary": "Mic placement; compression/EQ suggestions; input/output delay alignment; sidechain; effect type primers; RTA while mixing."},
    "troubleshooting": {"name": "Specs & troubleshooting", "summary": "Specifications, block diagrams, troubleshooting section."},
}

def list_topics():
    return list(TOPICS.keys())

def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "fat": "fat_channel", "eq": "fat_channel", "compressor": "fat_channel",
        "flexmix": "buses", "aux": "buses", "matrix": "buses", "dca": "mix_basics",
        "scene": "scenes", "project": "scenes", "record": "sd_recording", "sd": "sd_recording",
        "network": "ucnet", "avb": "patching", "usb": "patching", "solo": "monitoring",
        "rta": "geq", "gain": "getting_started",
    }
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic {name}. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
'''
    recipes = '''from __future__ import annotations
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
'''
    readme = """# PreSonus StudioLive Series III GitHub Agent

From StudioLive Series III Owner’s Manual V6 EN.

```bash
python -m studiolive_kb info
python -m studiolive_kb topic fat_channel
python -m studiolive_kb recipe gain_structure
```

Manual © PreSonus. Scaffolding for local agent use.
"""
    package_common(root, "studiolive_kb", "StudioLive Series III", agents, instrument, recipes, readme, "studiolive-kb")


def write_index() -> None:
    readme = """# GitHub Agents Library

Local collection of **separate** manufacturer-manual GitHub agents.

**Location:** `Documents/github-agents/`

| Folder | Product | Manual source |
|--------|---------|----------------|
| `matriarch-github-agent` | Moog Matriarch | https://cdn.inmusicbrands.com/Moog/Matriarch/Matriarch_Manual_012023.pdf |
| `monologue-github-agent` | Korg monologue | https://cdn.korg.com/us/support/download/files/d05d6cb06052aed2b067eea2dfa4f7cd.pdf |
| `tr8s-github-agent` | Roland TR-8S | https://static.roland.com/assets/media/pdf/TR-8S_Reference_eng01_W.pdf |
| `studiolive-github-agent` | PreSonus StudioLive Series III | https://pae-web.presonusmusic.com/downloads/products/pdf/StudioLive_Series_III_OwnersManual_V6_EN_10062019.pdf |
| `schoenberg-github-agent` | Schoenberg *Fundamentals of Musical Composition* | monoskop / text edition extract |

## How each agent is laid out

```
<agent-name>/
  AGENTS.md                 # system prompt for GitHub / Copilot agent
  <pkg>_kb/                 # queryable Python knowledge package
  knowledge/
    *.pdf                   # source manual
    manual_extract.txt      # full text extract (when available)
  .github/copilot-instructions.md
  README.md
```

## Quick tests

```powershell
cd "$env:USERPROFILE\\Documents\\github-agents"

python -m matriarch-github-agent.matriarch_kb 2>$null
# from each folder:
cd matriarch-github-agent;  python -m matriarch_kb info
cd ..\\monologue-github-agent; python -m monologue_kb info
cd ..\\tr8s-github-agent;      python -m tr8s_kb info
cd ..\\studiolive-github-agent; python -m studiolive_kb info
cd ..\\schoenberg-github-agent; python -m schoenberg_kb info
```

## Notes

- Agents are **separate** on purpose (do not merge knowledge bases).
- Manufacturer manuals remain copyright of their owners; packages re-encode operational knowledge for local assistants.
- Matriarch official CDN PDF is largely image-based; structured `matriarch_kb` comes from prior full transcription. Extract quality varies by PDF text layer.
"""
    w(BASE / "README.md", readme)


def touch_matriarch_source_note() -> None:
    p = BASE / "matriarch-github-agent" / "knowledge" / "SOURCE.txt"
    p.write_text(
        "Official manual: https://cdn.inmusicbrands.com/Moog/Matriarch/Matriarch_Manual_012023.pdf\n"
        "Local file: Matriarch_Manual_012023.pdf\n"
        "Note: PDF is largely non-OCR; structured knowledge is in ../matriarch_kb and AGENTS.md.\n",
        encoding="utf-8",
    )
    print("  matriarch SOURCE.txt")


def main() -> None:
    build_tr8s()
    build_monologue()
    build_studiolive()
    touch_matriarch_source_note()
    write_index()
    print("ALL DONE")


if __name__ == "__main__":
    main()
