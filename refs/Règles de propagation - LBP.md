---
# === Identité ===
title: "Règles de propagation - LBP"
doc_type: doc_meta
code: "META_PROPAGATION_RULES_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "TPL_META_CATALOGUE"
template_version: "1.6"
created_at: "03-05-2026"
updated_at: "03-05-2026"

# === Spec d'usage ===
function_meta: "META.FUNCTION.NORMER"
item_id_prefix: "PROP"
summary: "Catalogue des règles de propagation atomiques PROP-XXX qui décrivent les cascades obligatoires entre objets de l'écosystème LBP : quand un objet source est modifié, quels objets/docs cibles doivent être propagés, sous quelle condition, par quelles étapes concrètes, et comment auditer la propagation. Réceptacle canonique de toute cascade documentée dans LBP."
purpose: "Source de vérité atomique des cascades de propagation. Importé par les workflows opérationnels (qui orchestrent l'application de plusieurs PROP) et invoqué par les agents lors des modifications d'objets structurants. Garantit la cohérence transverse de l'écosystème en formalisant explicitement chaque dépendance de propagation."
aliases:
  - "PROPAGATION_RULES_LBP"
  - "Cascades LBP"
  - "Catalogue de propagations"
tags:
  - doc_meta
  - catalogue
  - propagation
  - normer
  - lbp
---

# Règles de propagation - LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta LBP`).
> **Fonction systémique** : `META.FUNCTION.NORMER` (catalogue normatif des cascades obligatoires).
> **Public visé** : intervenants LBP (Leonard, Clément, futurs collaborateurs), agents (brain architect, agents d'analyse, futurs agents de propagation).

---

# 1) Vocation et périmètre

## 1.1 Vocation

Catalogue exhaustif des règles de propagation atomiques (PROP-XXX) qui décrivent les **cascades obligatoires** entre objets de l'écosystème LBP. Chaque PROP est figée à un instant t avec son ID, sa portée, sa source de déclenchement, ses cibles, sa condition d'activation, son action de propagation, ses anti-patterns et son origine. Le doc est consulté lors de toute modification structurante d'un objet pour identifier la cascade à dérouler.

## 1.2 Périmètre

**Inclus** :
- Cascades obligatoires Markdown ↔ Notion (manuels de BDD, WR-RD, taxonomies, notes de concept, docs méta).
- Cascades inter-catalogues docs méta (ajout/modif d'un item d'un catalogue qui en cite un autre).
- Cascades de codification (changement de code, archivage, paire CPT/GLO).
- Cascades de templates d'instanciation (bump version, marquage stale des instances).
- Cascades de conventions et règles (capture C-XXX, R-XXX).

**Exclus** (anti-doublon, application [[Règles intrinsèques - LBP#R-066]]) :
- Règles atomiques **statiques** (contraintes applicables à toute interaction avec l'objet, pas seulement à un changement) → vivent dans `[[Règles intrinsèques - LBP]]`.
- Décisions architecturales d'origine (`D-XXX`) → vivent dans `[[Décisions architecturales - LBP]]`.
- Workflows opérationnels (`WF-XXX`) qui orchestrent l'application de plusieurs PROP → vivent dans `[[Workflows opérationnels - LBP]]`.
- Conventions de codification détaillées → vivent dans `[[Codification - LBP]]`.
- Conventions de la collaboration Claude/Leonard (`C-XXX`) → vivent dans `CLAUDE.md` (scope Session).

**Couverture actuelle vs cible** : ce catalogue est **trans-écosystème** (Brain + Twin + Mission Ops) par construction. Les PROP actuelles (PROP-001 à PROP-011) capturent essentiellement les cascades **du Brain** (Manuel ↔ WR-RD ↔ Notion, paire CPT/GLO, items inter-catalogues docs méta), parce que le legacy `PROPAGATION_RULES_LBP.md` était centré Brain et que la production des cascades Twin / Mission Ops n'a pas encore eu lieu. Les futures cascades spécifiques seront ajoutées au fil de leur découverte :
- **Twin** (Supabase comme stockage cible, pas Notion) : Manuel BDD Twin → WR-RD Twin + tables Supabase ; modifications d'instances Twin (Actifs, Organisations, etc.) → cascades propres ; chaînes D-009 entre BDDs Twin.
- **Mission Ops** : modifications d'instances client (Bricks, Meetings, Actions) → cascades propres.

Ces extensions futures iront soit dans les sous-sections existantes (si la cascade rentre dans une thématique déjà couverte), soit dans de nouvelles sous-sections dédiées (`§5.6 Cascades spécifiques Twin`, `§5.7 Cascades spécifiques Mission Ops`) si le volume le justifie. Vision long terme (cf. `MAPPING_DOCS_META.md` §6.2bis) : split éventuel en 3 catalogues PROP par domaine + 1 catalogue transverse, si le catalogue unique devient trop hétérogène.

## 1.3 Granularité d'item

- **1 PROP-XXX = 1 cascade atomique** : 1 type de modification source produit 1 set de propagations cibles avec 1 set d'étapes cohérent.
- Si une cascade dépend d'un sous-cas de la modification source (ex. modif du frontmatter vs modif du corps), créer **1 PROP par sous-cas** (cf. PROP-005 vs PROP-006).
- Si plusieurs PROP partagent les mêmes cibles et étapes mais avec des sources distinctes, vérifier qu'elles ne se généralisent pas en 1 PROP unique (anti-doublon).

**Test rapide de granularité** : si je peux écrire un déclencheur événementiel concret (« quand X est modifié alors propager vers Y ») et auditer mécaniquement la propagation a posteriori, c'est une PROP-XXX légitime. Si la « cascade » est en fait une contrainte applicable à toute lecture (pas seulement à un changement), c'est une R-XXX (cf. test discriminant R vs PROP en [[Règles intrinsèques - LBP#R-075]] note de migration).

---

# 2) Anatomie d'un item

## 2.1 Schéma des champs (figé v1.0)

| Champ | Type | Description | Exemple |
|---|---|---|---|
| ID | code | Format `PROP-XXX` (3 chiffres, extension à 4 si > 999). Immuable. | `PROP-001` |
| Nom | texte court | Titre lisible humain de la cascade, 5-15 mots. | Modification du schéma d'un Manuel de BDD propage au WR-RD et à la fiche Notion |
| Portée | texte libre | Brain / Twin / Mission Ops / Transverse / Contextuel. Peut être préfixée pour préciser un sous-périmètre. | Brain (Manuels de BDD avec WR-RD) |
| Source | texte court | Type d'objet ou modification source qui déclenche la cascade. | Modification de la section 4 d'un Manuel de BDD (sous-sections 4.1 à 4.5) |
| Cible(s) | texte | Objet(s) ou doc(s) cible(s) qui doivent être propagés. | WR-RD du même nom + fiche Notion `Manuels de BDD` |
| Condition de déclenchement | texte | Quand la cascade s'active : immédiate, conditionnelle (préciser), post-validation, etc. | Immédiate à toute modification de propriété (création / suppression / changement de Type / Cardinalité / Taxonomie / Forme logique / Instructions d'écriture / Clefs de lecture / Utilité / Exemples) |
| Action de propagation | texte long | Étapes concrètes ordonnées de la propagation. Peut inclure les contrôles d'audit en étape finale. | (5-10 étapes typiques) |
| Anti-patterns | texte | Cas explicitement interdits dans cette cascade (fortement recommandé). | Modifier le WR-RD pour corriger un bug d'écriture sans repasser par le manuel parent |
| Articulation | texte | Wikilinks vers règles invoquées, workflows orchestrant cette cascade, autres PROP en lien. | [[Règles intrinsèques - LBP#R-001]], `[[Workflows opérationnels - LBP#WF-008]]` |
| Origine | texte court | Date `JJ-MM-YYYY` + 1 ligne de contexte d'émergence. | 26-04-2026, instanciation des 3 premiers WR-RD (Actifs, Pratiques organisationnelles, Journal des signaux). |

**Lecture du tableau** :
- Champs **génériques obligatoires** : ID, Nom, Portée, Origine.
- Champs **spécifiques à PROP** : Source, Cible(s), Condition de déclenchement, Action de propagation (tous obligatoires : c'est l'anatomie d'une cascade).
- Champs **fortement recommandés** : Anti-patterns, Articulation.
- **Flexibilité de contenu** : `Action de propagation` accepte sous-titres H5, listes numérotées imbriquées, blocs de code (commandes grep, regex) si la nature de la cascade le justifie (cf. [[Règles intrinsèques - LBP#R-073]]).

## 2.2 Format de l'ID

- **Préfixe** : `PROP` (figé)
- **Numéro** : 3 chiffres (extension à 4 si dépassement de 999)
- **Incrément** : monotone, jamais réutilisé même après archivage d'une PROP
- **Immuabilité** : un ID attribué ne change jamais. Une PROP retirée conserve son ID (cf. §6 Archives)

## 2.3 Mini-exemple d'un item bien formé

```
#### PROP-001 : Modification du schéma d'un Manuel de BDD propage au WR-RD et à la fiche Notion

- **Portée** : Brain (Manuels de BDD avec WR-RD instancié)
- **Source** : Modification de la section 4 d'un Manuel de BDD (sous-sections 4.1 à 4.5)
- **Cible(s)** : WR-RD du même nom + fiche Notion `Manuels de BDD` (Lien Drive, Version, propriétés dérivées)
- **Condition de déclenchement** : Immédiate à toute création / suppression / modification de propriété
- **Action de propagation** : (1) Modifier la section 4 du Manuel ; (2) Bumper version Manuel selon R-056 ; (3) Re-projeter mot pour mot vers le WR-RD ; (4) Bumper version WR-RD ; (5) Update fiche Notion (Lien Drive, Version) ; (6) Annoncer C-009 « ✓ Manuel modifié + ✓ WR-RD mis à jour »
- **Anti-patterns** : Modifier le WR-RD pour corriger un bug d'écriture sans repasser par le manuel parent (interdit) ; sauter l'annonce C-009
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-041]] (sera archivée en PROP-001), [[CLAUDE.md#C-009]], `[[Workflows opérationnels - LBP#WF-008]]` (orchestrateur)
- **Origine** : 26-04-2026, instanciation des 3 premiers WR-RD (Actifs, Pratiques organisationnelles, Journal des signaux). Initialement capturée comme R-041 dans Règles intrinsèques, migrée vers PROP-001 le 03-05-2026.
```

---

# 3) Garde-fous de cohérence

## 3.1 Avec [[Règles intrinsèques - LBP]]

- **Garde-fou** : une PROP-XXX ne **redéfinit pas** une R-XXX. Elle peut **invoquer** une R-XXX dans son champ Articulation (« cette cascade applique [[Règles intrinsèques - LBP#R-XXX]] »), mais le contenu de la règle elle-même reste dans son catalogue d'origine.
- **Justification** : application directe de [[Règles intrinsèques - LBP#R-066]] (propriétaire canonique unique).

## 3.2 Avec [[Workflows opérationnels - LBP]]

- **Garde-fou** : un WF-XXX qui orchestre une cascade **invoque** la PROP-XXX correspondante (« étape N : appliquer [[Règles de propagation - LBP#PROP-XXX]] »). Il **ne reproduit pas** les étapes de la PROP. Si un workflow contient une cascade détaillée qui n'est pas dans ce catalogue, c'est une PROP-XXX manquante à capturer.
- **Justification** : séparation propre entre la cascade atomique (PROP) et son orchestration (WF).

## 3.3 Avec [[Décisions architecturales - LBP]]

- **Garde-fou** : toute PROP-XXX doit pouvoir être rattachée à une (ou plusieurs) D-XXX qui motive l'existence de la cascade. Si une PROP-XXX n'a pas de décision d'origine identifiable, c'est probablement une convention informelle qui devrait être promue par une décision explicite.
- **Justification** : la boucle de gouvernance documentaire (cf. `[[Constitution des docs méta - LBP]]` §7) dit : Décision → Règle/Propagation → Workflow.

---

# 4) Récap tabulaire

| ID | Nom | Sous-section (§5.x) | Origine |
|---|---|---|---|
| PROP-001 | Modification du schéma d'un Manuel de BDD propage au WR-RD et à la fiche Notion | 5.1 Cascades de modèle de données | 26-04-2026 |
| PROP-002 | Modification du frontmatter / autres sections d'un Manuel de BDD propage à la fiche Notion | 5.1 Cascades de modèle de données | 24-04-2026 |
| PROP-003 | Modification d'une taxonomie propage aux manuels qui la référencent et aux BDDs Notion consommatrices | 5.2 Cascades de taxonomies | 27-04-2026 |
| PROP-004 | Bump majeur d'un template d'instanciation marque les instances stale et planifie leur migration | 5.3 Cascades de templates et codification | 28-04-2026 |
| PROP-005 | Modification du frontmatter d'une note de concept propage à la paire Glossaire LBP + Registre des notes de concept | 5.4 Cascades de notes de concept et glossaire | 24-04-2026 |
| PROP-006 | Modification du corps d'une note de concept ne propage qu'au Lien Drive Notion | 5.4 Cascades de notes de concept et glossaire | 24-04-2026 |
| PROP-007 | Capture / modification d'une R-XXX propage à Règles intrinsèques + ECOSYSTEM-STATE + audit transverse | 5.5 Cascades inter-catalogues docs méta | 03-05-2026 |
| PROP-008 | Capture / modification d'une D-XXX propage à Décisions architecturales + Règles intrinsèques si dérivation | 5.5 Cascades inter-catalogues docs méta | 03-05-2026 |
| PROP-009 | Capture / modification d'une C-XXX propage à CLAUDE.md + ECOSYSTEM-STATE | 5.5 Cascades inter-catalogues docs méta | 03-05-2026 |
| PROP-010 | Modification d'un code de codification (R-054) propage au bundle docs méta + scripts d'audit | 5.3 Cascades de templates et codification | 01-05-2026 |
| PROP-011 | Ajout / modification d'un item d'un catalogue citant un autre catalogue déclenche une vérification croisée | 5.5 Cascades inter-catalogues docs méta | 03-05-2026 |

---

# 5) Catalogue

## 5.1 Cascades de modèle de données

Cascades qui propagent les modifications du modèle de données d'une BDD (manuel de BDD ↔ WR-RD ↔ fiche Notion d'index) pour préserver la cohérence triple Markdown SoT / précis runtime / index Notion.

#### PROP-001 : Modification du schéma d'un Manuel de BDD propage au WR-RD et à la fiche Notion

- **Portée** : Brain (Manuels de BDD avec WR-RD instancié)
- **Source** : Modification de la section 4 d'un Manuel de BDD (sous-sections 4.1 à 4.5) — création / suppression / modification de propriété (Type, Cardinalité, Taxonomie, Forme logique, Instructions d'écriture, Clefs de lecture, Utilité, Exemples)
- **Cible(s)** : WR-RD du même nom + fiche Notion dans BDD `Manuels de BDD` (Lien Drive, Version du document, Version du template)
- **Condition de déclenchement** : Immédiate à toute modification de propriété en section 4 du Manuel. Direction unilatérale **manuel → WR-RD, jamais l'inverse**.
- **Action de propagation** :
  1. Modifier la section 4 du Manuel (ajout / suppression / modification de propriété).
  2. Bumper la version du Manuel selon [[Règles intrinsèques - LBP#R-056]] et [[Règles intrinsèques - LBP#R-063]] (MINOR pour ajout/modif compatible, MAJOR pour refonte structurelle).
  3. Re-projeter **mot pour mot** vers le WR-RD les 9 colonnes retenues : Champ, Type, Taxonomie(s) - codes, Cardinalité / multiplicité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité, Exemples (cf. [[Règles intrinsèques - LBP#R-042]] QA stricte d'égalité).
  4. Bumper la version du WR-RD selon [[Règles intrinsèques - LBP#R-056]].
  5. Si le `template_version` du Manuel a changé, le propager au WR-RD (`template_version`).
  6. Update fiche Notion `Manuels de BDD` correspondante (Lien Drive si renommage, Version du document, Version du template, updated_at).
  7. **Annonce explicite** [[CLAUDE.md#C-009]] : « ✓ Manuel modifié : X manuel(s) · ✓ Propagation WR-RD : Y WR-RD mis à jour » (ou explicitement « WR-RD non concerné car ... »).
  8. **Audit post-propagation** : diff manuel ↔ WR-RD sur les 9 colonnes (aucun écart non-typographique ne doit subsister).
- **Anti-patterns** :
  - ❌ Modifier le WR-RD pour corriger un bug d'écriture sans repasser par le manuel parent (interdiction propagation remontante).
  - ❌ Sauter l'annonce explicite C-009 → propagation considérée non vérifiable par Leonard.
  - ❌ Modifier le manuel sans propager au WR-RD → divergence fatale entre source et précis agent.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]] (Markdown SoT), [[Règles intrinsèques - LBP#R-041]] (sera archivée comme remplacée par PROP-001), [[Règles intrinsèques - LBP#R-042]] (sera archivée comme remplacée par PROP-001), [[Règles intrinsèques - LBP#R-028]] (sera archivée comme généralisée par PROP-001), [[Règles intrinsèques - LBP#R-056]], [[Règles intrinsèques - LBP#R-063]], [[CLAUDE.md#C-009]], `[[Workflows opérationnels - LBP#WF-008]]` (orchestrateur), `[[Workflows opérationnels - LBP#WF-013]]` (génération initiale).
- **Origine** : 26-04-2026, instanciation des 3 premiers WR-RD (Actifs, Pratiques organisationnelles, Journal des signaux). Initialement capturée en 3 règles distinctes (R-028, R-041, R-042) dans Règles intrinsèques. Consolidée et migrée en PROP-001 le 03-05-2026 lors de la production du catalogue PROP.

#### PROP-002 : Modification du frontmatter ou des sections hors §4 d'un Manuel de BDD propage à la fiche Notion

- **Portée** : Brain (Manuels de BDD)
- **Source** : Modification du frontmatter du Manuel (title, version, summary, purpose, tags, etc.) ou de toute section hors §4 (intro, périmètre, gouvernance, exemples, etc.)
- **Cible(s)** : Fiche Notion dans BDD `Manuels de BDD` (Lien Drive si renommage, Version du document, Statut de l'objet, propriétés dérivées du frontmatter)
- **Condition de déclenchement** : Immédiate à toute modification du Manuel hors §4. Le WR-RD n'est PAS impacté (R-042 ne joue pas).
- **Action de propagation** :
  1. Modifier le frontmatter ou la section concernée du Manuel.
  2. Bumper la version du Manuel selon [[Règles intrinsèques - LBP#R-056]] / [[Règles intrinsèques - LBP#R-063]] si la modification est structurante.
  3. Update fiche Notion `Manuels de BDD` : Version du document, updated_at, et toute propriété dérivée du frontmatter modifié (Statut, Aliases, Description, etc. selon [[Règles intrinsèques - LBP#R-029]]).
  4. **Annonce explicite** : « ✓ Manuel X modifié (frontmatter / section Y) · ✓ Fiche Notion alignée ».
- **Anti-patterns** :
  - ❌ Toucher la fiche Notion sans modifier le Markdown amont → désync fatal détecté au prochain audit transverse.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-029]], [[Règles intrinsèques - LBP#R-055]] (frontmatter), `D-020` (Version du template propagée Brain).
- **Origine** : 24-04-2026, capture initiale comme R-029 dans Règles intrinsèques. Reformulée comme PROP-002 le 03-05-2026 pour distinguer la cascade frontmatter (PROP-002) de la cascade schéma §4 (PROP-001).

## 5.2 Cascades de taxonomies

Cascades qui propagent les modifications d'une taxonomie source vers les manuels qui la référencent et les propriétés select / multi-select Notion qui en consomment les valeurs.

#### PROP-003 : Modification d'une taxonomie propage aux manuels qui la référencent et aux BDDs Notion consommatrices

- **Portée** : Transverse (Brain + Twin + Mission Ops)
- **Source** : Modification d'un mini-doc de taxonomie `.md` (ajout / suppression / renommage de taxon, modification de définition, modification de l'observable d'un taxon, changement de scale_kind ou is_open)
- **Cible(s)** : Manuels qui référencent la taxo (section « Usages des taxonomies ») + BDDs Notion consommatrices (options select / multi-select à aligner via DDL) + WR-RD si les valeurs impactent les Instructions d'écriture
- **Condition de déclenchement** : Immédiate à toute modification de la taxo `.md`. Cascade large : 1 taxo peut impacter 5-10 BDDs Notion et autant de manuels.
- **Action de propagation** :
  1. Modifier la taxo `.md` source de vérité.
  2. Bumper la version de la taxo selon [[Règles intrinsèques - LBP#R-056]] (MAJOR si refonte structurelle, MINOR si ajout/correction compatible).
  3. Aligner la fiche Notion `Registre des taxonomies` correspondante.
  4. **Identifier les manuels qui référencent la taxo** (relation `utilise (taxonomies)` côté BDD `Manuels de BDD`).
  5. Pour chaque manuel impacté : update section « Usages des taxonomies » + WR-RD si applicable + cascade PROP-001 si Instructions d'écriture impactées.
  6. **Pour chaque BDD Notion concernée** : `ALTER` les options select/multi-select via DDL (cf. `[[Workflows opérationnels - LBP#WF-017]]` ALTER taxonomies).
  7. **Annonce explicite** : « Taxo X mise à jour → N manuels + M BDDs Notion alignés ».
- **Anti-patterns** :
  - ❌ Modifier les options select Notion sans propager à la taxo `.md` source → désync silencieuse.
  - ❌ Énumérer les nouveaux taxons dans une instruction d'écriture (viole [[Règles intrinsèques - LBP#R-072]]).
  - ❌ Renommer un taxon sans archiver l'ancien → casse les fiches existantes qui pointaient sur l'ancien (cf. PROP-010 codification).
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-007]], [[Règles intrinsèques - LBP#R-049]], [[Règles intrinsèques - LBP#R-052]], [[Règles intrinsèques - LBP#R-067]] (libellés humains), [[Règles intrinsèques - LBP#R-072]] (anti-énumération), `[[Workflows opérationnels - LBP#WF-017]]` (ALTER taxonomies).
- **Origine** : 27-04-2026, Phase A4 (taxonomies). Capture initiale dans le legacy `PROPAGATION_RULES_LBP.md` cheat sheet ligne 59. Migrée en PROP-003 le 03-05-2026.

## 5.3 Cascades de templates et codification

Cascades liées aux modifications structurantes de templates d'instanciation (qui impactent les instances générées) et de la codification (changements de codes, archivage par renaming).

#### PROP-004 : Bump majeur d'un template d'instanciation marque les instances stale et planifie leur migration

- **Portée** : Brain (templates d'instanciation indexés dans BDD `Templates Brain`)
- **Source** : Bump MAJOR d'un template `.md` (X.Y → (X+1).0) — refonte structurelle des sections, changement du frontmatter structurel, changement du sens canonique
- **Cible(s)** : Fiche Notion `Templates Brain` (Version du template) + audit mécanique des instances (champ `template_version` du frontmatter des docs générés < cible) + planification de migration
- **Condition de déclenchement** : À tout bump MAJOR du template uniquement. Un bump MINOR ne déclenche pas de marquage stale (rétro-compatible).
- **Action de propagation** :
  1. Modifier le template `.md` (refonte structurelle) + bumper version selon [[Règles intrinsèques - LBP#R-056]].
  2. Update fiche Notion `Templates Brain` (Version du template à la nouvelle valeur, Description si refonte sémantique).
  3. **Audit mécanique des instances stale** : grep / Dataview sur le champ `template_version` du frontmatter des instances `< version cible`.
  4. **Lister les instances stale** dans `ECOSYSTEM-STATE.md` (à migrer dans une phase dédiée).
  5. **Planifier une phase de migration** des instances (workflow `[[Workflows opérationnels - LBP#WF-015]]` migration de masse si applicable).
  6. **Ne pas propager dans l'urgence** : c'est un chantier dédié, pas une cascade immédiate.
- **Anti-patterns** :
  - ❌ Bumper MAJOR sans audit des instances stale → dette silencieuse, instances divergentes.
  - ❌ Tenter de migrer 1 instance en isolation sans phase dédiée → traitement incomplet, retour en arrière probable.
- **Articulation** : [[Règles intrinsèques - LBP#R-004]] (template obligatoire), [[Règles intrinsèques - LBP#R-040]] (blocs @INSTR-*), [[Règles intrinsèques - LBP#R-055]] (frontmatter `template_version`), [[Règles intrinsèques - LBP#R-056]] (versioning), `D-020` (Version du template propagée Brain), `[[Workflows opérationnels - LBP#WF-015]]` (migration de masse).
- **Origine** : 28-04-2026, capture initiale dans le legacy `PROPAGATION_RULES_LBP.md` cheat sheet ligne 60. Migrée en PROP-004 le 03-05-2026.

#### PROP-010 : Modification d'un code de codification (R-054) propage au bundle docs méta et aux scripts d'audit

- **Portée** : Transverse (Brain — codification universelle des objets)
- **Source** : Création / modification / archivage d'un préfixe de code dans la grammaire de codification (ajout d'un nouveau type d'objet avec son préfixe, changement de format d'un préfixe, etc.)
- **Cible(s)** : Bundle `*_LBP.md` qui mentionne les codes (notamment `Codification - LBP`, `Règles intrinsèques - LBP` §5.2 R-054, `Constitution des docs méta - LBP` Annexe A) + scripts d'audit qui filtrent par regex sur les codes
- **Condition de déclenchement** : Immédiate à toute modification de la grammaire de codification ([[Règles intrinsèques - LBP#R-054]]). Cascade large.
- **Action de propagation** :
  1. Modifier `Codification - LBP.md` (source de vérité de la grammaire des codes).
  2. Bumper version selon [[Règles intrinsèques - LBP#R-056]] / [[Règles intrinsèques - LBP#R-063]].
  3. Aligner [[Règles intrinsèques - LBP#R-054]] dans `Règles intrinsèques - LBP` si la modification impacte la table de préfixes ou les règles transverses.
  4. Aligner Annexe A de `Constitution des docs méta - LBP` si la modification impacte le naming d'un type de doc méta.
  5. **Identifier les scripts d'audit** qui filtrent par regex sur les codes impactés (chercher dans `scripts/`).
  6. Adapter les regex si nécessaire.
  7. Pour un **changement de code stable** (renommage d'un préfixe ou refonte de format) : c'est **archivage de l'ancien + création du nouveau** ([[Règles intrinsèques - LBP#R-053]]) — jamais une modification simple.
  8. Si paire CPT/GLO impactée ([[Règles intrinsèques - LBP#R-031]]) : propager aux 2 entrées en miroir.
  9. **Annonce explicite** : « Codification modifiée (préfixe X) → N docs bundle alignés + M scripts adaptés ».
- **Anti-patterns** :
  - ❌ Inventer un préfixe de code sans vérifier [[Règles intrinsèques - LBP#R-054]] → asymétrie silencieuse dans le bundle.
  - ❌ Renommer un code en place (sans archiver l'ancien) → casse les références cross-écosystème, ruptures de lignée.
  - ❌ Modifier la grammaire sans aligner les scripts d'audit → faux positifs/négatifs en audit.
- **Articulation** : [[Règles intrinsèques - LBP#R-005]] (code unique stable), [[Règles intrinsèques - LBP#R-031]] (paire CPT/GLO), [[Règles intrinsèques - LBP#R-053]] (renaming via archivage), [[Règles intrinsèques - LBP#R-054]] (codification universelle), [[Règles intrinsèques - LBP#R-064]] (naming docs méta).
- **Origine** : 01-05-2026, capture initiale dans le legacy `PROPAGATION_RULES_LBP.md` cheat sheet ligne 66. Migrée en PROP-010 le 03-05-2026.

## 5.4 Cascades de notes de concept et glossaire

Cascades propres à la double indexation des notes de concept (Registre des notes de concept + Glossaire LBP) et à la distinction frontmatter (propage à 2 BDDs) vs corps (lien Drive uniquement).

#### PROP-005 : Modification du frontmatter d'une note de concept propage à la paire Glossaire LBP + Registre des notes de concept

- **Portée** : Brain (Notes de concept double-indexées)
- **Source** : Modification du frontmatter d'une note de concept (title, version, code, aliases, keywords, etc.)
- **Cible(s)** : Fiche Notion `Glossaire LBP` (propriétés sémantiques) + fiche Notion `Registre des notes de concept` (Lien Drive, Version, Statut). **Paire CPT/GLO synchronisée** ([[Règles intrinsèques - LBP#R-031]]).
- **Condition de déclenchement** : Immédiate à toute modification du frontmatter. Si le code unique change, c'est un cas d'archivage + création (cf. PROP-010).
- **Action de propagation** :
  1. Modifier le frontmatter de la note de concept `.md`.
  2. Bumper version selon [[Règles intrinsèques - LBP#R-056]].
  3. Update fiche `Registre des notes de concept` (Lien Drive si renommage, Version, Statut, Code unique si modifié).
  4. Update fiche `Glossaire LBP` correspondante (propriétés sémantiques dérivées du frontmatter et du corps).
  5. **Vérifier l'alignement Code unique entre les 2 fiches** ([[Règles intrinsèques - LBP#R-031]]) : `CPT_<DOMAIN>_<TOKEN>` et `GLO_<DOMAIN>_<TOKEN>` doivent partager strictement le même `<DOMAIN>_<TOKEN>`.
  6. Si applicable, mettre à jour les relations Glossaire → Méthodes (`est mis en oeuvre par`) et/ou Glossaire → Manuels de BDD (`est modélisé par`).
  7. **Annonce explicite** : « Note de concept X modifiée → 2 fiches Notion (Registre + Glossaire) alignées ».
- **Anti-patterns** :
  - ❌ Update fiche Glossaire sans update fiche Registre → asymétrie silencieuse, paire CPT/GLO cassée.
  - ❌ Modifier directement les fiches Notion sans toucher la note `.md` source → désync fatale.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-029]], [[Règles intrinsèques - LBP#R-030]], [[Règles intrinsèques - LBP#R-031]] (alignement code), [[Règles intrinsèques - LBP#R-054]] (paire CPT/GLO).
- **Origine** : 24-04-2026, capture initiale comme R-030 dans Règles intrinsèques. Migrée en PROP-005 le 03-05-2026 (R-030 reste comme contrainte statique « toute note de concept est double-indexée », PROP-005 décrit la cascade événementielle).

#### PROP-006 : Modification du corps d'une note de concept ne propage qu'au Lien Drive Notion

- **Portée** : Brain (Notes de concept)
- **Source** : Modification du corps Markdown d'une note de concept (sections 1 à N, sans toucher au frontmatter ni au code)
- **Cible(s)** : Lien Drive Notion uniquement (la fiche Notion ne stocke pas le contenu, juste l'URL Drive)
- **Condition de déclenchement** : Immédiate à toute modification du corps de la note. **Pas d'update de Notion** sauf si le corps a impacté des propriétés synthétisées (Description, Règles d'usage, Valeur ajoutée, Usages IA potentiels — auquel cas cascade PROP-005).
- **Action de propagation** :
  1. Modifier le corps de la note de concept `.md`.
  2. Bumper version selon [[Règles intrinsèques - LBP#R-056]] si modification structurante.
  3. **Si les modifications du corps impactent les propriétés synthétisées Notion** (Définition, Règles d'usage, Valeur ajoutée, Usages IA potentiels — cf. [[Règles intrinsèques - LBP#R-029]] et [[Règles intrinsèques - LBP#R-037]]) : déclencher PROP-005 (update fiches Glossaire + Registre).
  4. **Sinon** : aucune update Notion nécessaire (Notion = miroir d'index, pas de contenu).
  5. Annonce : « Note de concept X corps modifié (sans impact sur les fiches Notion) » ou « Note de concept X modifiée → cascade PROP-005 déclenchée ».
- **Anti-patterns** :
  - ❌ Tenter de copier le corps de la note dans la fiche Notion → confusion source de vérité, dette de maintenance.
  - ❌ Ignorer les impacts sur les propriétés synthétisées → fiches Notion stale silencieuses.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-029]] (Markdown SoT pour indexation), [[Règles intrinsèques - LBP#R-037]] (lecture complète obligatoire).
- **Origine** : 24-04-2026, capture initiale dans le legacy `PROPAGATION_RULES_LBP.md` cheat sheet ligne 62. Migrée en PROP-006 le 03-05-2026.

## 5.5 Cascades inter-catalogues docs méta

Cascades qui propagent l'ajout / la modification d'items dans les catalogues docs méta (Règles intrinsèques, Décisions architecturales, Workflows opérationnels, Codification, Règles de propagation, et Conventions Session).

#### PROP-007 : Capture / modification d'une R-XXX propage à Règles intrinsèques + ECOSYSTEM-STATE + audit transverse

- **Portée** : Transverse (gouvernance documentaire LBP)
- **Source** : Capture d'une nouvelle R-XXX ou modification format-impactante d'une R existante (changement de portée, refonte du How to apply, archivage)
- **Cible(s)** : `Règles intrinsèques - LBP.md` (ajout/modif item + récap §4) + `ECOSYSTEM-STATE.md` (trace) + audit / migration des docs concernés si la règle impacte un format existant
- **Condition de déclenchement** : Immédiate à toute capture / modification structurante de R-XXX.
- **Action de propagation** :
  1. Identifier la sous-section thématique de [[Règles intrinsèques - LBP]] où placer la R-XXX (cf. découpage §5.1 à §5.8).
  2. Ajouter / modifier l'item dans la bonne sous-section avec le schéma figé (ID, Nom, Portée, Why, How to apply, Articulation, Exemples, Conséquence, Origine).
  3. Mettre à jour le récap tabulaire §4 du catalogue.
  4. Bumper version Règles intrinsèques selon [[Règles intrinsèques - LBP#R-063]] (patch pour ajout d'entrée atomique).
  5. Update fiche Notion `Règles intrinsèques - LBP` dans BDD `Docs méta LBP` (Version du document, updated_at).
  6. Tracer dans `ECOSYSTEM-STATE.md` la nouvelle règle ([[CLAUDE.md#C-011]]).
  7. **Si la règle impacte un format existant** (ex. R-052 apostrophes, R-061 tirets simples) : identifier l'ensemble impacté (grep transverse), planifier une migration au canon ([[Workflows opérationnels - LBP#WF-015]] si applicable).
  8. Mirror `refs/Règles intrinsèques - LBP.md` côté repo collab.
  9. Commit + push 2 repos ([[CLAUDE.md#C-013]] + [[CLAUDE.md#C-019]]).
- **Anti-patterns** :
  - ❌ Capturer une R-XXX sans la rattacher à une sous-section thématique → item orphelin.
  - ❌ Capturer dans `RULES_LBP.md` legacy au lieu du nouveau `Règles intrinsèques - LBP.md` (le legacy est archivé depuis 03-05-2026).
  - ❌ Oublier la trace ECOSYSTEM-STATE → perte de traçabilité incrémentale.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-063]] (politique bump), [[CLAUDE.md#C-011]] (ECOSYSTEM-STATE), [[CLAUDE.md#C-013]] (push systématique), [[CLAUDE.md#C-019]] (push 2 repos), `[[Workflows opérationnels - LBP#WF-015]]` (migration de masse si format-impactante).
- **Origine** : 03-05-2026, capture lors de la production du catalogue PROP. Initialement intuitionnée dans le legacy `PROPAGATION_RULES_LBP.md` cheat sheet ligne 63 (mention « Règle R-XXX (création / modification format-impactante) »). Formalisée en PROP-007 le 03-05-2026.

#### PROP-008 : Capture / modification d'une D-XXX propage à Décisions architecturales + Règles intrinsèques si dérivation

- **Portée** : Transverse (gouvernance documentaire LBP)
- **Source** : Capture d'une nouvelle D-XXX ou modification d'une décision existante
- **Cible(s)** : `Décisions architecturales - LBP.md` (ajout/modif item + récap) + `Règles intrinsèques - LBP.md` si la décision dérive en R-XXX nouvelle ou modifie une R existante + `ECOSYSTEM-STATE.md`
- **Condition de déclenchement** : Immédiate à toute capture / modification de D-XXX. Cascade vers Règles intrinsèques **conditionnelle** (seulement si dérivation R).
- **Action de propagation** :
  1. Identifier la sous-section thématique de `Décisions architecturales - LBP` (à produire en Phase 4).
  2. Ajouter / modifier l'item dans la bonne sous-section avec le schéma figé (ID, Nom, Portée, Contexte, Options envisagées, Décision, Conséquences, Articulation, Origine).
  3. Mettre à jour le récap tabulaire §4.
  4. Bumper version Décisions selon [[Règles intrinsèques - LBP#R-063]].
  5. **Si la D-XXX dérive en R-XXX** (cas typique : une décision de doctrine implique une nouvelle règle applicable) : déclencher PROP-007 pour propager à Règles intrinsèques.
  6. Update fiche Notion `Décisions architecturales - LBP` dans BDD `Docs méta LBP`.
  7. Tracer dans ECOSYSTEM-STATE.
  8. Mirror `refs/Décisions architecturales - LBP.md`.
  9. Commit + push 2 repos.
- **Anti-patterns** :
  - ❌ Dériver une R-XXX sans capturer la D-XXX d'origine → règle sans rationale auditable (cf. garde-fou §3.1 de Règles intrinsèques).
  - ❌ Capturer une D-XXX dans le legacy `DECISIONS_LBP.md` après que le nouveau `Décisions architecturales - LBP` est actif.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]], [[Règles intrinsèques - LBP#R-063]], [[CLAUDE.md#C-011]], [[CLAUDE.md#C-019]], `[[#PROP-007]]` (cascade conditionnelle vers Règles intrinsèques).
- **Origine** : 03-05-2026, capture lors de la production du catalogue PROP. Initialement dans le legacy cheat sheet ligne 64.

#### PROP-009 : Capture / modification d'une C-XXX propage à CLAUDE.md + ECOSYSTEM-STATE

- **Portée** : Session (collaboration Claude/Leonard, hors bundle LBP canonique)
- **Source** : Capture d'une nouvelle convention C-XXX ou modification d'une convention de session existante
- **Cible(s)** : `CLAUDE.md` (ajout/modif convention) + `ECOSYSTEM-STATE.md` (trace optionnelle si convention structurante)
- **Condition de déclenchement** : Immédiate à toute capture C-XXX.
- **Action de propagation** :
  1. Ajouter / modifier la convention dans `CLAUDE.md` section 4 (Habitudes de travail) ou section appropriée.
  2. Format : ID + énoncé + why + how + articulation + découverte (cohérent avec les conventions existantes).
  3. **Pas de propagation Notion** : `CLAUDE.md` n'est pas indexé en Notion (scope Session, hors bundle LBP).
  4. Optionnel : trace dans ECOSYSTEM-STATE si la convention est structurante.
  5. Commit + push collab repo (le vault `Architecture data` n'est PAS impacté).
- **Anti-patterns** :
  - ❌ Capturer une convention de session dans le bundle LBP (`refs/RULES_LBP.md` ou `Règles intrinsèques - LBP`) → mélange scope Session et scope LBP, viole [[Règles intrinsèques - LBP#R-070]] (ban noms agents) implicitement.
  - ❌ Inversement : capturer une vraie R-XXX (transverse, agent-agnostique) en C-XXX → érosion du catalogue de règles canoniques.
- **Articulation** : [[CLAUDE.md#C-006]] (relecture avant modif), `CLAUDE.md` section 5 (protocole de capture proactive), [[Règles intrinsèques - LBP#R-070]] (Brain agent-agnostique).
- **Origine** : 03-05-2026, capture lors de la production du catalogue PROP. Initialement dans le legacy cheat sheet ligne 65.

#### PROP-011 : Ajout / modification d'un item d'un catalogue citant un autre catalogue déclenche une vérification croisée

- **Portée** : Transverse (tous les catalogues docs méta)
- **Source** : Ajout / modification / suppression d'un item dans un catalogue (R-XXX, PROP-XXX, D-XXX, WF-XXX, code-XXX) qui cite par wikilink inter-doc un item d'un autre catalogue
- **Cible(s)** : Le catalogue cité (vérification que l'item cité existe, est cohérent, n'est pas dédoublonné, et que la dépendance bidirectionnelle éventuelle est matérialisée)
- **Condition de déclenchement** : À chaque ajout / modification d'item contenant un wikilink inter-doc vers un autre catalogue.
- **Action de propagation** :
  1. Identifier les wikilinks inter-doc dans l'item ajouté/modifié (pattern `[[<Autre catalogue>#<PREFIXE>-XXX]]`).
  2. Pour chaque wikilink inter-doc, **ouvrir le catalogue cité en parallèle** et vérifier :
     - **Existence** : l'item cité existe et a le bon ID (pas de wikilink mort).
     - **Cohérence sémantique** : le sens cité est cohérent avec ce que l'item cible définit réellement (relire l'item cible).
     - **Anti-doublon** : aucun doublon implicite n'est créé entre les deux catalogues (même contrainte ou cascade exprimée 2× sous formes différentes — auquel cas garder un seul propriétaire canonique cf. [[Règles intrinsèques - LBP#R-066]]).
     - **Bidirectionnalité éventuelle** : si la citation crée une dépendance bidirectionnelle (l'item cité devrait à son tour mentionner cet item pour cohérence), faire la modification réciproque OU documenter pourquoi non.
  3. Si une asymétrie est détectée, corriger côté catalogue concerné (peut déclencher PROP-007 ou PROP-008 selon le catalogue).
  4. Annoncer la vérification croisée dans le commit message.
- **Anti-patterns** :
  - ❌ Ajouter un wikilink `[[Catalogue X#PROP-099]]` sans vérifier que PROP-099 existe → wikilink mort silencieux.
  - ❌ Citer un sens divergent de ce que l'item cible définit (drift sémantique silencieux).
  - ❌ Créer un doublon implicite entre 2 catalogues (même règle exprimée sous 2 formes) → viole [[Règles intrinsèques - LBP#R-066]].
- **Articulation** : [[Règles intrinsèques - LBP#R-066]] (propriétaire canonique unique), [[Règles intrinsèques - LBP#R-074]] (méthodes pour règles de maintenance — PROP-011 fera partie de la future Méthode - Maintenance d'un catalogue Brain), [[Règles intrinsèques - LBP#R-075]] (sera archivée comme remplacée par PROP-011), [[CLAUDE.md#C-024]] (wikilinks).
- **Origine** : 03-05-2026, en discussion Leonard sur la maintenance croisée inter-catalogues. Initialement capturée comme R-075 dans Règles intrinsèques avec note de migration explicite. Migrée en PROP-011 le 03-05-2026 lors de la production du catalogue PROP — elle est conceptuellement événementielle (déclenchée par ajout/modif d'item), donc PROP plutôt que R.

---

# 6) Archives — Règles de propagation - LBP

*(Aucun item archivé à ce jour.)*

[[Quand des PROP seront archivées, les déplacer ici depuis §5 en conservant leur ID, leur schéma, et en ajoutant les champs `Archivé` (date + raison) et optionnellement `Remplacé par`.]]

---

> **Maintenance et évolution de ce catalogue** : voir `[[Méthode - Maintenance d'un catalogue Brain]]`.
