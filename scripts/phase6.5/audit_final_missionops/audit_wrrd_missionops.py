"""Audit Manuel Mission Ops <-> WR-RD (lecture seule)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

PARSED_DIR = Path(r"C:\Users\leona\LBP - dev\Claude - Brain architect temporaire\scripts\phase6.5\audit_final_missionops\manuels_parsed")
WRRD_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Mission Ops\WR-RD")
ROOT = PARSED_DIR.parent

SYSTEM_PROPS = {"created date", "last updated date"}


def norm(s):
    if s is None:
        return ""
    return s.replace("’", "'").lower().strip()


def has_ascii_apos(s):
    return "'" in s


def split_md_row(line):
    line = line.strip()
    if not line.startswith("|"):
        return None
    inner = line.strip().strip("|")
    return [c.strip() for c in inner.split("|")]


def is_separator_row(line):
    line = line.strip()
    if not line.startswith("|"):
        return False
    inner = line.strip().strip("|")
    cells = [c.strip() for c in inner.split("|")]
    return all(re.fullmatch(r":?-+:?", c) for c in cells if c)


def parse_wrrd(text):
    lines = text.splitlines()
    props = {}
    in_table = False
    headers = None
    for i, line in enumerate(lines):
        if line.strip().startswith("| Champ "):
            headers = split_md_row(line)
            in_table = True
            continue
        if in_table and is_separator_row(line):
            continue
        if in_table:
            if line.strip().startswith("|"):
                cells = split_md_row(line)
                if cells and len(cells) >= 2 and cells[0]:
                    name = cells[0]
                    if name.lower() == "champ":
                        continue
                    key = norm(name)
                    col_map = {}
                    for h, v in zip(headers or [], cells):
                        col_map[h.strip()] = v
                    col_map["_raw_name"] = name
                    props[key] = col_map
            else:
                in_table = False
                headers = None
    return props


def main():
    results = []
    apos_wrrd = []
    for parsed_file in sorted(PARSED_DIR.glob("*.json")):
        bdd_name = parsed_file.stem
        wrrd_path = WRRD_DIR / f"WR-RD - {bdd_name}.md"
        if not wrrd_path.exists():
            print(f"!! WR-RD manquant pour {bdd_name}")
            continue
        manuel = json.load(open(parsed_file, encoding="utf-8"))
        wrrd_text = wrrd_path.read_text(encoding="utf-8")
        wrrd_props = parse_wrrd(wrrd_text)

        # Apostrophes ASCII dans WR-RD
        for k, v in wrrd_props.items():
            raw = v.get("_raw_name", "")
            if has_ascii_apos(raw):
                apos_wrrd.append({"source": "WR-RD", "bdd": bdd_name, "name": raw})

        manuel_expected = [p for p in manuel["props"] if p.get("expected_in_wrrd") and norm(p["name"]) not in SYSTEM_PROPS]
        manuel_keys = set(norm(p["name"]) for p in manuel_expected)
        wrrd_keys = set(wrrd_props.keys())

        missing_in_wrrd = sorted(manuel_keys - wrrd_keys)
        extra_in_wrrd = sorted(wrrd_keys - manuel_keys)

        # Map missing/extra to original names
        missing_named = []
        for k in missing_in_wrrd:
            for p in manuel_expected:
                if norm(p["name"]) == k:
                    missing_named.append({"name": p["name"], "section": p["section"], "type": p["type"]})
                    break
        extra_named = []
        for k in extra_in_wrrd:
            extra_named.append({"name": wrrd_props[k]["_raw_name"]})

        results.append({
            "bdd": bdd_name,
            "manuel_count": len(manuel_expected),
            "wrrd_count": len(wrrd_props),
            "missing_in_wrrd": missing_named,
            "extra_in_wrrd": extra_named,
        })

    print(f"\n{'BDD':<28} {'Manuel':<8} {'WR-RD':<8} {'Miss':<6} {'Extra':<6}")
    print("-" * 65)
    for r in results:
        flag = "X" if r["missing_in_wrrd"] or r["extra_in_wrrd"] else "."
        print(f"{flag} {r['bdd']:<26} {r['manuel_count']:<8} {r['wrrd_count']:<8} {len(r['missing_in_wrrd']):<6} {len(r['extra_in_wrrd']):<6}")
        for m in r["missing_in_wrrd"]:
            print(f"    - missing in WR-RD: {m['name']} ({m['section']})")
        for e in r["extra_in_wrrd"]:
            print(f"    - extra in WR-RD: {e['name']}")

    print(f"\nApostrophes ASCII WR-RD : {len(apos_wrrd)}")
    for v in apos_wrrd:
        print(f"  - {v['bdd']} :: {v['name']}")

    json.dump(results, open(ROOT / "audit_wrrd_report.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(apos_wrrd, open(ROOT / "apos_wrrd.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
