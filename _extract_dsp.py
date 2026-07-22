import fitz, json, re
from pathlib import Path

agent = Path(__file__).resolve().parent / "dsp-wiley-github-agent"
pdf = agent / "knowledge" / "Wiley_Digital_Audio_Signal_Processing_2nd_Edition.pdf"
doc = fitz.open(pdf)
print("pages", doc.page_count)
parts = []
index = []
for i in range(doc.page_count):
    t = doc[i].get_text("text") or ""
    parts.append(f"---PAGE {i+1}---\n{t}")
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
    index.append({"page": i + 1, "head": " | ".join(lines[:10])[:220], "chars": len(t)})

k = agent / "knowledge"
k.mkdir(parents=True, exist_ok=True)
(k / "manual_extract.txt").write_text("\n\n".join(parts), encoding="utf-8")
(k / "page_index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
print("extract_chars", (k / "manual_extract.txt").stat().st_size)

# Find TOC-like pages and chapter starts
for row in index[:50]:
    print(f"P{row['page']:03d} ({row['chars']:5d}): {row['head'][:160]}")
print("--- sample ---")
for row in index[50::25]:
    print(f"P{row['page']:03d} ({row['chars']:5d}): {row['head'][:160]}")

# Extract early front matter + TOC for structure
front = []
for i in range(min(40, doc.page_count)):
    front.append(doc[i].get_text("text"))
(k / "front_matter.txt").write_text("\n=====\n".join(front), encoding="utf-8")
print("front_matter chars", (k / "front_matter.txt").stat().st_size)
