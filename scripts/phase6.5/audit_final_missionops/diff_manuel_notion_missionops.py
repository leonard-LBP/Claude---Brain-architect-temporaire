"""Diff Manuel Mission Ops <-> Notion."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_final_missionops")
MANUELS_DIR = ROOT / "manuels_parsed"
NOTION_CACHE = json.load(open(ROOT / "notion_schemas.json", encoding="utf-8"))

NOTION_SYSTEM_TYPES = {"created_time", "last_edited_time"}
SYSTEM_NAMES_NORM = {"created date", "last updated date"}


def norm(s):
    if s is None:
        return ""
    return s.replace("’", "'").lower().strip()


def has_ascii_apos(s):
    return "'" in s


def main():
    missing = {}
    extras = {}
    apos_violations = []
    summary = []

    for manuel_file in sorted(MANUELS_DIR.glob("*.json")):
        bdd_name = manuel_file.stem
        manuel = json.load(open(manuel_file, encoding="utf-8"))

        if bdd_name not in NOTION_CACHE:
            print(f"!! {bdd_name} : pas de schema Notion")
            continue

        notion = NOTION_CACHE[bdd_name]
        notion_norm = {norm(n): (n, t) for n, t in notion.items()}

        # Apostrophes ASCII dans noms Notion
        for n in notion:
            if has_ascii_apos(n):
                apos_violations.append({"source": "Notion", "bdd": bdd_name, "name": n})

        manuel_expected = [p for p in manuel["props"] if p["expected_in_notion"]]
        manuel_norm_set = set(norm(p["name"]) for p in manuel_expected)

        # Apostrophes ASCII dans noms manuel
        for p in manuel["props"]:
            if has_ascii_apos(p["name"]):
                apos_violations.append({"source": "Manuel", "bdd": bdd_name, "name": p["name"]})

        bdd_missing = []
        for p in manuel_expected:
            n = norm(p["name"])
            if n in SYSTEM_NAMES_NORM:
                continue
            if n == "lien vers la note avancée" and not manuel["has_advanced_note"]:
                continue
            if n not in notion_norm:
                bdd_missing.append({
                    "name": p["name"],
                    "type": p["type"],
                    "raw_type": p["raw_type"],
                    "section": p["section"],
                })

        bdd_extras = []
        for n_norm, (n_orig, t) in notion_norm.items():
            if t in NOTION_SYSTEM_TYPES or n_norm in SYSTEM_NAMES_NORM:
                continue
            if t == "rollup":
                continue
            # Skip auto-mirror text (Notion crée auto les jumelles texte avec suffixe "(texte)")
            if n_norm.endswith("(texte)"):
                # vérifier qu'elle est bien attendue côté manuel (présence sans suffixe + miroir DUAL)
                # Comme manuel les déclare avec "(texte)" aussi → on garde comparaison normale
                pass
            if n_norm not in manuel_norm_set:
                bdd_extras.append({"name": n_orig, "type": t})

        if bdd_missing:
            missing[bdd_name] = bdd_missing
        if bdd_extras:
            extras[bdd_name] = bdd_extras

        summary.append({
            "bdd": bdd_name,
            "manuel_expected": len(manuel_expected),
            "notion_actual": len(notion),
            "missing": len(bdd_missing),
            "extras": len(bdd_extras),
            "pass4_deferred": manuel.get("n_pass4_deferred", 0),
        })

    print(f"\n{'BDD':<28} {'ManExp':<8} {'Notion':<8} {'Miss':<6} {'Extra':<6} {'P4def':<6}")
    print("-" * 70)
    for s in summary:
        flag = "X" if s["missing"] > 0 else "."
        print(f"{flag} {s['bdd']:<26} {s['manuel_expected']:<8} {s['notion_actual']:<8} {s['missing']:<6} {s['extras']:<6} {s['pass4_deferred']:<6}")

    print(f"\nApostrophes ASCII (R-052) : {len(apos_violations)}")
    for v in apos_violations:
        print(f"  - [{v['source']}] {v['bdd']} :: {v['name']}")

    json.dump(missing, open(ROOT / "missing_in_notion.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(extras, open(ROOT / "extra_in_notion.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(apos_violations, open(ROOT / "apos_violations.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(summary, open(ROOT / "diff_summary.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
