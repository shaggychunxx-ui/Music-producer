# Music Producer’s Complete Genre Guide — GitHub Agent

Separate agent from your desktop handbook:

`C:\Users\Box One\Desktop\Music_Producers_Genre_Guide.pdf`

**The Music Producer’s Complete Genre Guide** — production blueprints, mix notes, arrangement maps across 30+ genres.

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `producers_kb/` | Foundations + all genre blueprints |
| `knowledge/Music_Producers_Genre_Guide.pdf` | Local copy |
| `knowledge/manual_extract.txt` | Full text (49 pages) |

## CLI

```bash
cd producers-genre-guide-github-agent
python -m producers_kb genres
python -m producers_kb genre trap
python -m producers_kb foundation mix_master
python -m producers_kb recipe start_track
python -m producers_kb search "sidechain"
```

Lives under `Documents\github-agents\` with your other agents (kept separate). Complements `genre-mixing-github-agent` (Pirate.com article) with deeper per-genre blueprints.
