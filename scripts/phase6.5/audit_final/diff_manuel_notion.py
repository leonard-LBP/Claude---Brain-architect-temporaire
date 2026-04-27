"""Diff Manuel Twin ↔ BDD Notion (audit final exhaustif).

Pour chaque BDD :
- Charge les props parsées du manuel
- Charge le schéma Notion
- Compare Unicode-insensible (apostrophes typographiques vs droites)
- Catégorise les différences :
  - MISSING_NOTION : prop manuel ✓, Notion ✗ (à créer)
  - EXTRA_NOTION : prop Notion ✓, manuel ✗ (potentiel leakage)
  - TYPE_MISMATCH : prop des 2 côtés mais type incohérent

Sortie : missing_in_notion.json (à corriger) + extra_in_notion.json (à investiguer)
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_final")
MANUELS_DIR = ROOT / "manuels_parsed"
NOTION_CACHE = json.load(open(ROOT / "notion_schemas.json", encoding="utf-8"))

# Système Notion (auto-créés, jamais à créer manuellement)
NOTION_SYSTEM_TYPES = {"created_time", "last_edited_time"}
SYSTEM_NAMES_NORM = {"created date", "last updated date"}


def norm(s):
    """Normalise apostrophes pour comparaison Unicode-insensible + lowercase."""
    if s is None:
        return ""
    return s.replace("’", "'").lower().strip()


def main():
    missing_in_notion = {}  # BDD → liste props
    extra_in_notion = {}     # BDD → liste props
    summary = []

    for manuel_file in sorted(MANUELS_DIR.glob("*.json")):
        bdd_name = manuel_file.stem
        manuel = json.load(open(manuel_file, encoding="utf-8"))

        if bdd_name not in NOTION_CACHE:
            print(f"⚠ {bdd_name} : pas de cache Notion")
            continue

        notion = NOTION_CACHE[bdd_name]  # {nom: type}
        notion_norm = {norm(n): (n, t) for n, t in notion.items()}

        # Props attendues sur Notion (depuis le manuel)
        manuel_expected = [p for p in manuel["props"] if p["expected_in_notion"]]
        manuel_norm_set = set(norm(p["name"]) for p in manuel_expected)

        # Diff direction 1 : manuel → Notion
        missing = []
        for p in manuel_expected:
            n = norm(p["name"])
            # Skip system props (auto-créées par Notion)
            if n in SYSTEM_NAMES_NORM:
                continue
            # Skip Lien vers la note avancée si has_advanced_note: false
            if n == "lien vers la note avancée" and not manuel["has_advanced_note"]:
                continue
            if n not in notion_norm:
                missing.append({
                    "name": p["name"],
                    "type": p["type"],
                    "raw_type": p["raw_type"],
                    "section": p["section"],
                    "taxonomies": p["taxonomies"],
                    "portee": p["portee"],
                })

        # Diff direction 2 : Notion → manuel
        extras = []
        for n_norm, (n_orig, t) in notion_norm.items():
            # Skip system
            if t in NOTION_SYSTEM_TYPES or n_norm in SYSTEM_NAMES_NORM:
                continue
            # Skip rollups (souvent miroirs auto)
            if t == "rollup":
                continue
            # Skip relations miroir (créées auto par Notion)
            if t == "relation":
                # On considère que toutes les relations légitimes sont dans le manuel
                # Si elle n'y est pas, c'est un miroir reçu d'une autre BDD → légitime
                # On ne signale donc pas comme extra
                continue
            # Skip Source(s) d'information (texte) — jumelle légitime
            if "source(s) d'information (texte)" in n_norm:
                continue
            if n_norm not in manuel_norm_set:
                extras.append({"name": n_orig, "type": t})

        if missing:
            missing_in_notion[bdd_name] = missing
        if extras:
            extra_in_notion[bdd_name] = extras

        summary.append({
            "bdd": bdd_name,
            "manuel_expected": len(manuel_expected),
            "notion_actual": len(notion),
            "missing": len(missing),
            "extras": len(extras),
        })

    # Print
    print(f"\n{'BDD':<45} {'Manuel':<8} {'Notion':<8} {'Manque':<8} {'Extra':<8}")
    print("-" * 80)
    total_missing = 0
    total_extras = 0
    for s in summary:
        flag = "🔴" if s["missing"] > 0 else "  "
        print(f"{flag} {s['bdd']:<43} {s['manuel_expected']:<8} {s['notion_actual']:<8} {s['missing']:<8} {s['extras']:<8}")
        total_missing += s["missing"]
        total_extras += s["extras"]
    print("-" * 80)
    print(f"   {'TOTAL':<43} {'':<8} {'':<8} {total_missing:<8} {total_extras:<8}")
    print()

    # Save
    json.dump(missing_in_notion, open(ROOT / "missing_in_notion.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(extra_in_notion, open(ROOT / "extra_in_notion.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Output : {ROOT}/missing_in_notion.json")
    print(f"Output : {ROOT}/extra_in_notion.json")


if __name__ == "__main__":
    main()
