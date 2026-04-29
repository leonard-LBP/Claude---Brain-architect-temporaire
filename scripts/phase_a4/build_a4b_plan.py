"""
Phase A4.B — Build the execution plan for mass apply.

Combines:
- manuel_taxos_extracted.json (parsed from .md): title, codes
- taxo_code_to_url.json: code → Notion URL
- notion query dump: Nom canonique → page url (page_id)

Output: scripts/phase_a4/output/a4b_plan.json
  [{"page_id": "...", "title": "...", "n_codes": N, "taxo_urls": [...]}]
"""
from __future__ import annotations
import io, json, sys, re
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).parent / "output"
QUERY_DUMP = Path(r"C:\Users\leona\.claude\projects\C--Users-leona-LBP---dev-Claude---Brain-architect-temporaire\665c6c60-dd66-4615-ac98-78b9622882d5\tool-results\mcp-44de9dc4-eaa9-4046-af64-acaf6e4890a1-notion-query-database-view-1777490195468.txt")

SKIP = {
    "Manuel de BDD - Actifs",  # already done (test)
}
NO_SECTION = set()  # filled below


def normalize_title(s: str) -> str:
    return s.replace("’", "'").strip()


def main():
    extracted = json.loads((ROOT / "manuel_taxos_extracted.json").read_text(encoding="utf-8"))
    code_to_url = json.loads((ROOT / "taxo_code_to_url.json").read_text(encoding="utf-8"))

    # Load Notion query dump
    raw = json.loads(QUERY_DUMP.read_text(encoding="utf-8"))
    payload = json.loads(raw[0]["text"])
    rows = payload["results"]

    # Build title → page url map (only Validé)
    nom_to_url = {}
    for r in rows:
        statut = r.get("Statut de l’objet") or r.get("Statut de l'objet")
        if statut != "Validé":
            continue
        nom = r.get("Nom canonique", "")
        url = r.get("url", "")
        nom_to_url[normalize_title(nom)] = url

    plan = []
    skipped = []
    unmatched = []

    for e in extracted:
        title = normalize_title(e.get("title", ""))
        if title in SKIP:
            skipped.append({"title": title, "reason": "already done (test)"})
            continue
        if not e.get("section"):
            skipped.append({"title": title, "reason": "no Usages des taxonomies section"})
            continue
        url = nom_to_url.get(title)
        if not url:
            unmatched.append(title)
            continue
        codes = e.get("codes", [])
        taxo_urls = [code_to_url[c] for c in codes if c in code_to_url]
        # extract page_id from url
        m = re.search(r"/p/([0-9a-f]{32})", url)
        page_id = m.group(1) if m else url
        plan.append({
            "page_id": page_id,
            "page_url": url,
            "title": title,
            "scope": e.get("scope"),
            "n_codes": len(taxo_urls),
            "taxo_urls": taxo_urls,
        })

    out = ROOT / "a4b_plan.json"
    out.write_text(json.dumps({"plan": plan, "skipped": skipped, "unmatched": unmatched}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Plan: {len(plan)} updates")
    print(f"Skipped: {len(skipped)}")
    for s in skipped:
        print(f"  - {s['title']} :: {s['reason']}")
    if unmatched:
        print(f"UNMATCHED ({len(unmatched)}):")
        for t in unmatched:
            print(f"  - {t}")
    total_relations = sum(p["n_codes"] for p in plan)
    print(f"Total relations to set: {total_relations}")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
