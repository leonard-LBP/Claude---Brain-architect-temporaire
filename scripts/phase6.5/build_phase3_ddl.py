"""
Passe 1 — Builder DDL R-047 v2 pour générer le schéma complet d'une BDD Twin.

Génère, pour une BDD donnée du manifest, les statements DDL R-047 v2 :
  - Bloc 1 (tête) : Nom (skip, déjà créé) · Statut · Aliases · Erreurs · Description
  - Bloc 2a Spécifiques (4.2)
  - Bloc 2b 5D regroupée (4.4)
  - Bloc 2c Paires jumelles+relations (4.3) — adjacentes (jumelle, puis relation)
  - Bloc 2d Calculés natifs (différés selon décision Leonard)
  - Bloc 3 Queue gestion (ordre fixe)
  - Bloc 4 Sources : Source(s) d'info (texte) + Source(s) d'info (relation mono)

Exclut :
  - Bloc 5 (rollups) — créés en Passe 2 globale
  - Formules natives (différées Leonard) — créées en Passe finale
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
MANIFEST = json.load(open(ROOT / "manifest.json", encoding="utf-8"))
REGISTRY = json.load(open(ROOT / "bdd_registry.json", encoding="utf-8"))


def get_taxo_options(taxo_code, niveau=None):
    """Retourne une liste de tuples (libellé_notion, couleur) pour la taxo,
    filtrée par 'Type de nœud' si niveau spécifié (taxon|category)."""
    t = MANIFEST["taxonomies"].get(taxo_code)
    if not t:
        return []
    rows = t.get("rows") or []
    options = []
    for r in rows:
        if niveau:
            type_node = r.get("Type de nœud", "").strip().lower()
            if type_node != niveau.lower():
                continue
        label = r.get("Libellé Notion (recommandé)", "").strip() or r.get("Libellé (canonique)", "").strip()
        color = r.get("Couleur Notion", "").strip().lower() or "default"
        # Notion DDL valid colors
        valid = {"default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red"}
        if color not in valid:
            color = "default"
        if label:
            options.append((label, color))
    return options


def escape_label(s):
    """Escape pour les single-quoted options du DDL."""
    return s.replace("'", "\\'")


def build_select_ddl(taxo_code, niveau=None, multi=False):
    options = get_taxo_options(taxo_code, niveau)
    if not options:
        return None
    parts = [f"'{escape_label(lbl)}':{color}" for lbl, color in options]
    keyword = "MULTI_SELECT" if multi else "SELECT"
    return f"{keyword}({', '.join(parts)})"


def is_taxon_level_5d(prop):
    """Heuristique : si la prop fait référence aux 'sous-dimensions' → niveau taxon (10),
    si elle fait référence aux 'dimensions' (sans 'sous-') → niveau category (5)."""
    name = prop["name"].lower()
    if "sous-dimension" in name or "sous-dim" in name:
        return "taxon"
    if "dimension" in name:
        return "category"
    # Fallback : taxo_niveau du manifest si présent
    return prop.get("taxo_niveau") or "taxon"


def build_property_ddl(prop):
    """Construit la portion de DDL pour une propriété native.
    Retourne (col_name, ddl_type) ou None si à différer."""
    name = prop["name"]
    cat = prop["category"]

    if cat == "title":
        return None  # déjà créé en Phase 2
    if cat == "formula":
        return None  # différé
    # 'Nom' est créé comme TITLE en Phase 2, peu importe sa classification
    # texte_short dans le manuel parent. Exclure ici pour éviter doublon.
    if name.strip() == "Nom":
        return None

    if cat == "select":
        # Cas Statut, Type d'actif, Mode provenance, Cycle de vie, Substituabilité, Criticité
        if prop["taxo_codes"]:
            taxo = prop["taxo_codes"][0]  # une seule taxo généralement
            ddl = build_select_ddl(taxo, niveau=None, multi=False)
            if ddl:
                return name, ddl
        return name, "SELECT()"  # fallback (vide)

    if cat == "multi_select":
        if prop["taxo_codes"]:
            taxo = prop["taxo_codes"][0]
            niveau = None
            if taxo == "ORG5D.DIM.LBP":
                niveau = is_taxon_level_5d(prop)
            ddl = build_select_ddl(taxo, niveau=niveau, multi=True)
            if ddl:
                return name, ddl
        return name, "MULTI_SELECT()"

    if cat == "date":
        # Created Date / Last Updated Date → natives Notion renommées (R-047)
        if "created" in name.lower():
            return name, "CREATED_TIME"
        if "last updated" in name.lower() or "last edited" in name.lower():
            return name, "LAST_EDITED_TIME"
        return name, "DATE"

    if cat == "number":
        return name, "NUMBER"

    if cat == "url":
        return name, "URL"

    if cat in ("text_short", "text_long", "text_twin"):
        return name, "RICH_TEXT"

    return None


def normalize_apo(s):
    return s.replace("’", "'").replace("'", "")


def build_for_db(db_canonical_name):
    """Construit l'ensemble de statements DDL ordonnés selon R-047 v2.
    Inclut les paires jumelles+relations couplées (Bloc 2c)."""
    db = MANIFEST["databases"].get(db_canonical_name)
    if not db:
        raise ValueError(f"BDD inconnue : {db_canonical_name}")

    natives = db["properties"]["natives"]
    text_twins = db["properties"]["text_twins"]
    relations = db["properties"]["relations"]

    # Group by R-047 v2 block
    bloc1, bloc2a_spec, bloc2b_5d, bloc3, bloc4_text = [], [], [], [], []
    bloc4_relation_mono = []  # Source(s) d'information relation

    # Sort natives into blocks
    for p in natives:
        if p["category"] == "title":
            continue
        if p["category"] == "formula":
            continue  # différé Passe finale
        ddl_pair = build_property_ddl(p)
        if not ddl_pair:
            continue
        sec = p["section"]
        if p["block"] == 1:
            bloc1.append((p, ddl_pair))
        elif p["block"] == 3:
            bloc3.append((p, ddl_pair))
        elif p["block"] == 4:
            bloc4_text.append((p, ddl_pair))
        else:  # block 2
            if sec == "4.2":
                bloc2a_spec.append((p, ddl_pair))
            elif sec in ("4.4", "4.5"):
                bloc2b_5d.append((p, ddl_pair))
            else:
                bloc2a_spec.append((p, ddl_pair))  # fallback

    # Bloc 2c : R-047 v2.2 — jumelles textes SEULES (sans les relations)
    # Les relations bidir sont créées en Passe 2 globale (après Passe 1 sur les 28 BDD)
    # pour éviter les miroirs prématurés (cf. WF-014 v3 et R-047 v2.2).
    bloc2c_twins_only = []
    for t in text_twins:
        twin_ddl = build_property_ddl(t)
        if twin_ddl:
            bloc2c_twins_only.append((t, twin_ddl))

    # Bloc 4 relation mono (Sources d'informations) :
    # DIFFÉRÉ — la BDD Sources d'informations sera créée plus tard.
    pass

    # R-047 v2 explicit order for Bloc 1 (Statut avant Aliases)
    HEAD_ORDER = ["Nom", "Statut de l'objet", "Aliases", "Erreurs de transcription", "Description"]
    bloc1_sorted = []
    for target in HEAD_ORDER:
        target_norm = normalize_apo(target)
        for p, dd in bloc1:
            n_norm = normalize_apo(p["name"])
            if n_norm == target_norm:
                bloc1_sorted.append((p, dd))
                break
    seen = {p["name"] for p, _ in bloc1_sorted}
    for p, dd in bloc1:
        if p["name"] not in seen:
            bloc1_sorted.append((p, dd))

    # R-047 v2.1 explicit order for Bloc 3 (queue) — Lien vers la note avancée en tête
    TAIL_ORDER = [
        "Lien vers la note avancée",  # R-050, R-047 v2.1 (conditionnel)
        "Exemples concrets", "Commentaires libres", "Notes du consultant",
        "Confidentialité (option)", "Confidentialité",
        "Indices observés", "Indices d'existence de l'objet",
        "Created Date", "Last Updated Date",
        "Logs / Révisions LBP", "Merge Notes", "Merge Flags",
    ]
    bloc3_sorted = []
    for target in TAIL_ORDER:
        target_norm = normalize_apo(target)
        for p, dd in bloc3:
            n_norm = normalize_apo(p["name"])
            if n_norm == target_norm:
                bloc3_sorted.append((p, dd))
                break
    seen = {p["name"] for p, _ in bloc3_sorted}
    for p, dd in bloc3:
        if p["name"] not in seen:
            bloc3_sorted.append((p, dd))

    # Final ordered list R-047 v2.2 — Passe 1 (natives + jumelles, pas de relations)
    ordered = (
        bloc1_sorted          # 1
        + bloc2a_spec         # 2a
        + bloc2b_5d           # 2b
        + bloc2c_twins_only   # 2c (jumelles textes seules)
        + bloc3_sorted        # 3
        + bloc4_text          # 4 — Sources texte
    )
    # Bloc 5 (relations bidir) → Passe 2 globale
    # Bloc 6 (rollups) → Passe 3 globale
    # Sources mono (relation) → Passe finale après création BDD Sources d'infos

    return ordered


def build_show_directive(ordered):
    """Construit la directive SHOW pour update_view (ordering UI R-051).
    Place 'Nom' en tête puis l'ordre des props natives R-047 v2.2."""
    names = ["Nom"] + [p["name"] for p, _ in ordered]
    # Échapper les apostrophes pour la DSL
    quoted = [f'"{n}"' for n in names]
    return "SHOW " + ", ".join(quoted)


def to_ddl(ordered):
    """Convert ordered list of (prop, (col_name, ddl_type)) to ADD COLUMN statements."""
    statements = []
    for p, (name, ddl_type) in ordered:
        statements.append(f'ADD COLUMN "{name}" {ddl_type}')
    return statements


def stats(ordered):
    by_block = {}
    by_cat = {}
    for p, _ in ordered:
        by_block[p["block"]] = by_block.get(p["block"], 0) + 1
        by_cat[p["category"]] = by_cat.get(p["category"], 0) + 1
    return by_block, by_cat


def generate_all():
    """Generate Passe 1 DDL + SHOW directive for all 28 BDD as a JSON output."""
    out = {}
    for db_name in REGISTRY["databases"]:
        try:
            ordered = build_for_db(db_name)
            statements = to_ddl(ordered)
            show = build_show_directive(ordered)
            out[db_name] = {
                "data_source_id": REGISTRY["databases"][db_name]["data_source_id"],
                "n_props": len(statements),
                "ddl": ";\n".join(statements),
                "show": show,
            }
        except Exception as e:
            print(f"  ✗ ERROR on {db_name}: {e}")
    out_path = ROOT / "phase1_passe1_all.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Generated DDL + SHOW for {len(out)} BDD → {out_path}")
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        generate_all()
    else:
        target = sys.argv[1] if len(sys.argv) > 1 else "Actifs"
        ordered = build_for_db(target)
        statements = to_ddl(ordered)
        show = build_show_directive(ordered)
        by_block, by_cat = stats(ordered)
        print(f"=== {target} ===")
        print(f"Total props à ajouter : {len(statements)}")
        print(f"Par bloc : {by_block}")
        print(f"Par catégorie : {by_cat}")
        print()
        print("=== STATEMENTS ===")
        for i, s in enumerate(statements, 1):
            if len(s) > 200:
                print(f"  {i:2d}. {s[:120]}... [{len(s)} chars]")
            else:
                print(f"  {i:2d}. {s}")
        print(f"\n=== SHOW directive ===")
        print(show[:500] + ("..." if len(show) > 500 else ""))

        out = ROOT / f"phase1_ddl_{target.replace(' ', '_')}.sql"
        with open(out, "w", encoding="utf-8") as f:
            f.write(";\n".join(statements) + ";")
        print(f"\nDDL sauvegardé : {out}")
