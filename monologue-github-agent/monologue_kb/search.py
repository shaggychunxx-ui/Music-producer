from __future__ import annotations
from pathlib import Path
from monologue_kb import instrument, recipes

_EXTRACT = Path(__file__).resolve().parent.parent / "knowledge" / "manual_extract.txt"

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
    corpus = {"instrument": instrument.INSTRUMENT, "topics": instrument.TOPICS, "recipes": recipes.RECIPES}
    for path, text in _walk(corpus):
        blob = f"{path} {text}".lower()
        if all(t in blob for t in terms):
            hits.append({"source": "kb", "path": path, "text": text[:400]})
            if len(hits) >= limit:
                return hits
    if _EXTRACT.exists() and len(hits) < limit:
        raw = _EXTRACT.read_text(encoding="utf-8", errors="ignore")
        for block in raw.split("---PAGE "):
            if not block.strip():
                continue
            head, _, body = block.partition("---")
            page = head.strip().split()[0] if head.strip() else "?"
            low = body.lower()
            if all(t in low for t in terms):
                i = low.find(terms[0])
                sn = body[max(0, i - 60) : i + 280].replace("\n", " ")
                hits.append({"source": "extract", "path": f"page {page}", "text": sn.strip()})
                if len(hits) >= limit:
                    break
    return hits
