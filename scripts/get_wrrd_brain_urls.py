"""WF-011 — Récupère les URLs Drive des 11 WR-RD Brain depuis la base SQLite locale Drive."""
import sqlite3
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = r"C:\Users\leona\AppData\Local\Google\DriveFS\101486418960336612156\mirror_metadata_sqlite.db"

WRRD_BRAIN_FILES = [
    "WR-RD - Docs méta LBP.md",
    "WR-RD - Glossaire LBP.md",
    "WR-RD - Registre des notes de concept.md",
    "WR-RD - Registre des taxonomies.md",
    "WR-RD - Prompts LBP.md",
    "WR-RD - Registre des logic blocks.md",
    "WR-RD - Méthodes LBP.md",
    "WR-RD - Templates de bricks.md",
    "WR-RD - Agents LBP.md",
    "WR-RD - Outils externes.md",
    "WR-RD - Manuels de BDD.md",
]

conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
cursor = conn.cursor()

# Trouver le stable_id du dossier "WR-RD" dans "Manuels de BDD/Brain/"
# Approche : chercher tous les items WR-RD - X.md, joindre avec stable_parents pour filtrer ceux dont
# le path remonte par "WR-RD" puis "Brain" puis "Manuels de BDD".

# Plus simple : récupérer tous les items qui matchent par titre, puis filtrer en regardant le path.
# On affichera tous les matches pour que Leonard valide visuellement.

results = {}
for title in WRRD_BRAIN_FILES:
    cursor.execute("""
        SELECT i.id, i.local_title, i.stable_id
        FROM items i
        WHERE i.local_title = ?
        AND i.is_folder = 0
        AND i.trashed = 0
    """, (title,))
    rows = cursor.fetchall()
    results[title] = [{"file_id": r[0], "stable_id": r[2]} for r in rows]

# Pour distinguer le bon (Brain WR-RD) des autres (Twin WR-RD homonyme dans le cas Manuels de BDD…),
# on remonte la chaîne parent_stable_id jusqu'à trouver le mot "Brain" dans le path.
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

print("=== URLs Drive WR-RD Brain ===\n")
final = {}
for title, candidates in results.items():
    if not candidates:
        print(f"❌ {title} : NON TROUVÉ")
        continue
    # Pour chaque candidat, vérifier qu'il est dans Manuels de BDD/Brain/WR-RD
    for c in candidates:
        path = get_path(c["stable_id"])
        path_str = " > ".join(reversed(path[:5]))
        if "Brain" in path:
            url = f"https://drive.google.com/file/d/{c['file_id']}/view"
            final[title] = url
            print(f"✓ {title}")
            print(f"  Path: {path_str}")
            print(f"  URL : {url}\n")
            break
    else:
        # Aucun candidat dans Brain — afficher tous les candidats pour debug
        print(f"⚠ {title} : trouvé mais pas dans Brain")
        for c in candidates:
            path = get_path(c["stable_id"])
            print(f"  Candidat: {' > '.join(reversed(path[:5]))} (file_id={c['file_id']})")
        print()

print("\n=== JSON final ===")
print(json.dumps(final, indent=2, ensure_ascii=False))

conn.close()
