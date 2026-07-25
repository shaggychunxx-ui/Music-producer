# Handoff: Music-producer (brain) → Studio-One (hands)

## Rule

| Repo | Role |
|------|------|
| **Music-producer** (this agent) | Production choices: brief, gates, recipes, MIDI intent, **plan jobs** |
| **Studio-One** (`s1-remote`) | Execution only: run `s1_jobs/current.json` via `tools/execute_job.py` |

Studio One must not decide pocket/lead approval or phase order.

## Song folder (shared disk, split ownership)

```
Song/
  GATES.txt          ← producer only
  NOTES.txt          ← producer only
  MIDI/              ← producer supplies files; S1 streams them
  s1_jobs/
    current.json     ← producer writes
    last_result.json ← Studio-One writes
    session.json     ← Studio-One writes at Template→Save As start
  _vision/           ← Studio-One eyes screenshots
```

## Song start (Studio-One hands — required)

Production **must** open the standing Template, then **Save As** a new song before any stream/record:

```bat
cd C:\Users\Box One\s1-remote
set PYTHONPATH=%CD%;%CD%\tools
py -3.12 tools\start_from_template.py --name SongName
:: S1_SONG_DIR now points at ...\Songs\SongName
```

Default template: `Documents\Studio One\Songs\Template\Template.song`  
Do **not** write production takes into the Template package.

## CLI (this package)

```bash
cd song-creation-pipeline-github-agent

python -m song_pipeline_kb init-song --song-dir PATH --name Song
python -m song_pipeline_kb next --song-dir PATH
python -m song_pipeline_kb gate brief locked --song-dir PATH
python -m song_pipeline_kb plan mvp --song-dir PATH
python -m song_pipeline_kb plan stream --song-dir PATH --part lead --track 3
python -m song_pipeline_kb status --song-dir PATH
python -m song_pipeline_kb observe --song-dir PATH   # vision+audio cues → decision
python -m song_pipeline_kb decide --song-dir PATH
python -m song_pipeline_kb cycle --song-dir PATH --execute --max-sec 8
python -m song_pipeline_kb gate pocket locked --song-dir PATH   # after user OK
```

## Execute (other repo)

```bash
cd path/to/Studio-One   # e.g. C:\Users\Box One\s1-remote
set PYTHONPATH=%CD%;%CD%\tools
:: Prefer: start_from_template first, then:
set S1_SONG_DIR=PATH
py -3.12 tools/execute_job.py
py -3.12 tools/execute_job.py --no-prompt --max-sec 8
```

## Cues (autonomy)

| Cue | Where | Used for |
|-----|-------|----------|
| Screenshots | `Song/_vision/arm_watch/` | Rec red, UI presence, clip hints |
| Loopback WAV | `Song/_vision/ears/` | has_signal / RMS / activity |
| `last_result.json` | `Song/s1_jobs/` | Structured evidence for `observe` |

**Policy:** metrics can recommend retry / user-listen; they **do not** lock pocket/lead.
Taste gates stay human (or explicit CLI). Programmer agents should open eyes PNGs
to verify, not trust `note_ons` alone.

## MVP flow

1. `init-song` + reference / `gate brief locked`
2. Create `MIDI/drums.mid` + `MIDI/bass.mid` (producer or composer tools)
3. `plan mvp` → writes job **or** `cycle --execute`
4. Studio-One `execute_job.py` (eyes + ears)
5. `observe` → confidence + recommendation
6. User listens → `gate pocket locked` only if approved
7. Later: `plan stream --part lead …` after pocket

See Studio-One `docs/EXECUTION_JOBS.md` for job ops.
