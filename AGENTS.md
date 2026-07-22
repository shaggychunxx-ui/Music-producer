# Music-producer monorepo — agent router

You are working inside a **library of separate music-production agents**. Do not merge their knowledge. Pick the **single best agent folder** for the user’s question, then follow that folder’s `AGENTS.md`.

## Route by topic

| User is asking about… | Open this folder first |
|----------------------|-------------------------|
| Studio One DAW (record, edit, mix, master, instruments, effects) | `studio-one-6.6-agent-knowledge/` |
| StudioLive mixer / Series III | `studiolive-github-agent/` |
| Moog Matriarch patches, MIDI, modules | `matriarch-github-agent/` |
| Korg monologue | `monologue-github-agent/` |
| Roland TR-8S | `tr8s-github-agent/` |
| Output MOVEMENT | `movement-github-agent/` |
| How to produce a **genre** (BPM, drums, arrangement, vibe) | `producers-genre-guide-github-agent/` |
| **Recording/mixing techniques** by genre (EQ, comp, low end) | `genre-mixing-github-agent/` |
| Modes, modulation, advanced theory drills | `music-theory-advanced-github-agent/` |
| Motives, form, classical composition craft | `schoenberg-github-agent/` |
| Synthesis / electronic music **technique** (MSP / Puckette) | `msp-techniques-github-agent/` |
| DSP math, filters, transforms (Zölzer) | `dsp-wiley-github-agent/` |

## Rules

1. **Read the target folder’s `AGENTS.md`** before answering product- or book-specific questions.
2. Prefer **CLI/package data** (`python -m <pkg> …`) and `knowledge/` extracts over memory.
3. If two agents could apply (e.g. trap genre + mix), answer with **genre blueprint first**, then **mix notes**, and say which sources you used.
4. Never invent hardware CC maps, SysEx IDs, or edition-locked DAW features.
5. Manufacturer and publisher materials remain their copyright; you restate operational knowledge only.

## Quick CLI map

```text
producers_kb      producers-genre-guide-github-agent
genre_mix_kb      genre-mixing-github-agent
matriarch_kb      matriarch-github-agent
monologue_kb      monologue-github-agent
tr8s_kb           tr8s-github-agent
movement_kb       movement-github-agent
studiolive_kb     studiolive-github-agent
theory_kb         music-theory-advanced-github-agent
schoenberg_kb     schoenberg-github-agent
msp_kb            msp-techniques-github-agent
dsp_kb            dsp-wiley-github-agent
```

Studio One: use `INDEX.md` / `manifest.json` / `chapters/*.md` (no Python package required).
