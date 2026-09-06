"""Clip-edit knowledge + ffmpeg tools ported from Mira-Soline for music."""

from clip_edit_kb.catalog import SOURCE, TOOLS, SKIPPED, get_tool, list_tools
from clip_edit_kb.recipes import RECIPES, get_recipe
from clip_edit_kb.search import search_kb

__all__ = [
    "SOURCE",
    "TOOLS",
    "SKIPPED",
    "RECIPES",
    "get_tool",
    "list_tools",
    "get_recipe",
    "search_kb",
]
__version__ = "1.0.0"
__source__ = "Mira-Soline Edit-Video.py generic subset, ported 2026-09-06"
