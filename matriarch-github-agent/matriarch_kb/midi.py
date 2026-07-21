"""MIDI CC map and SysEx parameter table (Matriarch manual 012023)."""

from __future__ import annotations

from typing import Any

# 14-bit parameters list (MSB, LSB); 7-bit have lsb=None
CC_MAP: list[dict[str, Any]] = [
    {"name": "Mod Wheel", "msb": 1, "lsb": 33, "values": "0–16383"},
    {"name": "Mod Rate", "msb": 3, "lsb": 35, "values": "0–16383"},
    {"name": "Glide Time", "msb": 5, "lsb": 37, "values": "0–16383"},
    {"name": "Arp Rate", "msb": 8, "lsb": 40, "values": "0–16383"},
    {"name": "Noise Filter Cutoff", "msb": 9, "lsb": 41, "values": "0–16383"},
    {"name": "Delay Time", "msb": 12, "lsb": 44, "values": "0–16383"},
    {"name": "Delay Spacing", "msb": 13, "lsb": 45, "values": "0–16383"},
    {"name": "Arp Swing", "msb": 14, "lsb": 46, "values": "0–16383"},
    {"name": "Arp Gate Length", "msb": 15, "lsb": 47, "values": "0–16383"},
    {"name": "Osc 2 Frequency", "msb": 16, "lsb": 48, "values": "0–16383"},
    {"name": "Osc 3 Frequency", "msb": 17, "lsb": 49, "values": "0–16383"},
    {"name": "Osc 4 Frequency", "msb": 18, "lsb": 50, "values": "0–16383"},
    {"name": "Sustain Pedal", "msb": 64, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Glide On", "msb": 65, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Arp Latch", "msb": 69, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Arp Play", "msb": 73, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Osc 1 Octave", "msb": 74, "lsb": None, "values": "0–31=16', 32–63=8', 64–95=4', 96–127=2'"},
    {"name": "Osc 2 Octave", "msb": 75, "lsb": None, "values": "0–31=16', 32–63=8', 64–95=4', 96–127=2'"},
    {"name": "Osc 3 Octave", "msb": 76, "lsb": None, "values": "0–31=16', 32–63=8', 64–95=4', 96–127=2'"},
    {"name": "Osc 4 Octave", "msb": 77, "lsb": None, "values": "0–31=16', 32–63=8', 64–95=4', 96–127=2'"},
    {"name": "Hard Sync Enable", "msb": 80, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Osc 2 Sync", "msb": 81, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Osc 3 Sync", "msb": 82, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Osc 4 Sync", "msb": 83, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Portamento Control", "msb": 84, "lsb": None, "values": "MIDI note of currently-playing note to tie to"},
    {"name": "Glide Type", "msb": 85, "lsb": None, "values": "0–42 LCR, 43–84 LCT, 85–127 EXP"},
    {"name": "Gated Glide", "msb": 86, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Legato Glide", "msb": 87, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Delay Ping Pong", "msb": 88, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Delay Sync", "msb": 89, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "Square LFO Polarity", "msb": 90, "lsb": None, "values": "0–63 Unipolar, 64–127 Bipolar"},
    {"name": "Arp Mode", "msb": 91, "lsb": None, "values": "0–42 ARP, 43–84 SEQ, 85–127 REC"},
    {"name": "Arp Pattern", "msb": 92, "lsb": None, "values": "0–42 ORDER, 43–84 FW/BW, 85–127 RANDOM"},
    {"name": "Arp Range / Bank", "msb": 93, "lsb": None, "values": "0–42=1, 43–84=2, 85–127=3"},
    {"name": "Paraphony Voice Mode", "msb": 94, "lsb": None, "values": "0–42=1v, 43–84=2v, 85–127=4v"},
    {"name": "Multi Trig", "msb": 95, "lsb": None, "values": "0–63 OFF, 64–127 ON"},
    {"name": "KB Octave", "msb": 105, "lsb": None, "values": "0–25=−2 … 102–127=+2"},
]

# MIDI implementation highlights
MIDI_IMPL = {
    "channels": "1–16",
    "note_numbers": "0–127",
    "program_change": "1–12 select saved sequences",
    "modes": ["Mode 3 Omni-Off Poly", "Mode 4 Omni-Off Mono"],
    "note_on_velocity": True,
    "channel_aftertouch": True,
    "pitch_bend": True,
    "midi_clock": {"tx": True, "rx": True},
    "start_stop": {"tx": True, "rx": True},
    "song_position_pointer": {"tx": False, "rx": True},
    "midi_tuning_standard": True,
    "manufacturer_sysex": "F0 04 17 … F7 (Moog); no public factory-cal docs",
}

# SysEx parameter IDs (decimal) from manual
SYSEX_PARAMS: dict[int, dict[str, Any]] = {
    0: {"name": "Unit ID", "values": "0–15 (default 0)"},
    1: {"name": "Tuning Scale", "values": "0–31 (0=12-TET)"},
    2: {"name": "Knob Mode", "values": "0=Snap, 1=Pass-Thru, 2=Relative (default)"},
    3: {"name": "Note Priority", "values": "0=Low, 1=High, 2=Last (default)"},
    4: {"name": "Transmit Program Change", "values": "0=Off (default), 1=On"},
    5: {"name": "Receive Program Change", "values": "0=Off, 1=On (default)"},
    6: {"name": "MIDI Input Ports", "values": "0=none, 1=DIN, 2=USB, 3=Both (default)"},
    7: {"name": "MIDI Output Ports", "values": "0=none, 1=DIN, 2=USB, 3=Both (default)"},
    8: {"name": "MIDI Echo USB In", "values": "0=Off, 1=DIN Out, 2=USB Out, 3=Both"},
    9: {"name": "MIDI Echo DIN In", "values": "0=Off, 1=DIN Out, 2=USB Out, 3=Both"},
    10: {"name": "MIDI Channel IN", "values": "0–15 = ch 1–16"},
    11: {"name": "MIDI Channel OUT", "values": "0–15 = ch 1–16"},
    12: {"name": "MIDI Out Filter - Keys", "values": "0=Off, 1=On (default)"},
    13: {"name": "MIDI Out Filter - Wheels", "values": "0=Off, 1=On (default)"},
    14: {"name": "MIDI Out Filter - Panel", "values": "0=Off, 1=On (default)"},
    15: {"name": "Output 14-bit MIDI CCs", "values": "0=Off (default), 1=On"},
    16: {"name": "Local Control: Keys", "values": "0=Off, 1=On (default)"},
    17: {"name": "Local Control: Wheels", "values": "0=Off, 1=On (default)"},
    18: {"name": "Local Control: Panel", "values": "0=Off, 1=On (default)"},
    19: {"name": "Local Control: Arp/Seq", "values": "0=Off, 1=On (default)"},
    20: {"name": "Sequence Transpose Mode", "values": "0=First note, 1=Middle C"},
    21: {"name": "Arp/Seq Keyed Timing Reset", "values": "0=Off (default), 1=On"},
    22: {"name": "Arp FW/BW Repeats", "values": "0=no end repeats, 1=repeat ends (default)"},
    23: {"name": "Arp/Seq Swing", "values": "0–16383 (8192=50% default)"},
    24: {"name": "Sequence Keyboard Control", "values": "0=Off, 1=On (default)"},
    25: {"name": "Delay Sequence Change", "values": "0=Off (default), 1=On"},
    26: {"name": "Sequence Latch Restart", "values": "0=Off (default), 1=On"},
    27: {"name": "Arp/Seq Clock Input Mode", "values": "0=Clock (default), 1=Step-Advance"},
    28: {"name": "Arp/Seq Clock Output", "values": "0=Always, 1=Only When Playing (default)"},
    29: {"name": "Arp MIDI Output", "values": "0=Off, 1=On (default)"},
    30: {"name": "Send MIDI Clock", "values": "0=Off (default), 1=When Playing, 2=Always"},
    31: {"name": "Send MIDI Start/Stop", "values": "0=Off (default), 1=On"},
    32: {"name": "Follow MIDI Clock", "values": "0=Off, 1=On (default)"},
    33: {"name": "Follow MIDI Start/Stop", "values": "0=Off, 1=On (default)"},
    34: {"name": "Follow Song Position Pointer", "values": "0=Off, 1=On (default)"},
    35: {"name": "Clock Input PPQN Index", "values": "0–15 (default 3 = 4 PPQN)"},
    36: {"name": "Clock Output PPQN Index", "values": "0–15 (default 3 = 4 PPQN)"},
    37: {"name": "Pitch Bend Range (semitones)", "values": "0–12 (default 2)"},
    38: {"name": "Keyboard Octave Transpose", "values": "0–4 = −2…+2 (default 2)"},
    39: {"name": "Delayed KB Octave Transpose", "values": "0=Off, 1=On (default)"},
    40: {"name": "Glide Type", "values": "0=LCR, 1=LCT, 2=EXP (default LCR)"},
    41: {"name": "Gated Glide", "values": "0=Off, 1=On (default)"},
    42: {"name": "Legato Glide", "values": "0=Off, 1=On (default 1 in sysex table)"},
    43: {"name": "Osc 2 Freq Knob Range", "values": "0–24 st (default 7)"},
    44: {"name": "Osc 3 Freq Knob Range", "values": "0–24 st (default 7)"},
    45: {"name": "Osc 4 Freq Knob Range", "values": "0–24 st (default 7)"},
    46: {"name": "Hard Sync Enable", "values": "0=Off, 1=On"},
    47: {"name": "Osc 2 Hard Sync", "values": "0/1"},
    48: {"name": "Osc 3 Hard Sync", "values": "0/1"},
    49: {"name": "Osc 4 Hard Sync", "values": "0/1"},
    50: {"name": "Delay Ping Pong", "values": "0/1"},
    51: {"name": "Delay Sync", "values": "0/1"},
    52: {"name": "Delay Filter Brightness", "values": "0=Dark, 1=Bright (default)"},
    53: {"name": "Delay CV Sync-Bend", "values": "0=Off (default), 1=On"},
    54: {"name": "Tap-Tempo Clock Division Persistence", "values": "0=Off (default), 1=On"},
    55: {"name": "Paraphony Mode", "values": "0=Mono, 1=Duo, 2=Quad"},
    56: {"name": "Paraphonic Unison", "values": "0=Off (default), 1=On"},
    57: {"name": "Multi Trig", "values": "0=Off (default), 1=On"},
    58: {"name": "Pitch Variance", "values": "0–400 (±40 cents in 0.1 cent steps)"},
    59: {"name": "KB CV OUT Range", "values": "0=−5…+5, 1=0…10"},
    60: {"name": "Arp/Seq CV OUT Range", "values": "0=−5…+5, 1=0…10"},
    61: {"name": "KB VEL OUT Range", "values": "0=0…5, 1=0…10"},
    62: {"name": "Arp/Seq VEL OUT Range", "values": "0=0…5, 1=0…10"},
    63: {"name": "KB AT OUT Range", "values": "0=0…5, 1=0…10"},
    64: {"name": "MOD WHL OUT Range", "values": "0=0…5, 1=0…10"},
    65: {"name": "KB GATE OUT Range", "values": "0=+5, 1=+10"},
    66: {"name": "Arp/Seq GATE OUT Range", "values": "0=+5, 1=+10"},
    67: {"name": "Round-Robin Mode", "values": "0=Off, 1=First-Note Reset (default), 2=On"},
    68: {"name": "Restore Stolen Voices", "values": "0=Off (default), 1=On"},
    69: {"name": "Update Unison on Note-Off", "values": "0=Off (default), 1=On"},
    70: {"name": "Mod Osc Square Polarity", "values": "0=Unipolar, 1=Bipolar (default)"},
    71: {"name": "Noise Filter Cutoff", "values": "0–16383"},
    72: {"name": "Arp/Seq Random Repeats", "values": "0=no adjacent repeats, 1=allow (default)"},
    73: {"name": "ARP/SEQ CV OUT Mirrors KB CV", "values": "0=Off (default), 1=On"},
    74: {"name": "KB CV OUT Mirrors ARP/SEQ CV", "values": "0=Off (default), 1=On"},
}

SYSEX_SET = (
    "F0 04 17 23 [param_id] [value_MSB] [value_LSB] 00 00 00 00 00 00 00 00 [unit_id] F7"
)
SYSEX_GET = "F0 04 17 3E [param_id] 00 00 00 00 00 00 00 00 00 00 [unit_id] F7"
# value encoding: if v < 128 → MSB=0 LSB=v; else MSB=v//128 LSB=v%128
# unit_id 0x7F addresses all; reply messages set byte before unit_id to 1


def lookup_cc(query: str) -> list[dict[str, Any]]:
    q = query.lower()
    hits = [c for c in CC_MAP if q in c["name"].lower() or q == str(c["msb"])]
    if q.isdigit():
        n = int(q)
        hits = [c for c in CC_MAP if c["msb"] == n or c.get("lsb") == n]
    return hits


def lookup_sysex(param_id: int | str) -> dict[str, Any] | None:
    if isinstance(param_id, str) and not param_id.isdigit():
        q = param_id.lower()
        for pid, meta in SYSEX_PARAMS.items():
            if q in meta["name"].lower():
                return {"id": pid, **meta}
        return None
    pid = int(param_id)
    meta = SYSEX_PARAMS.get(pid)
    return {"id": pid, **meta} if meta else None


def encode_sysex_value(value: int) -> tuple[int, int]:
    if value < 128:
        return 0, value
    return value // 128, value % 128


def build_set_sysex(param_id: int, value: int, unit_id: int = 0x7F) -> list[int]:
    msb, lsb = encode_sysex_value(value)
    return [
        0xF0,
        0x04,
        0x17,
        0x23,
        param_id & 0x7F,
        msb & 0x7F,
        lsb & 0x7F,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        unit_id & 0x7F,
        0xF7,
    ]
