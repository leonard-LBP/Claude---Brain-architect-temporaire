"""
Passe 2.2 — Génération des DDL rollups + SHOW final v3.

Pour chaque BDD ayant des rollups :
- Parse robuste du `type_raw` (Rollup (relation_porteuse → propriété_cible))
  avec gestion des parenthèses imbriquées (target_property tronqué dans le manifest).
- DDL ADD COLUMN "Nom" ROLLUP('rel_prop', 'target_prop', 'show_unique')
- SHOW final v3 = SHOW Passe 2.1 + rollups appendus en queue (Bloc 6 R-047 v2.2).

Output : phase2_pass2_rollups.json
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
MANIFEST = json.load(open(ROOT / "manifest.json", encoding="utf-8"))
REGISTRY = json.load(open(ROOT / "bdd_registry.json", encoding="utf-8"))
PASS2_1 = json.load(open(ROOT / "phase2_pass1_relations.json", encoding="utf-8"))


def sanitize(s):
    """Apostrophe droite → typographique pour le DDL Notion."""
    return s.replace("'", "’")


def clean_rel_name(s):
    """Nettoie une source_relation extraite du manuel : retire préfixe
    'relation : ' et les backticks `…`."""
    s = s.strip()
    # Strip "relation : " prefix
    if s.lower().startswith("relation :"):
        s = s.split(":", 1)[1].strip()
    # Strip surrounding backticks
    s = s.strip("`").strip()
    return s


def clean_target_prop(s):
    """Nettoie le target_property : certains manuels utilisent le format
    'propriété source : `X` ; BDD source : `Y`' au lieu de juste `X`."""
    s = s.strip()
    # Detect the verbose format
    m = re.match(r"propriété(?:\s+source)?\s*:\s*`([^`]+)`", s)
    if m:
        return m.group(1).strip()
    # Strip surrounding backticks
    s = s.strip("`").strip()
    # Add closing paren if unbalanced (extract regex truncation)
    if s.count("(") > s.count(")"):
        s = s + ")" * (s.count("(") - s.count(")"))
    return s


def parse_rollup_type_raw(type_raw):
    """Parse robuste de 'Rollup (rel → target)' avec parens imbriquées.
    Retourne (rel_prop, target_prop) ou None si parse échoue.

    Cas non supportés (multi-source, indirect via BDD intermédiaire) :
    retournent None — à traiter en formule en Passe finale.
    """
    s = type_raw.strip()
    # Skip non-supportés
    if "multi-source" in s.lower():
        return None
    if "indirect" in s.lower() or "BDD intermédiaire" in s:
        return None
    # Strip prefix
    for prefix in ("Rollup ", "Agrégation / rollup ", "Agrégation rollup ", "Agrégation "):
        if s.startswith(prefix):
            s = s[len(prefix):]
            break
    # Now should start with '(' and end with ')'
    if not (s.startswith("(") and s.endswith(")")):
        return None
    inner = s[1:-1]
    # Split on ' → '
    if " → " not in inner:
        return None
    rel, target = inner.split(" → ", 1)
    return clean_rel_name(rel), clean_target_prop(target)


def map_function(forme_logique):
    """Toutes les formes 'Liste dédoublonnée de ...' → show_unique.
    À étendre si d'autres formes apparaissent."""
    f = forme_logique.lower()
    if "liste" in f or "valeur taxonomique" in f or "consolidée" in f:
        return "show_unique"
    # default
    return "show_unique"


def build_pass3_for_db(db_name):
    db = MANIFEST["databases"].get(db_name)
    if not db:
        return None
    rollups = db["properties"].get("rollups", [])
    if not rollups:
        return None

    pass2_1 = PASS2_1.get(db_name, {})
    natives = db["properties"]["natives"]
    relations_bidir = [r for r in db["properties"]["relations"] if r.get("bidirectional")]
    rel_names = {r["name"] for r in relations_bidir}

    ddl_statements = []
    rollup_names = []
    warnings = []

    for r in rollups:
        name = r["name"]
        type_raw = r.get("type_raw", "")
        parsed = parse_rollup_type_raw(type_raw)
        if not parsed:
            warnings.append(f"  ⚠ Parse failed for '{name}' (type_raw='{type_raw}')")
            continue
        rel_prop, target_prop = parsed
        # Validate rel_prop exists in this BDD as a bidir relation
        if rel_prop not in rel_names:
            # Try fuzzy match : maybe relation has slightly different name
            cand = [r for r in rel_names if rel_prop.lower() in r.lower() or r.lower() in rel_prop.lower()]
            if len(cand) == 1:
                rel_prop = cand[0]
            else:
                warnings.append(f"  ⚠ Relation '{rel_prop}' not found in BDD '{db_name}' for rollup '{name}' (cands={cand})")
                continue
        func = map_function(r.get("forme_logique", ""))
        ddl = (f'ADD COLUMN "{name}" '
               f"ROLLUP('{sanitize(rel_prop)}', '{sanitize(target_prop)}', '{func}')")
        ddl_statements.append(ddl)
        rollup_names.append(name)

    # Build SHOW final v3 = SHOW Passe 2.1 + rollups appended
    base_show = pass2_1.get("show", "")
    if base_show.startswith("SHOW "):
        base_props_str = base_show[len("SHOW "):]
        # parse: comma-separated quoted props
        base_props = re.findall(r'"([^"]+)"', base_props_str)
    else:
        base_props = []
    # Append rollups (avoid duplicates)
    seen = set(base_props)
    final_props = list(base_props)
    for n in rollup_names:
        if n not in seen:
            final_props.append(n)
            seen.add(n)

    quoted = [f'"{n}"' for n in final_props]
    show = "SHOW " + ", ".join(quoted)

    return {
        "data_source_id": REGISTRY["databases"][db_name]["data_source_id"],
        "view_id": REGISTRY["databases"][db_name].get("view_id"),
        "n_rollups_to_create": len(ddl_statements),
        "n_rollups_skipped": len(rollups) - len(ddl_statements),
        "ddl": ";\n".join(ddl_statements) if ddl_statements else "",
        "show": show,
        "warnings": warnings,
    }


def main():
    out = {}
    total_rolls = 0
    total_skipped = 0
    all_warnings = []
    for db_name in REGISTRY["databases"]:
        result = build_pass3_for_db(db_name)
        if result:
            out[db_name] = result
            total_rolls += result["n_rollups_to_create"]
            total_skipped += result["n_rollups_skipped"]
            if result["warnings"]:
                all_warnings.extend([f"[{db_name}]"] + result["warnings"])
    out_path = ROOT / "phase2_pass2_rollups.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Passe 2.2 généré : {len(out)} BDD avec rollups, {total_rolls} rollups à créer, {total_skipped} skipped.")
    print(f"Output : {out_path}")
    print(f"\n=== Top BDD par nb rollups ===")
    for name in sorted(out, key=lambda x: -out[x]["n_rollups_to_create"])[:10]:
        n = out[name]["n_rollups_to_create"]
        sk = out[name]["n_rollups_skipped"]
        print(f"  {name:45s} : {n} créés, {sk} skipped")
    if all_warnings:
        print(f"\n=== ⚠ {len([w for w in all_warnings if not w.startswith('[')])} warnings ===")
        for w in all_warnings:
            print(w)
    return out


if __name__ == "__main__":
    main()
