"""Search structured knowledge and optional full extract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from schoenberg_kb import book, chapters, concepts, exercises, forms

_EXTRACT = Path(__file__).resolve().parent.parent / "knowledge" / "manual_extract.txt"


def _walk(obj: Any, path: str = "") -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else str(k)
            rows.extend(_walk(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            rows.extend(_walk(v, f"{path}[{i}]"))
    else:
        rows.append((path, str(obj)))
    return rows


def _structured_corpus() -> list[tuple[str, str]]:
    blobs = [
        ("book", book.BOOK),
        ("glossary", book.GLOSSARY),
        ("pedagogy", book.PEDAGOGY),
        ("chapters", chapters.CHAPTERS),
        ("concepts", concepts.CONCEPTS),
        ("forms", forms.FORMS),
        ("exercises", exercises.EXERCISES),
    ]
    rows: list[tuple[str, str]] = []
    for name, obj in blobs:
        rows.extend(_walk(obj, name))
    return rows


def search_kb(query: str, limit: int = 25, include_extract: bool = True) -> list[dict[str, str]]:
    terms = query.lower().split()
    if not terms:
        return []
    hits: list[dict[str, str]] = []
    for path, text in _structured_corpus():
        low = f"{path} {text}".lower()
        if all(t in low for t in terms):
            hits.append({"source": "kb", "path": path, "text": text[:500]})
            if len(hits) >= limit:
                return hits

    if include_extract and _EXTRACT.exists() and len(hits) < limit:
        try:
            raw = _EXTRACT.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            return hits
        # crude page search
        for block in raw.split("---PAGE "):
            if not block.strip():
                continue
            head, _, body = block.partition("---")
            page = head.strip().split()[0] if head.strip() else "?"
            low = body.lower()
            if all(t in low for t in terms):
                # grab a window around first term
                idx = low.find(terms[0])
                snippet = body[max(0, idx - 80) : idx + 320].replace("\n", " ")
                hits.append({"source": "extract", "path": f"page {page}", "text": snippet.strip()})
                if len(hits) >= limit:
                    break
    return hits


def dump_json() -> str:
    payload = {
        "book": book.BOOK,
        "glossary": book.GLOSSARY,
        "pedagogy": book.PEDAGOGY,
        "chapters": chapters.CHAPTERS,
        "concepts": concepts.CONCEPTS,
        "forms": forms.FORMS,
        "exercises": exercises.EXERCISES,
    }
    return json.dumps(payload, indent=2)
