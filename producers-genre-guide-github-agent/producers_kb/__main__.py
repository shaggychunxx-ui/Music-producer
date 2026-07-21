import argparse
import json

from producers_kb import (
    BOOK,
    get_foundation,
    get_genre,
    get_recipe,
    list_genres,
    search_kb,
)
from producers_kb.guide import FOUNDATIONS
from producers_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="producers_kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("genres")
    s.add_parser("foundations")
    g = s.add_parser("genre")
    g.add_argument("name")
    f = s.add_parser("foundation")
    f.add_argument("name")
    r = s.add_parser("recipe")
    r.add_argument("name", nargs="?", default="")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    if a.cmd == "info":
        _p(BOOK)
    elif a.cmd == "genres":
        print("\n".join(list_genres()))
    elif a.cmd == "foundations":
        print("\n".join(FOUNDATIONS.keys()))
    elif a.cmd == "genre":
        _p(get_genre(a.name))
    elif a.cmd == "foundation":
        _p(get_foundation(a.name))
    elif a.cmd == "recipe":
        if not a.name:
            print("Available:", ", ".join(RECIPES))
        else:
            _p(get_recipe(a.name))
    elif a.cmd == "search":
        _p(search_kb(a.query, a.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
