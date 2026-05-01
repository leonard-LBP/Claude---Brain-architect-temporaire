---
# === Identité ===
title: "Workflows LBP — Catalogue des workflows opérationnels"
doc_type: doc_meta
code: "CHRT_WORKFLOWS_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
created_at: "07-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Catalogue des 17 workflows opérationnels (WF-XXX) intrinsèques à l'écosystème LBP : récupération URL Drive (WF-011), indexation Notion (WF-012), génération WR-RD (WF-013), génération BDD (WF-014), migration au canon (WF-015), audit transverse (WF-016), sync DDL (WF-017), propagation d'impacts (WF-008), etc."
purpose: "Référence canonique pour conduire des opérations standardisées sur l'écosystème. Chaque workflow a un ID stable, un statut (Actif / À formaliser), un contexte, des étapes, des règles associées."
tags:
  - doc_meta
  - workflows
  - catalogue
  - operations
  - brain
  - digital_twin
  - mission_ops
  - lbp
---

# Workflows LBP — Brain / Twin / Mission Ops

> **Scope** : 🟦 LBP — Bundle écosystème.
> Ce fichier recense les workflows opérationnels intrinsèques à l'écosystème LBP (Brain, Digital Twin, Mission Ops). Il a vocation à être consommé par les agents et humains LBP (consultants, twin architect, brain architect) pour conduire des opérations standardisées sur l'écosystème.
> Les workflows propres à notre collaboration Claude (démarrage de session, etc.) sont dans `SESSION_WORKFLOWS.md`.
> Chaque workflow a un ID stable pour référence.
> Dernière mise à jour : 30-04-2026 — formalisation WF-008 (propagation d'impacts après modification).

---

## Index

| ID | Workflow | Statut |
|----|----------|--------|
| WF-011 | Récupérer l'URL Drive d'un fichier local du vault | Actif |
| WF-012 | Indexer un doc Markdown dans sa BDD Notion | Actif (itéré au fil des batchs) |
| WF-001 | Créer un nouveau doc Brain | À formaliser |
| WF-002 | Mettre à jour un doc Brain existant | À formaliser |
| WF-003 | Archiver un doc Brain (vault + Notion) | À formaliser |
| WF-008 | Propagation d'impacts après modification d'un doc/objet de l'écosystème | Actif (formalisé 30-04-2026) |
| WF-009 | Migration d'une BDD XXX | À formaliser |
| WF-013 | Générer un WR-RD à partir d'un Manuel de BDD | Actif (formalisé 26-04-2026 après 3 instanciations test ; applicable au Brain dès création de `Template - WR-RD - Brain.md`) |
| WF-014 | Générer une BDD Twin sur Notion à partir de son Manuel | Actif (cadrage 26-04-2026, Phase 6.5) |
| WF-015 | Migration au canon d’un type de doc Brain (frontmatter R-054 / R-055 / R-056) | Actif (formalisé 28-04-2026 après Phases 4-7) |
| WF-016 | Audit transverse Notion ↔ Manuels Brain | Actif (formalisé 28-04-2026) |
| WF-017 | Sync DDL Notion BDD Brain à partir des écarts d’audit | Actif (formalisé 28-04-2026) |

---

## WF-011 : Récupérer l'URL Drive d'un fichier local

**Statut** : Actif (découvert 24-04-2026, mini-batch 0 Twin v2)

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

## WF-008 : Propagation d'impacts après modification d'un doc/objet de l'écosystème

**Statut** : Actif (formalisé 30-04-2026)

### Contexte

L'écosystème LBP est constitué de docs Markdown qui se citent et se propagent entre eux selon des règles strictes (R-001 source de vérité Markdown, R-041/R-042 propagation Manuel↔WR-RD, R-029 indexation Notion, R-031 paire `CPT/GLO`, R-053 archivage). Toute modification d'un doc structurant peut déclencher des **cascades obligatoires** que ce workflow rassemble en un seul pas-à-pas.

**Principe directeur** : la propagation est **strictement descendante** (du doc source vers ses dérivés). Un dérivé ne corrige jamais en remontant — toute amélioration éditoriale repasse par le doc parent (R-041, R-042).

### Cartographie des chaînes de propagation

```
[Source de vérité Markdown]
        │
        ├── Manuel de BDD ─→ WR-RD (section 4 → sections 1-5) ─→ Fiche Notion `Manuels de BDD` (lien WR-RD)
        │
        ├── Taxonomie .md ─→ Manuels qui la référencent (Section "Usages") ─→ WR-RD ─→ Notion (options select/multi-select)
        │
        ├── Template d'instanciation ─→ Toutes les instances qui l'utilisent (frontmatter + structure)
        │
        ├── Note de concept ─→ Glossaire LBP Notion + Registre des notes de concept Notion (paire CPT/GLO)
        │
        ├── Règle R-XXX (RULES_LBP) ─→ Docs concernés (manuels, WR-RD, templates) si la règle change un format
        │
        └── Décision D-XXX (DECISIONS_LBP) ─→ Mise à jour des règles R impactées + manuels concernés + ECOSYSTEM-STATE
```

### Étapes (workflow générique en 7 phases)

#### Phase 1 — Identifier le **type de modification** et le **doc source**

Avant de propager, classer la modification :
- **Format** : changement de structure (frontmatter, sections, naming) → cascade large
- **Contenu** : changement de wording dans un champ existant → cascade ciblée (souvent juste WR-RD ou Notion)
- **Codification** : changement de code d'identification → cascade de tous les renvois (cf. WF étape de renames)
- **Statut / archivage** : passage à archivé → propagation Notion + nettoyage des renvois

#### Phase 2 — Cartographier les **dérivés directs** du doc source

Selon le type de doc modifié, lister les dérivés à mettre à jour :

| Doc source modifié | Dérivés directs à propager | Règle |
|---|---|---|
| **Manuel de BDD** (section 4) | WR-RD du même nom | R-041, R-042 |
| **Manuel de BDD** (frontmatter / autres sections) | Fiche Notion `Manuels de BDD` (lien Drive, version, statut) | R-029, D-020 |
| **WR-RD** (modification non triviale) | ⚠️ INTERDIT — repasser par le manuel parent | R-041 (interdiction propagation remontante) |
| **Taxonomie .md** (valeurs canoniques) | (a) Manuels référençant la taxo (section "Usages des taxonomies") + (b) Notion DDL : ALTER options select/multi-select de toutes les BDDs concernées + (c) WR-RDs si la valeur impacte une instruction d'écriture | R-049, WF-017 |
| **Template d'instanciation** | Toutes les instances existantes utilisant ce template (ré-évaluation au cas par cas) | R-056 (versioning), C-019 |
| **Note de concept** (frontmatter) | Glossaire LBP Notion + Registre des notes de concept Notion | R-029, R-031 |
| **Note de concept** (corps) | Lien Drive Notion uniquement (pas le contenu — Notion = miroir) | R-001, R-029 |
| **Règle R-XXX** (création / modification) | RULES_LBP.md + ECOSYSTEM-STATE + docs concernés si format-impactant | R-001, C-007 |
| **Décision D-XXX** | DECISIONS_LBP.md + RULES_LBP si dérivation R + ECOSYSTEM-STATE | R-001, C-007 |
| **Convention session C-XXX** | CLAUDE.md + ECOSYSTEM-STATE | C-006 |

#### Phase 3 — Propager **dans l'ordre strict** des dérivés

Important : ne jamais sauter d'étape, ne jamais réordonner.

1. **Markdown d'abord** : le doc dérivé Markdown (WR-RD, manuel impacté, template) est mis à jour avec QA stricte (R-042 pour WR-RD).
2. **Versions bumpées** : si le contenu structurant change (R-056), bumper la version du dérivé. Mettre à jour `updated_at` dans le frontmatter.
3. **Notion ensuite** : une fois le Markdown stable, aligner Notion (DDL si schéma, propriétés textuelles si contenu).
4. **Renvois croisés** : si le doc modifié est cité ailleurs (autres docs Markdown, ECOSYSTEM-STATE, CLAUDE.md), grep + remplacement systématique (cf. patterns rename Étape 2 bundle docs méta).

#### Phase 4 — QA après propagation

- **WR-RD** : appliquer R-042 (égalité mot pour mot des 9 colonnes retenues avec section 4 du manuel parent).
- **Notion** : re-fetch et comparer avec le manuel (WF-016 audit transverse).
- **Renvois** : `grep -r "ancien_nom"` doit renvoyer 0 match (sauf dans archives explicites).
- **Cohérence narrative** : relire le doc parent et son dérivé pour vérifier qu'aucune incohérence sémantique n'a été introduite.

#### Phase 5 — Annonce explicite C-009

Si la modification touche un Manuel et son WR-RD : **annoncer explicitement** dans la même réponse :
> ✓ Manuel modifié : X manuel(s) · ✓ Propagation WR-RD : Y WR-RD mis à jour

Ou explicitement « WR-RD non concerné car ... » (C-009). Sans cette annonce, la propagation est considérée non vérifiable.

#### Phase 6 — Tracer dans ECOSYSTEM-STATE.md

Mise à jour systématique du journal vivant (C-011) :
- « Dernière mise à jour » avec date du jour
- Section « Phase actuelle » si phase notable
- Section « État du Brain » si volumétrie change
- Pas de batch — un commit ECOSYSTEM-STATE par phase de propagation (C-011)

#### Phase 7 — Commit + push (C-013)

- Commit avec message explicite : `[Domain] [Action] [Volume] — propagation [doc source] → [dérivés]`
- Push immédiat dans la même réponse (C-013)
- Annoncer : « ✓ Push : N commit(s) poussé(s) sur origin/master »

### Cas particuliers et edge cases

#### Cas 1 — Modification de codification (R-054)

Si on change un code stable (ex : `CPT_X` → `CPT_Y`), ce n'est jamais une modification simple : c'est un **archivage de l'ancien + création du nouveau** (R-053).

1. Archiver l'ancienne entrée Notion (Statut → Archivé), pas de suppression
2. Créer la nouvelle entrée avec le nouveau code
3. Propager les renvois (grep + remplacement, cf. Étape 2 bundle docs méta)
4. Si paire `CPT/GLO` (R-031), propagation aux 2 entrées Notion en miroir

#### Cas 2 — Modification d'une taxonomie (cascade large)

Une taxo est référencée par N manuels et M propriétés Notion. La propagation est :
1. Mettre à jour la taxo `.md` (source de vérité) + Notion BDD `Registre des taxonomies` (lien Drive, version)
2. Identifier les manuels qui la référencent (relation `utilise (taxonomies)`)
3. Pour chaque manuel : mettre à jour la section "Usages des taxonomies" + propager au WR-RD si applicable
4. Pour chaque BDD Notion qui utilise la taxo : ALTER options select (WF-017)
5. Annoncer le volume total : « Taxo X mise à jour → N manuels + M BDDs Notion alignés »

#### Cas 3 — Modification d'un template d'instanciation (cascade très large)

Un bump majeur de template (X.Y → (X+1).0) ne propage pas automatiquement à toutes les instances. Au lieu de cela :
1. Mettre à jour le template (source de vérité dans `00 - Docs méta/Templates d'instanciation/`)
2. Mettre à jour la propriété Notion `Version du template` sur la fiche du template (D-020)
3. **Marquer les instances comme stale** : audit mécanique des docs `.md` instances ayant un `template_version` inférieur (D-020)
4. Planifier une phase de migration des instances (WF-015 si applicable)
5. **Ne pas propager dans l'urgence** — c'est un chantier dédié

#### Cas 4 — Modification d'une règle R-XXX qui change un format

Cas le plus délicat : si R-052 (apostrophes typographiques) change, des dizaines de docs sont concernés.

1. Mettre à jour la règle dans RULES_LBP.md (source)
2. Identifier l'ensemble impacté (grep sur les caractères concernés ou pattern)
3. Lancer un **WF-015** (migration au canon) si le pattern est massif
4. Si le pattern est ciblé : propagation manuelle doc par doc avec QA

### Anti-patterns à éviter

- ❌ Propager Notion → Markdown (viole R-001)
- ❌ Modifier un WR-RD pour corriger une coquille au lieu de remonter au manuel (viole R-041)
- ❌ Sauter la phase ECOSYSTEM-STATE (viole C-011)
- ❌ Propagation silencieuse sans annonce C-009 (manuel ↔ WR-RD)
- ❌ Commit local sans push (viole C-013)
- ❌ « Batch » de plusieurs phases en un seul commit ECOSYSTEM-STATE (perte de traçabilité incrémentale, C-011)

### Articulation avec autres workflows

- **WF-011** : récupérer URL Drive pour propager dans Notion
- **WF-012** : indexer un doc dans sa BDD Notion (utilisé en Phase 3 de WF-008)
- **WF-013** : générer/régénérer un WR-RD (cascade Manuel → WR-RD)
- **WF-016** : audit transverse Notion ↔ Manuels (utilisé en Phase 4 QA)
- **WF-017** : sync DDL Notion (utilisé en Phase 3 pour les changements DDL)

### Règles fondatrices

- **R-001** : source de vérité = Markdown
- **R-041** : propagation Manuel → WR-RD obligatoire
- **R-042** : QA stricte d'égalité WR-RD ↔ Manuel
- **C-009** : annonce explicite de la propagation Manuel ↔ WR-RD
- **C-011** : mise à jour systématique de ECOSYSTEM-STATE
- **C-013** : push systématique après commit

---

## WF-013 : Générer un WR-RD à partir d'un Manuel de BDD

**Statut** : Actif (formalisé 26-04-2026 après instanciation test de 3 WR-RD : Actifs, Pratiques organisationnelles, Journal des signaux)

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

## WF-014 : Générer une BDD Twin sur Notion à partir de son Manuel

**Statut** : Actif (cadrage 26-04-2026, Phase 6.5 — préparation génération des 28 BDD Twin v2). **Révisé 27-04-2026 (WF-014 v3)** : 3 passes globales séparées (natives → relations → rollups). Ce découplage évite la pollution croisée des BDD par les miroirs créés trop tôt (cf. R-047 v2.2 justification).

### Contexte

Générer une BDD du Digital Twin sur Notion à partir de son manuel parent (source de vérité, R-045). Le manuel contient toute la spécification : propriétés génériques, spécifiques, 5D, relations, rollups, taxonomies référencées. Ce workflow s'applique à **chaque BDD individuellement**, mais quand on génère un ensemble cohérent (les 28 BDD Twin v2), il s'orchestre sous une boucle de phases globales pour respecter R-046 (relations bidirectionnelles → impossible avant que les 2 BDD existent ; rollups → impossible avant que les relations existent).

### Étapes (mode batch sur N BDD)

#### Phase 0 — Cadrage
1. Identifier la page hôte Notion (où les BDD seront posées en pleine page).
2. Confirmer le périmètre des BDD à générer (ex. les 28 manuels Twin v2).
3. Vérifier que les manuels parents sont à jour et conformes (R-027 naming, R-042 alignement WR-RD).

#### Phase 1 — Extraction du manifest
1. Pour chaque manuel, parser la section 4 (`4.1` à `4.5`) en JSON structuré :
   - `properties.natives` : type, taxonomie référencée, ordre, bloc d'ordering (R-047)
   - `properties.relations` : BDD cible, propriété miroir, jumelle texte associée, monodirectionnelle ? (cas `Sources d'informations`)
   - `properties.rollups` : relation source, propriété cible, agrégation
2. Pour chaque taxonomie référencée, lire le `.md` correspondant dans `Taxonomies/` et extraire les valeurs canoniques (codes + libellés). Gestion `Niveau: category` (5 dims pour ORG5D) vs `Niveau: taxon` (10 sous-dims pour ORG5D).
3. Validation interne du manifest :
   - Toute relation bidirectionnelle référence une BDD cible présente dans le manifest et a une propriété miroir cohérente côté cible.
   - Tout rollup référence une relation source qui existe dans la BDD courante.
   - Toute taxo référencée existe et a au moins une valeur extraite.

#### Phase 2 — Création des BDD vides
1. Créer N BDD pleine page sous la page hôte, **avec uniquement le titre** (R-048 : nom canonique simple).
2. Stocker l'ID Notion de chaque BDD créée pour usage ultérieur (relations + rollups).

#### Passe 1 — Schéma natif (toutes les BDD, props non-relationnelles)
> **Révision WF-014 v3 (27-04-2026, après pilote Actifs)** : la Passe 1 du v2 fusionnait natives + relations en une seule salve par BDD. Cela créait des miroirs prématurés sur les autres BDD (avant que leurs propres natives soient créées), cassant leur ordering. Solution v3 : **3 passes globales séparées**. Passe 1 = natives **sans relations** sur toutes les 28 BDD ; Passe 2 = relations bidir sur toutes les 28 BDD ; Passe 3 = rollups.

Pour chaque BDD, exécuter une salve unique `update_data_source` avec les statements ADD COLUMN dans cet ordre R-047 v2 strict :

1. **Bloc 1 — Tête** (5 props, ordre fixe) :
   `Nom` (title, déjà créé en Phase 2) · `Statut de l'objet` (select OBJ.STATUT.LBP) · `Aliases` · `Erreurs de transcription` (si dans le manuel) · `Description`

2. **Bloc 2 — Corpus métier** :
   - **2a. Spécifiques** (4.2)
   - **2b. 5D regroupée** (4.4 — natives + jumelles 5D si existent)
   - **2c. Jumelles textes seules** (4.3 — RICH_TEXT, **sans les relations**)
   - **2d. Calculés natifs** (4.5 hors rollups) — formules locales. Différé si Leonard valide.

3. **Bloc 3 — Queue gestion** (~11-12 props, ordre fixe) :
   `Lien vers la note avancée` (URL, conditionnelle, R-050) · `Exemples concrets` · `Commentaires libres` · `Notes du consultant` · `Confidentialité (option)` (si applicable) · `Indices observés` · `Indices d'existence de l'objet` · `Created Date` (CREATED_TIME native renommée) · `Last Updated Date` (LAST_EDITED_TIME native renommée) · `Logs / Révisions LBP` · `Merge Notes` · `Merge Flags`

4. **Bloc 4 — Sources textuelles** (1 prop) :
   `Source(s) d'information (texte)` (RICH_TEXT). La relation monodirectionnelle `Source(s) d'information` est différée (création de la BDD `Sources d'informations` plus tard sur la même page Notion).

**Pour les select/multi-select avec taxo** : peupler les options à la création (libellés Notion + couleurs depuis le manifest taxos).

#### Passe 2 — Relations bidirectionnelles (toutes BDD, après Passe 1 globale)
> Les relations sont créées **après** que les 28 BDD ont leurs schémas natifs propres. Notion crée alors automatiquement les miroirs côté BDD cibles, mais leur position en bout de schéma est cohérente (Bloc 7 — Miroirs reçus de R-047 v2.2).

1. Pour chaque BDD, exécuter une salve `update_data_source` avec les ADD COLUMN relations bidir :
   - Syntaxe : `RELATION('target_ds_id', DUAL 'mirror_name' 'mirror_id')` (DUAL = bidirectionnelle)
   - Pas la relation mono `Source(s) d'information` (différée).
2. QA après Passe 2 : pour chaque relation bidir, vérifier le miroir côté cible (nom + cardinalité conformes au manuel).

**Pour les sandboxes (R-014)** : Passe 2 quasi-vide (sauf relation Sources d'informations qui sera mono, créée plus tard).

#### Passe 3 — Rollups (toutes BDD, après Passe 2 globale)
> Les rollups dépendent des relations sources + des propriétés cibles côté BDD cible. Comme les Passes 1 + 2 ont peuplé toutes les BDD, on peut créer les rollups sans risque de référence vide. Ils sont ajoutés en **queue du schéma** (Bloc 6 R-047 v2.2), sémantiquement défendable comme couche calculée dérivée.

1. Pour chaque BDD, exécuter une salve `update_data_source` avec les ADD COLUMN ROLLUP :
   - Syntaxe : `ROLLUP('source_relation', 'target_property', 'function')`
2. QA après Passe 3 : pas d'erreur "propriété cible introuvable".

#### Passe finale — Sources d'informations + Calculés natifs différés
1. Créer la BDD `Sources d'informations` sur la même page Notion (section Mission Ops).
2. Ajouter sur chaque BDD Twin la relation mono `Source(s) d'information` vers la BDD Sources d'informations.
3. Si les formules ont été différées, les ajouter (queue de schéma, acceptable).

#### QA finale par BDD
1. Nombre de propriétés cohérent avec le manuel.
2. Toutes les options taxos peuplées correctement (libellés + couleurs).
3. Aucune propriété "fantôme" (créée par Notion à la volée, non documentée dans le manuel).
4. Mettre à jour la fiche du Manuel correspondant dans la BDD `Manuels de BDD` Notion : renseigner `Lien vers la BDD Notion` (URL de la nouvelle BDD).

### Notes opérationnelles

- **Idempotence** : le manifest est l'artefact de référence. Si on doit recommencer un batch, on rejoue le même manifest (versionable).
- **Rollback** : sur la page test, on peut détruire et recréer. À ne pas faire sur des BDD contenant déjà des données.
- **Ordre intra-Phase 2** : peu importe pour les BDD vides, mais pour la lisibilité on suit l'ordre fonctionnel (socle structurel d'abord, puis extraction → analytique → sandboxes).
- **Sandboxes** : Phase 4 et 5 sont quasi-vides pour les sandboxes (R-014 : pas de relations réelles sauf `Sources d'informations`).
- **Taxo ORG5D.DIM.LBP** : 5 dimensions au niveau `category`, 10 sous-dimensions au niveau `taxon` (2 sous-dims par dim).

### Règles et décisions liées

- **R-045** : source = manuel parent.
- **R-046** : ordre de création (DBs → props → relations → rollups → ordering).
- **R-047** (v2.2, 27-04-2026) : convention d'ordering en **7 blocs**, jumelles textes (Bloc 2c) et relations (Bloc 5) découplées en passes séparées pour préserver l'ordering global des 28 BDD (contrainte Notion DDL : pas de réordonnancement, et création d'une relation bidir crée automatiquement le miroir côté cible).
- **R-048** : naming BDD = nom canonique simple.
- **R-014** : sandboxes — pas de relations réelles sauf Sources.
- **R-019** : architecture en 5 couches d'une BDD bien spécifiée.

---

## WF-015 : Migration au canon d’un type de doc Brain (frontmatter R-054 / R-055 / R-056)

**Statut** : Actif (formalisé 28-04-2026 après Phases 4 à 7 — 318 docs migrés).

### Contexte

Migrer un lot homogène de docs Brain (manuels, WR-RD, notes de concept, instances de templates, etc.) au canon frontmatter : codification universelle (R-054 — préfixes `CPT_`, `GLO_`, `METH_`, `TPL_BRICK_`, `CHRT_`, `DBMAN_TW/MO/BR_`, `WRRD_TW/MO/BR_`, `LGBLK_`, `PRMPT_M/S/U/T_`, `OUT_`, `AGT_`… cf. `CODIFICATION_LBP.md`), 3 zones balisées (R-055 — Identité / Méta-gouvernance / Spec d’usage), versioning `X.Y` sans PATCH (R-056).

### Méthode (pattern script idempotent)

**1. Inventaire** — lister tous les docs du type cible (glob sur le dossier ou liste explicite).

**2. Parse frontmatter** — pour chaque doc : lire le frontmatter YAML, extraire l’état actuel.

**3. Calcul du frontmatter cible** — appliquer les règles :
- Génération du `code` selon R-054 (préfixe + token MAJUSCULES_UNDERSCORE).
- Réorganisation en 3 zones (R-055).
- Normalisation du `version` en `X.Y` (R-056). Si forme legacy `"DATE vX.Y.Z"` détectée : split en `version` + `created_at`.
- Normalisation des dates en `JJ-MM-YYYY` (R-044).
- Normalisation des apostrophes en typographiques `’` (R-052) dans les chaînes de description.

**4. Mode `--dry-run`** — produire un rapport diff par doc (avant / après) sans écrire. Permet revue avant application.

**5. Mode `--apply`** — écrire les frontmatters normalisés. Idempotent : un second passage ne doit produire aucun diff.

**6. QA post-migration** — re-lire un échantillon, vérifier la conformité aux 3 règles. Vérifier l’absence d’artefacts.

**7. Commit unifié** — un commit par phase de migration, message clair (volume + type cible).

### Volumes de référence (Phases 4-7)

| Phase | Type | Volume |
|---|---|---|
| 4 | Manuels de BDD | 43 |
| 5 | WR-RD | 32 |
| 6 | Notes de concept | 72 (split anti-pattern `version` géré) |
| 7 | Instances (Templates de Bricks + Méthodes + Doc méta) | 24 |

### Out of scope

- Logic Blocks (101) + Prompts (76) : différés en Phase 7 bis car obsolètes vs Twin v2 (refonte/regen plus que migration).

---

## WF-016 : Audit transverse Notion ↔ Manuels Brain

**Statut** : Actif (formalisé 28-04-2026 — rapport de référence : `scripts/notion_brain_audit/audit_notion_brain.md`).

### Contexte

Vérifier que les 11 BDDs Brain Notion sont alignées avec leurs manuels parents (section 4 du manuel = vérité, R-045). Produit un rapport d’écarts qui alimente WF-017 (sync DDL).

### Méthode

**1. Fetch des 11 data sources Notion** — via `mcp__...__notion-fetch` sur chaque BDD Brain : récupérer la liste exhaustive des propriétés (nom, type, options pour les select/multi-select).

**2. Parse de la section schéma de chaque manuel parent** — lire la ou les sections du manuel qui décrivent les propriétés Notion attendues (génériques, spécifiques, relations, rollups, taxonomies référencées).

**3. Comparaison ligne à ligne** — pour chaque propriété attendue côté manuel, vérifier sa présence côté Notion (nom exact, type exact, options exactes pour les select). Pour chaque propriété présente côté Notion, vérifier qu’elle est documentée dans le manuel.

**4. Classification des écarts** :
- **MANQUE** : présent manuel, absent Notion → ADD à prévoir.
- **OBSOLÈTE** : présent Notion, absent manuel → DROP à prévoir.
- **MISMATCH TYPE** : type différent → CONVERT à prévoir (ex : text → rollup).
- **MISMATCH OPTIONS** : valeurs select divergentes → ALTER à prévoir.
- **CASSE / TYPO / ACCENTS** : nom différent à la marge → RENAME à prévoir.
- **JUMELLE TEXTE INTERDITE (R-058)** : DROP à prévoir.

**5. Rapport markdown par BDD** — score (Conforme / Mineur / Majeur / Critique) + liste des écarts classés + recommandations DDL.

**6. Synthèse transverse** — tableau récap des 11 BDDs, total d’actions DDL nécessaires.

### Application 28-04-2026

11 BDDs auditées, ~26 actions DDL identifiées et appliquées via WF-017.

---

## WF-017 : Sync DDL Notion BDD Brain à partir des écarts d’audit

**Statut** : Actif (formalisé 28-04-2026 — appliqué sur les 11 BDDs Brain).

### Contexte

Appliquer sur Notion les actions DDL identifiées par WF-016. Limitation Notion API : pas de réordonnancement après création, donc l’ordre d’ajout matter. Pas de description sur les nouvelles propriétés via DDL (à compléter à la main).

### Pattern d’actions DDL

| Action | Quand | Exemple |
|---|---|---|
| **DROP** | Propriété obsolète (ex : `actif` Prompts), redondante (ex : `Type fonctionnel (BDD décrite)` Manuels — D-019), interdite (jumelles texte Logic blocks — R-058) | DROP `actif` |
| **ADD select / multi-select** | Propriété manquante avec taxo | ADD `Domaine(s) d’usage` multi-select avec 4 options (Core / Motor / Digital Twin / Mission Ops) |
| **ADD url** | Lien source manquant | ADD `System prompt (lien source)` URL (Agents LBP) |
| **ALTER options** | Valeurs select divergentes ou casse à harmoniser | ALTER `Statut de déploiement` (5 valeurs `PROMPT.DEPLOY_STATUS`), harmonisation casse `Domaine(s) d’usage` |
| **RENAME** | Casse / accents / apostrophes (R-052 / R-044 / typo) | `Statut de l'objet` → `Statut de l’objet` ; `Valeur ajoutee` → `Valeur ajoutée` ; `Entrees attendues` → `Entrées attendues` |
| **CONVERT text → rollup** | Champ texte à transformer en rollup via une relation existante | 8 conversions (Méthodes 2, Templates 2, Agents 4) |
| **CREATE rollup** | Rollup manquant alors que la relation source existe | 3 rollups Outils externes (Agents/Méthodes/Templates mobilisés via prompts) |

### Étapes

**1. Préparer le batch DDL par BDD** depuis le rapport d’audit (WF-016).

**2. Gérer les taxos vides** — si une option select doit être ajoutée mais la taxo Notion est vide, peupler les options à partir du manifest taxos (libellés + couleurs depuis le `.md` de la taxo dans `Taxonomies/`).

**3. Exécuter via `notion-update-data-source`** — une salve par BDD, opérations groupées dans l’ordre :
   1. RENAME (préparation)
   2. DROP (nettoyage)
   3. ALTER options (correction)
   4. ADD natives (compléments)
   5. CONVERT / CREATE rollups (couche dérivée — nécessite que les relations sources existent)

**4. Vérification post-DDL** — re-fetch la data source, comparer avec le manuel parent. Score doit être Conforme.

**5. Compléter les descriptions à la main** (limite API Notion) — pour les propriétés ajoutées, écrire la description sur la fiche Notion.

**6. Tracer dans ECOSYSTEM-STATE.md** — chronologie des actions par BDD.

### Application 28-04-2026

~26 actions DDL appliquées sur les 11 BDDs Brain. Toutes les BDDs en Conforme post-sync.

---

*Les autres workflows seront formalisés au fur et à mesure qu'on les pratiquera.*
