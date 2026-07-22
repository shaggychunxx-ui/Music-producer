import fitz, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
pdf = ROOT / "movement-github-agent" / "knowledge" / "Movement_User_Guide.pdf"
if not pdf.exists():
    pdf = ROOT / "_download_tmp" / "Movement_User_Guide.pdf"
if not pdf.exists():
    raise SystemExit(f"Missing Movement PDF under knowledge/ or _download_tmp/")
doc = fitz.open(pdf)
print("pages", doc.page_count)
parts = []
index = []
for i in range(doc.page_count):
    t = doc[i].get_text("text")
    parts.append(f"---PAGE {i+1}---\n{t}")
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
    index.append({"page": i + 1, "head": " | ".join(lines[:10])[:220]})

base = ROOT / "movement-github-agent"
(base / "knowledge").mkdir(parents=True, exist_ok=True)
(base / "knowledge" / "Movement_User_Guide.pdf").write_bytes(pdf.read_bytes())
(base / "knowledge" / "manual_extract.txt").write_text("\n\n".join(parts), encoding="utf-8")
(base / "knowledge" / "page_index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
print("extract", (base / "knowledge" / "manual_extract.txt").stat().st_size)
for row in index:
    print(f"P{row['page']:03d}: {row['head'][:180]}")
