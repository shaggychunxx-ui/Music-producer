import argparse
import json

from song_pipeline_kb import (
    GATES,
    META,
    SCAFFOLD,
    TEMP_TABLE,
    get_phase,
    get_recipe,
    list_phases,
    match_phrase,
    search_kb,
)
from song_pipeline_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="song_pipeline_kb")
    s = p.add_subparsers(dest="cmd", required=True)

    s.add_parser("info")
    s.add_parser("phases")
    ph = s.add_parser("phase")
    ph.add_argument("name")
    s.add_parser("gates")
    s.add_parser("temp")
    s.add_parser("scaffold")
    r = s.add_parser("recipe")
    r.add_argument("name", nargs="?", default="list")
    phr = s.add_parser("phrase")
    phr.add_argument("text")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)

    a = p.parse_args(argv)

    if a.cmd == "info":
        _p(META)
    elif a.cmd == "phases":
        for k in list_phases():
            z = get_phase(k)
            print(f"{z.get('id', '?'):3} {k:12}  {z.get('name', '')}")
    elif a.cmd == "phase":
        _p(get_phase(a.name))
    elif a.cmd == "gates":
        _p(GATES)
    elif a.cmd == "temp":
        _p(TEMP_TABLE)
    elif a.cmd == "scaffold":
        _p(SCAFFOLD)
    elif a.cmd == "recipe":
        if not a.name or a.name in ("list", "all"):
            print("Available:", ", ".join(RECIPES))
        else:
            _p(get_recipe(a.name))
    elif a.cmd == "phrase":
        _p(match_phrase(a.text))
    elif a.cmd == "search":
        _p(search_kb(a.query, a.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
