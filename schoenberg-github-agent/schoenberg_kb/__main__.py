"""CLI: python -m schoenberg_kb <command>"""

from __future__ import annotations

import argparse
import json
import sys

from schoenberg_kb import (
    BOOK,
    define,
    get_chapter,
    get_exercise,
    get_form,
    list_chapters,
    search_kb,
)
from schoenberg_kb.exercises import EXERCISES
from schoenberg_kb.forms import analysis_plan
from schoenberg_kb.search import dump_json


def _print(obj) -> None:
    if isinstance(obj, (dict, list)):
        print(json.dumps(obj, indent=2, ensure_ascii=False))
    else:
        print(obj)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="schoenberg_kb",
        description="Schoenberg Fundamentals of Musical Composition knowledge base",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("info", help="Book overview")
    sub.add_parser("list-chapters", help="List all chapters")
    ch = sub.add_parser("chapter", help="Show chapter by number or keyword")
    ch.add_argument("ref")
    d = sub.add_parser("define", help="Define a concept")
    d.add_argument("term")
    f = sub.add_parser("form", help="Show a formal type")
    f.add_argument("name")
    e = sub.add_parser("exercise", help="Show a practice exercise")
    e.add_argument("name", nargs="?", default="")
    s = sub.add_parser("search", help="Search KB + manual extract")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=20)
    a = sub.add_parser("analyze-plan", help="Generic analysis checklist for a passage")
    a.add_argument("context", nargs="*", default=["unspecified passage"])
    sub.add_parser("export-json", help="Dump structured KB as JSON")

    args = p.parse_args(argv)

    if args.cmd == "info":
        _print(BOOK)
    elif args.cmd == "list-chapters":
        print("\n".join(list_chapters()))
    elif args.cmd == "chapter":
        _print(get_chapter(args.ref))
    elif args.cmd == "define":
        _print(define(args.term))
    elif args.cmd == "form":
        _print(get_form(args.name))
    elif args.cmd == "exercise":
        if not args.name:
            print("Available:", ", ".join(EXERCISES))
        else:
            _print(get_exercise(args.name))
    elif args.cmd == "search":
        _print(search_kb(args.query, limit=args.limit))
    elif args.cmd == "analyze-plan":
        ctx = " ".join(args.context) if isinstance(args.context, list) else args.context
        _print(analysis_plan(ctx))
    elif args.cmd == "export-json":
        sys.stdout.write(dump_json())
    else:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
