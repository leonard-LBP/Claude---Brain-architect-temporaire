"""
Phase 6.5 — Extraction du manifest BDD Twin v2 depuis les manuels.

Pour chaque manuel Twin, parse la section 4 (4.1 à 4.5) et produit un JSON
structuré décrivant la BDD à générer sur Notion :
  - properties.natives : types simples (text, select, multi_select, date, formula)
  - properties.relations : relations bidirectionnelles + monodirectionnelles (Sources)
  - properties.rollups : rollups avec relation source + propriété cible
  - properties.text_twins : jumelles textes (text long associé à une relation)
  - bloc d'ordering R-047

Source de vérité (R-045) : manuel parent.
"""

import os
import re
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

VAULT_TWIN = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Manuels de BDD/Digital Twin")
TAXO_DIR = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Taxonomies")
OUT_DIR = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ----------------- HELPERS -----------------

def read_file(fp):
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()


def split_table_row(line):
    """Split a markdown table row into trimmed cells. Drops leading/trailing |."""
    if not line.strip().startswith("|"):
        return None
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts


def extract_section_table(content, section_header):
    """Extract a markdown table that follows a `## section_header` line.
    Returns list of dict rows keyed by header. None if section absent or empty."""
    lines = content.split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.strip().startswith("## ") and section_header in ln:
            start = i
            break
    if start is None:
        return None
    # Find table header (first | line after start)
    h_idx = None
    for j in range(start + 1, min(start + 50, len(lines))):
        if lines[j].lstrip().startswith("|"):
            h_idx = j
            break
        # If next ## appears before any table, no table here
        if lines[j].strip().startswith("## ") or lines[j].strip().startswith("# "):
            return None
    if h_idx is None:
        return None
    headers = split_table_row(lines[h_idx])
    if not headers:
        return None
    # row j+1 is separator |---|---| → skip
    rows = []
    j = h_idx + 2
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        cells = split_table_row(lines[j])
        if cells and len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
        j += 1
    return rows


# ----------------- TYPE CLASSIFICATION -----------------

def classify_field(row):
    """Given a row from section 4 of a manuel, classify it into:
    - 'relation_bidirectional', 'relation_monodirectional'
    - 'rollup'
    - 'formula'
    - 'text_twin'   (jumelle texte de relation, type=Texte long et nom contient (texte))
    - 'select', 'multi_select', 'text_short', 'text_long', 'date', 'number'
    Returns (category, extra_info_dict)."""
    type_ = row.get("Type", "")
    name = row.get("Champ", "")
    cardinality = row.get("Cardinalité / multiplicité", "")
    nature = row.get("Nature de production", "")

    # Rollup
    if type_.startswith("Rollup"):
        m = re.match(r"Rollup \((.+?) → (.+?)\)", type_)
        if m:
            source_relation = m.group(1).strip()
            target_property = m.group(2).strip()
            return "rollup", {
                "source_relation": source_relation,
                "target_property": target_property,
            }
        return "rollup", {"raw_type": type_}

    # Relation
    if type_.startswith("Relation"):
        # Patterns:
        # "Relation (bidirectionnelle ; BDD cible : X ; Propriété cible : Y)"
        # "Relation (BDD cible : X)" → mono
        is_bidir = "bidirectionnelle" in type_.lower()
        target_db_m = re.search(r"BDD cible\s*:\s*([^;)]+)", type_)
        # Mirror peut contenir des parens (ex. "comprend (actifs)") ; greedy + ancrage fin de cellule
        mirror_m = re.search(r"Propriété cible\s*:\s*(.+)\)\s*$", type_)
        info = {
            "target_db": target_db_m.group(1).strip() if target_db_m else None,
            "mirror_property": mirror_m.group(1).strip() if mirror_m else None,
            "raw_type": type_,
        }
        return ("relation_bidirectional" if is_bidir else "relation_monodirectional", info)

    # Formula
    if type_ == "Formule":
        return "formula", {}

    # Date
    if type_ == "Date":
        return "date", {}

    # Number
    if type_ in ("Number", "Nombre"):
        return "number", {}

    # URL (e.g. Lien vers la note avancée)
    if type_ == "URL":
        return "url", {}

    # Select / Multi-select
    if type_ == "Sélection":
        return "select", {}
    if type_ == "Multi-sélection":
        return "multi_select", {}

    # Text — distinguish text_short (Texte court) from text_long
    # Jumelle texte = Texte long avec "(texte)" dans le nom OU "Forme logique attendue" qui dit "Jumelle texte"
    forme = row.get("Forme logique attendue", "")
    if "Jumelle texte de relation" in forme:
        return "text_twin", {}
    if type_ == "Texte court":
        return "text_short", {}
    if type_ == "Texte long":
        return "text_long", {}

    return "unknown", {"raw_type": type_}


# ----------------- BLOC ORDERING (R-047) -----------------

# Bloc 1 — tête générique
HEAD_GENERIC = [
    "Nom",
    "Aliases",
    "Description",
    "Statut de l'objet",
    "Statut de l’objet",  # apostrophe variant
    "Erreurs de transcription",
]

# Bloc 3 — queue générique (R-047 v2.1 : Lien vers la note avancée en tête)
TAIL_GENERIC = [
    "Lien vers la note avancée",  # R-050, conditionnel, tête du Bloc 3
    "Exemples concrets",
    "Commentaires libres",
    "Notes du consultant",
    "Confidentialité (option)",
    "Confidentialité",
    "Indices observés",
    "Indices d'existence de l'objet",
    "Indices d’existence de l’objet",
    "Created Date",
    "Last Updated Date",
    "Logs / Révisions LBP",
    "Merge Notes",
    "Merge Flags",
]

# Bloc 4 — sources
SOURCES = [
    "Source(s) d'information (texte)",
    "Source(s) d’information (texte)",
    "Source(s) d'information",
    "Source(s) d’information",
]


def classify_block(field_name):
    """Return 1, 2, 3 or 4 (R-047 block)."""
    name = field_name.strip()
    # Normalize apostrophes
    name_norm = name.replace("’", "'")
    head_norm = [n.replace("’", "'") for n in HEAD_GENERIC]
    tail_norm = [n.replace("’", "'") for n in TAIL_GENERIC]
    sources_norm = [n.replace("’", "'") for n in SOURCES]
    if name_norm in head_norm:
        return 1
    if name_norm in tail_norm:
        return 3
    if name_norm in sources_norm:
        return 4
    return 2


# ----------------- TAXO EXTRACTION -----------------

def extract_taxo_from_text(taxo_str):
    """Returns a list of taxonomy codes referenced (e.g. ['ASSET.SUBTYPE.LBP'])."""
    if not taxo_str or taxo_str == "—":
        return []
    # Codes are pattern WORD.WORD.LBP or A.B.C
    codes = re.findall(r"\b[A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]*(?:\.[A-Z][A-Z0-9_]*)?(?:\.LBP)?\b", taxo_str)
    return list(dict.fromkeys(codes))  # dedupe preserving order


def extract_niveau_from_instruction(instruction_str):
    """Look for `Niveau: category` or `Niveau: taxon` in instruction text."""
    m = re.search(r"Niveau\s*:\s*(category|taxon)", instruction_str)
    return m.group(1) if m else None


# ----------------- MANUEL PARSING -----------------

def parse_manuel(fp):
    content = read_file(fp)
    fname = fp.name
    # Extract canonical name from frontmatter
    fm_match = re.search(r"bdd_canonical_name:\s*\"([^\"]+)\"", content)
    canonical_name = fm_match.group(1) if fm_match else fname.replace("Manuel de BDD - ", "").replace(".md", "")
    code_match = re.search(r"object_type:\s*\"([^\"]+)\"", content)
    object_type = code_match.group(1) if code_match else None
    family_match = re.search(r"architecture_family:\s*\"?([^\"\n]+)\"?", content)
    family = family_match.group(1).strip() if family_match else None
    officiality_match = re.search(r"officiality_regime:\s*\"?([^\"\n]+)\"?", content)
    officiality = officiality_match.group(1).strip() if officiality_match else None

    # Parse sections 4.1 to 4.5
    sections = {}
    section_titles = {
        "4.1": "4.1 Propriétés génériques",
        "4.2": "4.2 Propriétés spécifiques",
        "4.3": "4.3 Relations + jumelles textes + rollups relationnels",
        "4.4": "4.4 Couche 5D",
        "4.5": "4.5 Couche calculée",
    }
    for key, header in section_titles.items():
        rows = extract_section_table(content, header)
        sections[key] = rows  # may be None or []

    # Build properties list
    properties = {
        "natives": [],       # text, select, multi_select, date, number, formula
        "relations": [],     # bidir + mono
        "rollups": [],
        "text_twins": [],
    }

    seen_names = set()

    for sec_key, rows in sections.items():
        if not rows:
            continue
        for row in rows:
            name = row.get("Champ", "").strip()
            if not name or name in seen_names:
                continue
            seen_names.add(name)
            category, extra = classify_field(row)
            taxo_codes = extract_taxo_from_text(row.get("Taxonomie(s) — codes", ""))
            niveau = extract_niveau_from_instruction(row.get("Instructions d'écriture", "") + " " + row.get("Instructions d’écriture", ""))
            block = classify_block(name)

            entry = {
                "name": name,
                "category": category,
                "type_raw": row.get("Type", ""),
                "portee": row.get("Portée", ""),
                "cardinality": row.get("Cardinalité / multiplicité", ""),
                "nature": row.get("Nature de production", ""),
                "forme_logique": row.get("Forme logique attendue", ""),
                "taxo_codes": taxo_codes,
                "taxo_niveau": niveau,
                "block": block,
                "section": sec_key,
            }

            if category in ("relation_bidirectional", "relation_monodirectional"):
                entry.update(extra)
                entry["bidirectional"] = (category == "relation_bidirectional")
                properties["relations"].append(entry)
            elif category == "rollup":
                entry.update(extra)
                properties["rollups"].append(entry)
            elif category == "text_twin":
                properties["text_twins"].append(entry)
            else:
                properties["natives"].append(entry)

    return {
        "canonical_name": canonical_name,
        "object_type": object_type,
        "architecture_family": family,
        "officiality_regime": officiality,
        "source_manuel": str(fp.name),
        "code": f"DB_{canonical_name.upper().replace(' ', '_').replace('-', '_').replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Ç', 'C')}",
        "properties": properties,
        "sections_present": {k: (v is not None and len(v) > 0) for k, v in sections.items()},
    }


# ----------------- TAXO LOADING -----------------

def load_taxonomy_values(taxo_code):
    """Try to load values from Taxonomies/<taxo_code>.md.
    Returns dict {category_label: [taxon_label1, taxon_label2, ...]} or list of values."""
    fp = TAXO_DIR / f"{taxo_code}.md"
    if not fp.exists():
        return None
    content = read_file(fp)
    # The taxo .md typically has a table of values. Heuristic: extract table after a header
    # with columns like Code | Libellé | ...
    # We just extract all libellé values from the first non-meta table.
    # This is a stub — refined later if needed.
    rows = []
    in_table = False
    headers = None
    for line in content.split("\n"):
        ln = line.strip()
        if ln.startswith("|") and not in_table:
            cells = split_table_row(line)
            if cells and any("ibell" in c.lower() or "alue" in c.lower() or "ode" in c.lower() for c in cells):
                headers = cells
                in_table = True
                continue
        if in_table and ln.startswith("|"):
            cells = split_table_row(line)
            if cells and len(cells) == len(headers) and not all(c.startswith("-") or c == "" for c in cells):
                rows.append(dict(zip(headers, cells)))
        elif in_table and not ln.startswith("|"):
            # End of first table
            if rows:
                break
    return {
        "code": taxo_code,
        "headers": headers,
        "rows": rows,
        "n_values": len(rows),
    }


# ----------------- MAIN -----------------

def main(target=None):
    """If target is provided (canonical name), only process that one."""
    manuels = sorted(VAULT_TWIN.glob("Manuel de BDD - *.md"))
    print(f"Found {len(manuels)} manuels in {VAULT_TWIN}")

    manifest = {}
    for fp in manuels:
        if target and target.lower() not in fp.name.lower():
            continue
        try:
            data = parse_manuel(fp)
            manifest[data["canonical_name"]] = data
            print(f"  ✓ {data['canonical_name']}: {len(data['properties']['natives'])} natives + {len(data['properties']['relations'])} relations + {len(data['properties']['rollups'])} rollups + {len(data['properties']['text_twins'])} text_twins")
        except Exception as e:
            print(f"  ✗ ERROR on {fp.name}: {e}")

    # Collect all referenced taxos
    taxo_codes = set()
    for db in manifest.values():
        for prop_list in db["properties"].values():
            for p in prop_list:
                for code in p.get("taxo_codes", []):
                    taxo_codes.add(code)
    print(f"\n{len(taxo_codes)} unique taxonomies referenced")

    # Load taxo values
    taxos = {}
    for code in sorted(taxo_codes):
        v = load_taxonomy_values(code)
        if v:
            taxos[code] = v
            print(f"  ✓ {code}: {v['n_values']} values")
        else:
            taxos[code] = None
            print(f"  ✗ {code}: NOT FOUND in {TAXO_DIR}")

    # Save
    out_path = OUT_DIR / ("manifest_pilot.json" if target else "manifest.json")
    output = {
        "version": "0.1.0",
        "generated_at": "26-04-2026",
        "rule_refs": ["R-045", "R-046", "R-047", "R-048", "WF-014"],
        "databases": manifest,
        "taxonomies": taxos,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nManifest saved to {out_path}")
    return output


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    main(target)
