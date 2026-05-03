---
# === Identité ===
title: "Décisions architecturales - LBP"
doc_type: doc_meta
code: "META_DECISIONS_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "TPL_META_CATALOGUE"
template_version: "1.6"
created_at: "03-05-2026"
updated_at: "03-05-2026"

# === Spec d'usage ===
function_meta: "META.FUNCTION.EXPLIQUER"
item_id_prefix: "D"
summary: "Catalogue des décisions architecturales atomiques D-XXX qui contextualisent l'écosystème LBP. Chaque D documente le POURQUOI d'un choix structurant : contexte qui a appelé la décision, options envisagées, choix retenu, conséquences sur l'écosystème, articulation avec règles et propagations dérivées. Couverture transverse Brain + Twin + Mission Ops."
purpose: "Référence canonique pour comprendre POURQUOI tel choix architectural a été fait. Toute règle (R-XXX), cascade (PROP-XXX) ou workflow (WF-XXX) dérivée d'une décision doit pouvoir être rattachée à sa D-XXX d'origine via le champ Articulation. Permet la révision éclairée d'une décision quand le contexte évolue (archivage de la D ancienne + création D nouvelle qui la remplace, IDs immuables)."
aliases:
  - "DECISIONS_LBP"
  - "ADR LBP"
  - "Architecture Decision Records LBP"
tags:
  - doc_meta
  - catalogue
  - decisions
  - expliquer
  - lbp
---

# Décisions architecturales - LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta LBP`).
> **Fonction systémique** : `META.FUNCTION.EXPLIQUER` (catalogue normatif des choix architecturaux structurants).
> **Public visé** : intervenants LBP (Leonard, Clément, futurs collaborateurs), agents (brain architect, agents d'analyse).

---

# 1) Vocation et périmètre

## 1.1 Vocation

Catalogue exhaustif des décisions architecturales (D-XXX) qui contextualisent l'écosystème LBP — Brain, Digital Twin, Mission Ops. Chaque D documente le **pourquoi** d'un choix structurant à un instant t : contexte qui a appelé la décision, options alternatives envisagées avec leur analyse, choix retenu énoncé clairement, conséquences directes sur l'écosystème, articulation avec les règles / cascades / workflows dérivés.

Le catalogue se lit selon 2 axes :
- **Chronologique** (via le champ `Date de décision` et le récap §4 trié par date) — reconstitution de l'évolution doctrinale.
- **Thématique** (via les sous-sections de §5) — lookup d'une décision par domaine.

## 1.2 Périmètre

**Inclus** :
- Décisions structurantes d'ontologie et de frontières d'objets canoniques (création / scission / renommage de BDDs).
- Décisions d'architecture transverse (lecture analytique, prismes UX, articulation des agents).
- Décisions de conventions documentaires et de lifecycle (arborescence vault, naming filenames, archivage).
- Décisions de codification, de templates et de migrations docs méta.
- Décisions fondatrices d'écosystème (stack technique, isolation Brain ↔ Twin/MO).

**Exclus** (anti-doublon, application [[Règles intrinsèques - LBP#R-066]]) :
- Règles atomiques applicables (`R-XXX`) dérivées d'une décision → vivent dans `[[Règles intrinsèques - LBP]]`.
- Cascades de propagation (`PROP-XXX`) dérivées d'une décision → vivent dans `[[Règles de propagation - LBP]]`.
- Workflows opérationnels (`WF-XXX`) qui orchestrent l'application d'une décision → vivent dans `[[Workflows opérationnels - LBP]]`.
- Conventions de codification détaillées → vivent dans `[[Codification - LBP]]`.
- Conventions de session (`C-XXX`) → vivent dans `CLAUDE.md`.
- Décisions purement opérationnelles d'une mission client (instances) → vivent dans Mission Ops de la mission concernée, pas dans le Brain.

## 1.3 Granularité d'item

- **1 D-XXX = 1 décision atomique** : 1 problème ou besoin précis, 1 set d'options analysées, 1 choix retenu opposable.
- Si une « décision » mêle plusieurs choix structurants indépendants, la décomposer en N items D-XXX.
- Si plusieurs décisions partagent le même contexte mais aboutissent à des choix distincts (ex. D-024 préfixe + D-025 fonctions systémiques + D-026 BDD séparée — toutes Phase 1.0), garder N items distincts pour permettre la révision indépendante.

**Test rapide de granularité** : si je peux écrire le contexte qui a motivé la décision en 3-5 lignes et énoncer le choix retenu en 1 phrase opposable (« on a décidé que X »), c'est une D-XXX légitime. Si la « décision » est diffuse, normative (« il faut X »), ou implicite, c'est probablement une R-XXX ou une convention informelle à promouvoir.

---

# 2) Anatomie d'un item

## 2.1 Schéma des champs (figé v1.0)

| Champ | Type | Description | Exemple |
|---|---|---|---|
| ID | code | Format `D-XXX` (3 chiffres, extension à 4 si > 999). Immuable. | `D-024` |
| Nom | texte court | Titre lisible humain de la décision, 5-15 mots. | Adoption du préfixe `META_` pour les codes des docs méta indexés (remplace `CHRT_`) |
| Portée | texte libre | Brain / Twin / Mission Ops / Transverse / Contextuel. Peut être préfixée pour préciser un sous-périmètre. | Brain — BDD `Docs méta LBP` |
| Date de décision | date | Format `JJ-MM-YYYY`. Date à laquelle la décision a été prise (peut différer de la date de capture). Permet la reconstitution chronologique. | 03-05-2026 |
| Contexte | texte long | Problème ou besoin qui motive la décision. Équivalent du « Why » d'une R-XXX. | Le préfixe historique `CHRT_` est cryptique et n'évoque pas la nature « doc méta »... |
| Options envisagées | texte long | Alternatives considérées avec analyse coûts/bénéfices. Peut être omis si une seule option évidente. | (A) Garder CHRT_ + ajouter préfixe par fonction... (B) Remplacer par préfixe par fonction... (C) Statu quo... (D) META_... |
| Décision | texte long | Choix retenu, énoncé clair et opposable. | Préfixe `META_<TOKEN>_<SCOPE>` pour tous les codes des docs méta indexés... |
| Conséquences | texte long | Effets directs sur l'écosystème : règles dérivées (R-XXX), cascades (PROP-XXX), workflows à mettre à jour, migrations à planifier. | ✅ Code parlant immédiatement... ⚠️ Coût migration ~11 codes existants à renommer... |
| Articulation | texte long | Wikilinks vers R-XXX / PROP-XXX / WF-XXX dérivées, autres D-XXX antécédentes / conséquentes / révisées. | [[Règles intrinsèques - LBP#R-064]] (naming docs méta), `[[Constitution des docs méta - LBP]]` |
| Origine | texte court | Contexte de capture (qui, dans quelle session/chantier la décision a été formalisée). Pas de date ici (déjà dans `Date de décision`). | Phase 1.0 du chantier d'architecture des docs méta. |

**Lecture du tableau** :
- Champs **génériques obligatoires** : ID, Nom, Portée, Date de décision, Origine.
- Champs **spécifiques obligatoires** : Contexte, Décision, Conséquences (l'anatomie minimale d'un ADR).
- Champs **fortement recommandés** : Options envisagées, Articulation.
- **Flexibilité de contenu** : `Options envisagées`, `Décision`, `Conséquences` acceptent listes numérotées, sous-titres, blocs de code si la nature de la décision le justifie (cf. [[Règles intrinsèques - LBP#R-073]]).

**Pas de champ `Statut`** (Adoptée / Révisée / Abandonnée) — cohérent avec [[Règles intrinsèques - LBP]] et [[Règles de propagation - LBP]] : un item dans §5 = en vigueur, un item dans §6 = révisée ou abandonnée. Archivage avec champs `Archivé` (date + raison) + `Remplacée par` (wikilink vers D-YYY successeur) si applicable.

## 2.2 Format de l'ID

- **Préfixe** : `D` (figé)
- **Numéro** : 3 chiffres (extension à 4 si dépassement de 999)
- **Incrément** : monotone, jamais réutilisé même après archivage d'une D
- **Immuabilité** : un ID attribué ne change jamais (cf. [[Règles intrinsèques - LBP#R-005]] et §6 Archives)

## 2.3 Mini-exemple d'un item bien formé

```
#### D-024 : Adoption du préfixe `META_` pour les codes des docs méta indexés (remplace `CHRT_`)

- **Portée** : Brain — BDD `Docs méta LBP`
- **Date de décision** : 03-05-2026
- **Contexte** : Le préfixe historique `CHRT_` (« charte ») est cryptique et n'évoque pas la nature « doc méta »...
- **Options envisagées** : (A) garder CHRT_ + préfixe par fonction... (B) remplacer par préfixe par fonction... (C) statu quo... (D) remplacer par META_...
- **Décision** : (D) Préfixe `META_<TOKEN>_<SCOPE>` pour tous les codes des docs méta indexés.
- **Conséquences** : ✅ Code parlant immédiatement. ⚠️ Coût migration ~11 codes existants.
- **Articulation** : [[Règles intrinsèques - LBP#R-064]] (naming docs méta), `[[Constitution des docs méta - LBP]]`.
- **Origine** : Phase 1.0 du chantier d'architecture des docs méta.
```

---

# 3) Garde-fous de cohérence

## 3.1 Avec [[Règles intrinsèques - LBP]] et [[Règles de propagation - LBP]]

- **Garde-fou** : toute D-XXX qui produit une règle applicable (R-XXX) ou une cascade (PROP-XXX) doit citer cette dérivation dans son champ `Articulation`. Inversement, toute R-XXX ou PROP-XXX doit pouvoir être rattachée à au moins une D-XXX via son champ `Articulation`.
- **Justification** : la boucle de gouvernance documentaire (cf. `[[Constitution des docs méta - LBP]]` §7) dit : Décision → Règle / Propagation → Workflow. Une règle sans décision d'origine est suspecte (convention informelle non promue).

## 3.2 Avec [[Workflows opérationnels - LBP]]

- **Garde-fou** : un WF-XXX qui implémente une décision la cite par wikilink. La D-XXX décrit le pourquoi structurel ; le WF décrit le comment opérationnel. Pas de duplication.
- **Justification** : application directe de [[Règles intrinsèques - LBP#R-066]].

## 3.3 Avec `[[Codification - LBP]]`

- **Garde-fou** : les décisions de codification (préfixes de codes, format d'identifiants) sont énoncées comme D-XXX dans ce catalogue, mais leur grammaire détaillée vit dans `[[Codification - LBP]]`. Pas de duplication des règles de format.

---

# 4) Récap tabulaire

| ID | Nom | Date de décision | Sous-section (§5.x) | Origine |
|---|---|---|---|---|
| D-001 | Trio Drive + Obsidian + Git comme stack documentaire | 07-04-2026 | 5.1 Décisions fondatrices d'écosystème | Phase initiale de structuration LBP |
| D-002 | Scission UO → Organisation + Collectif | 22-04-2026 | 5.2 Ontologie des objets et frontières | Refonte Twin v2 (Panorama V2 v3) |
| D-003 | Renommage Ressources → Actifs | 22-04-2026 | 5.2 Ontologie des objets et frontières | Refonte Twin v2 |
| D-004 | Renommage Rôles officiels → Postes | 22-04-2026 | 5.2 Ontologie des objets et frontières | Refonte Twin v2 |
| D-005 | Création de la BDD Initiatives organisationnelles | 22-04-2026 | 5.2 Ontologie des objets et frontières | Refonte Twin v2 |
| D-006 | Création de la BDD edge Relations inter-organisations | 22-04-2026 | 5.2 Ontologie des objets et frontières | Refonte Twin v2 (suite à D-002) |
| D-007 | Création de 6 sandboxes spécialisées | 22-04-2026 | 5.2 Ontologie des objets et frontières | Refonte Twin v2 |
| D-008 | Tableau maître canonique à 29 BDD | 22-04-2026 | 5.3 Architecture transverse et lecture analytique | Refonte Twin v2 |
| D-009 | Chaînes de transformation de la connaissance comme paradigme de lecture | 22-04-2026 | 5.3 Architecture transverse et lecture analytique | Refonte Twin v2 |
| D-010 | Arborescence cible d'Architecture data (v2) | 24-04-2026 | 5.4 Conventions de docs et lifecycle documentaire | Phase préparation migration Twin v2 |
| D-011 | Conventions de nommage des fichiers Brain/Twin | 24-04-2026 | 5.4 Conventions de docs et lifecycle documentaire | Phase préparation migration Twin v2 |
| D-012 | Séquence de migration Twin v2 vers Architecture data (7 phases) | 24-04-2026 | 5.5 Codification, templates et migrations docs méta | Phase préparation migration Twin v2 |
| D-013 | Traçabilité de version de template d'instanciation | 25-04-2026 | 5.5 Codification, templates et migrations docs méta | Évolution template Manuel BDD vers v6.1.0 |
| D-014 | Colocalisation des docs WR-RD avec leurs manuels de BDD parents | 26-04-2026 | 5.4 Conventions de docs et lifecycle documentaire | Refonte arborescence post-Phase 5 |
| D-015 | Convention de nommage `00 - archives/` pour les dossiers d'archives | 26-04-2026 | 5.4 Conventions de docs et lifecycle documentaire | Refonte arborescence post-Phase 5 |
| D-016 | Rôle, contenu et format des docs WR-RD (Write Rules / Read Keys) | 26-04-2026 | 5.4 Conventions de docs et lifecycle documentaire | Phase 5 (génération WR-RD post-refonte Twin v2) |
| D-017 | Familles UI/UX comme prisme transverse de classification des BDD Twin | 27-04-2026 | 5.3 Architecture transverse et lecture analytique | Phase 6.5 (préparation app LBP côté UX) |
| D-018 | Bricks de connaissance comme Notes avancées des objets Twin | 27-04-2026 | 5.3 Architecture transverse et lecture analytique | Phase 6.5 (besoin de profondeur narrative sur objets Twin) |
| D-019 | Brain = environnement documentaire en évolution (Core+Motor) ; isolation Brain ↔ Mission Ops/Twin | 28-04-2026 | 5.1 Décisions fondatrices d'écosystème | Audit déséquilibre `Type fonctionnel` |
| D-020 | Propagation de la propriété `Version du template` à toutes les BDDs Brain | 28-04-2026 | 5.5 Codification, templates et migrations docs méta | Phase A4 (sync DDL Notion) |
| D-021 | Architecture des 3 agents LBP - Brain architect / Twin architect / KONTEXT | 28-04-2026 | 5.3 Architecture transverse et lecture analytique | Audit organisation Prompts + Logic blocks |
| D-022 | Différenciation assumée des frontmatters Twin et Mission Ops | 30-04-2026 | 5.4 Conventions de docs et lifecycle documentaire | Backlog 27-04-2026 (divergence templates) |
| D-023 | Mission Ops co-égal Brain/Twin + stack technique Notion (Brain) / Supabase (Twin + Mission Ops) | 30-04-2026 | 5.1 Décisions fondatrices d'écosystème | Audit absence formalisation MO + stack production |
| D-024 | Adoption du préfixe `META_` pour les codes des docs méta indexés (remplace `CHRT_`) | 03-05-2026 | 5.5 Codification, templates et migrations docs méta | Phase 1.0 chantier d'architecture des docs méta |
| D-025 | Adoption des 5 fonctions systémiques `META.FUNCTION` (remplace `META.FAMILY`) | 03-05-2026 | 5.5 Codification, templates et migrations docs méta | Phase 1.0 chantier d'architecture des docs méta |
| D-026 | Création de la BDD `Templates Brain` séparée — `Templates de Bricks` reste une BDD distincte | 03-05-2026 | 5.5 Codification, templates et migrations docs méta | Phase 1.0 chantier d'architecture des docs méta |

---

# 5) Catalogue

## 5.1 Décisions fondatrices d'écosystème

Décisions qui posent les contours fondamentaux de l'écosystème LBP : stack documentaire, frontières d'isolation entre domaines, choix de stack technique de production.

#### D-001 : Trio Drive + Obsidian + Git comme stack documentaire

- **Portée** : Transverse
- **Date de décision** : 07-04-2026
- **Contexte** : Besoin de stockage cloud (partage équipe), d'édition locale ergonomique, et de versioning fiable pour l'écosystème documentaire LBP.
- **Options envisagées** :
  - Tout sur Notion : simple mais pas de versioning fin, pas de portabilité.
  - Git + Markdown uniquement : portable mais pas de partage non-technique.
  - Drive + Obsidian + Git : combine les trois.
- **Décision** : Drive synchronise (partage équipe), Obsidian édite en local (ergonomie), Git versionne (historique fin et portabilité).
- **Conséquences** :
  - ✅ Portabilité maximale, historique fin, graphe Obsidian navigable.
  - ⚠️ Risque de désync entre les trois (à gouverner via [[Règles intrinsèques - LBP#R-001]] Markdown SoT).
- **Articulation** : [[Règles intrinsèques - LBP#R-001]] (Markdown source de vérité — règle dérivée).
- **Origine** : Phase initiale de structuration LBP.

#### D-019 : Brain = environnement documentaire en évolution (Core+Motor) ; isolation Brain ↔ Mission Ops/Twin

- **Portée** : Brain (transverse à toutes ses BDDs) + frontière avec Mission Ops et Digital Twin
- **Date de décision** : 28-04-2026
- **Contexte** : L'écosystème LBP distingue 4 grands environnements : `Core` (concepts, glossaire, taxonomies), `Motor` (méthodes, prompts, agents, templates, outils, logic blocks), `Digital Twin` (modélisation des organisations clients), `Mission Ops` (pilotage des missions et bricks produites). Les frontières Mission Ops ↔ Digital Twin sont nettes. En revanche, **côté Core et Motor, les contenus se mélangent en pratique** : la BDD Prompts LBP référence aussi bien des prompts qui manipulent le Twin d'un client que des prompts qui opèrent sur le Brain ; la BDD Manuels de BDD contient les manuels de toutes les BDDs (Brain + Twin + Mission Ops). Tenter de cloisonner Core et Motor dans le modèle de données crée des sous-typages artificiels.
- **Options envisagées** :
  1. Maintenir la distinction Core/Motor au niveau modèle de données → rejeté (sous-typages déséquilibrés).
  2. **Fusionner Core et Motor dans un « Brain » unifié** au niveau modèle de données, en conservant la nuance Core/Motor au niveau discours/documentation uniquement → **retenu**.
  3. Mapping Core/Motor en taxo séparée → rejeté (redondant avec `DBMAN.SCOPE`).
- **Décision** :
  1. **Brain = environnement documentaire en évolution** (les 11 BDDs Brain). Au niveau modèle de données, Core et Motor ne sont pas distingués : ce sont des **étiquettes de discours** utiles pour parler de l'écosystème, pas des prismes de classification structurels.
  2. **La nuance Core/Motor reste pertinente dans les `Domaine(s) d'usage`** des objets Motor Brain. La taxo `DOMAIN.USAGE` reste à 4 valeurs.
  3. **Isolation stricte Brain ↔ Mission Ops/Twin** : aucune relation Notion entre une BDD Brain et une BDD Mission Ops ou Digital Twin. Les BDDs MO/Twin sont **instanciées à chaque mission** (espaces clients distincts), tandis que les BDDs Brain sont **uniques et persistantes** (l'écosystème documentaire LBP).
- **Conséquences** :
  - ✅ Suppression de la propriété `Type fonctionnel` côté BDD Manuels de BDD (Notion + manuel).
  - ✅ La BDD Manuels de BDD ne porte plus de sous-typage par environnement (le scope est déjà capturé par `DBMAN.SCOPE`).
  - ✅ Cohérence sur `Domaine(s) d'usage` : conservé sur les 5 BDDs Motor Brain.
  - ⚠ Lorsqu'on parle « du Brain » en doctrine ou en règles, on parle de **l'environnement documentaire** (les 11 BDDs Brain + leurs docs) — pas des BDDs instanciées en mission.
  - ⚠ Les bricks produites en mission ne sont **pas** des objets Brain malgré leur valeur cognitive — elles vivent dans l'instance Mission Ops.
- **Articulation** : [[Règles intrinsèques - LBP#R-058]] (interdiction jumelles texte sur Brain — corollaire), [[#D-021]] (3 agents avec frontières d'isolation).
- **Origine** : Audit du déséquilibre observé sur la propriété `Type fonctionnel` de la BDD Manuels de BDD (Twin sur-subdivisé, Core/Motor/MO sans sous-familles).

#### D-023 : Mission Ops co-égal Brain/Twin + stack technique Notion (Brain) / Supabase (Twin + Mission Ops)

- **Portée** : Architecture transverse — gouvernance des 3 domaines + stack technique de production
- **Date de décision** : 30-04-2026
- **Contexte** : Audit 30-04-2026 a révélé l'absence de décision fondatrice formalisant **Mission Ops comme domaine co-égal** au Brain et au Twin. Toutes les décisions D-002 → D-021 couvraient essentiellement le Twin et le Brain. Mission Ops avait été instancié (4 BDDs, test Phase B) sans formalisation doctrinale. Par ailleurs, la **stack technique de production** n'avait jamais été formalisée : la maquette actuelle est sur Notion pour Brain et Twin/MO, mais le déploiement cible est différencié (Notion pour Brain, Supabase pour Twin + MO).
- **Options envisagées** :
  1. **MO sous-domaine du Twin** → rejeté (viole la séparation des régimes de connaissance et l'isolation D-019).
  2. **MO co-égal Brain/Twin avec stack unifié Notion** → rejeté (Notion ne supporte pas les volumes de Mission Ops à grande échelle, ni les instanciations multi-mission par client, ni les performances de lecture/écriture nécessaires en production).
  3. **MO co-égal Brain/Twin avec stack différencié** : Notion pour Brain (gouvernance, lent, manuel), Supabase pour Twin + MO (volumes, performance, instanciation client) → **retenu**.
- **Décision** :
  1. **Mission Ops est un domaine co-égal au Brain et au Twin**, gouverné par 4 BDDs structurelles : `Sources d'informations`, `Meetings`, `Actions LBP`, `Bricks`. Chaque mission consultant instancie son propre périmètre Twin + MO ; le Brain est partagé et stable.
  2. **Articulation entre les 3 domaines** :
     - Brain ↔ Twin : isolation stricte ([[#D-019]]). Le Brain fournit les manuels, taxonomies, méthodes, templates, prompts, agents, outils.
     - Brain ↔ MO : isolation stricte ([[#D-019]]). Le Brain fournit les templates de bricks que MO instancie.
     - Twin ↔ MO : articulation via les **Bricks** ([[#D-018]]) — les bricks MO documentent et alimentent les fiches Twin.
  3. **Stack technique cible** :
     - **Brain = Notion** : volumétrie modérée (~200 docs Markdown actifs), gouvernance manuelle, navigation hypertexte, audit visuel.
     - **Twin + Mission Ops = Supabase** : volumétrie potentiellement importante, performance critique, schéma stable car validé via la maquette Notion test. La maquette Notion actuelle de Twin+MO sera **portée** vers Supabase une fois le schéma figé.
  4. **Pas de pont direct Brain ↔ Twin/MO** au niveau technique. Les seuls « ponts » conceptuels sont les Bricks instanciées à partir des Templates de Bricks Brain (référence par code template, pas relation technique cross-stack).
- **Conséquences** :
  - ✅ Mission Ops devient un domaine de premier niveau, avec sa propre doctrine, ses règles propres, ses workflows propres.
  - ✅ Stack technique cible cohérente avec la nature de chaque domaine.
  - ✅ Le bundle de docs méta durables doit traiter les 3 domaines de façon symétrique.
  - ✅ Justifie la divergence assumée des frontmatters Twin/MO ([[#D-022]]).
  - ⚠ La maquette Notion Twin+MO devient une **fixture de validation de schéma**, pas une prod.
  - ⚠ Le portage Twin+MO vers Supabase est un chantier ultérieur (post-Phase C) qui devra être cadré séparément.
  - ⚠ Pas de pont direct Brain↔Twin/MO : les agents doivent intégrer cette frontière dans leur conception.
- **Articulation** : [[Règles intrinsèques - LBP#R-014]] (sandboxes Twin), [[#D-009]] (chaînes de transformation), [[#D-018]] (bricks comme notes avancées), [[#D-019]] (Brain isolé), [[#D-021]] (3 agents avec frontières), [[CLAUDE.md#C-018]] (régimes différents).
- **Origine** : Audit 30-04-2026 sur l'absence de formalisation MO + besoin de figer la stack technique avant le portage Twin/MO vers Supabase.

## 5.2 Ontologie des objets et frontières

Décisions qui définissent les frontières conceptuelles des objets canoniques du Twin (créations, scissions, renommages) et les sas d'exploration (sandboxes).

#### D-002 : Scission UO → Organisation + Collectif

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : La BDD `Unités Organisationnelles` mélangeait deux natures d'objets ontologiquement distinctes — entités juridiques instituées et groupements humains opérants. Cette confusion produisait des analyses imprécises (ex. un « département » rangé au même niveau qu'une « SA »).
- **Options envisagées** :
  - Garder UO avec un champ « type » (juridique vs opérant) : simple mais laisse la confusion structurelle.
  - **Scinder en deux BDD distinctes** : plus rigoureux, permet relations et propriétés spécifiques à chaque nature.
  - Créer une hiérarchie de sous-types : trop complexe pour le gain.
- **Décision** : Scinder en deux BDD canoniques :
  - `Organisations` = acteur collectif institué, doté d'une existence juridique/institutionnelle.
  - `Collectifs` = groupe humain opérant, stable ou temporaire, où du travail se coordonne.
- **Conséquences** :
  - ✅ Frontières ontologiques nettes (cf. [[Règles intrinsèques - LBP#R-011]]).
  - ✅ Ouvre la voie à une BDD edge `Relations inter-organisations` ([[#D-006]]) et à des relations propres Organisation→Collectif.
  - ⚠️ Archivage de l'ancienne UO + migration des entrées existantes.
  - ⚠️ Mise à jour des prompts maîtres et logic blocks qui référençaient UO.
- **Articulation** : [[Règles intrinsèques - LBP#R-011]] (frontières fortes), [[#D-006]] (BDD edge dérivée).
- **Origine** : Refonte Twin v2 (Panorama V2 v3).

#### D-003 : Renommage Ressources → Actifs

- **Portée** : Twin + Brain (propagation dans docs)
- **Date de décision** : 22-04-2026
- **Contexte** : Le terme « Ressources » était ambigu — confondu avec « ressources humaines », « ressources financières », ou simple support. Il ne traduisait pas la nature gouvernable et administrable de l'objet.
- **Options envisagées** :
  - Garder « Ressources » + préciser dans la description : ne résout pas l'ambiguïté perçue.
  - **Renommer en « Actifs »** : terme plus précis, aligné sur une notion d'objet mobilisable/gouvernable.
  - Terme plus spécialisé (ex. « Moyens », « Supports ») : moins générique, limitant.
- **Décision** : « Actifs » — objet non humain gouvernable, mobilisable, administrable ou transformable.
- **Conséquences** :
  - ✅ Frontière clarifiée avec Environnements (cadre d'usage) et Sources (artefact de preuve).
  - ✅ Ouvre la voie à des propriétés spécifiques : type, criticité, substituabilité, cycle de vie.
  - ⚠️ Mise à jour de tous les docs référençant « Ressources ».
  - ⚠️ Mise à jour taxonomies, manuels, prompts maîtres, logic blocks.
- **Articulation** : [[Règles intrinsèques - LBP#R-011]] (frontières fortes).
- **Origine** : Refonte Twin v2.

#### D-004 : Renommage Rôles officiels → Postes

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : Avec « Rôles officiels », un individu se retrouvait avec plusieurs rôles rattachés, générant du bruit et de la confusion entre fonction formelle et responsabilités multiples. Le terme « rôle » était aussi flou (officiel vs informel, formel vs opératoire).
- **Options envisagées** :
  - Garder « Rôles officiels » + règle « 1 rôle principal par individu » : laisse la friction terminologique.
  - **Renommer en « Postes »** + règle 1 individu = 1 poste : plus net structurellement.
  - Renommer en « Fonctions » : terme trop lié aux Fonctions de direction/pilotage.
- **Décision** : « Postes » — position formelle contextualisée, indépendante de son titulaire. **Règle associée** : un individu est rattaché à un seul poste (clarté et bruit réduit).
- **Conséquences** :
  - ✅ Charpente formelle du système plus lisible.
  - ✅ Distinction claire avec Individu (personne physique) et Collectif (groupe).
  - ⚠️ Migration des entrées Rôles officiels existantes vers Postes.
  - ⚠️ Si un individu avait plusieurs rôles, arbitrage humain nécessaire pour choisir le poste principal.
- **Articulation** : [[Règles intrinsèques - LBP#R-011]] (frontières fortes).
- **Origine** : Refonte Twin v2.

#### D-005 : Création de la BDD Initiatives organisationnelles

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : Le Twin ne portait pas explicitement les **efforts temporaires structurés** (projets, programmes, pilotes, chantiers). Ces objets finissaient dilués dans Événements, Actions détectées ou Processus — chacun étant une distorsion.
- **Options envisagées** :
  - Utiliser Événements pour les projets : confond repère temporel et effort intentionnel.
  - Utiliser Actions détectées : confond geste ponctuel et effort structuré.
  - **Créer une BDD dédiée** : porte correctement la nature « mouvement/transformation ».
- **Décision** : BDD `Initiatives organisationnelles` = effort intentionnel, temporaire et délimité, avec portage, sponsoring, jalons, état d'avancement, statuts temporels.
- **Conséquences** :
  - ✅ Chaîne de transformation `OKR → Initiatives` explicite (cf. Panorama §10.12).
  - ✅ Lecture de la transformation vivante du système (qui porte quoi, avec quels jalons).
  - ✅ Nouvelle famille architecturale « Mouvement / transformation ».
  - ⚠️ Risque de confusion avec Événements (repère temporel) et Pratiques (récurrent) — à gérer via [[Règles intrinsèques - LBP#R-011]].
- **Articulation** : [[Règles intrinsèques - LBP#R-011]].
- **Origine** : Refonte Twin v2.

#### D-006 : Création de la BDD edge Relations inter-organisations

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : Avec la scission UO → Organisation + Collectif ([[#D-002]]), les relations structurantes entre organisations (coopération, fourniture, dépendance, régulation, co-développement, fusion) nécessitaient un porteur dédié.
- **Options envisagées** :
  - Stocker les relations comme propriétés relations Notion sur Organisations : perd la richesse (nature, statut, ancienneté, réciprocité, événements associés).
  - **Créer une BDD « edge » dédiée** : le lien devient un objet first-class avec ses propres propriétés.
- **Décision** : BDD `Relations inter-organisations` = lien structurant directionnel entre deux organisations, porte la nature, le statut, l'ancienneté, la réciprocité.
- **Conséquences** :
  - ✅ Cartographie de l'écosystème relationnel externe exploitable.
  - ✅ Profils 5D d'exposition/dépendance externe possibles.
  - ⚠️ Seule BDD « edge » du Twin — singularité à documenter clairement.
- **Articulation** : [[Règles intrinsèques - LBP#R-011]], [[Règles intrinsèques - LBP#R-013]] (sobriété relationnelle), [[#D-002]] (scission antécédente).
- **Origine** : Refonte Twin v2 (suite à [[#D-002]]).

#### D-007 : Création de 6 sandboxes spécialisées

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : Les consolidations précoces polluaient le graphe officiel. Il manquait des sas d'exploration pour tester hypothèses et formulations sans engager la couche officielle.
- **Options envisagées** :
  - Utiliser le statut `Brouillon` dans les BDD officielles : reste visible dans le graphe officiel, nuisible.
  - Une sandbox unique multi-objets : moins rigoureux, frontière confuse.
  - **6 sandboxes spécialisées**, chacune avec BDD officielle cible précise : propre.
- **Décision** : 6 sandboxes spécialisées :
  - `Capacités métier candidates (sandbox)` → `Capacités organisationnelles`
  - `OKR (sandbox)` → `OKR`
  - `Pratiques organisationnelles (sandbox)` → `Pratiques organisationnelles`
  - `Principes organisationnels (sandbox)` → `Principes organisationnels`
  - `Problématiques (sandbox)` → `Problématiques`
  - `Processus candidats (sandbox)` → `Processus candidats`
- **Conséquences** :
  - ✅ Graphe officiel propre (hygiène).
  - ✅ Pré-consolidation réversible possible.
  - ✅ Doctrine de promotion explicite (cf. [[Règles intrinsèques - LBP#R-022]]).
  - ⚠️ Règle absolue : pas de relations réelles sauf vers `Sources d'informations` ([[Règles intrinsèques - LBP#R-014]]).
  - ⚠️ Attention à ne pas laisser les sandboxes devenir des BDD parallèles durables.
- **Articulation** : [[Règles intrinsèques - LBP#R-014]], [[Règles intrinsèques - LBP#R-021]], [[Règles intrinsèques - LBP#R-022]].
- **Origine** : Refonte Twin v2.

## 5.3 Architecture transverse et lecture analytique

Décisions qui structurent l'architecture transverse du Twin (tableau maître, chaînes de transformation, prismes UX, articulation des agents) et la lecture analytique de l'écosystème.

#### D-008 : Tableau maître canonique à 29 BDD

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : L'architecture du Twin avait évolué sans carte unique à jour. Il manquait un référentiel obligatoire auquel arbitrer toute création/modification/archivage de BDD.
- **Options envisagées** :
  - Tenir une carte informelle (wiki, doc hors refs) : non versionnée, dérive possible.
  - Faire du Panorama la carte canonique : trop doctrinal pour être consulté comme référence rapide.
  - **Créer un SPECS_ARCHITECTURE_TWIN dédié**, aligné sur SPECS_ARCHITECTURE_BRAIN : symétrie et scalabilité.
- **Décision** : 29 BDD canoniques dans le Twin :
  - 1 satellite de traçabilité (`Sources d'informations`)
  - 1 socle sémantique (`Glossaire spécifique entreprise`)
  - 3 extraction factuelle (`Journal des signaux`, `Actions détectées`, `Enjeux`)
  - 8 socle structurel (`Organisations`, `Relations inter-organisations`, `Collectifs`, `Individus`, `Postes`, `Actifs`, `Environnements`, `Événements`)
  - 1 mouvement/transformation (`Initiatives organisationnelles`)
  - 1 pivot de qualification (`Processus candidats`)
  - 8 couche analytique officielle (`Processus`, `Pratiques organisationnelles`, `Principes organisationnels`, `Capacités organisationnelles`, `Problématiques`, `OKR`, `Indicateurs`, `Modulateurs`)
  - 6 sandboxes spécialisées
- **Conséquences** :
  - ✅ Référence unique pour la gouvernance.
  - ✅ Création de `[[Architecture - Twin]]` qui reproduit le tableau.
  - ⚠️ Discipline obligatoire : toute modification de l'archi doit être arbitrée à partir de la carte ([[Règles intrinsèques - LBP#R-025]]).
- **Articulation** : [[Règles intrinsèques - LBP#R-025]].
- **Origine** : Refonte Twin v2.

#### D-009 : Chaînes de transformation de la connaissance comme paradigme de lecture

- **Portée** : Twin
- **Date de décision** : 22-04-2026
- **Contexte** : Le Twin était lu « table par table » ce qui masquait sa vraie valeur : la transformation progressive de la connaissance (preuve → qualification → consolidation → lecture → pilotage → action).
- **Options envisagées** :
  - Lecture par BDD isolées : simple mais occulte la chaîne de valeur.
  - Lecture par traversées : plus riche mais non guidée.
  - **Lecture par chaînes de transformation** : explicite le passage entre régimes de connaissance.
- **Décision** : Adopter les **chaînes de transformation** comme paradigme de lecture principal. Exemples clés :
  - `Sources → objets documentés` (auditabilité)
  - `Journal des signaux → Enjeux → Problématiques → OKR → Indicateurs` (chaîne diagnostic → pilotage)
  - `Actions détectées → Processus candidats → Processus` (passage brut → structuré)
  - `Actions détectées → Pratiques organisationnelles` (geste → pattern)
  - `Pratiques → Capacités` (pattern → aptitude durable)
  - `Principes → Pratiques` (norme → incarnation, cœur de la lecture 3P)
  - `Modulateurs ↔ Pratiques ↔ Capacités` (conditions d'effectivité)
  - `sandbox → Sources d'informations → indices → BDD officielle cible` (promotion)
- **Conséquences** :
  - ✅ Twin pensé comme machine de lecture systémique, pas entrepôt.
  - ✅ Séparation des 4 régimes de connaissance renforcée ([[Règles intrinsèques - LBP#R-012]]).
  - ✅ Chaînes exploratoires documentées (via sandboxes).
  - ⚠️ Les prompts maîtres et logic blocks doivent refléter ces chaînes.
- **Articulation** : [[Règles intrinsèques - LBP#R-012]], [[Règles intrinsèques - LBP#R-021]], [[Règles intrinsèques - LBP#R-022]], [[Règles intrinsèques - LBP#R-024]].
- **Origine** : Refonte Twin v2.

#### D-017 : Familles UI/UX comme prisme transverse de classification des BDD Twin

- **Portée** : Twin (et propagation app LBP)
- **Date de décision** : 27-04-2026
- **Contexte** : Les BDD du Twin disposent de plusieurs prismes de classification techniques (`architecture_family`, `knowledge_regime`, `officiality_regime`). Ces prismes sont utiles pour la gouvernance interne mais **opaques pour l'utilisateur final** de l'app LBP. Besoin d'un prisme **orienté utilisateur**.
- **Options envisagées** :
  1. Réutiliser un prisme existant comme `architecture_family` côté UI → rejeté (trop technique).
  2. **Créer un prisme dédié `ui_family` orthogonal** → retenu.
  3. Mapping ad hoc dans le code app sans formalisation Brain → rejeté (risque de divergence).
- **Décision** : Adopter une classification dédiée `ui_family` en **7 valeurs** :
  - **Langage** — *Les mots, termes métier, acronymes et définitions propres à l'organisation* (1 BDD)
  - **Structure** — *Qui existe, qui porte quoi* (5 BDD)
  - **Cadres** — *Les cadres, supports, objets et situations qui conditionnent l'action* (3 BDD)
  - **Moteur** — *Ce qui met l'organisation en mouvement* (5 BDD)
  - **Pilotage** — *Les sujets à traiter, objectifs, mesures, trajectoire* (5 BDD)
  - **Ancrages** — *Ce qui oriente, soutient, amplifie ou freine durablement l'action* (3 BDD)
  - **Objets candidats** — *Objets organisationnels saisis directement quand la source les exprime explicitement* (6 BDD sandbox)
- **Note typographique** : `Objets candidats` est intentionnellement en **2 mots** (les 6 autres en 1 mot). Dissonance assumée signalant que cette famille n'est pas un prisme de l'entreprise comme les autres, mais un statut d'objet (en cours de qualification).
- **Conséquences** :
  - ✅ Cohérence app ↔ Brain : la classification utilisée par l'app LBP est documentée dans le Brain.
  - ✅ Prisme **complémentaire** (non substitutif) aux autres : `architecture_family`, `knowledge_regime`, `officiality_regime` restent inchangés.
  - ⚠ Charge de propagation : chaque manuel Twin doit recevoir un champ frontmatter `ui_family` (28 manuels à enrichir).
  - ⚠ Charge Notion : la BDD `Manuels de BDD` doit recevoir une propriété `Famille UI` (select) avec les 7 valeurs.
- **Articulation** : [[Règles intrinsèques - LBP#R-049]] (déclaration obligatoire `ui_family`).
- **Origine** : Phase 6.5 (préparation app LBP côté UX).

#### D-018 : Bricks de connaissance comme Notes avancées des objets Twin

- **Portée** : Twin + écosystème Bricks
- **Date de décision** : 27-04-2026
- **Contexte** : Les fiches structurées du Twin (propriétés natives + relations + 5D) donnent une vue **quasi-tabulaire**. Mais certains objets méritent une **profondeur narrative** : profil organisationnel, profil d'individu, carte causale d'une problématique, dossier complet d'un actif critique. Cette profondeur ne peut pas être portée par les propriétés structurées sans casser la lisibilité.
- **Options envisagées** :
  1. Ajouter des champs texte longs dans la fiche → rejeté (alourdit, pas de format imposé).
  2. Créer un nouvel objet « Note avancée » comme BDD séparée → rejeté (doublon avec Bricks).
  3. **Réutiliser les Bricks** comme support des Notes avancées et lier la fiche Twin via une URL → retenu.
- **Décision** : Une **Note avancée** d'un objet Twin = un **Brick de connaissance** instancié depuis un Template de Brick approprié. La fiche Twin contient une propriété URL `Lien vers la note avancée` ([[Règles intrinsèques - LBP#R-050]]) qui pointe vers ce Brick.
- **Conséquences** :
  - ✅ Cohérence avec l'écosystème Bricks existant.
  - ✅ Profondeur narrative découplée de la fiche structurée (lisibilité préservée).
  - ✅ Réutilisation des Templates de Bricks pour homogénéiser les Notes avancées.
  - ⚠ Restriction : Notes avancées **uniquement pour des objets stabilisés** (cf. [[Règles intrinsèques - LBP#R-050]] — exclusion sandbox, candidats, signaux, actions, indicateurs).
- **Articulation** : [[Règles intrinsèques - LBP#R-050]] (déclaration de la propriété), [[Règles intrinsèques - LBP#R-047]] (position dans l'ordering).
- **Origine** : Phase 6.5 (besoin de profondeur narrative sur objets Twin stabilisés).

#### D-021 : Architecture des 3 agents LBP — Brain architect / Twin architect / KONTEXT

- **Portée** : Transverse écosystème LBP (Brain + Twin + Mission Ops)
- **Date de décision** : 28-04-2026
- **Contexte** : LBP a besoin d'une architecture d'agents claire pour distinguer (a) qui fait évoluer le Brain (méta-LBP, hors mission), (b) qui modélise/met à jour le Twin d'un client, (c) qui pilote l'exécution d'une mission côté consultant utilisateur. Sans frontières d'isolation explicites, risque que des opérations de mission contaminent le Brain.
- **Options envisagées** :
  1. Un seul agent généraliste qui fait tout → rejeté (pas de séparation des responsabilités).
  2. Deux agents (Brain architect + agent mission unique) → rejeté (confond modélisation Twin et pilotage mission).
  3. **Trois agents avec frontières d'isolation explicites** → retenu.
- **Décision** :
  1. **Brain architect** : opérations d'évolution sur le Brain. Agent méta-LBP — il fait évoluer l'écosystème documentaire.
  2. **Twin architect** : opérations sur le Twin d'un client (peuplement, refactor, dédoublonnage, complétion).
  3. **KONTEXT** (nom provisoire) : agent central côté consultant utilisateur. Gère les Mission Ops.
- **Frontière d'isolation infranchissable** : KONTEXT **ne peut pas** appeler Brain architect. Pendant une prestation, le Brain est **utilisé** mais **n'évolue pas**. L'évolution du Brain est une activité méta-LBP, pas de mission.
- **Délégations autorisées** :
  - KONTEXT → Twin architect : ✅ (mise à jour du Twin client = activité de mission légitime).
  - KONTEXT → Brain architect : ❌ (interdit).
  - Twin architect → Brain architect : à arbitrer ultérieurement (probable interdit).
- **Conséquences** :
  - ✅ Stabilité du Brain pendant les missions.
  - ✅ Séparation claire des responsabilités.
  - ✅ 3 agents = 3 fiches dans la BDD `Agents LBP`.
  - ⚠ Le nom `KONTEXT` est provisoire — à arbitrer avant publication finale.
  - ⚠ Cette doctrine bloque toute évolution du Brain en cours de mission. Tout besoin d'évolution → flagger comme remontée à traiter par Brain architect hors mission.
- **Articulation** : [[#D-019]] (isolation Brain ↔ Twin/MO antécédente), à venir : R-XXX sur frontières d'isolation des agents.
- **Origine** : Audit organisation Prompts + Logic blocks.

## 5.4 Conventions de docs et lifecycle documentaire

Décisions sur l'organisation de l'arborescence vault, les conventions de naming des filenames, l'archivage, le format des docs WR-RD et la différenciation Twin/MO des frontmatters.

#### D-010 : Arborescence cible d'Architecture data (v2)

- **Portée** : Transverse (Brain + Twin)
- **Date de décision** : 24-04-2026
- **Contexte** : La refonte Twin v2 produit ~200 nouveaux docs. Il faut définir une arborescence cible évolutive avant migration vers le vault Architecture data, pour obtenir des URLs Drive stables avant indexation Notion.
- **Options envisagées** :
  - Indexer Notion d'abord puis ranger : double passe Notion (indexation sans URL, puis ajout URL).
  - **Ranger d'abord puis indexer en une seule passe** : URLs Drive disponibles dès l'indexation.
  - Structure détaillée par famille architecturale : trop lourde pour 28 BDD.
  - Structure minimale (juste zone d'archives par dossier) : lisible, évolutive.
- **Décision** :
  - Séquence en 4 étapes : (0) clarifier statut Notion, (1) définir arborescence, (2) appliquer arborescence + archiver anciens, (3) indexer Notion en une passe.
  - Arborescence avec sous-dossiers par grand domaine + `archives/` local par dossier thématique.
  - Archivage **local par dossier thématique** (pas de grenier global).
- **Conséquences** :
  - ✅ URLs Drive disponibles dès la migration, indexation Notion en une passe.
  - ✅ Sandboxes visuellement séparées des BDD officielles.
  - ✅ Git garde l'historique complet des déplacements.
  - ⚠️ Application en 2 temps : d'abord dossier temporaire, puis migration vers vault.
- **Articulation** : [[Règles intrinsèques - LBP#R-014]] (sandboxes), [[Règles intrinsèques - LBP#R-025]] (tableau maître), [[Règles intrinsèques - LBP#R-026]] (archivage local), [[Règles intrinsèques - LBP#R-027]] (nommage).
- **Origine** : Phase préparation migration Twin v2.

#### D-011 : Conventions de nommage des fichiers Brain/Twin

- **Portée** : Transverse
- **Date de décision** : 24-04-2026
- **Contexte** : Les anciens fichiers utilisaient différentes conventions (casse CAPITALES, tirets simples). Les nouveaux docs générés arrivaient avec tiret cadratin `—`. Il faut trancher pour éviter les disparités dans le vault.
- **Options envisagées** :
  - Tiret cadratin `—` (nouveaux) : élégant typographiquement, compliqué à taper.
  - **Tiret simple `-`** (anciens) : standard clavier, lisible.
  - Underscore `_` : plus technique, moins convivial pour Obsidian.
- **Décision** :
  - **Séparateur** : tiret simple `-`.
  - **Casse** : Title Case pour les manuels (`Manuel de BDD - Actifs.md`), minuscule pour les notes de concept (legacy ; sera révisé en `Concept - X.md` Title Case en Phase 6), code taxonomie pour les taxonomies (`ACT.IMPACT_DOMAIN.md`).
  - **Uniformisation rétroactive** : à faire au moment de la migration.
- **Conséquences** :
  - ✅ Compatibilité clavier et interopérabilité avec tout outil.
  - ✅ Homogénéité visuelle dans Obsidian.
  - ⚠️ Les 28 nouveaux manuels Twin v2 ont été renommés (tiret cadratin → tiret simple) dans le dossier temporaire le 24-04-2026.
- **Articulation** : [[Règles intrinsèques - LBP#R-027]] (conventions de nommage), [[Règles intrinsèques - LBP#R-061]] (tirets simples — règle dérivée).
- **Origine** : Phase préparation migration Twin v2.

#### D-014 : Colocalisation des docs WR-RD avec leurs manuels de BDD parents

- **Portée** : Brain — organisation du vault Architecture data
- **Date de décision** : 26-04-2026
- **Contexte** : Les docs WR-RD étaient stockés dans un dossier global `Architecture data/Clefs de lectures/` à la racine du vault. Cette localisation détachait les WR-RD de leurs manuels parents, créait une asymétrie avec la nouvelle architecture par groupe (`Manuels de BDD/{Brain, Digital Twin, Mission Ops}/`).
- **Options envisagées** :
  - Conserver le dossier global `Clefs de lectures/` mais y créer une sous-structure par groupe : préserve le repère mais perpétue la séparation manuel/WR-RD.
  - **Colocaliser** chaque WR-RD avec ses manuels parents dans un sous-dossier `WR-RD/` au sein de chaque dossier de groupe.
- **Décision** :
  - Création d'un sous-dossier `WR-RD/` dans chaque groupe.
  - Chaque WR-RD a un `00 - archives/` pour ses propres anciennes versions.
  - Suppression du dossier `Clefs de lectures/` de la racine après migration.
- **Conséquences** :
  - ✅ Proximité topologique entre un manuel et ses docs WR-RD.
  - ✅ Symétrie complète : chaque groupe BDD a son `WR-RD/` + son `00 - archives/`.
  - ✅ Aucun WR-RD obsolète n'est laissé en zone active.
  - ⚠ Naming « WR-RD » non finalisé à cette date — reconfirmé par [[#D-016]].
- **Articulation** : [[#D-010]] (arborescence vault antécédente), [[#D-016]] (rôle WR-RD subséquent).
- **Origine** : Refonte arborescence post-Phase 5.

#### D-015 : Convention de nommage `00 - archives/` pour les dossiers d'archives

- **Portée** : Transverse — organisation visuelle de l'arborescence vault
- **Date de décision** : 26-04-2026
- **Contexte** : Le vault contenait 12 dossiers `archives/` répartis dans toute l'arborescence. En tri alphabétique standard, ces dossiers se mélangeaient avec les sous-dossiers actifs, rendant moins immédiat le repérage de la zone « actuel vs historique ».
- **Décision** : préfixer tous les dossiers d'archives par `00 - ` → renommage `archives/` → `00 - archives/`. Le préfixe `00 - ` garantit que ces dossiers remontent en haut de chaque liste (tri alpha standard) sans confusion possible avec un dossier actif.
- **Conséquences** :
  - ✅ Cohérent avec le pattern `00 - Docs méta/` déjà en racine du vault (préfixe `00 - ` = méta/transverse/historique remonté en haut).
  - ✅ Repérage visuel immédiat de la frontière « actuel vs historique ».
  - ✅ Convention extensible : tout futur dossier d'archives doit suivre ce naming.
- **Règle implicite** : tout nouveau dossier d'archive vault → toujours `00 - archives/`, jamais `archives/`. À formaliser comme règle si besoin.
- **Articulation** : [[Règles intrinsèques - LBP#R-026]] (archivage local par dossier thématique).
- **Origine** : Refonte arborescence post-Phase 5.

#### D-016 : Rôle, contenu et format des docs WR-RD (Write Rules / Read Keys)

- **Portée** : Brain (template d'instanciation) + Twin / Brain / Mission Ops (docs instanciés). Complète [[#D-014]].
- **Date de décision** : 26-04-2026
- **Contexte** : Suite à la refonte Twin v2, il fallait définir la place exacte des docs WR-RD dans l'écosystème agentique LBP, où coexistent : system prompts, prompts maîtres, logic blocks, manuels de BDD, descriptions de propriétés Notion. Le risque était soit de doublonner avec les logic blocks, soit de re-générer une doctrine déjà tenue par le manuel parent.
- **Options envisagées** :
  - **Option A — Statu quo discipliné** : maintenir un WR-RD éditorial avec sa propre doctrine.
  - **Option B — Fusion dans le manuel** : pas de WR-RD, l'agent charge le manuel complet.
  - **Option C — Fusion dans les logic blocks** : chaque logic block embarque les règles WR-RD.
  - **Option D — WR-RD comme projection stricte du manuel parent** : extraction automatique d'un sous-ensemble de colonnes ; aucune doctrine ni contenu propre.
- **Décision** : **Option D** — le WR-RD est une **projection stricte de la section 4 du manuel parent**, sans contenu propre.
  - **Rôle** : doc compact runtime pour les agents qui doivent lire/écrire dans une BDD sans charger le manuel complet.
  - **Frontière nette avec les autres docs** :
    - System Prompt → identité, autorité, garde-fous globaux.
    - Prompt Maître → mission, portée, format de sortie.
    - Logic Block → discernement, heuristiques, faux positifs.
    - **WR-RD (par BDD) → tableau champ-par-champ : format d'écriture + sens de lecture (extraction stricte)**.
    - Manuel de BDD → design conceptuel exhaustif, narratif.
    - Description Notion ≤280 → mini-prompt synthétique inline.
  - **9 colonnes retenues** du manuel parent : Champ, Type, Taxonomie(s), Cardinalité, Forme logique, Instructions d'écriture, Clefs de lecture, Utilité, Exemples.
  - **Naming** : fichier `WR-RD - [Nom de la BDD].md` ; code `WRRD_[NOM_TOKEN]`.
  - **Pas de section maintenance, ni doctrine, ni historique de version** dans le doc instancié.
- **Conséquences** :
  - ✅ Aucun risque de doublon avec logic blocks ni avec le manuel.
  - ✅ Source de vérité unique : la section 4 du manuel parent.
  - ✅ Doc compact, chargeable runtime par les agents.
  - ✅ Extension future possible : générateur automatique manuel → WR-RD.
  - ⚠ Toute évolution du WR-RD doit passer par une évolution du manuel parent puis re-projection.
- **Articulation** : [[Règles intrinsèques - LBP#R-041]] (cascade Manuel → WR-RD — sera migrée en PROP-001), [[Règles intrinsèques - LBP#R-042]] (QA stricte d'égalité — sera migrée en PROP-001), [[#D-014]] (colocalisation antécédente).
- **Origine** : Phase 5 (génération WR-RD post-refonte Twin v2).

#### D-022 : Différenciation assumée des frontmatters Twin et Mission Ops

- **Portée** : Architecture documentaire — Manuels de BDD Twin et Mission Ops
- **Date de décision** : 30-04-2026
- **Contexte** : Backlog 27-04-2026 a remonté une **divergence des frontmatters** entre les manuels Twin et Mission Ops. Le Twin embarque `ui_family`, `officiality_regime`, `has_advanced_note`, `aliases` ; Mission Ops ne les embarque pas. Pas d'arbitrage formel jusqu'ici → asymétrie silencieuse entre templates.
- **Options envisagées** :
  1. **Harmoniser** : ajouter les 4 champs aussi côté MO pour un audit transverse unifié.
  2. **Différencier explicitement** : assumer que Twin et MO ont des régimes de connaissance différents et que ces champs n'ont pas de sens en MO → retenu.
  3. **Laisser flou** : le statu quo, sans formalisation → rejeté.
- **Décision** : **Différenciation assumée**. Twin et MO sont deux domaines aux régimes de connaissance distincts :
  - Twin = **ontologique** (taxonomies, dimensions 5D, relations sémantiques). Les champs Twin spécifiques reflètent cette nature.
  - Mission Ops = **opérationnel** (workflows de mission, livrables, traçabilité). Les champs Twin n'ont pas de pertinence en MO : pas de famille UI à classer, pas de régime officiel/sandbox, pas de notes avancées (les bricks **sont** les fiches MO), pas d'aliases.
  → Conséquence : le frontmatter MO est plus mince, par design, et c'est correct.
- **Conséquences** :
  - ✅ Pas de champ vide systématique côté MO.
  - ✅ Audit transverse à scope-aware : les R-XXX et WF-XXX qui parlent du frontmatter doivent désormais préciser le scope (Brain / Twin / MO).
  - ⚠ Si un nouveau champ doit être commun (ex. `code`, `version`, `created_at`, `updated_at`), il doit être présent **dans les deux** frontmatters et formalisé en R-XXX transverse.
- **Articulation** : [[Règles intrinsèques - LBP#R-054]] (codification), [[Règles intrinsèques - LBP#R-055]] (frontmatter en 3 zones balisées Brain), [[Règles intrinsèques - LBP#R-056]] (versioning X.Y), [[CLAUDE.md#C-008]] (séparation des scopes en `refs/`), [[#D-023]] (justifié par stack technique différenciée).
- **Origine** : Backlog 27-04-2026 (divergence templates Twin/MO).

## 5.5 Codification, templates et migrations docs méta

Décisions sur la traçabilité des templates d'instanciation, la séquence de migration Twin v2, la propagation de la version du template, et la refonte Phase 1.0 de la codification des docs méta (préfixe META_, fonctions systémiques, BDD Templates Brain séparée).

#### D-012 : Séquence de migration Twin v2 vers Architecture data (7 phases)

- **Portée** : Transverse (Brain + Twin + Mission Ops)
- **Date de décision** : 24-04-2026
- **Contexte** : Après validation de l'arborescence cible ([[#D-010]]) et des conventions de nommage ([[#D-011]]), il fallait séquencer la migration de ~200 nouveaux docs + archivage de leurs v1 + refonte ciblée de l'arborescence existante. Objectif : avoir vault et Drive alignés AVANT l'indexation Notion (une seule passe avec URLs).
- **Options envisagées** :
  - Migration tout-en-un : risqué, pas de point de contrôle intermédiaire.
  - Par couche d'artefacts : OK mais mélange refonte arborescence et migration.
  - **Par phases avec refonte en amont** : plus rigoureux, chaque phase vérifiable.
- **Décision** : Séquence en 7 phases, refonte arborescence d'abord :
  1. Refondre l'arborescence d'Architecture data.
  2. Archiver les anciens docs v1.
  3. Migrer les nouveaux docs depuis dossier temporaire.
  4. Synchronisation Drive + vérification URLs.
  5. Indexation Notion (archivage des anciennes entrées + indexation des nouveaux avec URLs).
  6. Mise à jour des clefs de lecture (templatiser puis dérivés).
  7. Chantier Prompts + Logic blocks (séparé).
- **Conséquences** :
  - ✅ Vault propre avant ingestion des nouveaux docs.
  - ✅ Aucune indexation Notion sans URL Drive valide.
  - ✅ Claire séparation entre rangement, gouvernance Notion, dérivés docs, mise à jour de contenu.
- **Articulation** : [[Règles intrinsèques - LBP#R-026]] (archivage local), [[Règles intrinsèques - LBP#R-027]] (nommage), [[Règles intrinsèques - LBP#R-028]] (manuel = source de vérité — sera migrée en PROP-001).
- **Origine** : Phase préparation migration Twin v2.

#### D-013 : Traçabilité de version de template d'instanciation

- **Portée** : Brain (Manuels de BDD ; étendable à Notes concept, Glossaire, Bricks ultérieurement)
- **Date de décision** : 25-04-2026
- **Contexte** : Les templates d'instanciation LBP évoluent. Les manuels générés via d'anciens templates restent valides mais structurellement différents. Sans traçabilité explicite, on ne peut pas distinguer les manuels conformes au standard courant des manuels legacy à migrer.
- **Options envisagées** :
  - Pas de traçabilité : on suppose que tous les manuels suivent le standard courant. Casse dès qu'un template évolue.
  - Tag implicite via `tags` du frontmatter : non structuré, pas filtrable côté Notion.
  - **Champ dédié `template_version`** (frontmatter vault + propriété Notion) : explicite, filtrable, pérennise la traçabilité.
- **Décision** :
  - **Côté template** : ajouter une instruction au bloc `FRONTMATTER_INSTANCE` pour que tout manuel instancié porte un champ `template_version`.
  - **Côté vault** : ajouter `template_version` au frontmatter des manuels lors du batch B.
  - **Côté Notion** : ajouter une propriété `Version du template` à la BDD `Manuels de BDD`.
  - **Convention** : champ vide = manuel legacy (template antérieur ou inconnu).
- **Conséquences** :
  - ✅ Distinction propre entre manuels v2 conformes et manuels legacy.
  - ✅ Capacité à filtrer / piloter les migrations futures de templates.
  - ✅ Pattern réutilisable pour les autres BDD à templates.
  - ⚠️ Il faudra incrémenter `template_version` dans le manuel à chaque montée de version du template.
- **Articulation** : [[Règles intrinsèques - LBP#R-055]] (frontmatter canon), [[Règles intrinsèques - LBP#R-056]] (versioning X.Y), [[#D-020]] (généralisation à toutes les BDDs Brain).
- **Origine** : Évolution template Manuel BDD vers v6.1.0 (standard Twin v2).

#### D-020 : Propagation de la propriété `Version du template` à toutes les BDDs Brain

- **Portée** : 11 BDDs Brain (transverse)
- **Date de décision** : 28-04-2026
- **Contexte** : Aujourd'hui seule la BDD `Manuels de BDD` porte une propriété `Version du template` ([[#D-013]]). Or chaque BDD Brain indexe des docs qui sont eux aussi générés depuis un template. Sans propriété qui trace la lignée de génération, l'audit mécanique des docs stale est impossible.
- **Options envisagées** :
  1. Maintenir la propriété uniquement sur Manuels de BDD → rejeté.
  2. **Étendre à toutes les 11 BDDs Brain** → retenu.
  3. Stocker uniquement dans le frontmatter Markdown sans Notion → rejeté.
- **Décision** : ajouter la propriété `Version du template` sur les **10 BDDs Brain** qui ne la portent pas encore (Docs méta LBP, Glossaire LBP, Registre des notes de concept, Registre des taxonomies, Méthodes LBP, Prompts LBP, Templates de bricks, Agents LBP, Outils externes, Registre des logic blocks).
  - **Type** : `RICH_TEXT` (texte libre), pas `select`. Justification : un select obligerait à créer en permanence de nouvelles options à chaque bump, créant une accumulation illisible. Un texte libre suit la convention [[Règles intrinsèques - LBP#R-056]] (`X.Y`).
- **Conséquences** :
  - ✅ Audit mécanique possible des docs stale lors de bumps majeurs de templates.
  - ✅ Cohérence transverse Brain.
  - ⚠ Charge de propagation : 10 manuels Brain à enrichir + 11 WR-RD à propager.
  - ⚠ Charge de saisie : les ~310 entrées existantes des BDDs Brain devront être progressivement enrichies.
- **Articulation** : [[Règles intrinsèques - LBP#R-055]], [[Règles intrinsèques - LBP#R-056]], [[#D-013]] (décision antécédente).
- **Origine** : Phase A4 (sync DDL Notion).

#### D-024 : Adoption du préfixe `META_` pour les codes des docs méta indexés (remplace `CHRT_`)

- **Portée** : Brain — BDD `Docs méta LBP`
- **Date de décision** : 03-05-2026
- **Contexte** : Le préfixe historique `CHRT_` (« charte ») est cryptique et n'évoque pas la nature « doc méta » (qui peut être bien plus large qu'une charte : panorama, doctrine, spec, règle, workflow, codification, etc.). À l'occasion du chantier d'architecture des docs méta, opportunité de basculer.
- **Options envisagées** :
  - **(A)** Garder `CHRT_` + ajouter un préfixe par fonction systémique : long, redondance avec la propriété `Fonction systémique`.
  - **(B)** Remplacer `CHRT_` par préfixe par fonction (ex. `NRM_RULES_LBP`) : court mais perte du signal « doc méta ».
  - **(C)** Garder `CHRT_` (statu quo) : stable mais cryptique.
  - **(D)** Remplacer `CHRT_` par `META_` : explicite, court, cohérent avec le namespace `META.*`.
- **Décision** : **(D)** Préfixe `META_<TOKEN>_<SCOPE>` pour tous les codes des docs méta indexés. Le scope `_LBP` signale transverse, les scopes `_BRAIN` / `_TWIN` / `_MO` signalent un domaine spécifique.
- **Conséquences** :
  - ✅ Code parlant immédiatement (« si je vois `META_*`, c'est un doc méta »).
  - ✅ Cohérence avec le namespace `META.*` des taxos méta.
  - ✅ Lisibilité humaine et agent améliorée.
  - ⚠️ Coût de migration : ~11 codes existants à renommer en Phase 4.
- **Articulation** : [[Règles intrinsèques - LBP#R-064]] (naming des docs méta — règle dérivée), `[[Constitution des docs méta - LBP]]` (annexe A).
- **Origine** : Phase 1.0 du chantier d'architecture des docs méta.

#### D-025 : Adoption des 5 fonctions systémiques `META.FUNCTION` (remplace `META.FAMILY`)

- **Portée** : Brain — BDD `Docs méta LBP`
- **Date de décision** : 03-05-2026
- **Contexte** : La taxonomie historique `META.FAMILY` (8 valeurs : Naming conventions, Quality QA, Charts, Workflows playbooks, Tooling rules, Template rules, Data model rules, Security privacy) classait les docs méta par **type de contenu**. À l'usage, peu opérant pour le routage agent : un doc méta peut combiner plusieurs types de contenu, mais sa **fonction systémique de gouvernance** est unique.
- **Options envisagées** :
  - **(A)** Garder `META.FAMILY` (8 valeurs) + ajouter `META.FUNCTION` (5 valeurs) : 2 axes coexistent.
  - **(B)** Reconvertir `META.FAMILY` (renommer les 8 taxons → 5 fonctions) : moyen coût, perte de l'axe « type de contenu ».
  - **(C)** Virer `META.FAMILY`, créer `META.FUNCTION`, **typer le doc via la relation au template**. Le type est dérivé de la relation au template, pas dupliqué dans une taxo.
- **Décision** : **(C)**. Création de `META.FUNCTION` (5 valeurs : Orienter, Expliquer, Structurer, Normer, Opérer). Archivage de `META.FAMILY` ([[Règles intrinsèques - LBP#R-053]]). Le type de contenu sera porté par la **relation au template** côté BDD.
- **Conséquences** :
  - ✅ Axe de classification stable, exhaustif, agent-friendly (5 fonctions = 5 boucles de gouvernance).
  - ✅ Cohérence avec l'arborescence cible `00 - Docs méta/` (sous-dossiers numérotés).
  - ✅ Single source of truth pour le type d'un doc méta (= relation au template).
  - ⚠️ Coût migration : ~11 fiches Notion à mettre à jour en Phase 2-3.
  - ⚠️ Note : la fonction « Contrôler » (audit / QA) avait été envisagée comme 6e valeur, mais a été **fusionnée dans Opérer**.
- **Articulation** : [[Règles intrinsèques - LBP#R-049]] (taxos orthogonales), [[Règles intrinsèques - LBP#R-053]] (archivage), `[[Constitution des docs méta - LBP]]` §3.
- **Origine** : Phase 1.0 du chantier d'architecture des docs méta.

#### D-026 : Création de la BDD `Templates Brain` séparée — `Templates de Bricks` reste une BDD distincte

- **Portée** : Brain — BDDs `Docs méta LBP`, `Templates Brain`, `Templates de Bricks`
- **Date de décision** : 03-05-2026
- **Contexte** : Aujourd'hui les **templates d'instanciation** (TPL_NOTE_CONCEPT, TPL_TAXO, TPL_WRRD_BR, TPL_PROMPT, etc.) sont indexés dans la BDD `Docs méta LBP`. C'est un **mal-classement** : un template est un objet **gouverné** (un moule pour instancier d'autres objets), pas un doc de **gouvernance**. À côté, la BDD `Templates de Bricks` existe déjà et concerne les templates utilisés par kontext pour générer les livrables clients.
- **Options envisagées** :
  - **(A)** Garder les templates d'instanciation dans `Docs méta LBP` : simple mais BDD `Docs méta LBP` devient un grenier.
  - **(B)** Créer **1 seule BDD** `Templates Brain` qui regroupe tous les templates : kontext verrait du bruit.
  - **(C)** Créer une BDD `Templates Brain` pour les templates d'instanciation ET garder `Templates de Bricks` séparée : 2 BDDs distinctes par scope agent.
- **Décision** : **(C)**. Justifications :
  - **Scope agent différent** : brain architect produit/maintient les templates d'instanciation Brain ; kontext consomme les templates de bricks.
  - **Régime de vie différent** : les templates de bricks évoluent avec les besoins de livraison client ; les templates d'instanciation Brain évoluent avec la doctrine LBP.
  - **Frontière Brain ↔ Mission** : les templates de bricks sont **dans le Brain** (zone stable) MAIS **consommés par Mission Ops via kontext**.
- **Conséquences** :
  - ✅ `Docs méta LBP` redevient pure (uniquement docs de gouvernance).
  - ✅ Chaque BDD a un consommateur agent clair.
  - ✅ Permet une taxo dédiée `TPL.SCOPE` pour les sous-types de templates Brain.
  - ⚠️ Coût ponctuel : créer manuel `Manuel de BDD - Templates Brain` + WR-RD + générer BDD Notion + migrer ~6 fiches templates + créer taxo `TPL.SCOPE`.
- **Articulation** : [[Règles intrinsèques - LBP#R-012]] (séparation des régimes de connaissance), [[Règles intrinsèques - LBP#R-053]] (archivage si rename de codes), [[CLAUDE.md#C-018]] (régimes différents → BDDs distinctes), `[[Constitution des docs méta - LBP]]` §2.
- **Origine** : Phase 1.0 du chantier d'architecture des docs méta.

---

# 6) Archives — Décisions architecturales - LBP

*Items archivés — décisions révisées par une décision postérieure, abandonnées suite à un changement de contexte, ou dont la portée a disparu. Conservés ici pour traçabilité historique, IDs immuables jamais réutilisés.*

*(Aucun item archivé à ce jour.)*

[[Quand des décisions seront archivées, les déplacer ici depuis §5 en conservant leur ID, leur schéma, et en ajoutant les champs `Archivé` (date + raison) et optionnellement `Remplacée par` (wikilink vers la D-YYY successeur).]]

---

> **Maintenance et évolution de ce catalogue** : voir `[[Méthode - Maintenance d'un catalogue Brain]]`.
