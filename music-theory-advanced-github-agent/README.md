# Advanced Music Theory GitHub Agent

Separate agent for **Music Theory – Advanced Level** (June 2005; Eowyn / mysongbook.com compilation).

**Source:** http://beverlyteacher.com/Music%20Theory%20-%20Advanced.pdf

Focus: **modes**, modal improv/composition, modulation.

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `theory_kb/` | Modes, concepts, topics, recipes |
| `knowledge/Music_Theory_Advanced.pdf` | Local PDF |
| `knowledge/manual_extract.txt` | Full text (33 pages) |

## CLI

```bash
cd music-theory-advanced-github-agent
python -m theory_kb info
python -m theory_kb modes
python -m theory_kb mode dorian
python -m theory_kb define characteristic_modal_note
python -m theory_kb recipe vamp
python -m theory_kb search "Scarborough"
```

## Copyright (from the PDF)

Private educational use free; **selling prohibited**.

Lives under `Documents\github-agents\` with your other agents (kept separate).
