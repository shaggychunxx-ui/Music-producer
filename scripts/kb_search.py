#!/usr/bin/env python3
"""Unified search across all Music-producer knowledge packages + Studio One chapters.

Usage (from Music-producer root):
  python scripts/kb_search.py "sidechain"
  python scripts/kb_search.py "matriarch oscillator" --limit 8
  python scripts/kb_search.py "arm track" --only studio-one,matriarch
"""
from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (display_name, folder, package module path for search_kb, extra extract paths)
KB_PACKS: list[tuple[str, str, str | None, list[str]]] = [
    ("dsp", "dsp-wiley-github-agent", "dsp_kb.search", ["knowledge/manual_extract.txt"]),
    ("genre-mix", "genre-mixing-github-agent", "genre_mix_kb.search", ["knowledge/article_extract.txt"]),
    ("matriarch", "matriarch-github-agent", "matriarch_kb.search", ["knowledge/manual_extract.txt"]),
    ("monologue", "monologue-github-agent", "monologue_kb.search", ["knowledge/manual_extract.txt"]),
    ("movement", "movement-github-agent", "movement_kb.search", ["knowledge/manual_extract.txt"]),
    ("msp", "msp-techniques-github-agent", "msp_kb.search", ["knowledge/manual_extract.txt"]),
    ("theory", "music-theory-advanced-github-agent", "theory_kb.search", ["knowledge/manual_extract.txt"]),
    ("signals", "signals-music-studio-github-agent", "signals_kb.search", ["knowledge/lesson_extract.txt"]),
    ("producers", "producers-genre-guide-github-agent", "producers_kb.search", ["knowledge/manual_extract.txt"]),
    ("schoenberg", "schoenberg-github-agent", "schoenberg_kb.search", ["knowledge/manual_extract.txt"]),
    ("song-pipeline", "song-creation-pipeline-github-agent", "song_pipeline_kb.search", ["knowledge/workflow_extract.txt"]),
    ("studiolive", "studiolive-github-agent", "studiolive_kb.search", ["knowledge/manual_extract.txt"]),
    ("tr8s", "tr8s-github-agent", "tr8s_kb.search", ["knowledge/manual_extract.txt"]),
    ("clip-edit", "clip-edit-github-agent", "clip_edit_kb.search", ["knowledge/workflow_extract.txt"]),
]

S1_DIR = ROOT / "studio-one-6.6-agent-knowledge"


def _search_extract(path: Path, query: str, limit: int) -> list[dict]:
    if not path.exists():
        return []
    terms = query.lower().split()
    text = path.read_text(encoding="utf-8", errors="ignore")
    hits = []
    # page-ish blocks or paragraphs
    blocks = text.split("\n\n") if "---PAGE " not in text else text.split("---PAGE ")
    for block in blocks:
        low = block.lower()
        if not all(t in low for t in terms):
            continue
        i = low.find(terms[0])
        sn = block[max(0, i - 80) : i + 280].replace("\n", " ").strip()
        hits.append({"source": "extract", "path": path.name, "text": sn[:450]})
        if len(hits) >= limit:
            break
    return hits


def _search_s1(query: str, limit: int) -> list[dict]:
    terms = query.lower().split()
    hits: list[dict] = []
    if not S1_DIR.exists():
        return hits
    files = list(S1_DIR.glob("*.md")) + list((S1_DIR / "chapters").glob("*.md") if (S1_DIR / "chapters").exists() else [])
    for f in files:
        try:
            body = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        low = body.lower()
        if not all(t in low for t in terms):
            continue
        i = low.find(terms[0])
        sn = body[max(0, i - 80) : i + 280].replace("\n", " ").strip()
        hits.append({"source": "studio-one", "path": str(f.relative_to(ROOT)), "text": sn[:450]})
        if len(hits) >= limit:
            break
    return hits


def search_all(query: str, limit: int = 5, only: set[str] | None = None) -> list[dict]:
    results: list[dict] = []
    for name, folder, mod_path, extracts in KB_PACKS:
        if only and name not in only and folder not in only:
            continue
        folder_path = ROOT / folder
        if not folder_path.exists():
            continue
        # ensure package importable
        if str(folder_path) not in sys.path:
            sys.path.insert(0, str(folder_path))
        pack_hits: list[dict] = []
        if mod_path:
            try:
                mod = importlib.import_module(mod_path)
                search_fn = getattr(mod, "search_kb", None)
                if callable(search_fn):
                    pack_hits = search_fn(query, limit=limit) or []
            except Exception as e:
                pack_hits = [{"source": "error", "path": mod_path, "text": str(e)}]
        if len(pack_hits) < limit:
            for rel in extracts:
                pack_hits.extend(_search_extract(folder_path / rel, query, limit - len(pack_hits)))
        for h in pack_hits[:limit]:
            row = dict(h) if isinstance(h, dict) else {"text": str(h)}
            row["kb"] = name
            results.append(row)

    if not only or "studio-one" in only or "s1" in only:
        for h in _search_s1(query, limit):
            h["kb"] = "studio-one"
            results.append(h)

    return results


def main() -> int:
    ap = argparse.ArgumentParser(description="Search all Music-producer knowledge bases")
    ap.add_argument("query", help="Search terms (AND match)")
    ap.add_argument("--limit", type=int, default=5, help="Max hits per KB")
    ap.add_argument("--only", type=str, default="", help="Comma list of kb names")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    only = {x.strip() for x in args.only.split(",") if x.strip()} or None
    hits = search_all(args.query, limit=args.limit, only=only)
    if args.json:
        print(json.dumps(hits, indent=2))
    else:
        if not hits:
            print("No hits.")
            return 1
        for i, h in enumerate(hits, 1):
            kb = h.get("kb", "?")
            path = h.get("path", "")
            text = (h.get("text") or "")[:400]
            print(f"[{i}] ({kb}) {path}")
            print(f"    {text}")
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
