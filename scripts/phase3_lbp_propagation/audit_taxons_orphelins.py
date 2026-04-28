"""Pass B niveau 2 — Audit des taxons orphelins.

Pour chaque taxon cité dans manuels/WR-RD (citations_report.json), vérifier
qu'il existe bien comme code de taxon dans la taxo parente (fichier .md canon).

Sortie : liste des orphelins (cités mais absents) + faux orphelins potentiels
(citations qui ne ressemblent pas à des codes de taxons réels).
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
TAXOS_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Taxonomies")
CITATIONS = ROOT / "citations_report.json"


def extract_taxons_from_canon(taxo_file: Path) -> set[str]:
    """Extrait tous les codes de taxons (format X.Y.Z) propres à cette taxo."""
    taxo_name = taxo_file.stem  # ex. "OBJ.STATUT"
    text = taxo_file.read_text(encoding="utf-8")
    # Pattern : taxo_name + . + ALPHANUM_UNDERSCORE
    pattern = re.escape(taxo_name) + r"\.([A-Z0-9_]+)"
    matches = re.findall(pattern, text)
    return set(f"{taxo_name}.{m}" for m in matches)


def main():
    # Charger toutes les taxos canon (filename .md, hors archives)
    taxos_canon = {}
    for f in TAXOS_DIR.glob("*.md"):
        if "00 - archives" in f.parts:
            continue
        taxons = extract_taxons_from_canon(f)
        taxos_canon[f.stem] = taxons

    print(f"Taxos canon chargées : {len(taxos_canon)}")
    print(f"Total taxons valides détectés : {sum(len(t) for t in taxos_canon.values())}")

    # Charger citations
    report = json.load(open(CITATIONS, encoding="utf-8"))
    citations_taxons = []
    for f in report["files"]:
        for c in f["citations"]:
            if c["code_type"] == "taxon":
                citations_taxons.append({
                    "file": f["file_path"],
                    "line": c["line_number"],
                    "code": c["cited_code"],
                    "parent": c["parent_taxo"],
                    "context": c["line_content"],
                })

    print(f"Citations taxons à auditer : {len(citations_taxons)}")

    # Audit : pour chaque citation, vérifier que le code existe dans la taxo parente
    orphelins = []
    parent_inconnu = []
    for cit in citations_taxons:
        parent = cit["parent"]
        if parent not in taxos_canon:
            parent_inconnu.append(cit)
            continue
        if cit["code"] not in taxos_canon[parent]:
            orphelins.append(cit)

    # Dédoublonner orphelins par (parent, code) pour résumer
    orphelins_uniques = defaultdict(list)
    for o in orphelins:
        key = (o["parent"], o["code"])
        orphelins_uniques[key].append((o["file"], o["line"], o["context"][:120]))

    print(f"\n=== ORPHELINS (taxons cités absents de leur taxo parente) ===")
    print(f"Total citations orphelines : {len(orphelins)}")
    print(f"Codes uniques orphelins : {len(orphelins_uniques)}")
    for (parent, code), instances in sorted(orphelins_uniques.items()):
        print(f"\n  [{code}] (parent={parent}) cité {len(instances)}x :")
        for f, l, ctx in instances[:3]:
            print(f"    {f} L{l} :: {ctx}")
        if len(instances) > 3:
            print(f"    ... +{len(instances)-3} autres")

    if parent_inconnu:
        print(f"\n=== PARENT INCONNU ({len(parent_inconnu)}) ===")
        for cit in parent_inconnu[:5]:
            print(f"  {cit['code']} (parent {cit['parent']} introuvable) — {cit['file']} L{cit['line']}")

    # Save JSON
    out = {
        "metadata": {
            "total_taxons_cites": len(citations_taxons),
            "total_orphelins_citations": len(orphelins),
            "total_orphelins_uniques": len(orphelins_uniques),
            "total_parent_inconnu": len(parent_inconnu),
        },
        "orphelins_uniques": [
            {
                "parent_taxo": parent,
                "code_orphelin": code,
                "nb_citations": len(instances),
                "citations": [{"file": f, "line": l, "context": ctx} for f, l, ctx in instances],
            }
            for (parent, code), instances in sorted(orphelins_uniques.items())
        ],
        "parent_inconnu": parent_inconnu,
    }
    out_path = ROOT / "taxons_orphelins_report.json"
    json.dump(out, open(out_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"\nRapport sauvé : {out_path}")


if __name__ == "__main__":
    main()
