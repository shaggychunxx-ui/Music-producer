#!/usr/bin/env python3
"""Convert Studio One 6.6 Reference Manual PDF into agent-ready Markdown knowledge pack."""

from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

PDF_PATH = Path(r"C:\Users\rrodrigues\Studio_One_6.6_Reference_Manual_EN.pdf")
OUT_DIR = Path(r"C:\Users\rrodrigues\studio-one-6.6-agent-knowledge")
CHAPTERS_DIR = OUT_DIR / "chapters"

# Document page numbers from TOC -> section metadata
# PDF page index = document_page + 5  (doc p1 is PDF page 7 / index 6)
# Cover + TOC occupy PDF pages 1-6 (indices 0-5)

SECTIONS = [
    # (doc_start, doc_end_inclusive, slug, title, agent_topics)
    (1, 2, "01-introduction", "Introduction", [
        "editions", "Prime", "Artist", "Professional", "overview",
    ]),
    (3, 11, "02-installation-activation", "Installation and Activation", [
        "install", "activate", "license", "content installation", "my.presonus",
    ]),
    (12, 42, "03-setup", "Setup", [
        "system requirements", "audio device", "MIDI", "I/O setup", "content management",
        "new song", "Notion", "colors", "customization", "recovery", "options",
    ]),
    (43, 62, "04-fundamentals", "Fundamentals", [
        "undo", "retrospective recording", "mix engine", "delay compensation",
        "dropout protection", "transport", "key commands", "smart templates",
        "Control Link", "performance monitor", "note repeat", "video player",
    ]),
    (63, 70, "05-pages", "Pages", [
        "Start page", "Song page", "Show page", "Project page", "Quick Switch",
        "Smart Templates",
    ]),
    (71, 91, "06-recording", "Recording", [
        "audio tracks", "instrument tracks", "metronome", "loop recording",
        "step record", "track layers", "cue mix", "low-latency monitoring",
        "print effects", "monitor mix",
    ]),
    (92, 191, "07-editing", "Editing", [
        "events", "mouse tools", "clip gain", "grid", "comping", "timestretch",
        "transient detection", "track transform", "inspector", "presets",
        "Sound Variations", "patterns", "Melodyne", "macros", "edit view",
    ]),
    (192, 210, "08-score-editor", "The Score Editor", [
        "score", "notation", "staff", "drum notation", "tablature", "lyrics", "Notion",
    ]),
    (211, 231, "09-browser", "The Browser", [
        "browser", "search", "instruments", "effects", "loops", "files", "cloud",
        "shop", "pool",
    ]),
    (232, 267, "10-arranging", "Arranging", [
        "arranger track", "chord track", "signature track", "tempo track",
        "lyrics track", "scratch pad", "bounce", "folder tracks", "track list",
    ]),
    (268, 320, "11-mixing", "Mixing", [
        "console", "routing", "fader flip", "channel editor", "groups", "scenes",
        "VCA", "listen bus", "metering", "marker track", "mixdown", "export stems",
    ]),
    (321, 338, "12-spatial-audio", "Spatial Audio", [
        "Dolby Atmos", "spatial audio", "renderer", "immersive", "ADM",
    ]),
    (339, 369, "13-show-page", "The Show Page", [
        "live performance", "setlist", "players", "patches", "performance view",
        "show timeline",
    ]),
    (370, 378, "14-automation", "Automation", [
        "automation envelopes", "automation modes", "instrument part automation",
    ]),
    (379, 388, "15-control-link", "Control Link", [
        "Control Link", "MIDI controllers", "mapping", "Mackie Control", "hardware",
    ]),
    (389, 409, "16-mastering", "Mastering (Project Page)", [
        "Project page", "mastering", "track sequencing", "master device rack",
        "publishing", "song integration",
    ]),
    (410, 477, "17-built-in-effects", "Built-In Effects", [
        "plugins", "effects", "Pro EQ 3", "dynamics", "reverb", "delay",
        "distortion", "modulation", "Pipeline XT", "Mix Engine FX",
    ]),
    (478, 532, "18-virtual-instruments", "Built-In Virtual Instruments", [
        "Sample One XT", "Presence XT", "Impact XT", "MaiTai", "Mojito",
        "Multi Instruments", "Note FX",
    ]),
    (533, 546, "19-collaboration", "Collaboration", [
        "Studio One+", "collaboration", "workspaces", "sharing documents",
    ]),
    (547, 553, "20-video", "Video Playback and Sync", [
        "video player", "video track", "sync", "export video",
    ]),
    (554, 559, "21-saving-import-export", "Saving, Import and Export", [
        "import song data", "export audio", "export MIDI", "AAF", "zip",
        "import other DAWs",
    ]),
    (560, 564, "22-index", "Index", [
        "index", "lookup",
    ]),
]


def doc_to_pdf_index(doc_page: int) -> int:
    """Convert 1-based document page number to 0-based PDF page index."""
    return doc_page + 5


def clean_page_text(text: str, doc_page: int | None = None) -> str:
    """Normalize page text and strip running headers/footers."""
    if not text:
        return ""

    # Normalize line endings / non-breaking spaces
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ")
    text = text.replace("\u200b", "")

    lines = text.split("\n")
    cleaned: list[str] = []
    # Footer patterns like "Recording 71" or "Table of Contents"
    footer_re = re.compile(
        r"^(Table of Contents|"
        r"Introduction|"
        r"Installation and Activation|"
        r"Activation|"
        r"Content Installation|"
        r"Setup|"
        r"Fundamentals|"
        r"Pages|"
        r"Recording|"
        r"Editing|"
        r"The Score Editor|"
        r"The Browser|"
        r"Arranging|"
        r"Mixing|"
        r"Spatial Audio|"
        r"The Show Page|"
        r"Automation|"
        r"Control Link|"
        r"Mastering|"
        r"Built-In Effects|"
        r"Built-in Virtual Instruments|"
        r"Collaboration|"
        r"Video Playback and Sync|"
        r"Saving, Import and Export|"
        r"Index|"
        r"Set Up Your Audio Device|"
        r"Audio Tracks|"
        r"Retrospective Recording"
        r")\s+\d+\s*$",
        re.IGNORECASE,
    )
    # Also generic "Section Name N" at end of page
    generic_footer = re.compile(r"^[A-Za-z][A-Za-z0-9 /&\+\-–—™®\(\)]{0,60}\s+\d{1,3}\s*$")

    for i, line in enumerate(lines):
        s = line.rstrip()
        if not s.strip():
            cleaned.append("")
            continue
        # Drop sole page-number lines
        if re.fullmatch(r"\d{1,3}", s.strip()):
            continue
        if footer_re.match(s.strip()):
            continue
        # Only treat as footer if it's near end of page (last 3 non-empty-ish lines)
        if i >= len(lines) - 4 and generic_footer.match(s.strip()) and re.search(r"\d{1,3}\s*$", s):
            # Keep lines that look like real headings without trailing page alone? already matched
            continue
        cleaned.append(s)

    text = "\n".join(cleaned)
    # Collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def promote_headings(text: str) -> str:
    """Heuristic: turn short Title Case / known section lines into markdown headings."""
    lines = text.split("\n")
    out: list[str] = []
    # Known major headings to force as H2/H3
    major = {
        "studio one editions",
        "studio one prime",
        "studio one artist",
        "studio one professional",
        "installation",
        "activation",
        "content installation",
        "system requirements",
        "set up your audio device",
        "audio device input/output setup",
        "set up your midi devices",
        "managing your content",
        "creating a new song",
        "working with presonus notion software",
        "custom colors",
        "customization",
        "recovery options",
        "general options",
        "additional options",
        "advanced options",
        "nondestructive editing and undo/redo",
        "retrospective recording",
        "documents",
        "high-precision mix engine",
        "automatic delay compensation",
        "audio dropout protection",
        "transport controls",
        "key commands",
        "smart templates",
        "control link",
        "performance monitor",
        "note repeat",
        "video player",
        "audio tracks",
        "instrument tracks",
        "activating recording",
        "metronome control",
        "loop recording on audio tracks",
        "instrument track recording modes",
        "step record",
        "track layers",
        "cue mixes and low-latency monitoring",
        "print effects while recording",
        "events",
        "arrange view mouse tools",
        "clips and clip gain envelopes",
        "the grid",
        "common editing actions",
        "comping",
        "transient detection and editing",
        "track transform",
        "sound variations",
        "patterns",
        "pitch correction with melodyne integration",
        "macro toolbar",
        "score editor overview",
        "searching for files in the browser",
        "the loops tab",
        "files tab",
        "cloud tab",
        "the pool",
        "arranger track",
        "chord track",
        "signature track",
        "tempo track",
        "lyrics track",
        "scratch pad",
        "folder tracks",
        "the console",
        "effects signal routing",
        "groups",
        "scenes",
        "vca channels",
        "the listen bus",
        "mixing down",
        "export stems from your song",
        "spatial audio formats",
        "the dolby atmos renderer",
        "a tour of the show page",
        "the setlist",
        "players and patches",
        "performance view",
        "what is automation?",
        "automation types",
        "automation modes",
        "what is control link?",
        "mackie control support",
        "creating a new project",
        "publishing your project",
        "effect micro views",
        "pro eq 3",
        "pipeline xt",
        "sample one xt",
        "presence xt",
        "impact xt",
        "maitai",
        "mojito",
        "multi instruments",
        "note fx",
        "video track",
        "import video",
        "exporting video files",
        "import song data",
        "exporting audio and midi files",
        "aaf import and export",
        "export to zip",
    }

    for line in lines:
        stripped = line.strip()
        key = re.sub(r"\s+", " ", stripped).lower()
        # bullet marker normalization
        if stripped in ("l", "•", "●", "○"):
            out.append("-")
            continue
        if stripped.startswith("l ") and len(stripped) > 2:
            # PreSonus PDF often uses "l" as bullet
            out.append("- " + stripped[2:])
            continue
        if key in major and len(stripped) < 80:
            out.append("")
            out.append(f"## {stripped}")
            out.append("")
            continue
        # Short ALL CAPS or Title-ish lines alone as H3
        if (
            stripped
            and len(stripped) <= 70
            and not stripped.endswith(".")
            and not stripped.endswith(",")
            and not stripped.startswith("-")
            and not re.match(r"^\d", stripped)
            and stripped[0].isupper()
            and " " in stripped
            and len(stripped.split()) <= 8
            and not any(c in stripped for c in ":;/")
            and stripped == stripped  # keep
        ):
            # Only promote if next line exists and looks like body (heuristic done later)
            pass
        out.append(line)

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Fix standalone bullet "l" lines already handled; also "l\ntext"
    text = re.sub(r"(?m)^l\n", "- ", text)
    return text.strip()


def extract_all_pages(doc: fitz.Document) -> list[str]:
    pages: list[str] = []
    for i in range(doc.page_count):
        raw = doc.load_page(i).get_text("text")
        pages.append(raw or "")
    return pages


def build_section_markdown(
    title: str,
    slug: str,
    topics: list[str],
    doc_start: int,
    doc_end: int,
    page_texts: list[str],
) -> str:
    body_parts: list[str] = []
    for doc_page in range(doc_start, doc_end + 1):
        idx = doc_to_pdf_index(doc_page)
        if idx < 0 or idx >= len(page_texts):
            continue
        cleaned = clean_page_text(page_texts[idx], doc_page)
        if cleaned:
            body_parts.append(cleaned)

    body = promote_headings("\n\n".join(body_parts))

    front = [
        f"# {title}",
        "",
        f"> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)",
        f"> **Manual pages:** {doc_start}–{doc_end}",
        f"> **Slug:** `{slug}`",
        "",
        "**Agent topics:** " + ", ".join(f"`{t}`" for t in topics),
        "",
        "---",
        "",
        body,
        "",
    ]
    return "\n".join(front)


def build_toc_markdown(manifest: list[dict]) -> str:
    lines = [
        "# Studio One 6.6 — Knowledge Index",
        "",
        "Machine-oriented table of contents for agent retrieval.",
        "",
        "| # | Section | Manual pages | File | Topics |",
        "|---|---------|--------------|------|--------|",
    ]
    for i, m in enumerate(manifest, 1):
        topics = ", ".join(m["topics"][:6])
        if len(m["topics"]) > 6:
            topics += ", …"
        lines.append(
            f"| {i} | {m['title']} | {m['doc_start']}–{m['doc_end']} | "
            f"[`chapters/{m['slug']}.md`](chapters/{m['slug']}.md) | {topics} |"
        )
    lines += [
        "",
        "## How to retrieve",
        "",
        "1. Read `AGENTS.md` for role and rules.",
        "2. Use this index to pick the chapter file for the user question.",
        "3. Open only the relevant chapter(s); do not load all files unless needed.",
        "4. Prefer quoting procedures, key commands, and constraints from the chapter text.",
        "",
    ]
    return "\n".join(lines)


def build_agents_md(manifest: list[dict]) -> str:
    topic_map = []
    for m in manifest:
        topic_map.append(f"- **{m['title']}** → `chapters/{m['slug']}.md` — topics: {', '.join(m['topics'][:8])}")

    return f"""# Studio One 6.6 Agent Knowledge

You are an expert assistant for **PreSonus Studio One 6.6** (Prime, Artist, and Professional).

## Source of truth

All product behavior, UI names, workflows, and feature availability in this pack come from the official:

**Studio One 6.6 Reference Manual (English)** — PreSonus / pae-web.presonusmusic.com

- Pack root: this directory
- Chapter files: `chapters/*.md`
- Full index: `INDEX.md`
- Machine manifest: `manifest.json`

When answering, ground claims in these files. If something is not covered, say so rather than inventing Studio One behavior.

## Edition awareness

Studio One 6.6 has three editions activated by product key (single installer):

| Edition | Highlights from manual |
|---------|------------------------|
| **Prime** | Unlimited audio/instrument tracks, stereo I/O, basic plug-ins + Presence XT, Arranger Track, browser/shop |
| **Artist** | Unlimited simultaneous record inputs, advanced editing (comping, transients, Melodyne trial), VST/AU, macros, Remote, more FX/instruments |
| **Professional** | Project (mastering) + Show (live) pages, Chord Track, Score editor, Melodyne Essential, video, Multi Instruments, AAF, Atmos/spatial, extra FX |

If a feature is Professional-only (or Artist+), call that out.

## How to use this knowledge pack

1. Parse the user question for Studio One domain terms (recording, console, Chord Track, Atmos, Show page, etc.).
2. Open `INDEX.md` or `manifest.json` and select the matching chapter file(s).
3. Read those chapter files and answer with concrete steps, UI labels, and options from the manual.
4. For multi-domain questions (e.g. “record with low latency then mix to stems”), load 2–3 chapters max.

### Chapter map

{chr(10).join(topic_map)}

## Answer style

- Prefer step-by-step procedures from the manual.
- Use official names: Arrange view, Console, Browser, Pool, Inspector, Control Link, etc.
- Mention macOS/Windows differences only when the manual does.
- Key commands: report as written in the manual; note that user keymaps may differ.
- Do not invent menu paths or parameters not present in the pack.

## Copying into a GitHub agent

Place this entire folder in a repository, for example:

```text
your-repo/
  .github/
    agents/          # or copilot instructions location you use
  knowledge/
    studio-one-6.6/  # <-- copy contents of this pack here
      AGENTS.md
      INDEX.md
      manifest.json
      chapters/
```

Then point the agent instructions at:

- Primary: `knowledge/studio-one-6.6/AGENTS.md`
- Retrieval: `knowledge/studio-one-6.6/INDEX.md` + `chapters/`

Optional: add a one-line include in repo `AGENTS.md` / `.github/copilot-instructions.md`:

```markdown
For Studio One 6.6 product questions, use knowledge/studio-one-6.6/AGENTS.md and retrieve from chapters/ via INDEX.md.
```

## Provenance

- Converted from: Studio_One_6.6_Reference_Manual_EN.pdf
- Manual version: V6.6
- PDF page count: 570
- Document content pages mapped: 1–564 (approx.)
- Conversion: text extraction via PyMuPDF; light cleanup of footers/bullets; structured into chapters for RAG/agent use

## License / copyright notice

Manual content is © PreSonus / related rights holders. This pack is a **restructured text extract for private agent use**. Do not republish the full manual as your own product documentation. Redistribute only if you have rights to do so.
"""


def build_readme() -> str:
    return """# Studio One 6.6 — Agent Knowledge Pack

Structured extract of the **PreSonus Studio One 6.6 Reference Manual (EN)** for use with GitHub Copilot coding agents, custom agents, and other LLM tools that ingest Markdown.

## Contents

| Path | Purpose |
|------|---------|
| `AGENTS.md` | Agent role, edition rules, retrieval instructions (copy this into agent config) |
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
"""


def build_all_in_one(manifest: list[dict], chapter_bodies: dict[str, str]) -> str:
    parts = [
        "# Studio One 6.6 Reference Manual — Full Text (Agent Pack)",
        "",
        "Single-file concatenation of all chapters for bulk paste into an agent.",
        "Prefer chaptered files when the agent supports multi-file retrieval.",
        "",
        "---",
        "",
    ]
    for m in manifest:
        parts.append(chapter_bodies[m["slug"]])
        parts.append("\n\n---\n")
    return "\n".join(parts)


def main() -> None:
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Opening {PDF_PATH} ...")
    doc = fitz.open(PDF_PATH)
    print(f"Pages: {doc.page_count}")
    page_texts = extract_all_pages(doc)
    doc.close()

    # Also keep cover + TOC as raw reference
    toc_pages = []
    for i in range(0, 6):
        toc_pages.append(clean_page_text(page_texts[i]))
    (OUT_DIR / "00-cover-and-toc.md").write_text(
        "# Cover and Table of Contents\n\n"
        + "> Extracted from PDF pages 1–6\n\n---\n\n"
        + "\n\n".join(toc_pages)
        + "\n",
        encoding="utf-8",
    )

    manifest: list[dict] = []
    chapter_bodies: dict[str, str] = {}

    for doc_start, doc_end, slug, title, topics in SECTIONS:
        print(f"Building {slug} (doc pp. {doc_start}-{doc_end}) ...")
        md = build_section_markdown(title, slug, topics, doc_start, doc_end, page_texts)
        path = CHAPTERS_DIR / f"{slug}.md"
        path.write_text(md, encoding="utf-8")
        chapter_bodies[slug] = md
        manifest.append(
            {
                "slug": slug,
                "title": title,
                "doc_start": doc_start,
                "doc_end": doc_end,
                "path": f"chapters/{slug}.md",
                "topics": topics,
                "chars": len(md),
                "approx_tokens": max(1, len(md) // 4),
            }
        )

    (OUT_DIR / "INDEX.md").write_text(build_toc_markdown(manifest), encoding="utf-8")
    (OUT_DIR / "AGENTS.md").write_text(build_agents_md(manifest), encoding="utf-8")
    (OUT_DIR / "README.md").write_text(build_readme(), encoding="utf-8")
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(
            {
                "product": "PreSonus Studio One",
                "version": "6.6",
                "manual": "Studio_One_6.6_Reference_Manual_EN.pdf",
                "language": "en",
                "sections": manifest,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    all_in_one = build_all_in_one(manifest, chapter_bodies)
    (OUT_DIR / "ALL_IN_ONE.md").write_text(all_in_one, encoding="utf-8")

    total_chars = sum(m["chars"] for m in manifest)
    print("\nDone.")
    print(f"Sections: {len(manifest)}")
    print(f"Total chapter chars: {total_chars:,}")
    print(f"Approx tokens: {total_chars // 4:,}")
    print(f"Output: {OUT_DIR}")


if __name__ == "__main__":
    main()
