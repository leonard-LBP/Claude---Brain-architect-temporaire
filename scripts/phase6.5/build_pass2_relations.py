"""
Passe 2.1 — Génération des DDL relations bidirectionnelles + SHOW final.

Stratégie option (a) : pour chaque paire (A, B) reliée par une relation bidir,
le PORTEUR (créateur de la relation côté DDL) = celui dont le nom canonique
est alphabétiquement plus petit. Notion crée automatiquement la prop miroir
côté l'autre BDD.

Pour chaque BDD, génère :
- DDL ADD COLUMN pour les relations dont elle est porteur uniquement (peut être vide)
- SHOW final qui interleave jumelles + relations (acolées) selon R-047 v2.2
  + queue + sources

Les rollups arrivent en Passe 3 séparée (queue de schéma).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
MANIFEST = json.load(open(ROOT / "manifest.json", encoding="utf-8"))
REGISTRY = json.load(open(ROOT / "bdd_registry.json", encoding="utf-8"))


def is_carrier(db_name, target_db):
    """Option (a) — porteur = nom alphabétiquement plus petit."""
    return db_name < target_db


def syn_id(name):
    """ID synced stable depuis le nom."""
    return "syn_" + str(abs(hash(name)) % 10**10)


def sanitize_for_ddl(s):
    """Remplace les apostrophes droites par des typographiques pour éviter les
    échecs du parser DDL Notion (qui utilise ' comme délimiteur de string)."""
    return s.replace("'", "’")


def build_pass2_for_db(db_name):
    """Génère les DDL relations + le SHOW final pour une BDD."""
    db = MANIFEST["databases"].get(db_name)
    if not db:
        return None

    # Get the existing show from Passe 1 (natives + jumelles + queue + sources)
    # → on doit reconstruire le SHOW avec les relations interleaved aux jumelles

    natives = db["properties"]["natives"]
    text_twins = db["properties"]["text_twins"]
    relations_bidir = [r for r in db["properties"]["relations"] if r.get("bidirectional")]

    # 1. DDL ADD COLUMN relations
    ddl_statements = []
    own_ds = REGISTRY["databases"][db_name]["data_source_id"]
    self_rels_seen = set()  # pour self-relations, on ne crée qu'une fois la paire
    for rel in relations_bidir:
        target_db = rel.get("target_db")
        if not target_db or target_db not in REGISTRY["databases"]:
            continue
        target_ds = REGISTRY["databases"][target_db]["data_source_id"]
        mirror_name = rel.get("mirror_property")
        if not mirror_name:
            continue

        # Cas self-relation : créer les 2 colonnes ensemble (ex. comprend / est sous-processus de)
        if target_db == db_name:
            pair_key = tuple(sorted([rel["name"], mirror_name]))
            if pair_key in self_rels_seen:
                continue  # déjà créé via la passe précédente sur l'autre côté
            self_rels_seen.add(pair_key)
            # Choisir l'ordre : nom alphabétiquement plus petit = côté A, l'autre = côté B
            name_a, name_b = pair_key  # déjà triés
            syn_a = syn_id(name_a)
            syn_b = syn_id(name_b)
            # Add both columns at once with cross-references
            ddl_statements.append(
                f'ADD COLUMN "{name_a}" RELATION(\'{own_ds}\', DUAL \'{sanitize_for_ddl(name_b)}\' \'{syn_b}\')'
            )
            ddl_statements.append(
                f'ADD COLUMN "{name_b}" RELATION(\'{own_ds}\', DUAL \'{sanitize_for_ddl(name_a)}\' \'{syn_a}\')'
            )
            continue

        # Cas relation A↔B normale : porteur = nom alphabétiquement plus petit
        if not is_carrier(db_name, target_db):
            continue  # not the carrier, skip
        # Use double quotes for col name, single for option strings
        synced = syn_id(rel["name"] + "_" + db_name)
        ddl = f'ADD COLUMN "{rel["name"]}" RELATION(\'{target_ds}\', DUAL \'{sanitize_for_ddl(mirror_name)}\' \'{synced}\')'
        ddl_statements.append(ddl)

    # 2. Build SHOW with interleaved jumelle + relation
    # Replicate Passe 1 ordering for blocks 1, 2a, 2b, 3, 4
    # then for block 2c, interleave: jumelle texte → relation (with same target_db)

    # Re-derive blocks from natives (sorted)
    HEAD_ORDER = ["Nom", "Statut de l'objet", "Aliases", "Erreurs de transcription", "Description"]
    TAIL_ORDER = [
        "Lien vers la note avancée",
        "Exemples concrets", "Commentaires libres", "Notes du consultant",
        "Confidentialité (option)", "Confidentialité",
        "Indices observés", "Indices d'existence de l'objet",
        "Created Date", "Last Updated Date",
        "Logs / Révisions LBP", "Merge Notes", "Merge Flags",
    ]

    def norm(s):
        return s.replace("’", "'").replace("'", "")

    # Bloc 1 ordered
    bloc1 = []
    for target in HEAD_ORDER:
        for p in natives:
            if p["category"] == "title": continue
            if p["category"] == "formula": continue
            if p["name"] == "Nom": continue
            if norm(p["name"]) == norm(target):
                bloc1.append(p["name"])
                break
    # Add Nom in front
    bloc1 = ["Nom"] + bloc1

    # Bloc 2a (4.2) — order from manifest
    bloc2a = [p["name"] for p in natives if p["section"] == "4.2" and p["category"] not in ("title", "formula") and p["name"] != "Nom" and p["name"] not in HEAD_ORDER]

    # Bloc 2b (4.4 + 4.5 non-formula natives)
    bloc2b = []
    for p in natives:
        if p["section"] in ("4.4", "4.5") and p["category"] not in ("title", "formula") and p["name"] not in HEAD_ORDER:
            bloc2b.append(p["name"])

    # Bloc 2c — INTERLEAVED jumelle + relation
    # For each text_twin, add it then its matching relation (if any)
    bloc2c = []
    rel_by_basename = {r["name"]: r for r in relations_bidir}
    for t in text_twins:
        twin_name = t["name"]
        bloc2c.append(twin_name)
        if twin_name.endswith(" (texte)"):
            base = twin_name[:-len(" (texte)")]
            if base in rel_by_basename:
                bloc2c.append(base)  # the relation has the same name as the base

    # Bloc 3 (queue) ordered
    bloc3 = []
    natives_names = {p["name"] for p in natives if p["category"] not in ("title", "formula")}
    for target in TAIL_ORDER:
        for p in natives:
            if p["category"] in ("title", "formula"): continue
            if norm(p["name"]) == norm(target):
                bloc3.append(p["name"])
                break

    # Bloc 4 (Sources texte uniquement, mono différée)
    bloc4 = []
    for p in natives:
        if p["category"] in ("title", "formula"): continue
        if p["name"].startswith("Source(s) d") and "(texte)" in p["name"]:
            bloc4.append(p["name"])

    # Final SHOW order
    show_props = bloc1 + bloc2a + bloc2b + bloc2c + bloc3 + bloc4
    # Dedup (keep first occurrence)
    seen = set()
    show_props_unique = []
    for n in show_props:
        if n not in seen:
            seen.add(n)
            show_props_unique.append(n)

    # Build SHOW directive
    quoted = [f'"{n}"' for n in show_props_unique]
    show = "SHOW " + ", ".join(quoted)

    return {
        "data_source_id": REGISTRY["databases"][db_name]["data_source_id"],
        "view_id": REGISTRY["databases"][db_name].get("view_id"),
        "n_relations_to_create": len(ddl_statements),
        "ddl": ";\n".join(ddl_statements) if ddl_statements else "",
        "show": show,
    }


def main():
    out = {}
    total_rels = 0
    for db_name in REGISTRY["databases"]:
        result = build_pass2_for_db(db_name)
        if result:
            out[db_name] = result
            total_rels += result["n_relations_to_create"]
    out_path = ROOT / "phase2_pass1_relations.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Passe 2.1 généré : {len(out)} BDD, {total_rels} relations bidir au total (porteur alphabétique).")
    print(f"Output : {out_path}")
    # Stats
    print(f"\n=== Répartition des relations à créer (porteur alphabétique) ===")
    for name in sorted(out, key=lambda x: -out[x]["n_relations_to_create"])[:15]:
        n = out[name]["n_relations_to_create"]
        if n > 0:
            print(f"  {name:45s} : {n}")
    return out


if __name__ == "__main__":
    main()
