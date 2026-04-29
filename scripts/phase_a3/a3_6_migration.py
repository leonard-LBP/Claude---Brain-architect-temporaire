"""
Phase A3.6 — consolidation des updates Glossaire CPT_* → GLO_*.

Sources:
1. update_plan.json (A3 masse) — glossaire_url + drive_code
2. a3bis_plan.json (A3.bis) — glossaire_page_id + glossaire_props.Code unique
3. Hardcoded extras: 3 calibration + 2 A3.ter

Output: scripts/phase_a3/output/a3_6_migration.json
  [
    {"glossaire_page_id": "...", "old_code": "CPT_X_Y", "new_code": "GLO_X_Y", "name": "..."},
    ...
  ]
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).parent / "output"


def main():
    plan = json.loads((ROOT / "update_plan.json").read_text(encoding="utf-8"))
    a3bis = json.loads((ROOT / "a3bis_plan.json").read_text(encoding="utf-8"))

    migrations = []
    seen = set()

    # 1) A3 masse: 35 concepts (with their glossaire URLs when not collision)
    for u in plan["updates"]:
        if u.get("glossaire_url") and "collision_glossaire" not in u.get("flags", []) and "no_glossaire_link_yet" not in u.get("flags", []):
            gid = u["glossaire_url"].split("/p/")[-1]
            old = u["drive_code"]
            new = "GLO" + old[3:] if old.startswith("CPT") else None
            if new and gid not in seen:
                migrations.append({
                    "glossaire_page_id": gid,
                    "old_code": old,
                    "new_code": new,
                    "name": u.get("canonical"),
                    "source": "a3_masse",
                })
                seen.add(gid)

    # 2) A3.bis (24 new + 6 collision_fix = 30)
    for u in a3bis["updates"]:
        gid = u["glossaire_page_id"]
        old = u["glossaire_props"].get("Code unique", "")
        new = "GLO" + old[3:] if old.startswith("CPT") else None
        if new and gid not in seen:
            migrations.append({
                "glossaire_page_id": gid,
                "old_code": old,
                "new_code": new,
                "name": u.get("file", "").replace("Concept - ", "").replace(".md", ""),
                "source": u.get("phase"),
            })
            seen.add(gid)

    # 3) Hardcoded extras
    extras = [
        # 3 calibration (already done in earlier phase)
        {"glossaire_page_id": "2f7e1a18653c8061bdfaede8485cc6ce", "old_code": "CPT_FRAME_3P", "name": "3P (Philosophie, Principes, Pratiques)", "source": "a3_calibration"},
        {"glossaire_page_id": "30fe1a18653c80dbaaaae47da27a3c3b", "old_code": "CPT_CAP_ABSORPTION_MOTRICE", "name": "Absorption (capacité motrice)", "source": "a3_calibration"},
        {"glossaire_page_id": "30fe1a18653c80419c35eed9bf723abe", "old_code": "CPT_CAP_ADAPTATION_MOTRICE", "name": "Adaptation (capacité motrice)", "source": "a3_calibration"},
        # 2 A3.ter (Capacité générique + I/O Processus original — even if archived, migrate code)
        {"glossaire_page_id": "2f7e1a18653c80e2848ac28c2bc9fae7", "old_code": "CPT_CAP_CAPACITE_GENERIQUE", "name": "Capacité générique", "source": "a3_ter"},
        {"glossaire_page_id": "30fe1a18653c803985a6c383f1ce5692", "old_code": "CPT_PROC_INPUT_OUTPUT_PROCESSUS", "name": "Input/ Output (Processus) [archivé]", "source": "a3_ter_archived"},
    ]
    for e in extras:
        if e["glossaire_page_id"] not in seen:
            e["new_code"] = "GLO" + e["old_code"][3:]
            migrations.append(e)
            seen.add(e["glossaire_page_id"])

    out = ROOT / "a3_6_migration.json"
    out.write_text(json.dumps(migrations, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Total migrations: {len(migrations)}")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
