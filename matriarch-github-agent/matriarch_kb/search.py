"""Simple full-text search across structured knowledge."""

from __future__ import annotations

import json
from typing import Any

from matriarch_kb import globals as g
from matriarch_kb import instrument, midi, modules, recipes


def _walk(obj: Any, path: str = "") -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else str(k)
            out.extend(_walk(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.extend(_walk(v, f"{path}[{i}]"))
    else:
        out.append((path, str(obj)))
    return out


def _corpus() -> list[tuple[str, str]]:
    blobs = [
        ("instrument", instrument.INSTRUMENT),
        ("signal_flow", instrument.SIGNAL_FLOW),
        ("specs", instrument.SPECS),
        ("modules", modules.MODULES),
        ("cc", midi.CC_MAP),
        ("sysex", midi.SYSEX_PARAMS),
        ("globals", g.GLOBAL_GROUPS),
        ("recipes", recipes.RECIPES),
    ]
    rows: list[tuple[str, str]] = []
    for name, obj in blobs:
        for path, text in _walk(obj, name):
            rows.append((path, text))
    return rows


def search_kb(query: str, limit: int = 25) -> list[dict[str, str]]:
    q = query.lower().strip()
    if not q:
        return []
    terms = q.split()
    hits: list[dict[str, str]] = []
    for path, text in _corpus():
        low = text.lower()
        if all(t in low or t in path.lower() for t in terms):
            hits.append({"path": path, "text": text[:400]})
            if len(hits) >= limit:
                break
    return hits


def dump_json() -> str:
    """Export full structured KB as JSON string."""
    payload = {
        "instrument": instrument.INSTRUMENT,
        "signal_flow": instrument.SIGNAL_FLOW,
        "specs": instrument.SPECS,
        "modules": modules.MODULES,
        "midi_cc": midi.CC_MAP,
        "midi_impl": midi.MIDI_IMPL,
        "sysex": midi.SYSEX_PARAMS,
        "globals": g.GLOBAL_GROUPS,
        "recipes": recipes.RECIPES,
    }
    return json.dumps(payload, indent=2)
