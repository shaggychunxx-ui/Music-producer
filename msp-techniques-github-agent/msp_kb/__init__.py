"""Miller Puckette Theory and Technique of Electronic Music knowledge base."""

from msp_kb.book import BOOK, GLOSSARY, PEDAGOGY
from msp_kb.chapters import CHAPTERS, get_chapter, list_chapters
from msp_kb.concepts import CONCEPTS, define
from msp_kb.recipes import RECIPES, get_recipe
from msp_kb.search import search_kb

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
