"""
Phase A3.2 (d3) — produit le plan d'updates en série.

Pour chaque concept Drive, calcule les valeurs cibles Glossaire + Registre,
les associe aux URLs Notion via registre_index.json, et émet une liste
de tool calls (page_id, properties) à exécuter.

Output : scripts/phase_a3/output/update_plan.json
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent / "output"
DRIVE = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Notes de Concept")

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
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
            else:
                fm[k] = v.strip('"').strip("'")
                cur = None
    return fm


def norm(s: str) -> str:
    if not s:
        return ""
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return s


def canonical_from_drive_title(title: str) -> str:
    t = re.sub(r"^Concept\s*-\s*", "", title.strip(), flags=re.IGNORECASE)
    return norm(t)


def main() -> None:
    registre = json.loads((ROOT / "registre_index.json").read_text(encoding="utf-8"))["entries"]
    by_canon = {norm(e["name"]): e for e in registre}

    updates: list = []
    unmatched: list = []
    skipped_calibration: list = []

    for p in sorted(DRIVE.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)

        drive_canon = canonical_from_drive_title(p.stem)
        idx = by_canon.get(drive_canon)
        if not idx:
            unmatched.append({"file": p.name, "canonical": drive_canon, "code": fm.get("code")})
            continue

        if idx.get("_done_calibration"):
            skipped_calibration.append(p.name)
            continue

        # Compute target values
        code = fm.get("code", "")
        canonical_name = fm.get("canonical_name", "")
        aliases = fm.get("aliases", []) or []
        keywords = fm.get("keywords", []) or []
        tags = fm.get("tags", []) or []
        template_version = fm.get("template_version", "")

        if not isinstance(aliases, list):
            aliases = []
        if not isinstance(keywords, list):
            keywords = []
        if not isinstance(tags, list):
            tags = []

        type_concept = "Concept LBP" if "lbp" in [t.lower() for t in tags] else "Concept externe"

        glossaire_props = {
            "Code unique": code,
            "Nom canonique": canonical_name,
            "Aliases": "; ".join(aliases),
            "Mots clés": "; ".join(keywords),
            "Type de concept": type_concept,
            "Version du template": template_version,
        }

        registre_props = {
            "Code unique": code,
            "Version du template": template_version,
        }

        item = {
            "file": p.name,
            "canonical": drive_canon,
            "drive_code": code,
            "registre_url": idx.get("registre_url"),
            "glossaire_url": idx.get("glossaire_url"),
            "current_code_notion": idx.get("code_notion"),
            "glossaire_props": glossaire_props,
            "registre_props": registre_props,
            "flags": [],
        }
        if idx.get("_archived"):
            item["flags"].append("archived")
        if idx.get("_collision_glossaire"):
            item["flags"].append("collision_glossaire")
        if idx.get("_no_glossaire_link"):
            item["flags"].append("no_glossaire_link_yet")

        updates.append(item)

    out = ROOT / "update_plan.json"
    out.write_text(json.dumps({
        "updates": updates,
        "unmatched": unmatched,
        "skipped_calibration": skipped_calibration,
        "stats": {
            "to_update": len(updates),
            "unmatched": len(unmatched),
            "calibration_done": len(skipped_calibration),
        }
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"To update: {len(updates)}")
    print(f"Unmatched: {len(unmatched)} -> sub-phase A3.2.e")
    print(f"Already done (calibration): {len(skipped_calibration)}")
    if updates:
        print("\nFlags distribution:")
        from collections import Counter
        flags = []
        for u in updates:
            flags.extend(u["flags"] or ["none"])
        print(" ", dict(Counter(flags)))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
