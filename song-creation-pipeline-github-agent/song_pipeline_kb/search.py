from __future__ import annotations

from pathlib import Path

from song_pipeline_kb import pipeline, phrases, recipes

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


def search_kb(query: str, limit: int = 25):
    terms = query.lower().split()
    hits = []
    corpus = {
        "meta": pipeline.META,
        "phases": pipeline.PHASES,
        "gates": pipeline.GATES,
        "temp": pipeline.TEMP_TABLE,
        "scaffold": pipeline.SCAFFOLD,
        "recipes": recipes.RECIPES,
        "phrases": phrases.PHRASES,
    }
    for path, text in _walk(corpus):
        blob = f"{path} {text}".lower()
        if all(t in blob for t in terms):
            hits.append({"source": "kb", "path": path, "text": text[:400]})
            if len(hits) >= limit:
                return hits
    if _EXTRACT.exists() and len(hits) < limit:
        raw = _EXTRACT.read_text(encoding="utf-8", errors="ignore")
        # block-ish search
        for block in raw.split("\n\n"):
            low = block.lower()
            if all(t in low for t in terms):
                sn = " ".join(block.split())[:400]
                hits.append({"source": "extract", "path": "workflow_extract.txt", "text": sn})
                if len(hits) >= limit:
                    break
    return hits
