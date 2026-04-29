"""
Phase A3.2 — manifest unifié.

Combine :
  - 72 Drive concepts (frontmatter parsed) via drive_concepts.json
  - 72 Drive URLs résolus via drive_urls.json
  - Glossaire LBP visible (100 entries) via raw/glossaire_full.json
  - Match par Nom canonique (drive title strip "Concept - " ↔ Nom canonique Glossaire)

Output : scripts/phase_a3/output/manifest_a3.json
   [
     {
       "drive_file": "...",
       "drive_canonical_name": "individu",
       "drive_code": "CPT_TBD_INDIVIDU",
       "drive_url": "https://...",
       "drive_status": "Validé",
       "glossaire_match": {
           "url": "https://app.notion.com/p/...",
           "code_actuel": "CPT.TBD.LBP.INDIVIDU",
           "code_target": "CPT_TBD_INDIVIDU",
           "nom_canonique": "Individu",
           "statut": "Validé",
           "domaine": ["Motor"]
       } | null,
       "actions": ["update_code", "update_lien_note (registre)"]
     },
     ...
   ]
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent / "output"


def norm(s: str) -> str:
    if not s:
        return ""
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return s


def drive_canonical(title: str) -> str:
    if not title:
        return ""
    t = re.sub(r"^Concept\s*-\s*", "", title.strip(), flags=re.IGNORECASE)
    return norm(t)


def main() -> None:
    drive = json.loads((ROOT / "drive_concepts.json").read_text(encoding="utf-8"))
    urls = json.loads((ROOT / "drive_urls.json").read_text(encoding="utf-8"))
    gloss = json.loads((ROOT / "raw" / "glossaire_full.json").read_text(encoding="utf-8"))["results"]

    gloss_by_name = {norm(e.get("Nom canonique", "")): e for e in gloss}

    manifest = []
    for d in drive:
        title = d.get("title", "")
        file = d.get("file", "")
        canon = drive_canonical(title)
        url_entry = urls.get(file) or {}
        match = gloss_by_name.get(canon)

        item = {
            "drive_file": file,
            "drive_title": title,
            "drive_canonical_name": canon,
            "drive_code": d.get("code"),
            "drive_status": d.get("status"),
            "drive_version": d.get("version"),
            "drive_url": url_entry.get("url"),
            "drive_id": url_entry.get("drive_id"),
            "glossaire_match": None,
            "actions": [],
        }
        if match:
            current_code = (match.get("Code unique") or "").strip()
            target_code = d.get("code")
            item["glossaire_match"] = {
                "url": match.get("url"),
                "code_actuel": current_code,
                "code_target": target_code,
                "nom_canonique_notion": match.get("Nom canonique"),
                "statut_notion": match.get("Statut de l'objet"),
                "domaine_notion": match.get("Domaine d'usage"),
                "type_concept": match.get("Type de concept"),
            }
            if current_code != target_code:
                item["actions"].append("update_code_unique")
        else:
            item["actions"].append("glossaire_lookup_needed (not in visible 100)")

        manifest.append(item)

    out = ROOT / "manifest_a3.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    matched = sum(1 for x in manifest if x["glossaire_match"])
    code_to_update = sum(1 for x in manifest if "update_code_unique" in x["actions"])
    print(f"Drive concepts: {len(manifest)}")
    print(f"  matched in visible Glossaire: {matched}")
    print(f"  code à migrer R-054: {code_to_update}")
    print(f"  besoin lookup additionnel: {len(manifest) - matched}")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
