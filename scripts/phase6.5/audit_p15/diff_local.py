"""Diff local Unicode-insensible entre manuels parsés et schémas Notion."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_p15")
MANUALS = json.load(open(ROOT / "manuals_props.json", encoding="utf-8"))
SCHEMAS = json.load(open(ROOT / "notion_schemas.json", encoding="utf-8"))


def norm(s):
    """Normalise apostrophes pour comparaison Unicode-insensible."""
    if s is None:
        return ""
    return s.replace("’", "'").strip()


# Types à exclure (gérés en passes séparées)
EXCLUDED_TYPES = {"RELATION", "ROLLUP", "FORMULA"}

# Props nommées à exclure (différées en Phase finale)
EXCLUDED_NAMES_NORM = {
    norm("Source(s) d'information"),  # la relation, pas la jumelle texte
    norm("Created Date"),  # natif Notion
    norm("Last Updated Date"),  # natif Notion
    norm("Lien vers la note avancée"),  # conditionnel R-050 (géré séparément)
    norm("Confidentialité"),  # historiquement gérée comme option (cf. R-049+)
    norm("Confidentialité (option)"),
}

# Types raw à exclure (formules différées)
EXCLUDED_RAW_TYPES_KEYWORDS = ["Formule", "Rollup", "Agrégation", "Relation"]


def is_excluded(prop):
    n = norm(prop["name"])
    if n in EXCLUDED_NAMES_NORM:
        return True
    raw = prop.get("raw_type", "") or ""
    for kw in EXCLUDED_RAW_TYPES_KEYWORDS:
        if kw in raw:
            return True
    if prop.get("type", "") in EXCLUDED_TYPES:
        return True
    # Jumelles texte — on garde celles finissant par (texte)
    return False


def diff_db(db_name, has_advanced_note=True):
    if db_name not in SCHEMAS:
        return None  # not yet fetched
    notion_props = set(norm(p) for p in SCHEMAS[db_name])
    manuel_props = MANUALS[db_name]["props"]
    missing = []
    for p in manuel_props:
        if is_excluded(p):
            continue
        if not has_advanced_note and norm(p["name"]) == norm("Lien vers la note avancée"):
            continue
        if norm(p["name"]) not in notion_props:
            missing.append(p)
    return missing


def main():
    print("=== Diff local Unicode-insensible (12 BDDs auditées) ===\n")
    total_missing = 0
    out = {}
    for db_name in MANUALS:
        info = MANUALS[db_name]
        has_an = info.get("has_advanced_note", True)
        missing = diff_db(db_name, has_an)
        if missing is None:
            continue  # pas encore fetched
        if missing:
            out[db_name] = missing
            total_missing += len(missing)
            print(f"📋 {db_name} ({len(missing)} manques)")
            for p in missing:
                print(f"  - {p['name']:50s} [{p.get('raw_type','?'):30s}] taxos={p.get('taxonomies',[])} sec={p.get('section')}")
        else:
            print(f"✅ {db_name} : aucun manque")
        print()
    print(f"\n=== TOTAL : {total_missing} props manquantes sur {len([d for d in MANUALS if d in SCHEMAS])} BDDs auditées ===")
    json.dump(out, open(ROOT / "missing_props_real.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Output : {ROOT}/missing_props_real.json")


if __name__ == "__main__":
    main()
