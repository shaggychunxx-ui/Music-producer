"""
Persistent listen log + rolling taste profile for Music-producer.

Purpose
-------
Accumulate *your* listening preferences (refs you rate) so new songs can
inherit a default brief (mood, BPM band, mix shape, genre) without cloning
melodies. Audio files stay local / out of git; only metadata + numeric
fingerprints + tags live here.

Storage (under song-creation-pipeline-github-agent/taste_data/)
  listen_log.jsonl   — append-only listens
  taste_profile.json — rolling aggregate used by apply-brief

Ratings
  love | ok | no | unrated
  Weighted into the profile (love strong, no drives anti-goals).
"""

from __future__ import annotations

import json
import random
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence

from song_pipeline_kb.compose import GENRE_PROFILES
from song_pipeline_kb.song_state import append_notes, init_song, load_gates, set_gate

# Package root: .../song-creation-pipeline-github-agent/
_PKG_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TASTE_DIR = _PKG_ROOT / "taste_data"
LISTEN_LOG_NAME = "listen_log.jsonl"
PROFILE_NAME = "taste_profile.json"
REF_SET_SIZE = 10

RATINGS = ("love", "ok", "no", "unrated")
RATING_WEIGHT = {
    "love": 1.0,
    "ok": 0.45,
    "unrated": 0.12,
    "no": 0.0,  # excluded from positive means; used for anti-goals
}

BAND_KEYS = ("sub", "low", "lowmid", "mid", "himid", "high", "air")

# GitStatus phone captures land as source=spotify_phone.
# This PC (WASAPI loopback) uses source=spotify_pc.
# Older local loopback clips used spotify_clip.
SPOTIFY_SOURCES = frozenset({"spotify_phone", "spotify_pc", "spotify_clip", "spotify"})
_PLACEHOLDER_ARTISTS = frozenset({"", "spotify capture", "spotify", "unknown"})
_PLACEHOLDER_TITLES = frozenset({"", "unknown"})

# Map free tags / mood words → compose genre profiles
_GENRE_HINTS: Dict[str, tuple[str, ...]] = {
    "dark_pulse": ("dark", "pulse", "minor", "brooding", "cinematic", "moody"),
    "trap": ("trap", "808", "hihat", "drill"),
    "house": ("house", "four-on-floor", "club", "dance"),
    "ambient": ("ambient", "sparse", "pad", "drone", "atmospheric"),
}


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _new_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{stamp}-{secrets.token_hex(3)}"


def taste_dir(path: Optional[Path] = None) -> Path:
    d = Path(path) if path else DEFAULT_TASTE_DIR
    d.mkdir(parents=True, exist_ok=True)
    return d


def listen_log_path(data_dir: Optional[Path] = None) -> Path:
    return taste_dir(data_dir) / LISTEN_LOG_NAME


def profile_path(data_dir: Optional[Path] = None) -> Path:
    return taste_dir(data_dir) / PROFILE_NAME


def empty_profile() -> Dict[str, Any]:
    return {
        "version": 1,
        "updated_at": None,
        "listen_count": 0,
        "rated": {r: 0 for r in RATINGS},
        "preferred_bpm": None,
        "preferred_crest_db": None,
        "preferred_peak_db": None,
        "preferred_rms_db": None,
        "preferred_bands": None,
        "mood_lock": None,
        "listen_goals": [],
        "anti_goals": [],
        "genre_weights": {g: 0.0 for g in GENRE_PROFILES},
        "default_genre": "dark_pulse",
        "complexity_budget": "S",
        "mix_targets": {},
        "top_tags": [],
        "summary": "No listens yet — log refs with: python -m song_pipeline_kb taste listen ...",
        "source": "music-producer-taste",
    }


def _normalize_rating(raw: Optional[str]) -> str:
    if not raw:
        return "unrated"
    r = str(raw).strip().lower()
    aliases = {
        "like": "love",
        "yes": "love",
        "good": "love",
        "love": "love",
        "ok": "ok",
        "meh": "ok",
        "fine": "ok",
        "no": "no",
        "skip": "no",
        "hate": "no",
        "dislike": "no",
        "unrated": "unrated",
        "?": "unrated",
    }
    return aliases.get(r, r if r in RATINGS else "unrated")


def _normalize_fingerprint(fp: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not fp:
        return None
    out: Dict[str, Any] = {}
    for key in ("peak_db", "rms_db", "crest_db", "tempo_bpm", "duration_sec"):
        if fp.get(key) is not None:
            try:
                out[key] = float(fp[key])
            except (TypeError, ValueError):
                pass
    # accept peak / rms aliases
    if "peak_db" not in out and fp.get("peak") is not None:
        try:
            out["peak_db"] = float(fp["peak"])
        except (TypeError, ValueError):
            pass
    if "rms_db" not in out and fp.get("rms") is not None:
        try:
            out["rms_db"] = float(fp["rms"])
        except (TypeError, ValueError):
            pass
    if out.get("crest_db") is None and "peak_db" in out and "rms_db" in out:
        out["crest_db"] = round(out["peak_db"] - out["rms_db"], 3)
    if fp.get("key"):
        out["key"] = str(fp["key"]).strip()
    bands = fp.get("bands")
    if isinstance(bands, dict):
        cleaned = {}
        for b in BAND_KEYS:
            if bands.get(b) is not None:
                try:
                    cleaned[b] = float(bands[b])
                except (TypeError, ValueError):
                    pass
        if cleaned:
            # normalize if looks like raw energy
            total = sum(cleaned.values())
            if total > 0 and abs(total - 1.0) > 0.05:
                cleaned = {k: round(v / total, 4) for k, v in cleaned.items()}
            out["bands"] = cleaned
    return out or None


def _parse_tags(tags: Optional[Sequence[str] | str]) -> List[str]:
    if tags is None:
        return []
    if isinstance(tags, str):
        parts = re.split(r"[,;/|]+", tags)
        return [p.strip().lower() for p in parts if p.strip()]
    return [str(t).strip().lower() for t in tags if str(t).strip()]


def load_listens(
    data_dir: Optional[Path] = None,
    *,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    path = listen_log_path(data_dir)
    if not path.is_file():
        return []
    rows: List[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if limit is not None and limit > 0:
        return rows[-limit:]
    return rows


def is_spotify_listen(entry: Dict[str, Any]) -> bool:
    src = str(entry.get("source") or "").strip().lower()
    return src in SPOTIFY_SOURCES or "spotify" in src


def _is_named_ref(entry: Dict[str, Any]) -> bool:
    artist = str(entry.get("artist") or "").strip()
    title = str(entry.get("title") or "").strip()
    if artist.lower() in _PLACEHOLDER_ARTISTS and (
        title.lower() in _PLACEHOLDER_TITLES or title.lower().endswith(".wav")
    ):
        return False
    if not artist and title.lower().endswith(".wav"):
        return False
    return bool(artist or title)


def spotify_refs(
    data_dir: Optional[Path] = None,
    *,
    unique: bool = True,
    named_only: bool = False,
) -> List[Dict[str, Any]]:
    """Listens saved by GitStatus Spotify (and older spotify_clip rows)."""
    rows = [e for e in load_listens(data_dir) if is_spotify_listen(e)]
    if named_only:
        rows = [e for e in rows if _is_named_ref(e)]
    if not unique:
        return rows
    by_key: Dict[tuple[str, str], Dict[str, Any]] = {}
    for entry in rows:
        key = (
            str(entry.get("artist") or "").strip().lower(),
            str(entry.get("title") or "").strip().lower(),
        )
        by_key[key] = entry
    return sorted(by_key.values(), key=lambda e: str(e.get("ts") or ""))


def _clip_label(entry: Dict[str, Any]) -> str:
    bits = [x for x in (entry.get("artist"), entry.get("title")) if x]
    return " / ".join(bits) if bits else "(unnamed Spotify clip)"


def _clip_card(entry: Dict[str, Any]) -> Dict[str, Any]:
    fp = entry.get("fingerprint") if isinstance(entry.get("fingerprint"), dict) else {}
    return {
        "id": entry.get("id"),
        "ts": entry.get("ts"),
        "artist": entry.get("artist"),
        "title": entry.get("title"),
        "source": entry.get("source"),
        "rating": entry.get("rating"),
        "label": _clip_label(entry),
        "audio_path": entry.get("audio_path"),
        "bpm": fp.get("tempo_bpm"),
        "peak_db": fp.get("peak_db"),
        "rms_db": fp.get("rms_db"),
        "crest_db": fp.get("crest_db"),
        "bands": fp.get("bands"),
        "duration_sec": fp.get("duration_sec"),
    }


def _blend_clip_fingerprints(entries: List[Dict[str, Any]]) -> Dict[str, Any]:
    bpm_vals: List[float] = []
    crest_vals: List[float] = []
    peak_vals: List[float] = []
    rms_vals: List[float] = []
    band_acc: Dict[str, List[float]] = {b: [] for b in BAND_KEYS}
    for entry in entries:
        fp = entry.get("fingerprint") if isinstance(entry.get("fingerprint"), dict) else {}
        if fp.get("tempo_bpm") is not None:
            try:
                bpm_vals.append(float(fp["tempo_bpm"]))
            except (TypeError, ValueError):
                pass
        if fp.get("crest_db") is not None:
            try:
                crest_vals.append(float(fp["crest_db"]))
            except (TypeError, ValueError):
                pass
        if fp.get("peak_db") is not None:
            try:
                peak_vals.append(float(fp["peak_db"]))
            except (TypeError, ValueError):
                pass
        if fp.get("rms_db") is not None:
            try:
                rms_vals.append(float(fp["rms_db"]))
            except (TypeError, ValueError):
                pass
        bands = fp.get("bands") if isinstance(fp.get("bands"), dict) else {}
        for b in BAND_KEYS:
            if bands.get(b) is not None:
                try:
                    band_acc[b].append(float(bands[b]))
                except (TypeError, ValueError):
                    pass
    out: Dict[str, Any] = {}
    if bpm_vals:
        mean = sum(bpm_vals) / len(bpm_vals)
        out["tempo_bpm"] = round(mean, 1)
        out["bpm_range"] = {
            "mean": round(mean, 1),
            "min": round(max(60.0, min(bpm_vals) - 4), 1),
            "max": round(min(180.0, max(bpm_vals) + 4), 1),
        }
    if crest_vals:
        out["crest_db"] = round(sum(crest_vals) / len(crest_vals), 2)
    if peak_vals:
        out["peak_db"] = round(sum(peak_vals) / len(peak_vals), 2)
    if rms_vals:
        out["rms_db"] = round(sum(rms_vals) / len(rms_vals), 2)
    pref_bands = {
        b: round(sum(vs) / len(vs), 4) for b, vs in band_acc.items() if vs
    }
    if pref_bands:
        out["bands"] = pref_bands
    return out


def pick_spotify_reference_set(
    data_dir: Optional[Path] = None,
    *,
    count: int = REF_SET_SIZE,
) -> Dict[str, Any]:
    """Pick up to `count` random Spotify clips as the song's reference family."""
    pool = spotify_refs(data_dir, unique=False)
    named = [e for e in pool if _is_named_ref(e)]
    loves = [e for e in named if _normalize_rating(e.get("rating")) == "love"]
    # Prefer named clips; fall back to the full pool if needed.
    draw_from = named or pool
    if not draw_from:
        return {
            "ok": False,
            "error": "no Spotify refs in listen_log.jsonl",
            "requested": count,
            "hint": (
                "Play Spotify in Chrome on this PC or on the phone (GitStatus) "
                "so clips land in taste_data/listen_log.jsonl."
            ),
        }
    n = min(count, len(draw_from))
    chosen = random.sample(draw_from, n)
    chosen.sort(key=lambda e: str(e.get("ts") or ""))
    labels = [_clip_label(e) for e in chosen]
    primary = chosen[0]
    blend = _blend_clip_fingerprints(chosen)
    return {
        "ok": True,
        "requested": count,
        "picked": n,
        "pool": len(draw_from),
        "reference": (
            f"{n} random Spotify clips: " + "; ".join(labels) + " (fingerprint family; not clones)"
        ),
        "references": [_clip_card(e) for e in chosen],
        "listen": primary,
        "blend": blend,
        "source": "spotify_set",
        "count": len(pool),
        "named_count": len(named),
        "loved_named": len(loves),
    }


def pick_spotify_reference(
    data_dir: Optional[Path] = None,
    *,
    count: int = REF_SET_SIZE,
) -> Dict[str, Any]:
    """Default song refs: random set of Spotify clips (10 unless count is set)."""
    return pick_spotify_reference_set(data_dir, count=count)


def list_spotify_refs(
    data_dir: Optional[Path] = None,
    *,
    limit: int = 20,
) -> Dict[str, Any]:
    all_refs = spotify_refs(data_dir)
    shown = all_refs[-limit:] if limit else all_refs
    pick = pick_spotify_reference(data_dir)
    return {
        "count": len(all_refs),
        "pick": pick,
        "refs": [
            {
                "id": e.get("id"),
                "ts": e.get("ts"),
                "artist": e.get("artist"),
                "title": e.get("title"),
                "source": e.get("source"),
                "rating": e.get("rating"),
                "bpm": (e.get("fingerprint") or {}).get("tempo_bpm")
                if isinstance(e.get("fingerprint"), dict)
                else None,
            }
            for e in shown
        ],
    }


def load_profile(data_dir: Optional[Path] = None) -> Dict[str, Any]:
    path = profile_path(data_dir)
    if not path.is_file():
        return empty_profile()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return empty_profile()
    base = empty_profile()
    base.update(data if isinstance(data, dict) else {})
    return base


def save_profile(profile: Dict[str, Any], data_dir: Optional[Path] = None) -> Path:
    path = profile_path(data_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def _weighted_mean(pairs: Iterable[tuple[float, float]]) -> Optional[float]:
    num = 0.0
    den = 0.0
    for value, weight in pairs:
        if weight <= 0:
            continue
        num += value * weight
        den += weight
    if den <= 0:
        return None
    return num / den


def _guess_genre(entry: Dict[str, Any]) -> Optional[str]:
    hint = (entry.get("genre_hint") or "").strip().lower().replace("-", "_")
    if hint in GENRE_PROFILES:
        return hint
    blob = " ".join(
        [
            str(entry.get("title") or ""),
            str(entry.get("artist") or ""),
            str(entry.get("notes") or ""),
            " ".join(entry.get("tags") or []),
            str(entry.get("mood") or ""),
        ]
    ).lower()
    scores = {g: 0 for g in GENRE_PROFILES}
    for genre, words in _GENRE_HINTS.items():
        for w in words:
            if w in blob:
                scores[genre] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def rebuild_profile(data_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Recompute taste_profile.json from the full listen log."""
    listens = load_listens(data_dir)
    profile = empty_profile()
    profile["listen_count"] = len(listens)
    profile["updated_at"] = _utc()

    if not listens:
        save_profile(profile, data_dir)
        return profile

    rated_counts = {r: 0 for r in RATINGS}
    bpm_pairs: List[tuple[float, float]] = []
    crest_pairs: List[tuple[float, float]] = []
    peak_pairs: List[tuple[float, float]] = []
    rms_pairs: List[tuple[float, float]] = []
    band_acc: Dict[str, List[tuple[float, float]]] = {b: [] for b in BAND_KEYS}
    genre_scores: Dict[str, float] = {g: 0.0 for g in GENRE_PROFILES}
    tag_scores: Dict[str, float] = {}
    goals: Dict[str, float] = {}
    anti: Dict[str, float] = {}
    mood_scores: Dict[str, float] = {}

    for entry in listens:
        rating = _normalize_rating(entry.get("rating"))
        rated_counts[rating] = rated_counts.get(rating, 0) + 1
        w = RATING_WEIGHT.get(rating, 0.0)
        fp = entry.get("fingerprint") if isinstance(entry.get("fingerprint"), dict) else {}
        tags = _parse_tags(entry.get("tags"))
        mood = (entry.get("mood") or (fp.get("key") and f"key {fp['key']}") or "").strip()

        if rating == "no":
            for t in tags:
                anti[t] = anti.get(t, 0.0) + 1.0
            note = (entry.get("notes") or "").strip()
            if note:
                anti[note[:80]] = anti.get(note[:80], 0.0) + 0.5
            continue

        if w <= 0:
            continue

        if fp.get("tempo_bpm") is not None:
            try:
                bpm_pairs.append((float(fp["tempo_bpm"]), w))
            except (TypeError, ValueError):
                pass
        if fp.get("crest_db") is not None:
            try:
                crest_pairs.append((float(fp["crest_db"]), w))
            except (TypeError, ValueError):
                pass
        if fp.get("peak_db") is not None:
            try:
                peak_pairs.append((float(fp["peak_db"]), w))
            except (TypeError, ValueError):
                pass
        if fp.get("rms_db") is not None:
            try:
                rms_pairs.append((float(fp["rms_db"]), w))
            except (TypeError, ValueError):
                pass
        bands = fp.get("bands") if isinstance(fp.get("bands"), dict) else {}
        for b in BAND_KEYS:
            if bands.get(b) is not None:
                try:
                    band_acc[b].append((float(bands[b]), w))
                except (TypeError, ValueError):
                    pass

        genre = _guess_genre(entry)
        if genre:
            genre_scores[genre] = genre_scores.get(genre, 0.0) + w

        for t in tags:
            tag_scores[t] = tag_scores.get(t, 0.0) + w
            goals[t] = goals.get(t, 0.0) + w

        if mood:
            mood_scores[mood.lower()] = mood_scores.get(mood.lower(), 0.0) + w

    profile["rated"] = rated_counts

    bpm_mean = _weighted_mean(bpm_pairs)
    if bpm_mean is not None:
        # spread from weighted values
        vals = [v for v, w in bpm_pairs if w > 0]
        lo = min(vals) if vals else bpm_mean
        hi = max(vals) if vals else bpm_mean
        profile["preferred_bpm"] = {
            "mean": round(bpm_mean, 1),
            "min": round(max(60.0, lo - 4), 1),
            "max": round(min(180.0, hi + 4), 1),
        }

    crest_mean = _weighted_mean(crest_pairs)
    if crest_mean is not None:
        profile["preferred_crest_db"] = {"mean": round(crest_mean, 2)}
    peak_mean = _weighted_mean(peak_pairs)
    if peak_mean is not None:
        profile["preferred_peak_db"] = {"mean": round(peak_mean, 2)}
    rms_mean = _weighted_mean(rms_pairs)
    if rms_mean is not None:
        profile["preferred_rms_db"] = {"mean": round(rms_mean, 2)}

    pref_bands: Dict[str, float] = {}
    for b, pairs in band_acc.items():
        m = _weighted_mean(pairs)
        if m is not None:
            pref_bands[b] = round(m, 4)
    if pref_bands:
        profile["preferred_bands"] = pref_bands

    # genre default
    total_g = sum(genre_scores.values()) or 1.0
    profile["genre_weights"] = {
        g: round(genre_scores.get(g, 0.0) / total_g, 4) for g in GENRE_PROFILES
    }
    if any(genre_scores.values()):
        profile["default_genre"] = max(genre_scores, key=genre_scores.get)
    else:
        profile["default_genre"] = "dark_pulse"

    if mood_scores:
        profile["mood_lock"] = max(mood_scores, key=mood_scores.get)
    else:
        # fall back to genre mood text
        g = profile["default_genre"]
        profile["mood_lock"] = (GENRE_PROFILES.get(g) or {}).get("mood") or "dark minor"

    top_tags = sorted(tag_scores.items(), key=lambda kv: (-kv[1], kv[0]))[:12]
    profile["top_tags"] = [t for t, _ in top_tags]
    profile["listen_goals"] = [t for t, _ in sorted(goals.items(), key=lambda kv: -kv[1])[:8]]
    profile["anti_goals"] = [t for t, _ in sorted(anti.items(), key=lambda kv: -kv[1])[:8]]

    mix: Dict[str, Any] = {}
    if crest_mean is not None:
        mix["crest_db"] = round(crest_mean, 2)
    if peak_mean is not None:
        mix["peak_db"] = round(peak_mean, 2)
    if rms_mean is not None:
        mix["rms_db"] = round(rms_mean, 2)
    if pref_bands:
        # highlight strongest / weakest bands as plain goals
        strong = max(pref_bands, key=pref_bands.get)
        weak = min(pref_bands, key=pref_bands.get)
        mix["band_emphasis"] = strong
        mix["band_deemphasis"] = weak
    profile["mix_targets"] = mix

    # human summary
    bits = [f"{len(listens)} listen(s)"]
    loves = rated_counts.get("love", 0)
    if loves:
        bits.append(f"{loves} love")
    if profile.get("preferred_bpm"):
        bits.append(f"BPM ~{profile['preferred_bpm']['mean']}")
    if profile.get("mood_lock"):
        bits.append(f"mood: {profile['mood_lock']}")
    bits.append(f"genre: {profile['default_genre']}")
    if profile["listen_goals"]:
        bits.append("goals: " + ", ".join(profile["listen_goals"][:5]))
    if profile["anti_goals"]:
        bits.append("avoid: " + ", ".join(profile["anti_goals"][:4]))
    profile["summary"] = " · ".join(bits)

    save_profile(profile, data_dir)
    return profile


def log_listen(
    *,
    artist: str = "",
    title: str = "",
    rating: str = "unrated",
    source: str = "manual",
    url: Optional[str] = None,
    tags: Optional[Sequence[str] | str] = None,
    notes: str = "",
    mood: Optional[str] = None,
    genre_hint: Optional[str] = None,
    fingerprint: Optional[Dict[str, Any]] = None,
    audio_path: Optional[str] = None,
    data_dir: Optional[Path] = None,
    rebuild: bool = True,
) -> Dict[str, Any]:
    """Append one listen to the log and refresh the taste profile."""
    artist = (artist or "").strip()
    title = (title or "").strip()
    if not artist and not title:
        raise ValueError("artist and/or title required")

    entry: Dict[str, Any] = {
        "id": _new_id(),
        "ts": _utc(),
        "artist": artist,
        "title": title,
        "source": (source or "manual").strip().lower(),
        "url": (url or "").strip() or None,
        "rating": _normalize_rating(rating),
        "tags": _parse_tags(tags),
        "notes": (notes or "").strip(),
        "mood": (mood or "").strip() or None,
        "genre_hint": (genre_hint or "").strip().lower().replace("-", "_") or None,
        "fingerprint": _normalize_fingerprint(fingerprint),
        # local capture path only — never required; audio stays out of git
        "audio_path": (audio_path or "").strip() or None,
    }

    path = listen_log_path(data_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    profile = rebuild_profile(data_dir) if rebuild else load_profile(data_dir)
    return {"ok": True, "listen": entry, "profile_summary": profile.get("summary"), "log_path": str(path)}


def rate_listen(
    listen_id: str,
    rating: str,
    *,
    data_dir: Optional[Path] = None,
    notes: Optional[str] = None,
) -> Dict[str, Any]:
    """Update rating on an existing listen by id (rewrites jsonl)."""
    listen_id = listen_id.strip()
    rows = load_listens(data_dir)
    found = None
    for row in rows:
        if row.get("id") == listen_id:
            row["rating"] = _normalize_rating(rating)
            if notes is not None:
                row["notes"] = notes.strip()
            row["rated_at"] = _utc()
            found = row
            break
    if found is None:
        return {"ok": False, "error": f"listen id not found: {listen_id}"}

    path = listen_log_path(data_dir)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    profile = rebuild_profile(data_dir)
    return {"ok": True, "listen": found, "profile_summary": profile.get("summary")}


def brief_from_profile(
    profile: Optional[Dict[str, Any]] = None,
    *,
    data_dir: Optional[Path] = None,
    song_ref_override: Optional[str] = None,
) -> Dict[str, Any]:
    """Build a machine brief dict from the taste profile (+ optional song ref)."""
    profile = profile or load_profile(data_dir)
    genre = profile.get("default_genre") or "dark_pulse"
    if genre not in GENRE_PROFILES:
        genre = "dark_pulse"
    gp = GENRE_PROFILES[genre]
    bpm = profile.get("preferred_bpm") or {}
    bpm_mean = bpm.get("mean") if isinstance(bpm, dict) else None
    if bpm_mean is None:
        bpm_mean = gp.get("bpm")

    pick = pick_spotify_reference_set(data_dir, count=REF_SET_SIZE)
    blend = pick.get("blend") if pick.get("ok") else {}
    if isinstance(blend, dict):
        if blend.get("tempo_bpm") is not None:
            bpm_mean = blend["tempo_bpm"]
        if blend.get("bpm_range"):
            bpm = blend["bpm_range"]

    ref_line = song_ref_override
    if not ref_line:
        if pick.get("ok"):
            ref_line = pick["reference"]
        else:
            loves = [
                e
                for e in load_listens(data_dir)
                if _normalize_rating(e.get("rating")) == "love"
            ]
            if loves:
                last = loves[-1]
                bits = [x for x in (last.get("artist"), last.get("title")) if x]
                ref_line = " / ".join(bits) + " (taste profile; not a clone target)"
            else:
                ref_line = "TASTE PROFILE (no Spotify clips yet)"

    goals = list(profile.get("listen_goals") or [])
    anti = list(profile.get("anti_goals") or [])
    mood = profile.get("mood_lock") or gp.get("mood") or "dark minor"
    mix = dict(profile.get("mix_targets") or {})
    if isinstance(blend, dict):
        if blend.get("crest_db") is not None:
            mix["crest_db"] = blend["crest_db"]
        if blend.get("peak_db") is not None:
            mix["peak_db"] = blend["peak_db"]
        if blend.get("rms_db") is not None:
            mix["rms_db"] = blend["rms_db"]
        if blend.get("bands"):
            strong = max(blend["bands"], key=blend["bands"].get)
            weak = min(blend["bands"], key=blend["bands"].get)
            mix["band_emphasis"] = strong
            mix["band_deemphasis"] = weak

    brief = {
        "version": 1,
        "source": "spotify_clip_set",
        "applied_at": _utc(),
        "reference": ref_line,
        "references": pick.get("references") or [],
        "reference_count": pick.get("picked") or 0,
        "reference_waived": False,
        "mood_lock": mood,
        "listen_goals": goals,
        "anti_goals": anti,
        "complexity_budget": profile.get("complexity_budget") or "S",
        "genre": genre,
        "bpm": bpm_mean,
        "bpm_range": bpm if isinstance(bpm, dict) else None,
        "mix_targets": mix,
        "preferred_bands": (blend or {}).get("bands") or profile.get("preferred_bands"),
        "preferred_crest_db": (blend or {}).get("crest_db")
        or (profile.get("preferred_crest_db") or {}).get("mean"),
        "top_tags": profile.get("top_tags") or [],
        "profile_summary": profile.get("summary"),
        "notes": (
            f"Reference is a random set of {REF_SET_SIZE} Spotify clips "
            "(phone + this PC). Fingerprint only — do not clone melodies or riffs."
        ),
    }
    return brief


def apply_brief_to_song(
    song_dir: Path,
    *,
    data_dir: Optional[Path] = None,
    reference: Optional[str] = None,
    lock_gate: bool = False,
    force: bool = False,
) -> Dict[str, Any]:
    """
    Write BRIEF.json + NOTES from taste profile.
    Does not lock the brief gate unless lock_gate=True.
    """
    song = Path(song_dir)
    init_song(song)
    profile = load_profile(data_dir)
    if profile.get("listen_count", 0) <= 0 and not force:
        return {
            "ok": False,
            "error": "no GitStatus Spotify refs — play Spotify on the phone so GitStatus can save clips",
            "hint": "python -m song_pipeline_kb taste refs",
        }

    brief = brief_from_profile(profile, data_dir=data_dir, song_ref_override=reference)
    brief_path = song / "BRIEF.json"
    if brief_path.is_file() and not force:
        try:
            existing = json.loads(brief_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
        if existing.get("source") in {
            "taste_profile",
            "gitstatus_spotify",
            "spotify_clip_set",
        } and existing.get("locked_by_user"):
            return {
                "ok": False,
                "error": "BRIEF.json marked locked_by_user — pass --force to overwrite",
                "brief_path": str(brief_path),
            }

    brief_path.write_text(json.dumps(brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Also drop a human-readable fingerprint targets file (numbers only)
    fp_targets = {
        "from": "spotify_clip_set",
        "applied_at": brief["applied_at"],
        "tempo_bpm": brief.get("bpm"),
        "crest_db": brief.get("preferred_crest_db"),
        "peak_db": (brief.get("mix_targets") or {}).get("peak_db"),
        "rms_db": (brief.get("mix_targets") or {}).get("rms_db"),
        "bands": brief.get("preferred_bands"),
        "mood_lock": brief.get("mood_lock"),
        "genre": brief.get("genre"),
        "references": brief.get("references") or [],
    }
    (song / "ref_fingerprint.json").write_text(
        json.dumps(fp_targets, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    goals = ", ".join(brief.get("listen_goals") or []) or "(none yet)"
    anti = ", ".join(brief.get("anti_goals") or []) or "(none)"
    notes_block = (
        f"Taste brief applied ({brief['applied_at']})\n"
        f"  References ({brief.get('reference_count') or 0}): {brief['reference']}\n"
        f"  Mood lock: {brief['mood_lock']}\n"
        f"  Genre default: {brief['genre']} @ ~{brief.get('bpm')} BPM\n"
        f"  Goals: {goals}\n"
        f"  Avoid: {anti}\n"
        f"  Mix targets: {json.dumps(brief.get('mix_targets') or {})}\n"
        f"  Profile: {brief.get('profile_summary')}"
    )
    append_notes(song, notes_block)

    # Patch NOTES.md-style brief section if present with placeholders
    notes_p = song / "NOTES.txt"
    if notes_p.is_file():
        text = notes_p.read_text(encoding="utf-8", errors="replace")
        text2 = text
        text2 = re.sub(
            r"(- Reference (?:\(title \+ artist\) or WAIVED|\(GitStatus Spotify[^)]*\)):)\s*$",
            rf"\1 {brief['reference']}",
            text2,
            count=1,
            flags=re.M,
        )
        text2 = re.sub(
            r"(- Mood lock:)\s*$",
            rf"\1 {brief['mood_lock']}",
            text2,
            count=1,
            flags=re.M,
        )
        if text2 != text:
            notes_p.write_text(text2, encoding="utf-8")

    gates = load_gates(song)
    if lock_gate and gates.get("brief") != "locked":
        set_gate(song, "brief", "locked")
        gates = load_gates(song)

    return {
        "ok": True,
        "song_dir": str(song.resolve()),
        "brief_path": str(brief_path.resolve()),
        "ref_fingerprint_path": str((song / "ref_fingerprint.json").resolve()),
        "brief": brief,
        "gates": gates,
        "brief_locked": gates.get("brief") == "locked",
        "compose_hint": (
            f'python -m song_pipeline_kb compose --song-dir "{song}" '
            f'--genre {brief["genre"]}'
            + (f' --bpm {int(brief["bpm"])}' if brief.get("bpm") else "")
        ),
    }


def load_song_brief(song_dir: Path) -> Optional[Dict[str, Any]]:
    p = Path(song_dir) / "BRIEF.json"
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def status(data_dir: Optional[Path] = None) -> Dict[str, Any]:
    profile = load_profile(data_dir)
    recent = load_listens(data_dir, limit=5)
    spotify = list_spotify_refs(data_dir, limit=5)
    return {
        "taste_dir": str(taste_dir(data_dir).resolve()),
        "listen_log": str(listen_log_path(data_dir).resolve()),
        "profile_path": str(profile_path(data_dir).resolve()),
        "listen_count": profile.get("listen_count", 0),
        "spotify_ref_count": spotify.get("count", 0),
        "spotify_pick": spotify.get("pick"),
        "summary": profile.get("summary"),
        "default_genre": profile.get("default_genre"),
        "mood_lock": profile.get("mood_lock"),
        "recent": [
            {
                "id": e.get("id"),
                "artist": e.get("artist"),
                "title": e.get("title"),
                "rating": e.get("rating"),
                "ts": e.get("ts"),
            }
            for e in recent
        ],
        "profile": profile,
    }
