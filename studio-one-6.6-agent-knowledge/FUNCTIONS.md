# Studio One 6.6 — Function Map (agent learned)

Grounded in **Studio One 6.6 Reference Manual (EN)** via `chapters/*.md`.  
Use this as a quick ops map; open the chapter for full wording.

---

## Critical path: record MIDI into a Song

### Prerequisites (manual failure modes)
1. **Song open** (Song page).
2. **Keyboard** set up: `Options → External Devices → New Keyboard` (or predefined), **Receive From** = MIDI port that feeds notes (e.g. loopMIDI `S1 Controller 1`).
3. **Instrument Track** exists (not only an instrument in the Console).
4. Track **Input** = that Keyboard (or **All Inputs** if Keyboards exist).
5. Track **Output** = virtual instrument (Impact XT, Mojito, …) or external instrument.
6. Track is **Record-enabled** (button **red**). Without this, **no notes are recorded**.
7. **Monitor** is usually auto-on with Record Enable (turns **blue**). Configurable under Advanced/Devices.
8. Then activate **Transport Record** (`NumPad *` or Transport Record).

### Create Instrument Track
| Method | Access |
|--------|--------|
| Add Tracks dialog | **Track → Add Tracks** or **[T]** → Type **Instrument** → Count → Input Keyboard → Output New/Existing Instrument → OK |
| Quick menu | **Track → Add Instrument Track** (reliable UI path) |
| Track Column | **[Right/Ctrl]-click** blank Track Column → **Add Instrument Track** |
| Browser drop | **[F5]/[F6]** Instruments → drag instrument to **blank Arrange** → creates Track + instrument (**record+monitor on by default** per Browser chapter) |

### Record-enable (Instrument Track)
| Action | How |
|--------|-----|
| Arm | Click **Record Enable** once → **red** |
| Audio arm shortcut | Select Track + **[R]** (audio; instrument: button is specified) |
| Exclusive arm (audio) | **[Alt/Opt]+click** Record Enable → arm this, disarm others |
| Auto arm on select | Options: **Instrument Input Follows Selection** → select Instrument Track auto **Record + Monitor**, others off |
| Verify input | Play Keyboard → **Track meter moves** if note data arrives |

### Activate recording
| Mode | Access |
|------|--------|
| Manual | Transport **Record** or **[NumPad *]** — records from **cursor** to all record-enabled Tracks until Stop (**Space**) |
| Precount | Metronome Setup / **[Shift]+[C]** then Record |
| Preroll | **[O]** then Record |
| Auto Punch | Locators + **[I]** (letter i) + Record before Left Locator |
| Loop | **[NumPad /]** + Record |

### Import MIDI without real-time record (preferred handoff)
| Action | How |
|--------|-----|
| Drag MIDI | Browser **Files [F9]** → drag `.mid` to blank Arrange → **new Instrument Track** + Part |
| Onto track | Drop on existing Instrument Track → new Part |
| Still need instrument | Route Output / drag Impact/Mojito onto track to hear |

---

## External Devices (Setup)

| Type | Role | Access |
|------|------|--------|
| **Keyboard** | Plays instruments / records MIDI | External Devices → New Keyboard; Receive From / Send To; optional Default Instrument Input; Split Channels; MPE |
| **Instrument** | External MIDI sound module | New Instrument; Send To; Aux Channel for audio return |
| **Control Surface** | Mackie/HUI-class faders/transport | New Control Surface / Mackie Control; Placement for banks |
| **QWERTY Keyboard** | Computer keys as MIDI | PreSonus → QWERTY; only while UI open; only to record-enabled Instrument Tracks |

---

## Transport (Fundamentals)

| Control | Default key |
|---------|-------------|
| Play / Stop | **Space** (Stop also **NumPad 0**) |
| Record | **NumPad *** |
| Loop | **NumPad /** |
| Return to zero | **,** |
| Metronome | **C** |
| Precount | **Shift+C** |
| Preroll | **O** |
| Auto Punch | **I** |

**Retrospective Recording:** captures MIDI without pressing Record (buffer); recall **Shift+NumPad *** if enabled (Advanced/MIDI).

---

## Views / navigation

| View | Key |
|------|-----|
| Editor | **F2** |
| Console | **F3** (Small: **Shift+F3**) |
| Inspector | **F4** |
| Browser | **F5** · Instruments **F6** · Effects **F7** · Loops **F8** · Files **F9** · Pool **F10** |
| Channel / Instrument editor | **F11** / **Shift+F11** |
| Find Track / Channel | **Ctrl+Alt+T** / **Ctrl+Alt+C** |
| Command search | **Ctrl+K** |

---

## Audio Tracks (Recording)

- Create: **[T]** Type Audio, or Track → Add Audio Track mono/stereo, or Track Column right-click.
- Record Enable: button or **[R]**; exclusive **Alt+click**.
- Monitor: button **blue**; exclusive **Alt+click**.
- Input levels: set on **hardware**; clip indicator on track when armed.

---

## Editing / Arrange (high signal)

| Function | Key / access |
|----------|----------------|
| Tools 1–6 | Arrow, Range, Split, Eraser, Paint, Mute |
| Quantize | **Q** · half **Alt+Q** · restore **Shift+Q** |
| Duplicate | **D** · shared **Shift+D** · insert **Alt+D** |
| Merge | **G** |
| Bounce selection | **Ctrl+B** · to new track with inserts **Ctrl+Alt+B** |
| Crossfade | **X** |
| Pack Folder | Right-click tracks → Pack Folder |
| Arranger / Chord / Tempo / Signature | Global track buttons above Arrange |
| Bounce Instrument Part → audio | Bounce Selection |

---

## Browser load / content

| Drop target | Result |
|-------------|--------|
| Instrument → blank Arrange | New Instrument Track + device (often record+monitor on) |
| Instrument → existing Instrument Track | Replace / Combine / Keep |
| MIDI file → blank Arrange | New Instrument Track + Part |
| MIDI file → track | New Part on track |
| Effect → track/channel | Insert |
| Effect + Alt on Event | Event FX |

**Instruments:** Impact XT, Presence XT, Mai Tai, Mojito, Sample One XT, Multi Instruments (ch.18).  
Instrument Tracks **do not appear as mix channels**; instrument **audio** does in Console.

---

## Console / Mix

| Control | Key / note |
|---------|------------|
| Mute / Solo | **M** / **S** (on Instrument Track = note track, not instrument audio strip) |
| Solo Safe | **Shift+click** Solo (green) |
| Groups | **Ctrl+G** create · **Ctrl+Shift+G** dissolve |
| Export Mixdown | **Song → Export Mixdown** · **Ctrl+E** |
| Export Stems | **Song → Export Stems** |

---

## Control Link / Mackie

- Map hardware: External device → **MIDI Learn** → move controls → Assign (**Alt+M**).
- Mackie: transport, banked faders, **Rec arm**, mute, solo, V-Pots, plug-in mode (Control Link).
- Focus maps for plug-in params; track fader/pan/mute are global only.

---

## Pages

| Page | Role | Edition |
|------|------|---------|
| Start | New/Open, device config | All |
| Song | Record/edit/mix | All |
| Show | Live setlist / players | (Show features) |
| Project | Mastering / CD / loudness | **Professional** |

---

## Import / Export

| Task | Path |
|------|------|
| Import MIDI | Browser drag `.mid` into Arrange |
| Export MIDI | Right-click Part → Export Selection · drag Part to Browser · File Convert To MIDI (Song) |
| Import Song Data | Song → Import Song Data |
| Export audio | Export Selection / Mixdown / Stems |
| AAF / Zip / other DAWs | ch.21 |

---

## Automation / Spatial / Show / Video

- **Automation** (ch.14): envelopes; Write/Touch/Latch; Control Link can write during playback.
- **Spatial / Atmos** (ch.12): Professional immersive workflows.
- **Show page** (ch.13): setlist, players, performance view.
- **Video** (ch.20): video track/sync (Professional for some video features).

---

## Remote-control implications (for s1-remote)

| Manual requirement | Remote implication |
|--------------------|--------------------|
| Instrument Track must exist | UI: **Track → Add Instrument Track** (not ambiguous “Add” accelerator alone) |
| Record Enable **red** | Select track + arm (**[R]** / Record Enable / Mackie Rec) **before** Transport Record |
| Keyboard receives notes | loopMIDI Keyboard **Receive From** = note port |
| Transport Record | NumPad * / MCU Record |
| Import MIDI easier than live record | Drag `.mid` via Browser Files if UI allows |
| Meter moves = input working | Test notes only after Record/Monitor enabled |

**Order that matches the manual:**  
Create Instrument Track → set Input Keyboard + Output instrument → **Record Enable** → (optional Monitor) → **Transport Record** → play/stream MIDI → Stop.
