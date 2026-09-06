# Handoff: Music-producer (brain) → Studio-One (hands)

## Rule

| Repo | Role |
|------|------|
| **Music-producer** (this agent) | Production choices: brief, gates, **compose MIDI**, recipes, **plan jobs** |
| **Studio-One** | Execution only: Template→Save As, stream/import, mix MCU, export intent |

Studio One must not decide pocket/lead approval unless producer runs **unattended** policy.

Video/visualizer: Music-producer `clip-edit-github-agent` (`clip_edit_kb`). Studio-One executes `tools/prepare_video_for_s1.py` (48 kHz wav). GROMIT is Artist — no Video Track.

## Paths

Prefer GitHub Desktop clone (synced with live tools):

```
%USERPROFILE%\Documents\GitHub\Studio-One
```

Fallback / legacy:

```
%USERPROFILE%\s1-remote
```

Set `S1_REMOTE` to override. `song_pipeline_kb` auto-discovers either tree.

## Song folder (shared disk, split ownership)

```
Song/
  GATES.txt          ← producer only
  NOTES.txt          ← producer only
  MIDI/              ← producer compose writes; S1 streams
  tracks.json        ← Template roles (S1 hands)
  s1_jobs/
    current.json     ← producer writes
    last_result.json ← Studio-One writes
    autonomy_result.json
  _vision/           ← eyes + ears
  Masters/           ← export target
```

## Zero-human path

```bat
:: Brain
cd %USERPROFILE%\Documents\GitHub\Music-producer\song-creation-pipeline-github-agent
python -m song_pipeline_kb init-song --song-dir PATH --name MySong
python -m song_pipeline_kb compose --song-dir PATH --genre dark_pulse
python -m song_pipeline_kb gate brief locked --song-dir PATH
python -m song_pipeline_kb run-unattended --song-dir PATH --genre dark_pulse --max-sec 40 --prefer-import

:: Or hands-only orchestrator
cd %USERPROFILE%\Documents\GitHub\Studio-One
set PYTHONPATH=%CD%;%CD%\tools
py -3.12 tools\autonomous_run.py --name MySong --parts drums,bass,lead --max-sec 40
```

## CLI (brain package)

```bash
python -m song_pipeline_kb compose --song-dir PATH --genre trap
python -m song_pipeline_kb plan mvp --song-dir PATH
python -m song_pipeline_kb plan mix --song-dir PATH
python -m song_pipeline_kb cycle --song-dir PATH --compose --execute --unattended --max-sec 40
python -m song_pipeline_kb observe --song-dir PATH
python -m song_pipeline_kb decide --song-dir PATH --unattended
python -m song_pipeline_kb qc --song-dir PATH
```

## Execute (hands)

```bat
cd path\to\Studio-One
set PYTHONPATH=%CD%;%CD%\tools
py -3.12 tools\setup_check.py
py -3.12 tools\start_from_template.py --name SongName
py -3.12 tools\execute_job.py --no-prompt --max-sec 40
py -3.12 tools\produce.py --resume --song-dir PATH --parts drums,bass
py -3.12 tools\overnight_queue.py --names A,B --max-sec 30
```

## Policies

| Policy | Behavior |
|--------|----------|
| **taste** (default) | Metrics recommend only; human locks pocket/lead |
| **unattended** | Metric/QC auto-locks capture gates (not a taste claim) |

## Cues

| Cue | Where |
|-----|-------|
| Screenshots | `Song/_vision/arm_watch/` |
| Loopback WAV | `Song/_vision/ears/` |
| `last_result.json` | `Song/s1_jobs/` |

See Studio-One `docs/AUTONOMY.md`, `docs/TEMPLATE_CONTRACT.md`, `docs/EXECUTION_JOBS.md`.
