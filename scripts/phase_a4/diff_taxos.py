"""
Phase A4.A.1 — Diff entre 102 .md taxos et entrées Notion `Registre des taxonomies`.

Match par code après normalisation : Markdown `code` vs Notion `code` strip `.LBP`.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).parent / "output"


def normalize_notion_code(c: str) -> str:
    if not c:
        return ""
    if c.endswith(".LBP"):
        return c[:-4]
    return c


def main() -> None:
    drive = json.loads((ROOT / "drive_taxos.json").read_text(encoding="utf-8"))
    notion = json.loads((ROOT / "notion_taxos.json").read_text(encoding="utf-8"))["results"]

    drive_by_code = {e["code"]: e for e in drive if e.get("code")}
    notion_by_code = {}
    for e in notion:
        raw = (e.get("Code unique") or "").strip()
        norm = normalize_notion_code(raw)
        if norm:
            notion_by_code.setdefault(norm, []).append({
                "raw_code": raw,
                "url": e.get("url"),
                "name": e.get("Nom canonique"),
                "statut": e.get("Statut de l'objet"),
            })

    drive_set = set(drive_by_code.keys())
    notion_set = set(notion_by_code.keys())

    matched = drive_set & notion_set
    drive_only = drive_set - notion_set
    notion_only = notion_set - drive_set
    duplicates = {k: v for k, v in notion_by_code.items() if len(v) > 1}

    print(f"Drive taxos: {len(drive_set)}")
    print(f"Notion visible: {len(notion)} ({len(notion_by_code)} unique codes)")
    print()
    print(f"=== DIFF (visible 100 Notion only — has_more=True) ===")
    print(f"  Matched: {len(matched)}")
    print(f"  Drive only (à créer ou en page 2 Notion): {len(drive_only)}")
    print(f"  Notion only visible (orphelins ou pré-renamings): {len(notion_only)}")
    print(f"  Doublons Notion (même code 2x+): {len(duplicates)}")
    print()
    if drive_only:
        print("Drive only:")
        for c in sorted(drive_only):
            print(f"  - {c}")
    print()
    if notion_only:
        print("Notion only:")
        for c in sorted(notion_only):
            for e in notion_by_code[c]:
                print(f"  - [{e['statut']}] {c}  ({e['raw_code']})  \"{e['name']}\"")
    print()
    if duplicates:
        print("Doublons:")
        for c, vs in duplicates.items():
            print(f"  - {c} ({len(vs)} entries)")
            for v in vs:
                print(f"      [{v['statut']}] {v['url']}  \"{v['name']}\"")

    # Save the diff for next step
    diff = {
        "matched": sorted(matched),
        "drive_only": sorted(drive_only),
        "notion_only": sorted(notion_only),
        "duplicates": duplicates,
    }
    out = ROOT / "diff_a4.json"
    out.write_text(json.dumps(diff, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
