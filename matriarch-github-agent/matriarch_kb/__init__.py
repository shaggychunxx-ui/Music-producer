"""Moog Matriarch knowledge base for GitHub / coding agents.

Structured transcription of Matriarch Owner's Manual (012023).
"""

from __future__ import annotations

from matriarch_kb.instrument import INSTRUMENT, SIGNAL_FLOW, SPECS
from matriarch_kb.modules import MODULES, get_module, list_modules
from matriarch_kb.midi import CC_MAP, SYSEX_PARAMS, lookup_cc, lookup_sysex
from matriarch_kb.globals import GLOBAL_GROUPS, access_globals_howto
from matriarch_kb.recipes import RECIPES, get_recipe
from matriarch_kb.search import search_kb

__all__ = [
    "INSTRUMENT",
    "SIGNAL_FLOW",
    "SPECS",
    "MODULES",
    "get_module",
    "list_modules",
    "CC_MAP",
    "SYSEX_PARAMS",
    "lookup_cc",
    "lookup_sysex",
    "GLOBAL_GROUPS",
    "access_globals_howto",
    "RECIPES",
    "get_recipe",
    "search_kb",
]

__version__ = "1.0.0"
__manual__ = "Matriarch Owner's Manual 012023 (January 2023)"
