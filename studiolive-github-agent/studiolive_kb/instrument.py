from __future__ import annotations
from typing import Any

INSTRUMENT = {
    "name": "PreSonus StudioLive Series III",
    "type": "Digital mix console / recorder with motorized faders",
    "manual": "StudioLive Series III Owner's Manual V6 EN (2019-10-06)",
    "source_url": "https://pae-web.presonusmusic.com/downloads/products/pdf/StudioLive_Series_III_OwnersManual_V6_EN_10062019.pdf",
    "pages": 157,
    "models": {
        "S": ["StudioLive 64S", "StudioLive 32S", "StudioLive 32SX", "StudioLive 32SC"],
        "Blue": ["StudioLive 32", "StudioLive 24", "StudioLive 16"],
        "blue_firmware": "v2.0 or later required for Blue models in this manual family",
        "illustration_default": "StudioLive 64S for shared features",
    },
    "toc": [
        "1 Overview",
        "2 Getting Started (level setting, useful concepts)",
        "3 Hookup (rear configs, I/O, band/church diagrams)",
        "4 Basic mix (channel strip, fader layers, Filter DCA, meters, talkback)",
        "5 Buses (FlexMixes, aux, subgroups, matrix, FX, mono/LCR on 64S)",
        "6 Fat Channel (gate/comp/EQ plugins, navigation, input, assignments)",
        "7 Tape / Bluetooth",
        "8 SD Recording & virtual soundcheck",
        "9 Master Control (FLEX DSP FX, UCNET, DAW, scenes/projects)",
        "10 Monitoring / Solo",
        "11 Graphic EQ & RTA ring-out",
        "12 Home (system, user profiles, digital patching, soft power)",
        "13 Resources (networking, mic placement, compression/EQ guides, delays, sidechain, FX types)",
        "14 Technical (specs, default routing, block diagrams, troubleshooting)",
    ],
    "key_concepts": [
        "Select buttons + Fat Channel",
        "Fat Channel plugins",
        "FlexMixes",
        "Fader layers / User layer",
        "DCA / Filter DCA groups",
        "Recording & playback (USB/SD)",
        "Digital patching",
        "Projects, scenes, presets",
        "User profiles & permissions",
    ],
}

TOPICS: dict[str, dict[str, Any]] = {
    "overview": {"name": "Overview & models", "summary": "Series III S and Blue models; shared workflows; 64S used in illustrations; companion PreSonus ecosystem."},
    "getting_started": {"name": "Getting started / gain", "summary": "Level setting procedure; useful concepts for first session."},
    "hookup": {"name": "Hookup & I/O", "summary": "Model rear panels; analog I/O; digital/networking; power; band/church setup diagrams."},
    "mix_basics": {"name": "Basic mix functions", "summary": "Channel strip; fader layers/banks; User layer; Filter DCA create/edit; main meters; talkback."},
    "buses": {"name": "Buses & routing", "summary": "FlexMixes; aux pre/post; external FX; subgroups (fixed on some 32-ch); matrix/front fill; FX buses; 64S mono/LCR."},
    "fat_channel": {"name": "Fat Channel", "summary": "Gate; Standard/Tube/FET compressors; Standard/Passive/Vintage EQ; A/B compare; copy/paste/presets; aux sends mode; input polarity/phantom/stereo link; bus assigns."},
    "sd_recording": {"name": "SD recording", "summary": "New session; load playback; Capture screen; transport; virtual soundcheck."},
    "scenes": {"name": "Scenes & projects", "summary": "Create/recall projects & scenes; filters; list editor; scene safe; AutoStore; reset; nulling parameters."},
    "ucnet": {"name": "UCNET & control", "summary": "Mixer nickname; permissions; software control; control network IP; transport; DAW button."},
    "fx": {"name": "FLEX DSP effects", "summary": "Effects editor; types; presets for internal bus FX."},
    "monitoring": {"name": "Solo / monitoring", "summary": "Solo modes; solo bus; solo-in-place for mix setup."},
    "geq": {"name": "Graphic EQ & RTA", "summary": "Assign GEQs; presets; use RTA to ring out monitors."},
    "patching": {"name": "Digital patching", "summary": "Input sources; analog/AVB/USB/SD/AES sends; default routing tables in tech chapter."},
    "profiles": {"name": "User profiles", "summary": "Administrator; create profiles; edit permissions."},
    "resources": {"name": "Mixing resources", "summary": "Mic placement; compression/EQ suggestions; input/output delay alignment; sidechain; effect type primers; RTA while mixing."},
    "troubleshooting": {"name": "Specs & troubleshooting", "summary": "Specifications, block diagrams, troubleshooting section."},
}

def list_topics():
    return list(TOPICS.keys())

def get_topic(name: str) -> dict[str, Any]:
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "fat": "fat_channel", "eq": "fat_channel", "compressor": "fat_channel",
        "flexmix": "buses", "aux": "buses", "matrix": "buses", "dca": "mix_basics",
        "scene": "scenes", "project": "scenes", "record": "sd_recording", "sd": "sd_recording",
        "network": "ucnet", "avb": "patching", "usb": "patching", "solo": "monitoring",
        "rta": "geq", "gain": "getting_started",
    }
    key = aliases.get(key, key)
    if key not in TOPICS:
        for k, v in TOPICS.items():
            if key in k or key in v["name"].lower():
                return v
        raise KeyError(f"Unknown topic {name}. Try: {', '.join(TOPICS)}")
    return TOPICS[key]
