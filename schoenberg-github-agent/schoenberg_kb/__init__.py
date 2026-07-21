"""Schoenberg Fundamentals of Musical Composition — knowledge base for agents."""

from __future__ import annotations

from schoenberg_kb.book import BOOK, GLOSSARY, PEDAGOGY
from schoenberg_kb.chapters import CHAPTERS, get_chapter, list_chapters
from schoenberg_kb.concepts import CONCEPTS, define
from schoenberg_kb.forms import FORMS, get_form
from schoenberg_kb.exercises import EXERCISES, get_exercise
from schoenberg_kb.search import search_kb

__all__ = [
    "BOOK",
    "GLOSSARY",
    "PEDAGOGY",
    "CHAPTERS",
    "get_chapter",
    "list_chapters",
    "CONCEPTS",
    "define",
    "FORMS",
    "get_form",
    "EXERCISES",
    "get_exercise",
    "search_kb",
]

__version__ = "1.0.0"
__source__ = "Arnold Schoenberg, Fundamentals of Musical Composition (1967/1970 Faber)"
