#!/usr/bin/env python3
"""Fail if any audio file is tracked (or staged) in this repo.

Music tracks and clips belong on the computer (CURSOR /workspace/music-clips,
GROMIT FleetDrop), never in git. Used by CI and the optional pre-commit hook.
"""
import subprocess
import sys

AUDIO_EXT = (".wav", ".flac", ".mp3", ".ogg", ".m4a", ".aac", ".aif", ".aiff", ".opus", ".wma")


def main() -> int:
    args = ["git", "ls-files"]
    if "--staged" in sys.argv:
        args = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
    files = subprocess.run(args, capture_output=True, text=True, check=True).stdout.splitlines()
    bad = [f for f in files if f.lower().endswith(AUDIO_EXT)]
    if bad:
        print("Audio files must not be committed to this repo:")
        for f in bad:
            print("  " + f)
        return 1
    print("OK: no audio files tracked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
