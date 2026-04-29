"""
Phase A4.B — Parse "Usages des taxonomies" section in each manuel de BDD.

For each .md under Manuels de BDD/{Brain,Digital Twin,Mission Ops}/ (excl 00-archives, WR-RD/),
locate the section header `# N) Usages des taxonomies...` (any N), capture content until
next `# M)` header, extract unique taxo codes matching <NS>.<TAXO>.

Output: scripts/phase_a4/output/manuel_taxos_extracted.json
  [{"file": "...", "scope": "Brain|Twin|MO", "title": "...", "section": 5, "codes": [...]}]
"""
from __future__ import annotations
import io, json, re, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Manuels de BDD")
OUT = Path(__file__).parent / "output" / "manuel_taxos_extracted.json"

SCOPES = {"Brain": "Brain", "Digital Twin": "Twin", "Mission Ops": "MO"}
SECTION_RE = re.compile(r"^# (\d+)\)\s*Usages des taxonomies", re.MULTILINE)
NEXT_SECTION_RE = re.compile(r"^# \d+\)", re.MULTILINE)
CODE_RE = re.compile(r"\b([A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]*)\b")
TITLE_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)


def extract_codes_from_section(text: str) -> tuple[int | None, list[str]]:
    m = SECTION_RE.search(text)
    if not m:
        return None, []
    section_num = int(m.group(1))
    start = m.end()
    # Find next top-level section header
    nxt = NEXT_SECTION_RE.search(text, start)
    end = nxt.start() if nxt else len(text)
    body = text[start:end]
    # Drop lines that are header style/comment hints if any — keep table content
    codes = sorted(set(CODE_RE.findall(body)))
    # Filter false positives: typical false hits would be e.g. "OPS.STATUS" if same scheme — keep as-is.
    return section_num, codes


def main():
    entries = []
    for scope_dir, scope_label in SCOPES.items():
        d = ROOT / scope_dir
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            try:
                text = p.read_text(encoding="utf-8")
            except Exception as e:
                entries.append({"file": str(p.relative_to(ROOT)), "scope": scope_label, "error": str(e)})
                continue
            tm = TITLE_RE.search(text)
            title = tm.group(1).strip().strip('"').strip("'") if tm else p.stem
            section, codes = extract_codes_from_section(text)
            entries.append({
                "file": str(p.relative_to(ROOT)),
                "scope": scope_label,
                "title": title,
                "section": section,
                "codes": codes,
                "n_codes": len(codes),
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} manuels → {OUT}")
    for e in entries:
        flag = "" if e.get("section") else " [NO SECTION]"
        print(f"  [{e['scope']}] {e.get('title','?')} :: section {e.get('section')} :: {e.get('n_codes',0)} codes{flag}")


if __name__ == "__main__":
    main()
