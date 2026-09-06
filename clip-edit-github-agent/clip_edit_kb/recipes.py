"""Producer recipes for clip-edit (music)."""

from __future__ import annotations

from typing import Any

RECIPES: dict[str, dict[str, Any]] = {
    "extract_48k": {
        "title": "Pull 48 kHz wav from a video",
        "steps": [
            "python -m clip_edit_kb extract-audio CLIP.mp4 -o clip.wav",
            "Confirm 48000 Hz PCM. GROMIT DAW is 48 kHz — do not leave 44.1.",
            "Studio One Artist: File drag the wav onto an Audio Track (or Browser).",
            "Use for sampling, scoring, or replacing the video's baked soundtrack.",
        ],
    },
    "visualizer_loop": {
        "title": "Silent ping-pong visualizer, then mux the song",
        "steps": [
            "python -m clip_edit_kb loop CLIP.mp4 --fade 0.18 -o vis-loop.mp4",
            "QC the reverse turn (frames in vis-loop-qc/).",
            "Optional: python -m clip_edit_kb rife vis-loop.mp4  (Comfy :8189, after the join)",
            "python -m clip_edit_kb mux vis-loop.mp4 MASTER.wav -o promo.mp4",
            "Do not reverse-concat. Do not loop the audio.",
        ],
    },
    "stitch_promo": {
        "title": "Join two shots then attach the master",
        "steps": [
            "Match fps first (prepare-s1 / constant fps) or the xfade flashes black.",
            "python -m clip_edit_kb stitch A.mp4 B.mp4 --skip-b 0.30 --fade 0.20",
            "Hard cut if poses already match: --fade 0.",
            "QC seam frames. Then mux the bounced master.",
        ],
    },
    "score_to_picture_artist": {
        "title": "Score to picture on Studio One 6 Artist (GROMIT)",
        "steps": [
            "Artist has no Video Track (Professional-only).",
            "python -m clip_edit_kb prepare-s1 CLIP.mp4 --song-dir SONG_DIR",
            "Import the sidecar *.48k.wav as an Audio Track. Mute it if you only need the picture elsewhere.",
            "Compose against that wav. Bounce the song, then mux onto the prepared mp4.",
            "NLE cuts: OpenShot (no watermark). Loops: this agent, not OpenShot reverse.",
        ],
    },
    "score_to_picture_pro": {
        "title": "Score to picture on Studio One Professional",
        "steps": [
            "prepare-s1 then drag the mp4 onto the Video Track (ch.20).",
            "Audio Sub-track stays locked to the video. Drag it down to Arrange if you need independent edit.",
            "Song frame rate: Use Video Frame Rate in Timeline.",
            "Video mute is on by default in the Video Player — click to hear the clip audio.",
        ],
    },
    "rife_60": {
        "title": "60 fps after the join",
        "steps": [
            "Finish loop or stitch first.",
            "python -m clip_edit_kb rife CLIP.mp4",
            "Needs Comfy Desktop :8189 + rife49.pth. Skip if the reverse smears.",
            "Grain only after RIFE: python -m clip_edit_kb grain CLIP-60fps.mp4 --strength 8",
        ],
    },
    "openshot_cut": {
        "title": "Watermark-free NLE cut",
        "steps": [
            "Open C:\\Program Files\\OpenShot Video Editor\\openshot-qt.exe",
            "Trim / 9:16 crop / titles. Export mp4.",
            "Do not reverse+concat a loop in OpenShot (freezes the peak frame).",
            "Then loop / mux here if needed.",
        ],
    },
    "remux_clean": {
        "title": "Strip metadata before posting a promo",
        "steps": [
            "python -m clip_edit_kb remux promo.mp4",
            "Copy remux + map_metadata -1 + faststart. Drops C2PA-style boxes.",
            "Do not git the mp4.",
        ],
    },
}


def get_recipe(name: str) -> dict[str, Any] | None:
    key = name.strip().lower().replace("-", "_")
    return RECIPES.get(key)
