"""Pass B niveau 2 v2 — Audit des taxons orphelins.

Scan direct des manuels/WR-RD pour chercher les références au format
<NAMESPACE>.<TAXO>.<VALEUR> (3 segments, pattern de taxon valide).
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(r"H:\Drive partagés\LBP - shared\Architecture data")
TAXOS_DIR = VAULT / "Taxonomies"

DIRS = [
    VAULT / "Manuels de BDD" / "Digital Twin",
    VAULT / "Manuels de BDD" / "Digital Twin" / "WR-RD",
    VAULT / "Manuels de BDD" / "Mission Ops",
    VAULT / "Manuels de BDD" / "Mission Ops" / "WR-RD",
    VAULT / "Manuels de BDD" / "Brain",
]

# Pattern : XXX.YYY.ZZZ (3 segments) où chaque segment est MAJUSCULES + chiffres + underscore
TAXON_PATTERN = re.compile(r"\b([A-Z][A-Z0-9_]*)\.([A-Z][A-Z0-9_]*)\.([A-Z0-9_]+)\b")


def extract_taxons_from_canon(taxo_file: Path) -> set[str]:
    taxo_name = taxo_file.stem
    text = taxo_file.read_text(encoding="utf-8")
    pattern = re.escape(taxo_name) + r"\.([A-Z0-9_]+)"
    matches = re.findall(pattern, text)
    return set(f"{taxo_name}.{m}" for m in matches)


def main():
    # Charger taxons valides depuis canon
    taxos_canon = {}
    for f in TAXOS_DIR.glob("*.md"):
        if "00 - archives" in f.parts:
            continue
        taxos_canon[f.stem] = extract_taxons_from_canon(f)

    print(f"Taxos canon : {len(taxos_canon)}, total taxons valides : {sum(len(t) for t in taxos_canon.values())}")

    # Collecter fichiers cibles
    files = []
    for d in DIRS:
        for f in d.glob("*.md"):
            if "00 - archives" in f.parts:
                continue
            files.append(f)

    print(f"Fichiers à scanner : {len(files)}")

    # Scanner chaque fichier pour citations XXX.YYY.ZZZ
    all_citations = []
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for m in TAXON_PATTERN.finditer(line):
                ns, taxo_name, value = m.groups()
                full = f"{ns}.{taxo_name}.{value}"
                parent = f"{ns}.{taxo_name}"
                all_citations.append({
                    "file": str(f.relative_to(VAULT)),
                    "line": line_no,
                    "context": line[:150],
                    "code": full,
                    "parent": parent,
                    "value": value,
                })

    print(f"Citations potentielles XXX.YYY.ZZZ trouvées : {len(all_citations)}")

    # Audit : codes orphelins
    orphelins = []
    parent_inconnu = []
    for cit in all_citations:
        parent = cit["parent"]
        if parent not in taxos_canon:
            parent_inconnu.append(cit)
            continue
        if cit["code"] not in taxos_canon[parent]:
            orphelins.append(cit)

    # Dédoublonner
    orphelins_uniques = defaultdict(list)
    for o in orphelins:
        key = (o["parent"], o["code"])
        orphelins_uniques[key].append((o["file"], o["line"], o["context"][:120]))

    parent_inconnu_uniques = defaultdict(list)
    for o in parent_inconnu:
        key = o["parent"]
        parent_inconnu_uniques[key].append((o["file"], o["line"], o["code"], o["context"][:120]))

    print(f"\n=== ORPHELINS (taxons absents de leur taxo parente canon) ===")
    print(f"Citations orphelines : {len(orphelins)}")
    print(f"Codes uniques orphelins : {len(orphelins_uniques)}")
    for (parent, code), instances in sorted(orphelins_uniques.items()):
        print(f"\n  [{code}] (parent={parent}) cité {len(instances)}x")
        for f, l, ctx in instances[:2]:
            print(f"    {f} L{l}: {ctx}")
        if len(instances) > 2:
            print(f"    ... +{len(instances)-2} autres")

    print(f"\n=== PARENT INCONNU (taxos parents introuvables dans canon) ===")
    print(f"Citations : {len(parent_inconnu)}")
    print(f"Parents uniques : {len(parent_inconnu_uniques)}")
    for parent, instances in sorted(parent_inconnu_uniques.items()):
        codes = set(i[2] for i in instances)
        print(f"\n  [parent={parent}] {len(instances)} citations, {len(codes)} codes uniques")
        for f, l, code, ctx in instances[:2]:
            print(f"    {f} L{l}: {code} — {ctx}")

    # Save
    out = {
        "metadata": {
            "files_scanned": len(files),
            "total_citations_xyz": len(all_citations),
            "orphelins_citations": len(orphelins),
            "orphelins_uniques": len(orphelins_uniques),
            "parent_inconnu_citations": len(parent_inconnu),
            "parent_inconnu_uniques": len(parent_inconnu_uniques),
        },
        "orphelins_uniques": [
            {"parent": p, "code": c, "nb": len(insts), "citations": [{"file": f, "line": l, "context": ctx} for f,l,ctx in insts]}
            for (p, c), insts in sorted(orphelins_uniques.items())
        ],
        "parent_inconnu": [
            {"parent": p, "codes_cites": list(set(i[2] for i in insts)), "nb_citations": len(insts), "citations": [{"file": f, "line": l, "code": code, "context": ctx} for f,l,code,ctx in insts]}
            for p, insts in sorted(parent_inconnu_uniques.items())
        ],
    }
    out_path = Path(__file__).parent / "taxons_orphelins_v2_report.json"
    json.dump(out, open(out_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"\nRapport : {out_path}")


if __name__ == "__main__":
    main()
