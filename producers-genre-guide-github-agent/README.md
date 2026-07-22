# Music Producer’s Complete Genre Guide — GitHub Agent

Structured agent for **The Music Producer’s Complete Genre Guide** — production blueprints, mix notes, and arrangement maps across 30+ genres.

Source PDF (bundled): `knowledge/Music_Producers_Genre_Guide.pdf`

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

Part of the [Music-producer](https://github.com/shaggychunxx-ui/Music-producer) monorepo. Complements `genre-mixing-github-agent` (Pirate.com mixing article) with deeper per-genre production blueprints.
