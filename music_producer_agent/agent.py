"""The Music Producer Agent implementation."""

from dataclasses import dataclass, field
from typing import List

from .knowledge_base import KNOWLEDGE_BASE, find_topic
from .persona import NAME, SYSTEM_PROMPT

GREETING = (
    f"Hey, I'm {NAME}, your professional music producer and composer. "
    "Tell me about the track you're working on, or ask about composition, "
    "arrangement, mixing, mastering, or genre-specific production tips."
)

FALLBACK_RESPONSE = (
    "I'd love to help with that. Could you tell me more about the genre, "
    "mood, or stage of production you're at (writing, arranging, mixing, or "
    "mastering)? That'll help me give you specific, actionable advice."
)


@dataclass
class MusicProducerAgent:
    """A conversational agent with a professional music producer persona."""

    name: str = NAME
    system_prompt: str = SYSTEM_PROMPT
    history: List[str] = field(default_factory=list)

    def greet(self) -> str:
        """Return the agent's introductory greeting."""
        return GREETING

    def respond(self, message: str) -> str:
        """Generate a response to a user's message.

        Uses keyword matching against a music production knowledge base to
        provide targeted, expert advice. Falls back to a clarifying prompt
        when no topic is recognized.
        """
        if not message or not message.strip():
            return self.greet()

        self.history.append(message)

        topic = find_topic(message)
        if topic is not None:
            return KNOWLEDGE_BASE[topic]["advice"]

        return FALLBACK_RESPONSE
