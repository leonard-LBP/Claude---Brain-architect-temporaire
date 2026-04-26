"""
Phase 1d — Validation interne du manifest.

Vérifie :
1. Toute relation bidirectionnelle a sa symétrique côté cible (avec mirror_property concordant)
2. Tout rollup référence une relation source qui existe dans la BDD courante
3. Toutes les BDD cibles référencées par des relations existent dans le manifest
4. Toutes les taxos référencées sont résolues (ou explicitement notées absentes)
5. Compte par BDD : natives, relations, rollups, text_twins
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

OUT_DIR = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
MANIFEST_PATH = OUT_DIR / "manifest.json"


def main():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        m = json.load(f)
    dbs = m["databases"]
    taxos = m["taxonomies"]

    issues = []
    info = []

    # ======== 1. RELATIONS — bidirectionnelles symétriques ========
    print("=" * 60)
    print("1) Symétrie des relations bidirectionnelles")
    print("=" * 60)

    # Build index : (source_db, target_db) → list of (relation_name, mirror_name)
    forward = {}
    for db_name, db in dbs.items():
        for rel in db["properties"]["relations"]:
            if not rel.get("bidirectional"):
                continue
            target = rel.get("target_db")
            if not target:
                continue
            forward.setdefault((db_name, target), []).append((rel["name"], rel.get("mirror_property")))

    # For each forward, check that there's a reverse entry
    asymmetries = 0
    for (a, b), forward_list in forward.items():
        # B should have relations targeting A
        if b not in dbs:
            issues.append(f"  ✗ {a} → {b} : BDD cible absente du manifest")
            asymmetries += 1
            continue
        b_db = dbs[b]
        reverse_relations = [r for r in b_db["properties"]["relations"] if r.get("target_db") == a and r.get("bidirectional")]
        for rel_name, mirror_expected in forward_list:
            # Find a reverse relation with name == mirror_expected and mirror == rel_name
            match = [r for r in reverse_relations if r["name"] == mirror_expected]
            if not match:
                issues.append(f"  ✗ {a}.{rel_name} → {b} (miroir attendu '{mirror_expected}') : aucun miroir trouvé côté {b}")
                asymmetries += 1
            else:
                # Verify reciprocity
                reverse_mirror = match[0].get("mirror_property")
                if reverse_mirror != rel_name:
                    issues.append(f"  ⚠ {a}.{rel_name} ↔ {b}.{match[0]['name']} : miroir réciproque '{reverse_mirror}' ≠ '{rel_name}'")

    print(f"  Relations bidir analysées : {sum(len(v) for v in forward.values())}")
    print(f"  Asymétries : {asymmetries}")

    # ======== 2. ROLLUPS — relations sources existent ========
    print()
    print("=" * 60)
    print("2) Cohérence des rollups (relation source existante)")
    print("=" * 60)

    rollup_issues = 0
    rollup_total = 0
    for db_name, db in dbs.items():
        rel_names = {r["name"] for r in db["properties"]["relations"]}
        for ru in db["properties"]["rollups"]:
            rollup_total += 1
            src = ru.get("source_relation", "")
            if not src:
                issues.append(f"  ✗ {db_name}.{ru['name']} : pas de source_relation extraite")
                rollup_issues += 1
                continue
            # Check if the source matches any relation name
            if src not in rel_names:
                # Maybe partial match (truncation)
                matches = [r for r in rel_names if src.startswith(r) or r.startswith(src)]
                if not matches:
                    issues.append(f"  ✗ {db_name}.{ru['name']} : relation source '{src}' introuvable")
                    rollup_issues += 1
    print(f"  Rollups analysés : {rollup_total}")
    print(f"  Issues : {rollup_issues}")

    # ======== 3. BDD cibles existent ========
    print()
    print("=" * 60)
    print("3) BDD cibles existent dans le manifest")
    print("=" * 60)

    target_issues = 0
    targets_seen = set()
    for db_name, db in dbs.items():
        for rel in db["properties"]["relations"]:
            t = rel.get("target_db")
            if not t:
                continue
            targets_seen.add(t)
            if t not in dbs:
                # Sources d'informations is the only legitimate external target (R-046 monodir)
                if "Sources d" in t:
                    info.append(f"  ℹ {db_name}.{rel['name']} → {t} (relation monodirectionnelle légitime)")
                else:
                    issues.append(f"  ✗ {db_name}.{rel['name']} → {t} : BDD cible absente du manifest")
                    target_issues += 1
    print(f"  BDD cibles uniques référencées : {len(targets_seen)}")
    print(f"  BDD cibles présentes dans manifest : {len([t for t in targets_seen if t in dbs])}")
    print(f"  Issues (target absent et non-Sources) : {target_issues}")

    # ======== 4. Taxonomies résolues ========
    print()
    print("=" * 60)
    print("4) Taxonomies référencées résolues")
    print("=" * 60)

    n_taxos = len(taxos)
    n_resolved = sum(1 for v in taxos.values() if v is not None)
    n_unresolved = n_taxos - n_resolved
    print(f"  Taxos référencées : {n_taxos}")
    print(f"  Résolues : {n_resolved}")
    print(f"  Non résolues : {n_unresolved}")
    for code, v in taxos.items():
        if v is None:
            issues.append(f"  ✗ Taxonomie {code} : fichier .md absent du vault")

    # ======== 5. Volumétrie par BDD ========
    print()
    print("=" * 60)
    print("5) Volumétrie")
    print("=" * 60)
    print(f"  {'BDD':45s} {'Nat':>4s} {'Rel':>4s} {'Rol':>4s} {'Twn':>4s} {'Total':>6s}")
    total_props = 0
    for db_name in sorted(dbs):
        db = dbs[db_name]
        n = len(db["properties"]["natives"])
        r = len(db["properties"]["relations"])
        ro = len(db["properties"]["rollups"])
        t = len(db["properties"]["text_twins"])
        s = n + r + ro + t
        total_props += s
        print(f"  {db_name:45s} {n:4d} {r:4d} {ro:4d} {t:4d} {s:6d}")
    print(f"  {'TOTAL':45s} {'':>20s} {total_props:6d}")

    # ======== Résumé ========
    print()
    print("=" * 60)
    print("RÉSUMÉ")
    print("=" * 60)
    if issues:
        print(f"\n{len(issues)} issue(s) à examiner :")
        for i in issues:
            print(i)
    else:
        print("✓ Aucune issue détectée. Manifest cohérent.")

    if info:
        print(f"\n{len(info)} info(s) :")
        for i in info[:10]:
            print(i)
        if len(info) > 10:
            print(f"  ... +{len(info)-10} autres")


if __name__ == "__main__":
    main()
