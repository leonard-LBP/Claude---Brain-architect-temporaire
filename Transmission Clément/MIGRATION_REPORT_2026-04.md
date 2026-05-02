# Compte rendu de transformation — Avril 2026

> **Doc one-shot, daté, figé**. Pas un doc durable du bundle (pas de suffixe `_LBP`).
> **Public** : Clément (dev LBP).
> **Auteur** : Leonard + Claude (collaboration session avril 2026).
> **Date de production** : 01-05-2026.
> **Statut** : compte rendu **figé** au 01-05-2026. Toute évolution ultérieure de l'écosystème ne sera pas reflétée ici — voir le bundle de docs méta durables (`refs/*_LBP.md`).

---

## Préambule

Salut Clément,

Pendant les dernières semaines (avril 2026), Leonard et moi (Claude, agent IA) avons mené une refonte importante de l'écosystème documentaire LBP : Brain, Digital Twin, Mission Ops. Tu as travaillé jusqu'ici avec l'architecture telle qu'elle était au **22-04-2026** (Panorama V2 v3) — depuis, beaucoup a changé.

Ce document est ton **point d'entrée** pour comprendre :
1. **Ce qui a changé** depuis le 22-04 (le delta)
2. **L'architecture cible aujourd'hui** (où on en est)
3. **Les règles essentielles** à connaître pour ne rien casser
4. **Ce qui reste à refondre** (chantiers à venir)
5. **Comment naviguer** le bundle de docs méta durables

L'objectif : que tu puisses reprendre la main sur l'app et son intégration sans avoir à tout réabsorber d'un coup. Le bundle complet (10 docs `*_LBP.md`) est ta référence permanente. Ce rapport te donne le contexte narratif pour démarrer.

---

## 1. Ce qui a changé depuis le 22-04-2026

### 1.1 Brain — gouvernance documentaire

**Avant (22-04)** : Brain partitionné en zones strictes Core / Motor avec règles d'isolation rigides. Codification fragmentée en 6+ conventions (`DBMAN_X`, `CPT.X.LBP.Y`, `OBJ.STATUT.LBP`, `TPL_BRICK_X`, `METH_X`...). Beaucoup de docs sans code.

**Aujourd'hui (01-05)** :
- **D-019** : Brain unifié au niveau modèle de données. Les zones Core / Motor sont conservées comme **étiquette de discours** mais ne sont plus une partition stricte. La propriété `Domaine(s) d'usage` (multi-select Core / Motor / Digital Twin / Mission Ops) sur les 5 BDDs Motor localise fonctionnellement chaque entrée.
- **R-054** : codification universelle unifiée. Tous les codes Brain suivent une grammaire stable avec table de préfixes (`CPT_`, `GLO_`, `METH_`, `TPL_`, `TPL_BRICK_`, `CHRT_`, `DBMAN_TW/MO/BR_`, `WRRD_TW/MO/BR_`, `LGBLK_`, `PRMPT_M/S/U/T_`, `OUT_`, `AGT_`).
- **R-055** : frontmatter en 3 zones balisées (Identité / Méta-gouvernance / Spec d'usage).
- **R-056** : versioning `X.Y` sans PATCH.
- **R-058** : interdiction des jumelles texte sur Brain.
- **R-059** : hygiène d'écriture (pas de bruit historique ni spéculation future dans les docs).
- **318 docs migrés au canon** sur les Phases 4-7 (43 manuels + 32 WR-RD + 72 notes de concept + 24 instances de templates + autres).
- **102 taxonomies migrées au canon** (Phase A4.A 28-04-2026), codes `<X>.<Y>.LBP` migrés vers `<X>.<Y>` (suffix `LBP` éliminé).
- **Sync DDL Notion Brain** : ~26 actions DDL appliquées (DROP/ADD/ALTER) pour aligner Notion sur les manuels (28-04-2026).
- **D-020** : propagation de la propriété `Version du template` (RICH_TEXT) à toutes les BDDs Brain — permet l'audit mécanique des docs stale.
- **D-021** : architecture des **3 agents LBP** formalisée (Brain architect / Twin architect / KONTEXT) avec frontières d'isolation.

### 1.2 Digital Twin — modèle ontologique du client

**Avant (22-04)** : 28 BDDs Twin v2 conçues mais pas encore complètement maquettées. Architecture en 8 principes cardinaux et 11 lectures analytiques (Panorama V2).

**Aujourd'hui (01-05)** :
- Architecture stabilisée (28 BDDs : 22 officielles + 6 sandboxes), aucune modification structurelle majeure depuis le 22-04.
- **Test fonctionnel Phase B** mené sur scénario fictif **DeepSecAI v0** (30-04-2026) : 51 fiches créées sur la maquette Notion test (35 Twin + 10 Pilotage + 6 Mission Ops). Test end-to-end qui a validé :
  - Les chaînes D-009 (Sources → Actions détectées → Process candidats → Process officiels ; Sources → Enjeux → Problématiques → OKR → Indicateurs)
  - Les sandboxes (R-014 — relations dures uniquement vers Sources)
  - La propagation bidirectionnelle automatique Notion (Meeting ↔ Action, Action ↔ Brick, Source ↔ Brick)
  - Les bricks comme notes avancées Twin (D-018)
- **Captures C-017** (lire WR-RD avant remplissage) et **C-018** (vérifier régime BDD avant signaler une anomalie) issues du test.
- **Refonte des 4 templates secondaires** (Phase 6.5) : `Template - Méthode LBP.md` v2.0, `Template - Outil externe.md` v2.0, `Template - Template de Brick.md` v2.0, etc.
- **Génération des 11 WR-RD Brain** + alignement des 11 manuels Brain.

### 1.3 Mission Ops — gouvernance opérationnelle

**Avant (22-04)** : Mission Ops mentionné dans le Panorama mais pas formellement spécifié.

**Aujourd'hui (01-05)** :
- **D-023** : Mission Ops formalisé comme **domaine co-égal** au Brain et au Twin, gouverné par 4 BDDs (`Sources d'informations`, `Meetings`, `Actions LBP`, `Bricks`).
- **4 manuels MO** stabilisés au canon (Phase 6.5) :
  - `Manuel de BDD - Sources d'informations.md`
  - `Manuel de BDD - Meetings.md`
  - `Manuel de BDD - Actions LBP.md`
  - `Manuel de BDD - Bricks.md`
- **4 WR-RD MO** générés (instructions champ par champ pour agents).
- **Test Phase B** a validé l'articulation MO ↔ Twin via 3 ponts :
  - Sources d'informations (origine traçable)
  - Bricks (notes avancées D-018)
  - Actions LBP (production)
- **D-022** : différenciation assumée des frontmatters Twin et Mission Ops (régimes de connaissance distincts → champs distincts).
- **`SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`** créé (auparavant absent).

### 1.4 Stack technique cible (D-023)

**Décision majeure** : **Brain reste sur Notion** (12-18 mois), **Twin et Mission Ops migrent vers Supabase** post-Phase C.

Justification :
- Brain = volumétrie modérée (~200 docs Markdown actifs), gouvernance manuelle → Notion suffit
- Twin + MO = volumétrie potentiellement importante (fiches × missions actives), performance critique, instanciation par client → Supabase nécessaire

**Conséquences pour toi** : la maquette Notion Twin+MO actuelle est une **fixture de validation de schéma**, pas une production. Le portage Supabase est un chantier post-Phase C à cadrer ensemble.

---

## 2. Architecture cible aujourd'hui

Pour comprendre l'écosystème en 15 min, lis : **`refs/PANORAMA_LBP.md`**.

Pour comprendre **pourquoi** l'écosystème est conçu comme ça (les 9 doctrines structurantes : régimes de connaissance, isolation Brain/Twin/MO, agnosticisme backend, sandboxes, chaînes D-009, bricks pivot, 3 agents, propagation Markdown-first, hygiène d'écriture), lis : **`refs/DOCTRINE_LBP.md`**.

### Synthèse en 5 points

1. **3 domaines co-égaux** : Brain (méta) + Digital Twin (modèle client) + Mission Ops (opérationnel mission).
2. **Isolation infranchissable** : le Brain n'évolue pas pendant les missions (D-019, D-021). KONTEXT ⊥ Brain architect.
3. **Markdown source de vérité** : R-001. Notion (et demain Supabase) = miroir d'application, jamais l'inverse.
4. **Agnosticisme backend** : les manuels et templates ne mentionnent jamais Notion. Ils survivent aux migrations de stack.
5. **Stack cible** : Brain Notion / Twin+MO Supabase (post-Phase C).

---

## 3. Règles essentielles à connaître pour ne rien casser

### 3.1 La règle d'or

> **Markdown = source de vérité unique. Tout dérivé (WR-RD, fiche Notion, indexation) est aligné sur lui, jamais l'inverse.** (R-001)

Si tu modifies un objet :
1. Modifier d'abord le doc Markdown (vault `Architecture data\`)
2. Aligner ensuite Notion (DDL si schéma, propriétés si contenu)
3. Annoncer explicitement la propagation (C-009)
4. Tracer dans `ECOSYSTEM-STATE.md` (C-011)
5. Commit + push (C-013)

### 3.2 Cheat sheet de propagation

**`refs/PROPAGATION_RULES_LBP.md`** est la fiche de chevet :
- Matrice « si tu modifies X → propage dans Y »
- Checklist actionnable en 7 étapes
- Anti-patterns à NE JAMAIS faire

Pour le détail procédural en 7 phases : `refs/WORKFLOWS_LBP.md` § WF-008.

### 3.3 Codification

**`refs/CODIFICATION_LBP.md`** est la référence pour tout code :
- Grammaire G1 (général Brain) : `<PREFIXE>_<IDENTIFIANT>`
- Grammaire G2 (taxonomies) : `<NAMESPACE>.<TAXO>`
- Grammaire G3 (bricks) : `BRK_<mission_code>_<brick_code>_<discriminant>_<rev>`
- Grammaire G4 (occurrences MO) : codes `SRC-`, `MTG-`, `ACT-` (à arbitrer cf. §5.2 du doc)
- Table officielle des préfixes Brain (issue de R-054)
- IDs systèmes (R-XXX, D-XXX, WF-XXX, C-XXX)

⚠️ **Anti-pattern** : ne pas inventer de préfixe sans vérifier R-054 (cas vécu pendant la production du bundle, cf. CODIFICATION_LBP §9).

### 3.4 Frontières des 3 agents (D-021)

- **Brain architect** : évolue le Brain, **hors mission**
- **Twin architect** : modélise le Twin client, pendant mission
- **KONTEXT** : orchestre Mission Ops, pendant mission

**Frontière infranchissable** : KONTEXT ⊥ Brain architect. Si KONTEXT identifie un besoin d'évolution Brain, il **flagge** une remontée à traiter hors mission, pas plus.

### 3.5 Hygiène des docs

- Frontmatter en 3 zones (R-055 : Identité / Méta-gouvernance / Spec d'usage)
- Versioning `X.Y` (R-056 — pas de PATCH)
- Pas de jumelles texte sur Brain (R-058)
- Pas de bruit historique ni spéculation future dans le corps des docs (R-059) — l'historique vit dans git + DECISIONS_LBP, le futur vit dans le backlog
- Apostrophes typographiques (R-052 : `'` U+2019, pas `'` U+0027)
- Dates au format JJ-MM-YYYY (R-044)

---

## 4. Ce qui reste à refondre (chantiers à venir)

### 4.1 Chantier P — refonte Logic Blocks + Prompts + Agents + 4 templates legacy

**Périmètre** :
- Refonte des 4 templates legacy (templates secondaires non encore migrés au canon v2)
- Tri massif des **101 Logic Blocks** (état Twin v2)
- Tri massif des **76 Prompts** (état Twin v2)
- Création des **3 fiches `Agents LBP`** (Brain architect / Twin architect / KONTEXT) une fois Prompts/Logic blocks à jour
- Mise à jour des system prompts / prompts maîtres / logic blocks pour cohérence Twin v2 + D-019 + D-021

**Priorité** : Haute (à enchaîner après stabilisation du bundle docs méta).

### 4.2 Chantier M — réactualisation docs méta

**Périmètre** :
- Réactualisation `PLAYBOOK macro-archi v2` (équivalent du Panorama v3 obsolète)
- Tri des entrées Notion `Docs méta LBP` sans Markdown actif
- Bundle de docs méta dédiés à chaque doctrine (production en cours — c'est le bundle que tu as sous les yeux)

**Priorité** : Moyenne, post-Chantier P.

### 4.3 Phase C — audit final + figement Brain

**Périmètre** :
- Audit transverse Notion ↔ Manuels Brain (WF-016)
- Figement de l'architecture Brain (pas de modifs sans D-XXX explicite)
- Cogitation propriété **"Régime de l'entité"** (sandbox / officiel / avéré-figé / doublon archivé)

**Priorité** : Post-bundle docs méta complet.

### 4.4 Portage Supabase Twin+MO

**Périmètre** :
- Modélisation Postgres des 4 BDDs MO + 28 BDDs Twin + relations (foreign keys)
- Migration des taxonomies LBP en tables de référence
- Préservation des patterns de codification (R-054 + grammaire bricks)
- Workflows d'instanciation par mission
- Synchronisation avec le Brain (lecture seule des templates)

**Priorité** : Post-Phase C. Chantier dédié à cadrer ensemble.

### 4.5 Migration Notion Brain (éventuelle)

**Périmètre** : pas de plan à court terme. Notion suffit pour Brain à 12-18 mois. Si une migration devient nécessaire, ce sera un chantier dédié à part.

---

## 5. Roadmap suggérée pour Clément

### Étape 1 — Lecture du bundle (1-2 jours)

Dans cet ordre :
1. **`refs/PANORAMA_LBP.md`** (15 min) — vue macro
2. **`refs/DOCTRINE_LBP.md`** (30 min) — pourquoi structurel
3. Ce rapport (`MIGRATION_REPORT_2026-04.md`) — delta avec ce que tu connaissais
4. **`refs/SPECS_ARCHITECTURE_BRAIN_LBP.md`** (le domaine que tu connais le plus) — modèle conceptuel à jour
5. **`refs/SPECS_ARCHITECTURE_TWIN_LBP.md`** (architecture validée Phase B)
6. **`refs/SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`** (nouveau domaine pour toi)
7. **`refs/PROPAGATION_RULES_LBP.md`** (cheat sheet, à garder à portée de main)
8. **`refs/CODIFICATION_LBP.md`** (référence des codes)

Les catalogues (`RULES_LBP.md`, `DECISIONS_LBP.md`, `WORKFLOWS_LBP.md`) ne sont pas à lire d'une traite — ce sont des références à consulter quand tu cherches une règle/décision/workflow précis.

### Étape 2 — Vérification de l'app vs nouvelle architecture (~1 semaine)

L'app que tu as déployée est sur l'ancienne architecture. Ce qu'il faut auditer :
- Quelles BDDs de l'app correspondent encore aux BDDs cibles décrites dans SPECS_X_LBP ?
- Quelles propriétés de l'app sont obsolètes / manquantes / désynchronisées ?
- Comment l'app gère-t-elle la stack technique cible (Notion Brain + Supabase Twin+MO) ?

À l'issue : produire un **rapport d'écart app vs architecture cible** pour prioriser les évolutions.

### Étape 3 — Cadrage portage Supabase (post-Phase C, à arbitrer ensemble)

Cadrer ensemble :
- Schémas Postgres pour Twin et MO
- Stratégie de migration des données existantes
- Workflows d'instanciation par mission
- Synchronisation Brain (Notion) ↔ Twin/MO (Supabase) — lecture seule des templates et codes

### Étape 4 — Évolutions app au fil de l'eau

Au fur et à mesure que les Chantiers P et M avancent (Prompts, Logic Blocks, Agents, docs méta), ces évolutions devront se refléter dans l'app. À cadrer en flux continu.

---

## 6. Bundle docs méta — ta référence permanente

Le bundle est versionné dans le repo git `Claude - Brain architect temporaire` (sous `refs/`) **ET** sera publié dans le vault `Architecture data\00 - Docs méta\Doctrines & playbooks\Bundle écosystème LBP\` (post-finalisation, indexation Notion via WF-012).

### Pyramide à 4 niveaux

```
NIVEAU 1 — Vue d'entrée
└── PANORAMA_LBP.md                         [vue macro 3 ensembles]

NIVEAU 2 — Doctrine et règles
├── DOCTRINE_LBP.md                         [pourquoi structurel narratif]
├── RULES_LBP.md             (R-XXX)        [60 règles atomiques]
├── DECISIONS_LBP.md         (D-XXX)        [23 décisions architecturales]
└── WORKFLOWS_LBP.md         (WF-XXX)       [17 workflows opérationnels]

NIVEAU 3 — Spécifications par domaine
├── SPECS_ARCHITECTURE_BRAIN_LBP.md         [11 BDDs Brain]
├── SPECS_ARCHITECTURE_TWIN_LBP.md          [28 BDDs Twin]
└── SPECS_ARCHITECTURE_MISSION_OPS_LBP.md   [4 BDDs MO]

NIVEAU 4 — Outils transverses
├── CODIFICATION_LBP.md                     [grammaire de tous les codes]
└── PROPAGATION_RULES_LBP.md                [cheat sheet propagation]
```

### Convention C-008

Tous les docs durables du bundle ont le suffixe `_LBP.md`. Glob `refs/*_LBP.md` extrait le bundle complet. Les autres docs (`ECOSYSTEM-STATE.md`, `RULES_BRAIN_TWIN-backlog.md`, etc.) sont **hors bundle** (Scope Session, vivants ou backlog, non destinés à être indexés dans BDD `Docs méta LBP`).

---

## 7. Annexes

### 7.1 Captures de règles depuis le 22-04 (extrait)

| ID | Capture | Date |
|---|---|---|
| C-008 | Séparation scope LBP / Session dans `refs/` | 26-04 |
| C-009 | Annonce explicite propagation Manuel ↔ WR-RD | 27-04 |
| C-010 | Numérotation lettres latines / chiffres simples | 27-04 |
| C-011 | Mise à jour systématique ECOSYSTEM-STATE | 28-04 |
| C-012 | Calibration explicite avant production en série | 29-04 |
| C-013 | Push systématique après commit | 29-04 |
| C-014 | Quirk wrapper MCP Notion apostrophes ASCII | 29-04 |
| C-015 | Vocabulaire « notes Markdown » (pas « notes Drive ») | 29-04 |
| C-016 | Mise à jour plans JSON après ajouts inline | 29-04 |
| C-017 | Lire WR-RD avant remplissage BDD Notion | 30-04 |
| C-018 | Vérifier régime BDD avant signaler anomalie relation | 30-04 |
| D-018 | Bricks de connaissance comme Notes avancées Twin | — |
| D-019 | Brain unifié + isolation Brain ↔ MO/Twin | 28-04 |
| D-020 | Propagation `Version du template` à toutes BDDs Brain | 28-04 |
| D-021 | Architecture des 3 agents LBP | 28-04 |
| D-022 | Différenciation assumée frontmatters Twin/MO | 30-04 |
| D-023 | MO co-égal Brain/Twin + stack Notion/Supabase | 30-04 |
| R-052 | Apostrophes typographiques | — |
| R-053 | Convention de renaming des docs archivés | — |
| R-054 | Codification universelle des objets Brain | 28-04 |
| R-055 | Frontmatter canon en 3 zones balisées | 28-04 |
| R-056 | Versioning X.Y sans PATCH | 28-04 |
| R-058 | Pas de jumelles texte sur Brain | 28-04 |
| R-059 | Hygiène d'écriture des docs Brain | 28-04 |
| R-060 | Hygiène `summary/purpose` frontmatter | 29-04 |
| WF-008 | Propagation d'impacts (workflow exhaustif) | 30-04 |
| WF-013 | Génération WR-RD à partir d'un Manuel | 26-04 |
| WF-014 | Génération BDD Twin sur Notion à partir du Manuel | 26-04 |
| WF-015 | Migration au canon d'un type de doc Brain | 28-04 |
| WF-016 | Audit transverse Notion ↔ Manuels Brain | 28-04 |
| WF-017 | Sync DDL Notion BDD Brain | 28-04 |

### 7.2 État du test Phase B (30-04-2026)

Test fonctionnel mené sur scénario fictif **DeepSecAI v0** (mock data fournie par toi-même, Clément) :
- 51 fiches créées sur la maquette Notion test (page `352e1a18653c8079b1b6edd1c456aaeb`)
- 17 BDDs mobilisées (10 Twin officielles + 5 Pilotage + 3 MO)
- 10 vagues de remplissage (substrat → observation → consolidation → pilotage → MO → vérifs)
- Auto-propagation bidir Notion validée (Meeting↔Action, Action↔Brick, Source↔Brick)
- Chaînes D-009 validées de bout en bout

Apprentissages capitalisés dans `refs/TEST_TWIN_OPS_PLAYBOOK.md` (Scope Session, hors bundle).

### 7.3 Liste exhaustive du bundle docs méta

Glob `refs/*_LBP.md` au 01-05-2026 (10 docs) :

| Doc | Lignes | Rôle |
|---|---|---|
| PANORAMA_LBP.md | 274 | Doc d'entrée — vue macro 3 ensembles |
| DOCTRINE_LBP.md | 327 | Pourquoi structurel — 9 doctrines narratives |
| SPECS_ARCHITECTURE_BRAIN_LBP.md | 303 | Modèle conceptuel 11 BDDs Brain |
| SPECS_ARCHITECTURE_TWIN_LBP.md | 200 | Modèle conceptuel 28 BDDs Twin |
| SPECS_ARCHITECTURE_MISSION_OPS_LBP.md | 278 | Modèle conceptuel 4 BDDs MO |
| RULES_LBP.md | ~1 250 | Catalogue règles R-XXX (60 règles) |
| DECISIONS_LBP.md | ~620 | Catalogue décisions D-XXX (23 décisions) |
| WORKFLOWS_LBP.md | ~650 | Catalogue workflows WF-XXX (17 workflows) |
| CODIFICATION_LBP.md | 349 | Grammaire de tous les codes |
| PROPAGATION_RULES_LBP.md | 138 | Cheat sheet propagation |

Total : ~4 600 lignes de doc méta durable.

### 7.4 Mapping des changements v1 → v2 du Digital Twin

Pour ton onboarding rapide, voici les changements structurels du Twin entre l'ancienne et la nouvelle architecture :

| Avant (Twin v1) | Après (Twin v2) | Décision |
|---|---|---|
| Unités Organisationnelles | Organisations + Collectifs | D-002 |
| Ressources | Actifs | D-003 |
| Rôles officiels | Postes (1 individu = 1 poste) | D-004 |
| — | Initiatives organisationnelles (nouvelle BDD) | D-005 |
| — | Relations inter-organisations (BDD edge, nouvelle) | D-006 |
| — | 6 sandboxes spécialisées | D-007 |
| Carte informelle | Tableau maître canonique 28 BDDs Twin | D-008 |
| Lecture table par table | Chaînes de transformation de la connaissance | D-009 |

Détail complet : `refs/DECISIONS_LBP.md` D-002 à D-009.

### 7.5 Cycle de vie d'un doc Brain

```
Template (Docs méta) → instanciation (placeholders + @INSTR) → cleanup → doc MD final
→ validation humaine → indexation Notion (propriétés dérivées) → relations → propagation
```

Détail des workflows : `refs/WORKFLOWS_LBP.md` (WF-001 à WF-017, notamment WF-008 propagation).

### 7.6 Templates au 01-05-2026

**Templates au canon (v2.0 ou v1.1)** :

| Template | Génère |
|---|---|
| `Template - Manuel de BDD - Digital Twin.md` | Manuels de BDD Twin |
| `Template - Manuel de BDD - Mission Ops.md` | Manuels de BDD Mission Ops |
| `Template - Manuel de BDD - Brain.md` (v1.1) | Manuels de BDD Brain |
| `Template - WR-RD - Digital Twin.md` | WR-RD Twin |
| `Template - WR-RD - Mission Ops.md` | WR-RD Mission Ops |
| `Template - WR-RD - Brain.md` (v1.0) | WR-RD Brain |
| `Template - Note de concept.md` | Notes de concept |
| `Template - Taxonomie.md` (v2.0) | Taxonomies |
| `Template - Méthode LBP.md` (v2.0) | Méthodes LBP |
| `Template - Outil externe.md` (v2.0) | Fiches Outils externes |
| `Template - Template de Brick.md` (v2.0, méta-template) | Templates de Bricks |

**Templates legacy à refondre (Chantier P)** :

| Template | Génère |
|---|---|
| `Template de system prompt.md` | System prompts |
| `template-prompt_maitre_lbp.md` | Prompts maîtres |
| `Template-prompt_lbp.md` | Prompts LBP |
| `template-meta_logic_block_lbp.md` | Logic blocks |

### 7.7 Chemins d'accès — table technique

| Ressource | Chemin |
|---|---|
| Vault Obsidian | `Architecture data` (via Obsidian CLI) |
| Drive racine | `H:\Drive partagés\LBP - shared\Architecture data\` |
| Notion Brain (page maître) | `20be1a18653c8079aeb1e01047fddddd` |
| Docs méta LBP (templates) | `H:\...\Architecture data\00 - Docs méta\Templates d'instanciation\` |
| Bundle docs méta durables | `H:\...\Architecture data\00 - Docs méta\Doctrines & playbooks\Bundle écosystème LBP\` (post-publication) |
| Manuels de BDD | `H:\...\Architecture data\Manuels de BDD\` (sous-dossiers Brain / Digital Twin / Mission Ops) |
| WR-RD | `H:\...\Architecture data\Manuels de BDD\<Domain>\WR-RD\` |
| Notes de concept | `H:\...\Architecture data\Notes de concept\` |
| Méthodes | `H:\...\Architecture data\Méthodes LBP\` |
| Prompts | `H:\...\Architecture data\Prompts\` |
| Logic blocks | `H:\...\Architecture data\Logic Blocks\` |
| Taxonomies | `H:\...\Architecture data\Taxonomies\` |
| Templates de bricks | `H:\...\Architecture data\Templates de bricks\` |
| Repo git collab Claude | `C:\Users\leona\LBP - dev\Claude - Brain architect temporaire\` |
| Maquette Notion test Phase B | Page `352e1a18653c8079b1b6edd1c456aaeb` |

### 7.8 Anomalies / dettes connues au 01-05-2026

**Anomalies actives** (à traiter dans les chantiers à venir) :

1. Glossaire LBP : `est lié à (concepts)` reste un champ texte au lieu d'une relation Notion structurée (anomalie héritée v1, non traitée).
2. Logic blocks : `Lien Drive du logic block` toujours en `text` au lieu de `url` (héritée v1).
3. Pipeline de régénération Brain : full rebuild uniquement, pas de sync incrémentale.
4. Brain Studio (frontend) : 100% mock.
5. Prompts maîtres (76) et Logic Blocks (101) : obsolètes vs Twin v2 et hors canon → **refonte/regen Chantier P**.
6. ~275 docs ont `summary` / `purpose` en TODO (à remplir en Phase C).
7. Audit nettoyage backticks abusifs (R-057) à passer en transverse.
8. 6 BDDs "XXX" héritées de l'ancienne archi à migrer ou archiver.
9. Codes de codification ad hoc dans les fichiers du vault potentiellement encore présents (`TPL_BRK_` au lieu de `TPL_BRICK_`, `MET_` au lieu de `METH_`, etc.) — audit transverse à mener (cf. CODIFICATION_LBP §9).

**Anomalies résolues récemment (avril 2026)** :

- **Migration au canon de 318 docs Brain** (43 manuels + 32 WR-RD + 72 notes de concept + 96 taxonomies + 24 instances Phase 7) avec frontmatter R-054 / R-055 / R-056.
- **Sync DDL Notion Brain** : ~26 actions sur les 11 BDDs (DROP/ADD/ALTER/RENAME), 8 conversions text→rollup, 3 rollups manquants créés sur Outils externes.
- **R-058 — Suppression des jumelles texte sur Brain** : 2 jumelles DROP sur Logic blocks.
- **D-019 — DROP `Type fonctionnel (BDD décrite)`** sur Manuels de BDD (devenu redondant avec `Domaine(s) d'usage`).
- **R-053 — Convention de renaming des docs archivés** appliquée (suffix `(archivé v<X> le JJ-MM-YYYY)`).
- **R-052 — Apostrophes typographiques** : harmonisation Notion (Logic blocks `Statut de l'objet`).
- **Refonte v2.0 de 4 templates secondaires** (Phase 6.5).
- **Migration au canon des manuels Twin v2 + WR-RD Twin v2** (Phases 4-5).
- **Test Phase B Twin+MO** (51 fiches sur scénario DeepSecAI v0, 30-04-2026) — validation des chaînes D-009 + auto-propagation Notion + bricks D-018.

### 7.9 Hors bundle (Scope Session, non destinés à toi)

| Doc | Rôle |
|---|---|
| ECOSYSTEM-STATE.md | Journal vivant de l'écosystème (re-contextualisation Claude) |
| RULES_BRAIN_TWIN-backlog.md | Backlog de règles pressenties (avant promotion R-XXX) |
| SESSION_WORKFLOWS.md | Workflows propres à la collaboration Claude/Leonard |
| TEST_TWIN_OPS_PLAYBOOK.md | Apprentissages du test Phase B (à archiver post-Phase C) |
| CLAUDE.md | Conventions de collaboration C-XXX |

---

## Mot de la fin

L'écosystème est **stabilisé doctrinalement** au 01-05-2026 sur ses 9 doctrines structurantes. Le bundle de docs méta durables est ta source de vérité permanente. Ce rapport est ton point d'entrée narratif.

Si tu as des questions au fur et à mesure de ta lecture, on peut en discuter avec Leonard. Les règles évolueront au fil des chantiers (P, M, Phase C, Supabase) — chaque évolution sera capturée dans les docs durables (`refs/*_LBP.md`), pas dans ce rapport (qui reste figé au 01-05-2026).

Bonne reprise.

— Leonard + Claude
