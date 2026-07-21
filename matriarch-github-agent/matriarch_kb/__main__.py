"""CLI: python -m matriarch_kb <command> ..."""

from __future__ import annotations

import argparse
import json
import sys

from matriarch_kb import (
    INSTRUMENT,
    SPECS,
    access_globals_howto,
    get_module,
    get_recipe,
    list_modules,
    lookup_cc,
    lookup_sysex,
    search_kb,
)
from matriarch_kb.midi import SYSEX_GET, SYSEX_SET, build_set_sysex
from matriarch_kb.recipes import RECIPES
from matriarch_kb.search import dump_json


def _print(obj) -> None:
    if isinstance(obj, (dict, list)):
        print(json.dumps(obj, indent=2))
    else:
        print(obj)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="matriarch_kb",
        description="Moog Matriarch knowledge base (manual 012023)",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("info", help="Instrument overview")
    sub.add_parser("specs", help="Specifications")
    sub.add_parser("list-modules", help="List module ids")
    m = sub.add_parser("module", help="Show one module")
    m.add_argument("name")
    c = sub.add_parser("cc", help="Look up MIDI CC by name or number")
    c.add_argument("query")
    s = sub.add_parser("sysex", help="Look up SysEx parameter id or name")
    s.add_argument("query")
    sy = sub.add_parser("sysex-set", help="Build set-parameter SysEx bytes")
    sy.add_argument("param_id", type=int)
    sy.add_argument("value", type=int)
    sy.add_argument("--unit", type=int, default=0x7F)
    sub.add_parser("globals-howto", help="How to enter Global Settings")
    r = sub.add_parser("recipe", help="Show a patch recipe")
    r.add_argument("name", nargs="?", default="")
    q = sub.add_parser("search", help="Search the knowledge base")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=25)
    sub.add_parser("export-json", help="Dump full KB as JSON")

    args = p.parse_args(argv)

    if args.cmd == "info":
        _print(INSTRUMENT)
    elif args.cmd == "specs":
        _print(SPECS)
    elif args.cmd == "list-modules":
        print("\n".join(list_modules()))
    elif args.cmd == "module":
        _print(get_module(args.name))
    elif args.cmd == "cc":
        hits = lookup_cc(args.query)
        _print(hits or {"error": "no CC match", "query": args.query})
    elif args.cmd == "sysex":
        hit = lookup_sysex(args.query)
        _print(hit or {"error": "no sysex match", "query": args.query})
        print("SET template:", SYSEX_SET)
        print("GET template:", SYSEX_GET)
    elif args.cmd == "sysex-set":
        msg = build_set_sysex(args.param_id, args.value, args.unit)
        print(" ".join(f"{b:02X}" for b in msg))
    elif args.cmd == "globals-howto":
        print(access_globals_howto())
    elif args.cmd == "recipe":
        if not args.name:
            print("Available:", ", ".join(RECIPES))
        else:
            _print(get_recipe(args.name))
    elif args.cmd == "search":
        _print(search_kb(args.query, limit=args.limit))
    elif args.cmd == "export-json":
        sys.stdout.write(dump_json())
    else:
        p.error(f"unknown command {args.cmd}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
