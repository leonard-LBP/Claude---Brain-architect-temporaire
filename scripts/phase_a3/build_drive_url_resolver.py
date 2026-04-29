"""
Phase A3.2 — resolver Drive URLs.

Pour chacun des 72 fichiers Markdown Notes de Concept du Drive partagé,
extrait l'ID Drive depuis le cache DriveFS local (sqlite) et construit
l'URL stable `https://drive.google.com/file/d/<ID>/view`.

Output : scripts/phase_a3/output/drive_urls.json
  { "<file.md>": { "drive_id": "...", "url": "..." }, ... }
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

DRIVE_FOLDER = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Notes de Concept")
DRIVEFS_DB_CANDIDATES = [
    Path(r"C:/Users/leona/AppData/Local/Google/DriveFS/101486418960336612156/metadata_sqlite_db"),
    Path(r"C:/Users/leona/AppData/Local/Google/DriveFS/114540043112787619692/metadata_sqlite_db"),
]
OUT = Path(__file__).parent / "output" / "drive_urls.json"


def collect_titles_from_drive() -> list[str]:
    return sorted(p.name for p in DRIVE_FOLDER.glob("*.md"))


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
    titles = collect_titles_from_drive()
    out: dict = {}
    unresolved: list[str] = []
    multiple: list[str] = []

    for title in titles:
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

    print(f"Resolved: {len(out)}/{len(titles)}")
    print(f"Unresolved: {len(unresolved)}")
    for t in unresolved:
        print(f"  - {t}")
    print(f"Multiple candidates (kept most recent): {len(multiple)}")
    for m in multiple[:10]:
        print(f"  - {m}")
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
