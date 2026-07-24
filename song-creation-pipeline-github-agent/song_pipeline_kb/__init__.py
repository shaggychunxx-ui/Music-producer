"""Song creation pipeline knowledge base (gated original production process)."""

from song_pipeline_kb.pipeline import (
    GATES,
    META,
    PHASES,
    SCAFFOLD,
    TEMP_TABLE,
    get_phase,
    list_phases,
)
from song_pipeline_kb.phrases import PHRASES, match_phrase
from song_pipeline_kb.recipes import RECIPES, get_recipe
from song_pipeline_kb.search import search_kb

__all__ = [
    "META",
    "PHASES",
    "GATES",
    "TEMP_TABLE",
    "SCAFFOLD",
    "RECIPES",
    "PHRASES",
    "get_phase",
    "list_phases",
    "get_recipe",
    "match_phrase",
    "search_kb",
]
__version__ = "1.0.0"
