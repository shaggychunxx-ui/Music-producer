# Humanizing Programmed Music GitHub Agent

Agent based on the deep-dive knowledge-base article:

**Advanced Techniques for Humanizing Programmed Music**

Covers five core pillars for making MIDI/programmed music feel human:
micro-timing deviations, micro-dynamic (velocity) shaping, tonal/expression
modulation, arrangement imperfections, and spatial realism.

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `humanize_kb/` | Categories, techniques, recipes, search |
| `knowledge/article_extract.txt` | Full structured extract |

## CLI

```bash
cd humanizing-programmed-music-github-agent
python -m humanize_kb info
python -m humanize_kb categories
python -m humanize_kb category micro_timing
python -m humanize_kb techniques
python -m humanize_kb technique pocketing
python -m humanize_kb recipe hiphop_drums
python -m humanize_kb search "ghost notes"
```

Covers pocketing (rush/drag), chord flamming/strumming, groove extraction,
velocity accents and hierarchies, physiological velocity modeling, ghost
notes, velocity-to-filter mapping, round robin/sample start offset, CC
automation, avoiding the loop trap, tempo tracking, acoustic bleed, and
analog pitch drift.

Agent scaffolding for local study/production help.
