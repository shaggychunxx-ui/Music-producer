import argparse, json
from monologue_kb import INSTRUMENT, get_topic, list_topics, get_recipe, search_kb
from monologue_kb.recipes import RECIPES

def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)

def main(argv=None):
    p = argparse.ArgumentParser(prog="monologue-kb")
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("info")
    s.add_parser("topics")
    t = s.add_parser("topic"); t.add_argument("name")
    r = s.add_parser("recipe"); r.add_argument("name", nargs="?", default="")
    q = s.add_parser("search"); q.add_argument("query"); q.add_argument("--limit", type=int, default=20)
    a = p.parse_args(argv)
    if a.cmd == "info":
        _p(INSTRUMENT)
    elif a.cmd == "topics":
        print("\n".join(list_topics()))
    elif a.cmd == "topic":
        _p(get_topic(a.name))
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
