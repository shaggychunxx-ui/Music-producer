# Studio One 6.6 — Agent Knowledge Pack

Structured extract of the **PreSonus Studio One 6.6 Reference Manual (EN)** for use with GitHub Copilot coding agents, custom agents, and other LLM tools that ingest Markdown.

## Contents

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Agent role, edition rules, retrieval instructions (copy this into agent config) |
| `FUNCTIONS.md` | Quick function map: record MIDI, arm, transport, views, devices |
| `AGENT_OPS_LEARNED.md` | Live session ops: S1 Notes port, arm failures, agent vs user |
| `ARM_RECORD_LESSONS.md` | Deep arm/record failures + eyes policy |
| `S1_UI_PIPELINE.md` | **Preferred** S1-first UI control split |
| `MANUAL_WALKTHROUGH_CATALOG.md` | Phase catalog from full manual walk (KB/MIDI/user) |
| `FULL_MANUAL_WALK_REPORT.md` | Ch.1–22 walk results |
| `MANUAL_MISSED_REPORT.md` | Follow-up missed-ops results |
| `MANUAL_WALK_SUMMARY.md` | Short summary of light walk |
| `INDEX.md` | Human/agent table of contents with links to chapters |
| `manifest.json` | Machine-readable section map (slug, pages, topics, paths) |
| `chapters/*.md` | Full manual text split by major section |
| `ALL_IN_ONE.md` | Optional single-file concatenation for bulk paste into an agent context |

## Quick start for GitHub agents

1. Copy this folder into your repo (e.g. `knowledge/studio-one-6.6/`).
2. Point agent instructions at `AGENTS.md`.
3. Instruct the agent to open only relevant `chapters/*.md` files via `INDEX.md`.

### Minimal agent instruction snippet

```markdown
## Studio One 6.6
When the user asks about Studio One, read knowledge/studio-one-6.6/AGENTS.md
and retrieve from knowledge/studio-one-6.6/chapters/ using INDEX.md or manifest.json.
Ground answers in the manual text. Note Prime vs Artist vs Professional limits.
```

## Regenerating

If you update the PDF:

```bash
python _convert_manual.py
```

Requires: `pymupdf` and the PDF at the path set in the script.

## Notes

- Text is extracted programmatically; complex diagrams/screenshots are not included as images.
- Some layout-only artifacts (column breaks, soft hyphens) may remain.
- Official manual PDF remains the canonical visual reference.
