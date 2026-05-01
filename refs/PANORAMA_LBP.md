# PANORAMA LBP — Macro-architecture de l'écosystème

> **Scope** : 🟦 LBP — Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> **Doc d'entrée** : à lire en premier pour comprendre l'écosystème LBP. Vue macro des 3 ensembles, de leurs frontières, de leur stack technique et de leurs articulations.
> Pour le **pourquoi** structurel des choix : `DOCTRINE_LBP.md`.
> Pour le **détail** d'un domaine : `SPECS_ARCHITECTURE_<DOMAIN>_LBP.md`.
> Pour les **règles atomiques** : `RULES_LBP.md` (R-XXX), `DECISIONS_LBP.md` (D-XXX), `WORKFLOWS_LBP.md` (WF-XXX).
> **Public visé** : nouveau dev (Clément, futurs collaborateurs), consultants LBP, agents.
> **Format** : ~250 lignes, lisible en 15 min.
> Dernière mise à jour : 01-05-2026 — création post-bundle. Remplace le `Panorama V2 v3` du 22-04-2026 (obsolète).

---

## 1. LBP en une phrase

**LBP (Little Big Picture)** est un cabinet de conseil qui construit des **Digital Twins d'organisations** pour diagnostiquer, décider et agir. L'écosystème documentaire de LBP repose sur **3 domaines distincts mais articulés** : Brain, Digital Twin, Mission Ops.

---

## 2. Les 3 domaines de l'écosystème

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   BRAIN              DIGITAL TWIN              MISSION OPS        │
│   (méta)             (modèle client)           (opérationnel)     │
│                                                                   │
│   Référentiel        Représentation            Trace de mission   │
│   doctrinal LBP      structurée d'une          (sources, meetings,│
│   (manuels, taxos,   organisation cliente      actions LBP,       │
│   méthodes, prompts, (objets ontologiques,     bricks)            │
│   templates, agents) relations, 5D)                               │
│                                                                   │
│   STABLE             INSTANCIÉ PAR MISSION     INSTANCIÉ PAR      │
│   évolue HORS        évolue PENDANT mission    MISSION            │
│   mission            (peuplement progressif)   évolue EN FLUX     │
│                                                                   │
│   Notion             Supabase (cible D-023)    Supabase           │
│   (cible moyen       Maquette Notion test      (cible D-023)      │
│   terme)             validée Phase B 30-04     Maquette Notion    │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

### 2.1 Brain — référentiel doctrinal LBP

**Rôle** : porter la **gouvernance documentaire de LBP**. Il définit le vocabulaire (concepts, taxonomies), les méthodes (3P, etc.), les prompts, les templates de bricks, les agents, les outils, les manuels de BDD et les docs méta qui régissent l'ensemble.

**11 BDDs structurelles** :
- ADMIN : `Docs méta LBP`
- CORE : `Glossaire LBP`, `Notes de concept`, `Registre des taxonomies`
- MOTOR : `Méthodes LBP`, `Templates de Bricks`, `Agents LBP`, `Outils externes`, `Prompts LBP`, `Registre des logic blocks`
- CROSS : `Manuels de BDD`

**Stack** : Notion à moyen terme (12-18 mois), pas de migration prévue. Volumétrie modérée (~200 docs Markdown actifs), gouvernance manuelle, navigation hypertexte.

**Détail** → `SPECS_ARCHITECTURE_BRAIN_LBP.md`

### 2.2 Digital Twin — modèle ontologique du client

**Rôle** : représenter **une organisation cliente** sous forme d'objets ontologiques (Individus, Collectifs, Organisations, Postes, Actifs, Environnements, Événements, Processus, Pratiques, Principes, Capacités, etc.) reliés par des relations sémantiques. Le Twin permet de produire des lectures systémiques (5D, 3P, chaînes diagnostic→pilotage).

**28 BDDs structurelles** réparties en 7 familles :
- Socle sémantique (Glossaire spécifique entreprise)
- Socle structurel (Organisations, Collectifs, Individus, Postes, Actifs, Environnements, Événements, Relations inter-organisations)
- Extraction factuelle (Journal des signaux, Actions détectées, Enjeux)
- Mouvement (Initiatives organisationnelles)
- Pivot de qualification (Processus candidats)
- Couche analytique officielle (Processus, Pratiques, Principes, Capacités, Problématiques, OKR, Indicateurs, Modulateurs)
- Sandboxes exploratoires (6 sandboxes)

**Stack** : Supabase (cible D-023). Maquette Notion test validée Phase B (30-04-2026, 51 fiches Twin+MO sur le scénario DeepSecAI v0).

**Détail** → `SPECS_ARCHITECTURE_TWIN_LBP.md`

### 2.3 Mission Ops — gouvernance opérationnelle de la mission

**Rôle** : tracer **ce qui se passe pendant une mission de conseil LBP** (sources collectées, meetings tenus, actions exécutées par le consultant LBP, livrables produits).

**4 BDDs structurelles** :
- `Sources d'informations` — pivot d'origine (entretiens, docs, exports), articule MO ↔ Twin
- `Meetings` — trace des rendez-vous tenus
- `Actions LBP` — backlog des actions du consultant LBP
- `Bricks` — livrables documentaires produits (D-018 — pivot MO ↔ Twin)

**Stack** : Supabase (cible D-023). Maquette Notion test validée Phase B.

**Détail** → `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`

---

## 3. Frontières et articulations

### 3.1 Frontières infranchissables

| Frontière | Règle | Justification |
|---|---|---|
| **Brain ⊥ Twin / MO** (modèle de données) | D-019 | Le Brain ne contient aucune relation Notion vers Twin/MO. L'héritage se fait via les manuels de BDD. |
| **Brain stable pendant mission** | D-021 | L'évolution du Brain est une activité méta-LBP, pas une activité de mission. |
| **KONTEXT ⊥ Brain architect** | D-021 | L'agent qui orchestre la mission ne peut pas modifier le Brain. Si besoin → flagging hors mission. |

### 3.2 Articulations légitimes

```
        Brain (lecture seule)
          │
          ├── Templates de bricks ─────────────► Bricks (MO)            [instanciation]
          ├── Méthodes LBP ────────────────────► Actions LBP (MO)       [référence par code]
          ├── Prompts / Agents ────────────────► Actions LBP (MO)       [orchestration KONTEXT]
          ├── Manuels de BDD Twin ─────────────► Twin                   [schéma]
          ├── Manuels de BDD MO ───────────────► MO                     [schéma]
          ├── Taxonomies ──────────────────────► Twin + MO              [valeurs canoniques]
          └── Glossaire LBP / Notes concept ───► Twin (Glossaire entreprise) [vocabulaire]

        Mission Ops ↔ Digital Twin (intriqué)
          │
          ├── Sources d'informations (MO) ─────► toutes BDDs Twin       [origine traçable, C-018]
          ├── Bricks (MO) ─────────────────────► fiches Twin            [notes avancées D-018]
          └── Actions LBP (MO) → produit ──────► Bricks → enrichit ────► fiches Twin [chaîne]
```

### 3.3 Mécanique de référencement

Brain → Twin/MO se fait par **codes stables** (R-054), pas par relation cross-stack. Au moment de l'instanciation MO (création d'une brick par exemple), le code template (`TPL_BRICK_PRF_ORG`) est inscrit en référence textuelle dans la fiche brick. La structure du template est **lue** depuis le Brain au moment de l'instanciation, mais aucune relation technique cross-domaine n'est maintenue.

---

## 4. Stack technique

### 4.1 Stack actuelle (mai 2026)

| Domaine | Stack | Statut |
|---|---|---|
| Brain | Notion + manuels Markdown (vault `Architecture data`, sync Drive) | Production |
| Digital Twin | Maquette Notion (page test) + manuels Markdown | Maquette validée Phase B |
| Mission Ops | Maquette Notion (page test) + manuels Markdown | Maquette validée Phase B |

### 4.2 Stack cible (D-023)

| Domaine | Stack cible | Horizon |
|---|---|---|
| Brain | Notion (à moyen terme, pas de migration prévue 12-18 mois) | Stable |
| Digital Twin | **Supabase** | Portage post-Phase C |
| Mission Ops | **Supabase** | Portage post-Phase C |

**Justification du split** :
- Brain = volumétrie modérée, gouvernance manuelle → Notion suffit et apporte la richesse UX
- Twin + MO = volumétrie potentiellement importante (fiches × missions actives), performance lecture/écriture critique, instanciation par client → Supabase nécessaire

### 4.3 Source de vérité Markdown (R-001)

**Indépendamment du backend**, le doc Markdown du vault `Architecture data` reste **la source de vérité**. Notion (ou demain Supabase) est miroir d'application, jamais l'inverse. Cette doctrine garantit la portabilité de l'écosystème à travers toutes les évolutions de stack.

---

## 5. Les 3 agents (D-021)

LBP s'appuie sur 3 agents IA spécialisés avec des rôles strictement séparés :

| Agent | Rôle | Domaine d'intervention |
|---|---|---|
| **Brain architect** | Évolution du Brain (manuels, taxos, méthodes, templates, prompts) | Activité méta-LBP, **hors mission** |
| **Twin architect** | Modélisation Twin client (peuplement, dédoublonnage, qualification) | Activité de mission, sur le Twin |
| **KONTEXT** | Orchestration de la mission (Mission Ops) | Activité de mission, sur MO |

**Frontière** : KONTEXT ⊥ Brain architect (interdit). Délégation autorisée : KONTEXT → Twin architect.

**Détail** → `DOCTRINE_LBP.md` §7 + `DECISIONS_LBP.md` D-021.

---

## 6. Les 9 doctrines structurantes (vue express)

Pour comprendre **pourquoi** l'écosystème est conçu comme ça, voir `DOCTRINE_LBP.md`. Vue express :

1. **4 régimes de connaissance** (R-012) — preuve / qualification / consolidation / action
2. **Isolation Brain ↔ Twin/MO** (D-019, D-021) — le Brain ne change pas pendant les missions
3. **Agnosticisme backend** — les manuels survivent à Notion/Supabase
4. **Sandboxes** (R-014) — sas d'exploration sans relations dures
5. **Chaînes de transformation** (D-009) — paradigme de lecture du Twin
6. **Bricks comme pivot** (D-018) — unité documentaire entre MO et Twin
7. **3 agents avec frontières** (D-021)
8. **Propagation Markdown-first** (R-001 + R-041/042 + WF-008)
9. **Hygiène d'écriture** (R-055/056/058/059)

---

## 7. Le bundle de docs méta — comment naviguer

### Pyramide à 4 niveaux

```
NIVEAU 1 — Vue d'entrée (à lire en premier)
└── PANORAMA_LBP.md                         ← TU ES ICI

NIVEAU 2 — Doctrine et règles (pour comprendre)
├── DOCTRINE_LBP.md                         [doctrines transverses 3 ensembles]
├── DOCTRINE_TWIN_LBP.md                    [doctrine détaillée Twin — régimes, chaînes, gouvernance]
├── RULES_LBP.md             (R-XXX)        [catalogue règles atomiques]
├── DECISIONS_LBP.md         (D-XXX)        [catalogue décisions architecturales]
└── WORKFLOWS_LBP.md         (WF-XXX)       [catalogue workflows opérationnels]

NIVEAU 3 — Spécifications par domaine (pour construire)
├── SPECS_ARCHITECTURE_BRAIN_LBP.md         [modèle conceptuel 11 BDDs Brain]
├── SPECS_ARCHITECTURE_TWIN_LBP.md          [modèle conceptuel 28 BDDs Twin]
├── SPECS_ARCHITECTURE_MISSION_OPS_LBP.md   [modèle conceptuel 4 BDDs MO]

NIVEAU 4 — Outils transverses (pour exécuter sans erreur)
├── CODIFICATION_LBP.md                     [grammaire de tous les codes]
└── PROPAGATION_RULES_LBP.md                [cheat sheet propagation]
```

### Quand consulter quoi ?

| Tu veux... | Va voir... |
|---|---|
| Comprendre l'écosystème en 15 min | Ce doc (PANORAMA) |
| Comprendre pourquoi tel choix architectural | DOCTRINE_LBP |
| Construire une nouvelle BDD ou en modifier une | SPECS_ARCHITECTURE_<DOMAIN>_LBP |
| Coder un nouvel objet | CODIFICATION_LBP |
| Modifier un objet existant | PROPAGATION_RULES_LBP (cheat sheet) ou WF-008 (détail) |
| Lookup d'une règle précise | RULES_LBP (R-XXX) |
| Lookup d'une décision archivée | DECISIONS_LBP (D-XXX) |
| Suivre un workflow opérationnel | WORKFLOWS_LBP (WF-XXX) |

---

## 8. Volumétrie de l'écosystème (état mai 2026)

| Métrique | Valeur |
|---|---|
| BDDs Brain | 11 (catalogue stable) |
| BDDs Digital Twin | 28 (22 officielles + 6 sandboxes) |
| BDDs Mission Ops | 4 |
| Manuels de BDD Markdown | 43 (Phase 4 migrée au canon) |
| WR-RD Markdown | 32 + 11 Brain (43 au total) |
| Notes de concept | 72 (Phase 6 migrée au canon) |
| Taxonomies au canon | 102 (Phase A4.A) |
| Templates de bricks | 20 |
| Méthodes LBP | 3 |
| Règles R-XXX | 60 |
| Décisions D-XXX | 23 |
| Workflows WF-XXX | 17 (8 actifs + 4 à formaliser + 5 récents) |
| Conventions C-XXX | 19 |
| Test Phase B fiches Twin+MO | 51 (DeepSecAI v0, 30-04-2026) |

---

## 9. Ce qui reste à refondre (chantiers à venir)

| Chantier | Périmètre | Priorité |
|---|---|---|
| **Chantier P** | Refonte 4 templates legacy + Logic Blocks (101) + Prompts (76) + 3 fiches Agents D-021 | Haute, post-bundle |
| **Chantier M** | Réactualisation PLAYBOOK macro-archi v2 + tri entrées Notion `Docs méta LBP` sans Markdown actif | Moyenne, post-Chantier P |
| **Phase C** | Audit final + figement Brain | Post-bundle |
| **Portage Supabase Twin+MO** | Modélisation Postgres, migration des taxos, instanciation par mission | Post-Phase C |
| **Cogitation propriété "Régime de l'entité"** | Sandbox / officiel / avéré-figé / doublon archivé | Phase C |

---

## 10. Renvois

- **`refs/DOCTRINE_LBP.md`** — pourquoi structurel des 9 doctrines transverses
- **`refs/DOCTRINE_TWIN_LBP.md`** — doctrine détaillée Twin (régimes de structuration, 15 chaînes, gouvernance, merge/consolidation/promotion)
- **`refs/SPECS_ARCHITECTURE_BRAIN_LBP.md`** — détail des 11 BDDs Brain
- **`refs/SPECS_ARCHITECTURE_TWIN_LBP.md`** — détail des 28 BDDs Twin
- **`refs/SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`** — détail des 4 BDDs MO
- **`refs/RULES_LBP.md`** — catalogue règles R-XXX
- **`refs/DECISIONS_LBP.md`** — catalogue décisions D-XXX
- **`refs/WORKFLOWS_LBP.md`** — catalogue workflows WF-XXX
- **`refs/CODIFICATION_LBP.md`** — grammaire des codes
- **`refs/PROPAGATION_RULES_LBP.md`** — cheat sheet propagation

---

> Doc d'entrée du bundle. Mis à jour à chaque évolution structurante de l'écosystème (refonte de doctrine, nouveau domaine, migration de stack).
