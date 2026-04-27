"""Parser manuels Mission Ops (audit final) — adapté de parse_manuel.py."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

MANUALS_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Mission Ops")
OUT_DIR = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_final_missionops/manuels_parsed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SECTION_RE = re.compile(r"^## (4\.\d+)\b")
TABLE_HEADER_RE = re.compile(r"^\|\s+Champ\s+\|\s+Portée")
TABLE_SEP_RE = re.compile(r"^\|[\s\-:|]+$")

# Pass 4 différée : 3 props attendues manuel + WR-RD mais ABSENTES Notion (état temporaire)
PASS4_DEFERRED = {
    "Actions LBP": {
        "nb actions (activité)",
        "nb actions terminées (activité)",
        "avancement (activité)",
    }
}


def detect_type(raw_type):
    rt = raw_type.lower().strip()
    if "rollup" in rt or "agrégation" in rt:
        return "ROLLUP"
    if "relation" in rt:
        return "RELATION"
    if "formule" in rt:
        return "FORMULA"
    if "multi-sélection" in rt or "multi-selection" in rt or "multi sélection" in rt:
        return "MULTI_SELECT"
    if "sélection" in rt or "selection" in rt:
        return "SELECT"
    if "url" in rt:
        return "URL"
    if "date" in rt:
        return "DATE"
    if "nombre" in rt or "number" in rt:
        return "NUMBER"
    if "case" in rt or "checkbox" in rt:
        return "CHECKBOX"
    if "personne" in rt or "people" in rt:
        return "PEOPLE"
    if "fichier" in rt or "file" in rt:
        return "FILES"
    if "texte" in rt or "text" in rt or "log" in rt:
        return "RICH_TEXT"
    if "title" in rt or rt == "":
        return "TITLE"
    return "UNKNOWN"


def is_formula_differee(prop):
    if prop["type"] != "FORMULA":
        return False
    raw = prop.get("raw_type", "").lower()
    if "différée" in raw or "calcul différé" in raw or "à différer" in raw or "différé" in raw:
        return True
    return False


def parse_table_row(line):
    line = line.strip()
    if not line.startswith("|") or not line.endswith("|"):
        return None
    cells = [c.strip() for c in line.split("|")[1:-1]]
    if len(cells) < 4:
        return None
    return cells


def parse_manuel(path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

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

    sections = {}
    current_section = None
    in_table = False
    headers = None
    rows = []

    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            if current_section and rows:
                sections.setdefault(current_section, []).extend(rows)
            current_section = m.group(1)
            in_table = False
            headers = None
            rows = []
            continue

        if current_section is None:
            continue

        if TABLE_HEADER_RE.match(line):
            cells = parse_table_row(line)
            if cells:
                headers = [c.strip() for c in cells]
                in_table = True
                continue

        if in_table and TABLE_SEP_RE.match(line):
            continue

        if in_table and line.startswith("|"):
            cells = parse_table_row(line)
            if cells and len(cells) >= 4:
                if cells[0].strip().lower() in ("champ", ""):
                    continue
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

        if in_table and (not line.strip() or line.startswith("## ")):
            in_table = False

    if current_section and rows:
        sections.setdefault(current_section, []).extend(rows)

    all_props = []
    for sec, props in sections.items():
        all_props.extend(props)

    bdd_name_path = path.stem.replace("Manuel de BDD - ", "")
    pass4 = PASS4_DEFERRED.get(bdd_name_path, set())

    for p in all_props:
        name_norm = p["name"].lower().replace("’", "'").strip()
        is_pass4 = name_norm in pass4
        p["is_pass4_deferred"] = is_pass4
        p["expected_in_notion"] = (
            p["type"] not in ("FORMULA",)
            and not is_formula_differee(p)
            and not is_pass4
        )
        p["expected_in_wrrd"] = True
        p["is_formula_differee"] = is_formula_differee(p)

    return {
        "has_advanced_note": has_advanced_note,
        "props": all_props,
        "n_props": len(all_props),
        "n_expected_notion": sum(1 for p in all_props if p["expected_in_notion"]),
        "n_expected_wrrd": sum(1 for p in all_props if p["expected_in_wrrd"]),
        "n_pass4_deferred": sum(1 for p in all_props if p.get("is_pass4_deferred")),
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
                "n_pass4_deferred": parsed["n_pass4_deferred"],
                "has_advanced_note": parsed["has_advanced_note"],
            }
            print(f"  OK {bdd_name:35s} : {parsed['n_props']} props ({parsed['n_expected_notion']} attendues Notion ; {parsed['n_pass4_deferred']} pass4-deferred)")
        except Exception as e:
            print(f"  KO {bdd_name}: {e}")
            summary[bdd_name] = {"error": str(e)}

    summary_path = OUT_DIR.parent / "manuels_summary.json"
    with open(summary_path, "w", encoding="utf-8") as fp:
        json.dump(summary, fp, indent=2, ensure_ascii=False)
    print(f"\nOK {len(files)} manuels parses.")


if __name__ == "__main__":
    main()
