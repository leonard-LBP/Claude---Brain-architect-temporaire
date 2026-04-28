#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 5 : Migration des frontmatters WR-RD au canon Brain (R-054, R-055, R-056).

- Twin (28) : Manuels de BDD/Digital Twin/WR-RD/*.md
- Mission Ops (4) : Manuels de BDD/Mission Ops/WR-RD/*.md

Spec :
- 3 zones balisees (Identite / Meta-gouvernance / Spec d'usage)
- doc_type: WR_RD (token MAJUSCULES)
- code: WRRD_TW_<SLUG> ou WRRD_MO_<TOKEN> (NOUVEAU)
- target_bdd_code: DBMAN_TW_<SLUG> ou DBMAN_MO_<TOKEN> (MAJ)
- wr_rd_code historique : preserve tel quel
- version : tronquer X.Y.Z -> X.Y (R-056)
- template_code: TPL_WRRD_TW / TPL_WRRD_MO
- template_version: 2.0
- created_at en JJ-MM-YYYY (R-044) ; MO : convertit date_creation ISO -> created_at
- updated_at: 28-04-2026
- summary / purpose : "# TODO Phase 5 : a completer" si absents
- Apostrophes typographiques U+2019 strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD")
TWIN_DIR = ROOT / "Digital Twin" / "WR-RD"
MO_DIR = ROOT / "Mission Ops" / "WR-RD"

UPDATED_AT = "28-04-2026"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, content: str) -> None:
    p.write_text(content, encoding="utf-8", newline="\n")


def split_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, text
    fm = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body


def truncate_version(v) -> str:
    if v is None:
        return "0.1"
    s = str(v).strip()
    parts = s.split(".")
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}"
    return s


def iso_to_fr(s: str) -> str:
    """Convert YYYY-MM-DD -> DD-MM-YYYY (R-044). Idempotent on DD-MM-YYYY."""
    s = str(s).strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", s)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    return s


def parent_manual_code(parent_manual: str, parent_dir: Path) -> str | None:
    """Read the parent manual frontmatter to extract its `code` (DBMAN_*_*)."""
    if not parent_manual:
        return None
    p = parent_dir / parent_manual
    if not p.exists():
        return None
    fm, _ = split_frontmatter(read_text(p))
    if not fm:
        return None
    return fm.get("code")


def is_canon(fm_text: str) -> bool:
    """Detect already-canon frontmatter via the 3 zone markers."""
    return (
        "# === Identité ===" in fm_text
        and "# === Méta-gouvernance ===" in fm_text
        and "# === Spec d'usage ===" in fm_text
    )


def yaml_quote(s) -> str:
    if s is None:
        return '""'
    s = str(s)
    # use double quotes ; escape \" and \\
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_tags(tags) -> str:
    if not tags:
        return "tags: []"
    if isinstance(tags, str):
        tags = [tags]
    lines = ["tags:"]
    for t in tags:
        lines.append(f"  - {t}")
    return "\n".join(lines)


def build_canon_fm(domain: str, fm: dict, parent_dir: Path) -> tuple[str, dict]:
    """Build the canon frontmatter string. Returns (fm_text, info_dict)."""
    info = {}
    title = fm.get("title", "")
    target_canonical = fm.get("target_bdd_canonical_name", "")
    parent_manual = fm.get("parent_manual", "")
    wr_rd_code_hist = fm.get("wr_rd_code", "")
    tags = fm.get("tags", [])
    summary = fm.get("summary")
    purpose = fm.get("purpose")

    # version truncation
    version = truncate_version(fm.get("version"))

    # created_at : Twin = preserve ; MO = converti depuis date_creation ISO si besoin
    if domain == "Digital Twin":
        created_at = fm.get("created_at") or "26-04-2026"
        created_at = iso_to_fr(created_at)
        template_code = "TPL_WRRD_TW"
        domain_value = "Digital Twin"
    else:
        # Mission Ops : si created_at present -> preserve. Sinon utilise date_creation et convertit.
        if fm.get("created_at"):
            created_at = iso_to_fr(fm.get("created_at"))
        elif fm.get("date_creation"):
            created_at = iso_to_fr(fm.get("date_creation"))
        else:
            created_at = "27-04-2026"
        template_code = "TPL_WRRD_MO"
        domain_value = "Mission Ops"

    # codes
    parent_code = parent_manual_code(parent_manual, parent_dir)
    info["parent_manual"] = parent_manual
    info["parent_code_found"] = parent_code

    if domain == "Digital Twin":
        if parent_code and parent_code.startswith("DBMAN_TW_"):
            slug = parent_code[len("DBMAN_TW_"):]
        else:
            # fallback : derive from existing target_bdd_code
            old_tbc = str(fm.get("target_bdd_code", ""))
            slug = old_tbc.replace("DBMAN_", "", 1) if old_tbc else "UNKNOWN"
        new_code = f"WRRD_TW_{slug}"
        new_target_bdd_code = f"DBMAN_TW_{slug}"
    else:
        if parent_code and parent_code.startswith("DBMAN_MO_"):
            token = parent_code[len("DBMAN_MO_"):]
        else:
            old_tbc = str(fm.get("target_bdd_code", ""))
            token = old_tbc.replace("DBMAN_", "", 1) if old_tbc else "UNKNOWN"
        new_code = f"WRRD_MO_{token}"
        new_target_bdd_code = f"DBMAN_MO_{token}"

    info["new_code"] = new_code
    info["new_target_bdd_code"] = new_target_bdd_code
    info["wr_rd_code_hist"] = wr_rd_code_hist

    summary_val = summary if summary else "# TODO Phase 5 : à compléter"
    purpose_val = purpose if purpose else "# TODO Phase 5 : à compléter"
    info["summary_todo"] = summary is None
    info["purpose_todo"] = purpose is None

    lines = []
    lines.append("---")
    lines.append("# === Identité ===")
    lines.append(f"title: {yaml_quote(title)}")
    lines.append("doc_type: WR_RD")
    lines.append(f"code: {yaml_quote(new_code)}")
    lines.append("")
    lines.append("# === Méta-gouvernance ===")
    lines.append(f"version: {yaml_quote(version)}")
    lines.append(f"template_code: {yaml_quote(template_code)}")
    lines.append(f"template_version: {yaml_quote('2.0')}")
    lines.append(f"created_at: {yaml_quote(created_at)}")
    lines.append(f"updated_at: {yaml_quote(UPDATED_AT)}")
    lines.append("")
    lines.append("# === Spec d'usage ===")
    lines.append(f"target_bdd_canonical_name: {yaml_quote(target_canonical)}")
    lines.append(f"target_bdd_code: {yaml_quote(new_target_bdd_code)}")
    lines.append(f"parent_manual: {yaml_quote(parent_manual)}")
    lines.append(f"wr_rd_code: {yaml_quote(wr_rd_code_hist)}")
    lines.append(f"domain: {yaml_quote(domain_value)}")
    lines.append(f"summary: {yaml_quote(summary_val)}")
    lines.append(f"purpose: {yaml_quote(purpose_val)}")
    lines.append(emit_tags(tags))
    lines.append("---")
    lines.append("")
    return "\n".join(lines), info


def process_file(p: Path, domain: str, parent_dir: Path, apply: bool) -> dict:
    text = read_text(p)
    m = FM_RE.match(text)
    if not m:
        return {"file": p.name, "status": "no_frontmatter"}
    raw_fm_text = m.group(1)
    if is_canon(raw_fm_text):
        return {"file": p.name, "status": "skip_already_canon"}
    fm, body = split_frontmatter(text)
    new_fm, info = build_canon_fm(domain, fm, parent_dir)
    new_content = new_fm + body
    info["file"] = p.name
    info["status"] = "to_migrate"
    if apply:
        write_text(p, new_content)
        info["status"] = "migrated"
    return info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Apply changes (default = dry-run).")
    args = ap.parse_args()

    apply = args.apply
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"=== Phase 5 WR-RD canon migration [{mode}] ===\n")

    twin_files = sorted([p for p in TWIN_DIR.glob("*.md") if p.is_file()])
    mo_files = sorted([p for p in MO_DIR.glob("*.md") if p.is_file()])

    print(f"Twin    : {len(twin_files)} fichiers")
    print(f"MO      : {len(mo_files)} fichiers")
    print(f"Total   : {len(twin_files) + len(mo_files)} fichiers\n")

    results = []

    for p in twin_files:
        info = process_file(p, "Digital Twin", TWIN_DIR.parent, apply)
        results.append(("Twin", info))

    for p in mo_files:
        info = process_file(p, "Mission Ops", MO_DIR.parent, apply)
        results.append(("MO", info))

    # Reporting
    by_status = {}
    for cat, info in results:
        by_status.setdefault((cat, info["status"]), 0)
        by_status[(cat, info["status"])] += 1

    print("--- Bilan par catégorie / statut ---")
    for k, v in sorted(by_status.items()):
        print(f"  {k[0]:5s} {k[1]:25s} : {v}")

    print("\n--- Codes ajoutés (zone Identité) ---")
    for cat, info in results:
        if "new_code" in info and info["status"] in ("to_migrate", "migrated"):
            print(f"  [{cat}] {info['file']:55s} -> {info['new_code']:40s} | tbc={info['new_target_bdd_code']}")

    todos = [(cat, info) for cat, info in results if info.get("summary_todo") or info.get("purpose_todo")]
    print(f"\n--- TODO summary/purpose : {len(todos)} fichiers ---")

    missing_parent = [(cat, info) for cat, info in results if info.get("parent_code_found") is None and "new_code" in info]
    if missing_parent:
        print(f"\n!!! Anomalies parent_manual code introuvable : {len(missing_parent)}")
        for cat, info in missing_parent:
            print(f"  [{cat}] {info['file']} (parent_manual='{info.get('parent_manual')}')")


if __name__ == "__main__":
    sys.exit(main())
