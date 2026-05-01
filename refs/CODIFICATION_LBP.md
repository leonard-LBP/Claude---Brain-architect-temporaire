---
# === Identité ===
title: "Codification LBP - Grammaire des codes (Brain + Twin + Mission Ops + IDs systèmes)"
doc_type: doc_meta
code: "CHRT_CODIFICATION_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
created_at: "01-05-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Référence canonique de toutes les codifications LBP (R-054 + extensions Twin/MO + IDs systèmes R-XXX/D-XXX/WF-XXX/C-XXX). 4 grammaires : G1 général Brain, G2 taxonomies, G3 bricks instanciées MO, G4 occurrences MO. Table officielle des préfixes Brain. Anti-patterns + arbitrages en cours."
purpose: "Servir de référence pour toute production de code nouveau dans LBP. Évite les préfixes ad hoc qui produisent des asymétries silencieuses. Documente les conventions de codification universelle."
tags:
  - doc_meta
  - codification
  - codes
  - grammaire
  - r054
  - brain
  - digital_twin
  - mission_ops
  - lbp
---

# CODIFICATION - Grammaire des codes LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> Référence canonique de **toutes les codifications** utilisées dans LBP : objets Brain, objets Twin, occurrences Mission Ops, taxonomies, IDs systèmes (R-XXX / D-XXX / WF-XXX / C-XXX).
> Ce doc rassemble et explicite la grammaire officielle issue de **R-054** (RULES_LBP) + ses extensions Mission Ops + IDs systèmes.
> Dernière mise à jour : 30-04-2026 - création post-audit refs/.

---

## 1. Préambule - pourquoi une grammaire unifiée ?

### Le problème historique

Avant R-054, les codes LBP coexistaient en **6+ conventions différentes** (`DBMAN_X`, `CPT.X.LBP.Y`, `OBJ.STATUT.LBP`, `TPL_BRICK_X`, `METH_X`, etc.) avec mix de séparateurs (`_`, `.`, `-`) et suffix `LBP` parfois présent, parfois absent. Beaucoup de docs n'avaient aucun code.

**Conséquences** : les agents de maintenance et d'exploitation ne pouvaient ni filtrer fiable par regex ni vérifier l'unicité cross-écosystème ni tracer les lignées template → instance.

### Le principe directeur

**Tout objet de l'écosystème LBP porte un code stable et déterministe**, conforme à l'une des **4 grammaires** définies ci-dessous selon son type. Le code vit dans le frontmatter du doc Markdown source de vérité (R-001), et est miroiré dans Notion (R-029).

### Les 4 grammaires

| # | Grammaire | Périmètre | Exemple |
|---|---|---|---|
| **G1** | `<PREFIXE>_<IDENTIFIANT>` | Objets Brain (général) | `DBMAN_TW_ACTIFS`, `CPT_SOFT_SKILL`, `METH_CARTE_CAUSALITE` |
| **G2** | `<NAMESPACE>.<TAXO>` | Taxonomies | `OBJ.STATUT`, `BRICK.FAMILY`, `ORG5D.DIM` |
| **G3** | `BRK_<mission_code>_<brick_code>_<discriminant>_<rev>` | Bricks instanciées (Mission Ops) | `BRK_dsai-01_PRF-ORG_DEEPSECAI_R01` |
| **G4** | `<PREFIXE>_<IDENTIFIANT>` (occurrences MO) | Occurrences Mission Ops | `SRC_NUM_M02_ENTRETIEN_CFO`, `MTG_ATELIER_2026-04-25` |

---

## 2. Grammaire 1 - Format général (Brain)

```
<PREFIXE>_<IDENTIFIANT>
```

- `<PREFIXE>` : 2-7 chars MAJUSCULES, identifie le type de doc selon la **table officielle** ci-dessous.
- `<IDENTIFIANT>` : alphanumérique MAJUSCULES, slug court issu du nom canonique du doc, séparateur interne `_` autorisé.
- Exemples : `DBMAN_TW_ACTIFS`, `CPT_SOFT_SKILL`, `PRMPT_M_REFACTOR`, `LGBLK_T_PRBC_PRBC`, `METH_CARTE_CAUSALITE`.

### 2.1 Table de préfixes officielle Brain (R-054)

| Préfixe | Type de doc Brain | Taxo de référence | Sous-typage interne | Exemple |
|---|---|---|---|---|
| `DBMAN_TW` | Manuel de BDD (Twin) | `DOC.TYPE` + `DBMAN.SCOPE.TWIN` | - | `DBMAN_TW_ACTIFS` |
| `DBMAN_MO` | Manuel de BDD (Mission Ops) | + `DBMAN.SCOPE.MISSION_OPS` | - | `DBMAN_MO_BRICKS` |
| `DBMAN_BR` | Manuel de BDD (Brain) | + `DBMAN.SCOPE.BRAIN` | - | `DBMAN_BR_PROMPTS_LBP` |
| `WRRD_TW` | WR-RD (Twin) | `DOC.TYPE.WR_RD` + scope | - | `WRRD_TW_ACTIFS` |
| `WRRD_MO` | WR-RD (Mission Ops) | idem | - | `WRRD_MO_BRICKS` |
| `WRRD_BR` | WR-RD (Brain) | idem | - | `WRRD_BR_PROMPTS_LBP` |
| `CPT` | Note de concept | `DOC.TYPE.NOTE_CONCEPT` | - | `CPT_SOFT_SKILL` |
| `GLO` | Entry de glossaire | `DOC.TYPE.GLOSSAIRE_ENTRY` | - | `GLO_SOFT_SKILL` (paire R-031) |
| `TPL` | Template d'instanciation (général) | `DOC.TYPE.TEMPLATE_INSTANCIATION` | - | `TPL_MANUEL_BDD_BRAIN` |
| `TPL_BRICK` | Template de Brick | `DOC.TYPE.TEMPLATE_BRICK` | `BRICK.FAMILY` | `TPL_BRICK_PRF_ORG` |
| `PRMPT_M` | Prompt maître | `DOC.TYPE.PROMPT` | `PROMPT.ARCH_ROLE.PROMPT_MAITRE` | `PRMPT_M_REFACTOR_TWIN` |
| `PRMPT_S` | System prompt | idem | `PROMPT.ARCH_ROLE.SYSTEM_PROMPT` | `PRMPT_S_KONTEXT` |
| `PRMPT_U` | Prompt d'exécution | idem | `PROMPT.ARCH_ROLE.PROMPT_EXECUTION` | `PRMPT_U_GENERATE_PROFIL` |
| `PRMPT_T` | Template prompt | idem | `PROMPT.ARCH_ROLE.TEMPLATE_PROMPT` | `PRMPT_T_BRICK_GENERATION` |
| `LGBLK` | Logic block | `DOC.TYPE.LOGIC_BLOCK` | `LGBLK.FAMILY` | `LGBLK_T_PRBC_PRBC` |
| `METH` | Méthode | `DOC.TYPE.METHODE` | `MET.FAMILY` | `METH_CARTE_CAUSALITE` |
| `CHRT` | Doc méta (charte / doctrine / playbook) | `DOC.TYPE.DOC_META` | `META.FAMILY` (8 valeurs) | `CHRT_NAMING_CONVENTIONS` |
| `AGT` | Agent LBP | `DOC.TYPE.AGENT` | `AGENT.FAMILY` | `AGT_KONTEXT` |
| `OUT` | Outil externe | `DOC.TYPE.OUTIL_EXTERNE` | `OUT.FAMILY` | `OUT_NOTION_API` |

### 2.2 Paire `CPT_*` ↔ `GLO_*` (R-031)

Un concept LBP a **deux fiches en miroir** :
- `Registre des notes de concept` (`CPT_<TOKEN>`) - méta du fichier source
- `Glossaire LBP` (`GLO_<TOKEN>`) - identité + sémantique du concept

Les **deux fiches partagent le même TOKEN** dans leur code (R-031). Exemple : `CPT_SOFT_SKILL` et `GLO_SOFT_SKILL`.

### 2.3 Règles transverses Grammaire 1

- **Stabilité** : un code ne change jamais (R-038). Refonte = nouveau code + archivage de l'ancien (R-053).
- **Unicité cross-écosystème** : pas de collision entre préfixes (un code identifie un type unique).
- **Casse** : `<PREFIXE>` MAJUSCULES strict. `<IDENTIFIANT>` MAJUSCULES strict, séparateur `_`.
- **Pas de suffix `LBP`** : R-054 a éliminé ce suffix (héritage legacy).

---

## 3. Grammaire 2 - Taxonomies

```
<NAMESPACE>.<TAXO>
```

- `<NAMESPACE>` : MAJUSCULES, regroupe une famille de taxos (ex. `DOC`, `BRICK`, `OBJ`, `ORG5D`, `OPS`, `MTG`, `META`, etc.)
- `<TAXO>` : MAJUSCULES, nom de la taxonomie spécifique
- Séparateur : `.` (point)
- **Pas de suffix `LBP`** (Phase A4.A 28-04-2026 a migré tous les codes `<X>.<Y>.LBP` vers `<X>.<Y>`)

### 3.1 Exemples de namespaces

| Namespace | Taxos exemples | Domaine d'usage |
|---|---|---|
| `DOC` | `DOC.TYPE`, `DOC.TYPE.WR_RD`, `DOC.TYPE.NOTE_CONCEPT` | Méta-typage des docs Brain |
| `OBJ` | `OBJ.STATUT` | Statut universel des fiches (Brouillon/Validé/À revoir/Archivé) |
| `BRICK` | `BRICK.FAMILY` | Familles de bricks (Profil, Compte-rendu, Analyse, etc.) |
| `ORG5D` | `ORG5D.DIM` (5 dims `category` + 10 sous-dims `taxon`) | Lecture 5D du Twin |
| `MTG` | `MTG.TYPE`, `MTG.FORMAT` | Meetings (entretien/atelier/...; visio/présentiel/hybride) |
| `OPS` | `OPS.STATUS`, `OPS.ACTION_FAMILY`, `OPS.ACTION_ITEM_TYPE`, `OPS.RESPONSIBLE_MAIN` | Pilotage opérationnel MO |
| `PROMPT` | `PROMPT.ARCH_ROLE`, `PROMPT.DEPLOY_STATUS`, `PROMPT.TYPE`, `PROMPT.MODE` | Prompts |
| `LGBLK` | `LGBLK.FAMILY` | Logic blocks |
| `META` | `META.FAMILY` (8 valeurs) | Docs méta |
| `MET` | `MET.FAMILY` | Méthodes |
| `AGENT` | `AGENT.FAMILY` | Agents |
| `OUT` | `OUT.FAMILY` | Outils externes |
| `JOB` | `JOB.COVERAGE` | Postes Twin (couverture du poste) |
| `DBMAN` | `DBMAN.SCOPE` (TWIN/MISSION_OPS/BRAIN) | Scope des manuels |

### 3.2 Niveaux dans une taxonomie

Une taxonomie peut avoir plusieurs **niveaux** (R-049 + frontmatter taxo) :
- `category` : niveau le plus haut (ex. ORG5D : 5 dimensions Profil orga / Collectif / Individu / TI / Connexion env)
- `subdomain` : niveau intermédiaire
- `taxon` : niveau le plus bas (ex. ORG5D : 10 sous-dimensions Culture / Structure / ... / Écosystème externe)

La taxo elle-même déclare quels niveaux sont autorisés via `Niveaux autorisés` (multi-select).

### 3.3 Mode de sélection

Une taxo est `mono` (un seul taxon par fiche) ou `multi` (plusieurs taxons possibles). Déclaré dans le frontmatter de la taxo + miroiré dans Notion.

---

## 4. Grammaire 3 - Bricks instanciées (Mission Ops)

```
BRK_<mission_code>_<brick_code>_<discriminant>_<rev>
```

C'est la grammaire la plus structurée, utilisée pour les bricks instanciées par Mission Ops (D-018). Ses 4 segments éclatés sont stockés en propriétés Notion séparées (`mission_code`, `brick_code`, `Discriminant`, `rev`) en plus du Brick ID complet.

### 4.1 Détail des segments

| Segment | Format | Description | Exemple |
|---|---|---|---|
| `BRK` | Préfixe fixe | Identifie un objet « brick » (cohérent avec G1 par ailleurs) | `BRK` |
| `<mission_code>` | `<client_code>-<NN>` | Code de mission (slug client + numéro 2 chiffres) | `dsai-01`, `num-03` |
| `<brick_code>` | `<TYPE>-<SOUS_TYPE>` ou `<TYPE>` | Code logique de la famille/type de brick | `PRF-ORG`, `MTG-INT-IND-CR` |
| `<discriminant>` | Slug MAJUSCULES | Objet/contexte/occurrence visée | `DEEPSECAI`, `MAYA-2026-04-22` |
| `<rev>` | `R<NN>` | Révision au format `R01`, `R02`, ... | `R01` |

### 4.2 Exemple complet

`BRK_dsai-01_PRF-ORG_DEEPSECAI_R01`

- mission `dsai-01`
- brick code `PRF-ORG` (profil organisationnel)
- discriminant `DEEPSECAI` (l'objet du profil)
- révision `R01`

### 4.3 Règles spécifiques

- **Nom du fichier** = Brick ID **sans extension** (Brick ID = nom fichier sans `.md`).
- **Casse mixte** tolérée pour `<mission_code>` (`dsai-01` reste lisible) mais MAJUSCULES pour les autres segments.
- **Cohérence** : `Version` (Notion) = `<rev>` du Brick ID. Une nouvelle version crée une **nouvelle fiche** (pas de remplacement).
- **Lien drive** stable : URL du fichier `.md` dans le Drive de mission.

### 4.4 Codes de famille/type bricks observés

| Brick code | Famille | Usage |
|---|---|---|
| `PRF-ORG` | Profil | Profil organisationnel |
| `MTG-INT-IND-CR` | Compte-rendu | CR interne LBP d'un entretien individuel |
| `MTG-ATL-CR` | Compte-rendu | CR d'atelier collaboratif |
| `ANL-3P` | Analyse | Analyse 3P (Principes / Pratiques / pression) |
| `LIV-RESTIT` | Livrable | Livrable de restitution client |

(à compléter au fur et à mesure des templates créés)

---

## 5. Grammaire 4 - Codes d'occurrence Mission Ops

Pour les occurrences Mission Ops (Sources, Meetings, Actions LBP), **R-054 prévoit en Phase 2** une extension avec des préfixes dédiés. Pendant la Phase B test (30-04-2026), des codes ad hoc ont été utilisés avec séparateur `-`. À arbitrer (cf. §9 Anti-patterns et arbitrages).

### 5.1 Préfixes proposés (R-054 Phase 2)

| Préfixe | Type | Exemple cible |
|---|---|---|
| `SRC` | Source d'information | `SRC_NUM_M02_ENTRETIEN_CFO` |
| `MTG` | Meeting | `MTG_NUM_M02_KICKOFF1` |
| `ACT` | Action LBP | `ACT_NUM_M02_PREP_KICKOFF` |
| `IND` | Individu (Twin) | `IND_NUM_M02_JDUPONT` |
| `ORG` | Organisation (Twin) | `ORG_NUM_M02_NUMALIS` |
| `ACTF` | Actif (Twin) | `ACTF_NUM_M02_CONTRAT_X` |

### 5.2 Codes ad hoc observés en Phase B test (à arbitrer)

| Type | Code observé | Format | Différence vs R-054 Phase 2 |
|---|---|---|---|
| Source | `SRC-RED-FIRE-001` | `SRC-<TYPE>-<DISCRIMINANT>-<NNN>` | Séparateur `-`, pas de mission_code |
| Meeting | `MTG-ENT-MAYA-2026-04-22` | `MTG-<TYPE>-<DISCRIMINANT>-<DATE-ISO>` | Séparateur `-`, date ISO en suffix |
| Action | `ACT-CR-MAYA-2026-04-22` | `ACT-<DISCRIMINANT>-<DATE-ISO>` | Séparateur `-` |

**À arbitrer** par Leonard avant production : harmoniser sur G1 (`_` séparateur, mission_code obligatoire) ou figer la convention `-` observée comme G4 distincte.

---

## 6. IDs systèmes (règles, décisions, workflows, conventions)

Hors R-054 (qui se concentre sur les objets) - chaque type de capture transverse a son propre ID stable.

### 6.1 Format

| ID | Format | Origine | Lieu |
|---|---|---|---|
| **R-XXX** | `R-` + 3 chiffres (séquentiel) | Règles intrinsèques de l'écosystème LBP | `refs/RULES_LBP.md` |
| **D-XXX** | `D-` + 3 chiffres (séquentiel) | Décisions architecturales | `refs/DECISIONS_LBP.md` |
| **WF-XXX** | `WF-` + 3 chiffres (séquentiel) | Workflows opérationnels | `refs/WORKFLOWS_LBP.md` |
| **C-XXX** | `C-` + 3 chiffres (séquentiel) | Conventions de collaboration Claude/Leonard | `CLAUDE.md` |

### 6.2 Numérotation

- **Séquentielle** dans chaque famille (R-001, R-002, ..., R-060)
- **Stable** une fois attribuée (ne pas réutiliser un numéro retiré)
- **Pas de zéro-padding obligatoire** dans le corps des docs (`R-001` ou `R-1` toléré, `R-001` préféré)

### 6.3 Numérotation actuelle (à date 30-04-2026)

| Famille | Plage | Volume |
|---|---|---|
| R-XXX | R-001 → R-060 | 57 règles |
| D-XXX | D-001 → D-023 | 22 décisions |
| WF-XXX | WF-001 → WF-017 | 8 actifs + 4 à formaliser |
| C-XXX | C-001 → C-019 | 19 conventions |

### 6.4 Articulation entre familles

- Une **D-XXX** peut générer une ou plusieurs **R-XXX** (ex. D-019 → R-058)
- Une **R-XXX** peut s'appuyer sur une **D-XXX** comme justification
- Un **WF-XXX** mobilise plusieurs R-XXX et peut référencer des D-XXX
- Une **C-XXX** est propre à la collaboration Claude/Leonard, hors bundle LBP

---

## 7. Règles transverses de codification

### 7.1 Stabilité (R-038)

Un code ne change **jamais** une fois attribué. Refonte = nouveau code + archivage de l'ancien (R-053). Le code est l'identifiant pivot pour les taxonomies (R-038), distinct du nom canonique pour les autres BDDs Brain.

### 7.2 Archivage (R-053)

Quand un doc est archivé, son fichier est renommé avec le suffix `(archivé v<X> le JJ-MM-YYYY)`. Le code dans le frontmatter reste le même (preserve la traçabilité), mais le doc est marqué `Statut de l'objet: Archivé` côté Notion.

### 7.3 Paire CPT/GLO (R-031)

Voir §2.2. Un concept LBP a 2 codes synchronisés : `CPT_<TOKEN>` et `GLO_<TOKEN>` partagent le même TOKEN.

### 7.4 Identifiant pivot (R-038)

| Type d'objet | Identifiant pivot | Justification |
|---|---|---|
| Taxonomie | `Code unique` (G2) | Code immuable, format strict |
| Manuel de BDD, Note de concept, Glossaire, autres BDD Brain | `Nom canonique` (avec normalisation) | Le nom est plus stable que le code en cas de refonte |

Lors d'une indexation Notion : avant toute création, requêter le registre cible avec le bon champ pivot.

### 7.5 Versioning (R-056)

`<MAJOR>.<MINOR>` - pas de PATCH. Pas de zéro-padding. Bumps significatifs uniquement.

---

## 8. Anti-patterns et arbitrages en cours

### 8.1 Anti-patterns connus

| # | Anti-pattern | Origine | Correctif |
|---|---|---|---|
| 1 | Suffix `LBP` dans les codes (`CPT.X.LBP.Y`, `OBJ.STATUT.LBP`) | Convention legacy pré-R-054 | Migration Phase A4.A 28-04-2026 (96 codes migrés) |
| 2 | Codes Brain dispersés en 6+ conventions | Pré-R-054 | R-054 unifie tout |
| 3 | Confusion `BRK_` (préfixe) vs `BRICK.` (namespace taxo) | - | `BRK` = objet brick (G1, G3) ; `BRICK.FAMILY` = taxo des familles (G2) |
| 4 | Confusion `MTG-XX-DATE` (occurrence MO observée) vs `MTG_XX_NN` (R-054 Phase 2) | Phase B test | À arbitrer (cf. §5.2) |
| 5 | Préfixes inventés ad hoc dans le bundle (`AGENT_`, `MET_`, `META_`, `TPL_BRK_`, `PROMPT_`) au lieu des préfixes officiels (`AGT_`, `METH_`, `CHRT_`, `TPL_BRICK_`, `PRMPT_M/S/U/T`) | Bundle 30-04-2026 (SPECS_BRAIN, SPECS_MO, D-022, D-023) | Correction propagée dans la même unité de travail (cf. §10) |

### 8.2 Arbitrages en cours

1. **Convention de séparateur Mission Ops** : `_` (R-054 G1) ou `-` (observé Phase B) ?
2. **Format des codes d'occurrence Mission Ops** : avec mission_code obligatoire (R-054 Phase 2) ou date ISO en suffix (Phase B test) ?
3. **Préfixes Twin/MO Phase 2 R-054** : à figer formellement dans une mise à jour de R-054.

---

## 9. Anomalies détectées et corrigées dans le bundle

Audit interne du bundle docs méta (30-04-2026) a révélé que les docs récents (`SPECS_ARCHITECTURE_BRAIN_LBP.md`, `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`, `D-023`, `WORKFLOWS_LBP.md`, `ECOSYSTEM-STATE.md`, `TEST_TWIN_OPS_PLAYBOOK.md`) utilisaient des préfixes **inventés ad hoc** non conformes à R-054.

### 9.1 Corrections propagées (30-04-2026)

| Préfixe ad hoc | Préfixe officiel R-054 | Statut |
|---|---|---|
| `META_<TOKEN>` | `CHRT_<TOKEN>` | ✓ corrigé (SPECS_BRAIN §3) |
| `MET_<TOKEN>` | `METH_<TOKEN>` | ✓ corrigé (SPECS_BRAIN §2 §3 §7 §8.2, SPECS_MO §1 §7, WORKFLOWS_LBP §WF-015, ECOSYSTEM-STATE) |
| `TPL_BRK_<TOKEN>` | `TPL_BRICK_<TOKEN>` | ✓ corrigé (SPECS_BRAIN §2 §3 §7 §8.2, SPECS_MO §1 §3.4 §7 §9, DECISIONS_LBP D-023, WORKFLOWS_LBP §WF-015, ECOSYSTEM-STATE, TEST_TWIN_OPS_PLAYBOOK §6.3) |
| `AGENT_<TOKEN>` | `AGT_<TOKEN>` | ✓ corrigé (SPECS_BRAIN §2 §3 §7, SPECS_MO §1 §7, WORKFLOWS_LBP, ECOSYSTEM-STATE) |
| `PROMPT_<TOKEN>` | `PRMPT_M/S/U/T_<TOKEN>` (sous-typé par rôle architectural) | ✓ corrigé (SPECS_BRAIN §2 §3 §7, SPECS_MO §1 §7, WORKFLOWS_LBP, ECOSYSTEM-STATE) |

### 9.2 Cascade WF-008 effectuée

Conformément à WF-008 (propagation d'impacts) :
- Phase 2 : cartographie des dérivés (6 fichiers concernés)
- Phase 3 : propagation Markdown (grep + Edit ciblé sur chaque occurrence)
- Phase 4 : QA (grep final pour vérifier zéro occurrence des préfixes ad hoc dans le bundle durable)
- Phase 5 : annonce explicite (cf. commit message)
- Phase 6 : trace ECOSYSTEM-STATE
- Phase 7 : commit + push (C-013)

### 9.3 Note importante

R-054 (table officielle) reste **la source de vérité**. Les usages divergents historiques dans le bundle ont été corrigés. Toute nouvelle production de codes doit s'appuyer sur ce doc `CODIFICATION_LBP.md` (références dans SPECS_BRAIN, SPECS_MO, WORKFLOWS_LBP, ECOSYSTEM-STATE).

---

## 10. Liens vers la documentation détaillée

### Règles fondatrices

- `refs/RULES_LBP.md` - R-054 (codification universelle), R-031 (paire CPT/GLO), R-038 (identifiant pivot), R-053 (archivage), R-055 (frontmatter 3 zones), R-056 (versioning X.Y)

### Décisions

- `refs/DECISIONS_LBP.md` - D-019 (Brain unifié + isolation), D-021 (3 agents), D-022 (frontmatters Twin/MO différenciés), D-023 (stack Notion/Supabase)

### Workflows

- `refs/WORKFLOWS_LBP.md` - WF-008 (propagation d'impacts), WF-015 (migration au canon), WF-016 (audit transverse), WF-017 (sync DDL)

### Manuels et schémas

- Manuels Brain sous `Manuels de BDD/Brain/` (source de vérité du schéma)
- Manuels MO sous `Manuels de BDD/Mission Ops/`
- Manuels Twin sous `Manuels de BDD/Digital Twin/`
- Taxonomies sous `Taxonomies/` (102 taxos au canon, Phase A4.A)

### Specs architectures

- `refs/SPECS_ARCHITECTURE_BRAIN_LBP.md`
- `refs/SPECS_ARCHITECTURE_TWIN_LBP.md`
- `refs/SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`

---

> Dernière mise à jour : 30-04-2026 - création post-audit refs/. Référence canonique pour toute production de codes nouveaux dans LBP.
