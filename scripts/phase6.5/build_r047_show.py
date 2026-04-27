"""
Construit le SHOW R-047 v2.2 pour chaque BDD Twin Notion.

Sources:
  - bdd_registry.json -> view_id par BDD
  - audit_final/notion_schemas.json -> props live + types Notion (post-audit)
  - audit_final/manuels_parsed/<BDD>.json -> sections 4.1..4.5 par prop

Sortie: output/r047_show_statements.json
{
  "<BDD>": {
    "view_id": "...",
    "show": ["Nom", "Statut...", ...],
    "blocks": {"1": [...], "2a": [...], ...},
    "warnings": [...]
  }
}
"""

import json
import os
from pathlib import Path

ROOT = Path(r"C:\Users\leona\LBP - dev\Claude - Brain architect temporaire\scripts\phase6.5")
REGISTRY = ROOT / "output" / "bdd_registry.json"
SCHEMAS = ROOT / "audit_final" / "notion_schemas.json"
MANUELS_DIR = ROOT / "audit_final" / "manuels_parsed"
OUTPUT = ROOT / "output" / "r047_show_statements.json"

# Bloc 1 — Tête générique (ordre fixe)
BLOC1_ORDER = [
    "Nom",
    "Statut de l'objet",  # ASCII apostrophe — sera matché en typographique
    "Aliases",
    "Erreurs de transcription",
    "Description",
]

# Bloc 3 — Queue générique (ordre fixe)
BLOC3_ORDER = [
    "Lien vers la note avancée",
    "Exemples concrets",
    "Commentaires libres",
    "Notes du consultant",
    "Confidentialité (option)",
    "Confidentialité",
    "Indices observés",
    "Indices d'existence de l'objet",  # ASCII apostrophe — matché en typographique
    "Created Date",
    "Last Updated Date",
    "Logs / Révisions LBP",
    "Merge Notes",
    "Merge Flags",
]

# Bloc 4 — Sources textuelles (1 prop)
BLOC4_NAME_VARIANTS = {
    "Source(s) d'information (texte)",
    "Source(s) d’information (texte)",
}


def normalize_apos(s: str) -> str:
    """Normalise apostrophes pour matching."""
    return s.replace("’", "'").replace("ʼ", "'")


def find_actual_name(target: str, names: list[str]) -> str | None:
    """Trouve le nom exact dans la liste des props live, en gérant les apostrophes."""
    target_n = normalize_apos(target)
    for name in names:
        if normalize_apos(name) == target_n:
            return name
    return None


def is_5d_native(prop_name: str, manual_section: str | None) -> bool:
    """Détecte les props 5D natives (multi-select / select 5D + textes 5D narratifs)."""
    n = normalize_apos(prop_name)
    if "(5D)" in n:
        return True
    if manual_section == "4.4":
        return True
    return False


def is_text_jumelle(prop_name: str) -> bool:
    """Prop finissant en ' (texte)' SAUF Source(s) d'information (texte)."""
    n = normalize_apos(prop_name)
    if n in {normalize_apos(v) for v in BLOC4_NAME_VARIANTS}:
        return False
    return n.endswith(" (texte)")


def classify(prop_name: str, prop_type: str, manual_section: str | None) -> str:
    """Renvoie le bloc cible: '1', '2a', '2b', '2c', '2d', '3', '4', '5', '6'."""
    n = normalize_apos(prop_name)

    # Bloc 1 fixe
    bloc1_set = {normalize_apos(p) for p in BLOC1_ORDER}
    if n in bloc1_set:
        return "1"

    # Bloc 3 fixe
    bloc3_set = {normalize_apos(p) for p in BLOC3_ORDER}
    if n in bloc3_set:
        return "3"

    # Bloc 4
    if n in {normalize_apos(v) for v in BLOC4_NAME_VARIANTS}:
        return "4"

    # Type Notion
    if prop_type == "relation":
        return "5"
    if prop_type == "rollup":
        return "6"

    # Jumelle texte
    if is_text_jumelle(prop_name):
        return "2c"

    # 5D
    if is_5d_native(prop_name, manual_section):
        return "2b"

    # Section manuel
    if manual_section == "4.5":
        return "2d"
    if manual_section == "4.2":
        return "2a"

    # Fallback: 2a (props métier par défaut)
    return "2a"


def build_show_for_bdd(bdd_name: str, view_id: str, schema: dict, manual_props: list[dict]) -> dict:
    """Construit le SHOW ordonné pour une BDD."""
    warnings = []
    # Index manuel par nom normalisé
    manual_idx: dict[str, dict] = {}
    for p in manual_props:
        manual_idx[normalize_apos(p["name"])] = p

    live_names = list(schema.keys())

    # Classifier chaque prop live
    blocks: dict[str, list[str]] = {k: [] for k in ["1", "2a", "2b", "2c", "2d", "3", "4", "5", "6"]}
    classified: dict[str, str] = {}

    for name in live_names:
        ptype = schema[name]
        # Notion stocke type comme str
        if isinstance(ptype, dict):
            ptype = ptype.get("type", "")
        n_norm = normalize_apos(name)
        manual_p = manual_idx.get(n_norm)
        section = manual_p.get("section") if manual_p else None
        b = classify(name, ptype, section)
        blocks[b].append(name)
        classified[name] = b

    # Ordonner Bloc 1 (ordre fixe, en utilisant noms live exacts)
    bloc1_ordered = []
    for target in BLOC1_ORDER:
        actual = find_actual_name(target, blocks["1"])
        if actual:
            bloc1_ordered.append(actual)
    # Au cas où: ajout de toute prop classifiée Bloc 1 mais non trouvée dans la liste fixe
    for n in blocks["1"]:
        if n not in bloc1_ordered:
            bloc1_ordered.append(n)
            warnings.append(f"Bloc1 prop hors ordre fixe: {n}")
    blocks["1"] = bloc1_ordered

    # Ordonner Bloc 3 (ordre fixe, en utilisant noms live exacts)
    bloc3_ordered = []
    for target in BLOC3_ORDER:
        actual = find_actual_name(target, blocks["3"])
        if actual:
            bloc3_ordered.append(actual)
    for n in blocks["3"]:
        if n not in bloc3_ordered:
            bloc3_ordered.append(n)
            warnings.append(f"Bloc3 prop hors ordre fixe: {n}")
    blocks["3"] = bloc3_ordered

    # Bloc 2a/2b/2c/2d/5/6 : ordre alphabétique (stable)
    for k in ["2a", "2b", "2c", "2d", "5", "6"]:
        blocks[k] = sorted(blocks[k], key=lambda s: normalize_apos(s).lower())

    # Bloc 4 : a 0 ou 1 prop
    blocks["4"] = sorted(blocks["4"], key=lambda s: normalize_apos(s).lower())

    # Concat final
    show = (
        blocks["1"]
        + blocks["2a"]
        + blocks["2b"]
        + blocks["2c"]
        + blocks["2d"]
        + blocks["3"]
        + blocks["4"]
        + blocks["5"]
        + blocks["6"]
    )

    return {
        "view_id": view_id,
        "show": show,
        "blocks": blocks,
        "stats": {
            "total_live": len(live_names),
            "total_show": len(show),
            "bloc1": len(blocks["1"]),
            "bloc2a": len(blocks["2a"]),
            "bloc2b": len(blocks["2b"]),
            "bloc2c": len(blocks["2c"]),
            "bloc2d": len(blocks["2d"]),
            "bloc3": len(blocks["3"]),
            "bloc4": len(blocks["4"]),
            "bloc5": len(blocks["5"]),
            "bloc6": len(blocks["6"]),
        },
        "warnings": warnings,
    }


def main():
    registry = json.load(open(REGISTRY, encoding="utf-8"))
    schemas = json.load(open(SCHEMAS, encoding="utf-8"))

    result = {}
    for bdd_name, info in registry["databases"].items():
        view_id = info["view_id"]
        if bdd_name not in schemas:
            print(f"[WARN] {bdd_name} absent du cache notion_schemas.json")
            continue
        schema = schemas[bdd_name]

        manual_path = MANUELS_DIR / f"{bdd_name}.json"
        if manual_path.exists():
            manual = json.load(open(manual_path, encoding="utf-8"))
            manual_props = manual.get("props", [])
        else:
            manual_props = []
            print(f"[WARN] {bdd_name}: manuel parsé absent ({manual_path.name})")

        out = build_show_for_bdd(bdd_name, view_id, schema, manual_props)
        result[bdd_name] = out
        print(f"[OK] {bdd_name}: {out['stats']['total_show']} props SHOW (b1={out['stats']['bloc1']} 2a={out['stats']['bloc2a']} 2b={out['stats']['bloc2b']} 2c={out['stats']['bloc2c']} 2d={out['stats']['bloc2d']} 3={out['stats']['bloc3']} 4={out['stats']['bloc4']} 5={out['stats']['bloc5']} 6={out['stats']['bloc6']})")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(result, open(OUTPUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\n=> {OUTPUT}")


if __name__ == "__main__":
    main()
