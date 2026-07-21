import argparse
import json

from genre_mix_kb import ARTICLE, get_genre, get_recipe, get_tool, list_genres, search_kb
from genre_mix_kb.recipes import RECIPES


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None):
    p = argparse.ArgumentParser(prog="genre_mix_kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("genres")
    g = s.add_parser("genre")
    g.add_argument("name")
    t = s.add_parser("tool")
    t.add_argument("name")
    r = s.add_parser("recipe")
    r.add_argument("name", nargs="?", default="")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    if a.cmd == "info":
        _p(ARTICLE)
    elif a.cmd == "genres":
        print("\n".join(list_genres()))
    elif a.cmd == "genre":
        _p(get_genre(a.name))
    elif a.cmd == "tool":
        _p(get_tool(a.name))
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
