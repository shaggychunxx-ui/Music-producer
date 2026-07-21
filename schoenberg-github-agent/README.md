# Schoenberg Fundamentals — GitHub Agent

Structured transcription of **Arnold Schoenberg, *Fundamentals of Musical Composition*** (ed. Gerald Strang & Leonard Stein; Faber, 1967/1970) into a **GitHub / coding agent** knowledge package.

Source scan (no text layer):  
[monoskop.org — Schoenberg_Arnold_Fundamentals_of_Musical_Composition_no_OCR.pdf](https://monoskop.org/images/d/da/Schoenberg_Arnold_Fundamentals_of_Musical_Composition_no_OCR.pdf)

## What’s inside

| Path | Purpose |
|------|---------|
| [`AGENTS.md`](AGENTS.md) | System prompt for GitHub Agent / Copilot coding agent |
| [`schoenberg_kb/`](schoenberg_kb/) | Queryable Python knowledge (chapters, concepts, forms, exercises) |
| [`knowledge/manual_extract.txt`](knowledge/manual_extract.txt) | Full 125-page text extract |
| [`knowledge/Schoenberg_Fundamentals_of_Musical_Composition.pdf`](knowledge/) | Downloaded monoskop PDF |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Copilot pointer to AGENTS.md |

## Quick start

```bash
cd schoenberg-github-agent

python -m schoenberg_kb info
python -m schoenberg_kb list-chapters
python -m schoenberg_kb chapter motive
python -m schoenberg_kb define sentence
python -m schoenberg_kb form sonata
python -m schoenberg_kb exercise period
python -m schoenberg_kb search "liquidation"
python -m schoenberg_kb analyze-plan "Beethoven Op. 2 No. 1 opening"
```

### Python API

```python
from schoenberg_kb import define, get_chapter, get_form, get_exercise, search_kb

print(define("sentence")["summary"])
print(get_chapter(20)["key_points"])
print(get_form("small_ternary"))
print(get_exercise("period"))
print(search_kb("tonic form dominant form"))
```

## Doctrine hierarchy encoded

1. **Form** as organic organization (logic + coherence)  
2. **Phrase** → **Motive** + variation → **Connecting motive-forms**  
3. **Sentence** vs **Period** theme construction  
4. **Accompaniment**, character/mood, melody vs theme, self-criticism  
5. **Small forms**: ternary, irregular construction, minuet, scherzo, variations  
6. **Large forms**: transitions/coda, rondo types, **sonata-allegro** (incl. *Durchfuhrung*)

## Wire a GitHub agent

1. Push this folder to a GitHub repository.  
2. Set custom agent / repository instructions to **`AGENTS.md`**.  
3. Keep `schoenberg_kb` so the agent can look up definitions instead of guessing.  
4. Optional: `python -m schoenberg_kb export-json > knowledge/schoenberg.json`

## Copyright & use

- Book text © Estate of Gertrude Schoenberg / Faber publication rights.  
- This package **re-encodes pedagogical structure and concepts** for study agents and analysis tools.  
- Do **not** treat this as authorization to republish the full commercial book.  
- MIT applies to agent scaffolding/code only; the extract is for local reference.

## License (code)

MIT for `schoenberg_kb/`, `AGENTS.md` scaffolding, and tooling.
