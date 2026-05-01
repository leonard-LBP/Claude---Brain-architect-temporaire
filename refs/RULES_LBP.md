---
# === Identité ===
title: "Règles LBP - Catalogue des règles intrinsèques de l'écosystème"
doc_type: doc_meta
code: "CHRT_RULES_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
created_at: "07-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Catalogue exhaustif des 60 règles atomiques (R-XXX) qui gouvernent l'écosystème LBP (Brain + Digital Twin + Mission Ops). Chaque règle a un ID stable, une portée, un statut, un why, un how to apply, et la date de découverte."
purpose: "Référence canonique pour lookup d'une règle précise. Toute production ou modification structurante doit s'appuyer sur les règles applicables. Pour la narration doctrinale qui les sous-tend voir DOCTRINE_LBP."
tags:
  - doc_meta
  - rules
  - catalogue
  - brain
  - digital_twin
  - mission_ops
  - lbp
---

# Règles de gestion du Brain et du Digital Twin

> Ce fichier recense les règles **intrinsèques à l'écosystème LBP** (Brain + Twin + Mission Ops).
> Les règles contextuelles à notre collaboration (comportement de Claude, outillage) sont dans `CLAUDE.md` (IDs `C-XXX`).
> Chaque règle a un ID stable (`R-XXX`) qui ne change jamais, même si la règle déménage de section.
> Dernière mise à jour : 29-04-2026 - R-060 (hygiène d'écriture des champs `summary` et `purpose` du frontmatter Brain : `summary` = description neutre du quoi, `purpose` = verbe à l'infinitif décrivant la fonction ; lisible humain ET agent, formulation neutre sur le consommateur, anti-patterns « aider un agent à » proscrits). Découverte lors de la rédaction des 10 purpose taxos canoniques de référence (Phase 0a).

---

## Format d'une règle

Chaque règle suit ce format pour homogénéité et lisibilité :

```markdown
### R-XXX : Titre court

- **Portée** : Brain / Twin / Mission Ops / Transverse
- **Statut** : Actif / En discussion / Archivé
- **Why** : Motivation (raison d'être, incident à l'origine)
- **How to apply** : Quand et comment appliquer concrètement
- **Exemples** : ✅ bon usage / ❌ mauvais usage
- **Découverte** : Date + contexte d'émergence
```

---

## Règles d'évolution de ce document (auto-restructuration)

Ces règles sont mes engagements pour maintenir la lisibilité du document à mesure qu'il grossit. Je les applique proactivement et je propose les restructurations - tu arbitres.

- **Stabilité des IDs** : l'ID `R-XXX` est immuable. On ne renumérote jamais, même si la règle déménage de section.
- **Déplacement** : si une règle change de section, on la déplace mais on garde l'ID. On note l'ancienne section dans le champ *Découverte* si utile.
- **Remplacement** : si une règle est supplantée, on marque l'ancienne `Archivé` (sans la supprimer) avec un pointeur vers la nouvelle.
- **Règle de scission** : si une sous-section dépasse ~8 règles, je propose de la scinder en sous-sous-sections thématiques.
- **Règle de promotion (inbox)** : dès que la section *À classer (inbox)* accumule 3+ entrées, je propose de les reclasser.
- **Règle de fusion / conflit** : si deux règles se chevauchent ou se contredisent, je le signale et je propose fusion, fusion partielle, ou révision avec archivage.
- **Housekeeping périodique** : à chaque milestone majeur (fin d'un gros chantier), je propose une revue structurelle du doc (ordre des sections, dénomination, détection de doublons).
- **Cohérence avec le backlog** : quand je promeus une règle du backlog vers ce doc, je laisse une trace dans le backlog (section historique).

---

## Sommaire

- [1. Règles transverses (gouvernance globale)](#1-règles-transverses)
- [2. Règles Brain](#2-règles-brain)
- [3. Règles Digital Twin](#3-règles-digital-twin)
- [4. Règles Mission Ops](#4-règles-mission-ops)
- [5. Règles de propagation d'impacts](#5-règles-de-propagation-dimpacts)
- [6. À classer (inbox)](#6-à-classer-inbox)

---

## 1. Règles transverses

*Règles qui s'appliquent à tout l'écosystème, indépendamment du domaine.*

### 1.1 Source de vérité et gouvernance

#### R-001 : Source de vérité = doc Markdown

- **Portée** : Transverse
- **Statut** : Actif
- **Why** : Éviter la divergence entre le contenu et son index. Le doc est portable, versionable, lisible IA ; Notion peut évoluer sans perte.
- **How to apply** : Pour modifier un objet, on modifie d'abord le doc MD, puis on aligne Notion. Jamais l'inverse.
- **Découverte** : Principe architectural originel.

> Les règles R-003 (confirmation humaine), R-009 (vault unique) et R-010 (git) ont été déplacées vers `CLAUDE.md` (IDs `C-001`, `C-002`, `C-003`) car elles relèvent de notre collaboration plutôt que de l'écosystème lui-même.

### 1.2 Zero contamination

#### R-002 : Zero donnée client dans Core / Motor

- **Portée** : Transverse (frontière Brain / Twin / MissOps)
- **Statut** : Actif
- **Why** : Le Brain est réutilisable entre missions. Contamination = perte de réutilisabilité.
- **How to apply** : Les domaines Core et Motor Brain ne contiennent jamais de données client. Seuls Digital Twin et Mission Ops sont instanciés par mission.
- **Exemples** : ✅ "Capacité Organisationnelle" dans Glossaire LBP / ❌ "Capacité Organisationnelle - Client X" dans Glossaire LBP
- **Découverte** : Principe architectural originel.

### 1.3 Qualité documentaire (QA)

#### R-039 : Aucun artefact de génération IA dans les docs LBP

- **Portée** : Transverse (tous les documents LBP : manuels, notes de concept, glossaire, taxonomies, prompts, méthodes, templates, frontmatters, contenus de fiches Notion, etc.)
- **Statut** : Actif
- **Why** : Les générateurs IA (notamment ChatGPT/o1 avec sources web) laissent parfois des artefacts de citation ou de balisage qui ne devraient jamais apparaître dans le doc final. Ces artefacts cassent la lisibilité, polluent l'extraction sémantique, et trahissent un défaut de relecture avant publication.
- **How to apply** : Avant de finaliser ou publier tout doc LBP (vault, Notion, Drive), faire une **passe QA anti-artefacts** qui détecte et supprime au minimum :
  - `:contentReference[oaicite:N]{index=N}` (citation OpenAI/Bing brute)
  - `【N†source】` ou `[N†source]` (citations OpenAI tournée)
  - `[citation:N]`, `[ref:N]`, `[1]`, `[2]`... isolés sans bibliographie
  - `<sup>N</sup>` orphelins
  - Caractères de remplacement Unicode (`�`, `\ufffd`)
  - Balises markdown brisées (`**...` ou `[...](` non fermés)
  - Fragments de placeholders non résolus (`[[NOM_OBJET]]`, `<INSTR>...</INSTR>`)
  - Texte tronqué visible (phrases coupées en milieu, comme "décin collective" au lieu de "décisions et de la performance collective")
- **Exemples détectés** :
  - ❌ Note vault `concept - Repères communs.md` : `Ils peuvent être symboliques [...] fonctionnels:contentReference[oaicite:5]{index=5}iguïtés en rendant visibles des attentes communes.` (artefact de citation + texte tronqué) - corrigé manuellement à l'indexation Notion (batch C, 25-04-2026)
  - ❌ Note vault `concept - Soft skill.md` : `qualité des interactions, des décin collective.` (texte tronqué)
- **Outillage suggéré** : grep de motifs avant publication, ou contrôle automatique dans pipeline d'indexation.
- **Conséquence si violation** : doc à corriger en source (vault) ET en cible (Notion) ; relire systématiquement la sortie de tout générateur IA avant intégration.
- **Découverte** : 25-04-2026, Leonard, après détection en batch C de 2 occurrences sur 72 notes de concept.

#### R-044 : Format de date `JJ-MM-YYYY` (transverse LBP)

- **Portée** : Transverse à tout l'écosystème LBP (Brain, Twin, Mission Ops, refs/, templates, scripts, frontmatters Obsidian, propriétés Notion textuelles, Logs/Révisions, exemples de contenu).
- **Statut** : Actif
- **Why** : Cohérence visuelle francophone, lisibilité immédiate, alignement avec les conventions de l'écosystème LBP. Le séparateur `-` (dash ASCII) est préféré au `/` pour éviter les cassures de chemin et l'abus de barres obliques (déjà chargées de sens dans les paths, urls, taxonomies).
- **How to apply** : Toutes les dates affichées ou stockées en clair s'écrivent `JJ-MM-YYYY` (ex. `26-04-2026`). S'applique à : `created_at`, `updated_at`, `version_date` dans les frontmatters ; dates dans Logs/Révisions ; dates dans champs texte ; exemples de contenu dans manuels/WR-RD/templates.
- **Exception** : si une propriété Notion est typée `Date` natif, on conserve le type natif (le rendu est géré par Notion et localisé). Ne concerne donc que les **dates en texte clair**.
- **Migration** : règle appliquée going forward ; un sweep transverse des dates ISO `YYYY-MM-DD` héritées (notamment dans Logs/Révisions des manuels et `ECOSYSTEM-STATE.md`) est planifié ultérieurement, hors scope immédiat.
- **Exemples** :
  - ✅ `created_at: "26-04-2026"` (frontmatter manuel ou WR-RD)
  - ✅ `| 26-04-2026 | Création du doc | v0.1.0 |` (ligne de log)
  - ❌ `created_at: "2026-04-26"` (format ISO interdit en texte clair)
  - ❌ `created_at: "26/04/2026"` (slash interdit)
- **Découverte** : 26-04-2026, Leonard, lors de la finalisation des 28 WR-RD Twin v2 ; choix du dash ASCII pour éviter cassures et abus de `/`.

#### R-052 : Apostrophe typographique uniforme (U+2019) dans les noms

- **Portée** : Transverse à tout l'écosystème LBP - tous les noms de propriété, de BDD, de vue, et tout texte affiché aux utilisateurs (vault Obsidian, BDDs Notion, manuels, WR-RD, templates, taxonomies, frontmatters textuels). Concerne aussi bien le scope LBP que le scope Session.
- **Statut** : Actif
- **Why** : Unicode définit deux apostrophes visuellement quasi identiques mais incompatibles pour le matching strict - l'apostrophe ASCII droite `'` (U+0027) et l'apostrophe typographique courbe `’` (U+2019). Sur Notion, créer une colonne `"Statut de l'objet"` (ASCII) et `"Statut de l'objet"` (typo) crée **deux propriétés distinctes** sans alerte ; idem côté manuels où une recherche/un diff strict produit des faux négatifs. C'est un trou de symétrie silencieux qui contamine l'audit Manuel ↔ Notion ↔ WR-RD.
- **How to apply** : Tous les noms de propriété, de BDD, de vue, et tout texte affiché utilisent l'apostrophe typographique `’` (U+2019). L'apostrophe ASCII `'` (U+0027) est strictement réservée au code (scripts Python, JSON, DDL SQL, regex) et ne doit **jamais** apparaître dans un nom affiché. En pratique :
  - Obsidian (autocorrect actif par défaut) : la conversion est automatique, RAS.
  - Notion : vérifier visuellement à chaque création de propriété, ou normaliser via `RENAME COLUMN` après création par DDL si le code source contenait un `'` ASCII.
  - Scripts Python générant du DDL : préférer `'’'` ou `’` littéral dans les chaînes destinées à Notion.
  - Outils de diff/audit : normaliser Unicode-insensible (déjà appliqué dans `parse_manuel.py` et `diff_manuel_notion.py` via `s.replace("’", "'").lower()`).
- **Exemples** :
  - ✅ `Statut de l'objet`, `Critère observable d'existence`, `Source(s) d'information (texte)`
  - ❌ `Statut de l'objet`, `Source(s) d'information (texte)` (ASCII U+0027 dans un nom affiché)
- **Conséquence si violation** : faux négatifs en audit (props non détectées comme dupliquées), divergence silencieuse Manuel ↔ Notion, retrievers / agents ne matchent pas le nom attendu.
- **Découverte** : 27-04-2026, Leonard, après création par DDL de `Source(s) d'information (texte)` sur la BDD Capacités métier candidates sandbox avec apostrophe ASCII alors que le reste du schéma utilisait la typographique. Renommage immédiat puis formalisation de la règle.

#### R-053 : Convention de renaming des docs archivés (suffix dans filename)

- **Portée** : Transverse à tout le vault `Architecture data/` - manuels de BDD, WR-RD, taxonomies, notes de concept, templates, méthodes, prompts, logic blocks, chartes, playbooks, et tout doc Markdown susceptible d'être archivé.
- **Statut** : Actif
- **Why** : Le statut actif/archivé d'un doc dépendait jusqu'ici uniquement de son **dossier** (`00 - archives/`). Risque concret : un agent (ou un humain) qui recherche par nom (`Glob "**/Manuel de BDD - Actifs.md"`, search Obsidian/Drive) tombe sur 1 actif + N archivés homonymes et peut confondre / citer une version archivée comme source vérifiée. C'est un trou de discoverability silencieux qui peut générer des erreurs.
- **How to apply** :
  - **Format de renaming** : `<nom canonique> (archivé v<X> le JJ-MM-YYYY).md` si la version est connue, sinon `<nom canonique> (archivé le JJ-MM-YYYY).md`. Le format de version `<X>` suit **R-056** (grammaire `MAJOR.MINOR`).
  - **3 actions atomiques** lors de l'archivage :
    1. **Filename** : ajouter le suffix `(archivé [v<X> le ]JJ-MM-YYYY)` avant l'extension
    2. **`title` frontmatter** : aligner sur le filename (R-043, cohérence filename ↔ title)
    3. **Déplacement** : vers `00 - archives/` du dossier parent (pratique existante, double signal conservé)
  - **Date** : format JJ-MM-YYYY (R-044), date réelle d'archivage du jour
  - **Version** : extraite du frontmatter `version:` quand présente (semver `1.0.0` → `v1.0.0` dans le suffix), omise sinon
- **Exemples** :
  - ✅ `Manuel de BDD - Actifs (archivé v1.0.0 le 26-04-2026).md` (version connue)
  - ✅ `concept - Soft skill (archivé le 26-04-2026).md` (version absente)
  - ✅ `OBJ.STATUT.LBP (archivé le 26-04-2026).md`
  - ❌ `Manuel de BDD - Actifs.md` dans `00 - archives/` (filename non renommé - état pré-R-053)
- **Edge cases** :
  - Doc archivé plusieurs fois (v1 puis v2) : 2 fichiers cohabitent sans collision (`...(archivé v1.0.0 le X).md` + `...(archivé v2.0.0 le Y).md`)
  - Doc sans frontmatter : renommer filename uniquement, pas d'alignement title
  - Doc avec nom déjà ambigu (`Sans titre.md`) : flag manuel, ne pas auto-renommer
- **Regex de validation** : `\(archivé( v\d+\.\d+)? le (\d{2}-\d{2}-\d{4})\)\.md$` (post R-056 : version au format `MAJOR.MINOR`)
- **Date forfaitaire pour rétroactif** : `26-04-2026` (date du sweep d'archivage massif Phase 1-4 documenté dans `ECOSYSTEM-STATE.md`).
- **Conséquence si violation** : confusion de search, citation d'archives obsolètes comme sources vérifiées, erreurs silencieuses dans les pipelines IA qui consomment le vault.
- **Découverte** : 28-04-2026, Leonard, en préparant le chantier d'indexation Brain. Formalisation immédiate avant migration des 212 fichiers déjà archivés.

#### R-054 : Codification universelle des objets Brain

- **Portée** : Transverse à tout l'écosystème Brain - manuels de BDD, WR-RD, taxonomies, notes de concept, templates, prompts, logic blocks, méthodes, docs méta, agents, outils externes, entries de glossaire. Phase 2 prévue pour Twin / Mission Ops (instances de mission).
- **Statut** : Actif
- **Why** : Aujourd'hui les codes coexistent en 6+ conventions différentes (`DBMAN_X`, `CPT.X.LBP.Y`, `OBJ.STATUT.LBP`, `TPL_BRICK_X`, `METH_X`, etc.) avec mix de séparateurs (`_`, `.`, `-`) et suffix `LBP` parfois présent, parfois absent. Beaucoup de docs n'ont aucun code. Sans grammaire unifiée, les agents de maintenance et d'exploitation ne peuvent ni filtrer fiable par regex ni vérifier l'unicité cross-écosystème ni tracer les lignées template → instance.
- **How to apply** : Tout doc Brain porte un `code` dans son frontmatter, conforme à l'une des deux grammaires ci-dessous selon son type.

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
- Exemples : `OBJ.STATUT`, `CAP.FAMILY`, `PROMPT.ARCH_ROLE`, `META.FAMILY`, `LGBLK.FAMILY`.

**Justification du cas spécial** : les taxonomies ont une structure hiérarchique intrinsèque (`namespace.taxo`) qui est leur identité même, pas une description. Le namespace joue déjà le rôle de classifieur de premier niveau - équivalent fonctionnel d'un préfixe. Un agent voit `OBJ.STATUT` (format `XXX.YYY` avec point) → c'est sans ambiguïté une taxonomie.

##### Grammaire 3 - Codes de taxons (valeurs taxonomiques)

```
<NAMESPACE>.<TAXO>.<VALEUR>
```

- Hérite du code de la taxonomie parente, ajoute `.<VALEUR>`.
- `<VALEUR>` : MAJUSCULES, peut contenir `_`.
- Exemples : `OBJ.STATUT.BROUILLON`, `OBJ.STATUT.VALIDE`, `CAP.FAMILY.SOFT`, `META.FAMILY.CHARTS`.

##### Table de préfixes (Grammaire 1)

| Préfixe | Type de doc Brain | Taxo de référence | Sous-typage interne |
|---|---|---|---|
| `DBMAN_TW` | Manuel de BDD (Twin) | `DOC.TYPE` + `DBMAN.SCOPE.TWIN` | - |
| `DBMAN_MO` | Manuel de BDD (Mission Ops) | + `DBMAN.SCOPE.MISSION_OPS` | - |
| `DBMAN_BR` | Manuel de BDD (Brain) | + `DBMAN.SCOPE.BRAIN` | - |
| `WRRD_TW` | WR-RD (Twin) | `DOC.TYPE.WR_RD` + scope | - |
| `WRRD_MO` | WR-RD (Mission Ops) | idem | - |
| `CPT` | Note de concept | `DOC.TYPE.NOTE_CONCEPT` | - |
| `TPL` | Template d'instanciation | `DOC.TYPE.TEMPLATE_INSTANCIATION` | - |
| `TPL_BRICK` | Template de Brick | `DOC.TYPE.TEMPLATE_BRICK` | `BRICK.FAMILY` |
| `PRMPT_M` | Prompt maître | `DOC.TYPE.PROMPT` | `PROMPT.ARCH_ROLE.PROMPT_MAITRE` |
| `PRMPT_S` | System prompt | idem | `PROMPT.ARCH_ROLE.SYSTEM_PROMPT` |
| `PRMPT_U` | Prompt d'exécution | idem | `PROMPT.ARCH_ROLE.PROMPT_EXECUTION` |
| `PRMPT_T` | Template prompt | idem | `PROMPT.ARCH_ROLE.TEMPLATE_PROMPT` |
| `LGBLK` | Logic block | `DOC.TYPE.LOGIC_BLOCK` | `LGBLK.FAMILY` (à créer) |
| `METH` | Méthode | `DOC.TYPE.METHODE` | `MET.FAMILY` |
| `CHRT` | Doc méta (charte / doctrine / playbook) | `DOC.TYPE.DOC_META` | `META.FAMILY` (8 valeurs) |
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

1. **Stabilité absolue** : un code donné est immuable. Pour "renommer" un objet, on en crée un nouveau et on archive l'ancien (R-053).
2. **Pas de date dans les codes** (jamais). La date est un attribut de l'objet (`created_at`, `updated_at`, etc.), pas une composante de son identité.
3. **Pas de famille / sous-famille variable dans le code** : sauf namespace stable des taxonomies. Famille = propriété frontmatter / BDD, pas dans le code.
4. **Pas de rattachement multi-contexte** dans le code : le code reflète le contexte de création canonique. Les rattachements multiples (multi-orga, multi-mission) sont gérés via propriétés relationnelles.
5. **Casse** : MAJUSCULES partout (dans le code).
6. **Séparateur** : selon la grammaire - `_` pour Grammaire 1, `.` pour Grammaires 2 et 3.
7. **Pas de suffix `LBP`** : implicite, l'écosystème est entièrement LBP. Allègement.
8. **Unicité globale cross-écosystème** : aucun code ne doit collisionner avec un autre, tous types et scopes confondus.

##### `template_code` dans le frontmatter

Tout doc généré depuis un template porte dans son frontmatter (zone Méta-gouvernance, cf. R-055) :
- `template_code` : le code du template d'origine (ex. `TPL_DBMAN_TW`)
- `template_version` : version semver du template au moment de la génération (ex. `6.3.0`)

Permet l'audit de lignée structurelle (*"tous les docs avec `template_code: TPL_DBMAN_TW` doivent avoir `template_version >= 6.3.0`"*).

##### Phase 2 - Extension Twin / Mission Ops (à appliquer plus tard)

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
| etc. | (à compléter par BDD Twin) | |

##### Conséquence si violation

Faux positifs en audit, codes dupliqués, références cross-écosystème cassées, agents ne pouvant filtrer fiable par regex, ruptures de lignée template → instance.

##### Découverte

28-04-2026, Leonard, en préparation du chantier de migration globale. Capturé après audit ciblé des taxonomies Brain et arbitrages collaboratifs sur la grammaire (sub-agent `taxos_brain_audit.md`).

#### R-055 : Frontmatter canon des docs Brain (3 zones balisées)

- **Portée** : Transverse à tout doc Brain instancié dans l'écosystème (manuels, WR-RD, taxos, notes de concept, templates, prompts, logic blocks, méthodes, docs méta, agents, outils externes, glossaire).
- **Statut** : Actif
- **Why** : Le frontmatter sert simultanément 3 publics distincts (agents de gouvernance, agents de maintenance, agents d'usage qui consomment le doc) qui n'ont pas les mêmes besoins. Sans structure claire, le frontmatter devient une soupe illisible et les agents se mélangent les pinceaux. La structure en 3 zones balisées rend explicite la sépration des préoccupations sans rien retirer du frontmatter.
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
# + champs spécifiques au type (canonical_name, namespace_code, scale_kind,
#   bdd_canonical_name, object_type, target_bdd_canonical_name, etc.)
---
```

##### Champs obligatoires

| Zone | Champ | Type | Notes |
|---|---|---|---|
| Identité | `title` | string | affichage humain |
| Identité | `doc_type` | enum | **token MAJUSCULES** correspondant à un taxon de la taxonomie `DOC.TYPE` (sans le préfixe `DOC.TYPE.`). Valeurs autorisées : `MANUEL_BDD`, `WR_RD`, `NOTE_CONCEPT`, `TAXONOMIE`, `TEMPLATE_INSTANCIATION`, `TEMPLATE_BRICK`, `PROMPT`, `LOGIC_BLOCK`, `METHODE`, `DOC_META`, `AGENT`, `OUTIL_EXTERNE`, `GLOSSAIRE_ENTRY`. Validation regex : `^[A-Z_]+$`. Permet à un agent de retrouver mécaniquement le taxon `DOC.TYPE.<valeur>` dans la taxonomie `DOC.TYPE`. |
| Identité | `code` | string | conforme R-054 |
| Méta-gouvernance | `version` | string | format `MAJOR.MINOR` selon **R-056** (ex. `"1.0"`, pas de PATCH) |
| Méta-gouvernance | `template_code` | string | code du template d'origine (R-054) - obligatoire pour docs générés depuis un template |
| Méta-gouvernance | `template_version` | string | format `MAJOR.MINOR` selon **R-056**, version du template au moment de la génération |
| Méta-gouvernance | `created_at` | string | format JJ-MM-YYYY (R-044) |
| Méta-gouvernance | `updated_at` | string | format JJ-MM-YYYY (R-044) - **règle obligatoire** : à bumper à chaque modification, même mineure |
| Spec d'usage | `summary` | string | description courte du **contenu** ("qu'est-ce que c'est") |
| Spec d'usage | `purpose` | string | raison d'être / objectif fonctionnel ("à quoi ça sert") |
| Spec d'usage | `tags` | list | indexation |

##### Hors frontmatter (volontairement)

- **`status`** : vit en BDD Brain uniquement. Statut bouge agilement (brouillon → à revoir → validé → archivé), maintenir le doublon frontmatter ↔ BDD est coûteux et non rigoureux. La BDD est plus appropriée pour ce champ qui change vite.
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

À chaque modification d'un doc (même mineure : correction typo, ajout d'un mot, mise à jour d'un exemple), le champ `updated_at` du frontmatter doit être bumpé à la date du jour (format JJ-MM-YYYY, R-044).

Pour fiabilisation future : un hook git pre-commit peut être ajouté pour bumper automatiquement la date sur les fichiers modifiés.

##### Conséquence si violation

Frontmatter incohérent entre docs, agents qui ne trouvent pas les champs attendus, audit Brain ↔ vault impossible, perte de la traçabilité de lignée template.

##### Découverte

28-04-2026, Leonard, après audit factuel des frontmatter de toutes les typologies (sub-agent `frontmatter_audit_report.md`) qui a révélé 3 anomalies majeures, 5 templates sans bloc B, double frontmatter visuel sur 2 templates, et asymétries Twin / Mission Ops (`created_at` vs `date_creation`, R-044 violée côté Mission Ops, `code` absent des manuels Twin).

#### R-056 : Grammaire de versioning des docs Brain (`X.Y`)

- **Portée** : Transverse à tout doc Brain (manuels, WR-RD, taxos, notes de concept, templates, prompts, logic blocks, méthodes, docs méta, agents, outils externes, glossaire). Concerne le champ `version` du frontmatter (R-055).
- **Statut** : Actif
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

Pour un template, le MAJOR bump est **structurellement important** : il indique que les docs générés à partir des versions précédentes doivent être migrés (mise à jour structurelle). Le `template_version` dans le frontmatter des docs générés (R-055) permet d'auditer mécaniquement la lignée et de détecter les docs stale.

##### Migration des versions existantes

Pour les docs déjà existants qui portent un format `X.Y.Z`, la migration consiste à **tronquer le PATCH** (sans bumper) :

| Version actuelle | Version migrée |
|---|---|
| `1.0.0` | `1.0` |
| `0.3.0` | `0.3` |
| `6.3.0` | `6.3` |
| `5.1.0` | `5.1` |
| `07-04-2026 v0.5.0` (anti-pattern) | `0.5` + `created_at: "07-04-2026"` séparé |

C'est une migration de format pure (pas un changement de contenu) : la version reste la même, juste reformattée.

##### Impacts cascade sur autres règles

- **R-053** (filename des archives) : le suffix `(archivé v<X> le JJ-MM-YYYY)` utilise désormais le format `X.Y` (au lieu de `X.Y.Z`). Migration des 212 archives existantes : tronquer le PATCH dans les filenames.
- **R-055** (frontmatter canon) : le champ `version` suit R-056 (`X.Y`).
- **`template_version`** : suit également R-056 (`X.Y`).

##### Conséquence si violation

Versions illisibles ou ambiguës, audit de lignée template impossible, agents incapables de distinguer refonte et correction.

##### Découverte

28-04-2026, Leonard, en challengeant la convention semver `X.Y.Z` héritée par défaut. Constat : aucune convention de versioning n'a jamais été formalisée dans LBP, les versions actuelles ont été générées à la volée par différents agents sans règle commune, donc on n'est pas tenu de suivre semver. Décision : passer à `X.Y` plus simple et adapté aux docs.

---

#### R-057 : Discipline d'usage des backticks Markdown

- **Portée** : Transverse à tous les docs Markdown LBP (manuels de BDD, WR-RD, taxonomies, notes de concept, templates, méthodes, prompts, logic blocks, chartes, playbooks, docs méta).
- **Statut** : Actif
- **Why** : Les backticks `` ` `` ont une fonction Markdown précise : signaler un **token technique littéral** (rendu en `monospace`). Mais ils ont été utilisés sans discipline dans plusieurs docs (notamment manuels de BDD existants) - parfois autour de mots du langage courant pour de la mise en évidence générale, parfois aléatoirement. Conséquences : (a) bruit visuel, (b) confusion entre identifiant technique et prose, (c) perte de la valeur sémantique de la convention.
- **How to apply** : les backticks sont **réservés** aux usages suivants (liste fermée) :
  - Nom d'une propriété, d'une variable, d'un champ : `created_at`, `brick_type`, `purpose`
  - Valeur de taxo / code de doc : `BRICK.PROFIL_ORGA`, `BRK_PROFIL_ORGA_001`, `DOC.TYPE`
  - Fragment de syntaxe / commande / regex : `<!-- @INSTR-START -->`, `grep -E "@INSTR"`, `[A-Z]+_[A-Z]+`
  - Nom de fichier / chemin : `Template - Méthode LBP.md`, `refs/RULES_LBP.md`
  - Nom de bloc / section technique : `TEMPLATE_USAGE_GUIDE`, `SECTION_X_GUIDE`
- **Interdits** : mise en évidence générale dans la prose (utiliser `**gras**` pour insister, `*italique*` pour nuancer ou citer un terme), encadrer un mot du langage courant, encadrer une phrase entière.
- **Cas particulier** : à l'intérieur d'un commentaire HTML `<!-- ... -->`, ne **jamais** écrire la séquence `-->` littérale (même entourée de backticks), car le parseur HTML ferme le commentaire avant que Markdown n'agisse. Solution : sortir l'exemple à citer hors du commentaire HTML (cf. convention de structuration des templates v1.1+).
- **Conséquence si violation** : bruit visuel, confusion lecture, et dans le cas du `-->` dans un commentaire : commentaire HTML cassé en plein milieu, instructions exposées en zone visible.
- **Découverte** : 28-04-2026, Leonard, en repérant que le `` `<!-- @INSTR-START ... @INSTR-END -->` `` cité dans la procédure de purge finale d'un template cassait le périmètre du commentaire HTML englobant. Discussion menant aussi à formaliser l'usage discipliné des backticks au-delà du seul cas du `-->`.

---

#### R-058 : Aucune jumelle texte sur les BDDs Brain

- **Portée** : Les 11 BDDs Brain (Core + Motor : Glossaire LBP, Notes de concept, Taxonomies, Manuels de BDD, Docs méta LBP, Méthodes LBP, Prompts LBP, Templates de bricks, Agents LBP, Outils externes, Registre des logic blocks). **Hors scope** : BDDs Digital Twin (les jumelles texte y sont **autorisées et utiles**, cf. R-039 et conventions Twin) ; BDDs Mission Ops (usage **expérimental** à valider, non interdit pour l'instant).
- **Statut** : Actif
- **Why** : Une "jumelle texte" est une propriété texte qui duplique manuellement le contenu d'une relation native (ex : sur la BDD Logic blocks, la relation `est utilisé dans (Prompts LBP)` côté Notion + un champ texte `est utilisé dans (Prompts LBP) [texte]` qui répète à la main les noms des prompts liés). Côté Twin, ces jumelles servent à **capter des indices** dans des champs textes pour aider à la connexion logique d'objets quand la relation native échoue ou n'est pas encore créée. **Côté Brain**, ce besoin n'existe pas : les objets Brain sont créés et gérés de manière déterministe par les agents/consultants à partir de leurs manuels respectifs ; il n'y a pas d'indices textuels à interpréter. Une jumelle texte sur une BDD Brain est donc **toujours redondante avec une relation native** et introduit : (a) une dette de double saisie, (b) un risque silencieux de désynchronisation entre la relation native et son écho texte, (c) une charge cognitive sans contrepartie pour les agents en retrieval.
- **How to apply** :
  - Aucune propriété de type `text` ou `rich_text` portant un nom dérivé d'une relation existante (ex : `<rel> [texte]`, `<rel> (texte)`) sur une BDD Brain.
  - Si une jumelle texte est détectée sur une BDD Brain (audit ou découverte ad hoc), action : **DROP** côté Notion + retrait éventuel du manuel s'il en faisait mention.
  - À l'inverse, **ne pas chercher à créer** des jumelles texte sur les BDDs Brain dans une logique de "filet de sécurité" - l'isolation Brain ↔ Twin/MO (D-019) garantit que les relations Brain sont peu nombreuses et bien maîtrisées, donc le risque de relation cassée est faible.
- **Cas particulier Mission Ops** : usage expérimental autorisé pour tester si elles produisent des infos complémentaires utiles (capture d'indices sur les bricks/sources/meetings). À ré-évaluer après une mission complète.
- **Conséquence si violation** :
  - Doublonnage du modèle, sources de vérité multiples pour la même info.
  - Désynchronisation silencieuse (relation modifiée mais pas le texte, ou inverse).
  - Pollution des audits Manuel ↔ Notion (champ Notion non documenté = faux positif).
- **Découverte** : 28-04-2026, Leonard, lors de l'audit transverse Notion ↔ Manuels Brain (Phase 6.5 post-commit). Détection sur la BDD Registre des logic blocks de 2 jumelles texte (`est utilisé dans (Prompts LBP) [texte]`, `s'applique à (Manuels de BDD) [texte]`) en conflit avec la règle 3.1 du manuel Logic blocks. Décision Leonard : interdire la pratique sur Brain, conserver Twin (où elle est utile), tester Mission Ops.

---

#### R-059 : Hygiène d'écriture des docs Brain - pas de bruit historique ni de spéculation future

- **Portée** : Tous les docs de l'écosystème Brain LBP (Core + Motor) : manuels de BDD, WR-RD, notes de concept, taxonomies, templates, méthodes LBP, prompts, logic blocks, fiches agents, fiches outils externes, glossaires LBP. **Hors scope** : docs de session (`refs/`, `CLAUDE.md`, `DECISIONS_LBP.md`, backlog) qui ont vocation à porter justement l'historique et les hypothèses ; docs Mission Ops (où le journal de mission peut faire partie du livrable) ; docs Digital Twin (où certaines mentions de timeline mission sont structurellement utiles).
- **Statut** : Actif
- **Why** : Chaque doc Brain est consommé par des **agents en retrieval** qui n'ont pas connaissance du contexte historique de l'écosystème (sauf l'agent Brain architect qui pilote l'évolution). Pour qu'un agent puisse lire un manuel, une note de concept ou un template et **agir correctement à partir de ce seul doc**, il faut que le doc soit **autonome** : une source de vérité brute à l'instant t. Toute mention historique ("précédemment ce champ s'appelait X", "en V2 on faisait Y") ou spéculative ("à terme on pourrait", "piste à creuser", "amélioration future") crée du **bruit** : (a) charge cognitive inutile, (b) ambiguïté sur ce qui est canon vs ce qui est obsolète/futur, (c) risque que l'agent se base sur une version périmée ou non validée.
- **How to apply** : dans tout doc Brain, **interdiction** d'écrire :
  - **Mentions historiques** : "anciennement", "avant la V3", "ce champ s'appelait X", "on a supprimé Y", "migration depuis Z"
  - **Spéculations futures** : "à terme", "à voir plus tard", "piste à creuser", "amélioration potentielle", "TODO pour le futur", "à étudier"
  - **États transitoires** : "en cours de finalisation", "version provisoire", "draft à valider" (le statut vit dans le frontmatter ou la BDD, pas dans le corps)
- **Où vit l'historique** : commits Git (changelog), `refs/DECISIONS_LBP.md` (pourquoi tel choix structurant), backlog (`refs/RULES_BRAIN_TWIN-backlog.md` pour les règles pressenties).
- **Où vivent les pistes futures** : `refs/RULES_BRAIN_TWIN-backlog.md`, TodoWrite de session, ou notes personnelles de Leonard. Pas dans les docs Brain publiés.
- **Cas accepté** : un doc peut citer **explicitement** une règle (ex : R-058) ou une décision (ex : D-019) **comme référentiel canonique courant** - ce n'est pas une mention historique, c'est une déclaration de conformité.
- **Conséquence si violation** :
  - Agents en retrieval qui hésitent entre deux versions, choisissent mal, ou propagent l'incertitude.
  - Difficulté pour un humain de relire le doc et savoir "ce qui est vrai aujourd'hui".
  - Pollution sémantique : le doc devient un mélange de documentation et de log de chantier.
- **Découverte** : 28-04-2026, Leonard, après détection que mes propositions de mises à jour de manuels Brain incluaient des "notes de version" expliquant ce qui changeait par rapport à la version précédente - exactement le bruit historique que cette règle interdit. Capture immédiate.

---

#### R-060 : Hygiène d'écriture des champs `summary` et `purpose` du frontmatter Brain

- **Portée** : Tous les docs Brain (manuels de BDD, taxonomies, notes de concept, méthodes, prompts, agents, outils externes, templates de bricks, docs méta, WR-RD, logic blocks, glossaire, etc.). Concerne les deux champs `summary` et `purpose` du frontmatter R-055.
- **Statut** : Actif
- **Why** : Les champs `summary` et `purpose` sont consommés à la fois par les **agents en retrieval** (qui décident s'ils doivent ouvrir le doc complet) et par les **humains** qui parcourent les BDDs. Trois pièges détruisent leur valeur : (1) **doublon** entre les deux champs (rotation grammaticale stérile), (2) **couplages fragiles** (énumération des valeurs, citation d'objets voisins par leur code ou leur libellé, duplication de qualificatifs déjà portés par d'autres champs du frontmatter), (3) **exploitations métier en aval arbitraires** dans `purpose` (« pour la priorisation », « pour le diagnostic », « pour la transformation »...) qui figent un consommateur parmi N. Une discipline stricte sur ces 3 axes assure densité, robustesse aux évolutions, et lisibilité indépendante.
- **How to apply** :

##### Distinction conceptuelle `summary` vs `purpose`

| Champ | Répond à | Contenu attendu | Forme |
|---|---|---|---|
| `summary` | « **Qu'est-ce que c'est ?** » (description pédagogique, dans l'absolu) | Nature de l'objet (Référentiel / Échelle / Lexique / Cadre...) + axe ou dimension qu'il découpe. **Auto-suffisant** : aucune référence à un objet voisin. | Phrase nominale, lisible isolément. Ex : « Référentiel des grands types de mandats qu'un poste peut porter dans une organisation. » |
| `purpose` | « **À quoi ça sert ?** » (raison d'être structurelle dans l'écosystème LBP) | Action principale qu'on accomplit avec l'objet + **effet structurel direct** sur les objets ainsi qualifiés. **Pas d'exploitation métier en aval**. | **Verbe à l'infinitif en tête**, pattern « *Verbe + objet, pour + effet structurel direct (+ lest descriptif neutre éventuel)* ». Ex : « Qualifier un poste par son mandat dominant, pour cartographier de façon stable et lisible la nature des responsabilités tenues dans une organisation, indépendamment des intitulés de poste locaux. » |

##### Doctrine d'autonomie (zéro citation d'objet voisin)

Ni `summary` ni `purpose` ne citent jamais d'autres objets de l'écosystème - **ni par leur code, ni par leur libellé conceptuel, ni par référence indirecte** (« distinct de X », « complète Y », « à ne pas confondre avec Z »). Les distinguos cross-objets ont leur place dédiée en **section 6 du fichier** (« Cohérence & impacts croisés »), point d'autorité unique. `summary` et `purpose` décrivent l'objet **dans l'absolu**, comme une définition pédagogique autonome.

##### Doctrine de non-redondance (DRY)

| Type de redondance interdite | Exemple à proscrire | Pourquoi |
|---|---|---|
| Doublon `summary` ↔ `purpose` | summary: « Qualifie X selon Y... » + purpose: « Qualifier X selon Y... » | Rotation grammaticale stérile |
| Énumération des valeurs/taxons | « ...direction, management, expert, opérationnel, support... » | La section 3 du fichier est le point d'autorité unique. Couplage : un changement de taxon imposerait de toucher 3 endroits. |
| Citation d'un objet voisin (code OU libellé) | « ...JOB.FAMILLE », « ...la famille métier », « ...complète la séniorité » | Couplage avec un objet susceptible d'évoluer (renommage, refonte, suppression). Les distinguos vivent en section 6. |
| Nom de BDD ou de propriété d'instanciation | « ...via le champ `Famille (Doc méta)` de la BDD Notion » | Couplage avec le backend (Notion = transitoire). Le doc reste **agnostique du backend**. |
| Qualificatifs déjà portés par un champ structuré | « Référentiel **fermé nominal mono-sélection** des... » | `is_open`, `scale_kind`, `selection_mode`, `cardinality` portent déjà ces infos. Garder seulement la **nature de l'objet** (Référentiel / Échelle / Lexique / Cadre) dans le summary. |

##### Doctrine d'effet structurel direct (purpose)

Le `purpose` décrit **l'effet immédiat** que produit la taxo sur les objets qu'elle qualifie - **pas les exploitations en aval** qui consomment cet effet. Cas d'usage métier interdits : priorisation, diagnostic, transformation, recommandation, audit, allocation, pilotage.

✅ Effets structurels directs autorisés (intrinsèques à l'objet) : *cartographier, rendre comparable, qualifier de façon homogène, ancrer dans le temps, tracer, hiérarchiser, positionner, distinguer, normaliser, classer, catégoriser*.

✅ Lest descriptif neutre autorisé pour enrichir sans surspécifier : qualificatifs de l'effet (*stable, lisible, partagé, homogène, transverse, fiable*), ancrage descriptif neutre (*indépendamment des intitulés locaux, entre objets de natures différentes, dans le temps, à un instant donné*).

##### Forme des deux champs

- **≤400 caractères** chacun (plafond unifié).
- **Lisible isolément** : `summary` comme `purpose` doivent rester compréhensibles s'ils sont extraits seuls (sans le reste du frontmatter, sans le corps du fichier).
- **Lisible par humain ET par agent** - formulation neutre sur le consommateur. Ne jamais se référer explicitement à « l'agent », « le consultant », « les utilisateurs » dans ces champs.
- **Pas de jargon d'implémentation** : ni « Notion », « rollup », « update_data_source », ni nom de propriété backend.
- **Apostrophes typographiques** `’` (R-052).

##### Anti-patterns à proscrire (synthèse)

- ❌ « Aider un agent à classer X » → ✅ « Classer X »
- ❌ « Cette taxonomie permet de... » → ✅ aller direct à la fonction
- ❌ summary : « Qualifie X selon Y » + purpose : « Qualifier X selon Y » → ✅ summary nominal, purpose action + effet structurel
- ❌ Énumération des valeurs en prose → ✅ la section 3 du fichier est le point d'autorité
- ❌ Citation d'objet voisin (code OU libellé : `JOB.FAMILLE`, « la famille métier ») → ✅ section 6 « Cohérence & impacts croisés »
- ❌ Public cible explicite (« pour les consultants ») → ✅ neutre
- ❌ Qualificatifs déjà portés par un champ structuré du frontmatter → ✅ DRY
- ❌ Exploitation métier en aval (« pour la priorisation », « pour le diagnostic », « pour la transformation ») → ✅ effet structurel direct

##### Exemples canoniques (3 cas hétérogènes validés 29-04-2026)

**Cas nominal - `ORG.ROLE`** (mono, fermé)
- summary : « Référentiel des grands types de mandats qu'un poste peut porter dans une organisation. »
- purpose : « Qualifier un poste par son mandat dominant, pour cartographier de façon stable et lisible la nature des responsabilités tenues dans une organisation, indépendamment des intitulés de poste locaux. »

**Cas ordinal - `SCALE.CRITICALITY`** (1-5, mono, fermé)
- summary : « Échelle 1-5 de gravité des conséquences attendues d'un objet en cas de non-traitement ou de matérialisation. »
- purpose : « Positionner un objet sur une échelle de gravité, pour rendre comparable la sévérité des conséquences attendues entre objets de natures différentes, avec une lecture homogène et partagée. »

**Cas hiérarchique - `ASSET.SUBTYPE`** (mono, fermé)
- summary : « Cadre de classification des actifs non humains mobilisés ou produits par le système étudié, organisé par familles puis sous-types. »
- purpose : « Classer un actif non humain par sa famille puis son sous-type, pour qualifier le portefeuille observé de façon homogène, lisible et stable dans le temps. »

- **Conséquence si violation** : couplage fragile (renommage/suppression d'objets voisins → asymétries silencieuses), redondance stérile entre champs, surspécification arbitraire des cas d'usage, perte de densité informationnelle.
- **Découverte** :
  - 29-04-2026 (v1) : Leonard signale que tous mes purpose commençaient par « Aider un agent à... » - redondant et excluant.
  - 29-04-2026 (v2) : après refonte de 102 taxos, Leonard signale doublon summary↔purpose, énumération des valeurs, citation de codes externes. Ajout doctrine DRY et exemple canon ORG.ROLE.
  - 29-04-2026 (v3, version actuelle) : durcissement final après itération sur 3 cas test. Suppression totale des références à des objets voisins (même en libellé conceptuel), suppression des exploitations métier en aval dans purpose, ajout du pattern « verbe + objet + pour + effet structurel direct + lest descriptif neutre ».

---

## 2. Règles Brain

*Règles spécifiques à la gouvernance du Brain (Core + Motor + Admin).*

### 2.1 Nommage et identification des objets

#### R-005 : Code unique stable

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Référencement stable entre BDD, résistance aux renommages.
- **How to apply** : Le code unique d'un objet Brain (ex: `CPT.GOV.LBP.SSOT`) ne change jamais, même si le nom canonique évolue.
- **Découverte** : Règle initiale.

*Sous-section à enrichir quand on formalisera les conventions de nommage des nouveaux objets (actif, poste, collectif, etc.).*

### 2.2 Templates et instanciation

#### R-004 : Template obligatoire pour tout nouveau doc Brain

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Homogénéité, gouvernance par les Docs méta, agents IA capables d'instancier.
- **How to apply** : Tout doc Brain est généré à partir d'un template (indexé dans Docs méta LBP). Cycle : Template → instanciation → cleanup → validation → indexation Notion.
- **Découverte** : Principe architectural originel.

#### R-040 : Toutes les instructions de génération vivent dans des blocs `@INSTR-*`

- **Portée** : Brain (templates d'instanciation)
- **Statut** : Actif
- **Why** : Un template définit la structure du doc final (sections numérotées `# 1)`, `# 2)`, etc.). Si une instruction de génération apparaît sous forme d'un titre Markdown numéroté (ex. `# 0) GUIDE D'INSTANTIATION`), elle se confond visuellement avec les vraies sections du doc final, crée un parasitage cognitif (la séquence `0,1,2,3...` laisse penser que `0)` est le début légitime de la structure), et augmente le risque que l'agent générateur oublie de la supprimer ou la prenne par mimétisme pour un modèle de section. Par construction, les instructions de génération ne doivent **jamais** ressembler à une section du doc final.
- **How to apply** :
  - Tout contenu qui guide la génération du doc (instructions, doctrine, exemples normatifs, paramétrages, vocabulaire contrôlé, guide d'instanciation, settings…) DOIT vivre **exclusivement** dans un bloc `<!-- @INSTR-START: NOM_BLOC ... @INSTR-END: NOM_BLOC -->`.
  - **Aucun titre Markdown numéroté** (`# 0)`, `## 0.1`, etc.) ne doit servir de wrapper à des instructions de génération.
  - Les blocs `@INSTR-*` sont **flottants** dans le template (placés là où c'est lisible pour l'auteur du template) et tous **systématiquement supprimés** à l'instanciation par la `cleanup_rules` standard `SUPPRIMER tous les commentaires HTML @INSTR-*`.
  - La `cleanup_rules` du template ne doit **jamais** contenir une règle ad hoc du type `SUPPRIMER la section 0) GUIDE D'INSTANTIATION` puisque cette section ne doit pas exister.
  - Les sections numérotées `# 1)`, `# 2)`, etc. sont **réservées à la structure du doc final** et ne contiennent jamais de contenu d'instruction de génération.
  - Une vraie section structurelle d'un doc final peut légitimement être numérotée `# 0)` si elle décrit du contenu métadata du doc (ex. `# 0) Meta de la brick` dans `Template méta de Brick.md` qui contient des sous-sections 0.1 Contexte & mandat, 0.2 Sources & procédé de production…). Le critère de discrimination : ce contenu apparaît-il dans le doc instancié final (oui = structure, à laisser) ou est-il supprimé à l'instanciation (oui = instruction, à wrapper dans `@INSTR-*`) ?
- **Exemples** :
  - ✅ `<!-- @INSTR-START: INSTANTIATION_GUIDE [contenu] @INSTR-END: INSTANTIATION_GUIDE -->` placé entre les autres blocs `@INSTR-*` du template.
  - ❌ `# 0) GUIDE D'INSTANTIATION - [INSTR-SECTION] (SUPPRIMER APRÈS USAGE)` suivi de sous-titres `## 0.1`, `## 0.2`…
  - ❌ `cleanup_rules: - SUPPRIMER la section 0) GUIDE D'INSTANTIATION` (témoigne d'une violation à corriger).
- **Conséquences** :
  - ✅ Structure du doc final sacrée et lisible (numérotation commence à `1`, jamais à `0` pour des instructions).
  - ✅ Une seule règle de cleanup suffit : `SUPPRIMER tous les commentaires HTML @INSTR-*`.
  - ✅ Pas de risque de contamination structurelle ni d'oubli de suppression.
- **Migration effectuée** : 26-04-2026 - 6 templates corrigés (Template Manuel de BDD - Digital Twin v6.1.0→v6.2.0 ; Template WR-RD - Digital Twin v1.0.0→v1.1.0 ; template-methode_lbp v1.0.0→v1.1.0 ; Template-prompt_lbp v1.0.0→v1.1.0 ; Template-Fiche_outil_LBP v1.0.0→v1.1.0 ; template-taxonomie). Le 7e cas (`# 0) Meta de la brick` dans `Template méta de Brick.md`) est conservé car c'est une vraie section structurelle du doc final.
- **Découverte** : 26-04-2026, Leonard, après revue des templates Manuel de BDD - Digital Twin v6.1.0 et WR-RD - Digital Twin v1.0.0.

### 2.3 Indexation Notion (doc → BDD)

#### R-006 : Descriptions Notion ≤280 caractères

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Lisibilité Notion, cohérence inter-BDD, utilisabilité par les agents.
- **How to apply** : Les descriptions de propriétés dans Notion commencent par un verbe à l'infinitif, restent en texte brut, ne dépassent pas 280 caractères. On les copie directement depuis le manuel de BDD.
- **Découverte** : Convention établie dans les templates de manuels de BDD.

#### R-029 : Le doc Markdown est source de vérité pour l'indexation Notion

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Éviter toute divergence entre le contenu du doc et ses propriétés Notion. Les propriétés sont dérivées, pas inventées.
- **How to apply** : Avant de créer ou mettre à jour une entrée Notion, l'agent doit **lire l'intégralité du doc Markdown correspondant**. Les propriétés sont dérivées du contenu. Si une propriété ne peut pas être dérivée du doc de façon non-ambiguë, laisser vide et signaler plutôt qu'inventer. Respecter les contraintes de format portées par **la description de chaque propriété Notion** (qui fait office d'instructions d'écriture).
- **Exemples** : ✅ `Définition` remplie avec 3-10 lignes extraites/synthétisées du doc (car la description Notion impose 3-10 lignes) / ❌ `Définition` générée de toutes pièces par l'agent
- **Découverte** : 24-04-2026, Leonard, avant indexation Twin v2

#### R-030 : Double indexation d'une note de concept

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Le Glossaire LBP est un hub sémantique qui n'a pas de lien source direct. Le lien vers le doc vit côté `Registre des notes de concept`. Le Glossaire porte la sémantique, le Registre porte la traçabilité.
- **How to apply** : Indexer une note de concept = créer **2 entrées Notion liées** :
  1. Une entrée dans `Registre des notes de concept` avec `Lien note concept (source) = URL Drive`
  2. Une entrée dans `Glossaire LBP` avec les propriétés sémantiques (Type concept, Domaine, Définition, Règles d'usage, etc.)
  3. Lier l'entrée Glossaire → Registre via la relation `est documenté par (notes de concept)`
  4. Si applicable, lier également Glossaire → Méthodes (`est mis en oeuvre par`) et/ou Glossaire → Manuels de BDD (`est modélisé par`)
- **Découverte** : 24-04-2026, Leonard, avant indexation Twin v2

#### R-031 : Alignement du code unique entre note de concept et glossaire

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Traçabilité stable et navigation cohérente. Un même concept doit avoir le **même code** dans les deux BDD.
- **How to apply** : Le `Code unique` d'une entrée dans `Registre des notes de concept` et l'entrée correspondante dans `Glossaire LBP` doivent être strictement identiques (ex: `CPT.CAP.LBP.ACTIF` dans les deux). Ce code provient du doc Markdown source (propriété ou convention du template).
- **Découverte** : 24-04-2026

#### R-033 : Les descriptions de propriétés Notion sont des mini-prompts de remplissage

- **Portée** : Brain (indexation)
- **Statut** : Actif (temporaire - à updater quand les BDD Brain auront leurs docs d'instructions d'écriture et clefs de lecture)
- **Why** : Pour les BDD du Brain, les **instructions d'écriture** ne vivent pas encore dans des docs séparés ; elles sont portées par les **descriptions de chaque propriété Notion**. Ignorer ces descriptions produit des contenus hors format.
- **How to apply** : Avant de remplir une propriété, **lire sa description Notion** (via `notion-fetch` sur la data source). Respecter scrupuleusement les contraintes :
  - Format imposé (ex: "3 à 10 lignes", "séparateur ';'", "MAJUSCULES")
  - Structure imposée (ex: "Bon usage: ... ; Mauvais usage: ...")
  - Valeurs strictes pour les select/multi-select (ex: "valeurs strictes: Core; Motor")
  - Interdictions (ex: "ne pas inclure de contenu client")
- **Exemples** : ✅ Pour `Code unique` d'une taxo, la description impose format `NAMESPACE.FAMILLE.LBP` MAJUSCULES alignée au mini-doc → valeur dérivée du nom de fichier .md / ❌ Inventer un code libre
- **Découverte** : 24-04-2026. À faire évoluer quand les docs d'instructions d'écriture dédiés existeront pour les BDD Brain (aujourd'hui seules les BDD Twin en ont, cf. `Clefs de lectures/TWIN - Instructions écriture + clefs de lecture/`).

#### R-035 : Ordre d'indexation inter-types (graphe de dépendances)

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Chaque type d'artefact Brain a des relations vers d'autres types. Pour éviter de créer une dette de relations (à rattraper dans des passes ultérieures), on indexe par ordre de dépendance : feuilles d'abord, types qui les consomment ensuite.
- **How to apply** : Respecter cet ordre pour une indexation Brain complète :
  1. **Taxonomies** (type feuille - aucune dépendance vers d'autres types Brain)
  2. **Manuels de BDD** (consomment les Taxonomies via `utilise (taxonomies)`)
  3. **Notes de concept + Glossaire** (Glossaire peut référencer Manuels via `est modélisé par`, Méthodes via `est mis en oeuvre par`)
  4. **Méthodes, Agents, Prompts, Logic blocks, Outils externes, Templates de bricks** (consomment Glossaire, Manuels, Docs méta)
- **Généralise R-034** : R-034 dit "créer puis relier" au sein d'un batch. R-035 étend à l'échelle inter-types.
- **Exemples** : ✅ Indexer ASSET.SUBTYPE → puis Manuel Actifs peut référencer ASSET.SUBTYPE dans sa création / ❌ Indexer Manuel Actifs d'abord avec relation vide vers ASSET.SUBTYPE, puis revenir plus tard (dette)
- **Découverte** : 24-04-2026, mini-batch 0 a créé une dette (Manuel Actifs sans ses 7 autres taxos non encore créées). Règle posée pour ne pas reproduire.

#### R-037 : Lecture complète du doc obligatoire avant indexation (pas de raccourci frontmatter)

- **Portée** : Brain (indexation) - **tous types de docs**
- **Statut** : Actif (renforce R-029)
- **Why** : Le frontmatter YAML résume les métadonnées structurelles (title, code, scale_kind, aliases). Les propriétés Notion narratives (Description source, Description courte, Définition, Règles d'usage, Valeur ajoutée...) exigent le contenu approfondi qui vit dans les **sections du corps du doc** (intention + règles d'usage + exclusions + "quoi choisir / quand" + distinctions + patrons d'arbitrage + exemples). Se limiter au frontmatter produit des descriptions pauvres et non-actionnables.
- **How to apply** : Pour indexer **tout doc Brain** (taxonomie, note de concept, manuel de BDD, méthode, prompt, etc.), **lire l'intégralité du doc** avant de remplir les propriétés narratives. Le frontmatter sert uniquement à extraire les champs structurés (title, code, type). Tout le reste doit venir de la lecture du corps :
  - **Taxonomie** : sections 1 (objet/but), 2 (détection du domaine), 5 (heuristique), 8 (exemples) → Description source + Description courte
  - **Note de concept** : sections 1 (résumé, définition, périmètre), 2 (rôle, valeur), 3 (caractéristiques, modules), 4 (relations), 7 (bonnes pratiques) → Définition + Règles d'usage + Valeur ajoutée + Usages IA
  - **Manuel de BDD** : sections 1 (identité), 2 (périmètre/frontières), 3 (rôle systémique), 4 (modèle de données) → Description + Valeur ajoutée + Usages IA
  - **Glossaire** (dérivé de note de concept via R-030) : lire la note de concept ET le doc auquel elle fait référence pour synthétiser
- **Exemples** : ✅ Lire `ORG.CONTEXTE.LBP.md` en entier pour en tirer une Description source qui mentionne "qualifie le contexte organisationnel d'un poste par niveau de périmètre ; règles : choisir 1 seule valeur, ne pas typer un collectif ou une organisation avec cette taxo" / ❌ Se contenter du `summary:` du frontmatter qui dit juste "Qualifie le contexte d'ancrage d'un poste"
- **Découverte** : 24-04-2026, Leonard, après batch A1 où raccourci frontmatter-only a produit des descriptions jugées pauvres

#### R-034 : Ordonnancement création puis relation (2 passes)

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Notion exige que les 2 entrées cibles d'une relation existent avant de pouvoir les lier. Lors d'une indexation par batch, créer d'abord toutes les entrées, puis créer les relations dans une seconde passe.
- **How to apply** :
  1. **Passe 1 - Créations** : créer toutes les entrées Notion sans établir leurs relations (ou seulement les relations vers des entrées déjà existantes)
  2. **Passe 2 - Relations** : établir les relations entre entrées créées dans la passe 1
  3. En pratique : regrouper les doc par "type sans dépendance" en premier (ex: taxonomies), puis types dépendants (ex: manuels qui référencent taxonomies), puis types couvrant le graphe (ex: glossaire qui pointe vers manuels)
- **Exemples** : ✅ Créer Manuel Actifs + Taxo ASSET.SUBTYPE → puis relier Manuel → Taxo / ❌ Tenter de créer le Manuel avec relation vers Taxo qui n'existe pas encore
- **Découverte** : 24-04-2026, lors du dry-run mini-batch 0

#### R-032 : Mise à jour plutôt que création pour une entrée existante

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Éviter les doublons Notion. Les entrées existantes portent peut-être des relations, des rollups, des références qu'on casserait en recréant.
- **How to apply** : Avant de créer une entrée Notion, vérifier qu'elle n'existe pas déjà (par `Code unique` d'abord, puis par `Nom canonique`). Si elle existe :
  - **Mettre à jour** toutes les propriétés en lisant le nouveau doc (cf. R-029)
  - **Mettre à jour le lien source** si le chemin Drive a changé
  - **Ne pas changer le `Code unique`** (stable par R-005)
  - Si le doc v2 porte un **nom ou code différent** de la v1, alors **archiver l'entrée v1** (Statut = Archivé) et **créer une nouvelle entrée v2** (R-036)
- **Découverte** : 24-04-2026

#### R-036 : Le Code unique est l'identité ; MAJ en place tant que le code est stable

- **Portée** : Brain (indexation)
- **Statut** : Actif (révisé 25-04-2026 par Leonard)
- **Why** : Le `Code unique` est l'identité stable de l'objet ; le `Nom canonique` n'est qu'un libellé éditable. Tant que le code est inchangé, l'entité est la même - seul son libellé / sa description / son URL évoluent. Préserver l'entrée existante préserve aussi ses relations Notion entrantes (rollups, références d'autres BDD), ses ID Notion stables, et évite de polluer le Registre avec des doublons archivés.
- **How to apply** :
  - **Code identique** (même si le nom canonique change, peu importe l'amplitude du changement) → **mise à jour en place** de l'entrée existante (Nom, Description, URL Drive, Aliases, etc.). Pas d'archivage.
  - **Code différent** (renommage de namespace, changement de TOKEN, scission/fusion d'objet) → archive de l'entrée v1 + création d'une nouvelle entrée v2.
- **Exemples** :
  - ✅ ORG.CONTEXTE.LBP : v1 "Contexte d'ancrage de rôle" → v2 "Contexte d'ancrage organisationnel d'un poste" (code stable) → **MAJ** de v1
  - ✅ ORG.DEP_LEVEL.LBP → COL.DEP_LEVEL.LBP (code change suite à scission UO→Orga+Collectif) → archive v1 + création v2
  - ✅ ACT.CANDIDATE_TYPE.LBP → ACT.CONSOLIDATION_TARGET.LBP (TOKEN change) → archive v1 + création v2
- **Conséquence** : Registre propre, IDs Notion stables, relations préservées. La trace des évolutions de libellés vit dans l'historique Notion (créé/last edited) et le journal git.
- **Note historique** : version initiale (24-04-2026) imposait archive+create dès que le nom changeait - révisée le 25-04-2026 après détection de 25 doublons inutiles dans batchs A1+A2 (correctifs appliqués).
- **Découverte / révision** : 25-04-2026, Leonard, après examen des batchs A1+A2

#### R-038 : Identifiant pivot par type d'objet (taxonomies = code, autres = nom)

- **Portée** : Brain (indexation, déduplication)
- **Statut** : Actif
- **Why** : R-036 (test de doublon par code unique) ne s'applique strictement qu'aux taxonomies. Pour les autres BDD Brain, le code n'est pas (encore) un identifiant fiable : il peut changer au cours d'updates, n'est pas systématiquement renseigné, ou n'est pas conçu comme pivot de déduplication. C'est le **Nom canonique** qui sert d'identifiant pivot pour ces objets. Confondre les deux logiques amène à créer des doublons (pour les taxos quand on dédoublonne par nom) ou à manquer des doublons (pour les manuels quand on dédoublonne par code).
- **How to apply** :
  - **Taxonomies** → identifiant pivot = `Code unique` (format `XXX.YYY.LBP`, immuable). Application stricte de R-036.
  - **Manuels de BDD, Notes de concept, Glossaire, autres BDD Brain** → identifiant pivot = `Nom canonique` (avec normalisation : trim, casse insensible, accents normalisés pour la comparaison). Le code éventuellement présent est informatif, pas pivot.
  - Lors d'une indexation Notion : avant toute création, requêter le registre cible avec le bon champ pivot. Si match → MAJ en place ; sinon → création.
- **Exemples** :
  - ✅ Taxo ORG.CONTEXTE.LBP : doublon détecté par code → MAJ v1
  - ✅ Manuel "Actifs" (anciennement "Ressources") : doublon détecté par nom (après normalisation) - pas par code, qui peut avoir changé
  - ❌ Tester un doublon de manuel uniquement par code : risque de rater une refonte de nom + code, ou de créer un faux doublon si le code a évolué
- **Conséquence** : R-036 reste valable mais son champ pivot dépend du type d'objet. Cette règle préfigure la procédure de réconciliation pour les batchs B (Manuels) et C (Notes concept + Glossaire).
- **Découverte** : 25-04-2026, Leonard, après correction des 25 doublons A1+A2 - précision donnée pour anticiper les batchs Manuels et Notes concept.

### 2.4 Gouvernance des taxonomies

#### R-007 : Taxonomies par codes

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Séparer le stockage lisible (libellés) du référencement stable (codes).
- **How to apply** : Les BDD stockent des libellés humains. Les codes taxonomiques (ex: `OBJ.STATUT.LBP`) apparaissent uniquement dans les descriptions ≤280 et dans la documentation. Pas de codes dans le corps des textes.
- **Découverte** : Convention établie dans les templates.

#### R-008 : Statuts harmonisés

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Uniformité de gouvernance à travers les 11 BDD Brain.
- **How to apply** : Toutes les BDD Brain utilisent la taxonomie `OBJ.STATUT.LBP` avec les valeurs `Brouillon`, `Validé`, `À revoir`, `Archivé`.
- **Découverte** : Convention établie.

### 2.5 Génération d'une BDD à partir d'un manuel

*Section à remplir quand on documentera le workflow "manuel de BDD → BDD Notion".*

### 2.6 Archivage des docs Brain

#### R-026 : Archivage local par dossier thématique

- **Portée** : Transverse (Brain + Twin)
- **Statut** : Actif
- **Why** : Éviter qu'un "grenier global" à la racine du vault gonfle sans fin et rende l'archivage illisible. Garder l'archive proche de son contexte thématique.
- **How to apply** : Chaque dossier thématique (`Manuels de BDD/Digital Twin/`, `Notes de Concept/`, `Taxonomies/`, `Logic Blocks/`, `Docs Méta LBP/`) a son propre sous-dossier `archives/`. Le git garde l'historique complet des déplacements - pas besoin de doublons dans le vault.
- **Exemples** : ✅ `Notes de Concept/archives/concept - Ressource.md` / ❌ `ARCHIVES/Notes de Concept/...`
- **Découverte** : 24-04-2026, conception arborescence cible pour refonte Twin v2 (D-010)

### 2.7 Conventions de nommage

#### R-027 : Conventions de nommage des fichiers Brain/Twin

- **Portée** : Transverse
- **Statut** : Actif (révisé 26-04-2026 : préfixe `Concept` capitalisé pour aligner avec R-043 ; em dash banni partout)
- **Why** : Homogénéité visuelle dans Obsidian, compatibilité clavier, interopérabilité inter-outils, cohérence fichier ↔ frontmatter (R-043).
- **How to apply** :
  - **Séparateur** : tiret simple `-` (jamais tiret cadratin `-`, jamais underscore). S'applique aux noms de fichiers ET aux champs `title` du frontmatter.
  - **Préfixe manuels de BDD** : `Manuel de BDD - X.md` (Title Case)
  - **Préfixe notes de concept** : `Concept - X.md` (Title Case, capitalisé)
  - **Préfixe WR-RD** : `WR-RD - X.md`
  - **Casse taxonomies** : code canonique, ex: `ACT.IMPACT_DOMAIN.LBP.md`
  - **Accents et apostrophes typographiques autorisés** dans le corps (Obsidian et Drive les gèrent)
  - **Caractères interdits Windows** (`<>:"/\|?*`) à éviter ; si le concept canonique contient `/` (ex. "Input / Output"), le filename utilise `-` à la place (ex. `Concept - Input - Output (LBP).md`).
- **Exemples** :
  - ✅ `Manuel de BDD - Relations inter-organisations.md`
  - ✅ `Concept - Poste.md`
  - ✅ `WR-RD - Actifs.md`
  - ✅ `ORG_REL.TYPE.LBP.md`
  - ❌ `Manuel de BDD - Actifs.md` (em dash banni)
  - ❌ `concept - Actif.md` (préfixe minuscule legacy)
  - ❌ `BDD_ACTIFS.md` (underscore)
- **Migration 26-04-2026** : 87 fichiers vault renommés en bulk + 100 frontmatters harmonisés (em dash → dash ASCII) lors de la cleanup Phase 6.
- **Découverte** : 24-04-2026, standardisation lors de la migration Twin v2 (D-011) ; révisée 26-04-2026 pour intégrer R-043 et bannir l'em dash dans les filenames.

#### R-043 : Cohérence stricte filename ↔ frontmatter `title`

- **Portée** : Brain (manuels de BDD, notes de concept, WR-RD, méthodes, prompts, logic blocks, etc.)
- **Statut** : Actif
- **Why** : Le `title` du frontmatter est la **source canonique de l'identité** du doc ; le nom de fichier doit refléter cette identité pour permettre une navigation cohérente, des liens cross-doc fiables et une lecture sans ambiguïté entre l'ouverture du fichier et son frontmatter. Un mismatch fichier ↔ title est une dette documentaire silencieuse.
- **How to apply** :
  - Pour tout doc Brain (hors taxonomies, voir exception ci-dessous), le nom de fichier doit être **strictement** la valeur du champ `title` du frontmatter, suivie de l'extension `.md`.
  - Si le `title` contient un caractère interdit en filename Windows (`<>:"/\|?*`), remplacer le caractère par `-` (cas standard `/` → ` - `) **dans le filename uniquement** ; le `title` du frontmatter conserve la formulation canonique.
  - Toute modification de `title` doit déclencher un renommage du fichier ; tout renommage de fichier doit être précédé d'une modification du `title` cohérente.
- **Exception : taxonomies** : le nom de fichier d'une taxonomie porte le `namespace_code` (ex: `ACT.IMPACT_DOMAIN.LBP.md`), pas le title. Le title humain reste lisible dans le frontmatter.
- **Exemples** :
  - ✅ Fichier `Concept - Actif.md` ↔ `title: "Concept - Actif"` dans le frontmatter.
  - ✅ Fichier `Concept - Input - Output (LBP).md` ↔ `title: "Concept - Input / Output (LBP)"` (le `/` est autorisé dans le title, remplacé par ` - ` dans le filename).
  - ❌ Fichier `BDD - AGENTS LBP.md` ↔ `title: "Manuel de BDD - Agents LBP"` (mismatch ; à corriger en renommant le fichier).
- **Conséquence si violation** : navigation incohérente (le titre vu en haut du doc diffère du nom dans l'arborescence), liens cross-doc fragiles, perte de confiance dans l'identité des fichiers.
- **Découverte** : 26-04-2026, Leonard, après audit de 114 mismatches dans le vault (manuels Brain en `BDD - X` au lieu de `Manuel de BDD - X`, notes en `concept - X` au lieu de `Concept - X`, manuels Twin avec em dash dans le title).

### 2.10 Relations inter-BDD Brain

*Section à remplir quand on formalisera les règles de relations (hub-spoke, miroirs, bidirectionnalité...).*

### 2.8 Hiérarchies et héritage

*Section à remplir quand on clarifiera les patterns d'héritage (notes de concept ← glossaire, manuels ← taxonomies, etc.).*

### 2.9 Docs WR-RD (Write Rules / Read Keys)

*Règles propres aux docs WR-RD dérivés des manuels de BDD. Voir D-014 (colocalisation), D-016 (rôle, contenu et format), Template - WR-RD - Digital Twin (v1.2.0+).*

#### R-041 : Propagation Manuel de BDD → WR-RD obligatoire

- **Portée** : Brain (toute BDD ayant un WR-RD instancié)
- **Statut** : Actif
- **Why** : Le WR-RD est une **projection stricte** de la section 4 du manuel parent (D-016). Si une propriété change dans le manuel (création, suppression, modification de Type, Cardinalité, Taxonomie, Forme logique, Instructions d'écriture, Clefs de lecture, Utilité pour le Digital Twin ou Exemples) sans propagation au WR-RD, alors le WR-RD ment aux agents qui le consomment runtime → erreurs de saisie ou d'interprétation. La direction de propagation est unilatérale : **manuel → WR-RD, jamais l'inverse**.
- **How to apply** :
  - Toute modification d'une propriété en section 4 d'un Manuel de BDD (sous-sections 4.1 à 4.5) déclenche **obligatoirement** la mise à jour du WR-RD correspondant.
  - Pour chaque propriété modifiée, reporter les colonnes retenues dans le WR-RD : Champ, Type, Taxonomie(s) - codes, Cardinalité / multiplicité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité pour le Digital Twin, Exemples.
  - Bumper la version du WR-RD (`version` dans frontmatter) et son `template_version` si le template a évolué.
  - Le WR-RD ne doit **jamais** être édité indépendamment du manuel parent : si une formulation pose problème dans le WR-RD, corriger d'abord le manuel parent puis re-projeter.
  - À l'inverse : aucune modification du WR-RD ne doit remonter "à reculons" dans le manuel sans passer par une décision éditoriale explicite côté manuel.
- **Outillage suggéré** : à terme, un script de génération automatique du WR-RD à partir du manuel parent (extraction des 9 colonnes des sous-sections 4.1 à 4.5). Phase 6 / 6bis.
- **Conséquence si violation** : WR-RD désaligné = agents qui produisent des données non conformes au manuel = pollution silencieuse du Twin client. À détecter au plus tôt par audit régulier.
- **Découverte** : 26-04-2026, Leonard, après instanciation des 3 premiers WR-RD (Actifs, Pratiques organisationnelles, Journal des signaux).

#### R-042 : QA stricte d'égalité entre WR-RD et section 4 du manuel parent

- **Portée** : Brain (toute génération ou modification d'un WR-RD)
- **Statut** : Actif
- **Why** : Le WR-RD étant une projection stricte (D-016, R-041), tout écart entre le contenu d'une cellule du WR-RD et la cellule correspondante du manuel parent constitue une **dérive éditoriale** silencieuse. Une instruction d'écriture reformulée "pour faire mieux" dans le WR-RD est une violation : le canon est dans le manuel.
- **How to apply** :
  - À la génération ou à la modification d'un WR-RD, vérifier que **chaque cellule** des 9 colonnes retenues est **mot pour mot identique** à la cellule correspondante du manuel parent (sections 4.1 à 4.5, colonnes : Champ, Type, Taxonomie(s) - codes, Cardinalité / multiplicité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité pour le Digital Twin, Exemples).
  - Tolérances admises : adaptations purement typographiques inévitables au transfert Markdown (apostrophe droite vs typographique si le rendu force une normalisation) - à signaler dans les `Logs / Révisions` du WR-RD si appliquées.
  - Si une instruction d'écriture ou clef de lecture est jugée mal formulée dans le manuel, **corriger d'abord le manuel parent** puis re-projeter vers le WR-RD (cohérent avec R-041).
- **Contrôle** : avant tout commit / publication d'un WR-RD, faire un diff avec la section 4 du manuel parent sur les 9 colonnes retenues. Aucun écart non-typographique ne doit subsister.
- **Outillage suggéré** : script de diff automatique manuel ↔ WR-RD à terme, avec alerte sur les cellules divergentes.
- **Conséquence si violation** : voir R-041 - désalignement silencieux entre les deux artefacts, lecture incohérente côté agents et humains.
- **Découverte** : 26-04-2026, Leonard, après les 3 premiers WR-RD instanciés.

---

## 3. Règles Digital Twin

*Règles spécifiques à la gouvernance des BDD instanciées du Digital Twin. Source principale : Panorama V2 v3 (22-04-2026).*

### 3.1 Ontologie des objets

#### R-011 : Frontières fortes entre objets canoniques

- **Portée** : Twin
- **Statut** : Actif
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
- **Exemples** : ✅ Une équipe produit = Collectif ; SA TotalEnergies = Organisation / ❌ "Équipe ABC (SA)" dans Organisations
- **Découverte** : Panorama V2 v3, §3.2

#### R-012 : Séparation des 4 régimes de connaissance

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Éviter les glissements entre symptôme et diagnostic, la sur-interprétation du brut, la confusion entre vu/pensé/décidé.
- **How to apply** : Tout contenu du Twin relève d'un des 4 régimes, à ne jamais mélanger :
  1. **Preuve source** : observé, documenté, cité, transcrit
  2. **Qualification structurée** : typé, relié, mis en forme
  3. **Consolidation analytique** : stabilisé comme objet de lecture/diagnostic
  4. **Pilotage / action** : oriente, mesure, transforme
- **Découverte** : Panorama V2 v3, §3.1

### 3.2 Architecture des BDD

#### R-018 : Spécialisation des propriétés génériques à l'écriture

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Un socle générique commun ne garantit pas une grammaire de remplissage identique. Une description d'individu ne ressemble pas à une description d'actif.
- **How to apply** : Respecter les propriétés génériques communes (Description, Indices observés, Indices d'existence, Commentaires, Merge Notes, Logs) mais appliquer des **instructions d'écriture spécifiques à chaque objet**. Les manuels de BDD portent cette doctrine.
- **Exemples** : ✅ Description d'une problématique = nœud diagnostique consolidé + périmètre + logique centrale ; Description d'un actif = ce que c'est + à quoi il sert + pour qui / ❌ Description uniforme "texte libre 3-10 lignes"
- **Découverte** : Panorama V2 v3, §3.7 et §8.4

#### R-019 : Architecture en 5 couches d'une BDD bien spécifiée

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Homogénéité de design et lisibilité des fiches. Chaque couche répond à une question distincte.
- **How to apply** : Une BDD importante du Twin est pensée comme un empilement cohérent :
  1. **Propriétés génériques** (gouvernance, traçabilité)
  2. **Relations + jumelles textes** (graphe + formulation observée)
  3. **Propriétés spécifiques** (pouvoir explicatif propre)
  4. **Couche 5D** (traversabilité systémique)
  5. **Couche calculée** (rollups + formules)
- **Exemples** : Variantes d'intensité selon famille (registre, socle sémantique, extraction factuelle, socle structurel, post-traitement analytique) - cf. Panorama §9.2
- **Découverte** : Panorama V2 v3, §9.1

### 3.3 Doctrine relationnelle

#### R-013 : Sobriété relationnelle

- **Portée** : Twin
- **Statut** : Actif
- **Why** : La saturation relationnelle rend le graphe illisible et les rollups peu fiables. Les "edges décoratifs" détériorent la valeur analytique.
- **How to apply** : Une relation réelle n'est créée que si elle apporte un gain clair de : compréhension, traversée, consolidation, comparaison, ou diagnostic. Éviter les relations "au cas où" et les raffinements sans gain net.
- **Exemples** : ✅ `Organisation → comprend → Collectif` ; `OKR → est mesuré par → Indicateur` / ❌ Relation décorative "est mentionné par"
- **Découverte** : Panorama V2 v3, §3.3 et §8.1

#### R-014 : Règle absolue des sandboxes

- **Portée** : Twin
- **Statut** : Actif (absolue)
- **Why** : Les sandboxes servent à explorer et pré-consolider sans figer le graphe officiel. Y introduire des relations réelles transformerait la sandbox en BDD parallèle semi-officielle.
- **How to apply** : Une BDD sandbox n'a **jamais** de relations réelles avec les autres BDD du Twin, **à une seule exception** : la relation vers `Sources d'informations`. Les liens se matérialisent uniquement via jumelles textes.
- **Exemples** : ✅ Sandbox Pratiques → jumelle texte "est conduite par (collectifs) (texte)" / ❌ Sandbox Pratiques → relation réelle vers Collectifs
- **Découverte** : Panorama V2 v3, §3.4

#### R-015 : Jumelles textes systématiques

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Préserver la formulation observée dans les sources, permettre la consolidation progressive, garder un indice relationnel avant validation, servir de base de vérification pour humain ou agent.
- **How to apply** : Pour chaque relation réelle dans une BDD officielle, prévoir une **jumelle texte** qui conserve les formulations observées. Exemple : `est conduite par (collectifs) (texte)` accompagne `est conduite par (collectifs)`. Dans une sandbox, **seule la jumelle texte** existe.
- **Découverte** : Panorama V2 v3, §8.2

### 3.4 5D, rollups et formules

#### R-016 : La 5D est une matrice de lecture, jamais une preuve primaire

- **Portée** : Twin
- **Statut** : Actif
- **Why** : La 5D sert à rendre visibles des structures, comparer des objets hétérogènes, synthétiser des traversées. Elle ne remplace pas la preuve, qui reste portée par objets, relations, propriétés spécifiques, sources, indices.
- **How to apply** : Utiliser la 5D pour : contribution, exposition, dépendance, causalité/impact/risque, pilotage/mesure. Ne jamais l'utiliser pour reclassifier les objets ou fonder un diagnostic.
- **Découverte** : Panorama V2 v3, §3.5 et §8.5

#### R-017 : Sobriété des rollups et formules

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Les couches calculées ne sont pas là pour "faire riche". Elles doivent révéler un écart, un profil, une dépendance, une vulnérabilité, ou un état utile à la lecture.
- **How to apply** : Un rollup ou une formule n'est conservé que s'il améliore réellement l'intelligibilité. Jamais de formule décorative. Pas de rollup dans une sandbox sans relations réelles.
- **Exemples** : ✅ Formule `Vulnérabilité nette de l'actif`, rollup `Profils 5D agrégés d'exposition` / ❌ Formule "nombre total de relations"
- **Découverte** : Panorama V2 v3, §3.6, §8.6, §8.7

### 3.5 Traçabilité et gouvernance

#### R-020 : Traçabilité obligatoire des fiches importantes

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Un diagnostic ou une lecture doit toujours pouvoir être relu, questionné, justifié, recontextualisé.
- **How to apply** : Toute fiche importante doit rester **réauditable** via :
  - Sources (relation vers `Sources d'informations`)
  - Indices observés (journal structuré)
  - Indices d'existence de l'objet
  - Logs / Révisions LBP
  - Traces de merge si applicable
- **Découverte** : Panorama V2 v3, §13.2

#### R-023 : Progressivité du remplissage

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Le Twin n'est pas conçu pour être "plein" immédiatement mais densifié progressivement à mesure que la preuve augmente. Imposer une complétude uniforme génère du remplissage artificiel.
- **How to apply** : Toutes les BDD n'ont pas besoin du même niveau de densité au même moment. Ce qui compte : la qualité de ce qui est utile pour la question analytique du moment.
- **Découverte** : Panorama V2 v3, §13.5

#### R-025 : Tableau maître canonique obligatoirement tenu à jour

- **Portée** : Twin
- **Statut** : Actif (absolue)
- **Why** : Le tableau maître est la référence canonique du Twin. Sans lui, l'architecture dérive.
- **How to apply** :
  - Toute création de BDD doit être ajoutée au tableau maître
  - Toute suppression doit y être arbitrée
  - Tout changement de régime architectural doit y être explicité
  - Toute sandbox doit être distinguée de sa BDD officielle cible
- **Découverte** : Panorama V2 v3, §4.3. Tableau maître reproduit dans `refs/SPECS_ARCHITECTURE_TWIN_LBP.md`.

### 3.6 Lecture et traversées

#### R-024 : Lecture du Twin sur 3 niveaux simultanés

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Le Twin n'est pas un entrepôt mais une machine de lecture systémique. Séparer les 3 niveaux évite les lectures faussement sûres.
- **How to apply** : Toute traversée/analyse doit articuler :
  1. **Niveau 1 - ce qui existe** : objets, acteurs, supports, contextes, temps
  2. **Niveau 2 - ce qui se passe** : actions, pratiques, processus, signaux, enjeux, transformations
  3. **Niveau 3 - ce que cela signifie et ce qu'il faut en faire** : problématiques, capacités, principes, modulateurs, OKR, indicateurs
- **Découverte** : Panorama V2 v3, §14.3

### 3.7 Génération des BDD Twin sur Notion

#### R-045 : Source de vérité pour la génération d'une BDD = Manuel parent

- **Portée** : Twin (génération initiale ou refonte d'une BDD Notion)
- **Statut** : Actif
- **Why** : Le manuel a 12 colonnes (vs 9 dans le WR-RD) - notamment **Portée**, **Nature de production** (Saisie / Calculé / Dérivé) et **Forme logique** détaillée. Ces champs sont indispensables pour générer correctement (ex. distinguer une formule d'une saisie, une relation native d'une jumelle texte, un rollup d'une propriété directe). Le WR-RD est une projection runtime, pas un canon de génération.
- **How to apply** : Toute génération de BDD Notion ou refonte de schéma repose strictement sur la section 4 du manuel parent (4.1 à 4.5). Le WR-RD n'est consulté qu'en runtime par les agents. Si un écart apparaît entre manuel et WR-RD, c'est le manuel qui prime (cohérent avec R-041 / R-042).
- **Découverte** : 26-04-2026, Phase 6.5 - préparation génération des 28 BDD Twin v2 sur Notion.

#### R-046 : Ordre de création des éléments d'une BDD sur Notion

- **Portée** : Twin (toute création de BDD ou ajout massif de propriétés relationnelles/calculées)
- **Statut** : Actif
- **Why** : Les contraintes Notion impliquent des dépendances strictes :
  - une **relation bidirectionnelle** ne peut exister que si les deux BDD cibles existent
  - un **rollup** ne peut exister que si la relation source qu'il agrège existe
  - une **propriété multi-select avec taxonomie** doit avoir ses options peuplées au moment de la création (sinon Notion les crée à la volée à partir du contenu)
- **How to apply** : Suivre l'ordre suivant pour générer un ensemble cohérent de BDD :
  1. **Créer toutes les BDD vides** (pleine page sous la page hôte) - uniquement le titre
  2. **Ajouter les propriétés natives non-relationnelles** (texte, sélection, multi-sélection avec valeurs taxonomiques peuplées, date, number) dans l'ordre d'ordering R-047
  3. **Créer les relations bidirectionnelles** (les 2 BDD existent désormais) ; cas particulier : `Sources d'informations` est le seul lien **monodirectionnel** (le Twin référence Sources sans miroir côté Sources)
  4. **Créer les rollups** (les relations sources existent désormais)
  5. **Réordonner les propriétés** selon R-047 si l'ordre s'est dégradé après ajouts post-création
- **Exception monodirectionnalité** : la relation `Source(s) d'information` côté Twin est mono - pas de propriété miroir côté Sources d'informations.
- **Découverte** : 26-04-2026, Leonard, Phase 6.5.

#### R-047 : Convention d'ordering des propriétés Notion (Twin)

- **Portée** : Twin (toute BDD du Digital Twin)
- **Statut** : Actif
- **Why** : Lisibilité des fiches dans Notion. Les propriétés métier importantes doivent rester en haut ; les propriétés de gouvernance / journal / traçabilité, peu consultées au quotidien, sont reléguées en bas. Cohérence visuelle entre les 28 BDD Twin.
- **How to apply** : **Sept blocs séquentiels** (ordre R-047 v2.2, révisée 27-04-2026 après pilote Actifs) :
  1. **Bloc 1 - Tête générique** (5 props, ordre fixe) : `Nom` · `Statut de l'objet` · `Aliases` · `Erreurs de transcription` (conditionnelle, présente uniquement si dans le manuel) · `Description`.
  2. **Bloc 2 - Corpus métier**, avec **ordre interne strict** :
     - **2a. Propriétés spécifiques** (4.2)
     - **2b. Couche 5D** regroupée intégralement (4.4 - natives + jumelles 5D si existent)
     - **2c. Jumelles textes seules** (4.3 jumelles uniquement, **sans les relations**)
     - **2d. Calculés natifs** (4.5 hors rollups relationnels) - formules locales.
  3. **Bloc 3 - Queue générique** (~11-12 props, ordre fixe) : `Lien vers la note avancée` (URL, conditionnelle, R-050) · `Exemples concrets` · `Commentaires libres` · `Notes du consultant` · `Confidentialité (option)` (conditionnelle) · `Indices observés` · `Indices d'existence de l'objet` · `Created Date` · `Last Updated Date` · `Logs / Révisions LBP` · `Merge Notes` · `Merge Flags`
  4. **Bloc 4 - Sources textuelles** (1 prop) : `Source(s) d'information (texte)` (RICH_TEXT). La relation monodirectionnelle `Source(s) d'information` est différée (création de la BDD `Sources d'informations` plus tard sur la même page Notion).
  5. **Bloc 5 - Relations sortantes** (Passe 2 globale, après que les 28 BDD ont leur Passe 1 finie) : toutes les relations bidirectionnelles documentées en 4.3, créées via `RELATION('target_ds', DUAL 'mirror_name' 'mirror_id')`. Notion crée automatiquement les miroirs côté BDD cibles (qui apparaîtront en bloc 7 côté cible).
  6. **Bloc 6 - Rollups & couche calculée relationnelle** (Passe 3 globale, après les relations) : tous les rollups documentés en 4.3 et 4.5.
  7. **Bloc 7 - Miroirs reçus** (créés automatiquement par Notion lors de la Passe 2 des **autres** BDD) : propriétés relation miroir des relations bidir entrantes. Ces props apparaissent en bout de schéma au moment où une autre BDD nous référence.
- **Renommage des natives Notion** : `Created Date` et `Last Updated Date` réutilisent les propriétés natives Notion `Created time` / `Last edited time` mais sont **renommées** pour rester cohérent avec la nomenclature des manuels.
- **Justification doctrinale du décalage relations/rollups en queue (Bloc 5+)** : sémantiquement défendable - relations et rollups forment la **couche calculée et le graphe dérivé** (lecture analytique secondaire), pas une saisie directe par humain. Les voir en bout de schéma signale visuellement leur nature dérivée et complète la lecture `[Identité] → [Substance métier] → [Gestion] → [Traçabilité sources] → [Graphe + Couche calculée]`.
- **Justification du découplage jumelle ↔ relation (R-047 v2.2)** : le couplage par paires (R-047 v2) garantissait l'adjacence jumelle+relation **sur la BDD courante**, mais polluait toutes les autres BDD avec un miroir prématuré (avant que leurs propres props natives ne soient créées), cassant leur ordering futur. Le découplage (jumelle en Passe 1, relation en Passe 2 globale) sacrifie l'adjacence locale au profit d'un **ordering global cohérent sur les 28 BDD**. Trade-off accepté.
- **Découverte** : 26-04-2026, Leonard, Phase 6.5. **R-047 v2 (27-04-2026)** : Bloc 1 ordonné (Statut avant Aliases), couplage jumelles+relations, Bloc 5 rollups en queue. **R-047 v2.1 (27-04-2026)** : ajout `Lien vers la note avancée` en tête Bloc 3. **R-047 v2.2 (27-04-2026)** : découplage jumelles+relations (jumelles seules en Bloc 2c Passe 1, relations en Bloc 5 Passe 2 globale), ajout Bloc 6 rollups + Bloc 7 miroirs reçus.

#### R-048 : Naming d'une BDD Notion = nom canonique simple

- **Portée** : Twin
- **Statut** : Actif
- **Why** : La BDD Notion représente l'objet métier (ex. `Actifs`), pas le doc qui le décrit (`Manuel de BDD - Actifs.md`). Confondre les deux dans le titre Notion crée une confusion durable et casse la cohérence avec les manuels qui pointent vers la BDD via `Nom de la BDD Notion`.
- **How to apply** : Le titre d'une BDD Notion = **nom canonique simple** au pluriel et avec accents (ex. `Actifs`, `Collectifs`, `Pratiques organisationnelles`, `Événements`, `Problématiques sandbox`). Aucun préfixe `Manuel de BDD - `, aucun suffixe descriptif. Le nom canonique du manuel et le titre de la BDD doivent matcher 1:1.
- **Exemples** : ✅ `Actifs` / ❌ `Manuel de BDD - Actifs` / ❌ `BDD Actifs Twin v2`
- **Découverte** : 26-04-2026, Leonard, Phase 6.5.

#### R-049 : Déclaration obligatoire de la `ui_family` pour toute BDD Twin

- **Portée** : Twin
- **Statut** : Actif
- **Why** : D-017 a adopté un prisme `ui_family` orienté utilisateur (app LBP) en 7 valeurs (Langage, Structure, Cadres, Moteur, Pilotage, Ancrages, Objets candidats). Sans déclaration explicite et systématique de cette famille pour chaque BDD, l'app et le Brain peuvent diverger silencieusement, ce qui casse la cohérence UX/source de vérité.
- **How to apply** : Toute BDD du Twin (officielle ou sandbox) doit déclarer son `ui_family` dans :
  1. **Frontmatter du manuel parent** (champ `ui_family` parmi les 7 valeurs canoniques). Ex. : `ui_family: "Structure"`.
  2. **Registre Notion `Manuels de BDD`** (propriété select `Famille UI` avec les 7 valeurs).
  3. **bdd_registry.json** (Phase 6.5 et artefacts ultérieurs de génération) : champ `ui_family`.
  4. **Nouvelle BDD** : la déclaration `ui_family` est obligatoire dès la création du manuel parent ; aucune BDD ne peut être indexée Notion sans ce champ.
- **Valeurs canoniques** (strictes, casse exacte) : `Langage`, `Structure`, `Cadres`, `Moteur`, `Pilotage`, `Ancrages`, `Objets candidats`.
- **Note** : `Objets candidats` est en **2 mots** intentionnellement (les 6 autres sont en 1 mot). Cette dissonance typographique signale que cette famille n'est pas un prisme de l'entreprise comme les autres, mais un **statut d'objet** (en cours de qualification). Détail dans D-017.
- **Hors scope** : les WR-RD ne portent **pas** ce champ (le WR-RD est un artefact runtime agent ; l'UX n'est pas son rôle).
- **Exemples** :
  - ✅ `ui_family: "Structure"` (Organisations, Collectifs, Postes, Individus, Relations inter-organisations)
  - ✅ `ui_family: "Objets candidats"` (toutes les sandboxes)
  - ❌ `ui_family: "objets candidats"` (casse non canonique - la 1ère lettre doit être majuscule)
  - ❌ `ui_family: "Sandboxes"` (valeur non canonique)
  - ❌ `ui_family: "Candidats"` (valeur non canonique - `Candidats` seul a été écarté car ambigu, voir D-017)
  - ❌ `ui_family: "Lab"` (valeur initiale temporaire abandonnée le 27-04-2026)

#### R-051 : Ordering des propriétés Notion via `update_view SHOW` (et non via l'ordre des `ADD COLUMN`)

- **Portée** : Twin (toute génération ou modification d'une BDD Notion)
- **Statut** : Actif
- **Why** : L'ordre des `ADD COLUMN` dans une salve DDL **ne détermine pas** l'ordre d'affichage côté UI Notion. Notion affiche les colonnes selon le tableau `displayProperties` de chaque vue, qui par défaut suit un ordre alphabétique automatique sur les vues nouvellement modifiées (notamment après DROP+ADD). Vouloir préserver l'ordre R-047 v2.2 via l'ordre des ADD COLUMN est donc **vain et coûteux** (chronophage, fragile aux miroirs créés par les relations bidir, exige des passes successives lourdes). La bonne approche : **séparer création des propriétés (ordre indifférent) et ordering UI (1 appel `update_view` final par BDD)**.
- **How to apply** :
  1. Pour la création/ajout de propriétés sur une BDD Notion : utiliser `update_data_source` avec une salve DDL **dans n'importe quel ordre** (peu importe).
  2. Pour configurer l'ordre d'affichage final : appeler `update_view` sur la vue concernée avec la directive `SHOW "prop1", "prop2", ...` listant **toutes** les propriétés visibles dans l'ordre voulu (R-047 v2.2 pour les BDD Twin).
  3. Effectuer cet appel `SHOW` **une seule fois par BDD à la toute fin** du workflow (après Passes natives + relations + rollups + formules + Sources mono), pour éviter de devoir le rappeler à chaque passe intermédiaire.
- **Conséquence sur le workflow** : R-047 v2.2 décrit l'ordre **cible final** ; WF-014 v3 séquence les passes techniques (relations après natives, rollups après relations) ; R-051 garantit que l'ordering UI final est conforme **indépendamment** de l'ordre de création.
- **Effets de bord** : si une nouvelle propriété est créée après le `SHOW` final (ex. ajout d'une relation oubliée), elle apparaît en queue de la vue. Il faut alors relancer `update_view SHOW` pour la repositionner.
- **Outillage suggéré** : générer la liste `SHOW` par BDD à partir du manifest + des règles R-047 v2.2 (ordre fixe Bloc 1 et Bloc 3 ; ordre du manuel pour Bloc 2 ; ordre stable pour Bloc 4 / 5 / 6).
- **Découverte** : 27-04-2026, Leonard, après pilote Actifs - l'IA Notion a démontré qu'elle pouvait réordonner via `displayProperties`, et l'outil MCP `notion-update-view` expose la même capacité via la directive `SHOW`. Test concluant sur `_TEST_ORDRE` et Actifs.

#### R-050 : Propriété conditionnelle `Lien vers la note avancée` (URL)

- **Portée** : Twin (BDD à objets stabilisés)
- **Statut** : Actif
- **Why** : Compléter l'identité structurée d'un objet par un **lien vers une note approfondie** (Brick de connaissance générée via les Templates de Bricks LBP). Cela donne aux agents et consultants un canal d'approfondissement narratif (profil avancé d'un individu, d'une organisation, d'un actif, etc.) qui complète les propriétés structurées sans alourdir la fiche. Cf. D-018 pour le lien doctrinal Bricks ↔ Notes avancées.
- **How to apply** :
  1. **Type Notion** : URL.
  2. **Position dans le schéma** : tête du Bloc 3 (queue générique), juste avant `Exemples concrets` (R-047 v2.1).
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
- **Exemples** : ✅ `https://notion.so/Profil-Organisationnel-Numalis-...` / ❌ propriété présente sur fiche `OKR sandbox` (sandbox = exclu).
- **Découverte** : 27-04-2026, Leonard, Phase 6.5 - propriété oubliée lors de la refonte Twin v2 et redécouverte au moment d'attaquer la Phase 3 propriétés natives. Présente dans l'ancien template (archivé `00 - archives/template-db-manual.md`, ligne 353) sous le nom `Lien vers la note avancée`.
- **Découverte** : 27-04-2026, Leonard, après mise en place visuelle sur la page Notion `BDD test - 26/04/2026 - Digital Twin update`.

---

## 4. Règles Mission Ops

*Règles spécifiques à la gouvernance de Mission Ops.*

### 4.1 Instanciation

*Section à remplir.*

### 4.2 Relations Twin ↔ Mission Ops

*Section à remplir - notamment la règle de monodirectionnalité Mission Ops → Twin sans miroir.*

---

## 5. Règles de propagation d'impacts

*Règles qui décrivent comment propager un changement à travers l'écosystème.*

### 5.1 Renommage d'un objet

*Section à remplir quand on traitera ressources→actifs, rôles officiels→postes, etc.*

### 5.2 Suppression / archivage d'une BDD

*Section à remplir quand on traitera l'archivage de l'ancienne UO.*

### 5.3 Modification d'une taxonomie

*Section à remplir.*

### 5.4 Mise à jour d'un template

*Section à remplir.*

### 5.5 Mise à jour d'un manuel de BDD

#### R-028 : Cohérence manuel ↔ doc clefs de lecture

- **Portée** : Brain (propagation vers docs dérivés)
- **Statut** : Actif
- **Why** : Le doc *Instructions d'écriture & clefs de lecture* d'une BDD est **dérivé** du manuel de BDD correspondant. Une asymétrie entre les deux produit des agents qui écrivent/lisent différemment de la spec, et des incohérences dans le Twin.
- **How to apply** : Le **manuel de BDD est source de vérité**. À chaque mise à jour d'un manuel :
  1. Identifier le doc clefs de lecture correspondant dans `Architecture data/Clefs de lectures/TWIN - Instructions écriture + clefs de lecture/`
  2. Vérifier la cohérence (champs, instructions d'écriture, clefs de lecture, taxonomies référencées)
  3. Mettre à jour le doc dérivé si asymétrie
  4. Consigner la MAJ dans les logs du doc dérivé
- **Exemples** : ✅ On renomme le champ "Rôles officiels" en "Postes" dans le manuel → on met à jour `écriture + lecture - Rôles officiels.md` (ou on le renomme/recrée en `Postes`) / ❌ On modifie un manuel sans vérifier le doc dérivé
- **Découverte** : 24-04-2026, confirmé par Leonard

### 5.6 Consolidation et promotion (sandbox → officielle)

#### R-021 : Distinction stricte fusionner / consolider / promouvoir

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Ces trois opérations sont fondamentalement différentes. Les confondre produit des décisions mal arbitrées et des graphes incohérents.
- **How to apply** : Distinguer systématiquement :
  - **Fusionner** : plusieurs fiches désignent réellement le même objet → merge (au sein d'une même BDD)
  - **Consolider** : plusieurs entrées amont convergent vers un objet plus structuré (signaux → enjeu, enjeux → problématique, actions → processus candidat, actions → pratique)
  - **Promouvoir** : une entrée sandbox devient une BDD officielle
- **Exemples** : ✅ "Fusion" dans Merge Notes d'une BDD ; "Consolidation" dans le passage Journal des signaux → Enjeux / ❌ Parler de "fusion" pour une promotion sandbox
- **Découverte** : Panorama V2 v3, §13.3

#### R-022 : Critères minimaux de promotion sandbox → BDD officielle

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Éviter les promotions trop précoces qui polluent le graphe officiel.
- **How to apply** : Une promotion est autorisée uniquement si tous les critères suivants sont remplis :
  1. **Preuves suffisantes** (indices observés + indices d'existence)
  2. **Formulation stabilisée**
  3. **Absence de confusion majeure** avec un objet déjà existant
  4. **Valeur analytique nette** attendue après promotion
  5. **Cohérence avec la frontière conceptuelle** de la BDD cible
- **Découverte** : Panorama V2 v3, §13.4

---

### 5.7 Hygiène typographique

#### R-061 : Préférer les tirets simples `-` aux tirets cadratins `-`

- **Portée** : Transverse à tout l'écosystème LBP - vault Markdown (titres, noms canoniques, corps des docs), fiches Notion (Nom canonique, Description, autres champs textuels), tout texte affiché. Concerne aussi bien le scope LBP que le scope Session.
- **Statut** : Actif
- **Why** : Les caractères cadratins `-` (U+2014) et demi-cadratins `-` (U+2013) ne sont pas directement accessibles au clavier français de Leonard. Leur saisie ralentit la production de docs. Ils créent aussi des asymétries dans les recherches (un grep `-` ne retrouve pas un `-`). Le tiret simple `-` (U+002D) est universellement disponible, lisible et rétro-compatible.
- **How to apply** :
  - Dans tout texte produit (docs Markdown, fiches Notion, frontmatter, commits) : utiliser `-` (U+002D) à la place de `-` ou `-`.
  - Pour les usages typographiques où un tiret long est sémantiquement attendu (incise, énumération), utiliser `-` simple suivi/précédé d'un espace : `Texte - incise - suite` au lieu de `Texte - incise - suite`.
  - Si on hérite d'un doc avec des `-` (ex. fichiers archivés ou import de doc tiers) : migration au fil de l'eau (sed `-` → `-`) lors de la prochaine modification.
- **Hors scope (à conserver)** :
  - **Flèches** `→` (U+2192), `↔` (U+2194), `↕` (U+2195), `←` (U+2190) : sémantiquement non substituables (schémas techniques, articulations doctrinales). Conservées.
  - **Apostrophes typographiques** `'` (U+2019) : restent obligatoires (R-052, indépendant).
  - **Symboles techniques** `≥`, `≤`, `≠`, `±`, `°`, etc. : conservés si pertinents.
- **Articulation** :
  - Extension de **C-010** (préférer caractères latins simples accessibles au clavier).
  - Complémentaire à **R-052** (apostrophes typographiques obligatoires) : R-052 et R-061 traitent de caractères différents avec des doctrines différentes (cadratin = à éviter, apostrophe typographique = à préférer).
- **Exemples** :
  - ✅ `Panorama LBP - Macro-architecture de l'écosystème` (titre fiche Notion)
  - ✅ `R-061 - Préférer les tirets simples` (titre section)
  - ✅ `Brain → Twin` (flèche conservée)
  - ❌ `Panorama LBP - Macro-architecture` (cadratin)
  - ❌ `R-061 - Préférer` (cadratin)
- **Découverte** : 01-05-2026, Leonard, lors de la création de la 1ère fiche Notion du bundle docs méta (`CHRT_PANORAMA_LBP`) - confirmation explicite « on n'utilise plus de tirets `-`, on utilise `-` à la place ».

---

## 6. À classer (inbox)

*Zone tampon pour les règles qui émergent mais dont la section définitive n'est pas encore évidente. À reclasser régulièrement.*

*(vide pour l'instant)*

---

## Annexe : règles archivées

*Règles qui ne sont plus actives, conservées pour traçabilité.*

*(vide pour l'instant)*
