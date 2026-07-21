from __future__ import annotations

from pathlib import Path

from humanize_kb import article, recipes

_EXTRACT = Path(__file__).resolve().parent.parent / "knowledge" / "article_extract.txt"


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


def search_kb(query: str, limit: int = 25):
    terms = query.lower().split()
    hits = []
    corpus = {
        "article": article.ARTICLE,
        "categories": article.CATEGORIES,
        "recipes": recipes.RECIPES,
    }
    for path, text in _walk(corpus):
        blob = f"{path} {text}".lower()
        if all(t in blob for t in terms):
            hits.append({"source": "kb", "path": path, "text": text[:400]})
            if len(hits) >= limit:
                return hits
    if _EXTRACT.exists() and len(hits) < limit:
        raw = _EXTRACT.read_text(encoding="utf-8", errors="ignore")
        low = raw.lower()
        if all(t in low for t in terms):
            i = low.find(terms[0])
            sn = raw[max(0, i - 80) : i + 350].replace("\n", " ")
            hits.append({"source": "extract", "path": "article_extract.txt", "text": sn.strip()})
    return hits
