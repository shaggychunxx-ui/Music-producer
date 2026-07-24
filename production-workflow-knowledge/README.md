# Production workflow knowledge (standalone)

Song-agnostic standing rules for original music production.

## Source of truth

| File | Role |
|------|------|
| **`PRODUCTION_WORKFLOW.md`** | Full standing process: MVP gates, temperature, signal flow, duck, voice match, parts ≠ form, late arrange, final lock |

This pack is **not** a list of past songs. Per-song status lives only in each song’s `NOTES.txt` / `GATES.txt` under the local DAW songs folder.

## Related

| Pack / repo | Role |
|-------------|------|
| `../song-creation-pipeline-github-agent/` | Searchable agent + short extract + recipes |
| `../studio-one-6.6-agent-knowledge/` | Studio One 6.6 manual + UI ops |
| **Studio-One** (`s1-remote`) `docs/S1_UI_PIPELINE.md` | **Preferred** real-time S1 UI control split |

## Agent use

1. Read `PRODUCTION_WORKFLOW.md` for process order and gates.
2. Use song-creation-pipeline recipes for duck/temp shortcuts.
3. Prefer S1-first UI pipeline when a Song is open (see Studio-One docs).

## Local studio scaffolds

Templates and helpers used with this workflow often live under a DAW songs `_studio_lib` (GATES/NOTES templates, `signal_flow`, `solo_ab_voices`). They are optional; the **rules** here stand alone.
