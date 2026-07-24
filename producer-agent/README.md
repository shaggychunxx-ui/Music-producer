# Producer Agent

A single unified agent that holds **all** knowledge in the Music-producer monorepo simultaneously: song pipeline, genre blueprints, recording/mixing, DAW operation, hardware instruments, music theory, composition, synthesis, and DSP.

## System prompt

Point your agent at **`AGENTS.md`** in this folder. It synthesises every domain in one place.

## What it knows

| Domain | Source |
|--------|--------|
| Gated original song pipeline (MVP → mix → late form → lock) | `song-creation-pipeline-github-agent/` · `production-workflow-knowledge/` |
| Genre production blueprints (37+ genres) | `producers-genre-guide-github-agent/` |
| Recording & mixing techniques by genre | `genre-mixing-github-agent/` |
| Studio One 6.6 DAW (all 22 chapters) | `studio-one-6.6-agent-knowledge/` |
| Moog Matriarch (full manual) | `matriarch-github-agent/` |
| Korg monologue | `monologue-github-agent/` |
| Roland TR-8S | `tr8s-github-agent/` |
| Output MOVEMENT | `movement-github-agent/` |
| PreSonus StudioLive Series III | `studiolive-github-agent/` |
| Music theory — modes & modulation | `music-theory-advanced-github-agent/` |
| Composition craft (Schoenberg) | `schoenberg-github-agent/` |
| Electronic music synthesis (Puckette) | `msp-techniques-github-agent/` |
| Digital audio signal processing (Zölzer) | `dsp-wiley-github-agent/` |

## When to use this vs individual agents

- **Producer agent** — conversational, multi-domain questions; full production sessions where you need genre + mix + DAW + hardware in one context.
- **Individual agents** — deep single-domain reference; exact hardware CC maps; per-chapter DAW lookups; CLI data queries against a specific `*_kb` package.

## Quick start

```powershell
# Run any sub-kb directly (no special producer-agent package needed)
cd ..\producers-genre-guide-github-agent
python -m producers_kb genre trap

cd ..\song-creation-pipeline-github-agent
python -m song_pipeline_kb phases
```

See root `README.md` and `AGENTS.md` for the full routing table.
