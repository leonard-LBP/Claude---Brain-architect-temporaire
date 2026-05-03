---
# === Identité ===
title: "Workflows opérationnels - LBP"
doc_type: doc_meta
code: "META_WORKFLOWS_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "TPL_META_CATALOGUE"
template_version: "1.6"
created_at: "03-05-2026"
updated_at: "03-05-2026"

# === Spec d'usage ===
function_meta: "META.FUNCTION.OPERER"
item_id_prefix: "WF"
summary: "Catalogue des workflows opérationnels WF-XXX qui orchestrent les opérations standardisées sur l'écosystème LBP : production de BDDs (manuels, WR-RD, BDDs Notion), production et maintenance des catalogues docs méta, audits transverses, migrations de masse, cascades de propagation et utilitaires. Référentiel canonique des procédures pas-à-pas."
purpose: "Référence canonique pour conduire une opération standardisée sur l'écosystème (production, audit, migration, propagation, utilitaire). Chaque WF-XXX a un trigger, des préconditions, des étapes ordonnées, une sortie, et des articulations avec les règles, décisions et autres workflows. Réceptacle exclusif des procédures opérationnelles ; les contraintes statiques vivent dans [[Règles intrinsèques - LBP]] et les cascades événementielles dans [[Règles de propagation - LBP]]."
aliases:
  - "WORKFLOWS_LBP"
  - "Catalogue de workflows"
  - "Procédures opérationnelles LBP"
tags:
  - doc_meta
  - catalogue
  - workflows
  - operer
  - lbp
---

# Workflows opérationnels - LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta LBP`).
> **Fonction systémique** : `META.FUNCTION.OPERER` (catalogue opératoire des procédures pas-à-pas).
> **Public visé** : intervenants LBP (Leonard, Clément, futurs collaborateurs), agents (brain architect, twin architect, mission architect, scripts d'audit/migration).

---

# 1) Vocation et périmètre

## 1.1 Vocation

Catalogue exhaustif des workflows opérationnels (WF-XXX) qui orchestrent les opérations standardisées sur l'écosystème LBP — Brain, Digital Twin, Mission Ops, et docs méta transverses. Chaque workflow est figé à un instant t avec son ID, sa portée, son trigger, ses préconditions, ses étapes ordonnées, sa sortie, ses articulations et sa date de formalisation. Le doc est consulté par lookup ponctuel (« quel est le WF pour générer un WR-RD ? ») et par composition (« quels WF s'enchaînent pour produire une nouvelle BDD ? »).

## 1.2 Périmètre

**Inclus** :
- Workflows de production initiale (manuels, WR-RD, BDDs Notion, fiches, indexation Markdown→Notion).
- Workflows de production et maintenance des catalogues docs méta (capture d'item R/PROP/D, production d'une décision, refonte de template, audit grep d'un catalogue).
- Workflows d'audit transverse (cohérence Notion ↔ Manuels) et de migration de masse (passage au canon frontmatter, sync DDL).
- Workflows de cascade et de propagation orchestrée entre objets de l'écosystème.
- Utilitaires transverses récurrents (récupération d'URL Drive, etc.).

**Exclus** (anti-doublon, application [[Règles intrinsèques - LBP#R-066]]) :
- Règles atomiques applicables à toute interaction (`R-XXX`) → vivent dans [[Règles intrinsèques - LBP]]. Un WF cite les R applicables, il ne les redéfinit pas (cf. [[Règles intrinsèques - LBP#3.2]]).
- Cascades événementielles atomiques (`PROP-XXX`) → vivent dans [[Règles de propagation - LBP]]. Un WF peut orchestrer plusieurs PROP, mais ne décrit pas la cascade elle-même.
- Décisions architecturales d'origine (`D-XXX`) → vivent dans [[Décisions architecturales - LBP]].
- Conventions de codification détaillées → vivent dans [[Codification - LBP]].
- Conventions de la collaboration Claude/Leonard (`C-XXX`) → vivent dans `CLAUDE.md` (scope Session, hors bundle).
- Workflows de session (re-contextualisation, fin de session) → vivent dans `SESSION_WORKFLOWS.md` (scope Session, hors bundle).
- Méthodes de niveau supérieur qui composent plusieurs WF → vivront dans la BDD `Méthodes LBP` (à formaliser dans le futur ; un WF est une brique opérationnelle, une méthode en compose plusieurs).

## 1.3 Granularité d'item

- **1 WF-XXX = une procédure cohérente avec un trigger clair, une sortie attendue et une séquence d'étapes ordonnées non décomposable sans perte de sens.**
- Si une procédure « grosse » regroupe plusieurs sous-procédures indépendantes (chacune avec son propre trigger et sa propre sortie), la décomposer en N WF distincts, articulés par wikilinks.
- Si plusieurs procédures partagent le même trigger, les mêmes préconditions, et ne diffèrent que par des paramètres mineurs, les fusionner en 1 seul WF avec cas particuliers traités dans les étapes ou en garde-fous.
- **Anti-pattern** : WF « fourre-tout » (trigger vague, étapes qui appellent N autres WF sans logique propre). Symptôme : impossible de décrire en 1 phrase ce qu'il produit, ou les étapes sont une simple liste de « faire WF-X puis WF-Y ».

## 1.4 Agent-agnosticité

Un WF décrit **quoi faire et dans quel ordre**, pas **qui le fait**. L'attribution à un agent (Claude, Brain Architect, Twin Architect, Mission Architect, script automatisé, humain seul, collaboration humain+agent) est faite ailleurs : dans les system prompts, prompts maîtres, logic blocks ou méthodes qui consomment et composent les WF. Cette agnosticité préserve la réutilisabilité des WF sous différents régimes d'exécution.

→ Application directe de [[Règles intrinsèques - LBP#R-070]] (Brain agent-agnostique) étendue au catalogue opérationnel.

## 1.5 Sous-section anticipée §5.5

Une sous-section **« Production des autres docs canoniques »** (notes de concept, taxonomies, terme glossaire, manuels, WR-RD pris isolément, templates, méthodes) est anticipée mais non créée à la v1.0 du catalogue. Elle sera ajoutée par bump MINOR (cf. R-056 et R-063) dès qu'un premier WF de cette famille sera formalisé. Cette anticipation est tracée ici pour orienter la maintenance future et éviter de forcer un WF de production de doc canonique non-BDD non-catalogue dans une sous-section inadaptée.

---

# 2) Anatomie d'un item

## 2.1 Schéma des champs (figé v1.0)

| Champ | Type | Description | Exemple |
|---|---|---|---|
| ID | code | Format `WF-XXX` (3 chiffres, extension à 4 si > 999). Immuable. | `WF-013` |
| Nom | texte court | Titre lisible humain. **Verbe d'action en tête** (Générer, Auditer, Migrer, Capturer, Récupérer, Indexer, Produire, Synchroniser, Propager…). 4-12 mots. | Générer un WR-RD à partir d'un Manuel de BDD |
| Portée | select | Brain / Twin / Mission Ops / Transverse | Transverse |
| Trigger | texte court | Événement ou besoin déclencheur, en 1 phrase. | Besoin de générer ou re-générer un WR-RD après création ou modification d'un Manuel de BDD parent. |
| Préconditions | bullets | État du système requis avant de lancer le WF (docs existants, outils disponibles, validations préalables). | - Manuel parent stabilisé · - Template WR-RD disponible. |
| Étapes | liste numérotée | Procédure ordonnée 1./2./3./… (5-10 étapes typiquement). Sous-étapes en `a./b./c.` ou bullets `-`. **Seul champ qui s'autorise une liste numérotée multi-lignes** ; le reste du WF est en bullets ou prose courte. | 1. Lire la section 4 du manuel parent. 2. Préparer le frontmatter du WR-RD. 3. ... |
| Sortie | bullets | Livrables concrets attendus en fin de WF (artefacts produits, état du système modifié). | - WR-RD instancié dans le bon dossier · - Fiche Notion mise à jour avec le lien Drive. |
| Garde-fous & anti-patterns | bullets | **Optionnel** (omettre si rien à dire). Pièges connus, comportements à proscrire, violations courantes à anticiper. | - ❌ Modifier le WR-RD pour corriger une coquille au lieu de remonter au manuel parent. |
| Articulation | texte long | Wikilinks denses vers règles `[[Règles intrinsèques - LBP#R-XXX]]`, propagations `[[Règles de propagation - LBP#PROP-XXX]]`, décisions `[[Décisions architecturales - LBP#D-XXX]]`, autres workflows `[[#WF-XXX]]`. | [[Règles intrinsèques - LBP#R-041]], [[Règles de propagation - LBP#PROP-001]], [[#WF-011]]. |
| Origine | texte court | Date `JJ-MM-YYYY` + 1 ligne de contexte de formalisation (peut être : observation répétée, formalisation post-batch, capture proactive en session, généralisation d'un anti-pattern). | 26-04-2026, formalisé après instanciation test de 3 WR-RD (Actifs, Pratiques, Journal). |

Tous les champs ci-dessus sont obligatoires (convention par défaut), à l'exception de `Garde-fous & anti-patterns` qui peut être omis si la procédure est sans piège connu ou si les anti-patterns sont déjà capturés en règles citées dans `Articulation`.

## 2.2 Format de l'ID

- **Préfixe** : `WF` (figé)
- **Numéro** : 3 chiffres (extension à 4 si dépassement de 999)
- **Incrément** : monotone, jamais réutilisé même après archivage d'un workflow
- **Immuabilité** : un ID attribué ne change jamais. Un workflow retiré conserve son ID (cf. §6 Archives)

## 2.3 Mini-exemple d'un item bien formé

```
## WF-011 : Récupérer l'URL Drive d'un fichier local du vault

- **Portée** : Transverse
- **Trigger** : Besoin d'obtenir l'URL Drive d'un fichier `.md` du vault pour la coller dans une propriété Notion (ex. `Lien vers le manuel de BDD (.md)`, `Lien vers le doc WR-RD (.md)`).
- **Préconditions** :
  - Google Drive for Desktop installé et synchronisé sur la machine.
  - Fichier cible présent et stabilisé dans `H:\Drive partagés\LBP - shared\Architecture data\`.
  - Fichier remonté côté Drive web (synchronisation effective).
- **Étapes** :
  1. Identifier le `user_id` Drive for Desktop actif (sous-dossier numéroté de `C:\Users\<user>\AppData\Local\Google\DriveFS\` dont les fichiers `mirror_metadata_sqlite.db-wal` ont une date récente).
  2. Ouvrir la base SQLite `mirror_metadata_sqlite.db` en read-only.
  3. Joindre `items` avec `stable_parents` filtré par le `parent_stable_id` du dossier actif (évite les doublons via dossier `00 - archives/`).
  4. Récupérer l'`id` du fichier ciblé.
  5. Construire l'URL au format `https://drive.google.com/file/d/{file_id}/view`.
- **Sortie** :
  - URL Drive prête à coller dans la propriété Notion ciblée.
- **Garde-fous & anti-patterns** :
  - ❌ Filtrer uniquement par `local_title` sans le `parent_stable_id` → faux positifs si le fichier a un homonyme dans `00 - archives/`.
  - ❌ Ouvrir la base SQLite en écriture → corruption potentielle de la base de Drive for Desktop.
- **Articulation** : [[Règles intrinsèques - LBP#R-029]] (indexation Notion à partir du Markdown), [[Règles intrinsèques - LBP#R-052]] (lien Drive dans manuels), [[#WF-012]] (indexation Markdown→Notion qui consomme l'URL).
- **Origine** : 24-04-2026, mini-batch 0 Twin v2, formalisé après plusieurs récupérations manuelles répétitives.
```

---

# 3) Garde-fous de cohérence

## 3.1 Avec [[Règles intrinsèques - LBP]]

- **Garde-fou** : un WF-XXX **applique** les R-XXX pertinentes (citation par wikilink dans `Articulation`), il **ne les redéfinit pas**. Si un workflow contient une nouvelle contrainte qui n'est pas dans le catalogue de règles, c'est une R-XXX manquante à capturer.
- **Justification** : application directe de [[Règles intrinsèques - LBP#R-066]] (propriétaire canonique unique). Symétrique du garde-fou §3.2 du catalogue R.

## 3.2 Avec [[Règles de propagation - LBP]]

- **Garde-fou** : un WF-XXX peut **orchestrer** une cascade en invoquant une PROP-XXX (« en fin d'étape, déclencher [[Règles de propagation - LBP#PROP-001]] »), mais ne décrit pas la cascade en détail. La cascade atomique vit dans le catalogue PROP.
- **Justification** : séparation propre des responsabilités. Le WF est une procédure transverse qui peut traverser plusieurs cascades ; chaque cascade reste atomique côté PROP.

## 3.3 Avec [[Décisions architecturales - LBP]]

- **Garde-fou** : tout WF-XXX structurant doit pouvoir être rattaché à une (ou plusieurs) D-XXX qui le motive (typiquement la décision qui a posé le besoin de la procédure standardisée). Si un WF n'a pas de décision d'origine identifiable, c'est probablement une procédure ad hoc qui devrait être promue par une décision explicite avant capture canonique.
- **Justification** : application de la boucle de gouvernance documentaire (Décision → Règle → Workflow). Sauter l'étape Décision crée des workflows sans rationale auditable.

## 3.4 Avec les futures `Méthodes LBP`

- **Garde-fou** : un WF est une **brique opérationnelle** consommée par des méthodes de niveau supérieur (qui composent plusieurs WF, ajoutent du jugement contextuel, gèrent l'attribution agent). Si un item documenté ici ne décrit pas une procédure pas-à-pas mais un assemblage stratégique, il vit dans `Méthodes LBP`, pas ici.
- **Justification** : §1.4 (agent-agnosticité) + §1.3 (granularité). Un WF n'attribue jamais à un agent ; une méthode peut le faire.

---

# 4) Récap tabulaire

| ID | Nom | Sous-section (§5.x) | Origine |
|---|---|---|---|
| WF-013 | Générer un WR-RD à partir d'un Manuel de BDD | 5.1 Cycle de vie d'une BDD | 26-04-2026 |
| WF-014 | Générer une BDD Notion à partir de son Manuel | 5.1 Cycle de vie d'une BDD | 26-04-2026 (révisé v3 27-04-2026) |
| WF-012 | Indexer un doc Markdown dans sa BDD Notion | 5.1 Cycle de vie d'une BDD | itéré au fil des batchs d'indexation |
| WF-017 | Synchroniser le DDL Notion d'une BDD à partir des écarts d'audit | 5.1 Cycle de vie d'une BDD | 28-04-2026 |
| WF-022 | Produire une nouvelle décision D-XXX | 5.2 Cycle de vie d'un catalogue doc méta | 03-05-2026 |
| WF-019 | Capturer proactivement un anti-pattern en R/PROP/D/code | 5.2 Cycle de vie d'un catalogue doc méta | 03-05-2026 |
| WF-021 | Auditer par grep un doc catalogue après instanciation | 5.2 Cycle de vie d'un catalogue doc méta | 03-05-2026 |
| WF-020 | Propager une refonte structurelle d'un template (bump MAJOR) | 5.2 Cycle de vie d'un catalogue doc méta | 03-05-2026 |
| WF-016 | Auditer la cohérence Notion ↔ Manuels Brain | 5.3 Audits & migrations transverses | 28-04-2026 |
| WF-015 | Migrer au canon frontmatter un type de doc Brain | 5.3 Audits & migrations transverses | 28-04-2026 |
| WF-008 | Propager les impacts d'une modification d'un doc/objet de l'écosystème | 5.4 Cascades, utilitaires & sync transverses | 30-04-2026 |
| WF-011 | Récupérer l'URL Drive d'un fichier local du vault | 5.4 Cascades, utilitaires & sync transverses | 24-04-2026 |

---

# 5) Catalogue

## 5.1 Cycle de vie d'une BDD

Workflows qui orchestrent la production initiale, l'indexation et la synchronisation des BDDs canoniques (Brain, Twin, Mission Ops) et de leurs artefacts dérivés (manuels, WR-RD, fiches Notion).

## WF-013 : Générer un WR-RD à partir d'un Manuel de BDD

- **Portée** : Transverse (Brain / Twin / Mission Ops)
- **Trigger** : Besoin de générer ou re-générer un WR-RD après création ou modification structurante du Manuel de BDD parent.
- **Préconditions** :
  - Manuel de BDD parent existant et stabilisé (au moins en `version: "0.1"` avec section 4 renseignée).
  - Template WR-RD disponible et à jour (`Template - WR-RD - Digital Twin.md` v1.2+ pour Twin, équivalent pour Brain dès création).
  - Sous-dossier `WR-RD/` créé dans le groupe BDD cible (`Manuels de BDD/{Brain,Digital Twin,Mission Ops}/WR-RD/`).
- **Étapes** :
  1. Lire intégralement la section 4 du manuel parent. Identifier les sous-sections renseignées (4.1 Génériques, 4.2 Spécifiques, 4.3 Relations + jumelles + rollups, 4.4 Couche 5D, 4.5 Couche calculée). Repérer celles vides ou marquées non applicables.
  2. Préparer le frontmatter du WR-RD selon le `FRONTMATTER_INSTANCE` du template : `target_bdd_canonical_name`, `target_bdd_code` (`DBMAN_*`), `parent_manual` (filename exact), `wr_rd_code` (`WRRD_*`, token aligné avec le manuel), `domain`, `version: "0.1"` pour première instanciation, `template_version`, `created_at`.
  3. Projeter chaque sous-section 4.X dans la section X correspondante du WR-RD selon le mapping fixe (4.1→1, 4.2→2, 4.3→3, 4.4→4, 4.5→5). Pour chaque ligne du tableau du manuel, extraire **strictement** les 9 colonnes retenues (Champ, Type, Taxonomie(s) - codes, Cardinalité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité, Exemples). Les colonnes Portée, Nature de production, Prérequis ne sont PAS reprises (cf. [[Décisions architecturales - LBP#D-016]]).
  4. Si la BDD n'a pas de couche 5D ou pas de couche calculée native, supprimer la section correspondante du WR-RD (au lieu d'un tableau vide). Optionnellement ajouter une note brève en fin de doc expliquant pourquoi la section est absente.
  5. Appliquer la QA stricte d'égalité ([[Règles intrinsèques - LBP#R-042]], archivée en PROP-001) : vérifier cellule par cellule l'égalité mot pour mot entre le WR-RD et la section 4 du manuel parent sur les 9 colonnes retenues. Tolérances admises : adaptations typographiques liées au rendu Markdown.
  6. Appliquer la QA anti-artefacts ([[Règles intrinsèques - LBP#R-039]]) : vérifier l'absence d'artefacts IA (`:contentReference[oaicite:N]{index=N}`, `[citation:N]`, texte tronqué, placeholders non résolus).
  7. Récupérer l'URL Drive du WR-RD via [[#WF-011]] et la coller dans la propriété `Lien vers le doc WR-RD (.md)` de la fiche Notion correspondant au manuel parent dans la BDD `Manuels de BDD`.
  8. Vérifier la conformité finale : le WR-RD est-il bien dans `Manuels de BDD/{Domain}/WR-RD/` ? Frontmatter complet et conforme ? Sections (ou subset) correctes ? Fiche Notion du manuel parent pointe-t-elle vers le WR-RD ?
- **Sortie** :
  - WR-RD instancié dans `Manuels de BDD/{Domain}/WR-RD/WR-RD - <Nom de la BDD>.md`, conforme au template et égal mot pour mot au manuel parent sur les 9 colonnes retenues.
  - Fiche Notion du manuel parent enrichie de la propriété `Lien vers le doc WR-RD (.md)`.
- **Garde-fous & anti-patterns** :
  - ❌ Modifier le WR-RD pour corriger une coquille — toute amélioration éditoriale repasse par le manuel parent (PROP-001).
  - ❌ Reprendre dans le WR-RD les colonnes Portée, Nature de production, Prérequis du manuel — colonnes hors périmètre WR-RD ([[Décisions architecturales - LBP#D-016]]).
  - ❌ Produire des tableaux vides pour les sections sans contenu — supprimer la section et expliquer brièvement pourquoi.
- **Articulation** : [[Règles intrinsèques - LBP#R-039]] (anti-artefacts), [[Règles de propagation - LBP#PROP-001]] (cascade Manuel → WR-RD, ex-R-041/R-042/R-028), [[Décisions architecturales - LBP#D-014]] (colocalisation WR-RD/manuel), [[Décisions architecturales - LBP#D-016]] (rôle, contenu, format des WR-RD), [[#WF-011]] (récupération URL Drive), [[#WF-008]] (propagation orchestrée si modification Manuel impacte aussi d'autres dérivés).
- **Origine** : 26-04-2026, formalisé après instanciation test de 3 WR-RD (Actifs, Pratiques organisationnelles, Journal des signaux).

## WF-014 : Générer une BDD Notion à partir de son Manuel

- **Portée** : Transverse (Brain / Twin / Mission Ops)
- **Trigger** : Besoin de matérialiser sur Notion une nouvelle BDD canonique à partir de son manuel parent (cas typique : ensemble cohérent comme les 28 BDDs Twin v2, 11 BDDs Brain, BDDs Mission Ops).
- **Préconditions** :
  - Manuel parent à jour et conforme au canon ([[Règles intrinsèques - LBP#R-027]] naming, [[Règles de propagation - LBP#PROP-001]] alignement WR-RD).
  - Page hôte Notion identifiée (où les BDDs seront posées en pleine page).
  - Périmètre des BDDs à générer arrêté.
  - Pour un batch homogène : toutes les taxonomies référencées disponibles dans `Taxonomies/` avec valeurs canoniques exhaustives.
- **Étapes** :
  1. **Phase 0 — Cadrage** : confirmer la page hôte, le périmètre, et que les manuels parents sont stabilisés.
  2. **Phase 1 — Manifest** : pour chaque manuel, parser la section 4 (4.1 à 4.5) en JSON structuré (`properties.natives`, `properties.relations`, `properties.rollups`). Lire chaque taxo référencée et extraire les valeurs canoniques (codes + libellés + couleurs). Valider en interne : toute relation bidirectionnelle référence une BDD cible présente dans le manifest avec un miroir cohérent ; tout rollup référence une relation source existante ; toute taxo a au moins une valeur extraite.
  3. **Phase 2 — Création des BDDs vides** : créer N BDDs pleine page sous la page hôte avec **uniquement le titre** ([[Règles intrinsèques - LBP#R-048]] nom canonique simple). Stocker l'`id` Notion de chaque BDD pour usage ultérieur.
  4. **Passe 1 — Schéma natif (toutes BDDs, props non-relationnelles)** : exécuter pour chaque BDD une salve `update_data_source` avec les ADD COLUMN dans l'ordre [[Règles intrinsèques - LBP#R-047]] strict (Bloc 1 Tête, Bloc 2 Corpus métier subdivisé en 2a/2b/2c/2d, Bloc 3 Queue gestion, Bloc 4 Sources textuelles). Peupler les options select/multi-select avec libellés et couleurs depuis le manifest taxos. **Important** : pas de relations à cette passe (sinon les miroirs créés trop tôt sur les autres BDDs cassent leur ordering — leçon WF-014 v3, 27-04-2026).
  5. **Passe 2 — Relations bidirectionnelles (toutes BDDs, après Passe 1 globale)** : exécuter pour chaque BDD une salve `update_data_source` avec les ADD COLUMN relations bidir (`RELATION('target_ds_id', DUAL 'mirror_name' 'mirror_id')`). Pas la relation mono `Source(s) d'information` (différée). QA : pour chaque relation bidir, vérifier le miroir côté cible (nom + cardinalité conformes au manuel).
  6. **Passe 3 — Rollups (toutes BDDs, après Passe 2 globale)** : exécuter pour chaque BDD une salve `update_data_source` avec les ADD COLUMN ROLLUP (`ROLLUP('source_relation', 'target_property', 'function')`). QA : aucune erreur « propriété cible introuvable ».
  7. **Passe finale — Sources d'informations + calculés différés** : créer la BDD `Sources d'informations` sur la même page Notion (section Mission Ops). Ajouter sur chaque BDD la relation mono `Source(s) d'information` vers cette BDD. Ajouter les formules locales si elles avaient été différées (queue de schéma).
  8. **QA finale par BDD** : nombre de propriétés cohérent avec le manuel, options taxos correctement peuplées, aucune propriété fantôme. Mettre à jour la fiche du manuel correspondant dans la BDD `Manuels de BDD` Notion : renseigner `Lien vers la BDD Notion` (URL de la nouvelle BDD).
- **Sortie** :
  - N BDDs Notion matérialisées avec schéma complet conforme au manuel parent (natives + relations bidir + rollups + sources).
  - N fiches `Manuels de BDD` Notion enrichies de la propriété `Lien vers la BDD Notion`.
  - Manifest JSON archivé pour idempotence (rejouable sur la même page test).
- **Garde-fous & anti-patterns** :
  - ❌ Fusionner natives + relations en une seule passe par BDD (anti-pattern WF-014 v2 corrigé en v3) → miroirs prématurés sur les autres BDDs avant que leurs propres natives soient créées, casse de l'ordering global.
  - ❌ Créer des rollups avant la Passe 2 → erreurs « propriété cible introuvable ».
  - ❌ Détruire/recréer une BDD qui contient déjà des données → perte irréversible. Le rollback ne s'applique qu'aux pages test vides.
  - ⚠️ Pour les sandboxes ([[Règles intrinsèques - LBP#R-014]]) : Passe 2 quasi-vide (sauf relation mono `Sources d'informations`).
- **Articulation** : [[Règles intrinsèques - LBP#R-045]] (manuel = source de vérité), [[Règles intrinsèques - LBP#R-046]] (ordre de création BDDs → props → relations → rollups), [[Règles intrinsèques - LBP#R-047]] (convention d'ordering 7 blocs), [[Règles intrinsèques - LBP#R-048]] (naming BDD nom canonique simple), [[Règles intrinsèques - LBP#R-014]] (sandboxes), [[Règles intrinsèques - LBP#R-019]] (5 couches d'une BDD), [[#WF-016]] (audit transverse Notion ↔ Manuels post-création), [[#WF-017]] (sync DDL si écarts détectés).
- **Origine** : 26-04-2026, cadrage Phase 6.5 préparation 28 BDDs Twin v2 ; révisé en WF-014 v3 le 27-04-2026 après pilote Actifs (découplage en 3 passes globales séparées pour préserver l'ordering global).

## WF-012 : Indexer un doc Markdown dans sa BDD Notion

- **Portée** : Transverse
- **Trigger** : Besoin de créer ou de mettre à jour une fiche Notion à partir d'un doc Markdown du vault (manuel de BDD, WR-RD, taxonomie, note de concept, doc méta indexé, template, etc.).
- **Préconditions** :
  - Doc Markdown source stabilisé dans le vault (frontmatter conforme, contenu finalisé).
  - BDD Notion cible identifiée (`Manuels de BDD`, `Registre des taxonomies`, `Notes de Concept LBP`, `Glossaire LBP`, `Docs méta LBP`, `Templates Brain`, etc.) avec son schéma à jour.
  - URL Drive du doc accessible via [[#WF-011]].
- **Étapes** :
  1. Récupérer l'URL Drive du doc via [[#WF-011]].
  2. Vérifier si l'entrée Notion existe déjà via `notion-search` filtré sur la `data_source_url` de la BDD cible. Pivot par type d'objet ([[Règles intrinsèques - LBP#R-038]]) : taxonomies = code unique ; autres = nom canonique. Trois cas : (a) existe avec même code/nom → mise à jour ([[Règles intrinsèques - LBP#R-032]], [[Règles intrinsèques - LBP#R-036]]) ; (b) existe avec code/nom différent (v1 obsolète remplacée par v2) → archiver v1 + créer v2 ; (c) n'existe pas → création.
  3. Lire intégralement le doc Markdown ([[Règles intrinsèques - LBP#R-029]] : SoT ; [[Règles intrinsèques - LBP#R-069]] : lecture complète obligatoire).
  4. Lire la description de chaque propriété Notion via `notion-fetch` sur la data source ([[Règles intrinsèques - LBP#R-033]] : descriptions = mini-prompts de remplissage). Récupérer contraintes de format, structure, valeurs canoniques (select/multi-select).
  5. Dériver les propriétés à partir du doc en respectant les contraintes : nom canonique, code unique, statut, domaines, etc. Pour les textes longs (Description ≤280, Règles d'usage, Valeur ajoutée) : synthétiser depuis le doc sans inventer ([[Règles intrinsèques - LBP#R-029]] : pas de fabrication). Pour les select/multi-select : utiliser uniquement les valeurs strictes autorisées ; pas d'énumération de taxons dans la description ([[Règles intrinsèques - LBP#R-072]]).
  6. **Passe 1 — Création/mise à jour sans relations** ([[Règles intrinsèques - LBP#R-034]]) : utiliser `notion-create-pages` (création) ou `notion-update-page` (mise à jour). Si des relations sont impossibles à cette passe (cibles pas encore créées dans le batch), laisser vides.
  7. **Passe 2 — Relations** : une fois toutes les entrées du batch créées, les relier via `notion-update-page` avec les URLs des pages cibles. Pour une note de concept, double indexation ([[Règles intrinsèques - LBP#R-030]]) : 1 entrée dans `Registre des notes de concept` + 1 dans `Glossaire LBP` avec **même code unique** ([[Règles intrinsèques - LBP#R-031]]), liées via `est documenté par (notes de concept)`.
  8. Si v1 remplacée par v2 : archiver l'entrée v1 (passer son `Statut` à `Archivé` ; pas de suppression).
  9. QA anti-artefacts ([[Règles intrinsèques - LBP#R-039]]) sur les contenus dérivés avant publication.
  10. Vérifier que les entrées sont bien créées et reliées. Tracer les ajouts/maj dans `ECOSYSTEM-STATE.md` si l'état évolue significativement.
- **Sortie** :
  - 1 (ou N) entrée(s) Notion créée(s) ou mise(s) à jour, conforme(s) au doc Markdown source.
  - Pour une note de concept : paire `CPT/GLO` à code identique reliée bidirectionnellement.
  - Anciennes versions éventuelles archivées (statut, pas suppression).
- **Garde-fous & anti-patterns** :
  - ❌ Inventer une valeur de propriété non dérivable du doc → laisser vide ([[Règles intrinsèques - LBP#R-029]]).
  - ❌ Modifier le code unique d'une entrée existante → le code est immuable ([[Règles intrinsèques - LBP#R-005]], [[Règles intrinsèques - LBP#R-036]]).
  - ❌ Créer relations avant que les cibles existent (Passe 1 → 2 obligatoire, [[Règles intrinsèques - LBP#R-034]]).
  - ❌ Énumérer les valeurs d'une taxo dans la description ≤280 d'une fiche ([[Règles intrinsèques - LBP#R-072]]) → ne mentionner que le code de la taxo.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]] (Markdown SoT), [[Règles intrinsèques - LBP#R-029]] à [[Règles intrinsèques - LBP#R-038]] (corpus indexation Notion), [[Règles intrinsèques - LBP#R-039]] (anti-artefacts), [[Règles intrinsèques - LBP#R-069]] (lecture complète), [[Règles intrinsèques - LBP#R-072]] (anti-énumération taxons), [[#WF-011]] (URL Drive), [[#WF-016]] (audit post-indexation), [[#WF-008]] (cascade plus large si modification du doc source).
- **Origine** : Itéré au fil des batchs d'indexation Brain (Phases 1-7 du chantier Brain v3 et Phase A du chantier docs méta) ; pattern stable formalisé.

## WF-017 : Synchroniser le DDL Notion d'une BDD à partir des écarts d'audit

- **Portée** : Transverse (Brain / Twin / Mission Ops)
- **Trigger** : Existence d'un rapport d'écarts produit par [[#WF-016]] indiquant des actions DDL à appliquer (DROP, ADD, ALTER options, RENAME, CONVERT text→rollup, CREATE rollup) sur une ou plusieurs BDDs Notion.
- **Préconditions** :
  - Rapport d'audit [[#WF-016]] disponible et validé.
  - Manuels parents stabilisés (les manuels font foi, [[Règles intrinsèques - LBP#R-045]]).
  - Pour les ADD select/multi-select : taxos référencées disponibles dans `Taxonomies/` avec libellés et couleurs canoniques.
- **Étapes** :
  1. Préparer le batch DDL par BDD depuis le rapport d'audit (regrouper les actions par BDD cible).
  2. Pour chaque BDD : identifier les taxos vides à peupler à partir du manifest taxos (libellés + couleurs depuis le `.md` de la taxo dans `Taxonomies/`).
  3. Exécuter via `notion-update-data-source` une salve par BDD, opérations groupées dans cet ordre obligatoire (ordre Notion DDL — pas de réordonnancement post-création) : (a) RENAME (préparation), (b) DROP (nettoyage), (c) ALTER options (correction), (d) ADD natives (compléments), (e) CONVERT text→rollup et CREATE rollup (couche dérivée — exige que les relations sources existent déjà).
  4. Vérifier post-DDL : re-fetch la data source via `notion-fetch`, comparer avec le manuel parent (mini-rerun de [[#WF-016]] sur la BDD ciblée). Score doit être Conforme.
  5. Compléter les descriptions des nouvelles propriétés à la main sur la fiche Notion (limite API Notion : pas de description settable via DDL).
  6. Tracer dans `ECOSYSTEM-STATE.md` la chronologie des actions par BDD (volume, type d'actions).
- **Sortie** :
  - 1 (ou N) BDD(s) Notion alignée(s) sur leur manuel parent (score Conforme).
  - Descriptions de propriétés complétées à la main sur les nouvelles propriétés.
  - Trace dans `ECOSYSTEM-STATE.md`.
- **Garde-fous & anti-patterns** :
  - ❌ Inverser l'ordre RENAME → DROP → ALTER → ADD → ROLLUP → références cassées ou collisions de noms.
  - ❌ Créer un rollup avant que la relation source existe → erreur Notion « propriété cible introuvable ».
  - ❌ Oublier de compléter les descriptions à la main → fiche Notion conforme structurellement mais inutilisable côté agent (les descriptions sont les mini-prompts de remplissage, [[Règles intrinsèques - LBP#R-033]]).
  - ❌ Modifier le manuel parent en réaction à un écart audit (« le manuel a tort, alignons-le sur Notion ») → viole [[Règles intrinsèques - LBP#R-001]] et [[Règles intrinsèques - LBP#R-045]]. Si l'écart révèle une erreur dans le manuel, corriger d'abord le manuel (workflow séparé), puis relancer audit + sync.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]] (Markdown SoT), [[Règles intrinsèques - LBP#R-045]] (manuel = SoT pour BDD), [[Règles intrinsèques - LBP#R-033]] (descriptions Notion = mini-prompts), [[Règles intrinsèques - LBP#R-051]] (ordering via `update_view SHOW`), [[Règles intrinsèques - LBP#R-058]] (pas de jumelles texte sur BDDs Brain), [[#WF-016]] (audit en amont), [[#WF-014]] (variantes pour création de BDD vs sync DDL d'existante).
- **Origine** : 28-04-2026, formalisé après application sur les 11 BDDs Brain (~26 actions DDL appliquées, toutes BDDs en Conforme post-sync).

## 5.2 Cycle de vie d'un catalogue doc méta

Workflows qui orchestrent la production et la maintenance des catalogues docs méta (Règles, Propagations, Décisions, Workflows, Codification, futurs catalogues) : production d'item, capture proactive, audit qualité, propagation des refontes structurelles de templates.

## WF-022 : Produire une nouvelle décision D-XXX

- **Portée** : Transverse
- **Trigger** : Émergence d'un choix architectural structurant à formaliser : décision spontanée à graver, arbitrage explicite suite à un audit, refonte structurante en cours de session, ou résolution d'un conflit entre règles existantes.
- **Préconditions** :
  - Le contexte qui motive la décision est clair et nommable.
  - Les options envisagées sont identifiables (au moins l'option retenue + une alternative écartée).
  - Le choix retenu est opposable (peut servir de référence pour arbitrer des cas futurs similaires).
  - Catalogue [[Décisions architecturales - LBP]] actif.
- **Étapes** :
  1. Décrire le **Contexte** (problème ou besoin qui motive la décision — équivalent du Why d'une R, mais centré sur la situation et les contraintes plutôt que sur le coût opérationnel).
  2. Identifier les **Options envisagées** (alternatives considérées avec analyse coûts/bénéfices ; au minimum l'option retenue + une option écartée explicitement).
  3. Énoncer la **Décision** (choix retenu, énoncé clair et opposable, formulé comme une assertion).
  4. Décrire les **Conséquences** (effets directs sur l'écosystème : R-XXX dérivées à capturer, PROP-XXX dérivées, WF-XXX à mettre à jour, migrations à planifier, dette technique éventuelle).
  5. Identifier l'**Articulation** (wikilinks vers R/PROP/WF dérivées, autres D antécédentes / conséquentes / révisées, doctrines impactées).
  6. Choisir la sous-section thématique de [[Décisions architecturales - LBP]] (5.1 fondatrices / 5.2 ontologie et frontières / 5.3 architecture transverse / 5.4 conventions docs et lifecycle / 5.5 codification, templates, migrations docs méta).
  7. Proposer ID + Nom + sous-section pour validation explicite (cf. protocole de capture proactive).
  8. Si validé : ajouter D-XXX dans le bon §5.x du catalogue + récap §4 (avec **Date de décision** et **Origine** distinctes — l'une pour la date du choix, l'autre pour la date/contexte de formalisation).
  9. Bumper la `version` du catalogue [[Décisions architecturales - LBP]] selon [[Règles intrinsèques - LBP#R-063]] (PATCH pour ajout d'entrée atomique, MINOR pour évolution structurelle).
  10. Mettre à jour la fiche Notion du catalogue dans BDD `Docs méta LBP` (`Version du document`, `updated_at`).
  11. Si la décision dérive en R-XXX nouvelle : déclencher [[#WF-019]] (capture R) en parallèle, et citer la R nouvelle en `Articulation` de la D.
  12. Mirror `refs/` du repo collab + commit + push sur les 2 repos pertinents.
- **Sortie** :
  - 1 nouvelle D-XXX capturée dans son catalogue, avec ID immuable.
  - R-XXX / PROP-XXX dérivées éventuellement capturées en parallèle (via [[#WF-019]]).
  - Catalogue [[Décisions architecturales - LBP]] bumpé + fiche Notion alignée.
  - Mirror `refs/` à jour, commit + push effectués.
- **Garde-fous & anti-patterns** :
  - ❌ Confondre Décision et Règle : une D capture le choix architectural et son contexte ; une R capture la contrainte opposable qui en découle. Une D peut exister sans R dérivée (décision purement architecturale) ; une R sans D rattachable est suspecte ([[Règles intrinsèques - LBP#3.1]]).
  - ❌ Ne pas distinguer **Date de décision** (jour où le choix a été acté) et **Origine** (jour où le choix est formalisé dans le catalogue, peut être ultérieur).
  - ❌ Énumérer en `Conséquences` toutes les dérivées hypothétiques sans les capturer ensuite — soit on capture les R/PROP/WF dérivées dans la même unité de travail, soit on les liste comme TODO ECOSYSTEM-STATE pour suivi.
- **Articulation** : [[Règles intrinsèques - LBP#R-063]] (politique bump), [[Règles de propagation - LBP#PROP-008]] (cascade D-XXX), [[#WF-019]] (capture R/PROP dérivées éventuellement), [[Décisions architecturales - LBP]] §2 (anatomie d'un item D-XXX).
- **Origine** : 03-05-2026, observé sur D-024, D-025, D-026 capturées en Phase 1.0 du chantier docs méta (pattern stable et éprouvé).

## WF-019 : Capturer proactivement un anti-pattern en R/PROP/D/code

- **Portée** : Transverse
- **Trigger** : Observation d'un anti-pattern : (a) signalement explicite d'un comportement défaillant qui crée une asymétrie ou une dette silencieuse, (b) détection d'un anti-pattern par un agent lors d'un audit, (c) constatation d'une convention informelle appliquée plusieurs fois sans avoir été formalisée.
- **Préconditions** :
  - L'anti-pattern est nommable (peut être décrit en 1 phrase).
  - Son coût opérationnel est mesurable ou décrivable concrètement.
  - Sa portée est identifiable (Brain / Twin / MO / Transverse).
  - Catalogues cibles actifs ([[Règles intrinsèques - LBP]], [[Règles de propagation - LBP]], [[Décisions architecturales - LBP]], futur [[Codification - LBP]], `CLAUDE.md` pour les conventions de session).
- **Étapes** :
  1. Observer et décrire l'anti-pattern : ce qui s'est passé, le coût opérationnel constaté ou anticipé, la portée affectée.
  2. Formuler la règle qui le proscrit : `Why` (pourquoi cette règle existe), `How to apply` (comment appliquer), `Articulation` (liens avec règles voisines), `Exemples` ✅/❌, `Conséquence si violation`.
  3. **Choisir le bon catalogue cible** selon la nature de la contrainte :
     - **R-XXX** ([[Règles intrinsèques - LBP]]) : règle statique applicable à toute interaction.
     - **PROP-XXX** ([[Règles de propagation - LBP]]) : cascade événementielle déclenchée par un changement.
     - **D-XXX** ([[Décisions architecturales - LBP]]) : décision architecturale structurante (déclencher [[#WF-022]]).
     - **code-XXX** ([[Codification - LBP]]) : convention de codification.
     - **C-XXX** (`CLAUDE.md`) : convention de session Claude/Leonard, pas de l'écosystème (test : si l'anti-pattern n'a de sens que dans la collaboration humain↔agent en session, c'est un C ; sinon c'est un R).
  4. Choisir la sous-section thématique correspondante dans le catalogue cible.
  5. Proposer ID + Nom + sous-section pour validation explicite (cf. protocole de capture proactive).
  6. Si validé : ajouter l'item dans le catalogue + mettre à jour le récap §4.
  7. Bumper la `version` du catalogue selon [[Règles intrinsèques - LBP#R-063]] (PATCH pour ajout d'entrée atomique).
  8. Mettre à jour la fiche Notion correspondante dans BDD `Docs méta LBP` (`Version du document`, `updated_at`).
  9. Mirror `refs/` + commit + push sur les 2 repos pertinents.
  10. Si l'anti-pattern impacte des docs existants déjà produits : déclencher la cascade [[Règles de propagation - LBP#PROP-007]] (R-XXX → audit transverse + migration ciblée des docs impactés).
- **Sortie** :
  - 1 nouvel item (R / PROP / D / code / C) capturé dans son catalogue cible avec ID immuable.
  - Catalogue bumpé + fiche Notion alignée.
  - Mirror `refs/` à jour, commit + push effectués.
  - Si applicable : cascade PROP-007 déclenchée pour aligner les docs existants impactés.
- **Garde-fous & anti-patterns** :
  - ❌ Capturer une R alors que le contenu est conjoncturel à une session de travail (test : sera-t-il opposable dans 6 mois indépendamment du contexte ? Si non → ne pas capturer ou capturer en C).
  - ❌ Mélanger R et PROP : si la formulation contient « quand X change, faire Y » → c'est PROP, pas R. Test discriminant systématique.
  - ❌ Capturer comme R une convention de session (collaboration humain↔agent) — ces conventions vont dans `CLAUDE.md` (C-XXX).
  - ❌ Sauter la cascade PROP-007 quand l'anti-pattern impacte des docs existants → asymétrie installée silencieusement.
- **Articulation** : [[Règles intrinsèques - LBP#R-063]] (politique bump), [[Règles intrinsèques - LBP#R-070]] (Brain agent-agnostique — guide pour bien arbitrer R vs C), [[Règles de propagation - LBP#PROP-007]] (cascade R-XXX → docs impactés), [[Règles de propagation - LBP#PROP-008]] (cascade D-XXX), [[Règles de propagation - LBP#PROP-009]] (cascade C-XXX), [[#WF-022]] (production D-XXX), [[#WF-021]] (audit grep post-instanciation).
- **Origine** : 03-05-2026, observé ≥7 fois pendant la session de production des catalogues fondateurs (R-072, R-073, R-074, R-075, C-028, et migrations R→PROP). Pattern qui définit la maintenance vivante de l'écosystème doctrinal.

## WF-021 : Auditer par grep un doc catalogue après instanciation

- **Portée** : Transverse (tous catalogues docs méta instanciés depuis [[Templates Brain - Template - META Catalogue]] ou un futur template de catalogue)
- **Trigger** : Production initiale ou modification structurante d'un doc catalogue (Règles, Propagations, Décisions, Workflows, Codification, futurs catalogues), avant publication ou commit final.
- **Préconditions** :
  - Doc catalogue produit en `.md` dans son dossier cible.
  - Python disponible pour scripts d'audit (parsing YAML, regex, comptage).
  - Connaissance du `item_id_prefix` du catalogue (ex. `R`, `PROP`, `D`, `WF`, `code`).
- **Étapes** :
  1. **Wikilinks intra-doc** : tout renvoi à un autre item du même catalogue est-il en wikilink interne `[[#PREFIXE-XXX]]` (et non en prose brute « voir R-027 ») ? Script Python avec regex `^#### ` (avec espace) pour H4 strict ; sans l'espace, on capte aussi H5+ et le body extrait est tronqué (bug détecté Phase 4.1).
  2. **Champ Origine rempli** : tous les items ont-ils un champ `Origine` non vide ? Vérifier l'absence de placeholders résiduels (`[[JJ-MM-YYYY...]]`, `TODO`, etc.).
  3. **Marqueurs temporels résiduels** ([[Règles intrinsèques - LBP#R-059]] et convention C-027) : aucun marqueur `(à créer|à venir|TBD|TODO|provisoire|sera créé|futur|en attente|à formaliser)` dans le doc instancié. Filtrer les exemples explicites en R-073 / R-059 qui les mentionnent légitimement.
  4. **Énumération de taxons** ([[Règles intrinsèques - LBP#R-072]]) : aucune liste explicite de valeurs de taxonomies dans les instructions / descriptions ≤280. Vérification visuelle des champs `How to apply` qui mentionnent `Taxo: <CODE>` — la mention du code est OK, l'énumération des valeurs ne l'est pas.
  5. **YAML frontmatter parseable** ([[Règles intrinsèques - LBP#R-073]]) : `python -c "import yaml; yaml.safe_load(open('instance.md', encoding='utf-8').read().split('---')[1])"` doit retourner sans erreur. Vérifier en plus que les items de liste contenant `:`, `"` ou apostrophes typographiques sont enveloppés en quotes.
  6. **Récap §4 vs catalogue §5** : compter les items dans §5 (regex H4 strict), vérifier l'égalité avec le nombre de lignes du tableau §4. Tout écart révèle un item présent dans une section mais pas l'autre.
  7. **IDs immuables et monotones** : extraire la séquence d'IDs (`PREFIX-001`, `PREFIX-002`, etc.) et vérifier qu'aucun ID n'est dupliqué et qu'aucun ID retiré n'est réutilisé (vérification croisée avec §6 Archives si applicable).
  8. **Si un contrôle échoue** : corriger avant publication. Ne pas committer un doc qui ne passe pas l'audit.
- **Sortie** :
  - Doc catalogue conforme aux règles de qualité, prêt pour publication, commit + push.
  - Rapport éphémère des contrôles passés (peut être conservé temporairement dans `scripts/.../output/` pour traçabilité du run).
- **Garde-fous & anti-patterns** :
  - ❌ Utiliser regex `^####` sans l'espace → capte aussi H5+, tronque les body extracts (bug récurrent — la règle est `^#### ` avec espace).
  - ❌ Sauter l'audit pour « gagner du temps » sur un doc volumineux → asymétries silencieuses qui ressortiront 3 mois plus tard lors d'un audit transverse plus coûteux.
  - ❌ Auditer uniquement le frontmatter en oubliant le corps → la majorité des asymétries vivent dans les items du catalogue (énumération de taxons, marqueurs temporels, wikilinks bruts).
  - ❌ Supprimer le rapport d'audit avant le commit → perte de traçabilité ; le conserver le temps du commit puis nettoyer.
- **Articulation** : [[Règles intrinsèques - LBP#R-027]] (conventions de naming), [[Règles intrinsèques - LBP#R-039]] (anti-artefacts IA), [[Règles intrinsèques - LBP#R-053]] (archivage), [[Règles intrinsèques - LBP#R-055]] (frontmatter 3 zones), [[Règles intrinsèques - LBP#R-056]] (versioning X.Y), [[Règles intrinsèques - LBP#R-059]] (hygiène — pas de bruit), [[Règles intrinsèques - LBP#R-064]] (naming docs méta), [[Règles intrinsèques - LBP#R-068]] (aliases anti-redondance), [[Règles intrinsèques - LBP#R-072]] (anti-énumération taxons), [[Règles intrinsèques - LBP#R-073]] (YAML), [[Templates Brain - Template - META Catalogue]] §7 INSTANTIATION_FLOW (audit déjà partiellement formalisé côté template).
- **Origine** : 03-05-2026, formalisé en cours de production des catalogues fondateurs après détection de plusieurs anomalies récurrentes (R-068 alias = code, R-073 YAML cassé sur cleanup_rules, regex audit qui matche H4+H5).

## WF-020 : Propager une refonte structurelle d'un template (bump MAJOR)

- **Portée** : Transverse (tous templates d'instanciation Brain : templates de manuels, WR-RD, notes de concept, taxonomies, catalogues docs méta, méthodes, prompts, logic blocks, etc.)
- **Trigger** : Bump MAJOR d'un template d'instanciation : refonte structurelle des sections, changement du frontmatter structurel, changement du sens canonique, ajout/retrait de blocs `@INSTR-*`.
- **Préconditions** :
  - Template `.md` source disponible et stabilisé.
  - Liste exhaustive des instances déjà générées avec leur `template_version` actuel (frontmatter ou propriété Notion `Version du template`).
  - Décision actée (typiquement une [[Décisions architecturales - LBP#D-013]] ou similaire) sur l'ampleur de la refonte et son besoin opérationnel.
- **Étapes** :
  1. Modifier le template `.md` source (refonte structurelle) et bumper `version` selon [[Règles intrinsèques - LBP#R-056]] (X.Y → (X+1).0 pour MAJOR).
  2. Documenter le changement dans le frontmatter `notes:` du template ou via un commit message clair (rationale, structure cible, impact attendu sur les instances).
  3. Mettre à jour la fiche Notion `Templates Brain` correspondante : `Version du template` à la nouvelle valeur, `Description` si refonte sémantique du sens du template.
  4. **Audit mécanique des instances stale** : grep / Dataview sur le champ `template_version` du frontmatter des instances existantes — toute instance avec `template_version < version cible` est stale.
  5. Lister les instances stale dans `ECOSYSTEM-STATE.md` (à migrer dans une phase dédiée — un chantier MAJOR n'est pas un commit isolé).
  6. **Pour chaque instance stale**, en cascade : (a) migrer au nouveau schéma (peut être structurellement lourd : réorganiser sections, ajouter / retirer champs frontmatter, etc.) ; (b) bumper `template_version` de l'instance ; (c) bumper `version` de l'instance (MINOR ou MAJOR selon impact côté instance) ; (d) mettre à jour la fiche Notion correspondante ; (e) mirror `refs/` + commit + push.
  7. Une fois toutes les instances migrées : audit final que `template_version` = version cible sur 100% des instances (script grep/Dataview).
- **Sortie** :
  - Toutes les instances alignées sur le nouveau template (`template_version` = version cible partout).
  - Aucune instance stale.
  - Fiche Notion `Templates Brain` à jour.
  - ECOSYSTEM-STATE tracé du chantier de migration.
- **Garde-fous & anti-patterns** :
  - ❌ Bumper le template sans audit préalable des instances stale → on ne sait pas combien d'instances sont impactées ni si la refonte est tenable opérationnellement.
  - ❌ Migrer les instances en silence sans tracer dans ECOSYSTEM-STATE → perte de traçabilité incrémentale.
  - ❌ Bumper le template MAJOR pour un changement qui aurait pu être MINOR (ajout de champ optionnel, renommage de section non-impactant) → propage une cascade lourde sur toutes les instances pour rien.
  - ❌ Migrer les instances « par batch silencieux » sans valider le pattern sur 1 ou 2 instances pilotes d'abord — risque d'asymétrie systémique sur N migrations.
- **Articulation** : [[Règles intrinsèques - LBP#R-004]] (template obligatoire), [[Règles intrinsèques - LBP#R-040]] (instructions @INSTR-*), [[Règles intrinsèques - LBP#R-055]] (frontmatter 3 zones), [[Règles intrinsèques - LBP#R-056]] (versioning X.Y), [[Règles intrinsèques - LBP#R-063]] (politique bump docs méta), [[Décisions architecturales - LBP#D-013]] (traçabilité template_version), [[Décisions architecturales - LBP#D-020]] (propagation Version du template Brain), [[Règles de propagation - LBP#PROP-004]] (cascade bump majeur template), [[#WF-015]] (migration de masse).
- **Origine** : 03-05-2026, observé sur la refonte du Template - META Catalogue (v1.4 → v1.5 → v1.6) qui a impacté Règles intrinsèques (v1.0 → v1.3) — cascade structurelle : ajout §6 Archives, swap §4↔§5 récap/catalogue, renommage Découverte→Origine, audit grep ajouté. Procédure cascade éprouvée.

## 5.3 Audits & migrations transverses

Workflows qui orchestrent la vérification de cohérence transverse (vault ↔ Notion, manuels ↔ schémas Notion) et les migrations de masse au canon (frontmatter, codification, versioning).

## WF-016 : Auditer la cohérence Notion ↔ Manuels Brain

- **Portée** : Brain (extension Twin / MO transposable au même schéma)
- **Trigger** : Vérification périodique de l'alignement Notion ↔ Manuels, ou pré-requis avant un sync DDL ([[#WF-017]]), ou après une cascade de modifications sur les manuels.
- **Préconditions** :
  - Manuels parents stabilisés (font foi, [[Règles intrinsèques - LBP#R-045]]).
  - Accès MCP Notion (`notion-fetch`) disponible.
  - Liste des BDDs cibles à auditer (les 11 BDDs Brain typiquement).
- **Étapes** :
  1. **Fetch des data sources Notion** : pour chaque BDD à auditer, via `notion-fetch`, récupérer la liste exhaustive des propriétés (nom, type, options pour les select/multi-select).
  2. **Parse de la section schéma de chaque manuel parent** : lire la (ou les) section(s) du manuel qui décrivent les propriétés Notion attendues (génériques 4.1, spécifiques 4.2, relations 4.3, rollups 4.5, taxonomies référencées).
  3. **Comparaison ligne à ligne** : pour chaque propriété attendue côté manuel, vérifier sa présence côté Notion (nom exact, type exact, options exactes pour les select). Pour chaque propriété présente côté Notion, vérifier qu'elle est documentée dans le manuel.
  4. **Classification des écarts** :
     - **MANQUE** : présent manuel, absent Notion → ADD à prévoir.
     - **OBSOLÈTE** : présent Notion, absent manuel → DROP à prévoir.
     - **MISMATCH TYPE** : type différent → CONVERT à prévoir.
     - **MISMATCH OPTIONS** : valeurs select divergentes → ALTER à prévoir.
     - **CASSE / TYPO / ACCENTS** : nom différent à la marge → RENAME à prévoir.
     - **JUMELLE TEXTE INTERDITE** ([[Règles intrinsèques - LBP#R-058]]) : DROP à prévoir.
  5. **Rapport markdown par BDD** : score (Conforme / Mineur / Majeur / Critique) + liste des écarts classés + recommandations DDL prêtes à consommer par [[#WF-017]].
  6. **Synthèse transverse** : tableau récap des BDDs auditées, total d'actions DDL nécessaires, prioritisation (BDDs Critique → Mineur).
  7. Tracer dans `ECOSYSTEM-STATE.md` la chronologie de l'audit (date, BDDs auditées, écarts trouvés, prochaine action).
- **Sortie** :
  - 1 rapport markdown par BDD auditée (score + écarts + recommandations DDL).
  - 1 synthèse transverse (typiquement `scripts/notion_brain_audit/audit_notion_brain.md` ou équivalent).
  - Trace dans `ECOSYSTEM-STATE.md`.
  - Input directement consommable par [[#WF-017]] pour application des actions DDL.
- **Garde-fous & anti-patterns** :
  - ❌ Modifier le manuel parent en réaction à un écart « pour aligner sur Notion » → viole [[Règles intrinsèques - LBP#R-001]] et [[Règles intrinsèques - LBP#R-045]]. Si l'écart révèle une erreur dans le manuel, corriger d'abord le manuel (workflow séparé), puis relancer l'audit.
  - ❌ Auditer en omettant les options des select/multi-select → MISMATCH OPTIONS silencieusement non détecté.
  - ❌ Accepter une divergence « mineure » sans la classer comme RENAME / ALTER → désynchronisation qui s'installe dans le temps.
  - ❌ Sauter la synthèse transverse et n'avoir que des rapports par BDD → perte de la vue d'ensemble nécessaire pour prioriser le sync.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]] (Markdown SoT), [[Règles intrinsèques - LBP#R-045]] (manuel = SoT pour BDD), [[Règles intrinsèques - LBP#R-052]] (apostrophes typographiques), [[Règles intrinsèques - LBP#R-058]] (pas de jumelles texte sur BDDs Brain), [[#WF-017]] (sync DDL en aval), [[#WF-014]] (génération initiale dont WF-016 vérifie la cohérence).
- **Origine** : 28-04-2026, formalisé après application sur les 11 BDDs Brain (rapport de référence : `scripts/notion_brain_audit/audit_notion_brain.md`, ~26 actions DDL identifiées).

## WF-015 : Migrer au canon frontmatter un type de doc Brain

- **Portée** : Brain (transposable Twin / MO mutatis mutandis)
- **Trigger** : Lot homogène de docs Brain (manuels, WR-RD, notes de concept, instances de templates, taxonomies, etc.) à migrer au canon frontmatter : codification universelle [[Règles intrinsèques - LBP#R-054]], 3 zones balisées [[Règles intrinsèques - LBP#R-055]], versioning `X.Y` [[Règles intrinsèques - LBP#R-056]]. Typiquement déclenché par adoption d'un nouveau standard ou par bump majeur de template.
- **Préconditions** :
  - Type de doc cible identifié (manuel, WR-RD, note de concept, etc.) avec sa convention canonique exacte connue.
  - Inventaire exhaustif possible (glob sur dossier ou liste explicite).
  - Python disponible pour script idempotent.
  - Backup git récent du vault (filet de sécurité avant migration de masse).
- **Étapes** :
  1. **Inventaire** : lister tous les docs du type cible (glob sur le dossier ou liste explicite). Snapshot du nombre total pour vérification post-migration.
  2. **Parse frontmatter** : pour chaque doc, lire le frontmatter YAML, extraire l'état actuel.
  3. **Calcul du frontmatter cible** : appliquer les règles canoniques :
     - Génération du `code` selon [[Règles intrinsèques - LBP#R-054]] (préfixe + token MAJUSCULES_UNDERSCORE).
     - Réorganisation en 3 zones (Identité / Méta-gouvernance / Spec d'usage) selon [[Règles intrinsèques - LBP#R-055]].
     - Normalisation du `version` en `X.Y` selon [[Règles intrinsèques - LBP#R-056]]. Si forme legacy `"DATE vX.Y.Z"` détectée : split en `version` + `created_at`.
     - Normalisation des dates en `JJ-MM-YYYY` ([[Règles intrinsèques - LBP#R-044]]).
     - Normalisation des apostrophes en typographiques `’` ([[Règles intrinsèques - LBP#R-052]]) dans les chaînes de description.
  4. **Mode `--dry-run`** : produire un rapport diff par doc (avant / après) sans écrire. Permet revue avant application — calibration impérative sur 2-3 docs avant de lancer en masse.
  5. **Mode `--apply`** : écrire les frontmatters normalisés. Idempotent (un second passage ne doit produire aucun diff).
  6. **QA post-migration** : re-lire un échantillon (5-10 docs représentatifs), vérifier la conformité aux 3 règles canoniques, vérifier l'absence d'artefacts.
  7. **Audit YAML parseable** : pour chaque doc migré, vérifier que le frontmatter parse sans erreur (`yaml.safe_load`) — détecte les apostrophes typographiques et `:` non quotés ([[Règles intrinsèques - LBP#R-073]]).
  8. **Commit unifié par phase de migration** : un commit par type de doc cible, message clair (volume + type + canon appliqué).
- **Sortie** :
  - N docs du type cible migrés au canon frontmatter, idempotents (rerun no-op).
  - Rapport `--dry-run` archivé pour traçabilité.
  - 1 commit par phase, mirror `refs/` aligné, push effectué.
- **Garde-fous & anti-patterns** :
  - ❌ Lancer `--apply` sans avoir validé le diff `--dry-run` sur 2-3 docs pilotes → risque d'asymétrie systémique sur N docs (cf. principe de calibration explicite).
  - ❌ Migrer plusieurs types de docs en un seul commit → perte de granularité pour rollback ciblé.
  - ❌ Ne pas vérifier l'idempotence (rerun → diff vide) → script pas vraiment au canon, dérive cachée.
  - ❌ Sauter l'audit YAML parseable post-migration → frontmatter cassé silencieusement (typique : apostrophes typographiques dans une string non quotée).
- **Articulation** : [[Règles intrinsèques - LBP#R-044]] (format date), [[Règles intrinsèques - LBP#R-052]] (apostrophes typographiques), [[Règles intrinsèques - LBP#R-054]] (codification universelle), [[Règles intrinsèques - LBP#R-055]] (frontmatter 3 zones), [[Règles intrinsèques - LBP#R-056]] (versioning X.Y), [[Règles intrinsèques - LBP#R-073]] (YAML parseable), [[Règles de propagation - LBP#PROP-002]] (cascade migration au canon), [[#WF-021]] (audit grep variant pour catalogues).
- **Origine** : 28-04-2026, formalisé après les Phases 4-7 du chantier Brain v3 — 318 docs migrés au total (43 manuels, 32 WR-RD, 72 notes de concept, 24 instances + autres). Volumes de référence et pattern script idempotent éprouvés.

## 5.4 Cascades, utilitaires & sync transverses

Workflows transverses : cascades de propagation orchestrée entre objets de l'écosystème, et utilitaires récurrents (récupération d'URL Drive, etc.) sans appartenance naturelle à un cycle de vie spécifique.

## WF-008 : Propager les impacts d'une modification d'un doc/objet de l'écosystème

- **Portée** : Transverse (tout doc structurant : manuels, WR-RD, taxonomies, templates, notes de concept, règles, décisions, conventions, docs méta indexés)
- **Trigger** : Modification d'un doc/objet structurant de l'écosystème dont les dérivés (autres docs, fiches Notion, mirrors `refs/`) doivent être réalignés. Workflow orchestrateur transverse qui rassemble en un pas-à-pas unique les cascades obligatoires de [[Règles de propagation - LBP]].
- **Préconditions** :
  - Modification du doc source effectuée (ou prête à effectuer) sur le `.md` canonique.
  - Connaissance du type de modification (format, contenu, codification, statut/archivage).
  - Connaissance du type de doc source modifié (manuel, WR-RD, taxo, template, etc.).
  - Accès aux mirrors (`refs/`) et à Notion pour propagation.
- **Étapes** :
  1. **Phase 1 — Identifier le type de modification et le doc source**. Classer la modification : (a) **format** (changement de structure : frontmatter, sections, naming) → cascade large ; (b) **contenu** (changement de wording dans un champ existant) → cascade ciblée ; (c) **codification** (changement de code d'identification) → cascade de tous les renvois (cf. cas particulier 1 ci-dessous) ; (d) **statut/archivage** (passage à archivé) → propagation Notion + nettoyage des renvois.
  2. **Phase 2 — Cartographier les dérivés directs**. Selon le type de doc modifié, lister les dérivés à propager (cf. tableau ci-dessous). Le **principe directeur** : la propagation est **strictement descendante** (du doc source vers ses dérivés) ; un dérivé ne corrige jamais en remontant — toute amélioration éditoriale repasse par le doc parent ([[Règles de propagation - LBP#PROP-001]]).
  3. **Phase 3 — Propager dans l'ordre strict des dérivés**. Ne jamais sauter d'étape, ne jamais réordonner : (a) **Markdown d'abord** : le doc dérivé Markdown est mis à jour ; (b) **Versions bumpées** : si le contenu structurant change ([[Règles intrinsèques - LBP#R-056]] et [[Règles intrinsèques - LBP#R-063]]), bumper la version + `updated_at` ; (c) **Notion ensuite** : une fois le Markdown stable, aligner Notion (DDL si schéma, propriétés textuelles si contenu) ; (d) **Renvois croisés** : si le doc modifié est cité ailleurs (autres docs Markdown, ECOSYSTEM-STATE), grep + remplacement systématique.
  4. **Phase 4 — QA après propagation**. (a) Pour cascade Manuel→WR-RD : appliquer la QA stricte ([[Règles de propagation - LBP#PROP-001]]) — égalité mot pour mot des colonnes retenues ; (b) Pour cascade vers Notion : re-fetch et comparer avec le manuel via [[#WF-016]] ; (c) Pour les renvois : grep sur l'ancien nom doit renvoyer 0 match (sauf dans archives explicites) ; (d) Cohérence narrative : relire le doc parent et son dérivé pour détecter toute incohérence sémantique introduite.
  5. **Phase 5 — Annonce explicite de la propagation**. Si la modification touche un Manuel et son WR-RD : annoncer explicitement dans la même unité de travail le volume propagé (« Manuel modifié : X · Propagation WR-RD : Y », ou « WR-RD non concerné car ... »). Sans cette annonce, la propagation est considérée non vérifiable.
  6. **Phase 6 — Tracer dans `ECOSYSTEM-STATE.md`**. Mise à jour systématique du journal vivant : « Dernière mise à jour », « Phase actuelle » si phase notable, « État du Brain » si volumétrie change. Pas de batch — un commit ECOSYSTEM-STATE par phase de propagation pour préserver la traçabilité incrémentale.
  7. **Phase 7 — Commit + push (sur tous les repos pertinents)**. Commit avec message explicite (`[Domain] [Action] [Volume] - propagation [doc source] → [dérivés]`). Push immédiat dans la même unité de travail, sur **chaque** repo touché par la cascade (typiquement vault `lbp-architecture-data-vault` + collab `Claude - Brain architect temporaire` quand `refs/` est miroir).

  **Tableau des dérivés directs par type de doc source** :

  | Doc source modifié | Dérivés directs à propager | Cascade |
  |---|---|---|
  | **Manuel de BDD** (section 4) | WR-RD du même nom | [[Règles de propagation - LBP#PROP-001]] |
  | **Manuel de BDD** (frontmatter / autres sections) | Fiche Notion `Manuels de BDD` (lien Drive, version, statut) | [[Règles intrinsèques - LBP#R-029]], [[Décisions architecturales - LBP#D-020]] |
  | **WR-RD** (modification non triviale) | ⚠️ INTERDIT — repasser par le manuel parent | [[Règles de propagation - LBP#PROP-001]] (interdiction propagation remontante) |
  | **Taxonomie .md** (valeurs canoniques) | (a) Manuels référençant la taxo (section "Usages") + (b) Notion DDL : ALTER options de toutes les BDDs concernées + (c) WR-RDs si la valeur impacte une instruction d'écriture | [[Règles de propagation - LBP#PROP-003]], [[#WF-017]] |
  | **Template d'instanciation** | Toutes les instances existantes utilisant ce template (cf. [[#WF-020]]) | [[Règles de propagation - LBP#PROP-004]] |
  | **Note de concept** (frontmatter) | Glossaire LBP Notion + Registre des notes de concept Notion | [[Règles de propagation - LBP#PROP-005]] |
  | **Note de concept** (corps) | Lien Drive Notion uniquement (Notion = miroir) | [[Règles intrinsèques - LBP#R-001]] |
  | **Règle R-XXX** (création/modification) | [[Règles intrinsèques - LBP]] + ECOSYSTEM-STATE + docs concernés si format-impactant | [[Règles de propagation - LBP#PROP-007]] |
  | **Décision D-XXX** | [[Décisions architecturales - LBP]] + R/PROP/WF dérivées + ECOSYSTEM-STATE | [[Règles de propagation - LBP#PROP-008]] |
  | **Convention C-XXX** | `CLAUDE.md` + ECOSYSTEM-STATE | [[Règles de propagation - LBP#PROP-009]] |
  | **Doc méta indexé** dans BDD `Docs méta LBP` | (a) Bumper `version` + `updated_at` du frontmatter ; (b) Fiche Notion `Docs méta LBP` (`Version du document`, `updated_at`, `Statut`) ; (c) Mirror `refs/<DOC>_LBP.md` du repo collab | [[Règles de propagation - LBP#PROP-006]] |

  **Cas particuliers** :
  - **Cas 1 — Modification de codification** : si on change un code stable (ex. `CPT_X` → `CPT_Y`), c'est un **archivage de l'ancien + création du nouveau** ([[Règles intrinsèques - LBP#R-053]]). Procédure : (a) archiver l'ancienne entrée Notion (Statut → Archivé, pas de suppression) ; (b) créer la nouvelle entrée avec le nouveau code ; (c) propager les renvois (grep + remplacement) ; (d) si paire `CPT/GLO`, propagation aux 2 entrées Notion en miroir.
  - **Cas 2 — Modification d'une taxonomie** (cascade large) : taxo référencée par N manuels et M propriétés Notion. Procédure : (a) MAJ taxo `.md` + fiche Notion `Registre des taxonomies` ; (b) identifier manuels qui la référencent ; (c) MAJ section "Usages" de chaque manuel + propagation WR-RD si applicable ; (d) ALTER options Notion via [[#WF-017]] ; (e) annoncer le volume total propagé.
  - **Cas 3 — Modification d'un template** (cascade très large) : ne pas propager dans l'urgence — c'est un chantier dédié [[#WF-020]] (audit instances stale + plan de migration).
  - **Cas 4 — Modification d'une règle qui change un format** (ex. R-052) : (a) MAJ règle dans [[Règles intrinsèques - LBP]] ; (b) identifier l'ensemble impacté (grep) ; (c) lancer [[#WF-015]] (migration au canon) si pattern massif ; (d) si pattern ciblé, propagation manuelle doc par doc avec QA.
- **Sortie** :
  - Doc(s) dérivé(s) Markdown alignés sur le doc source, avec QA passée.
  - Notion synchronisé (DDL, propriétés textuelles, statut).
  - Renvois croisés à jour (0 match résiduel sur l'ancien nom hors archives).
  - ECOSYSTEM-STATE tracé.
  - Commit + push effectués sur tous les repos touchés.
  - Annonce explicite du volume propagé.
- **Garde-fous & anti-patterns** :
  - ❌ Propager Notion → Markdown (viole [[Règles intrinsèques - LBP#R-001]]).
  - ❌ Modifier un WR-RD pour corriger une coquille au lieu de remonter au manuel ([[Règles de propagation - LBP#PROP-001]]).
  - ❌ Sauter la phase ECOSYSTEM-STATE (perte de traçabilité incrémentale).
  - ❌ Propagation silencieuse sans annonce du volume propagé (la propagation devient non vérifiable).
  - ❌ Commit local sans push immédiat sur tous les repos pertinents → filet de sécurité GitHub n'opère plus, risque de perte sur crash machine.
  - ❌ Batcher plusieurs phases en un seul commit ECOSYSTEM-STATE — un commit par phase de propagation.
  - ❌ Réordonner les phases (Markdown puis Notion puis renvois) — l'ordre est intrinsèque.
- **Articulation** : [[Règles intrinsèques - LBP#R-001]] (Markdown SoT — fondement de toute propagation), [[Règles intrinsèques - LBP#R-053]] (archivage), [[Règles intrinsèques - LBP#R-056]] (versioning), [[Règles intrinsèques - LBP#R-063]] (politique bump docs méta), [[Règles de propagation - LBP]] (toutes les PROP-XXX qui détaillent les cascades atomiques), [[#WF-011]] (URL Drive), [[#WF-012]] (indexation Notion), [[#WF-013]] (propagation Manuel→WR-RD), [[#WF-015]] (migration au canon), [[#WF-016]] (audit transverse), [[#WF-017]] (sync DDL), [[#WF-020]] (cascade template).
- **Origine** : 30-04-2026, formalisé après plusieurs cascades manuelles ad hoc lors des Phases 4-7 du chantier Brain v3 (manuels → WR-RD → Notion). Workflow orchestrateur transverse qui agrège les cascades atomiques [[Règles de propagation - LBP]].

## WF-011 : Récupérer l'URL Drive d'un fichier local du vault

- **Portée** : Transverse
- **Trigger** : Besoin d'obtenir l'URL Drive d'un fichier `.md` du vault pour la coller dans une propriété Notion (ex. `Lien vers le manuel de BDD (.md)`, `Lien vers le doc WR-RD (.md)`, `Lien vers la note de concept (.md)`, `Lien doc méta (source)`).
- **Préconditions** :
  - Google Drive for Desktop installé et synchronisé sur la machine.
  - Fichier cible présent et stabilisé dans `H:\Drive partagés\LBP - shared\Architecture data\`.
  - Fichier remonté côté Drive web (synchronisation effective vérifiable via le statut Drive de l'OS).
- **Étapes** :
  1. Identifier le `user_id` Drive for Desktop actif : ouvrir `C:\Users\<user>\AppData\Local\Google\DriveFS\`, repérer le sous-dossier numéroté dont les fichiers `mirror_metadata_sqlite.db-wal` ont une date de modification récente.
  2. Ouvrir la base SQLite `mirror_metadata_sqlite.db` en read-only (URI `file:<path>?mode=ro`).
  3. Exécuter une requête joignant `items` (filtrée sur `local_title`, `is_folder=0`, `trashed=0`) avec `stable_parents` (filtrée sur `parent_stable_id` du dossier actif). Le filtre par `parent_stable_id` évite les faux positifs liés à un homonyme dans `00 - archives/` ou autre dossier.
  4. Récupérer l'`id` du fichier ciblé dans le résultat.
  5. Construire l'URL au format `https://drive.google.com/file/d/{file_id}/view`.
  6. Pour un batch de N fichiers, faire **une seule** connexion SQLite avec une requête `IN (...)` plutôt que N connexions successives.
- **Sortie** :
  - URL Drive prête à coller dans la propriété Notion ciblée.
- **Garde-fous & anti-patterns** :
  - ❌ Filtrer uniquement par `local_title` sans le `parent_stable_id` du dossier actif → faux positifs si le fichier a un homonyme dans `00 - archives/` ou ailleurs.
  - ❌ Ouvrir la base SQLite en écriture → risque de corruption de la base de Drive for Desktop.
  - ❌ Échapper les caractères spéciaux des noms (apostrophes typographiques U+2019, tirets cadratins U+2014) → échec du match. Passer le `local_title` tel quel.
- **Articulation** : [[Règles intrinsèques - LBP#R-029]] (le doc Markdown est SoT pour l'indexation Notion), [[Règles intrinsèques - LBP#R-052]] (apostrophes typographiques uniformes dans les noms), [[#WF-012]] (indexation Markdown→Notion qui consomme l'URL).
- **Origine** : 24-04-2026, mini-batch 0 Twin v2, formalisé après plusieurs récupérations manuelles répétitives lors de l'indexation Notion.

---

# 6) Archives

Cette section accueille les workflows retirés du catalogue actif (caducs car remplacés par un nouveau workflow, par une cascade PROP, ou par une méthode de niveau supérieur ; portée disparue ; consolidation avec un autre WF). Les items archivés conservent leur ID immuable (jamais réutilisé) et restent lisibles ici pour traçabilité historique. Pour chaque item archivé, ajouter en tête : `**Archivé** : JJ-MM-YYYY — [raison]` et `**Remplacé par** : [[wikilink vers la cible]]`.

*(Aucun item archivé à v1.0.)*
