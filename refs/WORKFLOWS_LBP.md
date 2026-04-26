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
| WF-013 | Générer un WR-RD à partir d'un Manuel de BDD | Actif (formalisé 2026-04-26 après 3 instanciations test) |

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

---

## WF-013 : Générer un WR-RD à partir d'un Manuel de BDD

**Statut** : Actif (formalisé 2026-04-26 après instanciation test de 3 WR-RD : Actifs, Pratiques organisationnelles, Journal des signaux)

### Contexte

Le WR-RD (Write Rules / Read Keys) est un précis champ par champ destiné aux agents qui lisent et écrivent dans une BDD du Twin. Il est strictement dérivé de la section 4 du manuel parent (D-014, D-016). Ce workflow décrit comment instancier ou re-générer un WR-RD en respectant les règles R-041 (propagation manuel → WR-RD) et R-042 (QA stricte d'égalité).

### Prérequis

- Manuel de BDD parent existant et stabilisé (au moins en version v0.X.Y avec section 4 renseignée).
- Template `Template - WR-RD - Digital Twin.md` (v1.2.0+) accessible dans `00 - Docs méta/Templates d'instanciation/`.
- Sous-dossier `WR-RD/` créé dans le groupe BDD cible (`Manuels de BDD/{Brain,Digital Twin,Mission Ops}/WR-RD/`).

### Étapes

**1. Lire intégralement la section 4 du manuel parent**

Identifier les sous-sections renseignées (4.1 Génériques, 4.2 Spécifiques, 4.3 Relations + jumelles + rollups, 4.4 Couche 5D, 4.5 Couche calculée). Repérer celles qui sont vides ou marquées comme non applicables (ex : "Aucune propriété native de formule locale n'est définie").

**2. Préparer le frontmatter**

Selon le modèle FRONTMATTER_INSTANCE du Template WR-RD :
- `target_bdd_canonical_name` = nom canonique exact de la BDD (depuis le frontmatter du manuel parent)
- `target_bdd_code` = `DBMAN_[NOM_TOKEN]` (format underscore, MAJUSCULES, depuis le manuel)
- `parent_manual` = `Manuel de BDD - [Nom de la BDD].md` (nom de fichier exact)
- `wr_rd_code` = `WRRD_[NOM_TOKEN]` (token aligné avec le manuel)
- `domain` = "Digital Twin" / "Brain" / "Mission Ops"
- `version` = "0.1.0" pour première instanciation
- `template_version` = version du template (ex: "1.2.0")
- `created_at` = date ISO YYYY-MM-DD

**3. Projeter chaque sous-section 4.X dans la section X correspondante du WR-RD**

Mapping fixe :
- 4.1 Propriétés génériques → 1) Propriétés génériques
- 4.2 Propriétés spécifiques → 2) Propriétés spécifiques
- 4.3 Relations + jumelles textes + rollups relationnels → 3) Relations + jumelles textes + rollups relationnels
- 4.4 Couche 5D → 4) Couche 5D
- 4.5 Couche calculée → 5) Couche calculée

Pour chaque ligne du tableau de la sous-section du manuel, extraire **strictement** les 9 colonnes retenues, dans l'ordre fixe :
1. Champ
2. Type
3. Taxonomie(s) — codes
4. Cardinalité / multiplicité
5. Forme logique attendue
6. Instructions d'écriture
7. Clefs de lecture
8. Utilité pour le Digital Twin
9. Exemples

**Colonnes à NE PAS reprendre** (D-016) : Portée, Nature de production, Prérequis (Must / Should / Nice).

**4. Si la BDD n'a pas de couche 5D ou pas de couche calculée native, supprimer la section correspondante**

Au lieu de produire un tableau vide. Optionnellement, ajouter une note brève en fin de doc expliquant pourquoi la section a été supprimée.

**Exemple** (Journal des signaux V1) : section 5 supprimée + note `> La BDD Journal des signaux n'a pas de couche calculée native (pas de propriété de formule locale en V1). La couche calculée est ici portée par les rollups relationnels de la section 3.`

**5. QA stricte d'égalité (R-042)**

Avant tout commit, vérifier cellule par cellule l'**égalité mot pour mot** entre le WR-RD et la section 4 du manuel parent sur les 9 colonnes retenues. Tolérances admises : adaptations typographiques liées au rendu Markdown (apostrophe droite vs typographique selon contexte). Aucun reformulation éditoriale ne doit être introduite dans le WR-RD.

**6. QA anti-artefacts (R-039)**

Vérifier l'absence d'artefacts IA dans le doc final (`:contentReference[oaicite:N]{index=N}`, `[citation:N]`, texte tronqué, placeholders non résolus).

**7. Mettre à jour la fiche Notion correspondante dans la BDD "Manuels de BDD"**

Renseigner la propriété **`Lien vers le doc WR-RD (.md)`** (URL Drive du fichier .md du WR-RD) sur la fiche Notion correspondant au manuel parent. Workflow WF-011 pour récupérer l'URL Drive.

**8. Vérifier et tracer**

- Le WR-RD est-il bien dans `Manuels de BDD/{Domain}/WR-RD/` ? (D-014)
- Le frontmatter est-il complet et conforme ?
- Les 5 sections (ou subset) sont-elles correctes ?
- La fiche Notion du manuel pointe-t-elle vers le WR-RD ?

Tracer dans `ECOSYSTEM-STATE.md` (journal de session) la création/mise à jour du WR-RD avec sa version.

### Cas particulier : mise à jour d'un WR-RD existant après modification du manuel parent (R-041)

1. Identifier la modification dans le manuel parent (ajout, suppression, modification de propriété en section 4).
2. Reporter strictement la modification dans le WR-RD (colonnes retenues uniquement).
3. Bumper la version du WR-RD (ex : v0.1.0 → v0.2.0).
4. Si le template a évolué entretemps, mettre à jour `template_version`.
5. Re-passer la QA stricte (R-042) puis QA anti-artefacts (R-039).
6. Mettre à jour la propriété Notion `Lien vers le doc WR-RD (.md)` si l'URL Drive a changé (rare).

### Points d'attention

- **Pas de réinterprétation** : le WR-RD n'est jamais le lieu d'une amélioration éditoriale ; toute amélioration passe par le manuel parent (R-041, R-042).
- **Sections conditionnelles** : supprimer plutôt que produire des tableaux vides (préserve la lisibilité côté agent).
- **Codes alignés** : `WRRD_X` aligné avec `DBMAN_X` (token en miroir).
- **Naming fichier** : `WR-RD - [Nom de la BDD].md` strict (miroir de `Manuel de BDD - [Nom de la BDD].md`).
- **Frontières** (D-016) : pas de section maintenance, doctrine, articulation autres docs, ni historique de version au-delà du frontmatter.

### Articulation avec d'autres règles et workflows

- **R-041** : propagation Manuel → WR-RD obligatoire.
- **R-042** : QA stricte d'égalité WR-RD ↔ Manuel section 4.
- **R-039** : QA anti-artefacts IA.
- **D-014** : colocalisation WR-RD avec leur manuel parent.
- **D-016** : rôle, contenu et format des WR-RD.
- **WF-011** : récupérer l'URL Drive du fichier .md du WR-RD pour la propriété Notion.

---

*Les autres workflows seront formalisés au fur et à mesure qu'on les pratiquera.*
