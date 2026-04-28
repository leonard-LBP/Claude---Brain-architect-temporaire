#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 6 : Migration des frontmatters de Notes de Concept au canon Brain
(R-054, R-055, R-056).

Perimetre : Notes de Concept (non recursif, exclure 00 - archives/).

Spec :
- 3 zones balisees (Identite / Meta-gouvernance / Spec d'usage)
- doc_type: NOTE_CONCEPT (token MAJUSCULES R-055)
- code: CPT_<DOMAINE>_<TOKEN> (R-054 grammaire 1)
- concept_code: meme valeur que `code` (redondance R-055)
- version : extraire semver de "DATE vX.Y.Z" et tronquer X.Y (R-056)
- created_at: extraire DATE de la version mixte ; fallback 26-04-2026
- updated_at: 28-04-2026
- template_code: TPL_NOTE_CONCEPT
- template_version: 2.0
- purpose: TODO Phase 6 si absent
- preserve : canonical_name, summary, aliases, keywords, detection_clues,
  anti_confusions, tags
- Apostrophes typographiques U+2019 strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Notes de Concept")

UPDATED_AT = "28-04-2026"
CREATED_AT_FALLBACK = "26-04-2026"
DEFAULT_VERSION = "1.0"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# CPT.<DOMAINE>.LBP[.<TOKEN>] - majuscules / chiffres / underscores
CPT_LEGACY_RE = re.compile(r"^CPT\.([A-Z0-9_]+)\.LBP(?:\.([A-Z0-9_]+))?$")

# "<DD-MM-YYYY> v<X.Y[.Z]>" possibly with extra spaces
VERSION_MIXED_RE = re.compile(
    r"^\s*(\d{2}-\d{2}-\d{4})\s+v(\d+)\.(\d+)(?:\.(\d+))?\s*$"
)
VERSION_SEMVER_RE = re.compile(r"^\s*v?(\d+)\.(\d+)(?:\.(\d+))?\s*$")
DATE_FR_RE = re.compile(r"^\d{2}-\d{2}-\d{4}$")


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, content: str) -> None:
    p.write_text(content, encoding="utf-8", newline="\n")


def split_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, text, None
    fm = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body, m.group(1)


def is_canon(fm_text: str) -> bool:
    """Detect already-canon frontmatter via the 3 zone markers + code at canon."""
    has_zones = (
        "# === Identité ===" in fm_text
        and "# === Méta-gouvernance ===" in fm_text
        and "# === Spec d'usage ===" in fm_text
    )
    # Also require that `code:` is at the canon (CPT_...)
    has_code = re.search(r'^code:\s*"?CPT_', fm_text, re.MULTILINE) is not None
    return has_zones and has_code


def migrate_concept_code(old: str) -> tuple[str | None, str | None]:
    """Return (new_code, error). new_code is the CPT_X[_Y] migrated value."""
    if old is None:
        return None, "concept_code absent"
    s = str(old).strip()
    # Already at canon ?
    if s.startswith("CPT_") and "." not in s:
        return s, None
    m = CPT_LEGACY_RE.match(s)
    if not m:
        return None, f"format inattendu : {s!r}"
    domaine = m.group(1)
    token = m.group(2)
    if token:
        return f"CPT_{domaine}_{token}", None
    return f"CPT_{domaine}", None


def migrate_version(raw) -> tuple[str, str, dict]:
    """Returns (version_xy, created_at, info). info has flags applied."""
    info = {"version_fallback": False, "date_fallback": False, "raw_version": raw}
    if raw is None:
        return DEFAULT_VERSION, CREATED_AT_FALLBACK, {**info, "version_fallback": True, "date_fallback": True}
    s = str(raw).strip()
    m = VERSION_MIXED_RE.match(s)
    if m:
        date = m.group(1)
        major, minor = m.group(2), m.group(3)
        return f"{major}.{minor}", date, info
    # Just a semver maybe ?
    m = VERSION_SEMVER_RE.match(s)
    if m:
        major, minor = m.group(1), m.group(2)
        info["date_fallback"] = True
        return f"{major}.{minor}", CREATED_AT_FALLBACK, info
    # Just a date ?
    if DATE_FR_RE.match(s):
        info["version_fallback"] = True
        return DEFAULT_VERSION, s, info
    # Unknown format : double fallback
    info["version_fallback"] = True
    info["date_fallback"] = True
    return DEFAULT_VERSION, CREATED_AT_FALLBACK, info


def yaml_quote(s) -> str:
    if s is None:
        return '""'
    s = str(s)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_list(name: str, items) -> str:
    if items is None:
        return f"{name}: []"
    if isinstance(items, str):
        items = [items]
    if not items:
        return f"{name}: []"
    lines = [f"{name}:"]
    for it in items:
        lines.append(f"  - {yaml_quote(it)}")
    return "\n".join(lines)


def emit_tags(tags) -> str:
    if not tags:
        return "tags: []"
    if isinstance(tags, str):
        tags = [tags]
    lines = ["tags:"]
    for t in tags:
        lines.append(f"  - {t}")
    return "\n".join(lines)


def build_canon_fm(fm: dict) -> tuple[str | None, dict]:
    """Build the canon frontmatter string. Returns (fm_text or None, info)."""
    info: dict = {}
    title = fm.get("title", "")
    canonical_name = fm.get("canonical_name", "")
    summary = fm.get("summary", "")
    aliases = fm.get("aliases", [])
    keywords = fm.get("keywords", [])
    detection_clues = fm.get("detection_clues", [])
    anti_confusions = fm.get("anti_confusions", [])
    tags = fm.get("tags", [])
    purpose = fm.get("purpose")

    # --- concept_code migration ---
    new_code, err = migrate_concept_code(fm.get("concept_code"))
    info["old_concept_code"] = fm.get("concept_code")
    info["new_code"] = new_code
    info["concept_code_error"] = err
    if err:
        return None, info

    # --- version + created_at ---
    version_xy, created_at, vinfo = migrate_version(fm.get("version"))
    info["raw_version"] = vinfo.get("raw_version")
    info["new_version"] = version_xy
    info["new_created_at"] = created_at
    info["version_fallback"] = vinfo["version_fallback"]
    info["date_fallback"] = vinfo["date_fallback"]

    # --- purpose ---
    purpose_todo = False
    if purpose is None or str(purpose).strip() == "":
        purpose_val = ""
        purpose_todo = True
    else:
        purpose_val = str(purpose)
    info["purpose_todo"] = purpose_todo

    lines: list[str] = []
    lines.append("---")
    lines.append("# === Identité ===")
    lines.append(f"title: {yaml_quote(title)}")
    lines.append("doc_type: NOTE_CONCEPT")
    lines.append(f"code: {yaml_quote(new_code)}")
    lines.append("")
    lines.append("# === Méta-gouvernance ===")
    lines.append(f"version: {yaml_quote(version_xy)}")
    lines.append(f"template_code: {yaml_quote('TPL_NOTE_CONCEPT')}")
    lines.append(f"template_version: {yaml_quote('2.0')}")
    lines.append(f"created_at: {yaml_quote(created_at)}")
    lines.append(f"updated_at: {yaml_quote(UPDATED_AT)}")
    lines.append("")
    lines.append("# === Spec d'usage ===")
    lines.append(f"canonical_name: {yaml_quote(canonical_name)}")
    lines.append(f"concept_code: {yaml_quote(new_code)}")
    lines.append(f"summary: {yaml_quote(summary)}")
    if purpose_todo:
        lines.append('purpose: ""  # TODO Phase 6 : à compléter (1-3 phrases sur l’usage agent du concept)')
    else:
        lines.append(f"purpose: {yaml_quote(purpose_val)}")
    lines.append(emit_list("aliases", aliases))
    lines.append(emit_list("keywords", keywords))
    lines.append(emit_list("detection_clues", detection_clues))
    lines.append(emit_list("anti_confusions", anti_confusions))
    lines.append(emit_tags(tags))
    lines.append("---")
    lines.append("")
    return "\n".join(lines), info


def process_file(p: Path, apply: bool) -> dict:
    text = read_text(p)
    m = FM_RE.match(text)
    if not m:
        return {"file": p.name, "status": "no_frontmatter"}
    raw_fm_text = m.group(1)
    if is_canon(raw_fm_text):
        return {"file": p.name, "status": "skip_already_canon"}
    fm, body, _ = split_frontmatter(text)
    new_fm, info = build_canon_fm(fm)
    info["file"] = p.name
    if new_fm is None:
        info["status"] = "error_concept_code"
        return info
    new_content = new_fm + body
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
    print(f"=== Phase 6 Notes de Concept canon migration [{mode}] ===\n")

    files = sorted([p for p in ROOT.glob("*.md") if p.is_file()])
    print(f"Fichiers detectes : {len(files)}\n")

    results = [process_file(p, apply) for p in files]

    by_status: dict[str, int] = {}
    for info in results:
        by_status[info["status"]] = by_status.get(info["status"], 0) + 1

    print("--- Bilan par statut ---")
    for k, v in sorted(by_status.items()):
        print(f"  {k:25s} : {v}")

    # Errors
    errs = [info for info in results if info["status"] == "error_concept_code"]
    if errs:
        print(f"\n!!! Cas particuliers concept_code (a arbitrer) : {len(errs)}")
        for info in errs:
            print(f"  - {info['file']:60s} concept_code={info.get('old_concept_code')!r} -> {info.get('concept_code_error')}")

    # Sample CPT migrations
    migrated = [info for info in results if info.get("new_code") and info["status"] in ("to_migrate", "migrated")]
    print(f"\n--- Echantillon migrations concept_code (10 max) ---")
    for info in migrated[:10]:
        print(f"  {info['file']:55s} {info['old_concept_code']!s:40s} -> {info['new_code']}")

    # Sample version migrations
    print(f"\n--- Echantillon migrations version (10 max) ---")
    for info in migrated[:10]:
        flags = []
        if info.get("version_fallback"):
            flags.append("VER_FALLBACK")
        if info.get("date_fallback"):
            flags.append("DATE_FALLBACK")
        flag_str = " [" + ",".join(flags) + "]" if flags else ""
        print(f"  {info['file']:55s} {str(info.get('raw_version'))!s:30s} -> v={info['new_version']:6s} created_at={info['new_created_at']}{flag_str}")

    # Fallbacks list
    vfb = [info for info in results if info.get("version_fallback") and info["status"] in ("to_migrate", "migrated")]
    dfb = [info for info in results if info.get("date_fallback") and info["status"] in ("to_migrate", "migrated")]
    if vfb:
        print(f"\n--- Fallback version=1.0 applique : {len(vfb)} ---")
        for info in vfb:
            print(f"  - {info['file']} (version brute = {info.get('raw_version')!r})")
    if dfb:
        print(f"\n--- Fallback created_at=26-04-2026 applique : {len(dfb)} ---")
        for info in dfb:
            print(f"  - {info['file']} (version brute = {info.get('raw_version')!r})")

    # Purpose TODOs
    todos = [info for info in results if info.get("purpose_todo") and info["status"] in ("to_migrate", "migrated")]
    print(f"\n--- TODO purpose : {len(todos)} fichiers ---")
    if todos and apply:
        for info in todos:
            print(f"  - {info['file']}")


if __name__ == "__main__":
    sys.exit(main())
