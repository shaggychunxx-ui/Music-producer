"""Output MOVEMENT knowledge base for GitHub agents."""

from movement_kb.instrument import INSTRUMENT, TOPICS, get_topic, list_topics
from movement_kb.recipes import RECIPES, get_recipe
from movement_kb.search import search_kb

__all__ = [
    "INSTRUMENT",
    "TOPICS",
    "get_topic",
    "list_topics",
    "RECIPES",
    "get_recipe",
    "search_kb",
]
__version__ = "1.0.0"
