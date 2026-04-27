#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit + fix exhaustif Manuel Twin <-> WR-RD.
Pour chaque manuel parse, verifie que toutes les props expected_in_wrrd sont aussi
dans le WR-RD, et ajoute les manquantes en extrayant les colonnes pertinentes
depuis le manuel original.
"""
import json
import os
import re
import sys
from pathlib import Path

PARSED_DIR = Path(r"C:\Users\leona\LBP - dev\Claude - Brain architect temporaire\scripts\phase6.5\audit_final\manuels_parsed")
WRRD_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Digital Twin\WR-RD")
MANUEL_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Digital Twin")

SYSTEM_PROPS = {"Created Date", "Last Updated Date"}

def normalize(s: str) -> str:
    """Normalize apostrophes for comparison (U+2019 <-> U+0027)."""
    if s is None:
        return ""
    return s.replace("’", "'").strip()

def split_md_row(line: str):
    """Split a markdown table row into cells."""
    line = line.strip()
    if not line.startswith("|"):
        return None
    # Remove leading/trailing pipes
    inner = line.strip().strip("|")
    cells = [c.strip() for c in inner.split("|")]
    return cells

def is_separator_row(line: str) -> bool:
    line = line.strip()
    if not line.startswith("|"):
        return False
    inner = line.strip().strip("|")
    cells = [c.strip() for c in inner.split("|")]
    return all(re.fullmatch(r":?-+:?", c) for c in cells if c)

def parse_manuel_tables(text: str):
    """
    Parse manuel sections 4.1, 4.2, 4.3, 4.4, 4.5 etc.
    Returns dict[prop_name_normalized] -> dict with all 12 columns.
    Manuel cols: Champ | Portee | Type | Taxonomie | Cardinalite | Nature de production | Forme logique | Instructions | Prerequis | Clefs de lecture | Utilite | Exemples
    """
    props = {}
    lines = text.splitlines()
    i = 0
    current_section = None
    in_table = False
    headers = None
    while i < len(lines):
        line = lines[i]
        # Detect section header like "## 4.1 ..." or "## 4.2 ..."
        m = re.match(r"^##\s+(\d+\.\d+)\s+", line)
        if m:
            current_section = m.group(1)
            in_table = False
            headers = None
            i += 1
            continue
        # Detect table headers
        if current_section and current_section.startswith("4.") and line.strip().startswith("| Champ "):
            headers = split_md_row(line)
            in_table = True
            i += 1
            # next line should be separator
            if i < len(lines) and is_separator_row(lines[i]):
                i += 1
            continue
        if in_table:
            if line.strip().startswith("|"):
                cells = split_md_row(line)
                if cells and len(cells) >= 2:
                    name = cells[0]
                    if name and not is_separator_row(line):
                        key = normalize(name)
                        # Map cols based on header
                        col_map = {}
                        for h, v in zip(headers, cells):
                            col_map[h.strip()] = v
                        col_map["_section"] = current_section
                        col_map["_raw_name"] = name
                        props[key] = col_map
            else:
                in_table = False
                headers = None
        i += 1
    return props

def parse_wrrd_tables(text: str):
    """
    Parse WR-RD sections. Returns:
      - props: dict[normalized_name] -> dict with 9 cols + section info
      - sections: list of (section_num, section_title, table_start_line, table_end_line, last_row_line)
      - lines: original lines list
    """
    lines = text.splitlines()
    props = {}
    sections = []  # list of {num, title, header_line, sep_line, last_row_line, cols}
    i = 0
    current = None
    in_table = False
    headers = None
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^##\s+(\d+)\)\s+(.+)$", line)
        if m:
            if current is not None:
                sections.append(current)
            current = {
                "num": m.group(1),
                "title": m.group(2),
                "header_line": None,
                "sep_line": None,
                "last_row_line": None,
                "cols": None,
                "props_in_section": [],
            }
            in_table = False
            headers = None
            i += 1
            continue
        if current and line.strip().startswith("| Champ "):
            headers = split_md_row(line)
            current["header_line"] = i
            current["cols"] = headers
            in_table = True
            i += 1
            if i < len(lines) and is_separator_row(lines[i]):
                current["sep_line"] = i
                i += 1
            continue
        if in_table:
            if line.strip().startswith("|") and not is_separator_row(line):
                cells = split_md_row(line)
                if cells and len(cells) >= 2 and cells[0]:
                    name = cells[0]
                    key = normalize(name)
                    col_map = {}
                    for h, v in zip(headers, cells):
                        col_map[h.strip()] = v
                    col_map["_section_num"] = current["num"]
                    props[key] = col_map
                    current["last_row_line"] = i
                    current["props_in_section"].append(key)
            elif not line.strip().startswith("|"):
                in_table = False
                headers = None
        i += 1
    if current is not None:
        sections.append(current)
    return props, sections, lines

def build_wrrd_row(manuel_row: dict) -> str:
    """
    Build a 9-col WR-RD row from a 12-col manuel row.
    WR-RD cols: Champ | Type | Taxonomie | Cardinalite | Forme logique | Instructions | Clefs de lecture | Utilite | Exemples
    Manuel cols (key names as they appear in markdown header):
    """
    def g(key_substring):
        for k, v in manuel_row.items():
            if k.startswith("_"):
                continue
            if key_substring.lower() in k.lower():
                return v.strip() if v else ""
        return ""

    nom = manuel_row.get("_raw_name", "").strip()
    typ = g("Type")
    taxo = g("Taxonomie")
    card = g("Cardinalité")
    forme = g("Forme logique")
    instr = g("Instructions")
    clefs = g("Clefs de lecture")
    util = g("Utilité")
    ex = g("Exemples")

    # Special heuristic: 'Type' might match 'Type' column not 'Nature de production'
    # The manuel headers in order: Champ | Portée | Type | Taxonomie ...
    # Fix in case 'Type' picked up wrong
    headers_in_order = [k for k in manuel_row.keys() if not k.startswith("_")]
    # Use positional: Champ=0, Portée=1, Type=2, Taxonomie=3, Cardinalité=4, Nature=5, Forme=6, Instructions=7, Prérequis=8, Clefs=9, Utilité=10, Exemples=11
    if len(headers_in_order) == 12:
        nom = manuel_row[headers_in_order[0]].strip()
        typ = manuel_row[headers_in_order[2]].strip()
        taxo = manuel_row[headers_in_order[3]].strip()
        card = manuel_row[headers_in_order[4]].strip()
        forme = manuel_row[headers_in_order[6]].strip()
        instr = manuel_row[headers_in_order[7]].strip()
        clefs = manuel_row[headers_in_order[9]].strip()
        util = manuel_row[headers_in_order[10]].strip()
        ex = manuel_row[headers_in_order[11]].strip()

    cells = [nom, typ, taxo, card, forme, instr, clefs, util, ex]
    # Sanitize: collapse newlines/pipes within cells
    cells = [c.replace("\n", " ").replace("|", "\\|") for c in cells]
    return "| " + " | ".join(cells) + " |"

def find_section_for_prop(sections, manuel_section: str, manuel_props_keys_by_section):
    """
    Map manuel section (e.g. '4.1') to WR-RD section number (e.g. '1').
    Heuristic mapping: 4.1 -> 1, 4.2 -> 2, 4.3 -> 3, 4.4 -> 4, 4.5 -> 5
    """
    mapping = {"4.1": "1", "4.2": "2", "4.3": "3", "4.4": "4", "4.5": "5", "4.6": "6", "4.7": "7"}
    target_num = mapping.get(manuel_section)
    if not target_num:
        return None
    for s in sections:
        if s["num"] == target_num:
            return s
    return None

def insert_into_wrrd(lines, section, new_row: str):
    """
    Insert new_row at end of section's table (after last_row_line).
    Returns updated lines list and new last_row_line offset.
    """
    if section.get("last_row_line") is not None:
        idx = section["last_row_line"] + 1
    elif section.get("sep_line") is not None:
        idx = section["sep_line"] + 1
    else:
        return lines, None
    new_lines = lines[:idx] + [new_row] + lines[idx:]
    return new_lines, idx

def process_one(parsed_path: Path, dry_run: bool = False):
    bdd_name = parsed_path.stem  # e.g. "Modulateurs"
    wrrd_path = WRRD_DIR / f"WR-RD - {bdd_name}.md"
    manuel_path = MANUEL_DIR / f"Manuel de BDD - {bdd_name}.md"

    result = {
        "bdd": bdd_name,
        "missing_added": [],
        "type_mismatches": [],
        "wrrd_missing": False,
        "manuel_missing": False,
        "error": None,
    }

    if not wrrd_path.exists():
        result["wrrd_missing"] = True
        return result
    if not manuel_path.exists():
        result["manuel_missing"] = True
        return result

    parsed = json.loads(parsed_path.read_text(encoding="utf-8"))
    expected = [p for p in parsed["props"] if p.get("expected_in_wrrd") and p["name"] not in SYSTEM_PROPS]

    manuel_text = manuel_path.read_text(encoding="utf-8")
    manuel_rows = parse_manuel_tables(manuel_text)

    wrrd_text = wrrd_path.read_text(encoding="utf-8")
    wrrd_props, wrrd_sections, wrrd_lines = parse_wrrd_tables(wrrd_text)

    # Detect missing
    for p in expected:
        key = normalize(p["name"])
        if key not in wrrd_props:
            # Find row in manuel
            mrow = manuel_rows.get(key)
            if not mrow:
                result["missing_added"].append({
                    "name": p["name"],
                    "section": p.get("section"),
                    "status": "manuel_row_not_found",
                })
                continue
            section = find_section_for_prop(wrrd_sections, p.get("section", ""), None)
            if not section:
                result["missing_added"].append({
                    "name": p["name"],
                    "section": p.get("section"),
                    "status": "no_target_wrrd_section",
                })
                continue
            new_row = build_wrrd_row(mrow)
            wrrd_lines, ins_idx = insert_into_wrrd(wrrd_lines, section, new_row)
            # Update last_row_line for following sections (shift by 1) and for current
            for s in wrrd_sections:
                if s.get("header_line") is not None and s["header_line"] >= ins_idx:
                    s["header_line"] += 1
                if s.get("sep_line") is not None and s["sep_line"] >= ins_idx:
                    s["sep_line"] += 1
                if s.get("last_row_line") is not None and s["last_row_line"] >= ins_idx:
                    s["last_row_line"] += 1
            section["last_row_line"] = ins_idx
            result["missing_added"].append({
                "name": p["name"],
                "section": p.get("section"),
                "status": "added",
                "wrrd_section": section["num"],
            })
        else:
            # Both present: check type mismatch
            wrrd_type = wrrd_props[key].get("Type", "").strip()
            manuel_type = p.get("raw_type", "").strip()
            # Simplified comparison: just check the basic type label
            wt_low = wrrd_type.lower()
            mt_low = manuel_type.lower()
            # Consider mismatch only if first word differs significantly
            wfirst = wt_low.split()[0] if wt_low else ""
            mfirst = mt_low.split()[0] if mt_low else ""
            if wfirst and mfirst and wfirst != mfirst:
                # Special: "Relation" / "Rollup" / "Formule" are full prefixes
                # Check if both are same type family
                fams = ["texte", "sélection", "multi-sélection", "url", "date", "nombre",
                        "case", "personne", "fichier", "relation", "rollup", "formule",
                        "formula", "id", "création"]
                wfam = next((f for f in fams if wt_low.startswith(f)), None)
                mfam = next((f for f in fams if mt_low.startswith(f)), None)
                if wfam != mfam:
                    result["type_mismatches"].append({
                        "name": p["name"],
                        "wrrd_type": wrrd_type,
                        "manuel_type": manuel_type,
                    })

    # Write back if changes
    added_count = sum(1 for x in result["missing_added"] if x["status"] == "added")
    if added_count > 0 and not dry_run:
        new_text = "\n".join(wrrd_lines)
        # Preserve trailing newline if original had one
        if wrrd_text.endswith("\n") and not new_text.endswith("\n"):
            new_text += "\n"
        wrrd_path.write_text(new_text, encoding="utf-8")

    return result

def main():
    dry = "--dry" in sys.argv
    results = []
    parsed_files = sorted(PARSED_DIR.glob("*.json"))
    for pf in parsed_files:
        try:
            r = process_one(pf, dry_run=dry)
        except Exception as e:
            r = {"bdd": pf.stem, "error": str(e), "missing_added": [], "type_mismatches": []}
        results.append(r)

    # Print report
    total_added = 0
    total_modified = 0
    total_mismatches = 0
    print("=" * 80)
    print("AUDIT WR-RD <-> Manuel Twin")
    print("=" * 80)
    for r in results:
        added = [x for x in r.get("missing_added", []) if x["status"] == "added"]
        not_added = [x for x in r.get("missing_added", []) if x["status"] != "added"]
        if r.get("error"):
            print(f"[ERROR] {r['bdd']}: {r['error']}")
            continue
        if r.get("wrrd_missing"):
            print(f"[MISSING WR-RD] {r['bdd']}")
            continue
        if r.get("manuel_missing"):
            print(f"[MISSING MANUEL] {r['bdd']}")
            continue
        n_add = len(added)
        n_mis = len(r.get("type_mismatches", []))
        total_added += n_add
        total_mismatches += n_mis
        if n_add > 0:
            total_modified += 1
        status = "MODIFIED" if n_add > 0 else "OK"
        print(f"[{status}] {r['bdd']}: +{n_add} props ; {n_mis} type mismatches")
        for a in added:
            print(f"    + {a['name']} (manuel section {a['section']} -> WR-RD section {a.get('wrrd_section')})")
        for x in not_added:
            print(f"    ! {x['name']} : {x['status']}")
        for tm in r.get("type_mismatches", []):
            print(f"    ~ TYPE: {tm['name']} | WR-RD={tm['wrrd_type']!r} vs Manuel={tm['manuel_type']!r}")

    print("=" * 80)
    print(f"TOTAL: {len(results)} BDD ; {total_modified} WR-RD modifies ; {total_added} props ajoutees ; {total_mismatches} type mismatches")
    print("=" * 80)

    # Save JSON report
    out = PARSED_DIR.parent / "audit_wrrd_report.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Report -> {out}")

if __name__ == "__main__":
    main()
