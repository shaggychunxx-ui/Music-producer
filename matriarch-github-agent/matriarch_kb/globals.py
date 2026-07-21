"""Global Settings access and keyboard parameter map."""

from __future__ import annotations

from typing import Any

ACCESS_HOWTO = """
Enter Global Settings:
  1. Hold HOLD [SHIFT] on the Left-Hand Controller.
  2. Hold OSC 1 SYNC ENABLE until it blinks.
  3. Use black keys to select parameters (and upper black keys for groups).
  4. Use white keys to set values.
  5. Press SYNC ENABLE to exit (or double-tap a white key to set + exit).

Organization:
  - Groups of 10 parameters.
  - Default group (0): lower black keys C#0…A#1 alone.
  - Other groups: hold group select black key (from C#2) + parameter black key.
  - Settings persist through power cycle.
"""


def access_globals_howto() -> str:
    return ACCESS_HOWTO.strip()


GLOBAL_GROUPS: dict[str, list[dict[str, Any]]] = {
    "0": [
        {
            "id": "0.1",
            "name": "Note Priority",
            "key": "C#0",
            "blinks": 1,
            "options": {"C0": "LOW", "D0": "HIGH", "E0": "LAST"},
            "default": "LAST",
        },
        {
            "id": "0.2",
            "name": "Glide Type",
            "key": "D#0",
            "blinks": 2,
            "options": {"C0": "LCR", "D0": "LCT", "E0": "EXP"},
            "default": "LCR",
            "notes": "LCR=linear constant rate; LCT=constant time; EXP=exponential",
        },
        {
            "id": "0.3",
            "name": "Gated Glide",
            "key": "F#0",
            "blinks": 3,
            "options": {"C0": "OFF", "D0": "ON"},
            "default": "ON",
        },
        {
            "id": "0.4",
            "name": "Pitch Bend Range",
            "key": "G#0",
            "blinks": 4,
            "values": "0–12 semitones via white keys C0…A1",
            "default": "2 semitones (E0)",
        },
        {
            "id": "0.5",
            "name": "Pitch Variance",
            "key": "A#0",
            "blinks": 5,
            "values": "0–40 cents in ~1.4 cent steps (C0…C4)",
            "default": "0",
        },
        {
            "id": "0.6",
            "name": "Osc Frequency Knob Range",
            "key": "C#1",
            "blinks": 6,
            "values": "0–24 semitones (C0…F3)",
            "default": "7 (perfect fifth)",
        },
        {
            "id": "0.7",
            "name": "Square LFO Polarity",
            "key": "D#1",
            "blinks": 7,
            "options": {"C0": "Unipolar", "D0": "Bipolar"},
            "default": "Bipolar",
        },
        {
            "id": "0.8",
            "name": "Noise Filter Cutoff",
            "key": "F#1",
            "blinks": 8,
            "values": "HPF dark→bright C0…C4",
            "default": "lowest (C0)",
        },
        {
            "id": "0.9",
            "name": "Delay Filter Brightness",
            "key": "G#1",
            "blinks": 9,
            "options": {"C0": "Dark", "D0": "Bright"},
            "default": "Bright",
        },
        {
            "id": "0.10",
            "name": "Delay Sync CV Bend",
            "key": "A#1",
            "blinks": 10,
            "options": {"C0": "OFF", "D0": "ON"},
            "default": "OFF",
            "notes": "ON: TIME CVs bend ±33% of sync tempo; OFF: TIME CVs select divisions",
        },
    ],
    "1": [
        {"id": "1.1", "name": "MIDI Input Channel", "group_key": "C#2", "param_key": "C#0"},
        {"id": "1.2", "name": "MIDI Output Channel", "group_key": "C#2", "param_key": "D#0"},
        {"id": "1.3", "name": "MIDI Echo (USB)", "group_key": "C#2", "param_key": "F#0"},
        {"id": "1.4", "name": "MIDI Echo (DIN)", "group_key": "C#2", "param_key": "G#0"},
        {"id": "1.5", "name": "MIDI Clock Input", "group_key": "C#2", "param_key": "A#0"},
        {"id": "1.6", "name": "MIDI Clock Output", "group_key": "C#2", "param_key": "C#1"},
        {"id": "1.7", "name": "Local Control (Keyboard)", "group_key": "C#2", "param_key": "D#1"},
        {"id": "1.8", "name": "Local Control (Arp/Seq)", "group_key": "C#2", "param_key": "F#1"},
        {"id": "1.9", "name": "Receive Program Change", "group_key": "C#2", "param_key": "G#1"},
        {"id": "1.10", "name": "Send Program Change", "group_key": "C#2", "param_key": "A#1"},
    ],
    "2": [
        {"id": "2.1", "name": "Arp/Seq Clock Input Mode", "notes": "Clock vs Step-Advance"},
        {"id": "2.2", "name": "Arp/Seq Clock Output", "notes": "Always vs Only When Playing"},
        {"id": "2.3", "name": "Arp/Seq MIDI Output"},
        {"id": "2.4", "name": "Sequencer Transpose Mode", "notes": "First note vs Middle C"},
        {"id": "2.5", "name": "Sequence Keyboard Control"},
        {"id": "2.6", "name": "Sequence Keyed Restart"},
        {"id": "2.7", "name": "Arp/Seq Keyed Timing Reset"},
        {"id": "2.8", "name": "FW/BW Repeat"},
        {"id": "2.9", "name": "Delay Sequence Change"},
        {"id": "2.10", "name": "Arp/Seq Swing", "values": "22%–78% (50% default; 66% triplet feel)"},
    ],
    "3": [
        {"id": "3.1", "name": "Clock Input PPQN", "values": "1,2,3,4,5,6,7,8,9,10,11,12,24,48 (default 4)"},
        {"id": "3.2", "name": "Clock Output PPQN", "values": "same as input (default 4)"},
        {"id": "3.3", "name": "KB CV OUT Range", "values": "−5…+5 or 0…+10"},
        {"id": "3.4", "name": "Arp/Seq CV OUT Range"},
        {"id": "3.5", "name": "KB VEL OUT Range", "values": "0…+5 or 0…+10"},
        {"id": "3.6", "name": "Arp/Seq VEL OUT Range"},
        {"id": "3.7", "name": "KB AT OUT Range"},
        {"id": "3.8", "name": "MOD WHL OUT Range"},
        {"id": "3.9", "name": "KB GATE OUT Range", "values": "+5 or +10"},
        {"id": "3.10", "name": "Arp/Seq GATE OUT Range"},
    ],
    "4": [
        {"id": "4.1", "name": "Delayed Keyboard Octave Shift"},
        {"id": "4.2", "name": "Round-Robin Mode", "values": "Off / On with Reset / On"},
        {"id": "4.3", "name": "Paraphonic Unison"},
        {"id": "4.4", "name": "Update Unison on Note-Off"},
        {"id": "4.5", "name": "Restore Stolen Voices on Note-Off"},
        {"id": "4.6", "name": "Tuning Scale Select", "values": "0–28 (0=12-TET permanent)"},
        {"id": "4.7", "name": "Sequence Random Repeat"},
        {"id": "4.8", "name": "MIDI OUT Filter - Panel Knobs"},
        {"id": "4.9", "name": "MIDI OUT Filter - Pitch/Mod Wheels"},
        {"id": "4.10", "name": "MIDI OUT Filter - Keys"},
    ],
    "5": [
        {"id": "5.1", "name": "ARP/SEQ CV OUT Mirrors KB CV"},
        {"id": "5.2", "name": "KB CV OUT Mirrors ARP/SEQ CV"},
        {"id": "5.3", "name": "MIDI Velocity Curves", "values": "BASE / LINEAR / HARD / SOFT"},
    ],
    "10": [
        {
            "id": "10.1",
            "name": "Load Default Settings",
            "how": "Hold A#3 + press C#0; LHC buttons blink; exits Global mode",
        },
        {
            "id": "10.2",
            "name": "Show Firmware Version",
            "how": "Hold A#3 + press D#0; PLAY=major, HOLD=minor, TAP=patch blink counts",
        },
    ],
}

MIDI_TUNING = {
    "supports": [
        "Bulk Tuning Dump (128-note scales)",
        "Single-Note Tuning",
        "Scale/Octave Types 5, 6, 8, 9 (1-byte and 2-byte)",
    ],
    "tools": ["Scala", "Moog Phatty Tuner"],
    "spec": "MIDI 1.0 Detailed Specification / MIDI Tuning Standard (midi.org)",
}
