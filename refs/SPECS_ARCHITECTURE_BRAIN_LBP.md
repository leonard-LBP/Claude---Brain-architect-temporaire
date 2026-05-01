---
# === Identité ===
title: "Specs Architecture Brain LBP - Modèle conceptuel des 11 BDDs Brain"
doc_type: doc_meta
code: "CHRT_SPECS_BRAIN_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
template_version: "1.0"
created_at: "07-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Modèle conceptuel des 11 BDDs Brain (4 zones : ADMIN / CORE / MOTOR / CROSS-ZONE), leurs articulations (hub Prompts 6 relations, hub Glossaire 3 relations, paire CPT/GLO, taxos↔manuels, manuels↔WR-RD), architecture logique en couches sobres, articulation Brain → Twin/MO en lecture seule."
purpose: "Servir de référence canonique du modèle Brain pour toute production ou audit. Ne reproduit PAS les schémas DDL Notion volatiles (qui vivent dans les manuels parents Markdown source de vérité, R-001)."
tags:
  - doc_meta
  - specs
  - architecture
  - brain
  - bdd
  - lbp
---

# SPECS - Architecture Brain LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> Référence canonique des **11 BDDs structurelles** du domaine Brain, partagées et stables (pas instanciées par mission).
> Brain est un domaine **co-égal** au Digital Twin et à Mission Ops (cf. D-023). Il porte la **gouvernance documentaire de LBP** : vocabulaire, méthodes, templates, prompts, agents, outils, taxonomies, manuels de BDD.
> **Source de vérité** : les **manuels Brain Markdown** sous `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\` (R-001). Notion est miroir, pas source. Les schémas DDL exacts (champs, casses, options select) vivent dans les manuels parents et leur miroir Notion ; ce fichier porte la vue d'ensemble structurante.
> Dernière mise à jour : 30-04-2026 - refonte conceptuelle (séparation modèle conceptuel durable vs snapshot DDL Notion volatile, retiré du doc bundle).

---

## 1. Préambule - qu'est-ce que le Brain ?

Le **Brain** est la **couche de gouvernance documentaire de LBP**. Il définit le vocabulaire (concepts, taxonomies), les méthodes (3P, etc.), les prompts, les templates de bricks, les agents, les outils, les manuels de BDD et les docs méta qui régissent l'ensemble de l'écosystème.

### Frontières avec les 2 autres domaines

| Domaine | Rôle | Stack cible | Évolution pendant mission |
|---|---|---|---|
| **Brain** | Méta - référentiel doctrinal LBP. Stable, évolue **hors mission**. | Notion (à moyen terme) | ❌ Non (D-019, D-021) |
| **Digital Twin** | Représentation structurée d'une organisation cliente. | Supabase (cible D-023) | ✅ Oui |
| **Mission Ops** | Gouvernance opérationnelle de la mission. | Supabase (cible D-023) | ✅ Oui |

### Principe d'isolation (D-019, D-021)

Le Brain est **autonome et isolé** au niveau modèle de données :
- Aucune relation Notion ne lie directement les BDDs Brain aux BDDs Twin ou MO
- L'héritage se fait via les **Manuels de BDD** (qui décrivent les schémas Twin/MO mais vivent dans le Brain)
- Twin et MO **lisent** le Brain au moment de l'instanciation, mais n'écrivent jamais dedans (D-021 - KONTEXT ⊥ Brain architect)

### Régime documentaire

Brain est de régime **doctrinal et stable**. Il évolue **par bumps** (refontes, migrations cadrées) plutôt qu'en flux continu. C'est l'inverse de MO (régime opérationnel en flux). Conséquences :
- Hygiène d'écriture stricte (R-059) - pas de bruit historique ni spéculation future dans les docs
- Versioning conservateur (R-056 - X.Y, pas de PATCH)
- Codification rigoureuse (R-054)

---

## 2. Principes structurants

Le Brain est gouverné par **7 principes cardinaux** :

1. **Source de vérité = doc Markdown** (R-001) - Notion = miroir d'application aligné via sync DDL périodiques.
2. **Codification universelle** (R-054) - table de préfixes stable : `CPT_`, `GLO_`, `METH_`, `TPL_`, `TPL_BRICK_`, `CHRT_`, `DBMAN_TW/MO/BR_`, `WRRD_TW/MO/BR_`, `LGBLK_`, `PRMPT_M/S/U/T_`, `OUT_`, `AGT_`. Voir `CODIFICATION_LBP.md` pour la grammaire complète.
3. **Frontmatter en 3 zones balisées** (R-055) - Identité / Méta-gouvernance / Spec d'usage.
4. **Versioning X.Y sans PATCH** (R-056) - bumps significatifs uniquement.
5. **Pas de jumelles texte sur Brain** (R-058) - interdiction des champs texte doublonnant une relation Notion (autorisées sur Twin, expérimentales sur MO).
6. **Hygiène d'écriture des docs Brain** (R-059) - chaque doc = source de vérité brute à l'instant t : pas de bruit historique ni spéculation future dans le corps.
7. **Brain unifié au niveau modèle de données** (D-019) - les zones Core / Motor sont conservées comme **étiquette de discours** mais ne sont plus une partition stricte. L'appartenance fonctionnelle est portée par la propriété `Domaine(s) d'usage` sur les 5 BDDs Motor.

---

## 3. Tableau maître canonique des 11 BDDs Brain

| # | BDD | Zone | Objet principal | Rôle | Codification |
|---|---|---|---|---|---|
| 1 | `Docs méta LBP` | ADMIN | Doctrine méta | Règles de gouvernance, conventions, workflows, QA du Brain lui-même | `CHRT_<TOKEN>` |
| 2 | `Glossaire LBP` | CORE | Concept canonique LBP | Vocabulaire de référence - chaque concept a définition, domaine, règles d'usage | `GLO_<TOKEN>` (paire avec `CPT_<TOKEN>`) |
| 3 | `Registre des notes de concept` | CORE | Note détaillée d'un concept | Fiches détaillées des concepts LBP (paire avec Glossaire, R-031) | `CPT_<TOKEN>` |
| 4 | `Registre des taxonomies` | CORE | Liste de valeurs contrôlée | Toutes les taxonomies (listes de valeurs) utilisées dans les BDDs Twin/MO/Brain | `<NAMESPACE>.<FAMILLE>` |
| 5 | `Méthodes LBP` | MOTOR | Méthode d'analyse / production | Méthodes LBP (3P, etc.) - cadre conceptuel et procédural d'une activité | `METH_<TOKEN>` |
| 6 | `Templates de Bricks` | MOTOR | Template de livrable MO | Moules pour les bricks instanciées par Mission Ops (D-018) | `TPL_BRICK_<TOKEN>` |
| 7 | `Agents LBP` | MOTOR | Agent LBP | 3 agents (Brain architect / Twin architect / KONTEXT) (D-021) | `AGT_<TOKEN>` |
| 8 | `Outils externes` | MOTOR | Outil externe utilisé par LBP | Catalogue des outils tiers mobilisés (Notion API, Drive, etc.) | `OUT_<TOKEN>` |
| 9 | `Prompts LBP` | MOTOR | Prompt structurant | **HUB CENTRAL** - orchestre méthodes, logic blocks, templates, outils, docs méta, agents (6 relations sortantes) | `PRMPT_<TOKEN>` (sous-typé `PRMPT_M/S/U/T_*`) |
| 10 | `Registre des logic blocks` | MOTOR | Bloc de raisonnement réutilisable | Blocs logiques modulaires utilisés par les prompts | `LGBLK_<TOKEN>` |
| 11 | `Manuels de BDD` | CROSS | Manuel d'une BDD Twin/MO/Brain | Spécifications des BDDs des 3 domaines - pont Brain → Twin/MO | `DBMAN_<TOKEN>` |

### Zones architecturales (étiquettes de discours, pas partition stricte D-019)

| Zone | BDDs | Fonction architecturale |
|---|---|---|
| **ADMIN BRAIN** | Docs méta LBP | Gouvernance du Brain lui-même (doctrines, règles, workflows) |
| **CORE BRAIN** | Glossaire LBP, Notes de concept, Taxonomies | Référentiels sémantiques transverses |
| **MOTOR BRAIN** | Prompts, Logic blocks, Méthodes, Templates de Bricks, Agents, Outils externes | Exécution + orchestration (utilisé pendant les missions, lecture seule) |
| **CROSS-ZONE** | Manuels de BDD | Pont vers les domaines opérationnels (Twin/MO) - un manuel décrit une BDD Twin ou MO |

### Propriété `Domaine(s) d'usage` (D-019)

Les **5 BDDs Motor** (Méthodes, Templates de Bricks, Agents, Outils externes, Prompts) portent la propriété `Domaine(s) d'usage` (multi-select : `Core` / `Motor` / `Digital Twin` / `Mission Ops`) qui localise fonctionnellement chaque entrée.

Les **BDDs Core** (Glossaire, Notes de concept, Taxonomies) **n'ont pas** cette propriété : elles sont transverses par nature.

---

## 4. Cartographie des objets Brain

Définitions canoniques et frontières (à ne pas confondre).

| Objet Brain | Définition | Ne doit pas être confondu avec |
|---|---|---|
| **Doc méta** | Doctrine méta de gouvernance du Brain (règle d'écriture, convention, workflow) | Méthode (qui décrit une activité métier), Prompt (qui exécute) |
| **Concept LBP** | Unité sémantique stabilisée du vocabulaire LBP, paire `Glossaire` + `Note de concept` | Terme de glossaire spécifique entreprise (qui est un objet Twin) |
| **Taxonomie** | Liste de valeurs contrôlée nommée et versionnée | Multi-select libre, énumération ad hoc |
| **Méthode LBP** | Cadre conceptuel et procédural d'une activité métier (ex. méthode 3P) | Prompt (qui est une instance d'exécution), Logic block (qui est un bloc de raisonnement) |
| **Template de bricks** | Moule pour une catégorie de livrable MO (D-018) | Brick instanciée (qui est un objet MO) |
| **Agent LBP** | Agent IA avec rôle structuré (D-021 : Brain architect / Twin architect / KONTEXT) | Prompt (qui est un input à un agent), Outil (qui est mobilisable par un agent) |
| **Outil externe** | Service ou logiciel tiers mobilisé par LBP | Méthode (qui est un cadre LBP propre), Logic block (qui est un bloc interne) |
| **Prompt LBP** | Instruction structurée pour exécution par un agent (hub central, 6 relations) | Méthode (cadre), Doc méta (doctrine) |
| **Logic block** | Bloc de raisonnement modulaire réutilisable | Prompt entier, méthode complète |
| **Manuel de BDD** | Spécification complète d'une BDD Twin/MO/Brain (source de vérité du schéma) | Doc méta (doctrine du Brain), WR-RD (extrait pour agents) |

---

## 5. Architecture logique d'une BDD Brain (couches typiques)

Les BDDs Brain ont une architecture sobre, focalisée sur **identité et méta-gouvernance** :

| Couche | Contenu | Question à laquelle elle répond |
|---|---|---|
| 1. Identité | `Nom canonique`, `Code unique` (R-054), `Statut de l'objet`, `Aliases` | Cette fiche est-elle clairement identifiée ? |
| 2. Méta-gouvernance | `Created Date`, `Last Updated Date`, `Version du template` (D-020), `Domaine(s) d'usage` (D-019, Motor seulement) | Quelle est la traçabilité de gouvernance de cette fiche ? |
| 3. Spécifiques | Champs propres à la BDD (Description, Objectif, Mode, Famille, etc.) | Qu'est-ce qui caractérise cette entrée ? |
| 4. Lien source | URL Drive vers le doc Markdown (R-001 : doc = source de vérité) | Où vit la source de vérité ? |
| 5. Relations | Relations bidir intra-Brain (Prompts ↔ Méthodes/Logic blocks/Templates/Outils/Docs méta/Agents ; Glossaire ↔ Notes de concept ; Taxonomies ↔ Manuels) | À quoi cette fiche est-elle reliée ? |
| 6. Rollups | Rollups de domaine d'usage et familles (héritage transverse) | Quelle vue agrégée transverse ? |

**Différences avec Twin/MO** :
- ❌ Pas de couche 5D (le 5D est un prisme Twin)
- ❌ Pas de chaînes de transformation D-009
- ❌ Pas de couche pilotage opérationnel (OPS.STATUS) - Brain est doctrinal, pas opérationnel
- ✅ Frontmatter en 3 zones balisées (R-055) - Identité / Méta-gouvernance / Spec d'usage
- ✅ Pas de jumelles texte (R-058) - relations Notion uniquement, pas de doublonnage textuel

---

## 6. Articulations inter-BDDs Brain

### 6.1 Hub central : Prompts LBP

`Prompts LBP` est le **hub d'exécution du Brain** avec **6 relations sortantes bidirectionnelles** :

```
Prompts LBP
    ├── utilise (Méthodes LBP)
    ├── utilise (Logic blocks)
    ├── utilise (Docs méta LBP)
    ├── utilise (Outils externes)
    ├── utilise (Templates de bricks)
    └── est utilisé par (Agents LBP)
```

Chaque relation a son miroir bidir côté cible. C'est le graphe le plus dense du Brain.

### 6.2 Hub sémantique : Glossaire LBP

`Glossaire LBP` est le **hub sémantique du Brain** avec 3 relations sortantes :

```
Glossaire LBP
    ├── est documenté par (Notes de concept) [paire CPT/GLO, R-031]
    ├── est mis en oeuvre par (Méthodes LBP)
    └── est modélisé par (Manuels de BDD)
```

### 6.3 Paire CPT / GLO (R-031)

Un concept LBP a **deux fiches en miroir** :
- `Glossaire LBP` (`GLO_<TOKEN>`) - identité + sémantique du concept (Code, Aliases, Mots clés, Type, Définition, Valeur ajoutée, Règles d'usage, Usages IA, Équivalent langage courant)
- `Registre des notes de concept` (`CPT_<TOKEN>`) - méta du fichier source (Code `CPT_*`, Version du template, Statut, Lien Drive)

Les **deux fiches partagent le même TOKEN** dans leur code (R-031). Le contenu détaillé du concept vit dans le doc Markdown lié, pas dans Notion.

### 6.4 Articulation Taxonomies ↔ Manuels de BDD

Chaque taxonomie est référencée par N manuels de BDD (qui à leur tour décrivent N BDDs Twin/MO). La relation `utilise (taxonomies)` côté Manuels est bidirectionnelle avec `est utilisée dans (manuels de BDD)` côté Taxonomies. Ça permet l'audit transverse "quelle taxo est référencée où ?" (cf. WF-016).

### 6.5 Articulation Manuels ↔ WR-RD (cascade)

Chaque manuel de BDD a un **WR-RD dérivé** (Write Rules / Read Keys, D-014, D-016) - précis champ par champ pour agents. La cascade est :

```
Manuel de BDD (source de vérité, R-001)
    └── section 4 ───→ WR-RD (sections 1-5, 9 colonnes strictes)
                      └── propagation Notion (DDL options select, lien WR-RD)
```

Règles : R-041 (propagation obligatoire), R-042 (QA stricte d'égalité), C-009 (annonce explicite). Workflow : WF-008 (propagation d'impacts) + WF-013 (génération WR-RD).

---

## 7. Articulation Brain → Twin / Mission Ops (lecture seule)

Le Brain est **lu** par les domaines opérationnels au moment de l'instanciation, mais **n'évolue pas** pendant les missions (D-019, D-021).

| Objet Brain consommé par Twin/MO | Mode de consommation |
|---|---|
| `Manuels de BDD` | Source de vérité du schéma des BDDs Twin/MO (les manuels vivent dans le Brain mais décrivent Twin/MO) |
| `Taxonomies` | Référencées par les manuels Twin/MO ; valeurs canoniques utilisées en options select |
| `Templates de Bricks` (`TPL_BRICK_*`) | Moules instanciés par Mission Ops (D-018) |
| `Méthodes LBP` (`METH_*`) | Cadres mobilisés par Mission Ops (référence par code) |
| `Prompts LBP` (`PRMPT_*`) | Instructions agents pendant Mission Ops (référence par code) |
| `Agents LBP` (`AGT_*`) | KONTEXT (orchestration MO), Twin architect (peuplement Twin) - D-021 |
| `Outils externes` (`OUT_*`) | Outils tiers mobilisés pendant les actions (référence par code) |
| `Logic blocks` (`LGBLK_*`) | Blocs de raisonnement réutilisables |
| `Glossaire LBP` + `Notes de concept` | Référentiel sémantique LBP partagé |

**Mécanique** : la référence se fait par **code stable** (R-054). Au moment de l'instanciation Twin/MO, le code est inscrit en référence textuelle dans la fiche cible (pas de relation cross-stack - D-023).

**Frontière infranchissable** : KONTEXT et Twin architect ne peuvent pas appeler Brain architect (D-021). Toute évolution Brain est flaggée comme remontée hors mission.

---

## 8. Stack technique

### 8.1 Stack actuelle et cible

- **Brain = Notion** (cible à moyen terme, pas de migration prévue dans les 12-18 mois)
- Volumétrie : ~200 docs Markdown actifs sur l'ensemble des 11 BDDs (volumétrie modérée)
- Gouvernance : manuelle, navigation hypertexte, audit visuel
- Performance : adaptée à un usage gouvernance, pas de besoin temps réel
- Notion apporte la richesse UX nécessaire (relations, rollups, vues, filtres) à la gouvernance documentaire

### 8.2 Source de vérité Markdown

Tous les docs Brain ont leur source dans `H:\Drive partagés\LBP - shared\Architecture data\` :
- `Manuels de BDD/Brain/` - 11 manuels Brain
- `Manuels de BDD/Brain/WR-RD/` - 11 WR-RD Brain
- `Notes de concept/` - fiches concept (`CPT_*`)
- `Glossaire/` - mini-fiches concept
- `Taxonomies/` - 102 taxonomies au canon (Phase A4.A)
- `Templates de bricks/` - 20 templates `TPL_BRICK_*`
- `Méthodes LBP/` - méthodes `METH_*`
- `00 - Docs méta/` - doctrine méta
- `Logic Blocks/`, `Prompts/`, `Outils externes/`, `Agents LBP/` - à refondre (cf. Chantier P)

### 8.3 Synchronisation Markdown ↔ Notion

La sync est **descendante** (Markdown → Notion, R-001). Workflows associés :
- WF-011 : récupérer URL Drive d'un fichier
- WF-012 : indexer un doc Markdown dans sa BDD Notion
- WF-013 : générer un WR-RD à partir d'un manuel
- WF-015 : migration au canon d'un type de doc Brain
- WF-016 : audit transverse Notion ↔ Manuels Brain
- WF-017 : sync DDL Notion BDD Brain depuis écarts d'audit
- WF-008 : propagation d'impacts (workflow transverse)

---

## 9. Roadmap d'évolution

| Sujet | Statut | Priorité | Cible |
|---|---|---|---|
| **Chantier P** - refonte 4 templates legacy + Logic Blocks (101) + Prompts (76) + Agents LBP (3 fiches D-021) | À cadrer | Haute | Post bundle docs méta |
| **Chantier M** - réactualisation PLAYBOOK macro-archi v2 + tri entrées Notion `Docs méta LBP` sans Markdown actif + bundle de docs méta dédiés | Audit fait, exécution à venir | Moyenne | Post Chantier P |
| Création des 3 fiches `Agents LBP` (Brain architect / Twin architect / KONTEXT) | Décidé (D-021) | Haute | Post Chantier P (besoin de Logic blocks + Prompts à jour) |
| Cogitation propriété `Régime de l'entité` (sandbox / officiel / avéré-figé / doublon archivé) | Backlog | Moyenne | Phase C |
| Migration vers Supabase (éventuelle) | Pas planifiée | Basse | 12-18 mois |

### 9.1 Chantier P (détail)

Périmètre :
- Refonte des 4 templates legacy (templates secondaires non encore migrés au canon v2 : `Template de system prompt.md`, `template-prompt_maitre_lbp.md`, `Template-prompt_lbp.md`, `template-meta_logic_block_lbp.md` - cf. `MIGRATION_REPORT_2026-04.md` §7.6)
- Tri massif `Prompts/` (76 prompts → état Twin v2)
- Tri massif `Logic Blocks/` (101 logic blocks → état Twin v2)
- Création des 3 fiches `Agents LBP` (D-021) une fois Prompts/Logic blocks à jour
- Mise à jour des system prompts / prompts maîtres / logic blocks pour cohérence Twin v2 + D-019 + D-021

### 9.2 Chantier M (détail)

Périmètre :
- Réactualisation `PLAYBOOK macro-archi v2` (équivalent du Panorama v3 du 22-04, à refondre comme bundle)
- Tri des entrées Notion `Docs méta LBP` sans Markdown actif (audit à mener)
- Bundle de docs méta dédiés à chaque doctrine (production en cours - cf. PANORAMA_LBP, DOCTRINE_LBP, CODIFICATION_LBP, PROPAGATION_RULES_LBP, ce SPECS_BRAIN_LBP, etc.)

---

## 10. Liens vers la documentation détaillée

### Manuels de BDD Brain (source de vérité, R-001)

Sous `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\` :
- `Manuel de BDD - Docs méta LBP.md`
- `Manuel de BDD - Glossaire LBP.md`
- `Manuel de BDD - Registre des notes de concept.md`
- `Manuel de BDD - Registre des taxonomies.md`
- `Manuel de BDD - Méthodes LBP.md`
- `Manuel de BDD - Templates de Bricks.md`
- `Manuel de BDD - Agents LBP.md`
- `Manuel de BDD - Outils externes.md`
- `Manuel de BDD - Prompts LBP.md`
- `Manuel de BDD - Registre des logic blocks.md`
- `Manuel de BDD - Manuels de BDD.md`

### WR-RD Brain (instructions champ par champ pour agents)

Sous `Manuels de BDD/Brain/WR-RD/` - 11 fichiers `WR-RD - X.md` correspondant aux 11 manuels.

### Décisions et règles structurantes

- `refs/DECISIONS_LBP.md` - D-019 (Brain unifié + isolation), D-020 (Version du template), D-021 (3 agents), D-023 (stack Notion/Supabase)
- `refs/RULES_LBP.md` - R-054 (codification), R-055 (frontmatter 3 zones), R-056 (versioning), R-058 (anti-jumelles texte), R-059 (hygiène d'écriture), R-001 (source Markdown)
- `refs/WORKFLOWS_LBP.md` - WF-008 (propagation), WF-011 à WF-017 (génération, indexation, audit, sync DDL)
- `refs/CODIFICATION_LBP.md` (à venir) - grammaire complète des codes Brain + Twin + MO
- `refs/PROPAGATION_RULES_LBP.md` (à venir) - synthèse opérationnelle des règles de propagation

### Snapshot DDL Notion (volatile, hors bundle)

Le **schéma DDL exact** (champs, casses, options select) vit dans Notion + manuels parents Markdown. Pour audit ponctuel : utiliser `notion-fetch` sur les 11 BDDs Brain ou se référer aux manuels parents (R-001). Si un export auto est nécessaire pour audit : à scripter, hors bundle durable.

---

> Dernière mise à jour : 30-04-2026 - refonte conceptuelle. Modèle conceptuel stable, indépendant du DDL Notion volatile.
