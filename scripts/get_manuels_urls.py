"""Récupère les URLs Drive des Manuels de BDD depuis la base SQLite locale Drive."""
import sqlite3
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = r"C:\Users\leona\AppData\Local\Google\DriveFS\101486418960336612156\mirror_metadata_sqlite.db"

# Liste des manuels Markdown actifs (issus du Glob)
MANUELS = [
    # Brain
    ("Brain", "Manuel de BDD - Docs méta LBP.md"),
    ("Brain", "Manuel de BDD - Outils externes.md"),
    ("Brain", "Manuel de BDD - Registre des logic blocks.md"),
    ("Brain", "Manuel de BDD - Registre des notes de concept.md"),
    ("Brain", "Manuel de BDD - Templates de bricks.md"),
    ("Brain", "Manuel de BDD - Registre des taxonomies.md"),
    ("Brain", "Manuel de BDD - Prompts LBP.md"),
    ("Brain", "Manuel de BDD - Glossaire LBP.md"),
    ("Brain", "Manuel de BDD - Manuels de BDD.md"),
    ("Brain", "Manuel de BDD - Méthodes LBP.md"),
    ("Brain", "Manuel de BDD - Agents LBP.md"),
    # Digital Twin
    ("Digital Twin", "Manuel de BDD - Actifs.md"),
    ("Digital Twin", "Manuel de BDD - Actions détectées.md"),
    ("Digital Twin", "Manuel de BDD - Capacités organisationnelles.md"),
    ("Digital Twin", "Manuel de BDD - Collectifs.md"),
    ("Digital Twin", "Manuel de BDD - Enjeux.md"),
    ("Digital Twin", "Manuel de BDD - Environnements.md"),
    ("Digital Twin", "Manuel de BDD - Glossaire spécifique.md"),
    ("Digital Twin", "Manuel de BDD - Indicateurs.md"),
    ("Digital Twin", "Manuel de BDD - Individus.md"),
    ("Digital Twin", "Manuel de BDD - Initiatives organisationnelles.md"),
    ("Digital Twin", "Manuel de BDD - Journal des signaux.md"),
    ("Digital Twin", "Manuel de BDD - OKR.md"),
    ("Digital Twin", "Manuel de BDD - Organisations.md"),
    ("Digital Twin", "Manuel de BDD - Postes.md"),
    ("Digital Twin", "Manuel de BDD - Pratiques organisationnelles.md"),
    ("Digital Twin", "Manuel de BDD - Principes organisationnels.md"),
    ("Digital Twin", "Manuel de BDD - Problématiques.md"),
    ("Digital Twin", "Manuel de BDD - Processus candidats.md"),
    ("Digital Twin", "Manuel de BDD - Processus.md"),
    ("Digital Twin", "Manuel de BDD - Événements.md"),
    ("Digital Twin", "Manuel de BDD - Modulateurs.md"),
    ("Digital Twin", "Manuel de BDD - Relations inter-organisations.md"),
    # Mission Ops
    ("Mission Ops", "Manuel de BDD - Bricks.md"),
    ("Mission Ops", "Manuel de BDD - Meetings.md"),
    ("Mission Ops", "Manuel de BDD - Sources d’informations.md"),
    ("Mission Ops", "Manuel de BDD - Actions LBP.md"),
]

conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
cursor = conn.cursor()

def get_path(stable_id, depth=0):
    if depth > 12:
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

final = {}
for sub, title in MANUELS:
    cursor.execute("""
        SELECT i.id, i.stable_id
        FROM items i
        WHERE i.local_title = ?
        AND i.is_folder = 0
        AND i.trashed = 0
    """, (title,))
    rows = cursor.fetchall()
    if not rows:
        print(f"NOT FOUND: {sub}/{title}", file=sys.stderr)
        continue
    matched = None
    for file_id, stable_id in rows:
        path = get_path(stable_id)
        # Vérifier que path contient sub et "Manuels de BDD" et pas "00 - archives"
        if sub in path and "Manuels de BDD" in path and "00 - archives" not in path:
            matched = (file_id, path)
            break
    if matched:
        url = f"https://drive.google.com/file/d/{matched[0]}/view"
        key = f"{sub}/{title}"
        final[key] = url
    else:
        print(f"NO MATCH IN {sub}: {title}", file=sys.stderr)
        for fid, sid in rows:
            print(f"  Candidat path: {' > '.join(reversed(get_path(sid)[:6]))}", file=sys.stderr)

print(json.dumps(final, indent=2, ensure_ascii=False))
conn.close()
