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

## Phone (GitStatus) auto-clips

**GitStatus** (Oxygen-OS `status-app`) can capture **random 5–50 s** internal-audio clips **only while Spotify is playing** on the phone (no PC).

| Path | Role |
|------|------|
| `clips/YYYY/MM/clip_*.wav` | Mono 16 kHz WAV clips uploaded by the phone |
| `listen_log.jsonl` | Each clip appends a listen line (`source: spotify_phone`) |

After new phone listens land, rebuild the profile:

```bash
python -m song_pipeline_kb taste rebuild
python -m song_pipeline_kb taste apply-brief --song-dir PATH --lock --force
```

If captures are silent, GitStatus **skips** them (no log, no upload). OEM unlock / alternate capture may be needed later.
