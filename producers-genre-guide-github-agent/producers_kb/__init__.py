"""Music Producer's Complete Genre Guide knowledge base."""

from producers_kb.guide import BOOK, FOUNDATIONS, GENRES, get_genre, list_genres, get_foundation
from producers_kb.recipes import RECIPES, get_recipe
from producers_kb.search import search_kb

__all__ = [
    "BOOK",
    "FOUNDATIONS",
    "GENRES",
    "get_genre",
    "list_genres",
    "get_foundation",
    "RECIPES",
    "get_recipe",
    "search_kb",
]
__version__ = "1.0.0"
