"""Signals Music Studio (Jake Lizzio) knowledge base — songwriting techniques."""

from signals_kb.source import SOURCE, CATALOG
from signals_kb.lessons import (
    get_lesson,
    get_series,
    get_study_path,
    list_lessons,
    list_series,
    watch,
)
from signals_kb.modes import MODES, get_mode, list_modes
from signals_kb.techniques import TECHNIQUES, get_technique, list_techniques
from signals_kb.recipes import RECIPES, get_recipe
from signals_kb.search import search_kb

__all__ = [
    "SOURCE",
    "CATALOG",
    "get_lesson",
    "get_series",
    "get_study_path",
    "list_lessons",
    "list_series",
    "watch",
    "MODES",
    "get_mode",
    "list_modes",
    "TECHNIQUES",
    "get_technique",
    "list_techniques",
    "RECIPES",
    "get_recipe",
    "search_kb",
]
__version__ = "1.0.0"
