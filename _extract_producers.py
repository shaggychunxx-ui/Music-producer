import fitz, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
agent = ROOT / "producers-genre-guide-github-agent"
pdf = agent / "knowledge" / "Music_Producers_Genre_Guide.pdf"
if not pdf.exists():
    raise SystemExit(f"Missing PDF: {pdf}")

doc = fitz.open(pdf)
print("pages", doc.page_count)
parts = []
index = []
for i in range(doc.page_count):
    t = doc[i].get_text("text") or ""
    parts.append(f"---PAGE {i+1}---\n{t}")
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
    index.append({"page": i + 1, "head": " | ".join(lines[:14])[:260], "chars": len(t)})

k = agent / "knowledge"
(k / "manual_extract.txt").write_text("\n\n".join(parts), encoding="utf-8")
(k / "page_index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
print("extract", (k / "manual_extract.txt").stat().st_size)
for row in index:
    print(f"P{row['page']:03d} ({row['chars']:5d}): {row['head'][:180]}")
