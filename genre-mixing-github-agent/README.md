# Genre Recording & Mixing GitHub Agent

Separate agent from the Pirate.com article:

**[Recording and Mixing Techniques for Different Music Genres](https://pirate.com/en/blog/recording-mixing-techniques-different-genres/)**  
Will Bradbury · October 31, 2024

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `genre_mix_kb/` | Genres, tools, recipes |
| `knowledge/article_extract.txt` | Full structured extract |

## CLI

```bash
cd genre-mixing-github-agent
python -m genre_mix_kb genres
python -m genre_mix_kb genre dance
python -m genre_mix_kb tool compression
python -m genre_mix_kb recipe dance_low_end
python -m genre_mix_kb search "parallel"
```

Covers rock/indie, pop/hip-hop/R&B, dance, jazz/folk/classical/experimental, EQ/comp/FX/pan, bottom-up vs top-down, notable gear.

Article © Pirate.com. Agent scaffolding for local study/production help.
