"""
Phase 4 - Migration des frontmatters de manuels de BDD au canon Brain (R-054, R-055, R-056).

3 categories : Twin (28), Mission Ops (4), Brain (11).
Transforme un frontmatter a plat en 3 zones balisees : Identite, Meta-gouvernance, Spec d'usage.

Usage :
    python migrate_manuels.py --dry-run    (par defaut)
    python migrate_manuels.py --apply
"""

from __future__ import annotations

import argparse
import io
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT_MANUELS = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Manuels de BDD")

DIR_TWIN = ROOT_MANUELS / "Digital Twin"
DIR_MO = ROOT_MANUELS / "Mission Ops"
DIR_BRAIN = ROOT_MANUELS / "Brain"

DATE_TODAY = "28-04-2026"
DATE_FORFAIT = "26-04-2026"

# -----------------------------------------------------------------------------
# Mappings Brain
# -----------------------------------------------------------------------------

BRAIN_MAPPING = {
    "Manuel de BDD - Manuels de BDD.md": {
        "brain_layer": "CORE_AND_MOTOR",
        "brain_subtype": "CATALOGUE",
        "code": "DBMAN_BR_MANUELS_DE_BDD",
        "bdd_canonical_name": "Manuels de BDD",
        "object_type": "Manuel de BDD",
    },
    "Manuel de BDD - Registre des taxonomies.md": {
        "brain_layer": "CORE_AND_MOTOR",
        "brain_subtype": "REGISTRE_PIVOT",
        "code": "DBMAN_BR_TAXONOMIES",
        "bdd_canonical_name": "Registre des taxonomies",
        "object_type": "Taxonomie",
    },
    "Manuel de BDD - Prompts LBP.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "HUB",
        "code": "DBMAN_BR_PROMPTS_LBP",
        "bdd_canonical_name": "Prompts LBP",
        "object_type": "Prompt LBP",
    },
    "Manuel de BDD - Templates de bricks.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "SPOKE_MOTOR",
        "code": "DBMAN_BR_TEMPLATES_DE_BRICKS",
        "bdd_canonical_name": "Templates de bricks",
        "object_type": "Template de brick",
    },
    "Manuel de BDD - Méthodes LBP.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "SPOKE_MOTOR",
        "code": "DBMAN_BR_METHODES_LBP",
        "bdd_canonical_name": "Méthodes LBP",
        "object_type": "Méthode LBP",
    },
    "Manuel de BDD - Outils externes.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "SPOKE_MOTOR",
        "code": "DBMAN_BR_OUTILS_EXTERNES",
        "bdd_canonical_name": "Outils externes",
        "object_type": "Outil externe",
    },
    "Manuel de BDD - Docs méta LBP.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "SPOKE_MOTOR",
        "code": "DBMAN_BR_DOCS_META_LBP",
        "bdd_canonical_name": "Docs méta LBP",
        "object_type": "Doc méta LBP",
    },
    "Manuel de BDD - Agents LBP.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "SPOKE_MOTOR",
        "code": "DBMAN_BR_AGENTS_LBP",
        "bdd_canonical_name": "Agents LBP",
        "object_type": "Agent LBP",
    },
    "Manuel de BDD - Registre des logic blocks.md": {
        "brain_layer": "MOTOR",
        "brain_subtype": "REGISTRE_PIVOT",
        "code": "DBMAN_BR_LOGIC_BLOCKS",
        "bdd_canonical_name": "Registre des logic blocks",
        "object_type": "Logic block",
    },
    "Manuel de BDD - Registre des notes de concept.md": {
        "brain_layer": "CORE",
        "brain_subtype": "REGISTRE_PIVOT",
        "code": "DBMAN_BR_NOTES_CONCEPT",
        "bdd_canonical_name": "Registre des notes de concept",
        "object_type": "Note de concept",
    },
    "Manuel de BDD - Glossaire LBP.md": {
        "brain_layer": "CORE_AND_MOTOR",
        "brain_subtype": "GLOSSAIRE",
        "code": "DBMAN_BR_GLOSSAIRE_LBP",
        "bdd_canonical_name": "Glossaire LBP",
        "object_type": "Entrée de glossaire",
    },
}

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def split_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, text
    fm = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body


def slugify_upper(name: str) -> str:
    """Accent-strip + uppercase + non-alnum -> underscore."""
    nfkd = unicodedata.normalize("NFKD", name)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    upper = no_accents.upper()
    slug = re.sub(r"[^A-Z0-9]+", "_", upper).strip("_")
    return slug


def truncate_version(v) -> str:
    """X.Y.Z -> X.Y. Idempotent."""
    if v is None:
        return v
    s = str(v).strip()
    parts = s.split(".")
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}"
    return s


def iso_to_jjmmyyyy(d: str) -> str:
    """2026-04-27 -> 27-04-2026. Idempotent if already JJ-MM-YYYY."""
    s = str(d).strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", s)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    if re.match(r"^\d{2}-\d{2}-\d{4}$", s):
        return s
    return s


def is_already_canon(text: str) -> bool:
    """Detecte les 3 zones balisees du canon R-055."""
    head = text[:2000]
    return (
        "# === Identité ===" in head
        and "# === Méta-gouvernance ===" in head
        and "# === Spec d'usage ===" in head
    )


# -----------------------------------------------------------------------------
# YAML dumping with section separators
# -----------------------------------------------------------------------------

class _QuotedStr(str):
    pass


def _quoted_repr(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')


yaml.add_representer(_QuotedStr, _quoted_repr, Dumper=yaml.SafeDumper)


def dump_section(d: dict) -> str:
    """Dump un dict en YAML inline (sans markers ---), UTF-8, sans tri des cles."""
    return yaml.safe_dump(
        d,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=10000,
    )


def build_canonical_frontmatter(identity: dict, meta: dict, spec: dict, summary_todo: bool = False) -> str:
    """3 zones balisees, separees par les commentaires R-055."""
    spec_yaml = dump_section(spec).rstrip()
    if summary_todo:
        # Ajoute le marqueur TODO en commentaire en bout de ligne summary: ''
        spec_yaml = re.sub(
            r"^(summary: '')$",
            r"\1  # TODO Phase 4 : à compléter (1-3 phrases sur ce qu'est la BDD)",
            spec_yaml,
            count=1,
            flags=re.MULTILINE,
        )
    parts = ["---", "# === Identité ==="]
    parts.append(dump_section(identity).rstrip())
    parts.append("")
    parts.append("# === Méta-gouvernance ===")
    parts.append(dump_section(meta).rstrip())
    parts.append("")
    parts.append("# === Spec d'usage ===")
    parts.append(spec_yaml)
    parts.append("---")
    parts.append("")
    return "\n".join(parts)


# -----------------------------------------------------------------------------
# Migration par categorie
# -----------------------------------------------------------------------------

def migrate_twin(fm: dict, file_name: str) -> tuple[dict, dict, dict, list[str]]:
    """Twin : ajoute code DBMAN_TW_, harmonise template, derive summary TODO."""
    notes = []
    bdd_name = fm.get("bdd_canonical_name") or file_name.replace("Manuel de BDD - ", "").replace(".md", "")
    slug = slugify_upper(bdd_name)
    code = f"DBMAN_TW_{slug}"

    title = fm.get("title") or f"Manuel de BDD - {bdd_name}"

    identity = {
        "title": title,
        "doc_type": "MANUEL_BDD",
        "code": code,
    }

    version = truncate_version(fm.get("version", "0.1"))
    meta = {
        "version": version,
        "template_code": "TPL_DBMAN_TW",
        "template_version": "7.0",
        "created_at": fm.get("created_at") or DATE_FORFAIT,
        "updated_at": DATE_TODAY,
    }

    summary = fm.get("summary")
    summary_todo = False
    if not summary:
        summary = ""
        summary_todo = True
        notes.append(f"summary TODO: {file_name}")

    spec = {
        "bdd_canonical_name": fm.get("bdd_canonical_name", bdd_name),
        "object_type": fm.get("object_type", ""),
        "architecture_family": fm.get("architecture_family", ""),
        "ui_family": fm.get("ui_family", ""),
        "knowledge_regime": fm.get("knowledge_regime", ""),
        "officiality_regime": fm.get("officiality_regime", ""),
        "has_advanced_note": fm.get("has_advanced_note", False),
        "summary": summary,
        "purpose": fm.get("purpose", ""),
        "tags": fm.get("tags", []),
    }

    return identity, meta, spec, notes if not summary_todo else notes + [f"__summary_todo__:{file_name}"]


def migrate_mo(fm: dict, file_name: str) -> tuple[dict, dict, dict, list[str]]:
    notes = []
    bdd_name = fm.get("bdd_canonical_name") or file_name.replace("Manuel de BDD - ", "").replace(".md", "")
    title = fm.get("title") or f"Manuel de BDD - {bdd_name}"

    # code : preserver, prefixer avec MO_ si absent
    raw_code = fm.get("code", "")
    if raw_code.startswith("DBMAN_MO_"):
        code = raw_code
    elif raw_code.startswith("DBMAN_"):
        suffix = raw_code[len("DBMAN_"):]
        code = f"DBMAN_MO_{suffix}"
    else:
        code = f"DBMAN_MO_{slugify_upper(bdd_name)}"
        notes.append(f"MO code derived from name: {file_name} -> {code}")

    identity = {
        "title": title,
        "doc_type": "MANUEL_BDD",
        "code": code,
    }

    # created_at : migrer date_creation ISO -> created_at JJ-MM-YYYY
    created_raw = fm.get("created_at") or fm.get("date_creation") or DATE_FORFAIT
    created = iso_to_jjmmyyyy(created_raw)

    version = truncate_version(fm.get("version", "1.0"))
    meta = {
        "version": version,
        "template_code": "TPL_DBMAN_MO",
        "template_version": "6.0",
        "created_at": created,
        "updated_at": DATE_TODAY,
    }

    summary = fm.get("summary")
    summary_todo = False
    if not summary:
        summary = ""
        summary_todo = True

    spec = {
        "bdd_canonical_name": fm.get("bdd_canonical_name", bdd_name),
        "object_type": fm.get("object_type", ""),
        "architecture_scope": "mission_ops",
        "mission_ops_family": fm.get("mission_ops_family", ""),
        "knowledge_regime": fm.get("knowledge_regime", ""),
        "execution_tracking": fm.get("execution_tracking", False),
        "summary": summary,
        "purpose": fm.get("purpose", ""),
        "tags": fm.get("tags", []),
    }

    if summary_todo:
        notes.append(f"__summary_todo__:{file_name}")

    return identity, meta, spec, notes


def migrate_brain(fm: dict, file_name: str) -> tuple[dict, dict, dict, list[str]]:
    notes = []
    mapping = BRAIN_MAPPING.get(file_name)
    if not mapping:
        notes.append(f"!! Brain mapping missing for {file_name}")
        return None, None, None, notes

    bdd_name = mapping["bdd_canonical_name"]
    title = fm.get("title") or f"Manuel de BDD - {bdd_name}"

    identity = {
        "title": title,
        "doc_type": "MANUEL_BDD",
        "code": mapping["code"],
    }

    version = truncate_version(fm.get("version", "0.1"))
    meta = {
        "version": version,
        "template_code": "TPL_DBMAN_BR",
        "template_version": "1.1",
        "created_at": fm.get("created_at") or DATE_FORFAIT,
        "updated_at": DATE_TODAY,
    }

    # tags : retirer core_brain / motor_brain (migres vers brain_layer)
    tags = list(fm.get("tags") or [])
    tags = [t for t in tags if t not in ("core_brain", "motor_brain")]

    # Verif : tags actuels devaient inclure brain_layer source
    raw_tags = fm.get("tags") or []
    has_core = "core_brain" in raw_tags
    has_motor = "motor_brain" in raw_tags
    if not (has_core or has_motor):
        notes.append(f"!! Brain layer source missing in tags : {file_name} (mapping force={mapping['brain_layer']})")

    summary = fm.get("summary")
    summary_todo = False
    if not summary:
        summary = ""
        summary_todo = True

    spec = {
        "bdd_canonical_name": bdd_name,
        "object_type": mapping["object_type"],
        "architecture_scope": "Brain",
        "brain_layer": mapping["brain_layer"],
        "brain_subtype": mapping["brain_subtype"],
        "summary": summary,
        "purpose": fm.get("purpose", ""),
        "tags": tags,
    }

    if summary_todo:
        notes.append(f"__summary_todo__:{file_name}")

    return identity, meta, spec, notes


# -----------------------------------------------------------------------------
# Driver
# -----------------------------------------------------------------------------

def list_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(
        p for p in directory.iterdir()
        if p.is_file() and p.suffix == ".md" and p.name.startswith("Manuel de BDD - ")
    )


def process(category: str, files: list[Path], migrator, apply: bool) -> dict:
    stats = {"detected": len(files), "migrated": 0, "skipped": 0, "errors": 0,
             "codes": [], "summary_todos": [], "anomalies": []}

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            stats["errors"] += 1
            stats["anomalies"].append(f"READ ERR {path.name}: {e}")
            continue

        if is_already_canon(text):
            stats["skipped"] += 1
            continue

        fm, body = split_frontmatter(text)
        if fm is None:
            stats["errors"] += 1
            stats["anomalies"].append(f"NO FRONTMATTER {path.name}")
            continue

        identity, meta, spec, notes = migrator(fm, path.name)
        if identity is None:
            stats["errors"] += 1
            for n in notes:
                stats["anomalies"].append(n)
            continue

        summary_todo_flag = any(n.startswith("__summary_todo__:") for n in notes)
        new_fm = build_canonical_frontmatter(identity, meta, spec, summary_todo=summary_todo_flag)
        new_text = new_fm + body

        # Apostrophes typographiques R-052 : preserver les U+2019 existants
        # (pyyaml ne touche pas aux non-ASCII avec allow_unicode=True). Verif minimale :
        if "'" in new_fm and any(re.search(r"[a-z]'[a-z]", line) for line in new_fm.splitlines()):
            # apostrophe ASCII detectee dans valeur autre que delimiter -> warning
            pass  # acceptable car YAML peut quoter avec ' comme delimiter

        stats["migrated"] += 1
        stats["codes"].append(f"{path.name} -> {identity['code']}")
        for n in notes:
            if n.startswith("__summary_todo__:"):
                stats["summary_todos"].append(n.split(":", 1)[1])
            else:
                stats["anomalies"].append(n)

        if apply:
            path.write_text(new_text, encoding="utf-8")

    return stats


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--dry-run", action="store_true", default=True)
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    apply = args.apply

    print(f"Mode : {'APPLY' if apply else 'DRY-RUN'}\n")

    twin_files = list_files(DIR_TWIN)
    mo_files = list_files(DIR_MO)
    brain_files = list_files(DIR_BRAIN)

    print(f"Twin  : {len(twin_files)} fichiers")
    print(f"MO    : {len(mo_files)} fichiers")
    print(f"Brain : {len(brain_files)} fichiers")
    print(f"Total : {len(twin_files) + len(mo_files) + len(brain_files)} fichiers\n")

    results = {
        "Twin": process("Twin", twin_files, migrate_twin, apply),
        "MO": process("MO", mo_files, migrate_mo, apply),
        "Brain": process("Brain", brain_files, migrate_brain, apply),
    }

    print("=" * 70)
    for cat, st in results.items():
        print(f"\n[{cat}] detected={st['detected']} migrated={st['migrated']} "
              f"skipped={st['skipped']} errors={st['errors']}")
        if st["anomalies"]:
            print("  Anomalies :")
            for a in st["anomalies"]:
                print(f"    - {a}")
        if st["summary_todos"]:
            print(f"  Summary TODO ({len(st['summary_todos'])}):")
            for f in st["summary_todos"]:
                print(f"    - {f}")

    print("\n" + "=" * 70)
    print("Codes generes :")
    for cat in ("Twin", "MO", "Brain"):
        print(f"\n[{cat}]")
        for c in results[cat]["codes"]:
            print(f"  {c}")


if __name__ == "__main__":
    main()
