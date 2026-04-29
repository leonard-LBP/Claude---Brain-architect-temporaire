"""
Phase A4.A.1 — Diff complet 102 .md taxos vs 90 Notion Validé.

Source Notion : export Notion AI (90 entrées Validé) dans notion_validated_export.txt
Format ligne : Nom|Statut|Code(.LBP)|UUID|Lien Drive
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).parent / "output"
EXPORT = Path(__file__).parent / "notion_validated_export.txt"


def normalize(c: str) -> str:
    """Strip .LBP suffix."""
    if c.endswith(".LBP"):
        return c[:-4]
    return c


def main() -> None:
    drive = json.loads((ROOT / "drive_taxos.json").read_text(encoding="utf-8"))
    drive_by_code = {e["code"]: e for e in drive if e.get("code")}

    notion = []
    for line in EXPORT.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("|")
        if len(parts) != 5:
            print(f"BAD LINE: {line}")
            continue
        name, statut, code_lbp, uuid, drive_link = parts
        norm = normalize(code_lbp)
        notion.append({
            "name": name, "statut": statut, "code_lbp": code_lbp, "code_norm": norm,
            "uuid": uuid, "url": f"https://app.notion.com/p/{uuid}", "drive_link": drive_link,
        })

    notion_by_code = {}
    for e in notion:
        notion_by_code.setdefault(e["code_norm"], []).append(e)

    drive_set = set(drive_by_code.keys())
    notion_set = set(notion_by_code.keys())

    matched = drive_set & notion_set
    drive_only = drive_set - notion_set
    notion_only = notion_set - drive_set
    duplicates = {k: v for k, v in notion_by_code.items() if len(v) > 1}

    print(f"Drive .md: {len(drive_set)}")
    print(f"Notion Validé: {len(notion)} ({len(notion_by_code)} unique codes)")
    print()
    print(f"=== DIFF ===")
    print(f"  Matched (à update): {len(matched)}")
    print(f"  Drive only (à créer côté Notion): {len(drive_only)}")
    print(f"  Notion only Validé (orphelins, à archiver ou créer .md): {len(notion_only)}")
    print(f"  Doublons Notion: {len(duplicates)}")
    print()

    if drive_only:
        print(f"Drive only ({len(drive_only)} à créer dans Notion):")
        for c in sorted(drive_only):
            d = drive_by_code[c]
            print(f"  - {c}  (file: {d['file']})")
    print()

    if notion_only:
        print(f"Notion only ({len(notion_only)} validés sans .md) :")
        for c in sorted(notion_only):
            for e in notion_by_code[c]:
                print(f"  - {c}  (Notion: \"{e['name']}\")")
    print()

    if duplicates:
        print("Doublons:")
        for c, vs in duplicates.items():
            print(f"  - {c}: {len(vs)} entrées Validé")

    # Output upsert plan
    plan = []
    for c in sorted(matched):
        d = drive_by_code[c]
        n = notion_by_code[c][0]
        plan.append({
            "action": "update",
            "code": c,
            "code_lbp_old": n["code_lbp"],
            "uuid": n["uuid"],
            "drive_file": d["file"],
        })
    for c in sorted(drive_only):
        d = drive_by_code[c]
        plan.append({
            "action": "create",
            "code": c,
            "drive_file": d["file"],
        })
    out = ROOT / "upsert_plan.json"
    out.write_text(json.dumps({"plan": plan, "notion_only": sorted(notion_only), "duplicates": list(duplicates.keys())}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
