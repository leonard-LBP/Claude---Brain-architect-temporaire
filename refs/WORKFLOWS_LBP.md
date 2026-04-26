# Workflows LBP — Brain / Twin / Mission Ops

> **Scope** : 🟦 LBP — Bundle écosystème.
> Ce fichier recense les workflows opérationnels intrinsèques à l'écosystème LBP (Brain, Digital Twin, Mission Ops). Il a vocation à être consommé par les agents et humains LBP (consultants, twin architect, brain architect) pour conduire des opérations standardisées sur l'écosystème.
> Les workflows propres à notre collaboration Claude (démarrage de session, etc.) sont dans `SESSION_WORKFLOWS.md`.
> Chaque workflow a un ID stable pour référence.
> Dernière mise à jour : 2026-04-26 — scission depuis l'ancien `WORKFLOWS.md` (qui mélangeait LBP et session).

---

## Index

| ID | Workflow | Statut |
|----|----------|--------|
| WF-011 | Récupérer l'URL Drive d'un fichier local du vault | Actif |
| WF-012 | Indexer un doc Markdown dans sa BDD Notion | Actif (itéré au fil des batchs) |
| WF-001 | Créer un nouveau doc Brain | À formaliser |
| WF-002 | Mettre à jour un doc Brain existant | À formaliser |
| WF-003 | Archiver un doc Brain (vault + Notion) | À formaliser |
| WF-008 | Propagation d'impacts après modification | À formaliser |
| WF-009 | Migration d'une BDD XXX | À formaliser |
| WF-013 | Générer un WR-RD à partir d'un Manuel de BDD | À formaliser (Phase 6) |

---

## WF-011 : Récupérer l'URL Drive d'un fichier local

**Statut** : Actif (découvert 2026-04-24, mini-batch 0 Twin v2)

### Contexte

Les docs du vault Architecture data sont synchronisés avec Google Drive via Drive for Desktop. Pour indexer un doc dans Notion (R-029), il faut **l'URL Drive** à inscrire dans les propriétés "Lien vers..." des BDD Brain. Le MCP Drive n'étant plus disponible, on reconstruit l'URL à partir des métadonnées locales de Drive for Desktop.

### Prérequis

- Google Drive for Desktop installé et synchronisé
- Fichier déjà présent dans le vault `H:\Drive partages\LBP - shared\Architecture data\`
- Fichier synchronisé (vérifier qu'il a bien remonté sur Drive)

### Étapes

**1. Identifier le user_id de Drive for Desktop**

Le dossier `C:\Users\leona\AppData\Local\Google\DriveFS\` contient un ou plusieurs sous-dossiers numérotés par user_id (ex: `101486418960336612156`). Celui qui est actif est celui dont les fichiers `mirror_metadata_sqlite.db-wal` ont une date de modification récente.

Pour Leonard, le user_id opérationnel est `101486418960336612156`.

**2. Lire la base SQLite `mirror_metadata_sqlite.db` (read-only)**

```python
import sqlite3
db_path = r"C:\Users\leona\AppData\Local\Google\DriveFS\101486418960336612156\mirror_metadata_sqlite.db"
conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
cursor = conn.cursor()
```

**3. Joindre `stable_parents` avec `items` pour filtrer le bon dossier parent (évite les doublons archive vs actif)**

```python
cursor.execute("""
    SELECT i.local_title, i.id FROM items i
    JOIN stable_parents sp ON i.stable_id = sp.item_stable_id
    WHERE i.local_title = ?
    AND sp.parent_stable_id = <stable_id_du_dossier_parent_actif>
    AND i.is_folder = 0
    AND i.trashed = 0
""", ("Manuel de BDD - Actifs.md",))
row = cursor.fetchone()
file_id = row[1] if row else None
```

**4. Construire l'URL Drive**

```
https://drive.google.com/file/d/{file_id}/view
```

### Points d'attention

- **Doublons via dossier archive** : un fichier qui a aussi une copie dans `00 - archives/` apparaît 2 fois dans la base. Filtrer par `parent_stable_id` du dossier actif pour éviter les faux positifs.
- **Caractères spéciaux** : les noms avec apostrophes typographiques (U+2019) ou tirets cadratins (U+2014) doivent être passés tels quels — pas d'échappement.
- **Batch** : pour un batch de N fichiers, faire une seule connexion SQLite avec une requête IN (...) plutôt que N connexions.

### Alternative si Drive MCP disponible
Utiliser `google-drive-search` avec filtre sur le nom, puis extraire le `web_view_link`.

---

## WF-012 : Indexer un doc Markdown dans sa BDD Notion

**Statut** : Actif (itéré au fil des batchs d'indexation)

### Contexte

Workflow type pour créer/mettre à jour une entrée Notion à partir d'un doc MD du vault. Applique les règles R-029 à R-038.

### Étapes

**1. Récupérer l'URL Drive du doc** (cf. WF-011)

**2. Vérifier si l'entrée Notion existe déjà**

Utiliser `notion-search` filtré par `data_source_url` de la BDD cible, chercher par nom ou code unique selon l'identifiant pivot du type d'objet (R-038 : taxonomies = code, autres = nom canonique).
- Si existe avec même code/nom → **mise à jour** (R-032, R-036)
- Si existe avec nom/code différent (v1 obsolète remplacé par v2) → **archiver v1 + créer v2**
- Si n'existe pas → **création**

**3. Lire le doc Markdown** (R-029 : doc = source de vérité)

Lire l'intégralité du doc pour pouvoir remplir les propriétés en cohérence (R-037).

**4. Lire la description de chaque propriété Notion** (R-033)

Via `notion-fetch` sur la data source, récupérer les contraintes de format/structure/valeurs.

**5. Dériver les propriétés** à partir du doc, en respectant les contraintes

- Nom canonique, Code unique, Statut, Domaines, etc.
- Pour les textes longs (Définition, Règles d'usage, Valeur ajoutée) : synthétiser depuis le doc sans inventer
- Pour les select/multi-select : utiliser uniquement les valeurs strictes autorisées

**6. Créer/mettre à jour l'entrée** (Passe 1, sans relations — R-034)

Utiliser `notion-create-pages` (création) ou `notion-update-page` (mise à jour). Si relations impossibles car cibles pas encore créées → **laisser vides pour l'instant**.

**7. Créer les relations** (Passe 2, R-034)

Une fois toutes les entrées du batch créées, les relier via `notion-update-page` avec le champ de relation rempli avec les URLs des pages cibles.

**8. Pour une note de concept : double indexation** (R-030)

Créer 1 entrée dans `Registre des notes de concept` + 1 entrée dans `Glossaire LBP`, avec **même Code unique** (R-031), et lier via `est documenté par (notes de concept)`.

**9. Archiver les v1 obsolètes**

Pour chaque entrée v1 remplacée, passer le Statut à `Archivé`.

**10. Vérifier et commit**

Vérifier que les entrées sont bien créées et reliées. Commit dans git (refs/ si règles capturées, ECOSYSTEM-STATE.md si état change).

### Points d'attention

- **Ordonnancement** : création avant relation (R-034)
- **Pas d'invention** : si une propriété ne peut pas être dérivée du doc → laisser vide (R-029)
- **Codes stables** : le Code unique ne change jamais (R-005), même sur une mise à jour
- **Descriptions = instructions** : les descriptions Notion sont les règles de remplissage (R-033)
- **QA anti-artefacts** : vérifier l'absence d'artefacts IA (R-039) avant publication
- **Identifiant pivot par type** : taxonomies = code, autres = nom canonique (R-038)

---

*Les autres workflows seront formalisés au fur et à mesure qu'on les pratiquera.*
