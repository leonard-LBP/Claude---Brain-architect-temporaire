"""Parser robuste pour les manuels Twin v2 (Phase 6.5 audit final).

Extrait toutes les props de la section 4.x (4.1 → 4.5) pour chaque manuel.
Catégorise précisément : générique, spécifique, jumelle texte, relation, rollup,
calculé natif, formule différée.

Sortie : output/manuel_<NOM>.json par BDD.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

MANUALS_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Digital Twin")
OUT_DIR = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_final/manuels_parsed")
OUT_DIR.mkdir(parents=True, exist_ok=True)


# Patterns
SECTION_RE = re.compile(r"^## (4\.\d+)\b")
TABLE_HEADER_RE = re.compile(r"^\|\s+Champ\s+\|\s+Portée")
TABLE_SEP_RE = re.compile(r"^\|[\s\-:|]+$")


def detect_type(raw_type):
    """Catégorise le raw_type Type du manuel en type abstrait."""
    rt = raw_type.lower().strip()
    # ROLLUP / AGRÉGATION doit gagner sur RELATION (cas "Agrégation / rollup indirect (relation : ...)")
    if "rollup" in rt or "agrégation" in rt:
        return "ROLLUP"
    if "relation" in rt:
        return "RELATION"
    if "formule" in rt:
        return "FORMULA"
    if "sélection" in rt or "selection" in rt:
        if "multi" in rt:
            return "MULTI_SELECT"
        return "SELECT"
    if "multi-sélection" in rt or "multi-selection" in rt or "multi sélection" in rt:
        return "MULTI_SELECT"
    if "url" in rt:
        return "URL"
    if "date" in rt:
        return "DATE"
    if "nombre" in rt or "number" in rt:
        return "NUMBER"
    if "texte" in rt or "text" in rt or "log" in rt:
        return "RICH_TEXT"
    if "title" in rt or rt == "":
        return "TITLE"
    return "UNKNOWN"


def is_formula_differee(prop):
    """Détermine si une formule est différée (à exclure de l'audit Notion)."""
    if prop["type"] != "FORMULA":
        return False
    # Formules différées connues
    name = prop["name"].lower()
    differees_keywords = [
        "amplitude", "risque de plafond", "vulnérabilité", "dépendance externe",
        "pression contextuelle", "régime d'environnement", "indice composite",
        "score consolidé", "alerte", "criticité d'arbitrage",
    ]
    for kw in differees_keywords:
        if kw in name:
            return True
    # Si le manuel mentionne explicitement "différé" dans le raw_type
    raw = prop.get("raw_type", "").lower()
    if "différée" in raw or "calcul différé" in raw or "à différer" in raw:
        return True
    return False


def is_rollup_multi_source_or_indirect(prop):
    """Rollup multi-source ou indirect (déjà différés en backlog Phase 6.5)."""
    if prop["type"] != "ROLLUP":
        return False
    raw = prop.get("raw_type", "").lower()
    if "multi-source" in raw or "indirect" in raw or "intermédiaire" in raw:
        return True
    return False


def is_source_relation(prop):
    """Détermine si c'est la relation différée Sources d'informations (à exclure)."""
    name = prop["name"].lower()
    if prop["type"] == "RELATION" and "source" in name and "information" in name:
        return True
    return False


def parse_table_row(line):
    """Parse une ligne de table markdown. Retourne dict ou None si invalide."""
    line = line.strip()
    if not line.startswith("|") or not line.endswith("|"):
        return None
    # Split sur | en respectant les contenus
    cells = [c.strip() for c in line.split("|")[1:-1]]
    if len(cells) < 4:
        return None
    return cells


def parse_manuel(path):
    """Parse un manuel Twin et retourne dict {section: [props]}."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Parse frontmatter for has_advanced_note
    has_advanced_note = True
    in_frontmatter = False
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            break
        if in_frontmatter:
            if line.startswith("has_advanced_note:"):
                val = line.split(":", 1)[1].strip().lower()
                has_advanced_note = val in ("true", "yes", "1")

    # Find each 4.x section and parse the first table
    sections = {}
    current_section = None
    in_table = False
    headers = None
    rows = []

    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            # Close previous section if any
            if current_section and rows:
                sections.setdefault(current_section, []).extend(rows)
            current_section = m.group(1)
            in_table = False
            headers = None
            rows = []
            continue

        if current_section is None:
            continue

        # Detect table start
        if TABLE_HEADER_RE.match(line):
            cells = parse_table_row(line)
            if cells:
                headers = [c.strip() for c in cells]
                in_table = True
                continue

        # Skip separator
        if in_table and TABLE_SEP_RE.match(line):
            continue

        # Parse row
        if in_table and line.startswith("|"):
            cells = parse_table_row(line)
            if cells and len(cells) >= 4:
                # Skip if first cell is "Champ" (header re-emission) or empty
                if cells[0].strip().lower() in ("champ", ""):
                    continue
                # Build prop dict
                name = cells[0].strip()
                portee = cells[1].strip() if len(cells) > 1 else ""
                raw_type = cells[2].strip() if len(cells) > 2 else ""
                taxos_str = cells[3].strip() if len(cells) > 3 else ""
                taxos = [t.strip() for t in re.split(r"[,;]", taxos_str) if t.strip() and t.strip() != "—"]
                cardinalite = cells[4].strip() if len(cells) > 4 else ""
                rows.append({
                    "name": name,
                    "portee": portee,
                    "raw_type": raw_type,
                    "type": detect_type(raw_type),
                    "taxonomies": taxos,
                    "cardinalite": cardinalite,
                    "section": current_section,
                })

        # Detect end of table (empty line or new ## section)
        if in_table and (not line.strip() or line.startswith("## ")):
            in_table = False

    # Close last section
    if current_section and rows:
        sections.setdefault(current_section, []).extend(rows)

    # Flatten into single list with section preserved
    all_props = []
    for sec, props in sections.items():
        all_props.extend(props)

    # Categorize each prop with audit flags
    for p in all_props:
        p["expected_in_notion"] = (
            p["type"] not in ("FORMULA",)
            and not is_formula_differee(p)
            and not is_source_relation(p)
            and not is_rollup_multi_source_or_indirect(p)
        )
        p["expected_in_wrrd"] = True  # toutes les props sont attendues dans WR-RD
        p["is_formula_differee"] = is_formula_differee(p)
        p["is_source_relation"] = is_source_relation(p)
        p["is_rollup_multi_source_or_indirect"] = is_rollup_multi_source_or_indirect(p)

    return {
        "has_advanced_note": has_advanced_note,
        "props": all_props,
        "n_props": len(all_props),
        "n_expected_notion": sum(1 for p in all_props if p["expected_in_notion"]),
        "n_expected_wrrd": sum(1 for p in all_props if p["expected_in_wrrd"]),
    }


def main():
    files = sorted(MANUALS_DIR.glob("Manuel de BDD - *.md"))
    summary = {}
    for f in files:
        bdd_name = f.stem.replace("Manuel de BDD - ", "")
        try:
            parsed = parse_manuel(f)
            out_path = OUT_DIR / f"{bdd_name}.json"
            with open(out_path, "w", encoding="utf-8") as fp:
                json.dump(parsed, fp, indent=2, ensure_ascii=False)
            summary[bdd_name] = {
                "n_props": parsed["n_props"],
                "n_expected_notion": parsed["n_expected_notion"],
                "n_expected_wrrd": parsed["n_expected_wrrd"],
                "has_advanced_note": parsed["has_advanced_note"],
            }
            print(f"  ✓ {bdd_name:45s} : {parsed['n_props']} props ({parsed['n_expected_notion']} attendues Notion)")
        except Exception as e:
            print(f"  ✗ {bdd_name}: {e}")
            summary[bdd_name] = {"error": str(e)}

    summary_path = OUT_DIR.parent / "manuels_summary.json"
    with open(summary_path, "w", encoding="utf-8") as fp:
        json.dump(summary, fp, indent=2, ensure_ascii=False)
    print(f"\n✓ {len(files)} manuels parsés.")
    print(f"  Détails : {OUT_DIR}")
    print(f"  Summary : {summary_path}")


if __name__ == "__main__":
    main()
