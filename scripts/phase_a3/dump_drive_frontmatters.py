"""
Phase A3.0 — Dump frontmatters of all Notes de Concept Markdown files.

Reads every .md file in `Notes de Concept/` (excluding `00 - archives/`),
extracts YAML frontmatter, and writes a JSON dump for cross-matching against
Notion BDDs (Registre des notes de concept + Glossaire LBP).

Output: scripts/phase_a3/output/drive_concepts.json
"""
from __future__ import annotations

import json
import re
from pathlib import Path

DRIVE_ROOT = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Notes de Concept")
OUT = Path(__file__).parent / "output" / "drive_concepts.json"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    fm: dict = {}
    current_key = None
    list_buf: list = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        # list item under current key
        if line.startswith(("  - ", "- ")) and current_key is not None:
            val = line.lstrip(" -").strip().strip('"').strip("'")
            list_buf.append(val)
            fm[current_key] = list_buf
            continue
        # key: value
        m2 = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
        if m2:
            key = m2.group(1)
            val = m2.group(2).strip()
            current_key = key
            list_buf = []
            if val == "" or val == "[]":
                fm[key] = []
                list_buf = []
            else:
                # strip quotes
                v = val.strip('"').strip("'")
                fm[key] = v
                current_key = None
    return fm


def main() -> None:
    entries: list[dict] = []
    for p in sorted(DRIVE_ROOT.glob("*.md")):
        try:
            text = p.read_text(encoding="utf-8")
        except Exception as e:
            entries.append({"file": p.name, "error": str(e)})
            continue
        fm = parse_frontmatter(text)
        entries.append({
            "file": p.name,
            "code": fm.get("code"),
            "title": fm.get("title"),
            "summary": fm.get("summary"),
            "purpose": fm.get("purpose"),
            "version": fm.get("version"),
            "status": fm.get("status"),
            "domains": fm.get("domains") or fm.get("domain"),
            "frontmatter_keys": sorted(fm.keys()),
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} concept entries to {OUT}")
    # quick stats
    with_code = sum(1 for e in entries if e.get("code"))
    print(f"  with code: {with_code}")
    print(f"  without code: {len(entries) - with_code}")


if __name__ == "__main__":
    main()
