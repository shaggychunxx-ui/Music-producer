# GitHub Agent Instructions — Studio One 6.6

Copy this block into your repo’s agent entry file, e.g.:

- `AGENTS.md` (root)
- `.github/copilot-instructions.md`
- `.github/agents/<name>.md` (GitHub Copilot custom agent)

Adjust the path if you place the knowledge pack somewhere other than `knowledge/studio-one-6.6/`.

---

## Studio One 6.6 product knowledge

When the user asks about **PreSonus Studio One** (recording, mixing, editing, Show page, Project/mastering, Atmos, plug-ins, instruments, key commands, etc.):

1. Treat `knowledge/studio-one-6.6/` as the **source of truth** for Studio One 6.6 behavior.
2. Read `knowledge/studio-one-6.6/AGENTS.md` first.
3. Use `knowledge/studio-one-6.6/INDEX.md` or `manifest.json` to pick chapter file(s).
4. Open **only** the relevant `knowledge/studio-one-6.6/chapters/*.md` files (usually 1–3).
5. Answer with procedures, UI labels, and edition limits (Prime / Artist / Professional) grounded in those files.
6. If the manual pack does not cover something, say so; do not invent menu paths or parameters.

### Quick topic → chapter map

| User topic | Chapter file |
|------------|--------------|
| Install, activate, content download | `chapters/02-installation-activation.md` |
| Audio/MIDI setup, options, new song | `chapters/03-setup.md` |
| Undo, transport, key commands, Control Link intro | `chapters/04-fundamentals.md` |
| Start / Song / Show / Project pages | `chapters/05-pages.md` |
| Recording, metronome, cue mix, loop/step record | `chapters/06-recording.md` |
| Editing, comping, Melodyne, macros, patterns | `chapters/07-editing.md` |
| Score / notation / tablature | `chapters/08-score-editor.md` |
| Browser, loops, pool, cloud | `chapters/09-browser.md` |
| Arranger, Chord/Tempo tracks, scratch pad | `chapters/10-arranging.md` |
| Console, routing, VCA, mixdown, stems | `chapters/11-mixing.md` |
| Dolby Atmos / surround / spatial | `chapters/12-spatial-audio.md` |
| Live Show page, setlist, patches | `chapters/13-show-page.md` |
| Automation envelopes/modes | `chapters/14-automation.md` |
| Hardware controllers, Mackie Control | `chapters/15-control-link.md` |
| Mastering / Project page | `chapters/16-mastering.md` |
| Built-in FX (EQ, dynamics, reverb, Pipeline…) | `chapters/17-built-in-effects.md` |
| Sample One, Presence, Impact, MaiTai, Mojito | `chapters/18-virtual-instruments.md` |
| Collaboration / Studio One+ | `chapters/19-collaboration.md` |
| Video track / sync / export | `chapters/20-video.md` |
| Import/export, AAF, zip songs | `chapters/21-saving-import-export.md` |

For a single bulk paste (if multi-file retrieval is unavailable), use `ALL_IN_ONE.md` (~1.3 MB / ~335k tokens — too large for one context window; prefer chapters).
