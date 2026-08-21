# Signals Music Studio GitHub Agent

Study agent for **Jake Lizzio / Signals Music Studio** — music theory, modes, chords, songwriting, and song analysis.

**Videos:** https://www.youtube.com/@SignalsMusicStudio/videos  
**Lesson recaps:** https://signalsmusic.studio/lessons

Catalogues 87 free site lessons + the 7 official series, then restates **operational techniques** (loops, mixture, mode writing, rhythm grids) for the Music-producer workflow.

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `signals_kb/` | Lessons, modes, techniques, study recipes |
| `knowledge/catalog.json` | Slugs, series, YouTube ids |
| `knowledge/lesson_extract.txt` | Operational extracts from public lesson pages |
| `knowledge/SOURCE.txt` | Attribution + copyright |

## CLI

```bash
cd signals-music-studio-github-agent
python -m signals_kb info
python -m signals_kb series
python -m signals_kb study harmony_writer
python -m signals_kb mode mixolydian
python -m signals_kb recipe tresillo_steal
python -m signals_kb search "andalusian"
python -m signals_kb watch seven-ways-to-use-modes
```

## Study paths

| Path | Use when |
|------|----------|
| `harmony_writer` | First progressions → 7ths → V/x → borrowed |
| `modal_writer` | Parallel modes → write in each → 7 uses |
| `rhythm_producer` | 6/8–12/8 gym → tresillo → odd meter |
| `analysis_lab` | Steal moves from Imagine / Something / Champions / Orion |

After each video: write **one 8-bar idea** (`recipe daily_key`). Do not start a full original song here — still follow the song pipeline (GitStatus Spotify refs via `taste pick`).

## Copyright

Videos, charts, and lesson text © Jake Lizzio / Signals Music Studio.  
Agent scaffolding is MIT. Do not republish transcripts or paid Codex/course material.
