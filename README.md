# Music-producer

A conversational agent with the persona of a professional music producer and
composer. The agent, **Nova**, offers expert guidance on songwriting,
arrangement, mixing, mastering, and genre-specific production techniques.

## Usage

Chat with the agent interactively from the command line:

```bash
python -m music_producer_agent.cli
```

Or use it programmatically:

```python
from music_producer_agent import MusicProducerAgent

agent = MusicProducerAgent()
print(agent.greet())
print(agent.respond("What chord progression works for an emotional chorus?"))
```

## Running tests

```bash
pip install pytest
pytest
```
