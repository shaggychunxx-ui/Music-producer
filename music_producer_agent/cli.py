"""Interactive command-line chat interface for the Music Producer Agent."""

import sys

from .agent import MusicProducerAgent


def main() -> None:
    agent = MusicProducerAgent()
    print(agent.greet())
    print("(type 'exit' or 'quit' to leave the session)\n")

    for line in sys.stdin:
        message = line.strip()
        if message.lower() in {"exit", "quit"}:
            print("Great session — go make something amazing!")
            break
        if not message:
            continue
        print(f"\n{agent.name}: {agent.respond(message)}\n")


if __name__ == "__main__":
    main()
