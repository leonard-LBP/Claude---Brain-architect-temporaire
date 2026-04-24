# Workflows documentes — Ecosysteme LBP

> Ce fichier recense les workflows formalises au fil du travail.
> Chaque workflow a un ID stable pour reference.
> Derniere mise a jour : 2026-04-24 — ajout WF-011 (Drive URL) + WF-012 (indexation Notion)

---

## Index

| ID | Workflow | Statut |
|----|----------|--------|
| WF-010 | Demarrage de session Claude (re-contextualisation) | Actif |
| WF-011 | Recuperer l'URL Drive d'un fichier local du vault | Actif |
| WF-012 | Indexer un doc Markdown dans sa BDD Notion | Actif (itere au fil des batchs) |
| WF-001 | Creer un nouveau doc Brain | A formaliser |
| WF-002 | Mettre a jour un doc Brain existant | A formaliser |
| WF-003 | Archiver un doc Brain (vault + Notion) | A formaliser |
| WF-008 | Propagation d'impacts apres modification | A formaliser |
| WF-009 | Migration d'une BDD XXX | A formaliser |

---

## WF-010 : Demarrage de session Claude

**Statut** : Actif

### Etapes

1. CLAUDE.md est lu automatiquement
2. memory/ est lu automatiquement
3. Si reprise de travail en cours → lire `refs/ECOSYSTEM-STATE.md`
4. Si besoin de contexte architecture → lire `refs/ARCHITECTURE-DIGEST.md`
5. Si operation prevue → consulter `refs/RULES_BRAIN_TWIN.md` et `refs/WORKFLOWS.md`
6. Initialiser TodoWrite si taches multiples

### Declencheur
Debut de chaque nouvelle conversation.

---

## WF-011 : Recuperer l'URL Drive d'un fichier local

**Statut** : Actif (decouvert 2026-04-24, mini-batch 0 Twin v2)

### Contexte

Les docs du vault Architecture data sont synchronises avec Google Drive via Drive for Desktop.
Pour indexer un doc dans Notion (R-029), il faut **l'URL Drive** a inscrire dans les proprietes
"Lien vers..." des BDD Brain. Le MCP Drive n'etant plus disponible, on reconstruit l'URL a
partir des metadonnees locales de Drive for Desktop.

### Prerequis

- Google Drive for Desktop installe et synchronise
- Fichier deja present dans le vault `H:\Drive partages\LBP - shared\Architecture data\`
- Fichier synchronise (verifier qu'il a bien remonte sur Drive)

### Etapes

**1. Identifier le user_id de Drive for Desktop**

Le dossier `C:\Users\leona\AppData\Local\Google\DriveFS\` contient un ou plusieurs sous-dossiers
numerotes par user_id (ex: `101486418960336612156`). Celui qui est actif est celui dont les
fichiers `mirror_metadata_sqlite.db-wal` ont une date de modification recente.

Pour Leonard, le user_id operationnel est `101486418960336612156`.

**2. Lire la base SQLite `mirror_metadata_sqlite.db` (read-only)**

```python
import sqlite3
db_path = r"C:\Users\leona\AppData\Local\Google\DriveFS\101486418960336612156\mirror_metadata_sqlite.db"
conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
cursor = conn.cursor()
```

**3. Joindre `item_properties` (local-title) avec `items` (id) pour recuperer le Drive file ID**

```python
cursor.execute("""
    SELECT i.id FROM item_properties ip
    JOIN items i ON ip.item_stable_id = i.stable_id
    WHERE ip.key = 'local-title' AND ip.value = ?
""", ("Manuel de BDD - Actifs.md",))
file_id = cursor.fetchone()[0]
```

**4. Construire l'URL Drive**

```
https://drive.google.com/file/d/{file_id}/view
```

### Points d'attention

- **Doublons** : si un fichier a ete rectifie (supprime + re-uploade), la base peut contenir
  **plusieurs entrees** (ancien + nouveau). Dans ce cas, prendre la plus recente (verifier
  par ordre d'insertion stable_id descendant, ou par timestamp si disponible).
- **Caracteres speciaux** : les noms avec apostrophes typographiques (U+2019) ou tirets
  cadratins (U+2014) doivent etre passes tels quels — pas d'echappement.
- **Batch** : pour un batch de N fichiers, faire une seule connexion SQLite avec une
  requete IN (...) plutot que N connexions.

### Alternative si Drive MCP disponible
Utiliser `google-drive-search` avec filtre sur le nom, puis extraire le `web_view_link`.

---

## WF-012 : Indexer un doc Markdown dans sa BDD Notion

**Statut** : Actif (itere au fil des batchs d'indexation)

### Contexte

Workflow type pour creer/mettre a jour une entree Notion a partir d'un doc MD du vault.
Applique les regles R-029 a R-034.

### Etapes

**1. Recuperer l'URL Drive du doc** (cf. WF-011)

**2. Verifier si l'entree Notion existe deja**

Utiliser `notion-search` filtre par `data_source_url` de la BDD cible, chercher par nom
ou code unique.
- Si existe avec meme code → **mise a jour** (R-032)
- Si existe avec nom/code different (v1 obsolete remplace par v2) → **archiver v1 + creer v2**
- Si n'existe pas → **creation**

**3. Lire le doc Markdown** (R-029 : doc = source de verite)

Lire l'integralite du doc pour pouvoir remplir les proprietes en coherence.

**4. Lire la description de chaque propriete Notion** (R-033)

Via `notion-fetch` sur la data source, recuperer les contraintes de format/structure/valeurs.

**5. Deriver les proprietes** a partir du doc, en respectant les contraintes

- Nom canonique, Code unique, Statut, Domaines, etc.
- Pour les textes longs (Definition, Regles d'usage, Valeur ajoutee) : synthetiser depuis
  le doc sans inventer
- Pour les select/multi-select : utiliser uniquement les valeurs strictes autorisees

**6. Creer/mettre a jour l'entree** (Passe 1, sans relations R-034)

Utiliser `notion-create-pages` (creation) ou `notion-update-page` (mise a jour).
Si relations impossibles car cibles pas encore creees → **laisser vides pour l'instant**.

**7. Creer les relations** (Passe 2, R-034)

Une fois toutes les entrees du batch creees, les relier via `notion-update-page` avec le
champ de relation rempli avec les URLs des pages cibles.

**8. Pour une note de concept : double indexation** (R-030)

Creer 1 entree dans `Registre des notes de concept` + 1 entree dans `Glossaire LBP`,
avec **meme Code unique** (R-031), et lier via `est documente par (notes de concept)`.

**9. Archiver les v1 obsoletes**

Pour chaque entree v1 remplacee, passer le Statut a `Archive`.

**10. Verifier et commit**

Verifier que les entrees sont bien creees et reliees. Commit dans git (refs/ si regles
capturees, ECOSYSTEM-STATE.md si etat change).

### Points d'attention

- **Ordonnancement** : creation avant relation (R-034)
- **Pas d'invention** : si une propriete ne peut pas etre derivee du doc → laisser vide (R-029)
- **Codes stables** : le Code unique ne change jamais (R-005), meme sur une mise a jour
- **Descriptions = instructions** : les descriptions Notion sont les regles de remplissage (R-033)

---

*Les autres workflows seront formalises au fur et a mesure qu'on les pratiquera.*
