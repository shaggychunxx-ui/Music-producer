# Studio One 6.6 — Agent ops learned (live session)

**Date:** 2026-07-24  
**Sources:** Reference Manual chapters + live walk on Windows with s1-remote  
**Priority:** Keyboard → MIDI (MCU / Notes) → User mouse  

This file is **operational memory** for agents. Manual text remains in `chapters/`. Function map: `FUNCTIONS.md`. Walk catalog: `MANUAL_WALKTHROUGH_CATALOG.md`.

---

## Control split (hard rules)

| Job | Port / method | Do not |
|-----|----------------|--------|
| Transport, faders, mute/solo/select, banks | MCU on **S1 Controller** | Send instrument notes on MCU |
| Live Instrument Track notes / record | **S1 Notes** → Keyboard Receive From | Use MCU out for musical notes |
| Views, arm `[R]`, save, tools | Keyboard to focused S1 window | Assume MCU select = Arrange track |
| Load VST / Browser drag | **User mouse** | Trust `browser_load` as real assign |

---

## Song page only

- Agent work requires an open **Song** (not Start page).
- Typing on Start can open/search wrong songs (e.g. instrument names as titles).
- Stay on Song page before any type/search.

---

## Tracks

| Op | Working method |
|----|----------------|
| Add Instrument Track | Menu UIA: **Track → Add Instrument Track** (not `T` dialog hacks) |
| Instruments on track | User Browser-drags Impact / Mojito / etc. |
| Track numbering (user) | Track 1, 2, 3… (1-based) |
| MCU strip index | Often 0-based; **strip ≠ guaranteed Arrange track** |

---

## Record Enable (arm) — critical

From manual **Recording** chapter + live failures:

1. Select the **correct Arrange Instrument Track**.
2. **Record Enable** must be **red** before Transport Record.
3. Shortcut: select track + **`[R]`** — **this is a TOGGLE**.
4. Monitor usually follows arm (blue).
5. Exclusive arm: **Alt+click** Rec (mouse).
6. Optional: **Instrument Input Follows Selection** auto-arms selected instrument track.

### Failure modes observed live

| Mistake | Result |
|---------|--------|
| Press `[R]` or MCU rec when already armed | **Disarms** track |
| MCU `rec_arm(strip)` only | May **not** light Arrange Rec on instrument tracks |
| Toggle “clear” arm on another track | Arms empty track or steals arm |
| Stream MIDI with Rec grey | Transport runs; **no part** (or wrong track) |
| Claim `note_ons` from stream log | **≠** clip on instrument track — UI verify required |

### Agent policy (current)

- Prefer **user mouse-arms** Rec red on the target track, then agent: rewind → Transport Record → stream on **S1 Notes** only.
- If agent arms: **one** select + **one** `[R]` (or one Rec click), screenshot-verify red, **never** multi-toggle.
- Mid-stream: **no** `[R]`, **no** MCU rec toggle, **no** arming other tracks.
- Do not create empty tracks and stream into them.

---

## Live MIDI record path

1. loopMIDI: **S1 Controller** (MCU) + **S1 Notes** (notes).
2. External Devices: Mackie on Controller; **Keyboard Receive From = S1 Notes 1**.
3. Agent out: **S1 Notes 2** (`instrument_midi_out_port`).
4. Track Input = Keyboard; Output = instrument (user-loaded).
5. Rec **red** on that track only.
6. Transport Record → stream notes → Stop.
7. **User confirms** MIDI part on the right track.

### Preferred non-realtime handoff

Browser **Files** or **Song → Import File** drag/import `.mid` onto the instrument track (still needs instrument to hear).

---

## What automation can / cannot do

| Can (agent) | Cannot reliably (need user) |
|-------------|------------------------------|
| Views F2–F10, tools, save, undo | Browser **drag** instrument/FX |
| MCU transport/mix | Exclusive Alt+click arm without mouse |
| Menu Add Instrument Track | Confirm Rec red without vision/screenshot |
| Stream on S1 Notes | Guarantee MCU strip maps to Arrange track N |
| Screenshot watch | Pro-only pages if edition lacks them |

---

## Manual walk scores (2026-07-24)

| Run | Result |
|-----|--------|
| Light walk | 23 OK |
| Full ch.1–22 ops | 86 OK / ~32 user or fail |
| Missed follow-up | +19 OK (S1 Notes stream, menus) |
| Remaining | Drag VST, global tracks, some Pro UI |

Reports: `FULL_MANUAL_WALK_REPORT.md`, `MANUAL_MISSED_REPORT.md`, `MANUAL_WALK_SUMMARY.md`.

---

## Cross-repo

| Repo | Role |
|------|------|
| **Music-producer** `studio-one-6.6-agent-knowledge/` | Manual extract + this ops memory |
| **Studio-One** (s1-remote) | Runtime control code + `docs/` walk + `S1_NOTES_PORT_SETUP.md` |
