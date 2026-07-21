"""Structured transcription of Pirate.com genre recording/mixing article."""

from __future__ import annotations

from typing import Any

ARTICLE = {
    "title": "Recording and Mixing Techniques for Different Music Genres",
    "author": "Will Bradbury",
    "date": "2024-10-31",
    "site": "Pirate.com / Pirate Studios",
    "url": "https://pirate.com/en/blog/recording-mixing-techniques-different-genres/",
    "thesis": (
        "Production conventions make genres sound different beyond musical content. "
        "Recording and mixing should follow genre intent and listening context."
    ),
    "related_links": [
        "https://pirate.com/en/blog/music-production/",
        "https://pirate.com/en/blog/how-to-mix-music/",
        "https://pirate.com/en/blog/essential-recording-studio-equipment/",
        "https://pirate.com/en/blog/vst-plugins/",
        "https://pirate.com/en/blog/how-to-sample-a-song/",
        "https://pirate.com/en/blog/ai-tools-music-production/",
    ],
    "recording_vs_mixing": {
        "recording": (
            "Everything until audio is a file in the DAW: amps, mics (condenser vs ribbon), "
            "performance and room capture."
        ),
        "mixing": (
            "DAW-stage balancing/refinement. Primary tools: EQ, compression, FX, panning."
        ),
    },
    "mix_approaches": {
        "bottom_up": {
            "summary": "Start with individual tracks; precise control; good for complex projects.",
            "steps": [
                "Focus kick/bass/vocal (or key stems) first",
                "Balance each element before bus glue",
                "Reduce later frequency/dynamic conflicts",
            ],
        },
        "top_down": {
            "summary": "Shape whole mix/bus first; establish vibe; common in pop/electronic.",
            "steps": [
                "Bus compressor/EQ/saturation on mix",
                "Then refine individuals",
                "Avoid over-processing every track",
            ],
        },
    },
    "notable_gear": [
        {"name": "Big Muff Pi", "type": "fuzz pedal", "users": "Nirvana, Muse, Hendrix, Smashing Pumpkins"},
        {"name": "Pro Co RAT", "type": "distortion pedal", "users": "Blur, Arctic Monkeys, Radiohead"},
        {"name": "UA 1176", "type": "compressor/limiter", "users": "Rock (Green Day, Nirvana, etc.)"},
        {"name": "Antares Auto-Tune", "type": "pitch", "users": "Pop/hip-hop broadly"},
        {"name": "Pultec EQP-1A", "type": "tube EQ", "users": "Industry standard (Daft Punk to Calvin Harris cited)"},
        {"name": "Bricasti M7", "type": "reverb", "users": "Al Schmitt jazz/pop"},
        {"name": "Eventide H3000", "type": "multi FX", "users": "Brian Eno"},
        {"name": "Valhalla VintageVerb", "type": "reverb plugin", "users": "Cross-genre popular"},
        {"name": "Neve 1073", "type": "preamp", "users": "Rock analogue character (article)"},
        {"name": "Altiverb-class convolution", "type": "reverb", "users": "Classical/jazz natural spaces"},
    ],
    "closing": [
        "No absolute right/wrong — justify technique vs intent",
        "Keep a personal notes list of likes/dislikes",
        "Stay current with plugins and AI production tools",
    ],
}

TOOLS: dict[str, dict[str, Any]] = {
    "eq": {
        "name": "EQ (Equalisation)",
        "role": "Shape/sculpt frequency content",
        "general": "Cut mud (lows), boost presence (mids), control harshness (highs).",
        "by_genre": {
            "pop": "Bright polished highs; controlled mids; clarity and punch",
            "metal": "Surgical carve for guitars/drums; emphasize low mids + highs for impact",
            "jazz_classical": "Minimal, preservational",
        },
        "question": "What should come forward? What feeling?",
    },
    "compression": {
        "name": "Compression",
        "role": "Reduce dynamic range; add punch/glue",
        "general": "Attenuate above threshold; attack/release/ratio matter; buses vs tracks.",
        "by_genre": {
            "hip_hop_electronic": "Heavier for punchy kick/bass",
            "jazz_classical": "Subtle or none; keep natural dynamics",
            "rock": "Parallel/NY compression on drums common",
            "dance": "Sidechain to kick for pumping",
        },
        "warning": "Over-compress → dull/squashed",
    },
    "fx": {
        "name": "FX (reverb, chorus, saturation…)",
        "role": "Depth, texture, character",
        "by_genre": {
            "shoegaze": "Heavy reverb + chorus wash",
            "classical": "Minimal; natural acoustics",
            "rock": "Plate/hall on guitars varies by vibe",
            "experimental": "Often applied pre-record rather than mix 'fix'",
        },
    },
    "panning": {
        "name": "Panning / stereo field",
        "role": "Space and separation; L/R or mid-side",
        "by_genre": {
            "orchestral": "Stage-realistic placement",
            "electronic": "Creative motion and width",
            "modern": "M/S processing for width vs focus",
        },
    },
    "recording": {
        "name": "Recording technique",
        "role": "Capture before DAW",
        "examples": [
            "Rock: amp choice defines guitar",
            "Modern detail: condensers",
            "Jazz quartet warmth: ribbons",
            "Acoustic genres: room + placement first",
        ],
    },
}

GENRES: dict[str, dict[str, Any]] = {
    "folk_acoustic": {
        "name": "Folk / intimate acoustic (intro case)",
        "intent": "Purity of voice and songwriting; sparse accompaniment",
        "recording": ["Natural capture", "Minimal intervention", "May keep room noise for atmosphere"],
        "mixing": ["Light processing", "Wide dynamic range", "Home-listening dynamics"],
        "listening_context": "Home environment",
    },
    "drum_and_bass": {
        "name": "Drum & bass / club-warped electronic (intro case)",
        "intent": "Hard system impact; radical processing of sources",
        "mixing": ["Heavy compression", "Careful EQ", "Club-volume translation"],
        "listening_context": "Large sound system",
    },
    "rock": {
        "name": "Rock / Indie",
        "intent": "Impact + increasingly polished immersion",
        "recording": ["Distorted amps/mics", "Possible vocal distortion (Strokes Is This It)"],
        "mixing": [
            "Layer guitars with different FX/pan",
            "Parallel/New York compression on drums (Chris Lord-Alge)",
            "Analogue-style saturation (1073, 1176)",
            "Plate to hall reverb on guitars",
        ],
        "keywords": ["distortion", "parallel compression", "analogue warmth"],
    },
    "pop": {
        "name": "Pop",
        "intent": "Polished, chart-ready clarity",
        "mixing": [
            "Creative Autotune as effect",
            "Stacked processed harmonies",
            "Surgical EQ (Max Martin-style vocal clarity)",
            "Often top-down bus polish",
        ],
        "keywords": ["autotune", "harmonies", "surgical EQ"],
    },
    "hip_hop": {
        "name": "Hip-hop",
        "intent": "Punchy, upfront, sample-driven culture",
        "mixing": [
            "Heavy compression for punch",
            "Sampling as composition/production core",
            "808-driven low end",
            "Autotune/creative vocal processing common in modern styles",
        ],
        "keywords": ["808", "sample", "compression"],
    },
    "rnb": {
        "name": "R&B",
        "intent": "High-production polish shared with pop/hip-hop",
        "mixing": ["Vocal-forward processing", "Harmonies", "808/beat-driven low end as relevant"],
        "keywords": ["vocal polish", "harmonies"],
    },
    "dance": {
        "name": "Dance / electronic club music",
        "intent": "Clarity and impact on large (often mono) systems",
        "mixing": [
            "Frequent mono compatibility checks",
            "Split sub-bass and mid-bass",
            "Sidechain compression to kick (pumping; creative ghost-kick uses)",
            "Heavy automation for melodies/drops",
        ],
        "keywords": ["sidechain", "mono", "sub bass", "automation"],
    },
    "jazz": {
        "name": "Jazz",
        "intent": "Natural interplay and dynamics",
        "recording": ["Room + careful mic placement (Al Schmitt)", "Ribbons for warm natural"],
        "mixing": ["Minimal compression/EQ", "Natural/convolution reverb spaces"],
        "keywords": ["room", "dynamics", "minimal processing"],
    },
    "classical": {
        "name": "Classical",
        "intent": "Virtuosity + acoustic space; emotional dynamic range",
        "recording": ["Hall/room capture", "Placement over heavy processing"],
        "mixing": ["Minimal FX", "Preserve wide dynamics", "Convolution halls"],
        "keywords": ["dynamics", "natural reverb"],
    },
    "experimental": {
        "name": "Experimental",
        "intent": "Immersive or unconventional soundscapes",
        "recording": ["Maximal processing often pre-recording"],
        "mixing": ["Avoid killing character with corrective 'fixing'", "Ambient samples for immersion"],
        "keywords": ["soundscape", "pre-process"],
    },
    "metal": {
        "name": "Heavy metal (EQ example in article)",
        "intent": "Intense, gut-hitting clarity among dense guitars/drums",
        "mixing": ["Surgical EQ carve for guitars/drums", "Emphasize low mids and highs"],
        "keywords": ["surgical EQ", "aggression"],
    },
    "shoegaze": {
        "name": "Shoegaze (FX example)",
        "intent": "Ethereal washed textures",
        "mixing": ["Heavy reverb and chorus"],
        "keywords": ["reverb", "chorus"],
    },
}


def list_genres() -> list[str]:
    return list(GENRES.keys())


def get_genre(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")
    aliases = {
        "indie": "rock",
        "rock_indie": "rock",
        "dnb": "drum_and_bass",
        "d_and_b": "drum_and_bass",
        "edm": "dance",
        "electronic": "dance",
        "house": "dance",
        "techno": "dance",
        "hiphop": "hip_hop",
        "rap": "hip_hop",
        "r_and_b": "rnb",
        "r&b": "rnb",
        "folk": "folk_acoustic",
        "acoustic": "folk_acoustic",
        "singer_songwriter": "folk_acoustic",
        "orchestra": "classical",
        "heavy_metal": "metal",
    }
    key = aliases.get(key, key)
    if key not in GENRES:
        for k, v in GENRES.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown genre '{name}'. Try: {', '.join(list_genres())}")
    return GENRES[key]


def get_tool(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_")
    aliases = {
        "equalization": "eq",
        "equaliser": "eq",
        "compressor": "compression",
        "reverb": "fx",
        "effects": "fx",
        "pan": "panning",
        "stereo": "panning",
        "mic": "recording",
        "mics": "recording",
    }
    key = aliases.get(key, key)
    if key not in TOOLS:
        raise KeyError(f"Unknown tool '{name}'. Try: {', '.join(TOOLS)}")
    return TOOLS[key]
