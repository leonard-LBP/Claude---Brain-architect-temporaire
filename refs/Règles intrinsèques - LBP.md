---
# === Identité ===
title: "Règles intrinsèques - LBP"
doc_type: doc_meta
code: "META_RULES_LBP"

# === Méta-gouvernance ===
version: "1.3"
template_code: "TPL_META_CATALOGUE"
template_version: "1.6"
created_at: "03-05-2026"
updated_at: "03-05-2026"

# === Spec d'usage ===
function_meta: "META.FUNCTION.NORMER"
item_id_prefix: "R"
summary: "Catalogue des règles atomiques R-XXX qui gouvernent l'écosystème LBP : règles d'architecture, de naming, de gouvernance documentaire, de propagation, de traçabilité, d'hygiène d'écriture, de doctrine Twin. Réceptacle canonique de toute capture de règle déclenchée par une découverte ou une décision."
purpose: "Référence canonique pour lookup d'une règle précise. Toute production ou modification structurante doit s'appuyer sur les règles applicables. Pour la doctrine narrative qui sous-tend les règles, voir [[Cadre - LBP]] (à produire en Phase 4) ; pour les décisions architecturales d'origine, voir [[Décisions architecturales - LBP]]."
aliases:
  - "RULES_LBP"
  - "Règles LBP"
  - "Catalogue de règles"
tags:
  - doc_meta
  - catalogue
  - rules
  - normer
  - lbp
---

# Règles intrinsèques - LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta LBP`).
> **Fonction systémique** : `META.FUNCTION.NORMER` (catalogue normatif des règles atomiques).
> **Public visé** : intervenants LBP (Leonard, Clément, futurs collaborateurs), agents (brain architect, agents d'analyse).

---

# 1) Vocation et périmètre

## 1.1 Vocation

Catalogue exhaustif des règles atomiques (R-XXX) qui gouvernent l'écosystème LBP — Brain, Digital Twin, Mission Ops, et docs méta transverses. Chaque règle est figée à un instant t avec son ID, sa portée, son why, son how to apply, ses exemples, ses articulations et sa date de découverte. Le doc est consulté par lookup ponctuel (« quelle est la règle pour X ? ») et par audit transverse (« quelles règles s'appliquent à ce type d'objet ? »).

## 1.2 Périmètre

**Inclus** :
- Règles structurantes de l'architecture LBP (frontières Brain/Twin/Mission Ops, propriétaire canonique unique, séparation des régimes de connaissance).
- Règles de codification, de nommage et de versioning des objets canoniques.
- Règles de production et d'instanciation des docs (templates, frontmatter, génération de BDD à partir d'un manuel).
- Règles de gouvernance documentaire (qualité, hygiène d'écriture, anti-asymétries, indexation Notion, lifecycle des fiches).
- Règles spécifiques de doctrine Twin (relations, sandboxes, 5D, lecture multi-niveaux, promotion sandbox→officielle).
- Règles transverses applicables à plusieurs domaines.

**Exclus** (anti-doublon, application [[#R-066]]) :
- Conventions de la collaboration Claude/Leonard (`C-XXX`) → vivent dans `CLAUDE.md` (scope Session).
- Décisions architecturales d'origine (`D-XXX`) → vivent dans `[[Décisions architecturales - LBP]]`.
- Workflows opérationnels (`WF-XXX`) → vivent dans `[[Workflows opérationnels - LBP]]`.
- Règles de propagation atomiques (`PROP-XXX`) → vivent dans `[[Règles de propagation - LBP]]`.
- Conventions de codification détaillées (formats de codes par type d'objet) → vivent dans `[[Codification - LBP]]`. Ce catalogue cite la grammaire (R-054) sans la redéfinir en détail.
- Règles pressenties non encore confirmées → vivent dans `RULES_BRAIN_TWIN-backlog.md` (scope Session, hors bundle).

## 1.3 Granularité d'item

- **1 R-XXX = 1 règle atomique**, indépendante des autres règles, exprimable comme une contrainte testable.
- Si une règle « grosse » regroupe plusieurs sous-contraintes indépendantes, la décomposer en N items.
- Si plusieurs règles partagent le même Why et le même How, les fusionner en 1 seul item avec exemples multiples.
- **Anti-pattern** : règle « fourre-tout » (portée trop large, How vague). Symptôme : impossible de citer un cas concret de violation.

---

# 2) Anatomie d'un item

## 2.1 Schéma des champs (figé v1.0)

| Champ | Type | Description | Exemple |
|---|---|---|---|
| ID | code | Format `R-XXX` (3 chiffres, extension à 4 si > 999). Immuable. | `R-066` |
| Nom | texte court | Titre lisible humain de la règle, 3-12 mots. | Propriétaire canonique unique (anti-doublon) |
| Portée | select | Brain / Twin / Mission Ops / Transverse / Contextuel | Transverse |
| Why | texte long | Pourquoi cette règle existe ; coût opérationnel si non appliquée. | Éviter la divergence entre contenu et index. |
| How to apply | texte long | Comment appliquer concrètement. Étapes numérotées si plusieurs. | Modifier le doc MD d'abord, puis aligner Notion. |
| Articulation | texte long | Liens vers règles voisines (wikilinks internes `[[#R-XXX]]`), décisions D-XXX, doctrines, conventions C-XXX. | [[#R-066]], [[#R-074]] |
| Exemples | texte long | Cas ✅ / ❌ illustratifs. | ✅ ... / ❌ ... |
| Conséquence si violation | texte long | Impact opérationnel concret de la violation. | Asymétrie silencieuse, propagation manuelle obligatoire. |
| Origine | texte court | Date `JJ-MM-YYYY` + 1 ligne de contexte d'émergence (peut être : audit, observation d'une violation, formalisation post-discussion, généralisation d'un anti-pattern, capture proactive en session — pas obligatoirement rattachée à un doc spécifique). | 03-05-2026, Phase 4, Leonard a flaggé Y en discussion. |

Tous les champs ci-dessus sont obligatoires (convention par défaut), à l'exception de `Articulation`, `Exemples`, `Conséquence si violation` qui peuvent être omis si non pertinents pour la règle (ex. règle isolée sans articulation directe).

## 2.2 Format de l'ID

- **Préfixe** : `R` (figé)
- **Numéro** : 3 chiffres (extension à 4 si dépassement de 999)
- **Incrément** : monotone, jamais réutilisé même après archivage d'une règle
- **Immuabilité** : un ID attribué ne change jamais. Une règle retirée conserve son ID (cf. §6 Évolution)

## 2.3 Mini-exemple d'un item bien formé

```
#### R-066 : Propriétaire canonique unique (anti-doublon)

- **Portée** : Transverse
- **Why** : Éviter qu'une même information structurante existe en N copies dans plusieurs docs, ce qui crée des asymétries silencieuses dès qu'une copie évolue.
- **How to apply** : Toute information structurante a un seul propriétaire canonique. Les autres docs peuvent la résumer ou la citer (wikilink), mais doivent pointer vers le propriétaire — jamais la redéfinir.
- **Articulation** : [[#R-001]] (Markdown SoT), [[#R-074]] (méthodes pour règles de maintenance), [[Constitution des docs méta - LBP]].
- **Exemples** : ✅ Liste des 11 BDDs Brain → propriétaire = [[Architecture - Brain]] / ❌ Dupliquer la liste dans Panorama et 3 Cadres.
- **Conséquence si violation** : N copies à mettre à jour à chaque modification, asymétries silencieuses, érosion de la cohérence.
- **Origine** : 03-05-2026, Phase 1.0 chantier docs méta, formalisation de la règle anti-doublon.
```

---

# 3) Garde-fous de cohérence

## 3.1 Avec [[Décisions architecturales - LBP]]

- **Garde-fou** : toute R-XXX doit pouvoir être rattachée à une (ou plusieurs) D-XXX qui la motive. Si une R-XXX n'a pas de décision d'origine identifiable, c'est probablement une convention informelle qui devrait être promue par une décision explicite avant capture.
- **Justification** : la boucle de gouvernance documentaire (cf. [[Constitution des docs méta - LBP]] §7) dit : Décision → Règle → Workflow. Sauter l'étape Décision crée des règles sans rationale auditable.

## 3.2 Avec [[Workflows opérationnels - LBP]]

- **Garde-fou** : un WF-XXX qui orchestre une opération **applique** les R-XXX pertinentes (citation par wikilink), il **ne les redéfinit pas**. Si un workflow contient une nouvelle contrainte qui n'est pas dans le catalogue de règles, c'est une R-XXX manquante à capturer.
- **Justification** : application directe de [[#R-066]].

## 3.3 Avec [[Règles de propagation - LBP]]

- **Garde-fou** : une PROP-XXX décrit une cascade entre objets (« si X change, propager vers Y »). Une R-XXX peut **invoquer** une PROP-XXX (ex. « après modification, appliquer [[Règles de propagation - LBP#PROP-008]] »), mais ne décrit pas elle-même la cascade.
- **Justification** : séparation propre des responsabilités catalogue vs propagation.

---

# 4) Récap tabulaire

| ID | Nom | Sous-section (§5.x) | Origine |
|---|---|---|---|
| R-001 | Source de vérité = doc Markdown | 5.1 Fondations doctrinales | Principe architectural originel |
| R-002 | Zero donnée client dans Core / Motor | 5.1 Fondations doctrinales | Principe architectural originel |
| R-039 | Aucun artefact de génération IA dans les docs LBP | 5.1 Fondations doctrinales | 25-04-2026 |
| R-065 | Définition opérationnelle d'un doc méta — frontière « gouverne plusieurs objets » | 5.1 Fondations doctrinales | 03-05-2026 |
| R-066 | Propriétaire canonique unique (anti-doublon) | 5.1 Fondations doctrinales | 03-05-2026 |
| R-074 | Règles de maintenance d'un type de doc → propriétaire canonique unique = méthode dédiée | 5.1 Fondations doctrinales | 03-05-2026 |
| R-005 | Code unique stable | 5.2 Codification, identifiants & nommage | Règle initiale |
| R-027 | Conventions de nommage des fichiers Brain/Twin | 5.2 Codification, identifiants & nommage | 24-04-2026 |
| R-043 | Cohérence stricte filename ↔ frontmatter `title` | 5.2 Codification, identifiants & nommage | 26-04-2026 |
| R-044 | Format de date `JJ-MM-YYYY` (transverse LBP) | 5.2 Codification, identifiants & nommage | 26-04-2026 |
| R-052 | Apostrophe typographique uniforme (U+2019) dans les noms | 5.2 Codification, identifiants & nommage | 27-04-2026 |
| R-054 | Codification universelle des objets Brain | 5.2 Codification, identifiants & nommage | 28-04-2026 |
| R-061 | Préférer les tirets simples `-` aux tirets cadratins `—` | 5.2 Codification, identifiants & nommage | 01-05-2026 |
| R-062 | Naming des fiches Docs méta LBP - éviter les noms ambigus | 5.2 Codification, identifiants & nommage | 01-05-2026 |
| R-064 | Naming des docs méta indexés (filename humain + code `META_*` + scope explicite) | 5.2 Codification, identifiants & nommage | 03-05-2026 |
| R-053 | Convention de renaming des docs archivés (suffix dans filename) | 5.3 Frontmatter & versioning | 28-04-2026 |
| R-055 | Frontmatter canon des docs Brain (3 zones balisées) | 5.3 Frontmatter & versioning | 28-04-2026 |
| R-056 | Grammaire de versioning des docs Brain (`X.Y`) | 5.3 Frontmatter & versioning | 28-04-2026 |
| R-063 | Politique de bump version pour les docs méta indexés dans BDD `Docs méta LBP` | 5.3 Frontmatter & versioning | 02-05-2026 |
| R-073 | Frontmatter YAML — envelopper en quotes tout item de liste contenant `:`, apostrophes typographiques ou `"` | 5.3 Frontmatter & versioning | 03-05-2026 |
| R-004 | Template obligatoire pour tout nouveau doc Brain | 5.4 Templates & instanciation | Principe architectural originel |
| R-040 | Toutes les instructions de génération vivent dans des blocs `@INSTR-*` | 5.4 Templates & instanciation | 26-04-2026 |
| R-045 | Source de vérité pour la génération d'une BDD = Manuel parent | 5.4 Templates & instanciation | 26-04-2026 |
| R-006 | Descriptions Notion ≤280 caractères | 5.5 Indexation Notion & lifecycle | Convention établie |
| R-008 | Statuts harmonisés | 5.5 Indexation Notion & lifecycle | Convention établie |
| R-026 | Archivage local par dossier thématique | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-029 | Le doc Markdown est source de vérité pour l'indexation Notion | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-030 | Double indexation d'une note de concept | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-031 | Alignement du code unique entre note de concept et glossaire | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-032 | Mise à jour plutôt que création pour une entrée existante | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-033 | Les descriptions de propriétés Notion sont des mini-prompts de remplissage | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-034 | Ordonnancement création puis relation (2 passes) | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-035 | Ordre d'indexation inter-types (graphe de dépendances) | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-036 | Le Code unique est l'identité ; MAJ en place tant que le code est stable | 5.5 Indexation Notion & lifecycle | 25-04-2026 |
| R-037 | Lecture complète du doc obligatoire avant indexation (pas de raccourci frontmatter) | 5.5 Indexation Notion & lifecycle | 24-04-2026 |
| R-038 | Identifiant pivot par type d'objet (taxonomies = code, autres = nom) | 5.5 Indexation Notion & lifecycle | 25-04-2026 |
| R-046 | Ordre de création des éléments d'une BDD sur Notion | 5.5 Indexation Notion & lifecycle | 26-04-2026 |
| R-047 | Convention d'ordering des propriétés Notion (Twin) | 5.5 Indexation Notion & lifecycle | 26-04-2026 |
| R-048 | Naming d'une BDD Notion = nom canonique simple | 5.5 Indexation Notion & lifecycle | 26-04-2026 |
| R-051 | Ordering des propriétés Notion via `update_view SHOW` (et non via l'ordre des `ADD COLUMN`) | 5.5 Indexation Notion & lifecycle | 27-04-2026 |
| R-007 | Taxonomies par codes | 5.6 Gouvernance taxos & WR-RD | Convention établie |
| R-028 | Cohérence manuel ↔ doc clefs de lecture | 6 Archives — remplacée par PROP-001 | 24-04-2026 |
| R-041 | Propagation Manuel de BDD → WR-RD obligatoire | 6 Archives — remplacée par PROP-001 | 26-04-2026 |
| R-042 | QA stricte d'égalité entre WR-RD et section 4 du manuel parent | 6 Archives — remplacée par PROP-001 | 26-04-2026 |
| R-058 | Aucune jumelle texte sur les BDDs Brain | 5.6 Gouvernance taxos & WR-RD | 28-04-2026 |
| R-057 | Discipline d'usage des backticks Markdown | 5.7 Hygiène d'écriture | 28-04-2026 |
| R-059 | Hygiène d'écriture des docs Brain - pas de bruit historique ni de spéculation future | 5.7 Hygiène d'écriture | 28-04-2026 |
| R-060 | Hygiène d'écriture des champs `summary` et `purpose` du frontmatter Brain | 5.7 Hygiène d'écriture | 28-04-2026 |
| R-067 | Libellés humains pour les valeurs de select / multi-select Notion | 5.7 Hygiène d'écriture | 03-05-2026 |
| R-068 | Aliases ne contiennent ni le code unique ni le nom canonique | 5.7 Hygiène d'écriture | 03-05-2026 |
| R-069 | Lecture complète du doc avant indexation dans une BDD Notion | 5.7 Hygiène d'écriture | 03-05-2026 |
| R-070 | Ban des noms d'agents dans les sources de vérité (Brain agent-agnostique) | 5.7 Hygiène d'écriture | 03-05-2026 |
| R-071 | Auto-suffisance des descriptions dans les sources de vérité | 5.7 Hygiène d'écriture | 03-05-2026 |
| R-072 | Pas d'énumération de taxons dans les instructions d'écriture / descriptions ≤280 | 5.7 Hygiène d'écriture | 03-05-2026 |
| R-075 | Vérification de cohérence inter-catalogues lors de l'ajout/modification d'item citant un autre catalogue | 6 Archives — remplacée par PROP-011 | 03-05-2026 |
| R-011 | Frontières fortes entre objets canoniques | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-012 | Séparation des 4 régimes de connaissance | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-013 | Sobriété relationnelle | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-014 | Règle absolue des sandboxes | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-015 | Jumelles textes systématiques | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-016 | La 5D est une matrice de lecture, jamais une preuve primaire | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-017 | Sobriété des rollups et formules | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-018 | Spécialisation des propriétés génériques à l'écriture | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-019 | Architecture en 5 couches d'une BDD bien spécifiée | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-020 | Traçabilité obligatoire des fiches importantes | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-021 | Distinction stricte fusionner / consolider / promouvoir | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-022 | Critères minimaux de promotion sandbox → BDD officielle | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-023 | Progressivité du remplissage | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-024 | Lecture du Twin sur 3 niveaux simultanés | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-025 | Tableau maître canonique obligatoirement tenu à jour | 5.8 Architecture & doctrine Twin | Panorama V2 v3 |
| R-049 | Déclaration obligatoire de la `ui_family` pour toute BDD Twin | 5.8 Architecture & doctrine Twin | 27-04-2026 |
| R-050 | Propriété conditionnelle `Lien vers la note avancée` (URL) | 5.8 Architecture & doctrine Twin | 27-04-2026 |
# 5) Catalogue

## 5.1 Fondations doctrinales

Règles axiomatiques structurantes qui définissent les frontières fondamentales de l'écosystème LBP et les principes de gouvernance documentaire.

#### R-001 : Source de vérité = doc Markdown

- **Portée** : Transverse
- **Why** : Éviter la divergence entre le contenu et son index. Le doc Markdown est portable, versionable, lisible IA ; Notion peut évoluer sans perte de contenu structurant. Sans cette règle, on aurait deux SoT en compétition (Notion vs Markdown) et tôt ou tard une asymétrie à propager manuellement.
- **How to apply** : Pour modifier un objet (manuel, taxonomie, note de concept, doc méta, template, etc.), on modifie d'abord le doc `.md` source, puis on aligne Notion. Jamais l'inverse. Notion sert de mirror d'index pour navigation, filtrage, relations bidirectionnelles natives — pas de stockage de contenu canonique.
- **Articulation** : [[#R-066]] (propriétaire canonique unique — R-001 est le cas particulier où le propriétaire canonique est toujours Markdown), [[#R-029]] (le doc Markdown est SoT pour l'indexation Notion), [[Constitution des docs méta - LBP]] §1.2.
- **Exemples** :
  - ✅ Renommer une propriété d'une BDD : modifier d'abord le manuel `.md`, puis renommer la propriété dans Notion via DDL.
  - ❌ Renommer une propriété directement dans Notion sans toucher au manuel — désynchronisation immédiate et silencieuse.
- **Conséquence si violation** : SoT incertaine, asymétries silencieuses Markdown ↔ Notion, agents et humains ne savent plus laquelle source faire foi.
- **Origine** : Principe architectural originel (avant captures formelles).

#### R-002 : Zero donnée client dans Core / Motor

- **Portée** : Transverse (frontière Brain / Twin / Mission Ops)
- **Why** : Le Brain est par construction réutilisable entre missions. Toute contamination par une donnée client = perte de réutilisabilité, fuite de confidentialité, et pollution du graphe de connaissance LBP avec des spécificités non transverses.
- **How to apply** : Les domaines Core et Motor du Brain ne contiennent jamais de données client (noms, profils, contenu missionnel, livrables clients). Seuls Digital Twin et Mission Ops sont instanciés par mission et peuvent contenir des données client. Si un exemple est nécessaire dans un doc Brain, il est fictif ou anonymisé.
- **Articulation** : [[Constitution des docs méta - LBP]] §4 (frontière Brain ↔ Mission), [[#R-012]] (séparation des 4 régimes de connaissance), `D-007` (zero contamination — décision d'origine).
- **Exemples** :
  - ✅ Note de concept « Capacité Organisationnelle » dans `Glossaire LBP` (transverse, sans contexte client)
  - ❌ Note de concept « Capacité Organisationnelle - Client X » dans `Glossaire LBP`
- **Conséquence si violation** : pollution du Brain par contexte client, perte de la propriété de réutilisabilité cross-mission, risque de fuite si export du Brain.
- **Origine** : Principe architectural originel.

#### R-039 : Aucun artefact de génération IA dans les docs LBP

- **Portée** : Transverse (tous les docs LBP : manuels, notes de concept, glossaire, taxonomies, prompts, méthodes, templates, frontmatters, contenus de fiches Notion).
- **Why** : Les générateurs IA (notamment ChatGPT/o1 avec sources web) laissent parfois des artefacts de citation ou de balisage qui ne devraient jamais apparaître dans le doc final. Ces artefacts cassent la lisibilité, polluent l'extraction sémantique, et trahissent un défaut de relecture avant publication.
- **How to apply** : Avant de finaliser ou publier tout doc LBP (vault, Notion, Drive), faire une **passe QA anti-artefacts** qui détecte et supprime au minimum :
  - `:contentReference[oaicite:N]{index=N}` (citation OpenAI/Bing brute)
  - `【N†source】` ou `[N†source]` (citations OpenAI tournée)
  - `[citation:N]`, `[ref:N]`, `[1]`, `[2]`... isolés sans bibliographie
  - `<sup>N</sup>` orphelins
  - Caractères de remplacement Unicode (`�`, `�`)
  - Balises markdown brisées (`**...` ou `[...](` non fermés)
  - Fragments de placeholders non résolus (`[[NOM_OBJET]]`, `<INSTR>...</INSTR>`)
  - Texte tronqué visible (phrases coupées en milieu)
- **Articulation** : [[#R-059]] (hygiène d'écriture — pas de bruit historique), [[#R-069]] (lecture complète avant indexation).
- **Exemples** :
  - ❌ `concept - Repères communs.md` : `Ils peuvent être symboliques [...] fonctionnels:contentReference[oaicite:5]{index=5}iguïtés en rendant visibles des attentes communes.` (artefact de citation + texte tronqué)
  - ❌ `concept - Soft skill.md` : `qualité des interactions, des décin collective.` (texte tronqué visible)
- **Conséquence si violation** : doc à corriger en source (vault) ET en cible (Notion), pollution de l'extraction sémantique, perte de crédibilité.
- **Origine** : 25-04-2026, Leonard, après détection en batch C de 2 occurrences sur 72 notes de concept.

#### R-065 : Définition opérationnelle d'un doc méta — frontière « gouverne plusieurs objets »

- **Portée** : Transverse
- **Why** : Sans définition opérationnelle, la frontière entre « doc méta » et « doc qui décrit un objet spécifique » est arbitraire. Risque d'inflation de la BDD `Docs méta LBP` (devient un grenier) ou inversement de manquer un doc qui mériterait l'indexation. Une règle frontière testable permet d'arbitrer rapidement et de manière reproductible.
- **How to apply** :
  1. **Un doc est méta s'il gouverne plusieurs objets, plusieurs BDD, plusieurs familles d'artefacts ou plusieurs workflows.** Cas typiques : doctrines transverses, règles, chartes, cartographies, constitutions.
  2. **Un doc n'est pas méta s'il décrit un objet, une BDD, une taxonomie, un prompt, une méthode ou un template spécifique.** Ces docs vivent dans leurs BDDs dédiées (`Manuels de BDD`, `Registre des taxonomies`, `Notes de Concept LBP`, `Prompts LBP`, `Méthodes LBP`, `Templates Brain`).
  3. **Cas limite** (charte spécifique mission) : n'est pas un doc méta LBP — vit dans Twin de la mission ou Mission Ops.
- **Articulation** : [[#R-066]] (propriétaire canonique unique — un doc méta a un périmètre clair pour appliquer R-066), [[Constitution des docs méta - LBP]] §2.
- **Exemples** :
  - ✅ Doc méta : `Codification - LBP` (gouverne tous les codes de tous les types d'objets)
  - ✅ Doc méta : `Workflows opérationnels - LBP` (gouverne plusieurs workflows transverses)
  - ❌ Pas un doc méta : `Manuel de BDD - Actifs` (décrit une seule BDD spécifique, vit en `Manuels de BDD`)
  - ❌ Pas un doc méta : `Méthode - Carte de causalité` (décrit une méthode spécifique, vit en `Méthodes LBP`)
- **Conséquence si violation** : BDD `Docs méta LBP` devient un grenier mal calibré, frontière flottante, indexation incohérente.
- **Origine** : 03-05-2026, Phase 1.0 chantier docs méta, formalisation de la règle frontière en complément de la définition narrative dans la Constitution.

#### R-066 : Propriétaire canonique unique (anti-doublon)

- **Portée** : Transverse
- **Why** : Quand une même information structurante existe en N copies dans plusieurs docs, chaque modification doit être propagée manuellement à N endroits — ce qu'on oublie systématiquement. Résultat : asymétries silencieuses, érosion de la cohérence, perte de confiance dans les SoT. Une seule SoT par information = une seule maintenance.
- **How to apply** : Toute information structurante a un seul propriétaire canonique. Les autres docs peuvent la résumer ou la citer (wikilink Obsidian `[[Doc cible]]`), mais doivent pointer vers le propriétaire — jamais la redéfinir. Cas typiques de propriétaires canoniques :
  - Liste des 11 BDDs Brain → `[[Architecture - Brain]]`
  - Champs exacts d'une BDD → manuel de BDD correspondant
  - Valeurs d'une taxonomie → mini-doc de taxonomie
  - Code d'un objet Brain → `[[Codification - LBP]]` + frontmatter du doc
  - Pourquoi une décision a été prise → `[[Décisions architecturales - LBP]]`
  - Comment appliquer une règle → ce catalogue ou `[[Workflows opérationnels - LBP]]`
- **Articulation** : [[#R-001]] (Markdown SoT — cas particulier), [[#R-074]] (méthodes pour règles de maintenance — application directe), [[Constitution des docs méta - LBP]] §5.
- **Exemples** :
  - ✅ `[[Panorama LBP]]` résume l'architecture du Brain mais renvoie à `[[Architecture - Brain]]` pour les 11 BDDs
  - ❌ Liste des 11 BDDs Brain dupliquée dans Panorama, 3 Cadres et 5 manuels (asymétrie garantie au moindre changement)
- **Conséquence si violation** : N copies de la même info à mettre à jour à chaque modification, asymétries silencieuses, propagation manuelle obligatoire.
- **Origine** : 03-05-2026, Phase 1.0 chantier docs méta, formalisation de la règle anti-doublon comme principe structurant de la Constitution des docs méta.

#### R-074 : Règles de maintenance d'un type de doc → propriétaire canonique unique = méthode dédiée

- **Portée** : Transverse — tous les types de docs canoniques LBP qui ont N instances partageant des règles de maintenance communes (catalogues, manuels de BDD, taxonomies, chartes, specs d'architecture, etc.).
- **Why** : Quand plusieurs instances d'un même type de doc partagent des règles de maintenance / d'évolution communes (stabilité du schéma, traçabilité, cycle de vie, anti-patterns transverses), embarquer ces règles dans chaque instance crée doublon × N, asymétrie inévitable à chaque enrichissement, couplage fort entre instances qui devraient rester indépendantes, et viole directement [[#R-066]]. Ces règles relèvent du savoir-faire opérationnel transverse au type de doc → leur propriétaire canonique est une **méthode** indexée dans la BDD `Méthodes LBP`.
- **How to apply** :
  1. **Méthode dédiée** dans BDD `Méthodes LBP` (ex. `Méthode - Maintenance d'un catalogue Brain.md`, `Méthode - Maintenance d'un manuel de BDD Brain.md`) = SoT des règles de maintenance pour le type de doc. Cette méthode est durable et capitalise les conventions issues du chantier de production / refonte du type.
  2. **Template** d'instanciation = guide la **génération initiale** d'une instance via son `TEMPLATE_USAGE_GUIDE` (qui peut citer la méthode pour la maintenance future). Le template ne reproduit pas les règles de maintenance dans les docs générés.
  3. **Doc canonique généré** = peut citer la méthode en footer via wikilink (« voir `[[Méthode - Maintenance d'un X Brain]]` »). N'embarque jamais une copie des règles.
  4. **Prompts maîtres et logic blocks** consommés par les agents (brain architect, autres) = artefacts opérationnels dérivés de la méthode, tenus à jour en permanence avec un niveau de détail technique. Eux portent les règles d'exécution effectives. La méthode reste la source de vérité doctrinale ; les prompts/logic blocks la matérialisent côté agent.
- **Articulation** : [[#R-066]] (propriétaire canonique unique — R-074 est une application directe au cas des règles de maintenance), [[#R-001]] (Markdown SoT), [[#R-040]] (templates : instructions dans @INSTR-*).
- **Exemples** :
  - ✅ Footer d'un catalogue : « Maintenance et évolution : voir `[[Méthode - Maintenance d'un catalogue Brain]]` »
  - ✅ Section dans la méthode : « Stabilité du schéma d'item, traçabilité, cycle de vie, anti-patterns » (SoT unique)
  - ✅ Logic block consommé par brain architect : implémentation technique des règles de maintenance dérivées de la méthode (mise à jour en continu)
  - ❌ Section « Bonnes pratiques d'écriture du catalogue » dupliquée dans chaque catalogue → propagation manuelle obligatoire à chaque enrichissement, asymétrie garantie
- **Conséquence si violation** : N copies du contenu transverse, asymétrie inévitable, dégradation de la cohérence à chaque évolution.
- **Origine** : 03-05-2026, lors de la production de TPL_META_CATALOGUE v1.3. Le template incluait une section §6 « Bonnes pratiques d'écriture du catalogue » destinée à être reproduite dans chaque catalogue généré. Leonard a flaggé : « risque fort de doublon avec des méthodes/règles d'utilisation qui vivraient autre part ; le maintien de la cohérence à travers l'évolution est fondamental ». Section §6 supprimée du template (v1.3 → v1.4) ; principe formalisé en R-074 ; méthodes correspondantes à produire en Phase 4 final.

## 5.2 Codification, identifiants & nommage

Règles structurantes sur les codes, identifiants stables, formats de dates, conventions de nommage des fichiers, apostrophes et tirets typographiques, et grammaire universelle de codification des objets Brain.

#### R-005 : Code unique stable

- **Portée** : Brain
- **Why** : Référencement stable entre BDD, résistance aux renommages. Sans cette règle, tout renommage d'objet casse les références cross-BDD.
- **How to apply** : Le code unique d'un objet Brain (ex: `CPT_GOV_SSOT`) ne change jamais, même si le nom canonique évolue. Un renommage produit un nouveau code + archivage de l'ancien (cf. [[#R-053]]).
- **Articulation** : [[#R-053]] (archivage en cas de rename), [[#R-054]] (codification universelle).
- **Origine** : Règle initiale (pré-formalisation Phase A4).

#### R-027 : Conventions de nommage des fichiers Brain/Twin

- **Portée** : Transverse
- **Why** : Homogénéité visuelle dans Obsidian, compatibilité clavier, interopérabilité inter-outils, cohérence fichier ↔ frontmatter (cf. [[#R-043]]).
- **How to apply** :
  - **Séparateur** : tiret simple `-` (jamais tiret cadratin `—`, jamais underscore). S'applique aux noms de fichiers ET aux champs `title` du frontmatter.
  - **Préfixe manuels de BDD** : `Manuel de BDD - X.md` (Title Case)
  - **Préfixe notes de concept** : `Concept - X.md` (Title Case, capitalisé)
  - **Préfixe WR-RD** : `WR-RD - X.md`
  - **Casse taxonomies** : code canonique, ex: `ACT.IMPACT_DOMAIN.md`
  - **Accents et apostrophes typographiques autorisés** dans le corps (Obsidian et Drive les gèrent)
  - **Caractères interdits Windows** (`<>:"/\|?*`) à éviter ; si le concept canonique contient `/` (ex. "Input / Output"), le filename utilise `-` à la place (ex. `Concept - Input - Output (LBP).md`).
- **Articulation** : [[#R-043]] (cohérence filename ↔ title), [[#R-061]] (tirets simples), [[#R-052]] (apostrophes typographiques).
- **Exemples** :
  - ✅ `Manuel de BDD - Relations inter-organisations.md`
  - ✅ `Concept - Poste.md`
  - ✅ `WR-RD - Actifs.md`
  - ✅ `ORG_REL.TYPE.md`
  - ❌ `Manuel de BDD — Actifs.md` (em dash banni)
  - ❌ `concept - Actif.md` (préfixe minuscule legacy)
  - ❌ `BDD_ACTIFS.md` (underscore)
- **Migration 26-04-2026** : 87 fichiers vault renommés en bulk + 100 frontmatters harmonisés (em dash → dash ASCII) lors de la cleanup Phase 6.
- **Origine** : 24-04-2026, standardisation lors de la migration Twin v2 (D-011) ; révisée 26-04-2026 pour intégrer [[#R-043]] et bannir l'em dash dans les filenames.

#### R-043 : Cohérence stricte filename ↔ frontmatter `title`

- **Portée** : Brain (manuels de BDD, notes de concept, WR-RD, méthodes, prompts, logic blocks, etc.)
- **Why** : Le `title` du frontmatter est la **source canonique de l'identité** du doc ; le nom de fichier doit refléter cette identité pour permettre une navigation cohérente, des liens cross-doc fiables et une lecture sans ambiguïté entre l'ouverture du fichier et son frontmatter. Un mismatch fichier ↔ title est une dette documentaire silencieuse.
- **How to apply** :
  - Pour tout doc Brain (hors taxonomies, voir exception ci-dessous), le nom de fichier doit être **strictement** la valeur du champ `title` du frontmatter, suivie de l'extension `.md`.
  - Si le `title` contient un caractère interdit en filename Windows (`<>:"/\|?*`), remplacer le caractère par `-` (cas standard `/` → ` - `) **dans le filename uniquement** ; le `title` du frontmatter conserve la formulation canonique.
  - Toute modification de `title` doit déclencher un renommage du fichier ; tout renommage de fichier doit être précédé d'une modification du `title` cohérente.
- **Exception : taxonomies** : le nom de fichier d'une taxonomie porte le `namespace_code` (ex: `ACT.IMPACT_DOMAIN.md`), pas le title. Le title humain reste lisible dans le frontmatter.
- **Articulation** : [[#R-027]] (conventions naming filename), [[#R-064]] (naming des docs méta).
- **Exemples** :
  - ✅ Fichier `Concept - Actif.md` ↔ `title: "Concept - Actif"` dans le frontmatter.
  - ✅ Fichier `Concept - Input - Output (LBP).md` ↔ `title: "Concept - Input / Output (LBP)"` (le `/` est autorisé dans le title, remplacé par ` - ` dans le filename).
  - ❌ Fichier `BDD - AGENTS LBP.md` ↔ `title: "Manuel de BDD - Agents LBP"` (mismatch ; à corriger en renommant le fichier).
- **Conséquence si violation** : navigation incohérente (le titre vu en haut du doc diffère du nom dans l'arborescence), liens cross-doc fragiles, perte de confiance dans l'identité des fichiers.
- **Origine** : 26-04-2026, Leonard, après audit de 114 mismatches dans le vault (manuels Brain en `BDD - X` au lieu de `Manuel de BDD - X`, notes en `concept - X` au lieu de `Concept - X`, manuels Twin avec em dash dans le title).

#### R-044 : Format de date `JJ-MM-YYYY` (transverse LBP)

- **Portée** : Transverse à tout l'écosystème LBP (Brain, Twin, Mission Ops, refs/, templates, scripts, frontmatters Obsidian, propriétés Notion textuelles, Logs/Révisions, exemples de contenu).
- **Why** : Cohérence visuelle francophone, lisibilité immédiate, alignement avec les conventions de l'écosystème LBP. Le séparateur `-` (dash ASCII) est préféré au `/` pour éviter les cassures de chemin et l'abus de barres obliques (déjà chargées de sens dans les paths, urls, taxonomies).
- **How to apply** : Toutes les dates affichées ou stockées en clair s'écrivent `JJ-MM-YYYY` (ex. `26-04-2026`). S'applique à : `created_at`, `updated_at`, `version_date` dans les frontmatters ; dates dans Logs/Révisions ; dates dans champs texte ; exemples de contenu dans manuels/WR-RD/templates.
- **Exception** : si une propriété Notion est typée `Date` natif, on conserve le type natif (le rendu est géré par Notion et localisé). Ne concerne donc que les **dates en texte clair**.
- **Migration** : règle appliquée going forward ; un sweep transverse des dates ISO `YYYY-MM-DD` héritées (notamment dans Logs/Révisions des manuels et `ECOSYSTEM-STATE.md`) est planifié ultérieurement, hors scope immédiat.
- **Articulation** : [[#R-055]] (frontmatter), [[#R-061]] (tirets simples — même logique de simplicité clavier).
- **Exemples** :
  - ✅ `created_at: "26-04-2026"` (frontmatter manuel ou WR-RD)
  - ✅ `| 26-04-2026 | Création du doc | v0.1.0 |` (ligne de log)
  - ❌ `created_at: "2026-04-26"` (format ISO interdit en texte clair)
  - ❌ `created_at: "26/04/2026"` (slash interdit)
- **Origine** : 26-04-2026, Leonard, lors de la finalisation des 28 WR-RD Twin v2 ; choix du dash ASCII pour éviter cassures et abus de `/`.

#### R-052 : Apostrophe typographique uniforme (U+2019) dans les noms

- **Portée** : Transverse à tout l'écosystème LBP - tous les noms de propriété, de BDD, de vue, et tout texte affiché aux utilisateurs (vault Obsidian, BDDs Notion, manuels, WR-RD, templates, taxonomies, frontmatters textuels). Concerne aussi bien le scope LBP que le scope Session.
- **Why** : Unicode définit deux apostrophes visuellement quasi identiques mais incompatibles pour le matching strict - l'apostrophe ASCII droite `'` (U+0027) et l'apostrophe typographique courbe `’` (U+2019). Sur Notion, créer une colonne `"Statut de l'objet"` (ASCII) et `"Statut de l’objet"` (typo) crée **deux propriétés distinctes** sans alerte ; idem côté manuels où une recherche/un diff strict produit des faux négatifs. C'est un trou de symétrie silencieux qui contamine l'audit Manuel ↔ Notion ↔ WR-RD.
- **How to apply** : Tous les noms de propriété, de BDD, de vue, et tout texte affiché utilisent l'apostrophe typographique `’` (U+2019). L'apostrophe ASCII `'` (U+0027) est strictement réservée au code (scripts Python, JSON, DDL SQL, regex) et ne doit **jamais** apparaître dans un nom affiché. En pratique :
  - Obsidian (autocorrect actif par défaut) : la conversion est automatique, RAS.
  - Notion : vérifier visuellement à chaque création de propriété, ou normaliser via `RENAME COLUMN` après création par DDL si le code source contenait un `'` ASCII.
  - Scripts Python générant du DDL : préférer `'’'` ou `’` littéral dans les chaînes destinées à Notion.
  - Outils de diff/audit : normaliser Unicode-insensible (déjà appliqué dans `parse_manuel.py` et `diff_manuel_notion.py` via `s.replace("’", "'").lower()`).
- **Articulation** : [[#R-061]] (tirets simples — distinct mais même registre typographique), [[CLAUDE.md#C-014]] (quirk wrapper MCP Notion : apostrophes ASCII dans payloads en lecture).
- **Exemples** :
  - ✅ `Statut de l’objet`, `Critère observable d’existence`, `Source(s) d’information (texte)`
  - ❌ `Statut de l'objet`, `Source(s) d'information (texte)` (ASCII U+0027 dans un nom affiché)
- **Conséquence si violation** : faux négatifs en audit (props non détectées comme dupliquées), divergence silencieuse Manuel ↔ Notion, retrievers / agents ne matchent pas le nom attendu.
- **Origine** : 27-04-2026, Leonard, après création par DDL de `Source(s) d'information (texte)` sur la BDD Capacités métier candidates sandbox avec apostrophe ASCII alors que le reste du schéma utilisait la typographique. Renommage immédiat puis formalisation de la règle.

#### R-054 : Codification universelle des objets Brain

- **Portée** : Transverse à tout l'écosystème Brain - manuels de BDD, WR-RD, taxonomies, notes de concept, templates, prompts, logic blocks, méthodes, docs méta, agents, outils externes, entries de glossaire. Phase 2 prévue pour Twin / Mission Ops (instances de mission).
- **Why** : Aujourd'hui les codes coexistent en 6+ conventions différentes (`DBMAN_X`, `CPT.X.LBP.Y`, `OBJ.STATUT.LBP`, `TPL_BRICK_X`, `METH_X`, etc.) avec mix de séparateurs (`_`, `.`, `-`) et suffix `LBP` parfois présent, parfois absent. Beaucoup de docs n'ont aucun code. Sans grammaire unifiée, les agents de maintenance et d'exploitation ne peuvent ni filtrer fiable par regex ni vérifier l'unicité cross-écosystème ni tracer les lignées template → instance.
- **How to apply** : Tout doc Brain porte un `code` dans son frontmatter, conforme à l'une des grammaires ci-dessous selon son type.

##### Grammaire 1 - Format général (tous les types de docs sauf taxonomies)

```
<PREFIXE>_<IDENTIFIANT>
```

- `<PREFIXE>` : 2-7 chars MAJUSCULES, identifie le type de doc selon la table de préfixes.
- `<IDENTIFIANT>` : alphanumérique MAJUSCULES, slug court issu du nom canonique du doc, séparateur interne `_` autorisé.
- Exemples : `DBMAN_TW_ACTIFS`, `CPT_SOFT_SKILL`, `PRMPT_M_REFACTOR`, `LGBLK_T_PRBC_PRBC`, `METH_CARTE_CAUSALITE`.

##### Grammaire 2 - Cas spécial taxonomies (format hiérarchique)

```
<NAMESPACE>.<TAXO>
```

- `<NAMESPACE>` : MAJUSCULES, racine du namespace (ex. `OBJ`, `CAP`, `ORG5D`, `META`, `BRICK`, `MET`, `OUT`, `AGENT`, `PROMPT`, `PLATFORM`).
- `<TAXO>` : MAJUSCULES, nom de la taxonomie au sein du namespace, peut contenir `_` (ex. `STATUT`, `FAMILY`, `ARCH_ROLE`, `DEPLOY_STATUS`).
- Exemples : `OBJ.STATUT`, `CAP.FAMILY`, `PROMPT.ARCH_ROLE`, `META.FUNCTION`, `LGBLK.FAMILY`.

**Justification du cas spécial** : les taxonomies ont une structure hiérarchique intrinsèque (`namespace.taxo`) qui est leur identité même, pas une description. Le namespace joue déjà le rôle de classifieur de premier niveau - équivalent fonctionnel d'un préfixe. Un agent voit `OBJ.STATUT` (format `XXX.YYY` avec point) → c'est sans ambiguïté une taxonomie.

##### Grammaire 3 - Codes de taxons (valeurs taxonomiques)

```
<NAMESPACE>.<TAXO>.<VALEUR>
```

- Hérite du code de la taxonomie parente, ajoute `.<VALEUR>`.
- `<VALEUR>` : MAJUSCULES, peut contenir `_`.
- Exemples : `OBJ.STATUT.BROUILLON`, `OBJ.STATUT.VALIDE`, `CAP.FAMILY.SOFT`, `META.FUNCTION.NORMER`.

##### Table de préfixes (Grammaire 1)

| Préfixe | Type de doc Brain | Taxo de référence | Sous-typage interne |
|---|---|---|---|
| `DBMAN_TW` | Manuel de BDD (Twin) | `DOC.TYPE` + `DBMAN.SCOPE.TWIN` | - |
| `DBMAN_MO` | Manuel de BDD (Mission Ops) | + `DBMAN.SCOPE.MISSION_OPS` | - |
| `DBMAN_BR` | Manuel de BDD (Brain) | + `DBMAN.SCOPE.BRAIN` | - |
| `WRRD_TW` | WR-RD (Twin) | `DOC.TYPE.WR_RD` + scope | - |
| `WRRD_MO` | WR-RD (Mission Ops) | idem | - |
| `WRRD_BR` | WR-RD (Brain) | idem | - |
| `CPT` | Note de concept | `DOC.TYPE.NOTE_CONCEPT` | - |
| `TPL` | Template d'instanciation | `DOC.TYPE.TEMPLATE_INSTANCIATION` | - |
| `TPL_BRICK` | Template de Brick | `DOC.TYPE.TEMPLATE_BRICK` | `BRICK.FAMILY` |
| `PRMPT_M` | Prompt maître | `DOC.TYPE.PROMPT` | `PROMPT.ARCH_ROLE.PROMPT_MAITRE` |
| `PRMPT_S` | System prompt | idem | `PROMPT.ARCH_ROLE.SYSTEM_PROMPT` |
| `PRMPT_U` | Prompt d'exécution | idem | `PROMPT.ARCH_ROLE.PROMPT_EXECUTION` |
| `PRMPT_T` | Template prompt | idem | `PROMPT.ARCH_ROLE.TEMPLATE_PROMPT` |
| `LGBLK` | Logic block | `DOC.TYPE.LOGIC_BLOCK` | `LGBLK.FAMILY` |
| `METH` | Méthode | `DOC.TYPE.METHODE` | `MET.FAMILY` |
| `META` | Doc méta (charte / doctrine / playbook) | `DOC.TYPE.DOC_META` | `META.FUNCTION` (5 valeurs) |
| `AGT` | Agent LBP | `DOC.TYPE.AGENT` | `AGENT.FAMILY` |
| `OUT` | Outil externe | `DOC.TYPE.OUTIL_EXTERNE` | `OUT.FAMILY` |
| `GLO` | Entry de glossaire | `DOC.TYPE.GLOSSAIRE_ENTRY` | - |
| (cas spécial) | Taxonomie | `DOC.TYPE.TAXONOMIE` | code = `<NAMESPACE>.<TAXO>` (Grammaire 2) |

##### Paire `CPT_*` ↔ `GLO_*` (note de concept ↔ entry de glossaire)

Un même concept LBP est **double-représenté** dans l'écosystème :
- comme **note de concept** (fichier Markdown source de vérité, indexée dans la BDD Registre des notes de concept) → code `CPT_<DOMAIN>_<TOKEN>`
- comme **entry de glossaire** (fiche normative dans la BDD Glossaire LBP, vue opératoire enrichie) → code `GLO_<DOMAIN>_<TOKEN>`

Les deux codes partagent **strictement le même `<DOMAIN>_<TOKEN>`**, ce qui matérialise la relation 1:1 entre la note et le glossaire :

| Concept | Note (Registre) | Glossaire |
|---|---|---|
| Individu | `CPT_TBD_INDIVIDU` | `GLO_TBD_INDIVIDU` |
| 3P | `CPT_FRAME_3P` | `GLO_FRAME_3P` |
| Connaissance | `CPT_KNOW_CONNAISSANCE` | `GLO_KNOW_CONNAISSANCE` |

**Doctrine** : le préfixe désigne le **type d'objet documentaire** (note Markdown vs fiche-glossaire normative), pas le concept. Le concept lui-même est désigné par le `<DOMAIN>_<TOKEN>` commun.

**Frontmatter Markdown** des notes de concept : porte le code `CPT_*` dans le champ `code` (identité de la note). Le code `GLO_*` correspondant n'est pas matérialisé dans le frontmatter Markdown (il vit côté Notion uniquement).

##### 8 règles transverses

1. **Stabilité absolue** : un code donné est immuable. Pour "renommer" un objet, on en crée un nouveau et on archive l'ancien ([[#R-053]]).
2. **Pas de date dans les codes** (jamais). La date est un attribut de l'objet (`created_at`, `updated_at`, etc.), pas une composante de son identité.
3. **Pas de famille / sous-famille variable dans le code** : sauf namespace stable des taxonomies. Famille = propriété frontmatter / BDD, pas dans le code.
4. **Pas de rattachement multi-contexte** dans le code : le code reflète le contexte de création canonique. Les rattachements multiples (multi-orga, multi-mission) sont gérés via propriétés relationnelles.
5. **Casse** : MAJUSCULES partout (dans le code).
6. **Séparateur** : selon la grammaire - `_` pour Grammaire 1, `.` pour Grammaires 2 et 3.
7. **Pas de suffix `LBP`** : implicite, l'écosystème est entièrement LBP. Allègement.
8. **Unicité globale cross-écosystème** : aucun code ne doit collisionner avec un autre, tous types et scopes confondus.

##### `template_code` dans le frontmatter

Tout doc généré depuis un template porte dans son frontmatter (zone Méta-gouvernance, cf. [[#R-055]]) :
- `template_code` : le code du template d'origine (ex. `TPL_DBMAN_TW`)
- `template_version` : version semver du template au moment de la génération (ex. `1.4`)

Permet l'audit de lignée structurelle (*"tous les docs avec `template_code: TPL_DBMAN_TW` doivent avoir `template_version >= 7.0`"*).

##### Phase 2 - Extension Twin / Mission Ops

Pour les objets d'instance (créés dans le cadre d'une mission client), grammaire étendue :

```
<PREFIXE_TYPE>_<CLIENT>_<MISSIONID>_<SLUG>
```

- `<CLIENT>` : code court 3-4 chars (`NUM`, `RC`, `KARI`)
- `<MISSIONID>` : code compact `M01`, `M02`...
- `<SLUG>` : MAJUSCULES, underscore autorisé dans le slug

Préfixes proposés (à figer en Phase 2) :

| Préfixe | Type | Exemple |
|---|---|---|
| `BRK` | Brick (instance) | `BRK_NUM_M02_PROFIL_ORG` |
| `MTG` | Meeting | `MTG_NUM_M02_KICKOFF1` |
| `ACT` | Action LBP | `ACT_NUM_M02_PREP_KICKOFF` |
| `SRC` | Source d'information | `SRC_NUM_M02_ENTRETIEN_CFO` |
| `IND` | Individu | `IND_NUM_M02_JDUPONT` |
| `ORG` | Organisation | `ORG_NUM_M02_NUMALIS` |
| `ACTF` | Actif | `ACTF_NUM_M02_CONTRAT_X` |

- **Articulation** : [[#R-005]] (code unique stable), [[#R-053]] (renaming via archivage), [[#R-055]] (frontmatter), [[#R-064]] (naming des docs méta).
- **Conséquence si violation** : faux positifs en audit, codes dupliqués, références cross-écosystème cassées, agents ne pouvant filtrer fiable par regex, ruptures de lignée template → instance.
- **Origine** : 28-04-2026, Leonard, en préparation du chantier de migration globale. Capturé après audit ciblé des taxonomies Brain et arbitrages collaboratifs sur la grammaire.

#### R-061 : Préférer les tirets simples `-` aux tirets cadratins `—`

- **Portée** : Transverse à tout l'écosystème LBP - vault Markdown (titres, noms canoniques, corps des docs), fiches Notion (Nom canonique, Description, autres champs textuels), tout texte affiché. Concerne aussi bien le scope LBP que le scope Session.
- **Why** : Les caractères cadratins `—` (U+2014) et demi-cadratins `–` (U+2013) ne sont pas directement accessibles au clavier français. Leur saisie ralentit la production de docs. Ils créent aussi des asymétries dans les recherches (un grep `-` ne retrouve pas un `—`). Le tiret simple `-` (U+002D) est universellement disponible, lisible et rétro-compatible.
- **How to apply** :
  - Dans tout texte produit (docs Markdown, fiches Notion, frontmatter, commits) : utiliser `-` (U+002D) à la place de `—` ou `–`.
  - Pour les usages typographiques où un tiret long est sémantiquement attendu (incise, énumération), utiliser `-` simple suivi/précédé d'un espace : `Texte - incise - suite` au lieu de `Texte — incise — suite`.
  - Si on hérite d'un doc avec des `—` (ex. fichiers archivés ou import de doc tiers) : migration au fil de l'eau (sed `—` → `-`) lors de la prochaine modification.
- **Hors scope (à conserver)** :
  - **Flèches** `→` (U+2192), `↔` (U+2194), `↕` (U+2195), `←` (U+2190) : sémantiquement non substituables (schémas techniques, articulations doctrinales). Conservées.
  - **Apostrophes typographiques** `’` (U+2019) : restent obligatoires ([[#R-052]], indépendant).
  - **Symboles techniques** `≥`, `≤`, `≠`, `±`, `°`, etc. : conservés si pertinents.
- **Articulation** : Extension de [[CLAUDE.md#C-010]] (préférer caractères latins simples accessibles au clavier). Complémentaire à [[#R-052]] (apostrophes typographiques obligatoires) - traitent de caractères différents avec des doctrines différentes (cadratin = à éviter, apostrophe typographique = à préférer).
- **Exemples** :
  - ✅ `Panorama LBP - Macro-architecture de l'écosystème` (titre fiche Notion)
  - ✅ `R-061 - Préférer les tirets simples` (titre section)
  - ✅ `Brain → Twin` (flèche conservée)
  - ❌ `Panorama LBP — Macro-architecture` (cadratin)
  - ❌ `R-061 — Préférer` (cadratin)
- **Origine** : 01-05-2026, Leonard, lors de la création de la 1ère fiche Notion du bundle docs méta - confirmation explicite « on n'utilise plus de tirets `—`, on utilise `-` à la place ».

#### R-062 : Naming des fiches Docs méta LBP - éviter les noms ambigus

- **Portée** : Brain - BDD `Docs méta LBP` (et par extension toute BDD Brain qui accueille des fiches de typologie hétérogène : Méthodes LBP, Templates de Bricks, Outils externes, Agents LBP, Logic blocks, où le nom doit rester univoque même quand la BDD se peuple).
- **Why** : La BDD `Docs méta LBP` accueille dans le temps de nombreuses doctrines (chartes graphiques, chartes rédactionnelles, conventions de nommage, règles de modélisation, workflows de production, politiques de confidentialité, etc.). Si on nomme une fiche `Règles LBP` ou `Doctrine LBP` sans qualificatif, elle devient ambiguë dès qu'une autre fiche thématiquement proche apparaît (ex. `Règles graphiques LBP`, `Règles de confidentialité LBP`). Les noms ambigus dégradent le routage agent et la recherche humaine.
- **How to apply** : Le `Nom canonique` d'une fiche Docs méta (et plus largement Brain Motor) doit rester **univoque par construction**, en intégrant un qualificatif précisant la spécificité du contenu. Pattern recommandé : `<Nom + qualificatif précisant la spécificité>`.
  - Si le nom seul est déjà univoque (ex. `Codification - LBP`, `Panorama - LBP`) : pas besoin de qualificatif supplémentaire.
  - Si le nom seul est trop générique (ex. `Règles - LBP`, `Doctrine - LBP`, `Workflows - LBP`) : ajouter un qualificatif (ex. `Règles intrinsèques - LBP`, `Cadre - LBP`, `Workflows opérationnels - LBP`).
  - Si le nom seul est ambigu sur le périmètre : préciser le domaine (ex. `Architecture - Brain`, `Cadre - Twin`).
- **Articulation avec la Fonction systémique** : la fonction (taxo `META.FUNCTION`) **typifie** la fiche (Orienter / Expliquer / Structurer / Normer / Opérer). Le `Nom canonique` **précise la spécificité** dans cette fonction. Les deux jouent ensemble pour lever toute ambiguïté.
- **Articulation** : [[#R-064]] (naming des docs méta - règle complémentaire), [[#R-066]] (propriétaire canonique unique).
- **Exemples** :
  - ✅ `Règles intrinsèques - LBP` (Fonction : Normer) - distinct des futures règles graphiques ou de confidentialité
  - ✅ `Cadre - Twin` (Fonction : Expliquer) - périmètre Twin clair
  - ✅ `Architecture - Brain` (Fonction : Structurer) - périmètre Brain clair
  - ❌ `Règles LBP` - ambigu (règles de quoi ?)
  - ❌ `Doctrine LBP` - ambigu (toute fiche Docs méta est une doctrine)
- **Conséquence si violation** : confusion au lookup (humain ou agent), risque de doublons silencieux quand de nouvelles fiches arrivent.
- **Origine** : 01-05-2026, Leonard, lors du naming du bundle docs méta initial - anticipation de l'arrivée future de chartes graphiques / rédactionnelles / etc. dans la BDD `Docs méta LBP`.

#### R-064 : Naming des docs méta indexés (filename humain + code `META_*` + scope explicite)

- **Portée** : Brain — tous les docs méta indexés dans BDD `Docs méta LBP`.
- **Why** : Lever toute ambiguïté visuelle entre code (forme programmatique pour audits/scripts) et nom canonique (forme humaine pour navigation et lecture). Sans règle stricte, on tombe vite dans des asymétries (filename `DOC_MAP_META_LBP.md` vs title « Constitution des docs méta - LBP » vs Notion « Docs map ») qui dégradent la maintenabilité et l'agent-friendliness.
- **How to apply** : un doc méta indexé respecte 3 niveaux distincts mais corrélés :
  1. **Filename** = strictement identique au `title:` du frontmatter = strictement identique au `Nom canonique` côté Notion. Forme **humaine** : `<Type lisible> - <Scope>.md`. Exemples : `Constitution des docs méta - LBP.md`, `Cadre - Twin.md`, `Quality control - Brain.md`. **Aucun code dans le filename.**
  2. **Code** (frontmatter `code:` + Notion `Code unique`) : forme **programmatique** au format `META_<TOKEN>_<SCOPE>`. Préfixe `META_` obligatoire (cf. D-024, remplace l'historique `CHRT_`). `<TOKEN>` en MAJUSCULES `[A-Z0-9_]+`. `<SCOPE>` au choix selon le périmètre (cf. point 3).
  3. **Scope** dans le code (suffix obligatoire) :
     - `_LBP` si le doc est **transverse** (concerne Brain + Twin + Mission Ops + écosystème global). Exemples : `META_RULES_LBP`, `META_PANORAMA_LBP`, `META_CODIFICATION_LBP`.
     - `_BRAIN` / `_TWIN` / `_MO` si le doc concerne un **domaine spécifique**. Exemples : `META_CADRE_TWIN`, `META_QC_BRAIN`, `META_SPECS_ARCHITECTURE_MO`.
     - **Jamais de doublon `_LBP` + scope domaine** (ex. `META_CADRE_TWIN_LBP` est interdit — on choisit l'un ou l'autre).
- **Aliases (frontmatter)** : tout doc méta susceptible d'être cité sous plusieurs formes ou renommé doit déclarer ses `aliases:` (ancien nom, variantes courantes, code historique). Cohérent avec [[CLAUDE.md#C-024]] (résilience au rename via Obsidian UI).
- **Articulation** : [[#R-052]] (apostrophes typographiques), [[#R-053]] (archivage si rename de code), [[#R-054]] (codification), [[#R-061]] (tirets simples), [[#R-062]] (naming univoque), [[#R-063]] (bump version), `D-024` (préfixe `META_`).
- **Exemples** :
  - ✅ Filename `Cadre - Twin.md`, code `META_CADRE_TWIN`, scope `_TWIN`
  - ✅ Filename `Règles intrinsèques - LBP.md`, code `META_RULES_LBP`, scope `_LBP` (transverse)
  - ✅ Filename `Quality control - Brain.md`, code `META_QC_BRAIN`, scope `_BRAIN`
  - ❌ Filename `META_CADRE_TWIN.md` (code dans le filename — interdit)
  - ❌ Filename `Cadre Twin.md` (manque le séparateur tiret-espace)
  - ❌ Code `META_CADRE_TWIN_LBP` (doublon scope)
  - ❌ Code `CHRT_CADRE_TWIN` (préfixe historique, à migrer)
- **Conséquence si violation** : asymétrie entre filename / title / Notion → confusion humaine, casse les audits programmatiques qui s'appuient sur le filename ou le code, dégrade la lisibilité du file explorer Obsidian.
- **Origine** : 03-05-2026, Phase 1.0 du chantier d'architecture des docs méta. Leonard a flaggé la divergence filename `DOC_MAP_META_LBP.md` vs title « Constitution des docs méta - LBP » sur le premier doc créé selon la nouvelle convention.

## 5.3 Frontmatter & versioning

Règles structurantes sur le frontmatter en 3 zones balisées, la grammaire de versioning `X.Y`, l'archivage par renaming, la politique de bump pour les docs méta indexés et la robustesse YAML du frontmatter.

#### R-053 : Convention de renaming des docs archivés (suffix dans filename)

- **Portée** : Transverse à tout le vault `Architecture data/` - manuels de BDD, WR-RD, taxonomies, notes de concept, templates, méthodes, prompts, logic blocks, chartes, playbooks, et tout doc Markdown susceptible d'être archivé.
- **Why** : Le statut actif/archivé d'un doc dépendait jusqu'ici uniquement de son **dossier** (`00 - archives/`). Risque concret : un agent (ou un humain) qui recherche par nom (`Glob "**/Manuel de BDD - Actifs.md"`, search Obsidian/Drive) tombe sur 1 actif + N archivés homonymes et peut confondre / citer une version archivée comme source vérifiée. C'est un trou de discoverability silencieux qui peut générer des erreurs.
- **How to apply** :
  - **Format de renaming** : `<nom canonique> (archivé v<X> le JJ-MM-YYYY).md` si la version est connue, sinon `<nom canonique> (archivé le JJ-MM-YYYY).md`. Le format de version `<X>` suit [[#R-056]] (grammaire `MAJOR.MINOR`).
  - **3 actions atomiques** lors de l'archivage :
    1. **Filename** : ajouter le suffix `(archivé [v<X> le ]JJ-MM-YYYY)` avant l'extension
    2. **`title` frontmatter** : aligner sur le filename ([[#R-043]], cohérence filename ↔ title)
    3. **Déplacement** : vers `00 - archives/` du dossier parent (pratique existante, double signal conservé)
  - **Date** : format JJ-MM-YYYY ([[#R-044]]), date réelle d'archivage du jour
  - **Version** : extraite du frontmatter `version:` quand présente (`1.0` → `v1.0` dans le suffix), omise sinon
- **Articulation** : [[#R-027]] (conventions naming), [[#R-043]] (cohérence filename↔title), [[#R-044]] (format date), [[#R-056]] (versioning).
- **Exemples** :
  - ✅ `Manuel de BDD - Actifs (archivé v1.0 le 26-04-2026).md` (version connue)
  - ✅ `Concept - Soft skill (archivé le 26-04-2026).md` (version absente)
  - ✅ `OBJ.STATUT (archivé le 26-04-2026).md`
  - ❌ `Manuel de BDD - Actifs.md` dans `00 - archives/` (filename non renommé - état pré-R-053)
- **Edge cases** :
  - Doc archivé plusieurs fois (v1 puis v2) : 2 fichiers cohabitent sans collision (`...(archivé v1.0 le X).md` + `...(archivé v2.0 le Y).md`)
  - Doc sans frontmatter : renommer filename uniquement, pas d'alignement title
  - Doc avec nom déjà ambigu (`Sans titre.md`) : flag manuel, ne pas auto-renommer
- **Regex de validation** : `\(archivé( v\d+\.\d+)? le (\d{2}-\d{2}-\d{4})\)\.md$` (post [[#R-056]] : version au format `MAJOR.MINOR`)
- **Date forfaitaire pour rétroactif** : `26-04-2026` (date du sweep d'archivage massif Phase 1-4 documenté dans `ECOSYSTEM-STATE.md`).
- **Conséquence si violation** : confusion de search, citation d'archives obsolètes comme sources vérifiées, erreurs silencieuses dans les pipelines IA qui consomment le vault.
- **Origine** : 28-04-2026, Leonard, en préparant le chantier d'indexation Brain. Formalisation immédiate avant migration des 212 fichiers déjà archivés.

#### R-055 : Frontmatter canon des docs Brain (3 zones balisées)

- **Portée** : Transverse à tout doc Brain instancié dans l'écosystème (manuels, WR-RD, taxos, notes de concept, templates, prompts, logic blocks, méthodes, docs méta, agents, outils externes, glossaire).
- **Why** : Le frontmatter sert simultanément 3 publics distincts (agents de gouvernance, agents de maintenance, agents d'usage qui consomment le doc) qui n'ont pas les mêmes besoins. Sans structure claire, le frontmatter devient une soupe illisible et les agents se mélangent les pinceaux. La structure en 3 zones balisées rend explicite la séparation des préoccupations sans rien retirer du frontmatter.
- **How to apply** : Tout frontmatter Brain est structuré en **3 zones balisées par commentaires YAML** :

```yaml
---
# === Identité ===
title: "..."
doc_type: ...
code: "..."

# === Méta-gouvernance ===
version: "1.0"            # format X.Y (R-056)
template_code: "..."
template_version: "X.Y"   # format X.Y (R-056)
created_at: "JJ-MM-YYYY"
updated_at: "JJ-MM-YYYY"

# === Spec d'usage ===
summary: "..."
purpose: "..."
tags: [...]
# + champs spécifiques au type
---
```

##### Champs obligatoires

| Zone | Champ | Type | Notes |
|---|---|---|---|
| Identité | `title` | string | affichage humain |
| Identité | `doc_type` | enum | **token MAJUSCULES** correspondant à un taxon de la taxonomie `DOC.TYPE`. Valeurs autorisées : `MANUEL_BDD`, `WR_RD`, `NOTE_CONCEPT`, `TAXONOMIE`, `TEMPLATE_INSTANCIATION`, `TEMPLATE_BRICK`, `PROMPT`, `LOGIC_BLOCK`, `METHODE`, `DOC_META`, `AGENT`, `OUTIL_EXTERNE`, `GLOSSAIRE_ENTRY`. Validation regex : `^[A-Z_]+$`. |
| Identité | `code` | string | conforme [[#R-054]] |
| Méta-gouvernance | `version` | string | format `MAJOR.MINOR` selon [[#R-056]] (ex. `"1.0"`, pas de PATCH) |
| Méta-gouvernance | `template_code` | string | code du template d'origine ([[#R-054]]) - obligatoire pour docs générés depuis un template |
| Méta-gouvernance | `template_version` | string | format `MAJOR.MINOR` selon [[#R-056]], version du template au moment de la génération |
| Méta-gouvernance | `created_at` | string | format JJ-MM-YYYY ([[#R-044]]) |
| Méta-gouvernance | `updated_at` | string | format JJ-MM-YYYY ([[#R-044]]) - **règle obligatoire** : à bumper à chaque modification, même mineure |
| Spec d'usage | `summary` | string | description courte du **contenu** ("qu'est-ce que c'est") |
| Spec d'usage | `purpose` | string | raison d'être / objectif fonctionnel ("à quoi ça sert") |
| Spec d'usage | `tags` | list | indexation |

##### Hors frontmatter (volontairement)

- **`status`** : vit en BDD Brain uniquement. Statut bouge agilement (brouillon → à revoir → validé → archivé), maintenir le doublon frontmatter ↔ BDD est coûteux et non rigoureux.
- **`Logs / Révisions LBP`** : vit en BDD Brain (champ propre) ou git log. Verbose, multi-lignes, mauvais candidat pour le frontmatter.

##### Champs spécifiques par type (dans Spec d'usage)

| Type | Champs additionnels |
|---|---|
| Manuel BDD | `bdd_canonical_name`, `object_type`, `architecture_family/scope`, `knowledge_regime`, `officiality_regime`, `has_advanced_note` (Twin), `mission_ops_family`, `execution_tracking` (Mission Ops) |
| WR-RD | `target_bdd_canonical_name`, `target_bdd_code`, `parent_manual`, `wr_rd_code`, `domain` |
| Taxonomie | `canonical_name`, `namespace_code`, `is_open`, `open_policy`, `scale_kind`, `is_ordinal`, `selection_mode`, `cardinality`, `aliases`, `keywords`, `detection_clues` |
| Note de concept | `concept_code`, `canonical_name`, `aliases`, `keywords`, `detection_clues`, `anti_confusions` |
| Prompt | `prompt_code`, `target_function`, `intended_agent` |
| Logic block | `logic_block_code`, `operation`, `target_scope` |

Note : pour les taxonomies, `code` (zone Identité) et `canonical_name` peuvent être redondants (`OBJ.STATUT` partout). C'est volontaire pour cohérence transverse.

##### Règle obligatoire `updated_at`

À chaque modification d'un doc (même mineure : correction typo, ajout d'un mot, mise à jour d'un exemple), le champ `updated_at` du frontmatter doit être bumpé à la date du jour (format JJ-MM-YYYY, [[#R-044]]).

Pour fiabilisation future : un hook git pre-commit peut être ajouté pour bumper automatiquement la date sur les fichiers modifiés.

- **Articulation** : [[#R-044]] (format date), [[#R-054]] (codification), [[#R-056]] (versioning), [[#R-073]] (YAML frontmatter robuste).
- **Conséquence si violation** : frontmatter incohérent entre docs, agents qui ne trouvent pas les champs attendus, audit Brain ↔ vault impossible, perte de la traçabilité de lignée template.
- **Origine** : 28-04-2026, Leonard, après audit factuel des frontmatter de toutes les typologies (sub-agent `frontmatter_audit_report.md`) qui a révélé 3 anomalies majeures, 5 templates sans bloc B, double frontmatter visuel sur 2 templates, et asymétries Twin / Mission Ops.

#### R-056 : Grammaire de versioning des docs Brain (`X.Y`)

- **Portée** : Transverse à tout doc Brain (manuels, WR-RD, taxos, notes de concept, templates, prompts, logic blocks, méthodes, docs méta, agents, outils externes, glossaire). Concerne le champ `version` du frontmatter ([[#R-055]]).
- **Why** : Avant cette règle, le versioning des docs LBP était incohérent (généré au fil de l'eau par différents agents, mix de formats `1.0.0`, `0.3.0`, `07-04-2026 v0.5.0` mélangeant date et semver). Le format semver complet `X.Y.Z` (3 niveaux) est inutilement complexe pour des docs (le PATCH est typique des APIs où les bug fixes sont sémantiquement distincts des features - pour un doc, "correction de typo" et "ajout d'une phrase" peuvent toutes deux être MINOR sans gain à les distinguer).
- **How to apply** : Tout doc Brain porte une `version` au format `<MAJOR>.<MINOR>` (2 niveaux, pas de PATCH).

##### Format

```
<MAJOR>.<MINOR>
```

- Entiers naturels, séparés par `.`
- Pas de zéro-padding (`1.0`, pas `01.00`)
- Pas de PATCH (3e niveau interdit dans les docs Brain)

##### Règles de bump

**MAJOR bump** (`X` → `X+1.0`) : refonte structurelle
- Ajout, suppression ou réorganisation de sections H1 ou H2
- Changement du frontmatter structurel (champs obligatoires changent)
- Changement du sens canonique du doc (`purpose` / `summary` réécrit)
- Migration vers un nouveau template avec `template_version` MAJOR différent
- Pour un template : signale que **les docs générés depuis les versions précédentes deviennent stale et doivent être migrés**

**MINOR bump** (`X.Y` → `X.Y+1`) : enrichissement compatible
- Corrections de typos, fautes, ajustements éditoriaux
- Ajouts de contenu dans une section existante
- Enrichissements de tableaux, exemples
- Mises à jour de taxonomies citées
- Toute modification qui n'altère pas la structure ni le sens canonique

##### Création

À la création d'un doc, `version` initiale = `1.0` (pas `0.1`, pas `0.0`).

##### Cas spécifique des templates

Pour un template, le MAJOR bump est **structurellement important** : il indique que les docs générés à partir des versions précédentes doivent être migrés (mise à jour structurelle). Le `template_version` dans le frontmatter des docs générés ([[#R-055]]) permet d'auditer mécaniquement la lignée et de détecter les docs stale.

##### Migration des versions existantes

Pour les docs déjà existants qui portent un format `X.Y.Z`, la migration consiste à **tronquer le PATCH** (sans bumper) :

| Version actuelle | Version migrée |
|---|---|
| `1.0.0` | `1.0` |
| `0.3.0` | `0.3` |
| `6.3.0` | `6.3` |
| `07-04-2026 v0.5.0` (anti-pattern) | `0.5` + `created_at: "07-04-2026"` séparé |

C'est une migration de format pure (pas un changement de contenu) : la version reste la même, juste reformattée.

##### Impacts cascade sur autres règles

- [[#R-053]] (filename des archives) : le suffix `(archivé v<X> le JJ-MM-YYYY)` utilise désormais le format `X.Y` (au lieu de `X.Y.Z`).
- [[#R-055]] (frontmatter canon) : le champ `version` suit R-056 (`X.Y`).
- **`template_version`** : suit également R-056 (`X.Y`).

- **Articulation** : [[#R-053]] (archivage), [[#R-055]] (frontmatter), [[#R-063]] (politique bump docs méta indexés).
- **Conséquence si violation** : versions illisibles ou ambiguës, audit de lignée template impossible, agents incapables de distinguer refonte et correction.
- **Origine** : 28-04-2026, Leonard, en challengeant la convention semver `X.Y.Z` héritée par défaut. Constat : aucune convention de versioning n'a jamais été formalisée dans LBP, les versions actuelles ont été générées à la volée par différents agents sans règle commune, donc on n'est pas tenu de suivre semver. Décision : passer à `X.Y` plus simple et adapté aux docs.

#### R-063 : Politique de bump version pour les docs méta indexés dans BDD `Docs méta LBP`

- **Portée** : Brain - tous les docs méta indexés dans BDD `Docs méta LBP` (Règles intrinsèques, Décisions architecturales, Panorama, Cadres, Workflows opérationnels, Architecture Brain/Twin/MO, Codification, Règles de propagation, et tout futur doc méta indexé).
- **Why** : Les docs méta indexés évoluent en continu (capture de R-XXX, D-XXX, WF-XXX, refonte de sections). Sans politique de bump claire, soit (a) la version reste figée à 1.0 indéfiniment et perd toute valeur d'audit, soit (b) elle est bumpée à chaque virgule et le champ `Version du document` côté Notion devient un signal bruité. R-063 codifie un seuil de granularité.
- **How to apply** : suivre [[#R-056]] (format `X.Y`) avec les paliers suivants :
  - **Patch (1.0 → 1.1, 1.1 → 1.2, etc.)** : ajout d'une nouvelle entrée atomique (R-XXX, D-XXX, WF-XXX, PROP-XXX) sans refonte. Reformulation mineure d'une entrée existante. Mise à jour d'un exemple, d'une découverte, d'une articulation.
  - **Minor (1.X → 2.0, 2.X → 3.0, etc.)** : refonte d'une section entière. Ajout/suppression d'une section structurante. Changement de doctrine sur un sujet déjà traité.
  - **Pas de bump** : typo, correction orthographique, ajustement de mise en forme sans impact sémantique.
- **À chaque bump** : (i) modifier `version` dans le frontmatter ; (ii) modifier `updated_at` à la date du jour ; (iii) propager à la fiche Notion `Docs méta LBP` correspondante (`Version du document`, `updated_at`) ; (iv) rafraîchir le miroir `refs/<DOC>.md` du repo collab.
- **Articulation** : [[#R-001]] (Markdown SoT), [[#R-029]] (indexation Notion), [[#R-056]] (format `X.Y`).
- **Exemples** :
  - ✅ Capture de R-073 dans Règles intrinsèques : 1.0 → 1.1
  - ✅ Refonte complète d'une section structurante : 1.X → 2.0
  - ❌ Correction d'une coquille « lex » → « les » : pas de bump
- **Conséquence si violation** : `Version du document` bruitée côté Notion, audit de lignée stale impossible, perte de la valeur de signal du champ.
- **Origine** : 02-05-2026, arbitrage Leonard sur D1/D3 architecture des docs méta : besoin de codifier le critère de bump après que (a) le vault Architecture data est devenu source de vérité unique pour les docs méta (en application de [[#R-001]]), (b) la fiche Notion `Docs méta LBP` doit refléter les évolutions des docs sous-jacents.

#### R-073 : Frontmatter YAML — envelopper en quotes tout item de liste contenant `:`, apostrophes typographiques ou `"`

- **Portée** : Transverse — tout doc Markdown LBP avec frontmatter YAML (manuels de BDD, WR-RD, taxonomies, notes de concept, docs méta, templates).
- **Why** : Le parser YAML interprète tout `:` suivi d'un espace comme un séparateur clé/valeur. Si un item de liste contient un `:` non échappé (ex. `- VÉRIFIER (cf. R-072) : "à créer"`), le parser tente de créer un mapping imbriqué et échoue silencieusement. Conséquence : Obsidian affiche le frontmatter en texte brut au lieu du panneau Properties (sans message d'erreur), Bases / Dataview n'indexent pas les propriétés, et toute sync vers une fiche Notion peut échouer. Le piège est silencieux donc particulièrement dangereux.
- **How to apply** :
  1. Tout item de liste contenant `:` suivi d'un espace → envelopper en quotes (simples `'...'` ou doubles `"..."`).
  2. Single quotes recommandées si le texte contient des doubles quotes internes (pas d'échappement nécessaire).
  3. Double quotes recommandées si le texte contient des apostrophes ASCII `'`.
  4. Si le texte contient les deux : doubler les single quotes intérieures `''` ou échapper les doubles quotes `\"`.
  5. **Validation systématique** avant publication : parser le frontmatter avec `python -c "import yaml; yaml.safe_load(open('doc.md').read().split('---')[1])"` ou équivalent. Si erreur → corriger.
- **Articulation** : [[#R-001]] (Markdown SoT — frontmatter doit être lisible mécaniquement), [[#R-055]] (frontmatter en 3 zones balisées — la structure ne suffit pas, encore faut-il que YAML soit parseable).
- **Exemples** :
  - ❌ `- VÉRIFIER absence de marqueurs (cf. C-027) : "à créer", "TBD"` → parse échoué (le parser voit un mapping `VÉRIFIER absence... : valeur`)
  - ✅ `- 'VÉRIFIER absence de marqueurs (cf. C-027) : à créer, TBD'`
  - ❌ `- Note avec apostrophe typographique : c'est cassé` → ambigu
  - ✅ `- "Note avec apostrophe typographique : c'est OK"`
- **Conséquence si violation** : frontmatter affiché en texte brut dans Obsidian, propriétés non indexées par Bases / Dataview, fiche Notion potentiellement non-syncable, perte de discoverabilité.
- **Origine** : 03-05-2026, lors de la production de TPL_META_CATALOGUE v1.1. Leonard a flaggé le frontmatter affiché en rouge dans Obsidian au lieu du panneau Properties. Cause identifiée : item `cleanup_rules` contenant `: "à créer"` interprété comme mapping imbriqué par le parser YAML.

## 5.4 Templates & instanciation des docs

Règles structurantes sur la production des docs Brain via templates : obligation de template, encapsulation des instructions de génération dans des blocs `@INSTR-*`, et primauté du manuel parent sur le WR-RD pour la génération d'une BDD Notion.

#### R-004 : Template obligatoire pour tout nouveau doc Brain

- **Portée** : Brain
- **Why** : Homogénéité, gouvernance par les Docs méta, agents IA capables d'instancier de manière reproductible. Sans template obligatoire, chaque nouveau doc serait produit ad hoc avec des structures variantes, rendant l'audit transverse et la consommation par agents impossibles.
- **How to apply** : Tout doc Brain est généré à partir d'un template (indexé dans BDD `Templates Brain`). Cycle : Template → instanciation → cleanup → validation → indexation Notion.
- **Articulation** : [[#R-040]] (instructions dans @INSTR-*), [[#R-054]] (codification des templates), [[#R-055]] (frontmatter du doc généré reflète le template_code et template_version).
- **Origine** : Principe architectural originel.

#### R-040 : Toutes les instructions de génération vivent dans des blocs `@INSTR-*`

- **Portée** : Brain (templates d'instanciation)
- **Why** : Un template définit la structure du doc final (sections numérotées `# 1)`, `# 2)`, etc.). Si une instruction de génération apparaît sous forme d'un titre Markdown numéroté (ex. `# 0) GUIDE D'INSTANTIATION`), elle se confond visuellement avec les vraies sections du doc final, crée un parasitage cognitif (la séquence `0,1,2,3...` laisse penser que `0)` est le début légitime de la structure), et augmente le risque que l'agent générateur oublie de la supprimer ou la prenne par mimétisme pour un modèle de section. Par construction, les instructions de génération ne doivent **jamais** ressembler à une section du doc final.
- **How to apply** :
  - Tout contenu qui guide la génération du doc (instructions, doctrine, exemples normatifs, paramétrages, vocabulaire contrôlé, guide d'instanciation, settings…) DOIT vivre **exclusivement** dans un bloc `<!-- @INSTR-START: NOM_BLOC ... @INSTR-END: NOM_BLOC -->`.
  - **Aucun titre Markdown numéroté** (`# 0)`, `## 0.1`, etc.) ne doit servir de wrapper à des instructions de génération.
  - Les blocs `@INSTR-*` sont **flottants** dans le template (placés là où c'est lisible pour l'auteur du template) et tous **systématiquement supprimés** à l'instanciation par la `cleanup_rules` standard `SUPPRIMER tous les commentaires HTML @INSTR-*`.
  - La `cleanup_rules` du template ne doit **jamais** contenir une règle ad hoc du type `SUPPRIMER la section 0) GUIDE D'INSTANTIATION` puisque cette section ne doit pas exister.
  - Les sections numérotées `# 1)`, `# 2)`, etc. sont **réservées à la structure du doc final** et ne contiennent jamais de contenu d'instruction de génération.
  - Une vraie section structurelle d'un doc final peut légitimement être numérotée `# 0)` si elle décrit du contenu metadata du doc (ex. `# 0) Meta de la brick` dans `Template méta de Brick.md` qui contient des sous-sections `0.1 Contexte & mandat`, `0.2 Sources & procédé de production`…). Critère de discrimination : ce contenu apparaît-il dans le doc instancié final (oui = structure, à laisser) ou est-il supprimé à l'instanciation (oui = instruction, à wrapper dans `@INSTR-*`) ?
- **Articulation** : [[#R-004]] (template obligatoire), [[#R-074]] (méthode dédiée pour règles de maintenance — anti-doublon dans les docs générés).
- **Exemples** :
  - ✅ `<!-- @INSTR-START: INSTANTIATION_GUIDE [contenu] @INSTR-END: INSTANTIATION_GUIDE -->` placé entre les autres blocs `@INSTR-*` du template.
  - ❌ `# 0) GUIDE D'INSTANTIATION - [INSTR-SECTION] (SUPPRIMER APRÈS USAGE)` suivi de sous-titres `## 0.1`, `## 0.2`…
  - ❌ `cleanup_rules: - SUPPRIMER la section 0) GUIDE D'INSTANTIATION` (témoigne d'une violation à corriger).
- **Conséquences** :
  - ✅ Structure du doc final sacrée et lisible (numérotation commence à `1`, jamais à `0` pour des instructions).
  - ✅ Une seule règle de cleanup suffit : `SUPPRIMER tous les commentaires HTML @INSTR-*`.
  - ✅ Pas de risque de contamination structurelle ni d'oubli de suppression.
- **Migration effectuée** : 26-04-2026 - 6 templates corrigés. Le 7e cas (`# 0) Meta de la brick` dans `Template méta de Brick.md`) est conservé car c'est une vraie section structurelle du doc final.
- **Origine** : 26-04-2026, Leonard, après revue des templates Manuel de BDD - Digital Twin v6.1.0 et WR-RD - Digital Twin v1.0.0.

#### R-045 : Source de vérité pour la génération d'une BDD = Manuel parent

- **Portée** : Twin (génération initiale ou refonte d'une BDD Notion). Pattern applicable par extension à Brain et Mission Ops.
- **Why** : Le manuel a 12 colonnes (vs 9 dans le WR-RD) - notamment **Portée**, **Nature de production** (Saisie / Calculé / Dérivé) et **Forme logique** détaillée. Ces champs sont indispensables pour générer correctement (ex. distinguer une formule d'une saisie, une relation native d'une jumelle texte, un rollup d'une propriété directe). Le WR-RD est une projection runtime, pas un canon de génération.
- **How to apply** : Toute génération de BDD Notion ou refonte de schéma repose strictement sur la section 4 du manuel parent (4.1 à 4.5). Le WR-RD n'est consulté qu'en runtime par les agents. Si un écart apparaît entre manuel et WR-RD, c'est le manuel qui prime (cohérent avec [[#R-041]] / [[#R-042]]).
- **Articulation** : [[#R-041]] (propagation Manuel→WR-RD), [[#R-042]] (QA stricte égalité Manuel/WR-RD), [[#R-046]] (ordre de création des éléments).
- **Origine** : 26-04-2026, Phase 6.5 - préparation génération des 28 BDD Twin v2 sur Notion.

## 5.5 Indexation Notion & lifecycle des fiches

Règles structurantes sur la sync Markdown SoT → BDDs Notion : descriptions des propriétés, statuts harmonisés, doctrine d'indexation et de mise à jour, identifiants pivots de déduplication, ordering des propriétés, ordre de création des éléments d'une BDD.

#### R-006 : Descriptions Notion ≤280 caractères

- **Portée** : Brain
- **Why** : Lisibilité Notion, cohérence inter-BDD, utilisabilité par les agents. Au-delà de 280 caractères, la description est tronquée à l'affichage et perd sa fonction de mini-prompt actionnable.
- **How to apply** : Les descriptions de propriétés dans Notion commencent par un verbe à l'infinitif, restent en texte brut (pas de Markdown), ne dépassent pas 280 caractères. On les copie directement depuis le manuel de BDD (colonne « Description et règles ≤280 (à coller dans Notion) » côté Brain, ou « Instructions d'écriture » côté Twin/MO).
- **Articulation** : [[#R-029]] (doc Markdown SoT pour indexation), [[#R-033]] (descriptions = mini-prompts), [[#R-072]] (pas d'énumération de taxons dans descriptions ≤280).
- **Origine** : Convention établie dans les templates de manuels de BDD.

#### R-008 : Statuts harmonisés

- **Portée** : Brain
- **Why** : Uniformité de gouvernance à travers les 11 BDD Brain. Sans harmonisation, chaque BDD inventerait ses propres statuts (Actif, En cours, Validé, Final, Brouillon...) et les agents devraient maintenir une table de correspondance.
- **How to apply** : Toutes les BDD Brain utilisent la taxonomie `OBJ.STATUT` avec les valeurs canoniques : `Brouillon`, `Validé`, `À revoir`, `Archivé`. Pas de valeur ad hoc.
- **Articulation** : [[#R-007]] (taxonomies par codes), [[#R-067]] (libellés humains).
- **Origine** : Convention établie.

#### R-026 : Archivage local par dossier thématique

- **Portée** : Transverse (Brain + Twin)
- **Why** : Éviter qu'un "grenier global" à la racine du vault gonfle sans fin et rende l'archivage illisible. Garder l'archive proche de son contexte thématique.
- **How to apply** : Chaque dossier thématique (`Manuels de BDD/Digital Twin/`, `Notes de Concept/`, `Taxonomies/`, `Logic Blocks/`, `00 - Docs méta/`) a son propre sous-dossier `archives/` (ou `99-Archives/` pour les nouveaux dossiers fonctionnels). Le git garde l'historique complet des déplacements - pas besoin de doublons dans le vault.
- **Articulation** : [[#R-053]] (renaming des docs archivés).
- **Exemples** : ✅ `Notes de Concept/archives/Concept - Ressource.md` / ❌ `ARCHIVES/Notes de Concept/...`
- **Origine** : 24-04-2026, conception arborescence cible pour refonte Twin v2 (D-010).

#### R-029 : Le doc Markdown est source de vérité pour l'indexation Notion

- **Portée** : Brain (indexation)
- **Why** : Éviter toute divergence entre le contenu du doc et ses propriétés Notion. Les propriétés sont **dérivées**, pas **inventées**. Application directe de [[#R-001]] au cas spécifique de l'indexation.
- **How to apply** : Avant de créer ou mettre à jour une entrée Notion, l'agent doit **lire l'intégralité du doc Markdown correspondant**. Les propriétés sont dérivées du contenu. Si une propriété ne peut pas être dérivée du doc de façon non-ambiguë, laisser vide et signaler plutôt qu'inventer. Respecter les contraintes de format portées par **la description de chaque propriété Notion** (qui fait office d'instructions d'écriture).
- **Articulation** : [[#R-001]] (Markdown SoT — généralisation), [[#R-033]] (descriptions = mini-prompts), [[#R-037]] (lecture complète obligatoire), [[#R-069]] (lecture complète avant indexation).
- **Exemples** :
  - ✅ `Définition` remplie avec 3-10 lignes extraites/synthétisées du doc (car la description Notion impose 3-10 lignes)
  - ❌ `Définition` générée de toutes pièces par l'agent
- **Origine** : 24-04-2026, Leonard, avant indexation Twin v2.

#### R-030 : Double indexation d'une note de concept

- **Portée** : Brain (indexation)
- **Why** : Le `Glossaire LBP` est un hub sémantique qui n'a pas de lien source direct. Le lien vers le doc vit côté `Registre des notes de concept`. Le Glossaire porte la sémantique, le Registre porte la traçabilité.
- **How to apply** : Indexer une note de concept = créer **2 entrées Notion liées** :
  1. Une entrée dans `Registre des notes de concept` avec `Lien note concept (source) = URL Drive`
  2. Une entrée dans `Glossaire LBP` avec les propriétés sémantiques (Type concept, Domaine, Définition, Règles d'usage, etc.)
  3. Lier l'entrée Glossaire → Registre via la relation `est documenté par (notes de concept)`
  4. Si applicable, lier également Glossaire → Méthodes (`est mis en oeuvre par`) et/ou Glossaire → Manuels de BDD (`est modélisé par`)
- **Articulation** : [[#R-031]] (alignment code note↔glossaire), [[#R-054]] (paire `CPT_*` ↔ `GLO_*`).
- **Origine** : 24-04-2026, Leonard, avant indexation Twin v2.

#### R-031 : Alignement du code unique entre note de concept et glossaire

- **Portée** : Brain (indexation)
- **Why** : Traçabilité stable et navigation cohérente. Un même concept doit avoir le **même code** dans les deux BDD.
- **How to apply** : Le `Code unique` d'une entrée dans `Registre des notes de concept` (préfixe `CPT_`) et l'entrée correspondante dans `Glossaire LBP` (préfixe `GLO_`) doivent partager strictement le même `<DOMAIN>_<TOKEN>`. Ce code provient du doc Markdown source.
- **Articulation** : [[#R-030]] (double indexation), [[#R-054]] (paire `CPT_*` ↔ `GLO_*`).
- **Origine** : 24-04-2026.

#### R-032 : Mise à jour plutôt que création pour une entrée existante

- **Portée** : Brain (indexation)
- **Why** : Éviter les doublons Notion. Les entrées existantes portent peut-être des relations, des rollups, des références qu'on casserait en recréant.
- **How to apply** : Avant de créer une entrée Notion, vérifier qu'elle n'existe pas déjà (par `Code unique` d'abord, puis par `Nom canonique`). Si elle existe :
  - **Mettre à jour** toutes les propriétés en lisant le nouveau doc (cf. [[#R-029]])
  - **Mettre à jour le lien source** si le chemin Drive a changé
  - **Ne pas changer le `Code unique`** (stable par [[#R-005]])
  - Si le doc v2 porte un **nom ou code différent** de la v1, alors **archiver l'entrée v1** (Statut = Archivé) et **créer une nouvelle entrée v2** ([[#R-036]])
- **Articulation** : [[#R-005]] (code unique stable), [[#R-036]] (Code unique = identité), [[#R-038]] (identifiant pivot par type).
- **Origine** : 24-04-2026.

#### R-033 : Les descriptions de propriétés Notion sont des mini-prompts de remplissage

- **Portée** : Brain (indexation)
- **Why** : Pour les BDD du Brain, les **instructions d'écriture** sont portées par les **descriptions de chaque propriété Notion**. Ignorer ces descriptions produit des contenus hors format.
- **How to apply** : Avant de remplir une propriété, **lire sa description Notion** (via `notion-fetch` sur la data source). Respecter scrupuleusement les contraintes :
  - Format imposé (ex: "3 à 10 lignes", "séparateur ';'", "MAJUSCULES")
  - Structure imposée (ex: "Bon usage: ... ; Mauvais usage: ...")
  - Valeurs strictes pour les select/multi-select (ex: "valeurs strictes: Core; Motor")
  - Interdictions (ex: "ne pas inclure de contenu client")
- **Articulation** : [[#R-006]] (≤280 caractères), [[#R-029]] (Markdown SoT), [[CLAUDE.md#C-017]] (lecture WR-RD obligatoire avant remplissage).
- **Exemples** :
  - ✅ Pour `Code unique` d'une taxo, la description impose format `NAMESPACE.TAXO` MAJUSCULES → valeur dérivée du nom de fichier `.md`
  - ❌ Inventer un code libre
- **Origine** : 24-04-2026.

#### R-034 : Ordonnancement création puis relation (2 passes)

- **Portée** : Brain (indexation)
- **Why** : Notion exige que les 2 entrées cibles d'une relation existent avant de pouvoir les lier. Lors d'une indexation par batch, créer d'abord toutes les entrées, puis créer les relations dans une seconde passe.
- **How to apply** :
  1. **Passe 1 - Créations** : créer toutes les entrées Notion sans établir leurs relations (ou seulement les relations vers des entrées déjà existantes)
  2. **Passe 2 - Relations** : établir les relations entre entrées créées dans la passe 1
  3. En pratique : regrouper les docs par "type sans dépendance" en premier (ex: taxonomies), puis types dépendants (ex: manuels qui référencent taxonomies), puis types couvrant le graphe (ex: glossaire qui pointe vers manuels)
- **Articulation** : [[#R-035]] (généralisation inter-types), [[#R-046]] (ordre création BDD Notion).
- **Exemples** : ✅ Créer Manuel Actifs + Taxo ASSET.SUBTYPE → puis relier Manuel → Taxo / ❌ Tenter de créer le Manuel avec relation vers Taxo qui n'existe pas encore.
- **Origine** : 24-04-2026, lors du dry-run mini-batch 0.

#### R-035 : Ordre d'indexation inter-types (graphe de dépendances)

- **Portée** : Brain (indexation)
- **Why** : Chaque type d'artefact Brain a des relations vers d'autres types. Pour éviter de créer une dette de relations (à rattraper dans des passes ultérieures), on indexe par ordre de dépendance : feuilles d'abord, types qui les consomment ensuite.
- **How to apply** : Respecter cet ordre pour une indexation Brain complète :
  1. **Taxonomies** (type feuille - aucune dépendance vers d'autres types Brain)
  2. **Manuels de BDD** (consomment les Taxonomies via `utilise (taxonomies)`)
  3. **Notes de concept + Glossaire** (Glossaire peut référencer Manuels via `est modélisé par`, Méthodes via `est mis en oeuvre par`)
  4. **Méthodes, Agents, Prompts, Logic blocks, Outils externes, Templates de bricks** (consomment Glossaire, Manuels, Docs méta)
- **Généralise [[#R-034]]** : R-034 dit "créer puis relier" au sein d'un batch. R-035 étend à l'échelle inter-types.
- **Articulation** : [[#R-034]] (2 passes intra-batch).
- **Exemples** : ✅ Indexer ASSET.SUBTYPE → puis Manuel Actifs peut référencer ASSET.SUBTYPE dans sa création / ❌ Indexer Manuel Actifs d'abord avec relation vide vers ASSET.SUBTYPE, puis revenir plus tard (dette).
- **Origine** : 24-04-2026, mini-batch 0 a créé une dette (Manuel Actifs sans ses 7 autres taxos non encore créées). Règle posée pour ne pas reproduire.

#### R-036 : Le Code unique est l'identité ; MAJ en place tant que le code est stable

- **Portée** : Brain (indexation)
- **Why** : Le `Code unique` est l'identité stable de l'objet ; le `Nom canonique` n'est qu'un libellé éditable. Tant que le code est inchangé, l'entité est la même - seul son libellé / sa description / son URL évoluent. Préserver l'entrée existante préserve aussi ses relations Notion entrantes (rollups, références d'autres BDD), ses ID Notion stables, et évite de polluer le Registre avec des doublons archivés.
- **How to apply** :
  - **Code identique** (même si le nom canonique change, peu importe l'amplitude du changement) → **mise à jour en place** de l'entrée existante (Nom, Description, URL Drive, Aliases, etc.). Pas d'archivage.
  - **Code différent** (renommage de namespace, changement de TOKEN, scission/fusion d'objet) → archive de l'entrée v1 + création d'une nouvelle entrée v2.
- **Articulation** : [[#R-005]] (code unique stable), [[#R-032]] (MAJ vs création), [[#R-038]] (identifiant pivot par type d'objet).
- **Exemples** :
  - ✅ ORG.CONTEXTE : v1 "Contexte d'ancrage de rôle" → v2 "Contexte d'ancrage organisationnel d'un poste" (code stable) → **MAJ** de v1
  - ✅ ORG.DEP_LEVEL → COL.DEP_LEVEL (code change suite à scission UO→Orga+Collectif) → archive v1 + création v2
- **Conséquence** : Registre propre, IDs Notion stables, relations préservées. La trace des évolutions de libellés vit dans l'historique Notion (créé/last edited) et le journal git.
- **Origine** : 25-04-2026, Leonard, après examen des batchs A1+A2 (correctifs sur 25 doublons inutiles).

#### R-037 : Lecture complète du doc obligatoire avant indexation (pas de raccourci frontmatter)

- **Portée** : Brain (indexation) - **tous types de docs**
- **Why** : Le frontmatter YAML résume les métadonnées structurelles (title, code, scale_kind, aliases). Les propriétés Notion narratives (Description source, Description courte, Définition, Règles d'usage, Valeur ajoutée...) exigent le contenu approfondi qui vit dans les **sections du corps du doc** (intention + règles d'usage + exclusions + "quoi choisir / quand" + distinctions + patrons d'arbitrage + exemples). Se limiter au frontmatter produit des descriptions pauvres et non-actionnables.
- **How to apply** : Pour indexer **tout doc Brain** (taxonomie, note de concept, manuel de BDD, méthode, prompt, etc.), **lire l'intégralité du doc** avant de remplir les propriétés narratives. Le frontmatter sert uniquement à extraire les champs structurés (title, code, type). Tout le reste doit venir de la lecture du corps :
  - **Taxonomie** : sections 1 (objet/but), 2 (détection du domaine), 5 (heuristique), 8 (exemples) → Description source + Description courte
  - **Note de concept** : sections 1 (résumé, définition, périmètre), 2 (rôle, valeur), 3 (caractéristiques, modules), 4 (relations), 7 (bonnes pratiques) → Définition + Règles d'usage + Valeur ajoutée + Usages IA
  - **Manuel de BDD** : sections 1 (identité), 2 (périmètre/frontières), 3 (rôle systémique), 4 (modèle de données) → Description + Valeur ajoutée + Usages IA
  - **Glossaire** (dérivé de note de concept via [[#R-030]]) : lire la note de concept ET le doc auquel elle fait référence pour synthétiser
- **Articulation** : [[#R-029]] (doc Markdown SoT), [[#R-069]] (lecture complète avant indexation - extension Twin/MO).
- **Exemples** : ✅ Lire `ORG.CONTEXTE.md` en entier pour en tirer une Description source qui mentionne "qualifie le contexte organisationnel d'un poste par niveau de périmètre ; règles : choisir 1 seule valeur, ne pas typer un collectif ou une organisation avec cette taxo" / ❌ Se contenter du `summary:` du frontmatter qui dit juste "Qualifie le contexte d'ancrage d'un poste".
- **Origine** : 24-04-2026, Leonard, après batch A1 où raccourci frontmatter-only a produit des descriptions jugées pauvres.

#### R-038 : Identifiant pivot par type d'objet (taxonomies = code, autres = nom)

- **Portée** : Brain (indexation, déduplication)
- **Why** : [[#R-036]] (test de doublon par code unique) ne s'applique strictement qu'aux taxonomies. Pour les autres BDD Brain, le code n'est pas (encore) un identifiant fiable : il peut changer au cours d'updates, n'est pas systématiquement renseigné, ou n'est pas conçu comme pivot de déduplication. C'est le **Nom canonique** qui sert d'identifiant pivot pour ces objets. Confondre les deux logiques amène à créer des doublons (pour les taxos quand on dédoublonne par nom) ou à manquer des doublons (pour les manuels quand on dédoublonne par code).
- **How to apply** :
  - **Taxonomies** → identifiant pivot = `Code unique` (format `NAMESPACE.TAXO`, immuable). Application stricte de [[#R-036]].
  - **Manuels de BDD, Notes de concept, Glossaire, autres BDD Brain** → identifiant pivot = `Nom canonique` (avec normalisation : trim, casse insensible, accents normalisés pour la comparaison). Le code éventuellement présent est informatif, pas pivot.
  - Lors d'une indexation Notion : avant toute création, requêter le registre cible avec le bon champ pivot. Si match → MAJ en place ; sinon → création.
- **Articulation** : [[#R-032]] (MAJ vs création), [[#R-036]] (Code unique = identité).
- **Exemples** :
  - ✅ Taxo ORG.CONTEXTE : doublon détecté par code → MAJ v1
  - ✅ Manuel "Actifs" (anciennement "Ressources") : doublon détecté par nom (après normalisation)
  - ❌ Tester un doublon de manuel uniquement par code : risque de rater une refonte de nom + code, ou de créer un faux doublon si le code a évolué
- **Origine** : 25-04-2026, Leonard, après correction des 25 doublons A1+A2.

#### R-046 : Ordre de création des éléments d'une BDD sur Notion

- **Portée** : Twin (toute création de BDD ou ajout massif de propriétés relationnelles/calculées). Pattern applicable par extension à Brain et Mission Ops.
- **Why** : Les contraintes Notion impliquent des dépendances strictes :
  - une **relation bidirectionnelle** ne peut exister que si les deux BDD cibles existent
  - un **rollup** ne peut exister que si la relation source qu'il agrège existe
  - une **propriété multi-select avec taxonomie** doit avoir ses options peuplées au moment de la création (sinon Notion les crée à la volée à partir du contenu)
- **How to apply** : Suivre l'ordre suivant pour générer un ensemble cohérent de BDD :
  1. **Créer toutes les BDD vides** (pleine page sous la page hôte) - uniquement le titre
  2. **Ajouter les propriétés natives non-relationnelles** (texte, sélection, multi-sélection avec valeurs taxonomiques peuplées, date, number) dans l'ordre d'ordering [[#R-047]]
  3. **Créer les relations bidirectionnelles** (les 2 BDD existent désormais) ; cas particulier : `Sources d'informations` est le seul lien **monodirectionnel** (le Twin référence Sources sans miroir côté Sources)
  4. **Créer les rollups** (les relations sources existent désormais)
  5. **Réordonner les propriétés** selon [[#R-051]] (`update_view SHOW`) si l'ordre s'est dégradé après ajouts post-création
- **Exception monodirectionnalité** : la relation `Source(s) d'information` côté Twin est mono - pas de propriété miroir côté `Sources d'informations`.
- **Articulation** : [[#R-034]] (2 passes), [[#R-047]] (ordering Twin), [[#R-051]] (`update_view SHOW`).
- **Origine** : 26-04-2026, Leonard, Phase 6.5.

#### R-047 : Convention d'ordering des propriétés Notion (Twin)

- **Portée** : Twin (toute BDD du Digital Twin)
- **Why** : Lisibilité des fiches dans Notion. Les propriétés métier importantes doivent rester en haut ; les propriétés de gouvernance / journal / traçabilité, peu consultées au quotidien, sont reléguées en bas. Cohérence visuelle entre les 28 BDD Twin.
- **How to apply** : **Sept blocs séquentiels** (ordre R-047 v2.2) :
  1. **Bloc 1 - Tête générique** (5 props, ordre fixe) : `Nom` · `Statut de l'objet` · `Aliases` · `Erreurs de transcription` (conditionnelle, présente uniquement si dans le manuel) · `Description`.
  2. **Bloc 2 - Corpus métier**, avec **ordre interne strict** :
     - **2a. Propriétés spécifiques** (4.2)
     - **2b. Couche 5D** regroupée intégralement (4.4 - natives + jumelles 5D si existent)
     - **2c. Jumelles textes seules** (4.3 jumelles uniquement, **sans les relations**)
     - **2d. Calculés natifs** (4.5 hors rollups relationnels) - formules locales.
  3. **Bloc 3 - Queue générique** (~11-12 props, ordre fixe) : `Lien vers la note avancée` (URL, conditionnelle, [[#R-050]]) · `Exemples concrets` · `Commentaires libres` · `Notes du consultant` · `Confidentialité (option)` (conditionnelle) · `Indices observés` · `Indices d'existence de l'objet` · `Created Date` · `Last Updated Date` · `Logs / Révisions LBP` · `Merge Notes` · `Merge Flags`
  4. **Bloc 4 - Sources textuelles** (1 prop) : `Source(s) d'information (texte)` (RICH_TEXT). La relation monodirectionnelle `Source(s) d'information` est différée.
  5. **Bloc 5 - Relations sortantes** (Passe 2 globale, après que les 28 BDD ont leur Passe 1 finie) : toutes les relations bidirectionnelles documentées en 4.3.
  6. **Bloc 6 - Rollups & couche calculée relationnelle** (Passe 3 globale, après les relations) : tous les rollups documentés en 4.3 et 4.5.
  7. **Bloc 7 - Miroirs reçus** (créés automatiquement par Notion lors de la Passe 2 des **autres** BDD).
- **Renommage des natives Notion** : `Created Date` et `Last Updated Date` réutilisent les propriétés natives Notion `Created time` / `Last edited time` mais sont **renommées** pour rester cohérent avec la nomenclature des manuels.
- **Justification doctrinale** : relations et rollups forment la **couche calculée et le graphe dérivé** (lecture analytique secondaire), pas une saisie directe par humain. Les voir en bout de schéma signale visuellement leur nature dérivée.
- **Articulation** : [[#R-046]] (ordre création), [[#R-051]] (`update_view SHOW` final).
- **Origine** : 26-04-2026, Leonard, Phase 6.5. **R-047 v2.2 (27-04-2026)** : découplage jumelles+relations (jumelles seules en Bloc 2c Passe 1, relations en Bloc 5 Passe 2 globale), ajout Bloc 6 rollups + Bloc 7 miroirs reçus.

#### R-048 : Naming d'une BDD Notion = nom canonique simple

- **Portée** : Twin
- **Why** : La BDD Notion représente l'objet métier (ex. `Actifs`), pas le doc qui le décrit (`Manuel de BDD - Actifs.md`). Confondre les deux dans le titre Notion crée une confusion durable et casse la cohérence avec les manuels qui pointent vers la BDD via `Nom de la BDD Notion`.
- **How to apply** : Le titre d'une BDD Notion = **nom canonique simple** au pluriel et avec accents (ex. `Actifs`, `Collectifs`, `Pratiques organisationnelles`, `Événements`, `Problématiques sandbox`). Aucun préfixe `Manuel de BDD - `, aucun suffixe descriptif. Le nom canonique du manuel et le titre de la BDD doivent matcher 1:1.
- **Articulation** : [[#R-027]] (conventions naming filename), [[#R-062]] (naming univoque docs méta).
- **Exemples** : ✅ `Actifs` / ❌ `Manuel de BDD - Actifs` / ❌ `BDD Actifs Twin v2`
- **Origine** : 26-04-2026, Leonard, Phase 6.5.

#### R-051 : Ordering des propriétés Notion via `update_view SHOW` (et non via l'ordre des `ADD COLUMN`)

- **Portée** : Twin (toute génération ou modification d'une BDD Notion)
- **Why** : L'ordre des `ADD COLUMN` dans une salve DDL **ne détermine pas** l'ordre d'affichage côté UI Notion. Notion affiche les colonnes selon le tableau `displayProperties` de chaque vue, qui par défaut suit un ordre alphabétique automatique sur les vues nouvellement modifiées (notamment après DROP+ADD). Vouloir préserver l'ordre [[#R-047]] via l'ordre des ADD COLUMN est donc **vain et coûteux** (chronophage, fragile aux miroirs créés par les relations bidir, exige des passes successives lourdes). La bonne approche : **séparer création des propriétés (ordre indifférent) et ordering UI (1 appel `update_view` final par BDD)**.
- **How to apply** :
  1. Pour la création/ajout de propriétés sur une BDD Notion : utiliser `update_data_source` avec une salve DDL **dans n'importe quel ordre** (peu importe).
  2. Pour configurer l'ordre d'affichage final : appeler `update_view` sur la vue concernée avec la directive `SHOW "prop1", "prop2", ...` listant **toutes** les propriétés visibles dans l'ordre voulu ([[#R-047]] pour les BDD Twin).
  3. Effectuer cet appel `SHOW` **une seule fois par BDD à la toute fin** du workflow, pour éviter de devoir le rappeler à chaque passe intermédiaire.
- **Conséquence sur le workflow** : [[#R-047]] décrit l'ordre **cible final** ; R-051 garantit que l'ordering UI final est conforme **indépendamment** de l'ordre de création.
- **Effets de bord** : si une nouvelle propriété est créée après le `SHOW` final (ex. ajout d'une relation oubliée), elle apparaît en queue de la vue. Il faut alors relancer `update_view SHOW` pour la repositionner.
- **Articulation** : [[#R-046]] (ordre création), [[#R-047]] (ordering Twin).
- **Origine** : 27-04-2026, Leonard, après pilote Actifs - l'IA Notion a démontré qu'elle pouvait réordonner via `displayProperties`, et l'outil MCP `notion-update-view` expose la même capacité via la directive `SHOW`.

## 5.6 Gouvernance des taxonomies & WR-RD

Règles structurantes sur la gestion des taxonomies (séparation libellés humains / codes immuables) et la propagation Manuel de BDD → WR-RD (artefact runtime dérivé strict pour les agents).

#### R-007 : Taxonomies par codes

- **Portée** : Brain
- **Why** : Séparer le stockage lisible (libellés) du référencement stable (codes). Sans cette séparation, tout renommage de libellé casse les références.
- **How to apply** : Les BDD stockent des libellés humains. Les codes taxonomiques (ex: `OBJ.STATUT`) apparaissent uniquement dans les descriptions ≤280 et dans la documentation. Pas de codes dans le corps des textes.
- **Articulation** : [[#R-008]] (statuts harmonisés OBJ.STATUT), [[#R-054]] (codification universelle), [[#R-067]] (libellés humains pour les valeurs select Notion).
- **Origine** : Convention établie dans les templates.

#### R-058 : Aucune jumelle texte sur les BDDs Brain

- **Portée** : Les 11 BDDs Brain (Core + Motor : Glossaire LBP, Notes de concept, Taxonomies, Manuels de BDD, Docs méta LBP, Méthodes LBP, Prompts LBP, Templates de bricks, Agents LBP, Outils externes, Registre des logic blocks). **Hors scope** : BDDs Digital Twin (les jumelles texte y sont **autorisées et utiles**) ; BDDs Mission Ops (usage **expérimental** à valider, non interdit pour l'instant).
- **Why** : Une "jumelle texte" est une propriété texte qui duplique manuellement le contenu d'une relation native (ex : sur la BDD Logic blocks, la relation `est utilisé dans (Prompts LBP)` côté Notion + un champ texte `est utilisé dans (Prompts LBP) [texte]` qui répète à la main les noms des prompts liés). Côté Twin, ces jumelles servent à **capter des indices** dans des champs textes pour aider à la connexion logique d'objets quand la relation native échoue ou n'est pas encore créée. **Côté Brain**, ce besoin n'existe pas : les objets Brain sont créés et gérés de manière déterministe par les agents/consultants à partir de leurs manuels respectifs ; il n'y a pas d'indices textuels à interpréter. Une jumelle texte sur une BDD Brain est donc **toujours redondante avec une relation native** et introduit : (a) une dette de double saisie, (b) un risque silencieux de désynchronisation entre la relation native et son écho texte, (c) une charge cognitive sans contrepartie pour les agents en retrieval.
- **How to apply** :
  - Aucune propriété de type `text` ou `rich_text` portant un nom dérivé d'une relation existante (ex : `<rel> [texte]`, `<rel> (texte)`) sur une BDD Brain.
  - Si une jumelle texte est détectée sur une BDD Brain (audit ou découverte ad hoc), action : **DROP** côté Notion + retrait éventuel du manuel s'il en faisait mention.
  - À l'inverse, **ne pas chercher à créer** des jumelles texte sur les BDDs Brain dans une logique de "filet de sécurité" - l'isolation Brain ↔ Twin/MO (D-019) garantit que les relations Brain sont peu nombreuses et bien maîtrisées, donc le risque de relation cassée est faible.
- **Cas particulier Mission Ops** : usage expérimental autorisé pour tester si elles produisent des infos complémentaires utiles. À ré-évaluer après une mission complète.
- **Articulation** : [[#R-013]] (sobriété relationnelle), [[#R-015]] (jumelles textes côté Twin systématiques — distinction stricte des doctrines Brain vs Twin).
- **Conséquence si violation** :
  - Doublonnage du modèle, sources de vérité multiples pour la même info.
  - Désynchronisation silencieuse (relation modifiée mais pas le texte, ou inverse).
  - Pollution des audits Manuel ↔ Notion (champ Notion non documenté = faux positif).
- **Origine** : 28-04-2026, Leonard, lors de l'audit transverse Notion ↔ Manuels Brain. Détection sur la BDD Registre des logic blocks de 2 jumelles texte en conflit avec la règle 3.1 du manuel Logic blocks. Décision Leonard : interdire la pratique sur Brain, conserver Twin (où elle est utile), tester Mission Ops.

## 5.7 Hygiène d'écriture des docs

Règles structurantes sur la qualité éditoriale des docs LBP : discipline des backticks, anti-bruit historique et anti-spéculation future, hygiène des champs `summary`/`purpose`, libellés humains pour les select Notion, anti-redondance des aliases, lecture complète avant indexation, ban des noms d'agents, auto-suffisance des descriptions, anti-énumération de taxons.

#### R-057 : Discipline d'usage des backticks Markdown

- **Portée** : Transverse à tous les docs Markdown LBP (manuels de BDD, WR-RD, taxonomies, notes de concept, templates, méthodes, prompts, logic blocks, chartes, playbooks, docs méta).
- **Why** : Les backticks `` ` `` ont une fonction Markdown précise : signaler un **token technique littéral** (rendu en `monospace`). Mais ils ont été utilisés sans discipline dans plusieurs docs - parfois autour de mots du langage courant pour de la mise en évidence générale, parfois aléatoirement. Conséquences : (a) bruit visuel, (b) confusion entre identifiant technique et prose, (c) perte de la valeur sémantique de la convention.
- **How to apply** : les backticks sont **réservés** aux usages suivants (liste fermée) :
  - Nom d'une propriété, d'une variable, d'un champ : `created_at`, `brick_type`, `purpose`
  - Valeur de taxo / code de doc : `BRICK.PROFIL_ORGA`, `BRK_PROFIL_ORGA_001`, `DOC.TYPE`
  - Fragment de syntaxe / commande / regex : `<!-- @INSTR-START -->`, `grep -E "@INSTR"`, `[A-Z]+_[A-Z]+`
  - Nom de fichier / chemin : `Template - Méthode LBP.md`, `refs/RULES_LBP.md`
  - Nom de bloc / section technique : `TEMPLATE_USAGE_GUIDE`, `SECTION_X_GUIDE`
- **Interdits** : mise en évidence générale dans la prose (utiliser `**gras**` pour insister, `*italique*` pour nuancer ou citer un terme), encadrer un mot du langage courant, encadrer une phrase entière.
- **Cas particulier** : à l'intérieur d'un commentaire HTML `<!-- ... -->`, ne **jamais** écrire la séquence `-->` littérale (même entourée de backticks), car le parseur HTML ferme le commentaire avant que Markdown n'agisse. Solution : sortir l'exemple à citer hors du commentaire HTML.
- **Articulation** : [[#R-040]] (blocs `@INSTR-*`).
- **Conséquence si violation** : bruit visuel, confusion lecture, et dans le cas du `-->` dans un commentaire : commentaire HTML cassé en plein milieu, instructions exposées en zone visible.
- **Origine** : 28-04-2026, Leonard, en repérant que le `` `<!-- @INSTR-START ... @INSTR-END -->` `` cité dans la procédure de purge finale d'un template cassait le périmètre du commentaire HTML englobant.

#### R-059 : Hygiène d'écriture des docs Brain - pas de bruit historique ni de spéculation future

- **Portée** : Tous les docs de l'écosystème Brain LBP (Core + Motor) : manuels de BDD, WR-RD, notes de concept, taxonomies, templates, méthodes LBP, prompts, logic blocks, fiches agents, fiches outils externes, glossaires LBP. **Hors scope** : docs de session (`refs/`, `CLAUDE.md`, `DECISIONS_LBP.md`, backlog) qui ont vocation à porter justement l'historique et les hypothèses ; docs Mission Ops (où le journal de mission peut faire partie du livrable) ; docs Digital Twin (où certaines mentions de timeline mission sont structurellement utiles).
- **Why** : Chaque doc Brain est consommé par des **agents en retrieval** qui n'ont pas connaissance du contexte historique de l'écosystème. Pour qu'un agent puisse lire un manuel, une note de concept ou un template et **agir correctement à partir de ce seul doc**, il faut que le doc soit **autonome** : une source de vérité brute à l'instant t. Toute mention historique ("précédemment ce champ s'appelait X", "en V2 on faisait Y") ou spéculative ("à terme on pourrait", "piste à creuser", "amélioration future") crée du **bruit** : (a) charge cognitive inutile, (b) ambiguïté sur ce qui est canon vs ce qui est obsolète/futur, (c) risque que l'agent se base sur une version périmée ou non validée.
- **How to apply** : dans tout doc Brain, **interdiction** d'écrire :
  - **Mentions historiques** : "anciennement", "avant la V3", "ce champ s'appelait X", "on a supprimé Y", "migration depuis Z"
  - **Spéculations futures** : "à terme", "à voir plus tard", "piste à creuser", "amélioration potentielle", "TODO pour le futur", "à étudier"
  - **États transitoires** : "en cours de finalisation", "version provisoire", "draft à valider" (le statut vit dans le frontmatter ou la BDD, pas dans le corps)
- **Où vit l'historique** : commits Git (changelog), `[[Décisions architecturales - LBP]]` (pourquoi tel choix structurant), backlog (`refs/RULES_BRAIN_TWIN-backlog.md` pour les règles pressenties).
- **Où vivent les pistes futures** : `refs/RULES_BRAIN_TWIN-backlog.md`, TodoWrite de session, ou notes personnelles. Pas dans les docs Brain publiés.
- **Cas accepté** : un doc peut citer **explicitement** une règle (ex : R-058) ou une décision (ex : D-019) **comme référentiel canonique courant** - ce n'est pas une mention historique, c'est une déclaration de conformité.
- **Articulation** : [[CLAUDE.md#C-027]] (pas d'infos temporaires dans SoT — extension session de R-059), [[#R-060]] (hygiène summary/purpose).
- **Conséquence si violation** :
  - Agents en retrieval qui hésitent entre deux versions, choisissent mal, ou propagent l'incertitude.
  - Difficulté pour un humain de relire le doc et savoir "ce qui est vrai aujourd'hui".
  - Pollution sémantique : le doc devient un mélange de documentation et de log de chantier.
- **Origine** : 28-04-2026, Leonard, après détection que mes propositions de mises à jour de manuels Brain incluaient des "notes de version" expliquant ce qui changeait par rapport à la version précédente - exactement le bruit historique que cette règle interdit.

#### R-060 : Hygiène d'écriture des champs `summary` et `purpose` du frontmatter Brain

- **Portée** : Tous les docs Brain (manuels de BDD, taxonomies, notes de concept, méthodes, prompts, agents, outils externes, templates de bricks, docs méta, WR-RD, logic blocks, glossaire). Concerne les deux champs `summary` et `purpose` du frontmatter [[#R-055]].
- **Why** : Les champs `summary` et `purpose` sont consommés à la fois par les **agents en retrieval** (qui décident s'ils doivent ouvrir le doc complet) et par les **humains** qui parcourent les BDDs. Trois pièges détruisent leur valeur : (1) **doublon** entre les deux champs (rotation grammaticale stérile), (2) **couplages fragiles** (énumération des valeurs, citation d'objets voisins par leur code ou leur libellé, duplication de qualificatifs déjà portés par d'autres champs du frontmatter), (3) **exploitations métier en aval arbitraires** dans `purpose` qui figent un consommateur parmi N. Une discipline stricte sur ces 3 axes assure densité, robustesse aux évolutions, et lisibilité indépendante.
- **How to apply** :

##### Distinction conceptuelle `summary` vs `purpose`

| Champ | Répond à | Contenu attendu | Forme |
|---|---|---|---|
| `summary` | « **Qu'est-ce que c'est ?** » (description pédagogique, dans l'absolu) | Nature de l'objet (Référentiel / Échelle / Lexique / Cadre...) + axe ou dimension qu'il découpe. **Auto-suffisant** : aucune référence à un objet voisin. | Phrase nominale, lisible isolément. |
| `purpose` | « **À quoi ça sert ?** » (raison d'être structurelle dans l'écosystème LBP) | Action principale qu'on accomplit avec l'objet + **effet structurel direct** sur les objets ainsi qualifiés. **Pas d'exploitation métier en aval**. | **Verbe à l'infinitif en tête**, pattern « *Verbe + objet, pour + effet structurel direct (+ lest descriptif neutre éventuel)* ». |

##### Doctrine d'autonomie (zéro citation d'objet voisin)

Ni `summary` ni `purpose` ne citent jamais d'autres objets de l'écosystème - **ni par leur code, ni par leur libellé conceptuel, ni par référence indirecte** (« distinct de X », « complète Y », « à ne pas confondre avec Z »). Les distinguos cross-objets ont leur place dédiée en **section 6 du fichier** (« Cohérence & impacts croisés »), point d'autorité unique. `summary` et `purpose` décrivent l'objet **dans l'absolu**, comme une définition pédagogique autonome.

##### Doctrine de non-redondance (DRY)

| Type de redondance interdite | Exemple à proscrire | Pourquoi |
|---|---|---|
| Doublon `summary` ↔ `purpose` | summary: « Qualifie X selon Y... » + purpose: « Qualifier X selon Y... » | Rotation grammaticale stérile |
| Énumération des valeurs/taxons | « ...direction, management, expert, opérationnel, support... » | La section 3 du fichier est le point d'autorité unique. Couplage : un changement de taxon imposerait de toucher 3 endroits. |
| Citation d'un objet voisin (code OU libellé) | « ...JOB.FAMILLE », « ...la famille métier », « ...complète la séniorité » | Couplage avec un objet susceptible d'évoluer (renommage, refonte, suppression). Les distinguos vivent en section 6. |
| Nom de BDD ou de propriété d'instanciation | « ...via le champ `Famille (Doc méta)` de la BDD Notion » | Couplage avec le backend (Notion = transitoire). Le doc reste **agnostique du backend**. |
| Qualificatifs déjà portés par un champ structuré | « Référentiel **fermé nominal mono-sélection** des... » | `is_open`, `scale_kind`, `selection_mode`, `cardinality` portent déjà ces infos. Garder seulement la **nature de l'objet** dans le summary. |

##### Doctrine d'effet structurel direct (purpose)

Le `purpose` décrit **l'effet immédiat** que produit la taxo sur les objets qu'elle qualifie - **pas les exploitations en aval** qui consomment cet effet. Cas d'usage métier interdits : priorisation, diagnostic, transformation, recommandation, audit, allocation, pilotage.

✅ Effets structurels directs autorisés (intrinsèques à l'objet) : *cartographier, rendre comparable, qualifier de façon homogène, ancrer dans le temps, tracer, hiérarchiser, positionner, distinguer, normaliser, classer, catégoriser*.

✅ Lest descriptif neutre autorisé : qualificatifs de l'effet (*stable, lisible, partagé, homogène, transverse, fiable*), ancrage descriptif neutre (*indépendamment des intitulés locaux, entre objets de natures différentes, dans le temps, à un instant donné*).

##### Forme des deux champs

- **≤400 caractères** chacun (plafond unifié).
- **Lisible isolément** : `summary` comme `purpose` doivent rester compréhensibles s'ils sont extraits seuls (sans le reste du frontmatter, sans le corps du fichier).
- **Lisible par humain ET par agent** - formulation neutre sur le consommateur. Ne jamais se référer explicitement à « l'agent », « le consultant », « les utilisateurs » dans ces champs.
- **Pas de jargon d'implémentation** : ni « Notion », « rollup », « update_data_source », ni nom de propriété backend.
- **Apostrophes typographiques** `’` ([[#R-052]]).

- **Articulation** : [[#R-052]] (apostrophes), [[#R-055]] (frontmatter), [[#R-070]] (ban noms agents — extension), [[#R-071]] (auto-suffisance — généralisation).
- **Anti-patterns à proscrire (synthèse)** :
  - ❌ « Aider un agent à classer X » → ✅ « Classer X »
  - ❌ summary : « Qualifie X selon Y » + purpose : « Qualifier X selon Y » → ✅ summary nominal, purpose action + effet structurel
  - ❌ Énumération des valeurs en prose → ✅ la section 3 du fichier est le point d'autorité
  - ❌ Citation d'objet voisin → ✅ section 6 « Cohérence & impacts croisés »
  - ❌ Public cible explicite (« pour les consultants ») → ✅ neutre
- **Origine** : 28-04-2026, Leonard, après audit factuel des champs summary / purpose à travers les frontmatter Brain.

#### R-067 : Libellés humains pour les valeurs de select / multi-select Notion (le code immuable reste séparé)

- **Portée** : Transverse — toutes les taxonomies LBP consommées par des propriétés select / multi-select dans les BDDs Notion (Brain, Twin, Mission Ops).
- **Why** : Le code immuable d'un taxon (ex. `TPL.SCOPE.NOTE_CONCEPT`) est nécessaire pour les audits, scripts et références programmatiques ([[#R-054]]). Mais l'**afficher tel quel** comme libellé d'option Notion (« NOTE_CONCEPT ») dégrade fortement l'usage humain : illisible au premier coup d'œil, donne l'impression d'un système purement technique, peu engageant pour les utilisateurs LBP. Or les BDDs Notion sont aussi des outils de pilotage humain. La séparation **code (immuable) ↔ libellé (humain)** doit donc s'appliquer aux taxons exactement comme elle s'applique aux docs méta ([[#R-064]] : filename humain identique au title, code séparé en frontmatter).
- **How to apply** : pour toute taxonomie LBP consommée par une propriété select / multi-select Notion :
  1. **Code immuable du taxon** (frontmatter taxo, références dans les manuels, scripts d'audit) : forme programmatique en MAJUSCULES, format `<NAMESPACE>.<TAXO>.<TOKEN>` ([[#R-054]] grammaire 2). Ex : `TPL.SCOPE.NOTE_CONCEPT`, `META.FUNCTION.ORIENTER`, `OBJ.STATUT.VALIDE`.
  2. **Libellé canonique (= libellé Notion)** : forme **humaine courte**, lisible et engageante. Ex : « Note de concept », « Orienter », « Validé ». Sentence case français pour les français, casse adaptée aux noms propres pour les anglais (« System prompt », « WR-RD »).
  3. **Cohérence dans le tableau §3 du doc taxo** : les colonnes « Libellé (canonique) » et « Libellé Notion (recommandé) » sont identiques (forme humaine). Le « Code (immuable) » est séparé.
  4. **Aliases** : inclure le code MAJUSCULES dans les aliases pour permettre le matching agent (ex. alias `NOTE_CONCEPT` pour le libellé « Note de concept »).
- **Articulation** : [[#R-054]] (codification), [[#R-064]] (séparation code / nom humain pour docs méta), [[#R-068]] (aliases anti-redondance), [[CLAUDE.md#C-014]] (quirk wrapper MCP Notion).
- **Exemples** :
  - ✅ Taxo TPL.SCOPE : code `TPL.SCOPE.PROMPT_MAITRE`, libellé canonique = libellé Notion = « Prompt maître »
  - ✅ Taxo META.FUNCTION : code `META.FUNCTION.ORIENTER`, libellé canonique = libellé Notion = « Orienter »
  - ❌ Libellé Notion = `NOTE_CONCEPT` (forme code-style, peu humaine)
- **Conséquence si violation** : BDD Notion peu engageante pour les humains, illusion d'un système purement technique, lecture pénible des fiches.
- **Origine** : 03-05-2026, Phase 2.2 du chantier d'architecture des docs méta. Leonard a flaggé la dégradation visuelle lors de la création d'options select brutes.

#### R-068 : Aliases ne contiennent ni le code unique ni le nom canonique (anti-redondance)

- **Portée** : Transverse — toutes les BDDs LBP qui ont une propriété `Aliases` (ou équivalent : synonymes, noms alternatifs, alias).
- **Why** : Les aliases servent à matcher des **termes alternatifs** (ancien nom, variantes courantes, traductions, synonymes métier, jargon interne). Le code unique d'une fiche est déjà porté par la propriété `Code unique` ; le nom canonique est déjà porté par la propriété `Nom canonique` (ou `Title` Notion). Les inclure aussi en aliases est **redondant** et **dégrade le signal** des aliases.
- **How to apply** : pour toute fiche d'une BDD LBP, lors du remplissage de la propriété `Aliases` :
  1. **Inclure** : variantes courantes, anciens noms historiques, traductions, synonymes métier, jargon interne.
  2. **Exclure** : le `Code unique` exact, le `Nom canonique` exact, variantes triviales du nom canonique (ponctuation/casse seule).
  3. **Format** : liste séparée par `;`.
- **Articulation** : [[#R-064]] (séparation code / nom humain), [[#R-067]] (libellés humains pour valeurs select), [[CLAUDE.md#C-024]] (pattern wikilinks + aliases).
- **Exemples** :
  - ✅ Aliases pour fiche `TPL_NOTE_CONCEPT` : « template-note_concept_lbp ; template note de concept LBP ; template glossaire »
  - ❌ Aliases pour `TPL_DBMAN_BR` qui contient `TPL_DBMAN_BR` (déjà dans `Code unique`)
  - ❌ Aliases pour fiche « Template - Note de concept » qui contient « Template - Note de concept » (déjà dans `Nom canonique`)
- **Conséquence si violation** : redondance dans la BDD (signal bruité), maintenance dégradée (un rename oblige à 2 modifs au lieu d'1), perte de valeur de la propriété Aliases.
- **Origine** : 03-05-2026, Phase 2.2 b.2. Leonard a flaggé la redondance lors de la création de fiches calibration dans Templates Brain.

#### R-069 : Lecture complète du doc avant indexation dans une BDD Notion (pas seulement le frontmatter)

- **Portée** : Transverse — toute opération d'indexation d'un doc Markdown source dans une BDD Notion LBP (Brain, Twin, Mission Ops).
- **Why** : Le frontmatter d'un doc résume **le quoi** (titre, code, version, summary, purpose) ; mais le corps du doc porte **les singularités** : exemples concrets, anti-patterns, articulations avec d'autres objets, instructions agent, sections distinctes. Si l'agent indexeur se contente du frontmatter pour remplir les propriétés Notion, les fiches indexées deviennent **substituables les unes aux autres** et perdent leur valeur de routage agent / lecture humaine. La BDD se transforme en catalogue plat de descriptions génériques au lieu d'un index discriminant.
- **How to apply** : avant d'indexer un doc Markdown dans sa BDD Notion :
  1. **Lire l'intégralité du `.md` source** : frontmatter + corps + sections d'instructions agent (`@INSTR-START` etc.) + exemples + annexes.
  2. **Identifier les singularités** : qu'est-ce que ce doc fait que les autres docs du même type ne font pas ? Quels exemples concrets le caractérisent ? Quelles articulations spécifiques ? Quels anti-patterns documente-t-il ?
  3. **Rédiger les propriétés Notion en exploitant ces singularités** : Description discriminante, Valeur ajoutée LBP concrète, Usages IA potentiels qui citent les workflows concrets.
- **Articulation** : [[#R-029]] (Markdown SoT), [[#R-037]] (lecture complète obligatoire avant indexation Brain - généralisation à Twin/MO), [[CLAUDE.md#C-017]] (lecture WR-RD/taxos avant remplissage instance), [[CLAUDE.md#C-012]] (calibration avant production en série).
- **Exemples** :
  - ✅ Indexer `Template - Méthode LBP` en lisant ses 18 sections d'instructions agent + ses exemples → Description discriminante mentionnant les patterns spécifiques.
  - ❌ Indexer le même template en se contentant du `summary` → Description générique « modèle pour générer une méthode LBP au canon » qui pourrait s'appliquer à n'importe quel template.
- **Conséquence si violation** : BDD Notion devient un catalogue plat, routage agent dégradé, perte de valeur de la BDD.
- **Origine** : 03-05-2026, Phase 2.2 b.3. Indexation de 15 templates faite initialement à partir des seuls frontmatters → 15 fiches aux descriptions génériques détectées par Leonard. Refonte complète après lecture intégrale.

#### R-070 : Ban des noms d'agents dans les sources de vérité (Brain agent-agnostique)

- **Portée** : Transverse — toutes les sources de vérité Markdown LBP (manuels de BDD, WR-RD, taxonomies, docs méta indexés, notes de concept, templates) et toutes les fiches indexées dans les BDDs Notion (Brain, Twin, Mission Ops).
- **Why** : Les noms d'agents (ex. brain architect, twin architect, kontext, futurs agents) sont des **artefacts évolutifs** : ils sont créés, renommés, fusionnés ou supprimés au fil des chantiers. Citer un nom d'agent dans une SoT crée un point d'attache fragile : si l'agent est renommé ou supprimé, des dizaines de SoT deviennent stale silencieusement (asymétrie). Le Brain doit rester **agent-agnostique** : décrire des actions, des opérations, des fonctions, mais pas qui les exécute.
- **How to apply** : pour toute SoT (frontmatter, corps, descriptions Notion, instructions d'écriture) :
  1. **Décrire des actions, pas des acteurs nommés** : « Génération guidée d'une nouvelle note de concept » plutôt que « Consommé par brain architect au démarrage de la création d'une nouvelle note de concept ».
  2. **Si nécessaire de mentionner un acteur, utiliser un rôle générique** : « consultant », « agent d'analyse », « agent producteur », « agent orchestrateur ». Ces rôles sont stables.
  3. **Ne jamais citer** : brain architect, twin architect, kontext, ou tout autre nom d'agent spécifique LBP. Pas non plus de noms d'agents externes (Claude, GPT-4, etc.).
- **Articulation** : [[#R-002]] (zero contamination — extension), [[#R-001]] (Markdown SoT), [[#R-071]] (auto-suffisance — même logique). Cas particulier de C-XXX qui restent dans CLAUDE.md (scope Session, hors SoT LBP).
- **Exemples** :
  - ✅ « Lecture obligatoire avant remplissage d'une fiche dans une BDD Brain »
  - ✅ « Mode de remplissage : consultant ; agent d'analyse »
  - ❌ « Consommé par brain architect au démarrage de la création »
  - ❌ « Sera consommé par kontext (runtime MO) au moment de l'instanciation »
- **Conséquence si violation** : asymétries silencieuses lors de l'évolution des agents (rename, fusion, suppression), couplage fort SoT ↔ agents qui freine l'évolution architecturale, dégradation de la lisibilité par tout intervenant qui ne connaît pas les noms des agents internes.
- **Origine** : 03-05-2026, Phase 2.2 b.3. Leonard a flaggé l'anti-pattern lors de l'indexation de 15 templates citant « brain architect », « twin architect » et « kontext ».

#### R-071 : Auto-suffisance des descriptions dans les sources de vérité (pas de comparaisons relatives)

- **Portée** : Transverse — toutes les descriptions de fiches dans les BDDs LBP (Notion : Description, Valeur ajoutée LBP, Usages IA potentiels, etc.) et toutes les descriptions structurantes dans les SoT Markdown.
- **Why** : Décrire une fiche par **comparaison à une autre** (« 11 sections vs 8 côté Twin/MO », « contrairement à X », « comme Y mais sans Z ») crée une **dépendance silencieuse** entre 2 docs. Si un doc cité évolue (ex. le manuel Twin passe de 8 à 9 sections), la description comparative devient fausse sans qu'aucun audit ne le détecte. Chaque SoT doit se décrire **par elle-même** (par ses caractéristiques intrinsèques), pas par différence avec d'autres docs.
- **How to apply** : pour toute description dans une SoT :
  1. **Décrire l'objet par lui-même** : ses propriétés, sa fonction, ses sections, son contenu.
  2. **Pas de comparaisons relatives** : éviter « vs autre doc », « contrairement à », « comme X mais avec Y », « plus/moins que », etc.
  3. **Si une distinction est essentielle pour la compréhension**, l'exprimer en **caractéristique intrinsèque** : « couvre les spécificités Twin (5D, jumelles texte) » plutôt que « 5 sections vs 4 côté Brain ».
  4. **Pas de citation de structure d'autres docs** : décrire la structure du doc courant, jamais celle d'un autre.
- **Articulation** : [[#R-001]] (Markdown SoT), [[#R-066]] (propriétaire canonique unique), [[#R-070]] (ban noms agents — même logique d'auto-suffisance), [[CLAUDE.md#C-027]] (pas d'infos temporaires dans SoT).
- **Exemples** :
  - ✅ « Modèle pour générer un manuel de BDD du Brain LBP : spécification champ par champ du modèle de données d'une BDD du méta-écosystème Brain »
  - ✅ « Couvre les spécificités Twin (couche 5D, jumelles texte expressives) »
  - ❌ « 11 sections (vs 8 côté Twin/MO — divergence assumée) »
  - ❌ « Niveau d'orchestration intermédiaire entre system prompt et logic block » (compare à 2 autres docs)
- **Conséquence si violation** : asymétries silencieuses au moindre changement d'un doc cité, couplage fort entre docs qui devrait rester découplés, dégradation de la lisibilité.
- **Origine** : 03-05-2026, Phase 2.2 b.3. Leonard a flaggé l'anti-pattern lors de l'indexation de 15 templates avec descriptions comparatives.

#### R-072 : Pas d'énumération de taxons dans les instructions d'écriture / descriptions ≤280

- **Portée** : Transverse — colonnes « Description et règles ≤280 (à coller dans Notion) » des manuels de BDD Brain ; colonnes « Instructions d'écriture » des manuels de BDD Twin et Mission Ops ; et leurs WR-RD dérivés.
- **Why** : Inliner les valeurs (taxons) d'une taxonomie dans une instruction d'écriture crée une **dépendance silencieuse** entre l'instruction et la version courante de la taxonomie. Si la taxonomie évolue (ajout, retrait, renommage de taxon), l'instruction devient fausse sans qu'aucun audit ne le détecte. L'agent qui consomme l'instruction cherchera des valeurs qui n'existent plus dans la propriété select/multiselect, créant routage erroné ou fiches incomplètes.
- **How to apply** : pour toute instruction d'écriture sur un champ taxonomique :
  1. **Mentionner uniquement le code de la taxonomie** : `Taxo: META.FUNCTION`.
  2. **Si hiérarchique, mentionner le niveau attendu** : `Niveau: category | subdomain | taxon`.
  3. **Ne jamais énumérer les valeurs** (taxons) dans l'instruction.
  4. **La source de vérité des valeurs reste le `.md` de la taxonomie** (réf. [[#R-052]]) — l'agent doit consulter la taxonomie ou la propriété select Notion pour les valeurs valides.
- **Articulation** : [[#R-001]] (Markdown SoT), [[#R-052]] (mini-doc taxonomie source de vérité sémantique), [[#R-066]] (propriétaire canonique unique), [[#R-071]] (auto-suffisance des descriptions — même logique d'évitement des dépendances silencieuses).
- **Exemples** :
  - ✅ « Classer le doc selon sa fonction systémique dominante; choisir 1 valeur; Taxo: META.FUNCTION; Niveau: taxon. »
  - ✅ « Indiquer l'état de gouvernance de la fiche; Taxo: OBJ.STATUT. »
  - ❌ « Classer selon sa fonction systémique (Orienter, Expliquer, Structurer, Normer, Opérer); Taxo: META.FUNCTION; Niveau: taxon. »
  - ❌ « Indiquer l'état (à traiter, en cours, validé, archivé); Taxo: OBJ.STATUT. »
- **Conséquence si violation** : asymétries silencieuses dès la moindre évolution de la taxonomie référencée, agents en routage erroné, repassage manuel sur N manuels au lieu de modifier uniquement le `.md` de taxonomie.
- **Origine** : 03-05-2026, Phase 3.B refonte Manuel + WR-RD `Docs méta LBP`. Lors de la migration `META.FAMILY → META.FUNCTION`, j'avais inliné les 5 taxons. Leonard a flaggé.

#### R-011 : Frontières fortes entre objets canoniques

- **Portée** : Twin
- **Why** : Le Twin produit de la valeur à condition que ses objets restent conceptuellement nets. Sans frontières strictes, les relations deviennent incohérentes et les analyses inexploitables.
- **How to apply** : Maintenir les distinctions canoniques suivantes, qui ne doivent jamais être confondues :
  - une **Organisation** n'est pas un **Collectif** (institution juridique vs groupement humain opérant)
  - un **Poste** n'est pas un **Individu** (position formelle vs personne physique)
  - un **Actif** n'est pas un **Environnement** (support mobilisable vs cadre d'usage/contrainte)
  - une **Pratique** n'est pas un **Processus** (pattern opérant récurrent vs fonctionnement structuré)
  - une **Problématique** n'est pas un **Enjeu** (nœud diagnostique consolidé vs formulation structurée d'un besoin/tension)
  - un **Modulateur** n'est ni une **Capacité**, ni une **Pratique**, ni une **Problématique** (condition d'effectivité transversale)
  - un **Événement** n'est pas une **Initiative** (repère temporel vs effort intentionnel structuré)
  - une **Action détectée** n'est pas une **Pratique** (geste observé vs pattern récurrent consolidé)
- **Articulation** : [[#R-012]] (séparation 4 régimes — autre frontière fondamentale).
- **Exemples** : ✅ Une équipe produit = Collectif ; SA TotalEnergies = Organisation / ❌ "Équipe ABC (SA)" dans Organisations.
- **Origine** : Panorama V2 v3, §3.2.

#### R-012 : Séparation des 4 régimes de connaissance

- **Portée** : Twin
- **Why** : Éviter les glissements entre symptôme et diagnostic, la sur-interprétation du brut, la confusion entre vu/pensé/décidé.
- **How to apply** : Tout contenu du Twin relève d'un des 4 régimes, à ne jamais mélanger :
  1. **Preuve source** : observé, documenté, cité, transcrit
  2. **Qualification structurée** : typé, relié, mis en forme
  3. **Consolidation analytique** : stabilisé comme objet de lecture/diagnostic
  4. **Pilotage / action** : oriente, mesure, transforme
- **Articulation** : [[#R-002]] (zero contamination — autre frontière), [[#R-011]] (frontières objets), [[CLAUDE.md#C-018]] (vérifier régime BDD avant de signaler une anomalie de relation absente).
- **Origine** : Panorama V2 v3, §3.1.

#### R-013 : Sobriété relationnelle

- **Portée** : Twin
- **Why** : La saturation relationnelle rend le graphe illisible et les rollups peu fiables. Les "edges décoratifs" détériorent la valeur analytique.
- **How to apply** : Une relation réelle n'est créée que si elle apporte un gain clair de : compréhension, traversée, consolidation, comparaison, ou diagnostic. Éviter les relations "au cas où" et les raffinements sans gain net.
- **Articulation** : [[#R-014]] (règle absolue sandboxes), [[#R-017]] (sobriété rollups), [[#R-058]] (pas de jumelles texte sur Brain — distinction stricte).
- **Exemples** : ✅ `Organisation → comprend → Collectif` ; `OKR → est mesuré par → Indicateur` / ❌ Relation décorative "est mentionné par".
- **Origine** : Panorama V2 v3, §3.3 et §8.1.

#### R-014 : Règle absolue des sandboxes

- **Portée** : Twin
- **Why** : Les sandboxes servent à explorer et pré-consolider sans figer le graphe officiel. Y introduire des relations réelles transformerait la sandbox en BDD parallèle semi-officielle.
- **How to apply** : Une BDD sandbox n'a **jamais** de relations réelles avec les autres BDD du Twin, **à une seule exception** : la relation vers `Sources d'informations`. Les liens se matérialisent uniquement via jumelles textes.
- **Articulation** : [[#R-015]] (jumelles textes systématiques), [[#R-021]] (consolider vs promouvoir), [[#R-022]] (critères promotion sandbox→officielle).
- **Exemples** : ✅ Sandbox Pratiques → jumelle texte "est conduite par (collectifs) (texte)" / ❌ Sandbox Pratiques → relation réelle vers Collectifs.
- **Origine** : Panorama V2 v3, §3.4.

#### R-015 : Jumelles textes systématiques

- **Portée** : Twin
- **Why** : Préserver la formulation observée dans les sources, permettre la consolidation progressive, garder un indice relationnel avant validation, servir de base de vérification pour humain ou agent.
- **How to apply** : Pour chaque relation réelle dans une BDD officielle, prévoir une **jumelle texte** qui conserve les formulations observées. Exemple : `est conduite par (collectifs) (texte)` accompagne `est conduite par (collectifs)`. Dans une sandbox, **seule la jumelle texte** existe.
- **Articulation** : [[#R-014]] (sandbox = uniquement jumelles), [[#R-058]] (Brain = pas de jumelles — distinction stricte des doctrines Brain vs Twin).
- **Origine** : Panorama V2 v3, §8.2.

#### R-016 : La 5D est une matrice de lecture, jamais une preuve primaire

- **Portée** : Twin
- **Why** : La 5D sert à rendre visibles des structures, comparer des objets hétérogènes, synthétiser des traversées. Elle ne remplace pas la preuve, qui reste portée par objets, relations, propriétés spécifiques, sources, indices.
- **How to apply** : Utiliser la 5D pour : contribution, exposition, dépendance, causalité/impact/risque, pilotage/mesure. Ne jamais l'utiliser pour reclassifier les objets ou fonder un diagnostic.
- **Articulation** : [[#R-017]] (sobriété rollups — la 5D peut générer des rollups, à ne pas multiplier).
- **Origine** : Panorama V2 v3, §3.5 et §8.5.

#### R-017 : Sobriété des rollups et formules

- **Portée** : Twin
- **Why** : Les couches calculées ne sont pas là pour "faire riche". Elles doivent révéler un écart, un profil, une dépendance, une vulnérabilité, ou un état utile à la lecture.
- **How to apply** : Un rollup ou une formule n'est conservé que s'il améliore réellement l'intelligibilité. Jamais de formule décorative. Pas de rollup dans une sandbox sans relations réelles.
- **Articulation** : [[#R-013]] (sobriété relationnelle), [[#R-014]] (sandbox sans rollups), [[#R-016]] (5D = lecture, pas preuve).
- **Exemples** : ✅ Formule `Vulnérabilité nette de l'actif`, rollup `Profils 5D agrégés d'exposition` / ❌ Formule "nombre total de relations".
- **Origine** : Panorama V2 v3, §3.6, §8.6, §8.7.

#### R-018 : Spécialisation des propriétés génériques à l'écriture

- **Portée** : Twin
- **Why** : Un socle générique commun ne garantit pas une grammaire de remplissage identique. Une description d'individu ne ressemble pas à une description d'actif.
- **How to apply** : Respecter les propriétés génériques communes (Description, Indices observés, Indices d'existence, Commentaires, Merge Notes, Logs) mais appliquer des **instructions d'écriture spécifiques à chaque objet**. Les manuels de BDD portent cette doctrine via les colonnes « Instructions d'écriture » de leur section 4.
- **Articulation** : [[#R-019]] (5 couches BDD), [[#R-041]] (propagation Manuel→WR-RD).
- **Exemples** : ✅ Description d'une problématique = nœud diagnostique consolidé + périmètre + logique centrale ; Description d'un actif = ce que c'est + à quoi il sert + pour qui / ❌ Description uniforme "texte libre 3-10 lignes".
- **Origine** : Panorama V2 v3, §3.7 et §8.4.

#### R-019 : Architecture en 5 couches d'une BDD bien spécifiée

- **Portée** : Twin
- **Why** : Homogénéité de design et lisibilité des fiches. Chaque couche répond à une question distincte.
- **How to apply** : Une BDD importante du Twin est pensée comme un empilement cohérent :
  1. **Propriétés génériques** (gouvernance, traçabilité)
  2. **Relations + jumelles textes** (graphe + formulation observée)
  3. **Propriétés spécifiques** (pouvoir explicatif propre)
  4. **Couche 5D** (traversabilité systémique)
  5. **Couche calculée** (rollups + formules)
- **Articulation** : [[#R-018]] (spécialisation à l'écriture), [[#R-047]] (ordering Notion qui matérialise les couches dans l'UI).
- **Exemples** : Variantes d'intensité selon famille (registre, socle sémantique, extraction factuelle, socle structurel, post-traitement analytique) - cf. Panorama §9.2.
- **Origine** : Panorama V2 v3, §9.1.

#### R-020 : Traçabilité obligatoire des fiches importantes

- **Portée** : Twin
- **Why** : Un diagnostic ou une lecture doit toujours pouvoir être relu, questionné, justifié, recontextualisé.
- **How to apply** : Toute fiche importante doit rester **réauditable** via :
  - Sources (relation vers `Sources d'informations`)
  - Indices observés (journal structuré)
  - Indices d'existence de l'objet
  - Logs / Révisions LBP
  - Traces de merge si applicable
- **Articulation** : [[#R-023]] (progressivité — la traçabilité accompagne la densification), [[#R-025]] (tableau maître).
- **Origine** : Panorama V2 v3, §13.2.

#### R-021 : Distinction stricte fusionner / consolider / promouvoir

- **Portée** : Twin
- **Why** : Ces trois opérations sont fondamentalement différentes. Les confondre produit des décisions mal arbitrées et des graphes incohérents.
- **How to apply** : Distinguer systématiquement :
  - **Fusionner** : plusieurs fiches désignent réellement le même objet → merge (au sein d'une même BDD)
  - **Consolider** : plusieurs entrées amont convergent vers un objet plus structuré (signaux → enjeu, enjeux → problématique, actions → processus candidat, actions → pratique)
  - **Promouvoir** : une entrée sandbox devient une BDD officielle
- **Articulation** : [[#R-014]] (sandboxes), [[#R-022]] (critères promotion).
- **Exemples** : ✅ "Fusion" dans Merge Notes d'une BDD ; "Consolidation" dans le passage Journal des signaux → Enjeux / ❌ Parler de "fusion" pour une promotion sandbox.
- **Origine** : Panorama V2 v3, §13.3.

#### R-022 : Critères minimaux de promotion sandbox → BDD officielle

- **Portée** : Twin
- **Why** : Éviter les promotions trop précoces qui polluent le graphe officiel.
- **How to apply** : Une promotion est autorisée uniquement si tous les critères suivants sont remplis :
  1. **Preuves suffisantes** (indices observés + indices d'existence)
  2. **Formulation stabilisée**
  3. **Absence de confusion majeure** avec un objet déjà existant
  4. **Valeur analytique nette** attendue après promotion
  5. **Cohérence avec la frontière conceptuelle** de la BDD cible
- **Articulation** : [[#R-014]] (sandbox = pas de relations réelles), [[#R-021]] (distinction promotion vs fusion vs consolidation).
- **Origine** : Panorama V2 v3, §13.4.

#### R-023 : Progressivité du remplissage

- **Portée** : Twin
- **Why** : Le Twin n'est pas conçu pour être "plein" immédiatement mais densifié progressivement à mesure que la preuve augmente. Imposer une complétude uniforme génère du remplissage artificiel.
- **How to apply** : Toutes les BDD n'ont pas besoin du même niveau de densité au même moment. Ce qui compte : la qualité de ce qui est utile pour la question analytique du moment.
- **Articulation** : [[#R-020]] (traçabilité), [[#R-024]] (lecture 3 niveaux — la progressivité s'évalue par niveau).
- **Origine** : Panorama V2 v3, §13.5.

#### R-024 : Lecture du Twin sur 3 niveaux simultanés

- **Portée** : Twin
- **Why** : Le Twin n'est pas un entrepôt mais une machine de lecture systémique. Séparer les 3 niveaux évite les lectures faussement sûres.
- **How to apply** : Toute traversée/analyse doit articuler :
  1. **Niveau 1 - ce qui existe** : objets, acteurs, supports, contextes, temps
  2. **Niveau 2 - ce qui se passe** : actions, pratiques, processus, signaux, enjeux, transformations
  3. **Niveau 3 - ce que cela signifie et ce qu'il faut en faire** : problématiques, capacités, principes, modulateurs, OKR, indicateurs
- **Articulation** : [[#R-016]] (5D pour traversée), [[#R-023]] (progressivité par niveau).
- **Origine** : Panorama V2 v3, §14.3.

#### R-025 : Tableau maître canonique obligatoirement tenu à jour

- **Portée** : Twin (absolue)
- **Why** : Le tableau maître est la référence canonique du Twin. Sans lui, l'architecture dérive.
- **How to apply** :
  - Toute création de BDD doit être ajoutée au tableau maître
  - Toute suppression doit y être arbitrée
  - Tout changement de régime architectural doit y être explicité
  - Toute sandbox doit être distinguée de sa BDD officielle cible
- **Articulation** : [[#R-066]] (propriétaire canonique unique — le tableau maître applique R-066 au catalogue des BDDs Twin).
- **Origine** : Panorama V2 v3, §4.3. Tableau maître reproduit dans `[[Architecture - Twin]]`.

#### R-049 : Déclaration obligatoire de la `ui_family` pour toute BDD Twin

- **Portée** : Twin
- **Why** : D-017 a adopté un prisme `ui_family` orienté utilisateur (app LBP) en 7 valeurs (Langage, Structure, Cadres, Moteur, Pilotage, Ancrages, Objets candidats). Sans déclaration explicite et systématique de cette famille pour chaque BDD, l'app et le Brain peuvent diverger silencieusement, ce qui casse la cohérence UX/source de vérité.
- **How to apply** : Toute BDD du Twin (officielle ou sandbox) doit déclarer son `ui_family` dans :
  1. **Frontmatter du manuel parent** (champ `ui_family` parmi les 7 valeurs canoniques). Ex. : `ui_family: "Structure"`.
  2. **Registre Notion `Manuels de BDD`** (propriété select `Famille UI` avec les 7 valeurs).
  3. **bdd_registry.json** : champ `ui_family`.
  4. **Nouvelle BDD** : la déclaration `ui_family` est obligatoire dès la création du manuel parent ; aucune BDD ne peut être indexée Notion sans ce champ.
- **Valeurs canoniques** (strictes, casse exacte) : `Langage`, `Structure`, `Cadres`, `Moteur`, `Pilotage`, `Ancrages`, `Objets candidats`.
- **Note** : `Objets candidats` est en **2 mots** intentionnellement (les 6 autres sont en 1 mot). Cette dissonance typographique signale que cette famille n'est pas un prisme de l'entreprise comme les autres, mais un **statut d'objet** (en cours de qualification). Détail dans D-017.
- **Hors scope** : les WR-RD ne portent **pas** ce champ (le WR-RD est un artefact runtime ; l'UX n'est pas son rôle).
- **Articulation** : [[#R-055]] (frontmatter en 3 zones), [[#R-067]] (libellés humains pour les valeurs select Notion).
- **Exemples** :
  - ✅ `ui_family: "Structure"` (Organisations, Collectifs, Postes, Individus)
  - ✅ `ui_family: "Objets candidats"` (toutes les sandboxes)
  - ❌ `ui_family: "objets candidats"` (casse non canonique)
  - ❌ `ui_family: "Sandboxes"` (valeur non canonique)
- **Origine** : 27-04-2026, Phase 6.5 Twin v2. Capture déclenchée par l'adoption de D-017 (ui_family en 7 valeurs orientées utilisateur) et la nécessité d'imposer la déclaration sur les 28 BDDs Twin en cours de création. Champ `Découverte` non explicitement formalisé en legacy, restauré ici à partir du contexte de Phase 6.5.

#### R-050 : Propriété conditionnelle `Lien vers la note avancée` (URL)

- **Portée** : Twin (BDD à objets stabilisés)
- **Why** : Compléter l'identité structurée d'un objet par un **lien vers une note approfondie** (Brick de connaissance générée via les Templates de Bricks LBP). Cela donne aux agents et consultants un canal d'approfondissement narratif (profil avancé d'un individu, d'une organisation, d'un actif, etc.) qui complète les propriétés structurées sans alourdir la fiche. Cf. D-018 pour le lien doctrinal Bricks ↔ Notes avancées.
- **How to apply** :
  1. **Type Notion** : URL.
  2. **Position dans le schéma** : tête du Bloc 3 (queue générique), juste avant `Exemples concrets` ([[#R-047]]).
  3. **Inclusion conditionnelle** : la propriété est présente uniquement si la BDD désigne des **objets institutionnels stabilisés et durables**. Elle est **absente** dans :
     - Les BDD sandbox (objets en cours de stabilisation/test).
     - Les BDD de candidats (ex. Processus candidats - objets en cours de qualification).
     - Les BDD de signaux/actions/traces (Journal des signaux, Actions détectées) - l'objet est une trace, pas une entité durable méritant une note narrative.
     - Les BDD d'indicateurs (sur-documentation inutile sur des mesures).
  4. **Mécanisme d'inclusion** : chaque manuel Twin déclare dans son frontmatter `has_advanced_note: true | false`. Le template manuel BDD lit ce champ pour décider d'inclure ou non la propriété en section 4.1.
  5. **Instructions d'écriture** : "Renseigner, si elle existe, l'URL d'une note avancée (Brick de connaissance) qui approfondit l'objet (analyse détaillée, carte causale, profil organisationnel/individu, documents associés) ; laisser vide si non pertinent ; utiliser des liens stables."
  6. **Source de remplissage** : consultant.
- **Liste actuelle (Twin v2)** des BDD `has_advanced_note: true` (18) : Organisations, Collectifs, Postes, Individus, Actifs, Environnements, Événements, Relations inter-organisations, Glossaire spécifique, Initiatives organisationnelles, Modulateurs, Capacités organisationnelles, OKR, Pratiques organisationnelles, Principes organisationnels, Problématiques, Processus, Enjeux.
- **Liste actuelle (Twin v2)** des BDD `has_advanced_note: false` (10) : 6 sandboxes + Processus candidats + Journal des signaux + Actions détectées + Indicateurs.
- **Articulation** : [[#R-047]] (ordering propriétés Twin), [[#R-049]] (ui_family), [[#R-055]] (frontmatter has_advanced_note).
- **Exemples** : ✅ `https://notion.so/Profil-Organisationnel-Numalis-...` / ❌ propriété présente sur fiche `OKR sandbox` (sandbox = exclu).
- **Origine** : 27-04-2026, Leonard, Phase 6.5.

---


---

# 6) Archives — Règles intrinsèques - LBP


*Items migrés vers d'autres catalogues, conservés ici pour traçabilité (IDs immuables, jamais réutilisés).*

#### R-028 : Cohérence manuel ↔ doc clefs de lecture

- **Archivé** : 03-05-2026 — Migrée vers le catalogue Règles de propagation - LBP (cascade événementielle, donc PROP plutôt que R).
- **Remplacée par** : [[Règles de propagation - LBP#PROP-001]]
- **Portée** : Brain (propagation vers docs dérivés)
- **Why** : Le doc *Instructions d'écriture & clefs de lecture* d'une BDD est **dérivé** du manuel de BDD correspondant. Une asymétrie entre les deux produit des agents qui écrivent/lisent différemment de la spec, et des incohérences dans le Twin.
- **How to apply** : Le **manuel de BDD est source de vérité**. À chaque mise à jour d'un manuel :
  1. Identifier le doc clefs de lecture correspondant (WR-RD côté Brain Twin/MO ; ancien `Clefs de lectures/` legacy à migrer)
  2. Vérifier la cohérence (champs, instructions d'écriture, clefs de lecture, taxonomies référencées)
  3. Mettre à jour le doc dérivé si asymétrie
  4. Consigner la MAJ dans les logs du doc dérivé
- **Articulation** : [[#R-041]] (propagation Manuel→WR-RD obligatoire — extension générale de R-028 au cas WR-RD), [[#R-042]] (QA stricte d'égalité).
- **Exemples** : ✅ On renomme le champ "Rôles officiels" en "Postes" dans le manuel → on met à jour le WR-RD correspondant / ❌ On modifie un manuel sans vérifier le doc dérivé.
- **Origine** : 24-04-2026, confirmé par Leonard.


#### R-041 : Propagation Manuel de BDD → WR-RD obligatoire

- **Archivé** : 03-05-2026 — Migrée vers le catalogue Règles de propagation - LBP (cascade événementielle, donc PROP plutôt que R).
- **Remplacée par** : [[Règles de propagation - LBP#PROP-001]]
- **Portée** : Brain (toute BDD ayant un WR-RD instancié)
- **Why** : Le WR-RD est une **projection stricte** de la section 4 du manuel parent (D-016). Si une propriété change dans le manuel (création, suppression, modification de Type, Cardinalité, Taxonomie, Forme logique, Instructions d'écriture, Clefs de lecture, Utilité ou Exemples) sans propagation au WR-RD, alors le WR-RD ment aux agents qui le consomment runtime → erreurs de saisie ou d'interprétation. La direction de propagation est unilatérale : **manuel → WR-RD, jamais l'inverse**.
- **How to apply** :
  - Toute modification d'une propriété en section 4 d'un Manuel de BDD (sous-sections 4.1 à 4.5) déclenche **obligatoirement** la mise à jour du WR-RD correspondant.
  - Pour chaque propriété modifiée, reporter les colonnes retenues dans le WR-RD : Champ, Type, Taxonomie(s) - codes, Cardinalité / multiplicité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité, Exemples.
  - Bumper la version du WR-RD (`version` dans frontmatter) et son `template_version` si le template a évolué.
  - Le WR-RD ne doit **jamais** être édité indépendamment du manuel parent : si une formulation pose problème dans le WR-RD, corriger d'abord le manuel parent puis re-projeter.
  - À l'inverse : aucune modification du WR-RD ne doit remonter "à reculons" dans le manuel sans passer par une décision éditoriale explicite côté manuel.
- **Articulation** : [[#R-028]] (cohérence manuel ↔ doc clefs de lecture — généralisation), [[#R-042]] (QA stricte d'égalité), [[#R-045]] (manuel = SoT pour génération BDD), [[CLAUDE.md#C-009]] (annonce explicite de la propagation Manuel ↔ WR-RD).
- **Outillage suggéré** : à terme, un script de génération automatique du WR-RD à partir du manuel parent (extraction des 9 colonnes des sous-sections 4.1 à 4.5).
- **Conséquence si violation** : WR-RD désaligné = agents qui produisent des données non conformes au manuel = pollution silencieuse du Twin client. À détecter au plus tôt par audit régulier.
- **Origine** : 26-04-2026, Leonard, après instanciation des 3 premiers WR-RD (Actifs, Pratiques organisationnelles, Journal des signaux).


#### R-042 : QA stricte d'égalité entre WR-RD et section 4 du manuel parent

- **Archivé** : 03-05-2026 — Migrée vers le catalogue Règles de propagation - LBP (cascade événementielle, donc PROP plutôt que R).
- **Remplacée par** : [[Règles de propagation - LBP#PROP-001]]
- **Portée** : Brain (toute génération ou modification d'un WR-RD)
- **Why** : Le WR-RD étant une projection stricte (D-016, [[#R-041]]), tout écart entre le contenu d'une cellule du WR-RD et la cellule correspondante du manuel parent constitue une **dérive éditoriale** silencieuse. Une instruction d'écriture reformulée "pour faire mieux" dans le WR-RD est une violation : le canon est dans le manuel.
- **How to apply** :
  - À la génération ou à la modification d'un WR-RD, vérifier que **chaque cellule** des 9 colonnes retenues est **mot pour mot identique** à la cellule correspondante du manuel parent (sections 4.1 à 4.5, colonnes : Champ, Type, Taxonomie(s) - codes, Cardinalité / multiplicité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité, Exemples).
  - Tolérances admises : adaptations purement typographiques inévitables au transfert Markdown - à signaler dans les `Logs / Révisions` du WR-RD si appliquées.
  - Si une instruction d'écriture ou clef de lecture est jugée mal formulée dans le manuel, **corriger d'abord le manuel parent** puis re-projeter vers le WR-RD (cohérent avec [[#R-041]]).
- **Contrôle** : avant tout commit / publication d'un WR-RD, faire un diff avec la section 4 du manuel parent sur les 9 colonnes retenues. Aucun écart non-typographique ne doit subsister.
- **Articulation** : [[#R-041]] (propagation obligatoire), [[CLAUDE.md#C-009]] (annonce explicite).
- **Outillage suggéré** : script de diff automatique manuel ↔ WR-RD à terme, avec alerte sur les cellules divergentes.
- **Conséquence si violation** : voir [[#R-041]] - désalignement silencieux entre les deux artefacts, lecture incohérente côté agents et humains.
- **Origine** : 26-04-2026, Leonard, après les 3 premiers WR-RD instanciés.


#### R-075 : Vérification de cohérence inter-catalogues lors de l'ajout/modification d'item citant un autre catalogue

- **Archivé** : 03-05-2026 — Migrée vers le catalogue Règles de propagation - LBP (cascade événementielle, donc PROP plutôt que R).
- **Remplacée par** : [[Règles de propagation - LBP#PROP-011]]
- **Portée** : Transverse — tous les catalogues docs méta LBP (Règles intrinsèques, Décisions architecturales, Codification, Workflows opérationnels, Règles de propagation, et tout futur catalogue).
- **Why** : Quand un item d'un catalogue (ex. R-XXX) cite par wikilink un item d'un autre catalogue (ex. `[[Règles de propagation - LBP#PROP-XXX]]`), l'ajout / la modification de cet item crée une dépendance entre les deux catalogues. Sans vérification croisée systématique au moment du changement, on risque : (a) wikilink mort si l'item cité n'existe pas (faute de frappe ou item non encore créé) ; (b) sens cité divergent du sens réel de l'item cible (drift sémantique silencieux) ; (c) doublon implicite (même règle exprimée 2× sous formes différentes) ; (d) dépendance bidirectionnelle attendue mais non matérialisée côté cible. Ces asymétries silencieuses sont le 1er coût de la fragmentation en catalogues atomiques.
- **How to apply** : à chaque ajout / modification / suppression d'un item citant un autre catalogue, **consulter le catalogue cité en parallèle** et vérifier :
  1. **Existence** : l'item cité existe et a le bon ID (pas de wikilink mort).
  2. **Cohérence sémantique** : le sens cité par cet item est cohérent avec ce que l'item cible définit réellement (relire l'item cible).
  3. **Anti-doublon** : aucun doublon implicite n'est créé entre les deux catalogues (même contrainte ou cascade exprimée 2× sous formes différentes — auquel cas garder un seul propriétaire canonique cf. [[#R-066]]).
  4. **Bidirectionnalité** : si la citation crée une dépendance bidirectionnelle (l'item cité devrait à son tour mentionner cet item pour cohérence), faire la modification réciproque OU documenter pourquoi la bidirectionnalité n'est pas requise.
- **Articulation** : [[#R-066]] (propriétaire canonique unique — application directe), [[#R-074]] (méthodes pour règles de maintenance — R-075 sera intégrée à la future Méthode - Maintenance d'un catalogue Brain), [[CLAUDE.md#C-024]] (wikilinks). **Note de migration** : R-075 est conceptuellement une **règle de propagation** (déclenchée par un événement = ajout/modif d'item) ; elle migrera vers PROP-XXX quand `Règles de propagation - LBP` sera produite (Phase 4), aux côtés de [[#R-041]], [[#R-042]], [[#R-028]] qui sont elles aussi des PROP « déguisées ».
- **Exemples** :
  - ✅ Ajout d'un nouveau R-XXX qui cite `[[Règles de propagation - LBP#PROP-005]]` → ouvrir Règles de propagation, vérifier que PROP-005 existe et que ce qu'elle définit est bien ce qu'on cite.
  - ✅ Modification d'un WF-XXX qui cite plusieurs R-XXX → relire chaque R citée pour s'assurer que la modification du WF reste cohérente avec ce que les R prescrivent.
  - ❌ Capturer un nouveau D-XXX qui cite `[[Règles intrinsèques - LBP#R-099]]` sans vérifier que R-099 existe (résultat : wikilink mort silencieux).
- **Conséquence si violation** : wikilinks morts, drift sémantique silencieux entre catalogues, doublons implicites, dépendances bidirectionnelles oubliées. Asymétries détectables seulement par audit transverse (coût élevé).
- **Origine** : 03-05-2026, en discussion Leonard suite à la rétrospective de migration de Règles intrinsèques v1.1. Capture proactive avant production des 4 catalogues restants pour formaliser la discipline de maintenance croisée.

## 5.8 Architecture & doctrine Twin

Règles structurantes propres au Digital Twin LBP : ontologie des objets canoniques, séparation des régimes de connaissance, doctrine relationnelle, 5D, traçabilité, lifecycle sandbox→officielle, génération des BDD Notion (ui_family, lien note avancée).



---

> **Maintenance et évolution de ce catalogue** : voir `[[Méthode - Maintenance d'un catalogue Brain]]`.
