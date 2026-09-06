"""Catalog of Mira-Soline tools kept for music production."""

from __future__ import annotations

from typing import Any

SOURCE = {
    "title": "Clip-edit for music",
    "origin": "Mira-Soline scripts/Edit-Video.py + VIDEO-EDIT.md (generic subset)",
    "ported": "2026-09-06",
    "daw_host": "GROMIT",
    "sample_rate": 48000,
    "studio_one_edition": "Artist 6.6.4 (no Video Track; Pro-only)",
    "openshot": r"C:\Program Files\OpenShot Video Editor\openshot-qt.exe",
}

# What came from Mira, and where it lives now.
TOOLS: dict[str, dict[str, Any]] = {
    "loop": {
        "mira": "scripts/Edit-Video.py loop --fade 0.18",
        "here": "clip_edit_kb loop",
        "use": "Ping-pong visualizer. Xfade at reverse. Video-only; mux song after.",
        "repo": "Music-producer",
    },
    "stitch": {
        "mira": "scripts/Edit-Video.py stitch / Stitch-Clips.py",
        "here": "clip_edit_kb stitch",
        "use": "Join two shots: skip ~0.3s of B, short xfade. Constant fps first.",
        "repo": "Music-producer",
    },
    "rife": {
        "mira": "scripts/Edit-Video.py rife / To-60fps.py",
        "here": "clip_edit_kb rife",
        "use": "Comfy :8189 RIFE 4x to 60fps after the join. Not ffmpeg minterpolate.",
        "repo": "Music-producer",
    },
    "grain": {
        "mira": "scripts/Edit-Video.py grain",
        "here": "clip_edit_kb grain",
        "use": "Fine grain after RIFE. Never before interpolate.",
        "repo": "Music-producer",
    },
    "qc": {
        "mira": "scripts/Edit-Video.py qc",
        "here": "clip_edit_kb qc",
        "use": "Dump frames at 0/25/50/75/end. Check reverse turn and stitch seam.",
        "repo": "Music-producer",
    },
    "extract-audio": {
        "mira": "ffmpeg via Edit-Video (Mira strips -an; we invert that)",
        "here": "clip_edit_kb extract-audio",
        "use": "48 kHz PCM wav from a video for sampling or S1 Audio Track.",
        "repo": "Music-producer",
    },
    "mux": {
        "mira": "none (Mira ships silent). New for music.",
        "here": "clip_edit_kb mux",
        "use": "Attach bounced master to a silent visualizer. AAC 320k, +faststart.",
        "repo": "Music-producer",
    },
    "prepare-s1": {
        "mira": "none. New for DAW import.",
        "here": "clip_edit_kb prepare-s1 AND Studio-One tools/prepare_video_for_s1.py",
        "use": "Constant-fps mp4 + 48 kHz wav sidecar. Artist: import wav. Pro: Video Track.",
        "repo": "both",
    },
    "remux": {
        "mira": "Post-ToX.drop_c2pa",
        "here": "clip_edit_kb remux",
        "use": "Copy remux, strip metadata, +faststart. Drops C2PA-style boxes.",
        "repo": "Music-producer",
    },
    "openshot": {
        "mira": "docs/OPENSHOT.md",
        "here": "knowledge + OpenShot 3.5.1 on GROMIT",
        "use": "Watermark-free NLE cuts / 9:16 crop. Do not reverse-concat loops.",
        "repo": "Music-producer",
    },
}

SKIPPED = [
    "Pick-Body.py / Pick-Look.py / Pick-VaultRef.py (Mira identity)",
    "Venice-Chat.py / Venice-Video.py (adult captions / I2V compare)",
    "Vast Wan 14B / Generate-I2VFromPass.py / Generate-KeyframeChain.py",
    "Install-HfToolkit.py NSFW LoRAs / UMT5",
    "Manage-Library.py (Mira library paths)",
    "Draft-XPost.py / Track-Reach.py / Post-ToFanvue.py (Mira social)",
]


def list_tools() -> list[str]:
    return sorted(TOOLS)


def get_tool(name: str) -> dict[str, Any] | None:
    key = name.strip().lower().replace("_", "-")
    return TOOLS.get(key)
