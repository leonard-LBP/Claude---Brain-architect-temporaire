#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 2 - Migration des taxonomies au canon Brain (R-054, R-055, R-056).

Pour chaque fichier `XXX.YYY.LBP.md` dans Taxonomies/ (non recursif, hors archives) :
  1. Renomme le filename : XXX.YYY.LBP.md -> XXX.YYY.md
  2. Reformate le frontmatter en 3 zones balisees (Identite / Meta-gouvernance / Spec d'usage).
  3. Strip ".LBP" des codes internes dans le corps.

Modes :
  --dry-run (defaut)
  --apply

Usage :
  python migrate_taxos.py --dry-run
  python migrate_taxos.py --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

VAULT_TAXOS = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Taxonomies")

# 3 taxos socles deja au canon : a skipper
ALREADY_CANON = {"DOC.TYPE.md", "DBMAN.SCOPE.md", "LGBLK.FAMILY.md"}

# Date forfaitaire si created_at absent
DEFAULT_CREATED_AT = "26-04-2026"
# Date du jour pour updated_at
TODAY = "28-04-2026"

# Regex filename des cibles
LBP_FILENAME_RE = re.compile(r"^([A-Z0-9_]+)\.([A-Z0-9_]+)\.LBP\.md$")
# Regex pour stripper ".LBP" dans le corps (sur les codes type AAA.BBB.LBP[.XXX]).
# Capture aussi un eventuel `\` echappe devant le `.` (cas des regex documentees
# `\.LBP$` qui doivent devenir `$`, sans backslash orphelin).
LBP_CODE_RE = re.compile(r"\\?\.LBP\b")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str):
    """Retourne (meta_dict, body_str). meta_dict={} si pas de frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    # Strip lignes de commentaire pures (commencent par #) pour pyyaml
    # et supprimer les commentaires inline `  # ...`
    cleaned_lines = []
    for line in raw.splitlines():
        # Ligne entierement commentaire ou vide
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            cleaned_lines.append("")
            continue
        # Commentaire inline : couper a `  #` (mais pas dans une chaine quotee)
        # Heuristique simple : split sur '  #' ou ' #' uniquement si pas dans une string
        # Pour rester safe, on enleve les commentaires inline simplement quand le `#`
        # est precede d'au moins 1 espace et n'est pas dans une string quotee
        new_line = strip_inline_comment(line)
        cleaned_lines.append(new_line)
    cleaned = "\n".join(cleaned_lines)
    try:
        meta = yaml.safe_load(cleaned) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parse error: {exc}")
    body = text[m.end():]
    return meta, body


def strip_inline_comment(line: str) -> str:
    """Enleve un commentaire inline ' #...' s'il n'est pas dans une string quotee."""
    in_single = False
    in_double = False
    for i, ch in enumerate(line):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            # Verifier qu'il y a au moins un espace avant
            if i > 0 and line[i-1] in " \t":
                return line[:i].rstrip()
    return line


def derive_human_name(meta, ns_taxo_code):
    """Derive un title humain : prend canonical_name s'il existe, sinon ns_taxo_code."""
    cn = meta.get("canonical_name")
    if cn and isinstance(cn, str) and cn.strip():
        return f"Taxonomie - {cn.strip()}"
    return f"Taxonomie - {ns_taxo_code}"


def truncate_version(v):
    """Tronque X.Y.Z en X.Y. Si vide/absent => '1.0'."""
    if v is None or str(v).strip() == "":
        return "1.0"
    s = str(v).strip()
    parts = s.split(".")
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}"
    return s


def yaml_quote(val) -> str:
    """Serialise une valeur scalaire en YAML avec guillemets doubles si string."""
    if val is None:
        return ""
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, str):
        # Apostrophes typo U+2019 preservees, on quote en double
        # Echapper les " internes
        escaped = val.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return str(val)


def yaml_list(val) -> str:
    """Serialise une liste en YAML flow style ['a', 'b']."""
    if val is None:
        return "[]"
    if not isinstance(val, list):
        return "[]"
    parts = []
    for item in val:
        if isinstance(item, str):
            escaped = item.replace("\\", "\\\\").replace('"', '\\"')
            parts.append(f'"{escaped}"')
        else:
            parts.append(str(item))
    return "[" + ", ".join(parts) + "]"


def build_canonical_frontmatter(meta, ns_taxo_code, namespace_root):
    """Construit le frontmatter au canon en 3 zones."""
    title = derive_human_name(meta, ns_taxo_code)
    code_val = ns_taxo_code  # sans .LBP

    version = truncate_version(meta.get("version"))
    created_at = meta.get("created_at") or DEFAULT_CREATED_AT
    updated_at = TODAY  # toujours date du jour

    # Spec d'usage
    summary = meta.get("summary", "")
    purpose = meta.get("purpose", "")  # peut etre absent
    is_open = meta.get("is_open")
    open_policy = meta.get("open_policy", "")
    scale_kind = meta.get("scale_kind", "")
    is_ordinal = meta.get("is_ordinal")
    selection_mode = meta.get("selection_mode", "")
    cardinality = meta.get("cardinality", "")
    aliases = meta.get("aliases", [])
    keywords = meta.get("keywords", [])
    detection_clues = meta.get("detection_clues", [])
    tags = meta.get("tags", [])

    lines = []
    lines.append("---")
    lines.append("# === Identité ===")
    lines.append(f"title: {yaml_quote(title)}")
    lines.append(f"doc_type: TAXONOMIE")
    lines.append(f"code: {yaml_quote(code_val)}")
    lines.append("")
    lines.append("# === Méta-gouvernance ===")
    lines.append(f'version: "{version}"')
    lines.append(f'template_code: "TPL_TAXO"')
    lines.append(f'template_version: "2.0"')
    lines.append(f'created_at: "{created_at}"')
    lines.append(f'updated_at: "{updated_at}"')
    lines.append("")
    lines.append("# === Spec d'usage ===")
    lines.append(f"canonical_name: {yaml_quote(code_val)}")
    lines.append(f"namespace_code: {yaml_quote(namespace_root)}")
    # summary : utiliser block scalar > pour preserver multi-lignes ?
    if isinstance(summary, str) and "\n" in summary:
        # Rendre en block folded
        lines.append("summary: >")
        for sl in summary.strip().splitlines():
            lines.append(f"  {sl.strip()}")
    else:
        lines.append(f"summary: {yaml_quote(summary)}")
    if purpose:
        lines.append(f"purpose: {yaml_quote(purpose)}")
    else:
        lines.append(f'purpose: ""  # TODO Phase 2 : a renseigner (1-3 phrases sur usage agent)')
    if is_open is not None:
        lines.append(f"is_open: {yaml_quote(is_open) if isinstance(is_open, bool) else str(is_open).lower()}")
    if open_policy:
        lines.append(f"open_policy: {yaml_quote(open_policy)}")
    if scale_kind:
        lines.append(f"scale_kind: {yaml_quote(scale_kind)}")
    if is_ordinal is not None:
        lines.append(f"is_ordinal: {yaml_quote(is_ordinal) if isinstance(is_ordinal, bool) else str(is_ordinal).lower()}")
    if selection_mode:
        lines.append(f"selection_mode: {yaml_quote(selection_mode)}")
    if cardinality:
        lines.append(f"cardinality: {yaml_quote(cardinality)}")
    lines.append(f"aliases: {yaml_list(aliases)}")
    lines.append(f"keywords: {yaml_list(keywords)}")
    if detection_clues:
        lines.append("detection_clues:")
        for dc in detection_clues:
            if isinstance(dc, str):
                escaped = dc.replace("\\", "\\\\").replace('"', '\\"')
                lines.append(f'  - "{escaped}"')
    else:
        lines.append("detection_clues: []")
    lines.append(f"tags: {yaml_list(tags)}")
    lines.append("---")
    lines.append("")  # ligne vide apres frontmatter
    return "\n".join(lines)


def is_already_canon(meta) -> bool:
    """Detecte si le frontmatter est deja au canon (presence de title + code + template_code)."""
    return all(k in meta for k in ("title", "doc_type", "code", "template_code"))


def process_file(path: Path, apply: bool, log: list):
    fname = path.name
    entry = {"file": fname, "status": "pending"}

    if fname in ALREADY_CANON:
        entry["status"] = "skip_already_canon_socle"
        log.append(entry)
        return

    m = LBP_FILENAME_RE.match(fname)
    if not m:
        entry["status"] = "skip_filename_not_lbp_pattern"
        log.append(entry)
        return

    namespace_root = m.group(1)  # ex. OBJ
    taxo_part = m.group(2)        # ex. STATUT
    ns_taxo_code = f"{namespace_root}.{taxo_part}"  # ex. OBJ.STATUT
    new_filename = f"{ns_taxo_code}.md"
    new_path = path.with_name(new_filename)

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        entry["status"] = "error_read"
        entry["error"] = str(exc)
        log.append(entry)
        return

    try:
        meta, body = parse_frontmatter(text)
    except ValueError as exc:
        entry["status"] = "error_yaml_parse"
        entry["error"] = str(exc)
        log.append(entry)
        return

    if is_already_canon(meta):
        entry["status"] = "skip_already_canon"
        log.append(entry)
        return

    # Detection structures atypiques : flagger si pas canonical_name OU pas namespace_code
    if "canonical_name" not in meta and "namespace_code" not in meta:
        entry["status"] = "flag_atypical_no_canonical_no_namespace"
        log.append(entry)
        return

    # Construit nouveau frontmatter
    new_fm = build_canonical_frontmatter(meta, ns_taxo_code, namespace_root)

    # Update body : strip ".LBP" sur les codes
    new_body = LBP_CODE_RE.sub("", body)

    new_text = new_fm + new_body

    entry["new_filename"] = new_filename
    entry["namespace_code_new"] = namespace_root
    entry["code_new"] = ns_taxo_code
    entry["purpose_added"] = "purpose" not in meta or not meta.get("purpose")
    entry["body_lbp_strips"] = len(LBP_CODE_RE.findall(body))
    entry["status"] = "would_migrate" if not apply else "migrated"

    if apply:
        try:
            new_path.write_text(new_text, encoding="utf-8", newline="\n")
            if new_path != path:
                path.unlink()
        except Exception as exc:
            entry["status"] = "error_write"
            entry["error"] = str(exc)

    log.append(entry)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--out", type=str, default=None, help="Path to JSON log output")
    args = parser.parse_args()

    apply = args.apply
    mode_label = "APPLY" if apply else "DRY-RUN"
    print(f"[migrate_taxos] mode = {mode_label}")
    print(f"[migrate_taxos] target dir = {VAULT_TAXOS}")

    if not VAULT_TAXOS.exists():
        print(f"ERROR: target dir not found", file=sys.stderr)
        sys.exit(2)

    files = sorted(p for p in VAULT_TAXOS.iterdir() if p.is_file() and p.suffix == ".md")
    print(f"[migrate_taxos] {len(files)} .md files detected (pre-filter)")

    log = []
    for p in files:
        process_file(p, apply, log)

    # Resume
    counts = {}
    for e in log:
        counts[e["status"]] = counts.get(e["status"], 0) + 1

    print("\n=== RESUME ===")
    for status, n in sorted(counts.items()):
        print(f"  {status}: {n}")
    print(f"  TOTAL: {len(log)}")

    out_path = args.out or str(Path(__file__).parent / f"log_{mode_label.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"mode": mode_label, "counts": counts, "entries": log}, f, ensure_ascii=False, indent=2)
    print(f"\n[migrate_taxos] log written to: {out_path}")


if __name__ == "__main__":
    main()
