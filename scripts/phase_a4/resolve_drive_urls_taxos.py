"""
Phase A4 — resolver Drive URLs pour les 102 taxos.
Réutilise le pattern de scripts/phase_a3/build_drive_url_resolver.py.

Output: scripts/phase_a4/output/drive_urls_taxos.json
"""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path

DRIVE_FOLDER = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Taxonomies")
DRIVEFS_DB_CANDIDATES = [
    Path(r"C:/Users/leona/AppData/Local/Google/DriveFS/101486418960336612156/metadata_sqlite_db"),
    Path(r"C:/Users/leona/AppData/Local/Google/DriveFS/114540043112787619692/metadata_sqlite_db"),
]
OUT = Path(__file__).parent / "output" / "drive_urls_taxos.json"


def lookup(db: Path, title: str) -> list[dict]:
    con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    try:
        cur = con.execute(
            "SELECT id, local_title, modified_date, trashed FROM items WHERE local_title = ? AND trashed = 0",
            (title,),
        )
        return [{"id": r[0], "modified": r[2]} for r in cur.fetchall()]
    finally:
        con.close()


def main():
    titles = sorted(p.name for p in DRIVE_FOLDER.glob("*.md"))
    out: dict = {}
    unresolved = []
    for title in titles:
        rows = []
        for db in DRIVEFS_DB_CANDIDATES:
            if db.exists():
                rows.extend(lookup(db, title))
        seen = set()
        rows = [r for r in rows if not (r["id"] in seen or seen.add(r["id"]))]
        if not rows:
            unresolved.append(title)
            continue
        rows.sort(key=lambda r: r["modified"] or 0, reverse=True)
        out[title] = {
            "drive_id": rows[0]["id"],
            "url": f"https://drive.google.com/file/d/{rows[0]['id']}/view",
        }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Resolved: {len(out)}/{len(titles)}")
    if unresolved:
        print(f"Unresolved: {unresolved}")


if __name__ == "__main__":
    main()
