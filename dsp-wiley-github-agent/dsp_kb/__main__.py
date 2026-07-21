import argparse
import json

from dsp_kb import (
    BOOK,
    define,
    get_chapter,
    get_recipe,
    list_chapters,
    search_kb,
)
from dsp_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="dsp_kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("list-chapters")
    ch = s.add_parser("chapter")
    ch.add_argument("ref")
    d = s.add_parser("define")
    d.add_argument("term")
    r = s.add_parser("recipe")
    r.add_argument("name", nargs="?", default="")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    if a.cmd == "info":
        _p(BOOK)
    elif a.cmd == "list-chapters":
        print("\n".join(list_chapters()))
    elif a.cmd == "chapter":
        _p(get_chapter(a.ref))
    elif a.cmd == "define":
        _p(define(a.term))
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
