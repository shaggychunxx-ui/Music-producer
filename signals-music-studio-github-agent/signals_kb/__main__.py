import argparse
import json

from signals_kb import (
    SOURCE,
    get_lesson,
    get_mode,
    get_recipe,
    get_series,
    get_study_path,
    get_technique,
    list_lessons,
    list_modes,
    list_series,
    list_techniques,
    search_kb,
    watch,
)
from signals_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="signals_kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("series")
    ser = s.add_parser("series-show")
    ser.add_argument("name")
    les = s.add_parser("lessons")
    les.add_argument("--series", default="")
    one = s.add_parser("lesson")
    one.add_argument("name")
    s.add_parser("modes")
    md = s.add_parser("mode")
    md.add_argument("name")
    s.add_parser("techniques")
    tech = s.add_parser("technique")
    tech.add_argument("name", nargs="?", default="")
    rec = s.add_parser("recipe")
    rec.add_argument("name", nargs="?", default="")
    st = s.add_parser("study")
    st.add_argument("path", nargs="?", default="")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)
    w = s.add_parser("watch")
    w.add_argument("name")
    a = p.parse_args(argv)

    if a.cmd == "info":
        _p(SOURCE)
    elif a.cmd == "series":
        print("\n".join(list_series()))
    elif a.cmd == "series-show":
        _p(get_series(a.name))
    elif a.cmd == "lessons":
        print("\n".join(list_lessons(a.series or None)))
    elif a.cmd == "lesson":
        _p(get_lesson(a.name))
    elif a.cmd == "modes":
        print("\n".join(list_modes()))
    elif a.cmd == "mode":
        _p(get_mode(a.name))
    elif a.cmd == "techniques":
        print("\n".join(list_techniques()))
    elif a.cmd == "technique":
        if not a.name:
            print("Available:", ", ".join(__import__("signals_kb.techniques", fromlist=["TECHNIQUES"]).TECHNIQUES))
        else:
            _p(get_technique(a.name))
    elif a.cmd == "recipe":
        if not a.name:
            print("Available:", ", ".join(RECIPES))
        else:
            _p(get_recipe(a.name))
    elif a.cmd == "study":
        if not a.path:
            _p(
                {
                    "available": [
                        "harmony_writer",
                        "modal_writer",
                        "rhythm_producer",
                        "analysis_lab",
                    ],
                    "habit": "python -m signals_kb recipe daily_key",
                }
            )
        else:
            _p(get_study_path(a.path))
    elif a.cmd == "search":
        _p(search_kb(a.query, a.limit))
    elif a.cmd == "watch":
        _p(watch(a.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
