# Taste memory (persistent)

This folder holds the producer’s **listen log** and **taste profile**.

| File | Role |
|------|------|
| `listen_log.jsonl` | Append-only listens (metadata + ratings + numeric fingerprints) |
| `taste_profile.json` | Rolling aggregate used by `taste apply-brief` |

## Rules

- **No audio files here.** Captures stay local (optional `audio_path` on a listen entry only).
- Fingerprints are **numbers only** (peak/RMS/crest/bands/tempo) — not the track.
- Ratings drive taste: `love` weights strong, `ok` mild, `no` becomes anti-goals.
- Safe to commit JSON/JSONL to git so dual-PC + phone share preference memory.

## CLI

```bash
cd song-creation-pipeline-github-agent

# Log a ref you care about
python -m song_pipeline_kb taste listen \
  --artist "Artist" --title "Track" \
  --rating love --genre dark_pulse \
  --tags "dark,dry kick,round bass" \
  --bpm 92 --peak-db -2 --rms-db -12 --crest-db 10

# Inspect
python -m song_pipeline_kb taste status
python -m song_pipeline_kb taste profile
python -m song_pipeline_kb taste log --limit 20

# Rate later
python -m song_pipeline_kb taste rate <listen-id> love

# Apply to a song brief
python -m song_pipeline_kb taste apply-brief --song-dir PATH --lock --force
```

Created automatically on first `taste listen` or `taste rebuild`.

## Phone (GitStatus) = the reference-track source

**Standing rule:** each new original song gets **10 random Spotify clips** (`python -m song_pipeline_kb taste pick`). Do not ask the user for a title. If fewer than 10 exist, use all of them.

**GitStatus** (phone) and **this PC** both capture short clips **only while Spotify is playing**.

| Path | Role |
|------|------|
| `clips/YYYY/MM/clip_*.wav` | Mono 16 kHz WAV clips |
| `listen_log.jsonl` | Each clip appends a listen (`spotify_phone` or `spotify_pc`) |

PC capture (WASAPI loopback, 8–25 s):

```powershell
cd song-creation-pipeline-github-agent
python tools\spotify_pc_capture.py status
powershell -ExecutionPolicy Bypass -File tools\Install-SpotifyPcCapture.ps1
```

```bash
python -m song_pipeline_kb taste refs
python -m song_pipeline_kb taste pick
python -m song_pipeline_kb taste rebuild
python -m song_pipeline_kb taste apply-brief --song-dir PATH --lock --force
```

If captures are silent, GitStatus **skips** them (no log, no upload). OEM unlock / MediaProjection consent may be needed. If the log is empty, wait for a phone capture — do not invent a reference.
