import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from music_producer_agent import MusicProducerAgent, SYSTEM_PROMPT


def test_persona_mentions_producer_and_composer():
    assert "producer" in SYSTEM_PROMPT.lower()
    assert "composer" in SYSTEM_PROMPT.lower()


def test_greet_returns_introduction():
    agent = MusicProducerAgent()
    greeting = agent.greet()
    assert agent.name in greeting
    assert "producer" in greeting.lower()


def test_empty_message_returns_greeting():
    agent = MusicProducerAgent()
    assert agent.respond("") == agent.greet()


def test_chord_progression_topic():
    agent = MusicProducerAgent()
    response = agent.respond("Can you help me with a chord progression?")
    assert "progression" in response.lower() or "chord" in response.lower()


def test_mixing_topic():
    agent = MusicProducerAgent()
    response = agent.respond("How should I approach mixing my vocals?")
    assert "eq" in response.lower() or "compression" in response.lower()


def test_mastering_topic():
    agent = MusicProducerAgent()
    response = agent.respond("What LUFS should I master to?")
    assert "lufs" in response.lower() or "loudness" in response.lower()


def test_unrecognized_message_returns_fallback():
    agent = MusicProducerAgent()
    response = agent.respond("Tell me about underwater basket weaving")
    assert "genre" in response.lower() or "mood" in response.lower()


def test_history_tracks_messages():
    agent = MusicProducerAgent()
    agent.respond("Tell me about melody writing")
    assert "Tell me about melody writing" in agent.history
