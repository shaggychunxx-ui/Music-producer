#!/usr/bin/env python3
"""Download a public Google Drive file by ID."""
from __future__ import annotations

import re
import sys
from pathlib import Path

FILE_ID = "10rxiXHuJ9Oz89ByD5pEcgMr2Ax8E8y5z"
OUT_DIR = Path(__file__).resolve().parent / "_download_tmp"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> int:
    try:
        import requests
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
        import requests

    s = requests.Session()
    url = "https://drive.google.com/uc"
    params = {"export": "download", "id": FILE_ID}
    r = s.get(url, params=params, stream=True, timeout=180)
    print("pass1", r.status_code, r.headers.get("Content-Type"), r.headers.get("Content-Disposition"))

    # virus-scan / large file interstitial
    if "text/html" in (r.headers.get("Content-Type") or ""):
        text = r.text
        # save html for debug
        (OUT_DIR / "interstitial.html").write_text(text[:50000], encoding="utf-8", errors="ignore")
        token = None
        m = re.search(r"confirm=([0-9A-Za-z_-]+)", text)
        if m:
            token = m.group(1)
        uuid = None
        m_uuid = re.search(r'name="uuid"\s+value="([^"]+)"', text)
        if m_uuid:
            uuid = m_uuid.group(1)
        # form action download
        params2 = {"export": "download", "id": FILE_ID, "confirm": token or "t"}
        if uuid:
            params2["uuid"] = uuid
        r = s.get(url, params=params2, stream=True, timeout=600)
        print("pass2", r.status_code, r.headers.get("Content-Type"), r.headers.get("Content-Disposition"))

    # cookie-based confirm
    for k, v in list(s.cookies.items()):
        if "download" in k.lower() or k.startswith("download_warning"):
            r = s.get(url, params={"export": "download", "id": FILE_ID, "confirm": v}, stream=True, timeout=600)
            print("cookie confirm", r.status_code, r.headers.get("Content-Type"), r.headers.get("Content-Disposition"))

    cd = r.headers.get("Content-Disposition") or ""
    fname = "drive_file.bin"
    m = re.search(r'filename\*=UTF-8\'\'([^;]+)', cd) or re.search(r'filename="?([^";]+)"?', cd)
    if m:
        from urllib.parse import unquote

        fname = unquote(m.group(1).strip())

    out = OUT_DIR / fname
    size = 0
    with open(out, "wb") as f:
        for chunk in r.iter_content(1024 * 256):
            if chunk:
                f.write(chunk)
                size += len(chunk)
    print("saved", out, "bytes", size)

    # sniff type
    head = out.read_bytes()[:16]
    print("magic", head[:8])
    if head.startswith(b"%PDF"):
        print("TYPE=PDF")
    elif head[:2] == b"PK":
        print("TYPE=ZIP/OOXML")
    return 0 if size > 1000 else 1


if __name__ == "__main__":
    raise SystemExit(main())
