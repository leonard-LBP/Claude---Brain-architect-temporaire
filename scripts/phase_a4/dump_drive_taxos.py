"""
Phase A4.A.0 — Dump frontmatters of all Taxonomy Markdown files.

Reads every .md file in `Taxonomies/` (excluding `00 - archives/`),
extracts YAML frontmatter, and writes a JSON dump for cross-matching
against Notion `Registre des taxonomies`.

Output: scripts/phase_a4/output/drive_taxos.json
"""
from __future__ import annotations
import json
import re
from pathlib import Path

DRIVE_ROOT = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Taxonomies")
OUT = Path(__file__).parent / "output" / "drive_taxos.json"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_inline_array(v: str) -> list:
    """Parse an inline YAML array like ["a", "b", 'c'] into a list of strings."""
    inner = v.strip()[1:-1].strip()
    if not inner:
        return []
    items = []
    cur = ""
    in_q = None
    for ch in inner:
        if in_q:
            if ch == in_q:
                in_q = None
            else:
                cur += ch
        else:
            if ch in ('"', "'"):
                in_q = ch
            elif ch == ",":
                items.append(cur.strip())
                cur = ""
            else:
                cur += ch
    if cur.strip():
        items.append(cur.strip())
    return [s.strip().strip('"').strip("'") for s in items]


def parse_fm(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    fm: dict = {}
    cur = None
    buf: list = []
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith(("  - ", "- ")) and cur is not None:
            v = line.lstrip(" -").strip().strip('"').strip("'")
            buf.append(v)
            fm[cur] = buf
            continue
        m2 = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
        if m2:
            k = m2.group(1)
            v = m2.group(2).strip()
            cur = k
            buf = []
            if v == "" or v == "[]":
                fm[k] = []
                buf = []
            elif v.startswith("[") and v.endswith("]"):
                fm[k] = _parse_inline_array(v)
                cur = None
            else:
                fm[k] = v.strip('"').strip("'")
                cur = None
    return fm


def main() -> None:
    entries: list[dict] = []
    for p in sorted(DRIVE_ROOT.glob("*.md")):
        try:
            text = p.read_text(encoding="utf-8")
        except Exception as e:
            entries.append({"file": p.name, "error": str(e)})
            continue
        fm = parse_fm(text)
        entries.append({
            "file": p.name,
            "code": fm.get("code"),
            "title": fm.get("title"),
            "canonical_name": fm.get("canonical_name"),
            "namespace_code": fm.get("namespace_code"),
            "summary": fm.get("summary"),
            "purpose": fm.get("purpose"),
            "version": fm.get("version"),
            "template_version": fm.get("template_version"),
            "is_open": fm.get("is_open"),
            "open_policy": fm.get("open_policy"),
            "scale_kind": fm.get("scale_kind"),
            "is_ordinal": fm.get("is_ordinal"),
            "selection_mode": fm.get("selection_mode"),
            "cardinality": fm.get("cardinality"),
            "aliases": fm.get("aliases"),
            "keywords": fm.get("keywords"),
            "frontmatter_keys": sorted(fm.keys()),
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} taxo entries to {OUT}")
    with_code = sum(1 for e in entries if e.get("code"))
    print(f"  with code: {with_code}")
    print(f"  without code: {len(entries) - with_code}")
    # codes by namespace
    from collections import Counter
    namespaces = Counter()
    for e in entries:
        c = e.get("code")
        if c and "." in c:
            namespaces[c.split(".")[0]] += 1
    print(f"  namespaces: {dict(namespaces)}")


if __name__ == "__main__":
    main()
