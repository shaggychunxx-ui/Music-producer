import argparse
import json
from pathlib import Path

from song_pipeline_kb import (
    GATES,
    META,
    SCAFFOLD,
    TEMP_TABLE,
    get_phase,
    get_recipe,
    list_phases,
    match_phrase,
    search_kb,
)
from song_pipeline_kb.recipes import RECIPES
from song_pipeline_kb import song_state, s1_jobs, observe as observe_mod
from song_pipeline_kb import compose as compose_mod
from song_pipeline_kb import qc as qc_mod
from song_pipeline_kb import taste as taste_mod


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def _parse_bands(raw: str | None) -> dict | None:
    if not raw:
        return None
    out = {}
    for part in raw.split(","):
        part = part.strip()
        if not part or "=" not in part:
            continue
        k, v = part.split("=", 1)
        try:
            out[k.strip().lower()] = float(v.strip())
        except ValueError:
            continue
    return out or None


def _cmd_taste(a) -> int:
    data_dir = getattr(a, "data_dir", None)
    cmd = a.taste_cmd
    if cmd == "status":
        _p(taste_mod.status(data_dir))
        return 0
    if cmd == "log":
        rows = taste_mod.load_listens(data_dir, limit=a.limit)
        _p({"count": len(rows), "listens": rows})
        return 0
    if cmd == "profile":
        _p(taste_mod.load_profile(data_dir))
        return 0
    if cmd == "rebuild":
        _p(taste_mod.rebuild_profile(data_dir))
        return 0
    if cmd == "listen":
        fp: dict = {}
        if a.fingerprint_json:
            try:
                fp.update(json.loads(Path(a.fingerprint_json).read_text(encoding="utf-8")))
            except Exception as exc:
                _p({"ok": False, "error": f"fingerprint-json: {exc}"})
                return 2
        if a.bpm is not None:
            fp["tempo_bpm"] = a.bpm
        if a.peak_db is not None:
            fp["peak_db"] = a.peak_db
        if a.rms_db is not None:
            fp["rms_db"] = a.rms_db
        if a.crest_db is not None:
            fp["crest_db"] = a.crest_db
        if a.key:
            fp["key"] = a.key
        bands = _parse_bands(a.bands)
        if bands:
            fp["bands"] = bands
        try:
            _p(
                taste_mod.log_listen(
                    artist=a.artist,
                    title=a.title,
                    rating=a.rating,
                    source=a.source,
                    url=a.url,
                    tags=a.tags,
                    notes=a.notes,
                    mood=a.mood,
                    genre_hint=a.genre_hint,
                    fingerprint=fp or None,
                    audio_path=a.audio_path,
                    data_dir=data_dir,
                )
            )
        except ValueError as exc:
            _p({"ok": False, "error": str(exc)})
            return 2
        return 0
    if cmd == "rate":
        _p(
            taste_mod.rate_listen(
                a.id,
                a.rating,
                data_dir=data_dir,
                notes=a.notes,
            )
        )
        return 0
    if cmd == "apply-brief":
        _p(
            taste_mod.apply_brief_to_song(
                a.song_dir,
                data_dir=data_dir,
                reference=a.reference,
                lock_gate=a.lock,
                force=a.force,
            )
        )
        return 0
    return 2


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="song_pipeline_kb",
        description=(
            "Production brain: phases, gates, recipes, compose, S1 job plans, "
            "taste memory (listen log + profile), and vision/audio observation. "
            "Studio-One execute_job.py is the hands."
        ),
    )
    s = p.add_subparsers(dest="cmd", required=True)

    s.add_parser("info")
    s.add_parser("phases")
    ph = s.add_parser("phase")
    ph.add_argument("name")
    s.add_parser("gates")
    s.add_parser("temp")
    s.add_parser("scaffold")
    r = s.add_parser("recipe")
    r.add_argument("name", nargs="?", default="list")
    phr = s.add_parser("phrase")
    phr.add_argument("text")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)

    # --- song production state (brain) ---
    init_p = s.add_parser("init-song", help="Create GATES/NOTES/scaffold in a song folder")
    init_p.add_argument("--song-dir", type=Path, required=True)
    init_p.add_argument("--name", default=None)
    init_p.add_argument(
        "--apply-taste",
        action="store_true",
        help="Apply persistent taste profile to BRIEF.json after init",
    )
    init_p.add_argument(
        "--lock-brief",
        action="store_true",
        help="With --apply-taste, also lock the brief gate",
    )

    st = s.add_parser("status", help="Song gates + MIDI inventory")
    st.add_argument("--song-dir", type=Path, required=True)

    gt = s.add_parser("gate", help="Set a production gate open|locked|skipped")
    gt.add_argument("name")
    gt.add_argument("status", choices=["open", "locked", "skipped", "yes", "no"])
    gt.add_argument("--song-dir", type=Path, required=True)

    nxt = s.add_parser("next", help="What production should do next (no DAW control)")
    nxt.add_argument("--song-dir", type=Path, required=True)

    # --- compose MIDI (brain) ---
    comp = s.add_parser("compose", help="Write genre-profile MIDI under song/MIDI/")
    comp.add_argument("--song-dir", type=Path, required=True)
    comp.add_argument("--genre", default="dark_pulse", help="dark_pulse|trap|house|ambient")
    comp.add_argument("--seed", type=int, default=None)
    comp.add_argument("--bpm", type=int, default=None)
    comp.add_argument("--bars", type=int, default=None)
    s.add_parser("genres", help="List compose genre profiles")

    # --- plan S1 execution jobs (brain → hands handoff) ---
    plan = s.add_parser("plan", help="Write s1_jobs/current.json for Studio-One executor")
    plan_sub = plan.add_subparsers(dest="plan_cmd", required=True)

    mvp = plan_sub.add_parser("mvp", help="Plan MVP drums+bass stream job")
    mvp.add_argument("--song-dir", type=Path, required=True)
    mvp.add_argument(
        "--create-tracks",
        action="store_true",
        help="Add empty instrument tracks (default: use Template tracks)",
    )
    mvp.add_argument("--tracks", type=int, default=2)
    mvp.add_argument("--drums-track", type=int, default=None, help="1-based; default use role drums")
    mvp.add_argument("--bass-track", type=int, default=None, help="1-based; default use role bass")
    mvp.add_argument("--skip-brief-gate", action="store_true")
    mvp.add_argument("--max-sec", type=float, default=None)
    mvp.add_argument("--load", nargs="*", default=[], help="Optional browser_load names")

    part = plan_sub.add_parser("stream", help="Plan single-part stream job")
    part.add_argument("--song-dir", type=Path, required=True)
    part.add_argument("--part", required=True, help="lead|bed|color|name")
    part.add_argument("--track", type=int, required=True)
    part.add_argument("--midi", default=None)
    part.add_argument("--no-require-pocket", action="store_true")

    mixp = plan_sub.add_parser("mix", help="Plan MCU mix balance + export intent")
    mixp.add_argument("--song-dir", type=Path, required=True)
    mixp.add_argument("--preset", default="full_static")
    mixp.add_argument("--no-export", action="store_true")

    # --- observe vision/audio cues from Studio-One last_result ---
    obs = s.add_parser(
        "observe",
        help="Read last_result.json (eyes+ears cues) and recommend next step",
    )
    obs.add_argument("--song-dir", type=Path, required=True)

    dec = s.add_parser(
        "decide",
        help="Observe + policy (taste default; --unattended metric locks)",
    )
    dec.add_argument("--song-dir", type=Path, required=True)
    dec.add_argument(
        "--auto-tech",
        action="store_true",
        help="Log high-confidence technical note only (taste mode)",
    )
    dec.add_argument(
        "--unattended",
        action="store_true",
        help="Auto-lock capture gates when confidence/QC pass",
    )

    qc = s.add_parser("qc", help="Technical QC score from last_result (+ optional ref)")
    qc.add_argument("--song-dir", type=Path, required=True)

    cyc = s.add_parser(
        "cycle",
        help="next → compose? → plan if ready → optional execute_job → observe",
    )
    cyc.add_argument("--song-dir", type=Path, required=True)
    cyc.add_argument("--execute", action="store_true", help="Run Studio-One execute_job.py")
    cyc.add_argument("--s1-remote", type=Path, default=None)
    cyc.add_argument("--max-sec", type=float, default=None)
    cyc.add_argument("--allow-prompt", action="store_true")
    cyc.add_argument("--no-plan", action="store_true")
    cyc.add_argument("--compose", action="store_true", help="Compose MIDI if missing")
    cyc.add_argument("--genre", default="dark_pulse")
    cyc.add_argument("--unattended", action="store_true")

    full = s.add_parser(
        "run-unattended",
        help="Brief lock + compose + Studio-One autonomous_run (zero-human path)",
    )
    full.add_argument("--song-dir", type=Path, required=True)
    full.add_argument("--name", default=None)
    full.add_argument("--genre", default="dark_pulse")
    full.add_argument("--max-sec", type=float, default=40.0)
    full.add_argument("--parts", default="drums,bass,lead")
    full.add_argument("--s1-remote", type=Path, default=None)
    full.add_argument("--prefer-import", action="store_true")
    full.add_argument("--brain-only", action="store_true", help="Compose+plan only (no S1)")

    # --- taste memory (persistent listen log + profile) ---
    taste_p = s.add_parser(
        "taste",
        help="Listen log + taste profile (develop preferences from refs)",
    )
    taste_sub = taste_p.add_subparsers(dest="taste_cmd", required=True)

    t_stat = taste_sub.add_parser("status", help="Profile summary + recent listens")
    t_stat.add_argument("--data-dir", type=Path, default=None)

    t_log = taste_sub.add_parser("log", help="Show recent listen log entries")
    t_log.add_argument("--limit", type=int, default=20)
    t_log.add_argument("--data-dir", type=Path, default=None)

    t_prof = taste_sub.add_parser("profile", help="Print full taste_profile.json")
    t_prof.add_argument("--data-dir", type=Path, default=None)

    t_rebuild = taste_sub.add_parser("rebuild", help="Rebuild profile from listen log")
    t_rebuild.add_argument("--data-dir", type=Path, default=None)

    t_listen = taste_sub.add_parser(
        "listen",
        help="Log a reference listen (metadata + optional numeric fingerprint)",
    )
    t_listen.add_argument("--artist", default="")
    t_listen.add_argument("--title", default="")
    t_listen.add_argument(
        "--rating",
        default="unrated",
        help="love|ok|no|unrated (aliases: like, meh, skip)",
    )
    t_listen.add_argument(
        "--source",
        default="manual",
        help="manual|spotify|phone|loopback|…",
    )
    t_listen.add_argument("--url", default=None)
    t_listen.add_argument("--tags", default="", help="comma-separated vibe tags")
    t_listen.add_argument("--notes", default="")
    t_listen.add_argument("--mood", default=None, help="e.g. dark minor")
    t_listen.add_argument(
        "--genre",
        default=None,
        dest="genre_hint",
        help="dark_pulse|trap|house|ambient",
    )
    t_listen.add_argument("--bpm", type=float, default=None)
    t_listen.add_argument("--peak-db", type=float, default=None)
    t_listen.add_argument("--rms-db", type=float, default=None)
    t_listen.add_argument("--crest-db", type=float, default=None)
    t_listen.add_argument(
        "--bands",
        default=None,
        help="sub=0.2,low=0.3,... (relative band energy)",
    )
    t_listen.add_argument("--key", default=None)
    t_listen.add_argument(
        "--fingerprint-json",
        type=Path,
        default=None,
        help="Path to fingerprint JSON (numbers only; merges with flags)",
    )
    t_listen.add_argument(
        "--audio-path",
        default=None,
        help="Local capture path only (not committed; optional)",
    )
    t_listen.add_argument("--data-dir", type=Path, default=None)

    t_rate = taste_sub.add_parser("rate", help="Update rating on a listen by id")
    t_rate.add_argument("id")
    t_rate.add_argument("rating")
    t_rate.add_argument("--notes", default=None)
    t_rate.add_argument("--data-dir", type=Path, default=None)

    t_apply = taste_sub.add_parser(
        "apply-brief",
        help="Write BRIEF.json + NOTES from taste profile into a song folder",
    )
    t_apply.add_argument("--song-dir", type=Path, required=True)
    t_apply.add_argument(
        "--reference",
        default=None,
        help="Optional per-song ref label (overrides soft ref from loves)",
    )
    t_apply.add_argument(
        "--lock",
        action="store_true",
        help="Also lock the brief gate after applying",
    )
    t_apply.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing BRIEF.json",
    )
    t_apply.add_argument("--data-dir", type=Path, default=None)

    a = p.parse_args(argv)

    if a.cmd == "info":
        meta = dict(META)
        meta["role"] = "production brain — plans jobs; Studio-One executes"
        meta["s1_handoff"] = "s1_jobs/current.json → Studio-One tools/execute_job.py"
        _p(meta)
    elif a.cmd == "phases":
        for k in list_phases():
            z = get_phase(k)
            print(f"{z.get('id', '?'):3} {k:12}  {z.get('name', '')}")
    elif a.cmd == "phase":
        _p(get_phase(a.name))
    elif a.cmd == "gates":
        _p(GATES)
    elif a.cmd == "temp":
        _p(TEMP_TABLE)
    elif a.cmd == "scaffold":
        _p(SCAFFOLD)
    elif a.cmd == "recipe":
        if not a.name or a.name in ("list", "all"):
            print("Available:", ", ".join(RECIPES))
        else:
            _p(get_recipe(a.name))
    elif a.cmd == "phrase":
        _p(match_phrase(a.text))
    elif a.cmd == "search":
        _p(search_kb(a.query, a.limit))
    elif a.cmd == "init-song":
        out = song_state.init_song(a.song_dir, name=a.name)
        if getattr(a, "apply_taste", False):
            applied = taste_mod.apply_brief_to_song(
                a.song_dir,
                lock_gate=bool(getattr(a, "lock_brief", False)),
                force=True,
            )
            out["taste_brief"] = applied
        _p(out)
    elif a.cmd == "status":
        _p(song_state.summary(a.song_dir))
    elif a.cmd == "gate":
        _p(song_state.set_gate(a.song_dir, a.name, a.status))
    elif a.cmd == "next":
        _p(s1_jobs.next_action(a.song_dir))
    elif a.cmd == "compose":
        genre = a.genre
        bpm = a.bpm
        # Prefer song BRIEF.json from taste apply-brief when user left defaults
        brief = taste_mod.load_song_brief(a.song_dir)
        if brief:
            if genre == "dark_pulse" and brief.get("genre"):
                genre = str(brief["genre"])
            if bpm is None and brief.get("bpm") is not None:
                try:
                    bpm = int(round(float(brief["bpm"])))
                except (TypeError, ValueError):
                    pass
        _p(
            compose_mod.compose_song(
                a.song_dir,
                genre=genre,
                seed=a.seed,
                bpm=bpm,
                bars=a.bars,
            )
        )
    elif a.cmd == "taste":
        return _cmd_taste(a)
    elif a.cmd == "genres":
        _p(compose_mod.list_genres())
    elif a.cmd == "plan":
        if a.plan_cmd == "mvp":
            _p(
                s1_jobs.plan_mvp(
                    a.song_dir,
                    create_tracks=a.create_tracks,
                    track_count=a.tracks,
                    drums_track=a.drums_track,
                    bass_track=a.bass_track,
                    browser_loads=a.load,
                    skip_brief_gate=a.skip_brief_gate,
                    max_sec=a.max_sec,
                )
            )
        elif a.plan_cmd == "stream":
            _p(
                s1_jobs.plan_stream_part(
                    a.song_dir,
                    part=a.part,
                    track=a.track,
                    midi=a.midi,
                    require_pocket=not a.no_require_pocket,
                )
            )
        elif a.plan_cmd == "mix":
            _p(
                s1_jobs.plan_mix(
                    a.song_dir,
                    preset=a.preset,
                    export=not a.no_export,
                )
            )
        else:
            return 2
    elif a.cmd == "observe":
        _p(observe_mod.observe(a.song_dir))
    elif a.cmd == "decide":
        _p(
            observe_mod.decide(
                a.song_dir,
                auto_approve_technical=a.auto_tech,
                policy="unattended" if a.unattended else "taste",
            )
        )
    elif a.cmd == "qc":
        _p(qc_mod.qc_report(a.song_dir))
    elif a.cmd == "cycle":
        _p(
            observe_mod.run_cycle(
                a.song_dir,
                s1_remote=a.s1_remote,
                execute=a.execute,
                max_sec=a.max_sec,
                no_prompt=not a.allow_prompt,
                plan_if_ready=not a.no_plan,
                policy="unattended" if a.unattended else "taste",
                compose_if_missing=a.compose,
                genre=a.genre,
            )
        )
    elif a.cmd == "run-unattended":
        _p(
            observe_mod.run_full_unattended(
                a.song_dir,
                s1_remote=a.s1_remote,
                name=a.name,
                genre=a.genre,
                max_sec=a.max_sec,
                parts=a.parts,
                prefer_import=a.prefer_import,
                skip_s1_hands=a.brain_only,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
