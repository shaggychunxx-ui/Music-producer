# Output MOVEMENT GitHub Agent

Separate agent package for **Output MOVEMENT** (rhythmic dual-engine FX plugin).

**Manual source (Google Drive):**  
https://drive.google.com/file/d/10rxiXHuJ9Oz89ByD5pEcgMr2Ax8E8y5z/view  

Local copy: `knowledge/Movement_User_Guide.pdf`

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt for GitHub / Copilot agent |
| `movement_kb/` | Queryable Python knowledge base |
| `knowledge/manual_extract.txt` | Full text extract |
| `.github/copilot-instructions.md` | Copilot pointer |

## CLI

```bash
cd movement-github-agent
python -m movement_kb info
python -m movement_kb topics
python -m movement_kb topic rhythms
python -m movement_kb recipe pump
python -m movement_kb search "Flux"
```

## Lives with

`Documents\github-agents\` alongside Matriarch, monologue, TR-8S, StudioLive, Schoenberg — **kept separate**.

Manual © Output. Agent scaffolding for local use only.
