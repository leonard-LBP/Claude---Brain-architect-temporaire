"""
WF-011 ad hoc — récupération URLs Drive pour les 11 docs du bundle docs méta LBP.

Lit le SQLite local de Drive Desktop pour résoudre file_id de chacun des 11 fichiers
.md publiés dans Architecture data\00 - Docs méta\Doctrines & playbooks\

Output : scripts/bundle_docs_meta/output/bundle_urls.json
  { "<file.md>": { "drive_id": "...", "url": "..." }, ... }
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

BUNDLE_FOLDER = Path(r"H:/Drive partagés/LBP - shared/Architecture data/00 - Docs méta/Doctrines & playbooks")
DRIVEFS_DB_CANDIDATES = [
    Path(r"C:/Users/leona/AppData/Local/Google/DriveFS/101486418960336612156/metadata_sqlite_db"),
    Path(r"C:/Users/leona/AppData/Local/Google/DriveFS/114540043112787619692/metadata_sqlite_db"),
]
OUT = Path(__file__).parent / "output" / "bundle_urls.json"

EXPECTED_FILES = [
    "PANORAMA_LBP.md",
    "DOCTRINE_LBP.md",
    "DOCTRINE_TWIN_LBP.md",
    "RULES_LBP.md",
    "DECISIONS_LBP.md",
    "WORKFLOWS_LBP.md",
    "SPECS_ARCHITECTURE_BRAIN_LBP.md",
    "SPECS_ARCHITECTURE_TWIN_LBP.md",
    "SPECS_ARCHITECTURE_MISSION_OPS_LBP.md",
    "CODIFICATION_LBP.md",
    "PROPAGATION_RULES_LBP.md",
]


def lookup_in_db(db: Path, title: str) -> list[dict]:
    """Return all matches for an exact local_title in this DriveFS DB."""
    con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    try:
        cur = con.execute(
            "SELECT id, local_title, modified_date, trashed FROM items WHERE local_title = ? AND trashed = 0",
            (title,),
        )
        return [
            {"id": r[0], "title": r[1], "modified": r[2], "trashed": r[3]}
            for r in cur.fetchall()
        ]
    finally:
        con.close()


def main() -> None:
    out: dict = {}
    unresolved: list[str] = []
    multiple: list[str] = []

    for title in EXPECTED_FILES:
        rows = []
        for db in DRIVEFS_DB_CANDIDATES:
            if db.exists():
                rows.extend(lookup_in_db(db, title))

        # dedupe by id
        seen = set()
        rows = [r for r in rows if not (r["id"] in seen or seen.add(r["id"]))]

        if not rows:
            unresolved.append(title)
            continue
        if len(rows) > 1:
            multiple.append(f"{title} -> {len(rows)} candidates")
            # pick most recently modified
            rows.sort(key=lambda r: r["modified"] or 0, reverse=True)

        chosen = rows[0]
        out[title] = {
            "drive_id": chosen["id"],
            "url": f"https://drive.google.com/file/d/{chosen['id']}/view",
            "all_candidates": [r["id"] for r in rows],
        }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Resolved: {len(out)}/{len(EXPECTED_FILES)}")
    if unresolved:
        print(f"Unresolved ({len(unresolved)}):")
        for t in unresolved:
            print(f"  - {t}")
    if multiple:
        print(f"Multiple candidates ({len(multiple)}):")
        for m in multiple:
            print(f"  - {m}")


if __name__ == "__main__":
    main()
