from __future__ import annotations

from pathlib import Path

from clip_edit_kb import catalog, recipes

_EXTRACT = Path(__file__).resolve().parent.parent / "knowledge" / "workflow_extract.txt"


def _walk(obj, path=""):
    rows = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            rows += _walk(v, f"{path}.{k}" if path else str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            rows += _walk(v, f"{path}[{i}]")
    else:
        rows.append((path, str(obj)))
    return rows


def search_kb(query: str, limit: int = 20):
    terms = query.lower().split()
    hits = []
    corpus = {"source": catalog.SOURCE, "tools": catalog.TOOLS, "recipes": recipes.RECIPES}
    for path, text in _walk(corpus):
        blob = f"{path} {text}".lower()
        if all(t in blob for t in terms):
            hits.append({"source": "kb", "path": path, "text": text[:400]})
            if len(hits) >= limit:
                return hits
    if _EXTRACT.exists() and len(hits) < limit:
        raw = _EXTRACT.read_text(encoding="utf-8", errors="ignore")
        for block in raw.split("\n\n"):
            if not block.strip():
                continue
            low = block.lower()
            if all(t in low for t in terms):
                i = low.find(terms[0])
                sn = block[max(0, i - 60) : i + 280].replace("\n", " ")
                hits.append({"source": "extract", "path": "workflow_extract", "text": sn.strip()})
                if len(hits) >= limit:
                    break
    return hits
