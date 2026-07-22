import fitz, json, re
from pathlib import Path

agent = Path(__file__).resolve().parent / "msp-techniques-github-agent"
pdf = agent / "knowledge" / "Theory_and_Technique_of_Electronic_Music.pdf"
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
(k / "manual_extract.txt").write_text("\n\n".join(parts), encoding="utf-8")
(k / "page_index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
print("extract", (k / "manual_extract.txt").stat().st_size)

for row in index[:45]:
    print(f"P{row['page']:03d} ({row['chars']:5d}): {row['head'][:160]}")
print("---")
for row in index[45::15]:
    print(f"P{row['page']:03d} ({row['chars']:5d}): {row['head'][:160]}")

# chapter starts
for i in range(doc.page_count):
    t = doc[i].get_text("text")
    if re.match(r"\s*Chapter\s+\d+", t) or re.match(r"\s*\d+\s+[A-Z][a-z]+", t[:80]):
        first = t.strip().splitlines()[:3]
        if any("Chapter" in x or re.match(r"^\d+\s+[A-Z]", x) for x in first):
            print("MARK", i + 1, " | ".join(first)[:120])
