"""User language → pipeline action (phrase book)."""

from __future__ import annotations

from typing import Any

PHRASES: list[dict[str, str]] = [
    {
        "match": "sounds good|good go next|go next",
        "action": "Lock current layer; tick GATES+NOTES; advance one gate only",
        "recipe": "focus_one_part",
    },
    {
        "match": "perfect|\\+[0-9]+ ?db",
        "action": "Lock + apply exact level move only",
        "recipe": "focus_one_part",
    },
    {
        "match": "parts structured|organize parts|part organization",
        "action": "PARTS_STRUCTURE + role stems only — do not rewrite form",
        "recipe": "parts_not_form",
    },
    {
        "match": "didn't want.*changed|didn't want song changed|restore",
        "action": "Restore last full mix; archive form experiment",
        "recipe": "parts_not_form",
    },
    {
        "match": "still pumps|reduce release|pump",
        "action": "Shorten duck release (40–80 ms)",
        "recipe": "duck_dial",
    },
    {
        "match": "not so aggressive|too aggressive|hollow",
        "action": "Lower duck amount; raise floor",
        "recipe": "duck_dial",
    },
    {
        "match": "kick cut through|prefer ducking|sidechain",
        "action": "Mild duck + kick presence",
        "recipe": "duck_mild_short",
    },
    {
        "match": "less airy|dry -|aux \\+|wet.*dry",
        "action": "Lead send dial first (dry vs plate/delay)",
        "recipe": "lead_send_dial",
    },
    {
        "match": "hard pan|wide presence|wide pad",
        "action": "Hard L/R pad + presence + HPF",
        "recipe": "pad_hardpan_wide",
    },
    {
        "match": "start on the lead|start on lead|opens on lead",
        "action": "Late arrange: cut pre-lead intro",
        "recipe": "late_arrange",
    },
    {
        "match": "speed up|few bpm|faster tempo",
        "action": "Tempo +few BPM; keep compositions",
        "recipe": "late_arrange",
    },
    {
        "match": "4\\.5|5 minute|longform|full song length",
        "action": "Longform section map on locked stems",
        "recipe": "late_arrange",
    },
    {
        "match": "as good as|we're going to get|done|final",
        "action": "FINAL LOCK — stop rework",
        "recipe": "final_lock",
    },
    {
        "match": "don't like any|do not like any|hate all",
        "action": "Shelf track; re-brief",
        "recipe": "shelf_track",
    },
    {
        "match": "too happy|too bright|too major",
        "action": "Mood lock: darken harmony/tone before more layers",
        "recipe": "mvp_pocket",
    },
    {
        "match": "muddy|cheap",
        "action": "Fix sources + subtractive EQ; simplify layers",
        "recipe": "focus_one_part",
    },
    {
        "match": "workflow|knowledge base|process",
        "action": "Update process docs only; no song work unless asked",
        "recipe": "start_song",
    },
    {
        "match": "add lead|lead next",
        "action": "D1 lead only after pocket lock",
        "recipe": "add_lead",
    },
    {
        "match": "add pad|add bed|bed next",
        "action": "D2 one bed after lead lock",
        "recipe": "add_bed",
    },
]


def match_phrase(text: str) -> list[dict[str, Any]]:
    import re

    low = text.lower().strip()
    hits: list[dict[str, Any]] = []
    for row in PHRASES:
        if re.search(row["match"], low, re.I):
            hits.append(
                {
                    "matched": row["match"],
                    "action": row["action"],
                    "recipe": row["recipe"],
                    "input": text,
                }
            )
    if not hits:
        hits.append(
            {
                "matched": None,
                "action": "Clarify phase; prefer one-focus fix; see phases/gates",
                "recipe": None,
                "input": text,
            }
        )
    return hits
