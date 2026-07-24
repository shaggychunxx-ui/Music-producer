# Song Creation Pipeline GitHub Agent

Gated **original song** creation process: reference-first MVP, one part at a time, signal-flow mix, optional late form, final lock.

Song-agnostic standing rules (no track roster). Compatible with local studio scaffolds under a DAW songs folder.

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `song_pipeline_kb/` | Phases, gates, recipes, phrase book |
| `knowledge/workflow_extract.txt` | Structured process extract |

## CLI

```bash
cd song-creation-pipeline-github-agent
python -m song_pipeline_kb info
python -m song_pipeline_kb phases
python -m song_pipeline_kb phase mvp
python -m song_pipeline_kb gates
python -m song_pipeline_kb recipe list
python -m song_pipeline_kb recipe duck_mild_short
python -m song_pipeline_kb phrase "parts structured better"
python -m song_pipeline_kb scaffold
python -m song_pipeline_kb search "sidechain"
```

## When to use

- Starting or continuing an **original** song under approval gates
- Interpreting producer feedback (“pumps”, “less airy”, “organize parts”)
- Late arrangement on **locked** stems (length, start on hook, ±BPM)
- Not for: manufacturer manuals, pure theory drills, or genre encyclopedia alone (use sibling agents)

## Design

1. **One agent = one process** (pipeline + recipes).
2. Ground answers in `song_pipeline_kb` + extract.
3. Prefer simplify / one-focus fixes over full rewrites.
