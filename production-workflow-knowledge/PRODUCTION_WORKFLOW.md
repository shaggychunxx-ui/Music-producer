# Studio production workflow (standing rules)

These rules apply to **every** song. They exist so we do not thrash: many full-song rewrites, no locked foundation, complexity before quality.

**Standing rules are song-agnostic.** Per-song status, masters, and decisions live only in that song’s `NOTES.txt` / `GATES.txt` — not in this file.

**Core idea:** *Ship a simple song that sounds good, then add complexity only after the user approves each layer.*

**Second idea:** *Technique follows order. The right tool at the wrong stage still fails.*

**Third idea:** *Producer temperature changes per task* — analytical work stays cool; creative humanize runs hot only when the foundation is locked (see §11).

---

## 0. Lessons (why this process exists)

| Failure mode | Rule that prevents it |
|--------------|------------------------|
| Full song + poly + automation + new voices in one shot | **MVP first** (drums + bass only) |
| 5+ full masters without locking anything | **Approval gates** — stop and wait |
| “Muddy/cheap” fixed by more processing only | **Fix sources first**, then mix |
| Temp 10 + dense arrangement from bar 1 | **Temp 6–7 until foundation locked** |
| Agent keeps rewriting when user dislikes *everything* | **Shelf the track**; reset brief |
| Skipping pro mix path | **Signal flow 1–8** on every master |
| Masking fights between bass and kick / lead and pad | **Frequency ownership** + one mid hero |
| Over-limiting early | **Headroom first**, loudness last |
| User asked for **part** organization; agent rewrote **form** | **§21 Parts ≠ arrangement** — never rewrite form unless asked |
| Aggressive sidechain “pump” after kick cut-through | **Mild duck first**; **release** controls pump tail (§19.3) |
| Too happy / major / bright on a dark ref | **Mood lock in brief** — mode, color tones, lead leap limits |
| Full-song rewrite when only length/tempo/start is wrong | **Late arrange on locked stems** (§21) — don’t recompose |
| GATES.txt left unchecked after user approvals | **Update GATES + NOTES on every lock** |

Tracks improve with **one voice at a time**, locked stems, and **late form only after mix lock**. That is required.

---

## 1. Full pipeline map

```
A  Brief + reference analysis (+ ref fingerprint file) + mood lock
B  Arrangement sketch (form, contrast, mute map, frequency owners)
C  MVP: drums + bass (Temp 6–7) — kick/bass as one system
D  Gate: user approves pocket
E  Add ONE part at a time (lead → bed → color)
F  Full mix: signal flow stages 1–8 + stereo discipline
   (kick cut-through: prefer mild duck + kick presence — §19.3)
G  Automation (musical moves) — after static mix works
H  QC / A-B / mono / translation / version archive
I  Optional: late form pass on LOCKED stems only (length, start bar, tempo, section map) — §21
J  Optional Studio One final 10% polish
K  FINAL lock when user is done (“as good as we’ll get”) — stop rework
```

Detail and **techniques for each step** follow.  
§19 excellence · §20 voice match · **§21 parts vs arrangement / longform** · **§22 phrase book**.

---

## 2. Phase A — Brief & reference (before any MIDI)

Do **not** compose until the brief is clear.

### A1. Reference (required)

| Step | Process | Techniques |
|------|---------|------------|
| Get reference | Title + artist, or user plays → capture | WASAPI loopback on **Realtek** (`record_system_audio.py`, default `--device Realtek` — not Display Audio/HDMI), 45–60 s, peak ≈ −1 to −6 dBFS (not silent, not clipped). Windows Output should be Speakers (Realtek) so you hear the bus we capture. |
| Fingerprint | Measure, log to notes | Peak, RMS, **crest** (peak−RMS), band energy (sub / low / lowmid / mid / himid / high / air), tempo estimate, rough key/mode if known |
| Listen goals | Name 3–5 attributes to chase | e.g. “dry kick”, “round bass”, “wide pad”, “short room”, “not much air” |
| Non-goals | Explicitly list what *not* to clone | Melody, lyrics, signature riff — **fingerprint only**, original composition |

### A2. Scope (required)

Agree:
- Genre / uniqueness vs prior songs  
- **Mood lock** — dark/minor vs bright/major; lead leap limits (§21.4)  
- **Temp policy** — per task (MVP compose **7**, mix/QC **2–3**; see §11). User may override for a single task.  
- **Complexity budget** (S / M / C — default **S**)  
- Success criteria in plain language  
- Target length if known (demo vs **~4.5–5 min** full song) — form detail can wait until after mix lock

### A3. Sound plan (before render)

| Role | Plan | Technique |
|------|------|-----------|
| Kick/snare | Multi-vel samples preferred | Match ref weight: sub kick vs click |
| Bass | Multi-sample and/or factory bass PC | Decide who owns **50–80 Hz** (kick vs bass) |
| Lead | Factory lead / hybrid | Owns presence (~1–5 kHz); HPF mud |
| Beds | One type first | High-pass; stay out of lead/bass mid |

Prefer: multi-samples → Surge MIDI Programs → hybrid with clear frequency jobs → hand-init last.

**Voice matching to reference:** see **§20** (timbre brief, sample vs synth path, A/B solo).

**Stop gate A:** User confirms brief (or “proceed”).

---

## 3. Phase B — Arrangement sketch (lightweight, pre-render)

Often skipped; skipping causes muddy “everything always on” tracks.

| Step | Process | Techniques |
|------|---------|------------|
| Form | Map bars: intro / A / B / break / outro | Even short MVP: 32–48 bars is enough |
| Density map | Which parts play when | Intro: kick+hat or bass only; drop: full; break: pull drums |
| Frequency map | Who owns which band | Kick sub · bass low-mid definition · lead mid/high · beds high or very low |
| Contrast | Loud vs thin sections | Arrangement creates impact more than limiting |

**Do not** write poly ostinatos or automation maps until MVP is approved (unless complexity budget is already C **and** user insisted — still prefer MVP first).

---

## 4. Phase C — MVP song (minimum viable product)

### C1. Compose only the core

**Allowed:** drums (kick, snare/clap, simple hats) + bass.  
**Forbidden in MVP:** lead, poly, pads, stabs, FX, heavy automation.

| Role | Techniques |
|------|------------|
| **Kick** | On 1 & 3 (or genre pattern); leave **sidechain space** for bass (not both full on every 16th) |
| **Snare/clap** | 2 & 4 (or genre); consistent velocity band |
| **Hats** | 8ths first; 16ths only if still clean |
| **Bass** | Lock to kick pattern; shorter notes reduce mud; root movement clear |
| **Temp** | **6–7**: light swing, small timing/velocity variance — not T10 chaos |

### C2. Dry render (signal flow stage 1)

| Process | Techniques |
|---------|------------|
| Gain staging | Peak-safe stems ≈ **−6 to −3 dBFS** peaks; no inter-sample clipping |
| Sources | Multi-vel where possible; factory PCs via `program_change` |
| No creative FX | No insert reverb/delay/chorus “for vibe” on dry stems |
| Mono low | Kick/bass essentially mono below ~80–100 Hz |

### C3. MVP mix (abbreviated signal flow)

For MVP only: stages **2 → 3 → 4 → light 8** (skip fancy multi-send design until more parts exist).

| Stage | Techniques for MVP |
|-------|-------------------|
| **Faders** | Static balance first. Kick/snare pocket; bass under kick punch but audible. Sum peak ≈ **−6 dBFS** before limiting |
| **EQ** | HPF hats; cut boxiness ~200–400 on kit if needed; bass: cut mud ~200–300, maybe small definition ~800–1k; **kick vs bass carve** (e.g. kick 50–60, bass 80–100 or reverse by genre) |
| **Dynamics** | Gentle kit bus or kick/snare; bass compressor medium ratio, medium attack so transient lives |
| **Master** | Only enough level to listen vs ref; crest should still feel open |

**Stop gate C (MVP):** `Desktop\*_MVP_Master.wav`  
Ask: *drums? bass? pocket?* — **wait**.  
Do not add lead until core is OK or user names a fix.

---

## 5. Complexity budget

| Level | Contents | When allowed |
|-------|----------|--------------|
| **S — Simple (default)** | Drums + bass → then +1 lead | Always start here |
| **M — Medium** | + one bed (pad **or** pluck), light shared space | After S approved |
| **C — Complex** | Polyrhythms, heavy automation, many layers | User **asks** + S/M already clean |

---

## 6. Phase D — Add one layer at a time

| Step | Add | Techniques | Gate |
|------|-----|------------|------|
| **D1 Lead** | Main melody/hook | Own 1–5 kHz; HPF ≤150–250 Hz; leave bass mud region alone; short musical delay **on send** later | User OK? |
| **D2 One bed** | Pad **or** arp/pluck | HPF high; low level; duck under kick/bass if competing | User OK? |
| **D3 Color** | Stabs / FX / 2nd bed | Sparse hits; not continuous mid wash | User OK? |
| **D4 Complex** | Poly rhythms, rides, gates | Only if mix is already clear | User OK? |

### Voice focus rule (named part)

1. Lock other **dry** stems.  
2. Re-render **only** that source (better sample/patch/layer).  
3. Re-run stages **2→8**.  
4. One Desktop master → *better / worse / next?*  

**Never** rebuild every instrument because one part is wrong.

---

## 7. Signal flow stages 1–8 (full mix) — process & techniques

Helpers: `Songs\_studio_lib\signal_flow.py`

### Stage 1 — Dry sources

| Process | Techniques |
|---------|------------|
| Render | Peak-safe; consistent SR (48 kHz) |
| Quality | Multi-sample / factory first |
| Hybrids | Split jobs: e.g. Digi = &lt;100 Hz only; finger sample = 100 Hz–2 kHz definition |
| Cheap fix | Change patch/library — **not** more saturation/reverb |

### Stage 2 — Fader balance (static mix)

| Process | Techniques |
|---------|------------|
| Order | Often: drums → bass → lead → beds → FX (or reverse for vocal music) |
| Method | **Faders only** first — no EQ/comp yet if possible; if already lightly EQ’d, still set relative levels |
| Headroom | Mix bus peaks roughly **−6 dBFS** before heavy processing |
| Hierarchy | If everything is loud, nothing is important — carve level first |
| Mute test | Mute lead: groove must still work. Mute bass: kick must still work |

### Stage 3 — Cleanup EQ (subtractive first)

| Process | Techniques |
|---------|------------|
| HPF | Every non-bass/kick track: remove unused low (hats 200–400+, pads 120–250+, lead 150–250+) |
| Mud | 200–500 Hz: cut on competing tracks; keep on **one** body instrument |
| Boxiness | ~300–500 kit/guitars |
| Harshness | 2.5–5 kHz cuts if brittle |
| Air | Shelf only after mud is gone; don’t fake “pro” with only +air |
| Masking | Boost on one track ≈ cut on the one that fights it |
| Tool order | Cut first, small Q for musical cuts; narrow Q for resonances |

### Stage 4 — Dynamics (selective)

| Process | Techniques |
|---------|------------|
| When | Control peaks / glue — not to “make it loud” |
| Kick/snare | Medium attack so click remains; medium release to tempo |
| Bass | Faster attack if needed for evenness; leave some movement |
| Lead | Gentle leveling; don’t squash expression |
| Parallel | Optional punch bus (heavy comp, blend low) on drums |
| Avoid | Compressor on every track at high ratio |

### Stage 5 — Shared FX sends (space & depth)

| Process | Techniques |
|---------|------------|
| Architecture | **Sends → returns**, not unique hall on every channel |
| Typical set | (1) Short room/drums (2) Longer plate/hall (3) One tempo delay (e.g. 1/8 or dotted 1/8) |
| Pre-EQ wet | HPF and often LPF on send so mud/hiss don’t fill the verb |
| Depth | Dry = front (lead/kick); wetter = farther (pads) |
| Genre | Dance/house: drier than ambient; match ref wetness by ear + A/B |
| Level | Returns sit under dry; if verb is obvious first, it’s usually too loud |
| **Lead wet/dry dial** | User often wants **air on the send**, not a wetter dry stem. Prefer: keep dry lead, ride **plate/delay send ±3 dB**. “Less airy” → cut send first, then dry level. “Dry −3 / aux +3” is a valid one-move pass — do **only** that.

### Stage 6 — Groups / buses

| Bus | Techniques |
|-----|------------|
| **Drums** | Light glue comp; mono low; optional parallel punch |
| **Bass** | Mono; little or no reverb; lock with kick (sidechain/duck beds not bass into mud) |
| **Music** | Pads/plucks/stabs; duck under kick+bass envelope |
| **Lead** | Slight forward fader; delay/plate already on sends |
| **Returns** | Treat as instruments in the balance |

### Stage 7 — Mix bus (glue only)

| Process | Techniques |
|---------|------------|
| Light EQ | Tiny tilt toward ref (sub, mud cut, presence) — **not** a second master chain |
| Glue comp | Low ratio (~1.3–1.5:1), slowish attack, preserve crest |
| Mono below | ~80–100 Hz |
| Check | Crest still healthy vs reference (often ~9–13 for many pop/electronic masters) |

### Stage 8 — Master last

| Process | Techniques |
|---------|------------|
| Loudness | Match ref RMS **approximately**; sit slightly under if needed for crest |
| Limiter | Ceiling only (−0.3 to −1 dBTP class of thinking); if it pumps, **turn down into limiter** |
| Never | Use master limiting to hide a bad balance |
| Deliver | Desktop master + optional named archive master in project |

---

## 8. Phase E — Automation (after static mix works)

Automation is **arrangement in time**, not a fix for bad faders.

| Type | Techniques | When |
|------|------------|------|
| Level rides | Verse down, chorus up; lead phrases | After static balance OK |
| Mute/gates | Dropouts for impact | User wants drama |
| Filter | Build-ups; keep subtle unless genre is filter-house | Complexity M/C |
| Send rides | Delay throws on last words/notes; verb up in breaks | After sends exist |
| Pan | Slow moves for FX/perc — not bass/kick | Sparse |

**Temp 10 humanize** of MIDI can come **after** Temp 7 foundation is approved — not before.

---

## 9. Phase F — QC & A/B (before calling done)

| Check | Techniques |
|-------|------------|
| **A/B vs ref** | Level-match roughly; switch every 5–10 s; compare kick weight, bass note length, verb amount, brightness |
| **Bands** | Sub not empty; lowmid not a wall; air not fizzy vs ref |
| **Mono** | Sum to mono: kick+bass still solid; no total phase wipeout |
| **Mute tests** | Solo-free: does groove stand without lead? Does lead sit without pad? |
| **Translation** | If possible, quick listen on phone/laptop speaker — bass still defined, not only sub |
| **Fatigue** | If many passes: take a break; don’t chase loudness |

---

## 10. Instrument quality bar (recap)

1. Multi-sample libraries (multi-velocity)  
2. Surge XT MIDI Programs + `program_change`  
3. Hybrid layers **with split frequency jobs**  
4. Hand-init synth last / FX only  

**Anti-mud / anti-cheap:**
- One mid hero at a time  
- Beds HPF’d; mono sub  
- Cheap → **new source**, not more plugins  

---

## 11. Producer temperature (per task)

Temperature is **not one global knob** for the whole song.  
It is the **amount of creative variance / humanize / risk** allowed for *this* job.

Scale **1–10** (maps to humanize `T = temp/10` in MIDI scripts when applicable):

| Temp | Character |
|------|-----------|
| **1–3** | Surgical, deterministic, A/B-driven — almost no random humanize |
| **4–5** | Controlled — light musical choices, tight grid |
| **6–7** | **Default production pocket** — natural feel, still tight |
| **8–9** | Expressive — more swing, velocity, timing life |
| **10** | Max humanize / bold remix energy — **only after foundation approved** |

### 11.1 Default temp by task

| Task | Temp | Why / how to work |
|------|------|-------------------|
| **Reference capture** | **1** | No creativity — clean loopback, verify levels |
| **Reference analysis / fingerprint** | **1–2** | Measure peak/RMS/crest/bands/tempo; log facts |
| **Brief / genre / sound plan** | **3–4** | Clear decisions; one genre proposal if needed |
| **Arrangement sketch** (form, density map) | **4–5** | Structure first; no wild fills yet |
| **MVP compose** (drums + bass MIDI) | **6–7** | Default **7** — pocket without T10 chaos |
| **MVP dry render + simple mix** | **2–3** | Repeatable sources; faders/EQ by craft not luck |
| **Signal flow stages 2–8** (balance, EQ, dyn, sends, master) | **2–3** | Engineering discipline; match ref meters |
| **Add lead** (compose) | **6–7** | Melodic but still grid-aware until approved |
| **Add bed / pluck / stab** | **5–6** | Supportive; less variance than lead |
| **Voice focus re-render** (user named one part) | **3–5** | Improve source quality; small feel tweaks only |
| **Humanize pass** (after pocket approved) | **8–10** | User-requested or post-approval “bring life” |
| **Full Temp-10 creative remix** | **10** | Only if user asks **and** S foundation is locked |
| **Polyrhythm / heavy automation design** | **5–7** compose, **2–3** mix | Ideas at mid temp; execute automation curves cleanly |
| **QC / A-B / mono / shelf decision** | **1–2** | Honest listen; no “fix with more sauce” |
| **Workflow / docs / planning** | **2–3** | Precise process, not freeform invention |

### 11.2 Rules

1. **State the temp** when starting a task (in log or script header: `TEMP = 7`).
2. **Do not** run capture, mix engineering, or QC at Temp 8–10.
3. **Do not** compose MVP drums/bass at Temp 10 unless user explicitly overrides.
4. If user says **“Temp N”**, that overrides the table for that task only (not forever).
5. Raising temp later = **new humanize pass** on locked MIDI/arrangement — not redoing voices from scratch unless asked.
6. Scripts should take `TEMP` as a constant or CLI so per-task values are explicit.

### 11.3 Agent behavior

| Situation | Temp behavior |
|-----------|----------------|
| New song first MVP | **7** for MIDI; **2–3** for render/mix |
| User: “more human / looser / Temp 10” | Raise **humanize only** after confirming pocket OK |
| User: “muddy / fix mix / fix bass sound” | Drop to **2–4** — surgical source + EQ, not more random timing |
| User: “I don’t like any of it” | **1–2** — stop, shelf, re-brief; no hot creative thrash |

---

## 12. Feedback loop (agent behavior)

| User says | Agent does |
|-----------|------------|
| Likes X | **Lock** X stems; only change what they name next; tick **GATES.txt** + one line **NOTES.txt** |
| “Bass muddy” / “lead thin” | **One-focus** pass; stages 2–8; one master; stop |
| “Don’t like any of it” | **Shelf**; no silent full rewrite of same stack; new brief or other project |
| “Workflow / process” | Update this doc; don’t start a song unless asked |
| “Try again” on same muddy concept | Prefer **simplify** (drop parts) over **more processing** |
| “Parts structured better” / “organize parts” | **§21** stem/role hierarchy only — **do not** rewrite song form |
| “Change the arrangement / form / length / start on …” | Late arrange on **locked** stems (§21) — keep compositions |
| “Kick cut through” / “prefer ducking” | Mild duck + kick presence (§19.3); not max amount first |
| “Too aggressive” (duck) | Lower amount / raise floor |
| “Still pumps” | **Shorten duck release** |
| “Less airy” / “dry −N / aux +N” | Lead **send** dial first (§5); one move |
| “Sounds good / as good as we’ll get” | **FINAL lock** — stop creative work unless user reopens |

Full phrase book: **§22**.

---

## 13. Definition of done

- [ ] MVP (drums+bass) approved at some point  
- [ ] Lead approved if present  
- [ ] Signal flow 1–8 on final  
- [ ] A/B vs ref not wildly off  
- [ ] User not requesting more changes  
- [ ] **FINAL** language logged in NOTES + GATES (explicit lock)  
- [ ] If longform was requested: form documented in `STRUCTURE.txt`  

Desktop file ≠ done. **User “done” language = stop.**

---

## 14. Audio / git policy

- **No** audio/stems/sessions in git  
- Only agent/control code to remotes  

---

## 15. Master checklist (print)

```
BRIEF
[ ] Reference captured + fingerprint logged
[ ] Genre / temp / complexity (S/M/C) agreed
[ ] Sound plan (engine per role) listed
[ ] Form/density sketch (even rough)

MVP
[ ] MIDI: drums + bass only — **compose Temp 6–7**
[ ] Dry render + simple mix — **engineering Temp 2–3**
[ ] Kick/bass frequency ownership decided
[ ] Faders → subtractive EQ → selective dyn → light master
[ ] Desktop MVP master
[ ] USER APPROVAL on pocket ────────────── STOP

LAYERS
[ ] Lead only (compose ~6–7) + locked drums/bass → USER STOP
[ ] One bed only (compose ~5–6) → USER STOP
[ ] Extra color only if needed → USER STOP
[ ] Optional humanize **8–10** only after pocket approved

FULL MIX
[ ] Stage 1 dry locked
[ ] Stages 2–8 at **Temp 2–3** (no random “creative” mix chaos)
[ ] Stage 2 static faders / hierarchy / headroom
[ ] Stage 3 subtractive EQ / masking
[ ] Stage 4 selective dynamics (+ optional parallel)
[ ] Stage 5 shared room + plate + delay (pre-EQ sends)
[ ] Stage 6 groups + duck beds
[ ] Stage 7 light mix bus
[ ] Stage 8 master last (crest preserved)

FINISH
[ ] A/B vs ref — **Temp 1–2** (honest QC)
[ ] Mono check
[ ] Automation only if static mix already good
[ ] Complex poly/automation only if S/M clean + user asked
[ ] One-at-a-time fixes after that (focus Temp 3–5)
[ ] Kick/bass duck dialed if used (mild + short release if pump)
[ ] If user asked form/length/start: late arrange on locked stems only (§21)
[ ] FINAL lock language → NOTES + GATES; stop rework
```

---

## 16. Project status (per song only)

Do **not** maintain a song roster in this workflow file.

| Where | What |
|-------|------|
| `SongFolder/NOTES.txt` | Approvals, locks, final master path, decision log |
| `SongFolder/GATES.txt` | Checklist ticks for that project |
| `SongFolder/STRUCTURE.txt` | Form map when a late arrange exists |
| `SongFolder/PARTS_STRUCTURE.txt` | Role/stem hierarchy (not form) |

Status values (use in NOTES): `ACTIVE` · `SHELVED` · `FINAL LOCK` · `ARCHIVED`.

---

## 17. Shared code & script shape

| Path | Role |
|------|------|
| `Songs/PRODUCTION_WORKFLOW.md` | Source of truth (song-agnostic) |
| `Songs/_studio_lib/signal_flow.py` | Stages 2 / 5 / 7 / 8 + `duck()` (prefer mild short-release for kick/bass — §19.3) |
| `*/arrange_*longform*.py` (per song) | Late form on locked stems when needed |
| `Songs/_studio_lib/producer_temp.py` | Per-task TEMP defaults (`temp_for`, `t_norm`, `log_temp`) |
| `Songs/_studio_lib/VOICE_BRIEF_TEMPLATE.txt` | Timbre brief per role (§20) |
| `Songs/_studio_lib/PARTS_STRUCTURE_TEMPLATE.txt` | Role/stem hierarchy stub (§21) |
| `Songs/_studio_lib/STRUCTURE_TEMPLATE.txt` | Form/tempo/length stub (§21) |
| `Songs/_studio_lib/GATES_TEMPLATE.txt` | Gate checklist incl. late form + FINAL |
| `Songs/_studio_lib/NOTES_TEMPLATE.txt` | Decision log + mood lock |
| `Songs/_studio_lib/solo_ab_voices.py` | Metered solo A/B candidate vs ref |
| `Songs/_studio_lib/new_song_scaffold.py` | New song folders + all stubs above |
| `Songs/_studio_lib/record_system_audio.py` | Shared Realtek capture (copied into each song) |

**Script architecture for new songs:**
```
new_song_scaffold.py   # folders + VOICE_BRIEF, GATES, NOTES, PARTS_STRUCTURE, STRUCTURE
# fill brief + mood lock + capture ref (Realtek)
render_mvp()           # drums+bass dry; solo A/B bass & kick; simple mix → STOP
add_part(name)         # locked stems + one new dry voice + solo A/B + mix
mix_signal_flow()      # full 1–8
focus_part(name)       # re-voice one part only
# optional late arrange on locked stems only (§21)
```

Not one 800-line “do everything” as the only entry point.

**Voice match order (every role):**  
timbre brief → pick sample/synth family → dry render → `solo_ab_voices.py` + ear → lock stem → mix.

---

## 18. Quick technique cheat sheet

| Problem | First move | Avoid |
|---------|------------|--------|
| Muddy | HPF beds/lead; cut 200–400; shorten bass notes; lower pads | More reverb, more layers |
| Cheap | Better multi-sample / factory PC | Saturation + air shelf only |
| Weak kick | Sample/layer + short click; carve bass | Limit whole mix |
| Bass unclear | Definition ~800–1.2k; mono; less mid pad | Boost 50 Hz only |
| Lead buried | Fader + presence EQ; cut pads at 1–3k | Solo boost lead into limit |
| No depth | Shared sends, pre-HPF | Insert hall on every track |
| Harsh | Cut 2.5–5k; dull delay returns | Only cut highs on master |
| Lifeless | Less compression; raise crest; automation later | Another bus compressor |

---

## 19. Professional excellence (extra steps for pro-sounding tracks)

These are the highest-leverage additions beyond the core pipeline. Adopt them **in order of impact** when capacity allows. Not every song needs every item on day one — but **ignoring the whole list** is how tracks stay “demo quality.”

### 19.1 Priority stack (do these first)

| Priority | Addition | Why it sounds pro |
|----------|----------|-------------------|
| **P0** | MVP + gates + sources first | Already required — biggest win |
| **P1** | **Contrast** (arrangement) | Pros sell drops by *removing* parts, not only adding FX |
| **P1** | **Kick/bass marriage** | Commercial low end is designed as one system |
| **P1** | **True A/B loop** while mixing | Mix drifts without frequent ref checks at matched level |
| **P2** | **Stereo discipline** | Mono bass/kick; width only mid/high; mono-compatibility |
| **P2** | **Note length / silence** | Short bass and stabs create groove; long pads create mud |
| **P2** | **Print with tails** + section edits | Clean endings, reverb tails, no clicks |
| **P3** | **Micro-timing by role** | Kick tight; hats/perc can push/pull; bass slightly behind or locked by genre |
| **P3** | **Velocity storytelling** | Ghost notes, accents on 2/4, lead phrase dynamics |
| **P3** | **Final DAW polish pass** | Studio One for last 10%: clip gain, automation, stock limit |

### 19.2 Arrangement contrast (often missing in AI renders)

| Technique | How |
|-----------|-----|
| **Mute map** | Write which bars *remove* kick, bass, hats, lead |
| **Filter/open** | One rising filter on a bed into chorus — not on everything |
| **Call and response** | Lead phrase → gap → stab/bass answer |
| **Breakdown** | 4–8 bars thinner before final lift |
| **One new element per section** | Intro hats → verse bass → chorus lead — avoid all-in from bar 1 |

**Stop check:** Can you hum the form from memory? If every 8 bars sounds identical, the mix cannot save it.

### 19.3 Kick + bass as one instrument

| Technique | How |
|-----------|-----|
| **Sidechain / duck** | Prefer ducking over only EQ when kick must cut through bass |
| **Frequency split** | Decide: kick owns ~50–60 Hz **or** bass does; the other gets a notch/cut |
| **Kick presence** | Light EQ on kick (sub body + click ~2.5–5 kHz) **plus** mild duck — not max duck alone |
| **Note length** | Bass off before next kick if they clash (genre-dependent) |
| **Phase** | Flip bass polarity if low end thins in mono |
| **Listen in mono** | Low end must still be solid summed |

#### Duck dialing (use `signal_flow.duck`)

| User hears | Move first | Typical range |
|------------|------------|---------------|
| Kick buried under bass | Enable duck + kick presence | amount 0.35–0.5, floor 0.55–0.65 |
| **Too aggressive / hollow** | **Lower amount**, raise floor | amount ≈ **0.28–0.35**, floor ≈ **0.70–0.78** |
| **Bass still pumps** | **Shorten release** (main pump control) | release **40–80 ms** (not 150–200) |
| Duck clicks / too snappy | Lengthen release slightly or soften amount | release 60–100 ms |
| Beds fight kick | Duck **pads/stabs** harder than bass | pad amount 0.4–0.55; bass milder |

**Working “mild short-release” preset:**  
`amount≈0.30`, `floor≈0.74`, `attack_ms≈3`, `release_ms≈40`, key LPF ~120 Hz.

**Rule:** long release = audible pump tail; short release = kick hole without whoosh.  
Do **not** default to library defaults (`release_ms=160`) for kick/bass — that pumps.

### 19.4 Stereo image rules

| Element | Placement |
|---------|-----------|
| Kick, snare, bass, lead body | Center (or near-center) |
| Hats, perc, plucks, FX | Mild L/R; automate sparingly |
| Pads / wide layers | Wider, but HPF so sides have no sub |
| Check | Mono fold: no hole in center, no disappearing pad that was only sides |

#### Wide pad / “hard pan” presence (when user asks)

| Step | Technique |
|------|-----------|
| HPF | ≥150–200 Hz so sides carry no sub |
| **Hard L/R** | True hard image: L = dry mono body, R = Haas (~10–18 ms) + slight HF tilt — not “both channels same + stereo width plugin only” |
| Presence | Peak ~2.5–4.5 kHz + mild air shelf so width is *heard*, not only measured |
| Side boost | M/S: reduce mid a bit, lift side — stop before mono fold disappears |
| Level | Wide hard-pan can feel quieter; small gain after width is OK |
| Duck | Still light-duck pad under kick so wide bed doesn’t mask punch |

### 19.5 Performance realism (MIDI / samples)

| Technique | How | Temp note |
|-----------|-----|-----------|
| **Role-based timing** | Kick ~grid; snare ± few ms; hats looser; bass genre-locked or slightly late | Compose 6–7; humanize 8–10 later |
| **Velocity layers** | Use multi-vel samples; don’t flatten all notes to 100 | — |
| **Round-robin / RR feel** | Alternate samples or tiny pitch/vel variance on hats | 3–5 on focus |
| **Articulation** | Staccato vs legato by section; shorter notes in busy sections | — |
| **No machine-gun hats** | Same sample + same vel every 16th = cheap | Vary vel/RR |

### 19.6 Mix craft extras

| Technique | How |
|-----------|-----|
| **Clip gain before faders** | Normalize peaks of stems to similar ballpark, then fader |
| **EQ in context** | Solo only to find a problem; cut/boost with full mix playing |
| **High-pass the reverb/delay** | 200–400 Hz HPF on sends (already in flow — enforce it) |
| **Delay throws** | One send-up on phrase ends — not constant wet lead |
| **De-ess / harsh control** | On bright leads/hats if 5–8 kHz hurts |
| **Saturation on purpose** | Tape/soft sat on bass or drum bus *subtly* for glue — not every track |
| **Leave crest** | If crest collapses below ~8 on a pop/electronic ref that sits ~10–12, you’re over-squashing |

### 19.7 Reference workflow (pro habit)

| Step | Technique |
|------|-----------|
| Level-match | Match rough RMS before A/B so louder always “wins” |
| Loop 8 bars | Same section of ref vs same section of ours |
| One question per A/B | “Kick weight?” then “Bass note length?” then “Verb amount?” — not all at once |
| Mid-mix A/B | After stage 2 and after stage 7, not only at the end |
| Store targets | Keep fingerprint file next to song (`ref_fingerprint.txt`) |

### 19.8 Versioning & decisions

| Practice | Why |
|----------|-----|
| Name masters clearly | `Song_MVP.wav`, `Song_LeadFocus.wav`, `Song_MixA.wav` — not only overwrite Desktop |
| Keep last good | Never delete last approved master when trying a risky change |
| One change per bounce | User can hear what moved |
| Decision log | One line in `NOTES.txt`: “v3: shorter bass, −3 dB pad” |

### 19.9 Print / delivery hygiene

| Item | Technique |
|------|-----------|
| **Tail** | 1–3 s of reverb decay after last hit; no hard cut |
| **Fade** | Short fade-in on file start if click; musical fade-out if needed |
| **SR/bit** | 48 kHz, 24-bit stems; master 24-bit or 16-bit for casual listen |
| **True peak** | Ceiling ≈ −1.0 to −0.3 dBTP class; avoid inter-sample overs when limiting |
| **Stem set** | Dry or lightly processed group stems for Studio One if user will finish there |

### 19.10 Optional “final 10%” in Studio One

Python pipeline gets ~90%. For release-minded polish:

1. Import locked stems into Studio One  
2. Clip gain + ride lead/bass automation by ear  
3. Stock or preferred limiter / imager last  
4. Bounce final  

Do **not** start the song in a 50-plugin DAW template before MVP approval.

### 19.11 Genre templates (fill when a genre is chosen)

Keep a short checklist per genre in the song folder (`GENRE_CHECKLIST.txt`):

| Genre family | Pro tells |
|--------------|-----------|
| Soul / funk | Pocket, mono bass, dry-ish drums, EP/body mid, short rooms |
| Synth-pop / darkwave | Sidechain pulse, bright lead, controlled sub, tempo delays |
| House / dance | Four-on-floor, bass/kick marriage, drier than ambient, clap layer |
| Ambient / cinematic | Longer tails, wider pads, less hard limiting, slower automation |

### 19.12 Ear & session hygiene

| Practice | Why |
|----------|-----|
| Moderate monitor level | Loud always sounds more “impressive” |
| Breaks every 45–60 min | Fatigue → too much treble/comp |
| Morning A/B on big decisions | Fresh ears for “done?” |
| Second system once | Phone or earbuds — translation check |

### 19.13 What we will *not* chase in-pipeline

- Perfect streaming **LUFS** war as a substitute for balance  
- Cloning reference melodies or signature motifs  
- Unlimited plugin chains per stem before sources are good  
- Full complex arrangement before MVP approval  

### 19.14 Excellence checklist (add to song when aiming high)

```
[ ] Form has contrast (breakdown / dropout / new element per section)
[ ] Parts hierarchy documented if multi-stem (PARTS_STRUCTURE) — form only if asked
[ ] Kick+bass designed as a pair (split + duck + mono check; short release if pump)
[ ] Note lengths intentional (bass not always long)
[ ] Stereo: center foundation, width on beds/FX only
[ ] Velocity / RR so hats & drums don’t machine-gun
[ ] A/B vs ref at matched level (mid-mix + full)
[ ] Crest not crushed vs ref
[ ] Print with tail; clean start/end
[ ] Last good master archived with version name
[ ] Optional Studio One 10% polish if user wants release quality
[ ] Per-role timbre brief + solo A/B vs ref (§20)
```

---

## 20. Matching voices to the reference (samples & synths)

**Goal:** Same *family* and *mix role* as the reference — not a one-note sample of the hit song, and not a random free SFZ that only shares the MIDI note.

**Order of truth:**  
**1) Right source category → 2) Right envelope/articulation → 3) Right tone EQ/sat → 4) Right space.**  
EQ alone cannot turn a thin GM pluck into a thick Moog bass.

### 20.1 Build a *timbre brief* (per role) before picking a sound

Listen to the reference **solo-focused** (or with other parts ducked in your head) for each role. Write 5–8 words:

| Dimension | Questions | Examples |
|-----------|-----------|----------|
| **Source type** | Acoustic sample, electric, analog synth, digital/FM, ROMpler? | “Analog mono bass”, “real kit”, “supersaw lead” |
| **Pitch range** | Sub / low / mid / high? | Bass mostly &lt;150 Hz + growl ~800 Hz |
| **Attack** | Clicky, soft, slow pad swell? | Kick has click; bass has no click |
| **Body** | Thin, round, nasal, hollow? | Round 100–200 Hz |
| **Harmonics** | Dark, bright, distorted, filtered? | Dark LP; no fizzy air |
| **Motion** | Static, chorus, PWM, filter move? | Slight chorus on pad |
| **Space** | Dry, short room, long plate? | Lead dry + slap delay |
| **Width** | Mono, narrow, wide? | Bass mono; pad wide |

Save as `VOICE_BRIEF.txt` in the song folder. **Pick libraries/patches against this brief**, not against “bass = any bass”.

### 20.2 Sample path (closer to real instruments / recorded sources)

| Step | Technique |
|------|-----------|
| **1. Category match** | Kit vs electronic kit; finger bass vs synth bass; Rhodes vs DX — wrong category never matches |
| **2. Multi-velocity** | Soft/hard samples; map MIDI velocity to layers (GSCW, jRhodes-style) |
| **3. Multi-sample pitch** | Enough keyzones so pitch-shift is small (≤ few semitones ideal) |
| **4. Round-robin** | Alternate takes on hats/snares to kill machine-gun |
| **5. Envelope match** | Match ref **attack and release** (short bass notes vs long pads) via note length + ampeg |
| **6. Layer jobs** | e.g. acoustic kick body + sine sub; never two full-range bass samples fighting |
| **7. Tone to brief** | Subtractive EQ to remove what samples have that ref doesn’t; sat for harmonics if ref is driven |
| **8. Solo A/B** | Render one bar of *our* bass vs *ref* bass region at same loudness |

**Best free/pro-adjacent sources in this studio:** multi-vel drums (GSCW), FingerBass YR, jRhodes, FreePats multi-sample synths, dedicated SFZ kits — prefer these over single one-shots when the ref sounds “recorded.”

### 20.3 Synth path (closer to electronic / designed sounds)

| Step | Technique |
|------|-----------|
| **1. Architecture guess** | Mono bass vs poly pad; saw/square/FM/noise; unison? |
| **2. Start from factory** | Surge **MIDI Programs** / character patches — then tweak (faster than init) |
| **3. Oscillator** | Wave + unison detune amount (ref “thick” often = 3–7 unison, not 1 osc) |
| **4. Filter** | Cutoff/resonance/env amount — darkwave lead = lower cutoff + env poke |
| **5. Amp env** | Attack/decay/sustain/release — *this* is half of “sounds like” |
| **6. Movement** | Slow filter LFO, chorus, PWM — only if ref has motion |
| **7. FX last** | Distortion/chorus/delay *type* from brief; dry when ref is dry |
| **8. Hybrid** | Sample for body + synth for sub or air (split bands) |

**Studio rule:** load Surge via MIDI Programs + `program_change` (reliable). Document PC number in VOICE_BRIEF.

### 20.4 Processing stack to *finish* the match (after source is close)

Apply only what the brief still lacks:

| Need | Tools |
|------|--------|
| Darker | LP, cut highs, less air shelf |
| Brighter / more bite | Mild HP, presence 2–5 kHz, soft sat |
| Fatter low | Sub layer &lt;80–100 Hz, mono; not more mud 200–400 |
| More “analog” | Soft clip/sat, tiny pitch drift, less perfect timing (role-based) |
| More “digital/clean” | Less sat, tighter quantize, cleaner HP |
| Same space as ref | Shared send amount/type — not a different hall on every voice |

### 20.5 Solo A/B protocol (required for serious voice match)

1. Capture or isolate a **short loop** of ref where that instrument is clear (or full mix with focus).  
2. Render **4–8 bars** of *only* our candidate voice (dry or light FX).  
3. Level-match RMS.  
4. Flip every 2–4 bars: closer / farther on attack, body, brightness, length.  
5. Change **one** variable (patch, then env, then EQ).  
6. Lock the winner as dry stem; only then mix.

Temp for this work: **2–4** (surgical), not 9–10.

### 20.6 What *not* to do

| Trap | Why it fails |
|------|----------------|
| EQ a wrong-category sample until it “sort of” fits | Missing harmonics/envelope of the real source |
| Layer 3 full-range basses | Mud and phase; use frequency-split layers |
| Copy ref melody/hook to “match the voice” | Legal/creative wrong; voice match ≠ composition clone |
| Only match master spectrum of full mix | Hides that the lead itself is still wrong |
| Use GM one-shot for a multi-vel real kit ref | Always sounds cheap next to multi-samples |

### 20.7 Practical decision tree

```
Is the ref voice clearly acoustic/recorded?
  YES → multi-sample / multi-vel first; hybrid sub only if needed
  NO  → synth factory patch in same family; then filter/env/FX

Is attack wrong?
  YES → fix envelope / sample start / transient layer BEFORE EQ

Is body wrong after attack is right?
  YES → different sample zone or osc; then EQ

Is it close dry but wrong in mix?
  YES → level, carve, send space — not a new random patch yet
```

### 20.8 Voice match checklist (per role)

```
[ ] Timbre brief written (type, attack, body, bright, space, width)
[ ] Category chosen (sample vs synth) matches ref family
[ ] Candidate A/B solo vs ref at matched level
[ ] Attack/release match note length in MIDI
[ ] Multi-vel / RR if applicable
[ ] Hybrid layers frequency-split if used
[ ] Tone polish (EQ/sat) only after source is in the right family
[ ] Space matches ref dryness/wetness
[ ] Locked dry stem before full mix
```

---

## 21. Parts vs arrangement

**Highest-cost language confusion:** two different requests sound similar:

| User means | Do this | Do **not** do this |
|------------|---------|---------------------|
| **Parts** organized better | `PARTS_STRUCTURE.txt`, `Stems_Parts\` role names, hierarchy in notes | Rewrite bar order / MIDI form |
| **Arrangement / form** changed | Late pass on **locked** stems: section map, start bar, length, tempo | Recompose riffs or “improve” melodies unprompted |
| **Structure** (ambiguous) | **Ask once** if unclear: *parts hierarchy* or *song form*? | Guess and rewrite the song |

### 21.1 Phase B sketch vs late form

| When | What |
|------|------|
| **Early (B)** | Light mute map only — enough for MVP contrast |
| **After layers locked** | Optional longform / commercial length if user asks |
| **Never** | “Helpful” form rewrite while user is still approving voices |

### 21.2 Late arrangement on locked stems (preferred)

When user wants a **full song** (e.g. 4.5–5 min), tempo nudge, or “start on the lead”:

1. **Freeze** approved dry/processed stems (do not re-voice).  
2. Detect **lead entry bar** (energy map or MIDI).  
3. **Cut pre-hook intro** if they want the song to start on the lead/hook.  
4. **Tempo:** ± a few BPM via speed change (document pitch side-effect if resampling).  
5. **Section map** from existing blocks only (verse / chorus / break / bridge / outro / tag) — **loop and reorder**, don’t invent new melodies.  
6. Re-apply mix carries: short duck, wide pad, kick presence, send dial.  
7. Write `STRUCTURE.txt` + `Stems_Arrange\` + Desktop master.  
8. Stop and wait.

**Script shape:** per-song `arrange_*` that only slices/loops/speeds locked stems (no new composition).

### 21.3 Target lengths (when asked)

| Target | Rough length (4/4) | Notes |
|--------|-------------------|-------|
| Short / demo | 32–48 bars (~1.5–2.5 min at mid tempos) | MVP / focus |
| Full song | **~4.5–5 min** when requested | Loop locked material with contrast |
| Always | Contrast every 8–16 bars | Mute map; not wall-to-wall identical loops |

### 21.4 Mood lock

At brief time, write one line:

- Mode (minor/dark vs major/bright)  
- Allowed colors (e.g. bVI, bVII only — no happy leaps)  
- Lead: sparse, limited range, no major-pentatonic bounce  

If user says **“too happy”**: darken harmony + tone **before** adding layers.

---

## 22. Phrase book (user language → action)

| Phrase | Action | Section |
|--------|--------|---------|
| “Sounds good” / “good. go next” | Lock current layer; advance **one** gate | §6, §12 |
| “Perfect” / “+N dB” | Lock + apply exact level move only | §12 |
| “Parts structured / organized” | Role stems + PARTS doc — **not** form rewrite | §21 |
| “Didn’t want the song changed” | Restore last full mix; archive experiment | §19.8 |
| “Add DnB / swirl / wet” | Sparse color + lead send; keep amount modest | §5, §6 D3 |
| “Fewer DnB / less air” | Reduce color density / cut sends first | §5 |
| “Dry −3 / aux +3” / “repeat” | Exact lead dial; repeat = same move again | §5 |
| “Kick cut through bass” | Duck + kick presence | §19.3 |
| “Prefer ducking” | Sidechain path, not only EQ carve | §19.3 |
| “Not so aggressive” | Milder duck amount/floor | §19.3 |
| “Still pumps” / “reduce release” | Shorten duck **release** (40–80 ms) | §19.3 |
| “Hard pan the pad” / “wide presence” | Hard L/R + presence + HPF | §19.4 |
| “Start on the lead bar” | Cut pre-lead; late arrange | §21 |
| “Speed up a few BPM” | Tempo +few; keep compositions | §21 |
| “4.5–5 minute song” | Longform section map on locked stems | §21 |
| “As good as we’re going to get” | **FINAL LOCK** — NOTES + GATES; stop | §13 |
| “I don’t like any” | Shelf track; re-brief | §12 |
| “Workflow / knowledge base” | Update **this file** only; no song work | §12 |

---

## 23. Knowledge base maintenance

| When | Update |
|------|--------|
| User corrects process language | §0 lessons + §22 phrase |
| New mix recipe works (duck, pad width, lead dial) | §7 / §19 with **numbers** (no song names) |
| Song FINAL locked | That song’s `NOTES.txt` + `GATES.txt` only — **not** this file |
| New shared helper | §17 paths |
| Genre pattern repeats | §19.11 genre row |

**Source of truth (process):** `Songs/PRODUCTION_WORKFLOW.md` — song-agnostic  
**Per-song only:** `NOTES.txt`, `GATES.txt`, `STRUCTURE.txt`, `PARTS_STRUCTURE.txt`, `VOICE_BRIEF.txt`  
**Code:** `Songs/_studio_lib/` (`signal_flow.duck`, `producer_temp`, `solo_ab_voices`, scaffold)

Do not name specific tracks in this workflow. Do not scatter conflicting rules into random song READMEs.

---

*End of standing workflow. Update this file when process changes; do not invent conflicting one-off pipelines.*
