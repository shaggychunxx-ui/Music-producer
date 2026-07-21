import argparse
import json

from humanize_kb import (
    ARTICLE,
    get_category,
    get_recipe,
    get_technique,
    list_categories,
    list_techniques,
    search_kb,
)
from humanize_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="humanize_kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("categories")
    c = s.add_parser("category")
    c.add_argument("name")
    s.add_parser("techniques")
    t = s.add_parser("technique")
    t.add_argument("name")
    r = s.add_parser("recipe")
    r.add_argument("name", nargs="?", default="")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    if a.cmd == "info":
        _p(ARTICLE)
    elif a.cmd == "categories":
        print("\n".join(list_categories()))
    elif a.cmd == "category":
        _p(get_category(a.name))
    elif a.cmd == "techniques":
        print("\n".join(list_techniques()))
    elif a.cmd == "technique":
        _p(get_technique(a.name))
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
