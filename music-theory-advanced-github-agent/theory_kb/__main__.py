import argparse
import json

from theory_kb import (
    BOOK,
    define,
    get_mode,
    get_recipe,
    get_topic,
    list_modes,
    list_topics,
    search_kb,
)
from theory_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="theory_kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("topics")
    s.add_parser("modes")
    t = s.add_parser("topic")
    t.add_argument("name")
    m = s.add_parser("mode")
    m.add_argument("name")
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
    elif a.cmd == "topics":
        print("\n".join(list_topics()))
    elif a.cmd == "modes":
        print("\n".join(list_modes()))
    elif a.cmd == "topic":
        _p(get_topic(a.name))
    elif a.cmd == "mode":
        _p(get_mode(a.name))
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
