# Tools

## Spotify PC capture

Same job as GitStatus on the phone: while **Spotify is playing on this PC** (desktop app **or** Chrome/Edge web player), grab an 8–25 s WASAPI loopback clip and append `source: spotify_pc` to `taste_data/listen_log.jsonl`.

```powershell
python tools\spotify_pc_capture.py status
python tools\spotify_pc_capture.py once
powershell -ExecutionPolicy Bypass -File tools\Install-SpotifyPcCapture.ps1
```

Scheduled task: `GitStatus-SpotifyPcCapture` (at logon). Log: `taste_data/pc_capture.log`.

Prefers Realtek / Speakers over HDMI. Override: `$env:SPOTIFY_PC_DEVICE = "Realtek"`.
