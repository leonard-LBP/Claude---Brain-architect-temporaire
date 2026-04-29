"""Resolve Drive URLs for the 5 missing files (1 Brain manuel + 4 MO WR-RD)."""
from __future__ import annotations
import io, sqlite3, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DB = r"C:\Users\leona\AppData\Local\Google\DriveFS\101486418960336612156\mirror_metadata_sqlite.db"

TARGETS = [
    "Manuel de BDD - Registre des taxonomies.md",
    "WR-RD - Bricks.md",
    "WR-RD - Meetings.md",
    "WR-RD - Actions LBP.md",
    "WR-RD - Sources d’informations.md",
]

conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
cur = conn.cursor()
for t in TARGETS:
    cur.execute("""
        SELECT i.id, i.local_title FROM items i
        WHERE i.local_title = ? AND i.is_folder = 0 AND i.trashed = 0
    """, (t,))
    rows = cur.fetchall()
    print(f"=== {t} ===")
    for r in rows:
        print(f"  id={r[0]}  https://drive.google.com/file/d/{r[0]}/view")
conn.close()
