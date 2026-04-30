"""Phase A5 audit — Inventaire Markdown des Templates de bricks (frontmatter)."""
from __future__ import annotations
import io, json, re, sys
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Templates de Bricks")
OUT = Path(__file__).parent / "output"
OUT.mkdir(parents=True, exist_ok=True)

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def parse_fm(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        m2 = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
        if m2:
            k = m2.group(1); v = m2.group(2).strip().strip('"').strip("'")
            fm[k] = v
    return fm

entries = []
for p in sorted(ROOT.rglob("*.md")):
    if "00 - archives" in str(p): continue
    text = p.read_text(encoding="utf-8")
    fm = parse_fm(text)
    entries.append({
        "file": str(p.relative_to(ROOT)),
        "code": fm.get("code"),
        "title": fm.get("title"),
        "version": fm.get("version"),
        "template_version": fm.get("template_version"),
        "summary": fm.get("summary", "")[:80],
        "purpose": fm.get("purpose", "")[:80],
    })

(OUT / "templates_bricks_md.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total: {len(entries)} .md")
print(f"With code: {sum(1 for e in entries if e['code'])}")
print(f"With title: {sum(1 for e in entries if e['title'])}")
print(f"With summary: {sum(1 for e in entries if e['summary'])}")
print(f"With purpose: {sum(1 for e in entries if e['purpose'])}")
print(f"With version: {sum(1 for e in entries if e['version'])}")
print(f"With template_version: {sum(1 for e in entries if e['template_version'])}")
print()
for e in entries:
    print(f"  {e['code']:30s} | v{e['version']:4s} | {e['title']}")
