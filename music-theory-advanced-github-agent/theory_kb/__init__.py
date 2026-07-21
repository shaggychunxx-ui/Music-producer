"""Advanced Music Theory (Eowyn / mysongbook) knowledge base — modes & modulation."""

from theory_kb.book import BOOK, PEDAGOGY
from theory_kb.modes import MODES, get_mode, list_modes
from theory_kb.concepts import CONCEPTS, define
from theory_kb.topics import TOPICS, get_topic, list_topics
from theory_kb.recipes import RECIPES, get_recipe
from theory_kb.search import search_kb

__all__ = [
    "BOOK",
    "PEDAGOGY",
    "MODES",
    "get_mode",
    "list_modes",
    "CONCEPTS",
    "define",
    "TOPICS",
    "get_topic",
    "list_topics",
    "RECIPES",
    "get_recipe",
    "search_kb",
]
__version__ = "1.0.0"
