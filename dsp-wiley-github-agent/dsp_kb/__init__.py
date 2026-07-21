"""Udo Zölzer Digital Audio Signal Processing (2nd ed.) knowledge base."""

from dsp_kb.book import BOOK, GLOSSARY, PEDAGOGY
from dsp_kb.chapters import CHAPTERS, get_chapter, list_chapters
from dsp_kb.concepts import CONCEPTS, define
from dsp_kb.recipes import RECIPES, get_recipe
from dsp_kb.search import search_kb

__all__ = [
    "BOOK",
    "GLOSSARY",
    "PEDAGOGY",
    "CHAPTERS",
    "get_chapter",
    "list_chapters",
    "CONCEPTS",
    "define",
    "RECIPES",
    "get_recipe",
    "search_kb",
]
__version__ = "1.0.0"
__source__ = "Udo Zölzer, Digital Audio Signal Processing, 2nd Edition, Wiley 2008"
