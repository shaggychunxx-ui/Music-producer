from __future__ import annotations

import argparse
import json
from pathlib import Path

from clip_edit_kb import RECIPES, SKIPPED, SOURCE, TOOLS, get_recipe, get_tool, search_kb
from clip_edit_kb.ffmpeg_ops import (
    _need,
    cmd_extract_audio,
    cmd_grain,
    cmd_loop,
    cmd_mux,
    cmd_prepare_s1,
    cmd_qc,
    cmd_remux,
    cmd_rife,
    cmd_stitch,
)


def _p(o):
    print(json.dumps(o, indent=2, ensure_ascii=False) if isinstance(o, (dict, list)) else o)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="clip_edit_kb")
    s = p.add_subparsers(dest="cmd", required=True)

    s.add_parser("info")
    s.add_parser("recipes")
    s.add_parser("tools")
    rec = s.add_parser("recipe")
    rec.add_argument("name")
    tl = s.add_parser("tool")
    tl.add_argument("name")
    q = s.add_parser("search")
    q.add_argument("query")
    q.add_argument("--limit", type=int, default=20)

    ex = s.add_parser("extract-audio", help="48 kHz PCM wav from a video")
    ex.add_argument("src", type=Path)
    ex.add_argument("-o", "--out", type=Path)

    lp = s.add_parser("loop", help="Ping-pong visualizer; xfade at reverse; video-only")
    lp.add_argument("src", type=Path)
    lp.add_argument("-o", "--out", type=Path)
    lp.add_argument("--fade", type=float, default=0.18)

    st = s.add_parser("stitch", help="Join A then B with skip-B + short xfade")
    st.add_argument("a", type=Path)
    st.add_argument("b", type=Path)
    st.add_argument("-o", "--out", type=Path)
    st.add_argument("--skip-b", type=float, default=0.30)
    st.add_argument("--fade", type=float, default=0.20)

    mx = s.add_parser("mux", help="Attach bounced master to a silent visualizer")
    mx.add_argument("video", type=Path)
    mx.add_argument("audio", type=Path)
    mx.add_argument("-o", "--out", type=Path)

    pr = s.add_parser("prepare-s1", help="Constant-fps mp4 + 48 kHz wav sidecar")
    pr.add_argument("src", type=Path)
    pr.add_argument("-o", "--out-dir", type=Path)
    pr.add_argument("--song-dir", type=Path, help="Copy outputs into this Song folder")
    pr.add_argument("--fps", type=float)

    qc = s.add_parser("qc", help="Dump frames at 0/25/50/75/end")
    qc.add_argument("src", type=Path)
    qc.add_argument("-o", "--out", type=Path)

    gr = s.add_parser("grain", help="Fine grain after RIFE")
    gr.add_argument("src", type=Path)
    gr.add_argument("-o", "--out", type=Path)
    gr.add_argument("--strength", type=int, default=8)

    rm = s.add_parser("remux", help="Copy remux, strip metadata / C2PA-style boxes")
    rm.add_argument("src", type=Path)
    rm.add_argument("-o", "--out", type=Path)

    rf = s.add_parser("rife", help="Comfy RIFE 4x to 60fps (needs :8189)")
    rf.add_argument("src", type=Path)
    rf.add_argument("-o", "--out", type=Path)

    a = p.parse_args(argv)

    if a.cmd == "info":
        _p({"source": SOURCE, "tools": sorted(TOOLS), "skipped": SKIPPED, "recipes": sorted(RECIPES)})
        return 0
    if a.cmd == "recipes":
        print(", ".join(sorted(RECIPES)))
        return 0
    if a.cmd == "tools":
        _p({k: v.get("use") for k, v in TOOLS.items()})
        return 0
    if a.cmd == "recipe":
        hit = get_recipe(a.name)
        if not hit:
            print("unknown recipe. Available:", ", ".join(sorted(RECIPES)))
            return 2
        _p(hit)
        return 0
    if a.cmd == "tool":
        hit = get_tool(a.name)
        if not hit:
            print("unknown tool. Available:", ", ".join(sorted(TOOLS)))
            return 2
        _p(hit)
        return 0
    if a.cmd == "search":
        _p(search_kb(a.query, a.limit))
        return 0

    if a.cmd == "extract-audio":
        src = _need(a.src)
        dest = a.out or src.with_suffix(".wav")
        return cmd_extract_audio(src, dest)
    if a.cmd == "loop":
        src = _need(a.src)
        dest = a.out or src.with_name(src.stem.replace("-loop", "") + "-loop.mp4")
        return cmd_loop(src, dest, a.fade)
    if a.cmd == "stitch":
        dest = a.out or a.a.with_name(a.a.stem + "-stitched.mp4")
        return cmd_stitch(_need(a.a), _need(a.b), dest, a.skip_b, a.fade)
    if a.cmd == "mux":
        dest = a.out or a.video.with_name(a.video.stem + "-mux.mp4")
        return cmd_mux(_need(a.video), _need(a.audio), dest)
    if a.cmd == "prepare-s1":
        src = _need(a.src)
        dest_dir = a.song_dir or a.out_dir or (src.parent / f"{src.stem}-s1")
        return cmd_prepare_s1(src, dest_dir, fps=a.fps)
    if a.cmd == "qc":
        return cmd_qc(_need(a.src), a.out)
    if a.cmd == "grain":
        src = _need(a.src)
        dest = a.out or src.with_name(src.stem + "-grain.mp4")
        return cmd_grain(src, dest, a.strength)
    if a.cmd == "remux":
        src = _need(a.src)
        dest = a.out or src.with_name(src.stem + ".noc2pa" + src.suffix)
        return cmd_remux(src, dest)
    if a.cmd == "rife":
        src = _need(a.src)
        dest = a.out or src.with_name(src.stem.replace("-60fps", "") + "-60fps.mp4")
        return cmd_rife(src, dest)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
