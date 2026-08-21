from __future__ import annotations

from signals_kb.source import CATALOG

LESSONS: dict[str, dict] = {row["slug"]: row for row in CATALOG["lessons"]}
SERIES: dict[str, dict] = {row["id"]: row for row in CATALOG["series"]}
STUDY_PATHS: dict[str, list[str]] = CATALOG["study_paths"]


def youtube_url(youtube_id: str) -> str:
    return f"https://www.youtube.com/watch?v={youtube_id}"


def lesson_url(slug: str) -> str:
    return f"https://signalsmusic.studio/lessons/{slug}"


def list_lessons(series: str | None = None) -> list[str]:
    rows = CATALOG["lessons"]
    if series:
        rows = [r for r in rows if r.get("series") == series]
    return [f"{r['slug']}: {r['title']}" for r in rows]


def list_series() -> list[str]:
    return [f"{s['id']}: {s['title']} — {s['goal']}" for s in CATALOG["series"]]


def get_series(name: str) -> dict:
    key = name.strip().lower().replace(" ", "-")
    if key in SERIES:
        s = dict(SERIES[key])
        s["lessons"] = [r for r in CATALOG["lessons"] if r.get("series") == key]
        return s
    hits = [s for s in CATALOG["series"] if key in s["id"] or key in s["title"].lower()]
    if not hits:
        return {"error": f"unknown series {name!r}", "available": list(SERIES)}
    s = dict(hits[0])
    s["lessons"] = [r for r in CATALOG["lessons"] if r.get("series") == s["id"]]
    return s


def get_lesson(name: str) -> dict:
    key = name.strip().lower().replace(" ", "-")
    if key in LESSONS:
        row = dict(LESSONS[key])
        row["lesson_url"] = lesson_url(key)
        if row.get("youtube_id"):
            row["youtube"] = youtube_url(row["youtube_id"])
        return row
    hits = [
        r
        for r in CATALOG["lessons"]
        if key in r["slug"] or key in r["title"].lower()
    ]
    if not hits:
        return {"error": f"unknown lesson {name!r}", "hint": "python -m signals_kb lessons"}
    if len(hits) > 1:
        return {"matches": [r["slug"] for r in hits]}
    return get_lesson(hits[0]["slug"])


def get_study_path(name: str) -> dict:
    key = name.strip().lower().replace(" ", "_")
    aliases = {
        "harmony": "harmony_writer",
        "progressions": "harmony_writer",
        "modes": "modal_writer",
        "modal": "modal_writer",
        "rhythm": "rhythm_producer",
        "analysis": "analysis_lab",
        "analyze": "analysis_lab",
    }
    key = aliases.get(key, key)
    slugs = STUDY_PATHS.get(key)
    if not slugs:
        return {"error": f"unknown path {name!r}", "available": list(STUDY_PATHS)}
    steps = []
    for slug in slugs:
        row = LESSONS.get(slug, {"slug": slug, "title": slug})
        step = {
            "slug": slug,
            "title": row.get("title", slug),
            "lesson_url": lesson_url(slug),
        }
        if row.get("youtube_id"):
            step["youtube"] = youtube_url(row["youtube_id"])
        steps.append(step)
    return {
        "path": key,
        "watch_in_order": True,
        "apply_after_each": "Write one 4–8 bar idea using only that lesson's technique before the next video.",
        "steps": steps,
    }


def watch(name: str) -> dict:
    extra = {e["youtube_id"]: e for e in CATALOG.get("extra_youtube", [])}
    if name in extra:
        e = extra[name]
        return {"title": e["title"], "youtube": youtube_url(e["youtube_id"]), "use": e.get("use")}
    if name.replace("-", "") == "map" or "43" in name or name == "qeS8txkoUH4":
        e = CATALOG["extra_youtube"][0]
        return {"title": e["title"], "youtube": youtube_url(e["youtube_id"]), "use": e.get("use")}
    lesson = get_lesson(name)
    if "error" in lesson or "matches" in lesson:
        return lesson
    if not lesson.get("youtube"):
        return {
            "title": lesson["title"],
            "lesson_url": lesson["lesson_url"],
            "note": "No YouTube id catalogued — open the lesson page; the video is embedded there.",
        }
    return {
        "title": lesson["title"],
        "youtube": lesson["youtube"],
        "lesson_url": lesson["lesson_url"],
    }
