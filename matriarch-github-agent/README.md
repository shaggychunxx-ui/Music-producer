# Matriarch GitHub Agent

Structured knowledge base + agent instructions transcribed from the **Moog Matriarch Owner’s Manual (012023 / January 2023)**.

Use this repo to power a **GitHub coding agent**, Copilot custom agent, or any LLM that should answer Matriarch questions accurately (modules, patch points, MIDI CCs, SysEx, Global Settings, recipes).

## Contents

| Path | Purpose |
|------|---------|
| [`AGENTS.md`](AGENTS.md) | System prompt / agent behavior for GitHub Agent or similar |
| [`matriarch_kb/`](matriarch_kb/) | Queryable Python knowledge package |
| [`knowledge/manual_extract.txt`](knowledge/manual_extract.txt) | Full text extract of the 92-page manual |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Copilot-oriented pointer to AGENTS.md |

## Quick start

```bash
cd matriarch-github-agent

# Overview
python -m matriarch_kb info

# Modules
python -m matriarch_kb list-modules
python -m matriarch_kb module filters
python -m matriarch_kb module stereo_delay

# MIDI
python -m matriarch_kb cc "delay time"
python -m matriarch_kb sysex 55
python -m matriarch_kb sysex-set 55 2

# Recipes & search
python -m matriarch_kb recipe bass
python -m matriarch_kb search "ping pong"
python -m matriarch_kb globals-howto
```

### Python API

```python
from matriarch_kb import get_module, lookup_cc, lookup_sysex, get_recipe, search_kb

print(get_module("oscillators")["patch_points"])
print(lookup_cc("Delay Time"))
print(lookup_sysex(55))  # Paraphony Mode
print(get_recipe("sync_lead"))
print(search_kb("hard sync"))
```

## Wire up a GitHub agent

1. Push this folder to a GitHub repository.
2. Point your agent / custom instructions at **`AGENTS.md`** (primary) and **`matriarch_kb/`** (facts).
3. For GitHub Copilot coding agent, keep `.github/copilot-instructions.md` so the agent loads the same rules.
4. Optional: run `python -m matriarch_kb export-json > knowledge/matriarch.json` for non-Python tools.

## What was transcribed

- Instrument overview, signal flow, filter modes, paraphony
- Per-module controls and 3.5 mm patch-point voltage ranges
- Rear panel audio / CV / clock / MIDI
- Global Settings entry method + parameter groups
- Full MIDI CC map and SysEx parameter IDs 0–74
- Practical patch recipes (bass, sync, ring mod, S/H, delay, modular I/O)
- Specs, safety, support pointers

## Source & copyright

- Source PDF: `Matriarch_Manual_012023.pdf` (Moog Music Inc.)
- Technical facts re-encoded for personal / studio agent use.
- Manual prose, graphics, and trademarks remain © Moog Music Inc.
- Not an official Moog product or endorsement.

## License (code)

MIT for the Python package and agent scaffolding. Manual extract retained for local reference; do not republish Moog’s manual as your own work.
