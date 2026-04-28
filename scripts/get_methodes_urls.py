"""WF-011 — Récupère les URLs Drive des méthodes actives."""
import sqlite3
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = r"C:\Users\leona\AppData\Local\Google\DriveFS\101486418960336612156\mirror_metadata_sqlite.db"

FILES = [
    "Méthode - Carte d'alignement des Recommandations.md",
    "Méthode - Carte de causalité 5D des Problématiques.md",
]

conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
cursor = conn.cursor()

def get_path(stable_id, depth=0):
    if depth > 10:
        return []
    cursor.execute("""
        SELECT sp.parent_stable_id, p.local_title
        FROM stable_parents sp
        JOIN items p ON p.stable_id = sp.parent_stable_id
        WHERE sp.item_stable_id = ?
    """, (stable_id,))
    parent = cursor.fetchone()
    if parent is None:
        return []
    return [parent[1]] + get_path(parent[0], depth + 1)

results = {}
for title in FILES:
    cursor.execute("""
        SELECT i.id, i.local_title, i.stable_id
        FROM items i
        WHERE i.local_title = ? AND i.is_folder = 0 AND i.trashed = 0
    """, (title,))
    rows = cursor.fetchall()
    for r in rows:
        path = get_path(r[2])
        # Filtre : doit être dans Architecture data > Méthodes (pas archives)
        if "Méthodes" in path and "00 - archives" not in path:
            url = f"https://drive.google.com/file/d/{r[0]}/view"
            results[title] = url
            print(f"✓ {title}\n  Path: {' > '.join(reversed(path[:5]))}\n  URL : {url}\n")
            break
    else:
        print(f"❌ {title} : non trouvé hors archives")

print("\n=== JSON ===")
print(json.dumps(results, indent=2, ensure_ascii=False))
conn.close()
