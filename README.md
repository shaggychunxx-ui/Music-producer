# Music-producer

Monorepo of **separate, single-purpose music production agents** — gear manuals, theory books, DAW reference, and genre production guides.

Each agent is intentionally isolated: one knowledge base, one system prompt, one CLI. Use them with GitHub Copilot agents, custom LLM agents, or plain Python.

**GitHub:** [shaggychunxx-ui/Music-producer](https://github.com/shaggychunxx-ui/Music-producer)

## Agents

| Folder | Domain | CLI package | Source |
|--------|--------|-------------|--------|
| [`studio-one-6.6-agent-knowledge`](studio-one-6.6-agent-knowledge/) | PreSonus Studio One 6.6 | Markdown chapters + `manifest.json` | Reference Manual (EN) |
| [`studiolive-github-agent`](studiolive-github-agent/) | StudioLive Series III | `studiolive_kb` | Series III Owner's Manual |
| [`matriarch-github-agent`](matriarch-github-agent/) | Moog Matriarch | `matriarch_kb` | Matriarch Manual 01/2023 |
| [`monologue-github-agent`](monologue-github-agent/) | Korg monologue | `monologue_kb` | monologue Owner's Manual |
| [`tr8s-github-agent`](tr8s-github-agent/) | Roland TR-8S | `tr8s_kb` | TR-8S Reference |
| [`movement-github-agent`](movement-github-agent/) | Output MOVEMENT | `movement_kb` | Movement User Guide |
| [`producers-genre-guide-github-agent`](producers-genre-guide-github-agent/) | Genre production blueprints | `producers_kb` | Music Producer's Complete Genre Guide |
| [`genre-mixing-github-agent`](genre-mixing-github-agent/) | Recording & mixing by genre | `genre_mix_kb` | [Pirate.com article](https://pirate.com/en/blog/recording-mixing-techniques-different-genres/) |
| [`song-creation-pipeline-github-agent`](song-creation-pipeline-github-agent/) | Gated original song pipeline (MVP → mix → late form) | `song_pipeline_kb` | Standing studio process extract |
| [`music-theory-advanced-github-agent`](music-theory-advanced-github-agent/) | Modes, modulation, advanced theory | `theory_kb` | Music Theory Advanced |
| [`schoenberg-github-agent`](schoenberg-github-agent/) | Composition fundamentals | `schoenberg_kb` | Schoenberg *Fundamentals of Musical Composition* |
| [`msp-techniques-github-agent`](msp-techniques-github-agent/) | Electronic music technique | `msp_kb` | Miller Puckette *Theory and Technique of Electronic Music* |
| [`dsp-wiley-github-agent`](dsp-wiley-github-agent/) | Digital audio signal processing | `dsp_kb` | Zölzer *Digital Audio Signal Processing* 2e |

## Layout of each `*-github-agent`

```text
<agent-name>/
  AGENTS.md                      # system prompt (primary agent instructions)
  <pkg>_kb/                      # queryable Python knowledge package
  knowledge/
    *.pdf                        # source manual (when redistributable locally)
    manual_extract.txt           # full text extract
  .github/copilot-instructions.md
  README.md
  pyproject.toml
  LICENSE
```

Studio One uses a **Markdown chapter pack** (`chapters/`, `INDEX.md`, `manifest.json`) instead of a `*_kb` package — see its folder README.

## Quick start

### Requirements

- Python 3.10+
- Optional: `pymupdf` only if you re-run extract/build scripts

### Smoke-test every CLI agent

```powershell
cd path\to\Music-producer
python scripts/verify_agents.py
```

### Example queries

```powershell
# Song creation pipeline (gates, recipes, phrase book)
cd song-creation-pipeline-github-agent
python -m song_pipeline_kb info
python -m song_pipeline_kb phases
python -m song_pipeline_kb recipe duck_mild_short
python -m song_pipeline_kb phrase "still pumps"

# Genre blueprints
cd ..\producers-genre-guide-github-agent
python -m producers_kb genres
python -m producers_kb genre trap
python -m producers_kb foundation mix_master
python -m producers_kb recipe start_track
python -m producers_kb search "sidechain"

# Hardware
cd ..\matriarch-github-agent
python -m matriarch_kb module filters
python -m matriarch_kb search "ping pong"

# Mix by genre
cd ..\genre-mixing-github-agent
python -m genre_mix_kb genre dance
```

### Wire up a GitHub / Copilot agent

1. Open the agent folder (or point the agent at this monorepo).
2. Set system / custom instructions to that folder’s **`AGENTS.md`**.
3. Prefer structured `*_kb` modules and `knowledge/*_extract.txt` over inventing specs.
4. Keep agents **separate** — do not merge knowledge bases into one giant prompt.

For monorepo routing rules, see root [`AGENTS.md`](AGENTS.md).

## Design principles

1. **One agent = one source of truth** (one manual, book, or guide).
2. **Ground answers in extracts** — cite sections/pages when helpful; never invent MIDI CC maps or hardware limits.
3. **CLI for humans and automation** — every `*_kb` package is runnable via `python -m <pkg>`.
4. **Copyright stays with owners** — packages re-encode operational knowledge for local/studio assistants; do not republish manufacturer manuals as original work.

## Maintainer scripts (optional)

| Script | Purpose |
|--------|---------|
| `scripts/verify_agents.py` | Run `info` (or equivalent) on every CLI agent |
| `_build_agents.py` | Scaffold / regenerate instrument agent packages |
| `_extract_*.py` | PDF → `manual_extract.txt` helpers |
| `_download_gdrive.py` | Fetch sources that live on Google Drive |

Paths in maintainer scripts resolve relative to this repo root.

## License

MIT for agent scaffolding, Python packages, and documentation structure.  
Source manuals, books, and PDFs remain © their respective owners.
