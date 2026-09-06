# Clip-edit (music)

Generic **loop / stitch / RIFE / extract-audio / mux** tools ported from [Mira-Soline](https://github.com/shaggychunxx-ui/Mira-Soline) `scripts/Edit-Video.py` for **music production**.

Not the Mira character pipeline. Identity, Venice, Vast I2V, and adult QC stay in Mira-Soline.

## Why it lives here

Music-producer is the **brain**: recipes, 48 kHz extract, visualizer loop, mux bounced master onto picture.

Studio-One is the **hands**: `tools/prepare_video_for_s1.py` drops the wav/mp4 into a Song. GROMIT is Studio One **6 Artist** — Video Track is Professional-only — so the wav imports as an Audio Track.

## CLI

```powershell
cd clip-edit-github-agent
python -m clip_edit_kb info
python -m clip_edit_kb recipe extract_48k
python -m clip_edit_kb extract-audio CLIP.mp4 -o clip.wav
python -m clip_edit_kb loop CLIP.mp4 --fade 0.18
python -m clip_edit_kb mux vis-loop.mp4 MASTER.wav -o promo.mp4
python -m clip_edit_kb prepare-s1 CLIP.mp4 --song-dir SONG_DIR
```

Requires `ffmpeg` (or `pip install imageio-ffmpeg`). RIFE needs Comfy Desktop `:8189`.

OpenShot (watermark-free NLE on GROMIT): `C:\Program Files\OpenShot Video Editor\openshot-qt.exe`

## Source

See `knowledge/SOURCE.txt`. Loop/stitch keep Mira's video-only (`-an`) behavior so reverse does not rewind a soundtrack.
