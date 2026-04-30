# Architecture Digest — Ecosysteme LBP

> Vue macro transverse de l'écosystème — à relire au début de chaque conversation pour re-contextualisation rapide.
> Pour le détail des BDD : voir `SPECS_ARCHITECTURE_BRAIN_LBP.md` (Brain) et `SPECS_ARCHITECTURE_TWIN_LBP.md` (Twin).
> Dernière mise à jour : 28-04-2026 — refresh post-Phase 7 + sync DDL Notion Brain + captures R-053→R-059 et D-019.

## 1. Vue macro

LBP (Little Big Picture) est un cabinet de conseil qui construit des Digital Twins d'organisations pour diagnostiquer, décider et agir. L'écosystème repose sur 4 domaines :

| Domaine | Rôle | Permanent / Instancié | Nb BDD |
|---------|------|-----------------------|--------|
| **Core Brain** | Gouvernance : glossaire, taxonomies, notes de concept | Permanent | 3 |
| **Motor Brain** | Bibliothèque opérationnelle : prompts, agents, méthodes, logic blocks, templates, outils | Permanent | 7 |
| **Admin Brain** | Docs méta (doctrine) | Permanent | 1 |
| **Digital Twin** | Représentation structurée du client | Instancié par mission | **28** (v2) |
| **Mission Ops** | Pilotage opérationnel de mission | Instancié par mission | 4 |

## 2. Principe fondamental

Le **doc Markdown (Architecture data / Drive) est la source de vérité**. Notion indexe et relie, mais ne porte pas le contenu. Le trio Drive (cloud) + Obsidian (édition locale) + Git (versioning) assure stockage, ergonomie et réversibilité.

## 3. Pile d'orchestration Brain

```
1. System prompt          — identité stable de l'agent
2. Prompt maître          — protocole général d'une opération
3. Logic block(s)         — logique locale opération x cible
4. Manuels / taxonomies   — vérité métier (structure, sens, contraintes)
5. Instructions écriture / clefs lecture — cohérence champs
6. Template de sortie     — forme du rendu
```

Pas tous les prompts passent par toute la pile. Pattern privilégié pour les opérations structurées.

## 4. Hub central du Brain : Prompts LBP

6 relations bidirectionnelles vers : Agents, Méthodes, Logic blocks, Docs méta, Outils externes, Templates de bricks.

## 5. Structure des BDD

### Brain (11 BDD permanentes)
- **Admin** : Docs méta LBP
- **Core** : Glossaire LBP, Registre notes de concept, Registre taxonomies
- **Motor** : Prompts LBP (HUB), Logic blocks, Méthodes, Templates de Bricks, Agents, Outils externes
- **Cross-zone** : Manuels de BDD

→ Détail : `refs/SPECS_ARCHITECTURE_BRAIN_LBP.md`

### Digital Twin v2 (28 BDD instanciées)

> `Sources d'informations` est Mission Ops (satellite de traçabilité transverse), pas Twin.

**1 socle sémantique**
- Glossaire spécifique entreprise

**3 extraction factuelle**
- Journal des signaux, Actions détectées, Enjeux

**8 socle structurel**
- Organisations, Relations inter-organisations (BDD edge), Collectifs, Individus, Postes, Actifs, Environnements, Événements

**1 mouvement / transformation**
- Initiatives organisationnelles

**1 pivot de qualification**
- Processus candidats

**8 couche analytique officielle**
- Processus, Pratiques organisationnelles, Principes organisationnels, Capacités organisationnelles, Problématiques, OKR, Indicateurs, Modulateurs

**6 sandboxes exploratoires** (pas de relations réelles sauf vers Sources d'informations)
- Capacités métier candidates (sandbox), OKR (sandbox), Pratiques (sandbox), Principes (sandbox), Problématiques (sandbox), Processus candidats (sandbox)

→ Détail, objets ontologiques, moteurs analytiques et chaînes de transformation : `refs/SPECS_ARCHITECTURE_TWIN_LBP.md`

### Mission Ops (4 BDD instanciées)
- Sources d'informations, Meetings, Actions LBP, Bricks

## 6. Changements v1 → v2 du Digital Twin

Cf. décisions D-002 à D-009 dans `refs/DECISIONS_LBP.md`.

| Avant | Après | Décision |
|-------|-------|----------|
| Unités Organisationnelles | Organisations + Collectifs | D-002 |
| Ressources | Actifs | D-003 |
| Rôles officiels | Postes (1 individu = 1 poste) | D-004 |
| — | Initiatives organisationnelles (nouvelle) | D-005 |
| — | Relations inter-organisations (BDD edge, nouvelle) | D-006 |
| — | 6 sandboxes spécialisées | D-007 |
| Carte informelle | Tableau maître canonique 29 BDD | D-008 |
| Lecture table par table | Chaînes de transformation de la connaissance | D-009 |

## 6 bis. Brain comme environnement documentaire en évolution (D-019)

Le Brain est unifié au niveau du **modèle de données** : la distinction Core / Motor n’est plus une partition stricte des BDDs mais reste une étiquette de discours, matérialisée dans la propriété `Domaine(s) d’usage` (multi-select : Core / Motor / Digital Twin / Mission Ops) sur les 5 BDDs Motor (Méthodes, Templates, Agents, Outils, Prompts).

Conséquences appliquées (sync DDL 28-04-2026) :

- DROP de la propriété `Type fonctionnel (BDD décrite)` sur la BDD `Manuels de BDD` (devenue redondante avec `Domaine(s) d’usage`).
- ADD de `Domaine(s) d’usage` sur les 4 BDDs Motor qui ne l’avaient pas (Méthodes, Templates, Agents, Outils).
- **Isolation stricte** Brain ↔ Mission Ops/Twin : aucune relation Notion directe entre une BDD Brain et une BDD MO/Twin. Le pont reste les Manuels de BDD (cross-zone) qui documentent les schémas.
- **Pas de jumelles texte sur Brain (R-058)** : autorisées sur Twin, expérimentales sur Mission Ops, **interdites sur Brain**. 2 jumelles texte ont été DROP sur Logic blocks.

## 7. Cycle de vie d'un doc Brain

```
Template (Docs méta) → instanciation (placeholders + @INSTR) → cleanup → doc MD final
→ validation humaine → indexation Notion (propriétés dérivées) → relations → propagation
```

## 8. Templates disponibles (dans Docs Méta LBP)

État au 28-04-2026 — refonte v2.0 effectuée Phase 6.5 + ajout Template Manuel BDD Brain en v1.1.

**Templates au canon (v2.0 / v1.1)**

| Template | Génère |
|----------|--------|
| `Template - Manuel de BDD - Digital Twin.md` | Manuels de BDD Twin |
| `Template - Manuel de BDD - Mission Ops.md` | Manuels de BDD Mission Ops |
| `Template - Manuel de BDD - Brain.md` (v1.1, nouveau) | Manuels de BDD Brain |
| `Template - WR-RD - Digital Twin.md` | WR-RD Twin |
| `Template - WR-RD - Mission Ops.md` | WR-RD Mission Ops |
| `Template - Note de concept.md` | Notes de concept |
| `Template - Taxonomie.md` (v2.0) | Taxonomies |
| `Template - Méthode LBP.md` (v2.0, refondu Phase 6.5) | Méthodes LBP |
| `Template - Outil externe.md` (v2.0, refondu Phase 6.5) | Fiches Outils externes |
| `Template - Template de Brick.md` (v2.0, méta-template, refondu Phase 6.5) | Templates de Bricks |

**Templates legacy à refondre (Phase 7 bis)**

| Template | Génère |
|----------|--------|
| `Template de system prompt.md` | System prompts |
| `template-prompt_maitre_lbp.md` | Prompts maîtres |
| `Template-prompt_lbp.md` | Prompts LBP |
| `template-meta_logic_block_lbp.md` | Logic blocks |

**À créer (court terme)**

- `Template - WR-RD - Brain.md` (pour aligner sur les 2 WR-RD Twin / Mission Ops, en vue des 11 WR-RD Brain).

## 9. Chemins d'accès

| Ressource | Chemin |
|-----------|--------|
| Vault Obsidian | `Architecture data` (via Obsidian CLI) |
| Drive | `H:\Drive partages\LBP - shared\Architecture data\` |
| Notion Brain | Page `20be1a18653c8079aeb1e01047fddddd` |
| Docs Méta LBP (templates) | `H:\...\Architecture data\Docs Méta LBP\` |
| Manuels de BDD (actuels) | `H:\...\Architecture data\Manuels de BDD\` |
| Notes de concept | `H:\...\Architecture data\Notes de Concept\` |
| Méthodes | `H:\...\Architecture data\Méthodes\` |
| Prompts | `H:\...\Architecture data\Prompts\` |
| Logic blocks | `H:\...\Architecture data\Logic Blocks\` |
| Taxonomies | `H:\...\Architecture data\Taxonomies\` |
| Templates de Bricks | `H:\...\Architecture data\Templates de Bricks\` |
| Clefs de lecture | `H:\...\Architecture data\Clefs de lectures\` |
| Nouveaux docs Twin v2 (hors vault) | `C:\Users\leona\Documents\00. OBSIDIAN  PREDATOR\LBP BRAIN VAULT\BDD DIGITAL TWIN\NOUVELLE VERSION DIGITAL TWIN\` |

## 10. Anomalies / dettes connues

### Actives

1. Glossaire : "est lié à (concepts)" reste un champ texte, pas une relation Notion (anomalie héritée v1, non traitée).
2. Logic blocks : `Lien Drive du logic block` toujours en `text` au lieu de `url` (héritée v1).
3. Pipeline de régénération Brain : full rebuild uniquement, pas de sync incrémentale.
4. Brain Studio (frontend) : 100% mock.
5. Prompts maîtres (76) et Logic Blocks (101) : obsolètes vs Twin v2 et hors canon — refonte/regen reportée à **Phase 7 bis**.
6. ~275 docs ont `summary` / `purpose` en TODO (à remplir par moi avec vision globale).
7. Audit nettoyage backticks abusifs (R-057) à passer en transverse.
8. 6 BDD "XXX" à migrer (ancienne archi).

### Résolues récemment (avril 2026)

- **Migration au canon de 318 docs Brain** (43 manuels + 32 WR-RD + 72 notes de concept + 96 taxonomies + 24 instances Phase 7) avec frontmatter R-054 / R-055 / R-056.
- **Sync DDL Notion Brain** : ~26 actions sur les 11 BDDs (DROP/ADD/ALTER/RENAME), 8 conversions text→rollup, 3 rollups manquants créés sur Outils externes.
- **R-058 — Suppression des jumelles texte sur Brain** : 2 jumelles DROP sur Logic blocks.
- **D-019 — DROP `Type fonctionnel (BDD décrite)`** sur Manuels de BDD (devenu redondant avec `Domaine(s) d’usage`).
- **R-053 — Convention de renaming des docs archivés** appliquée (suffix `(archivé v<X> le JJ-MM-YYYY)`).
- **R-052 — Apostrophes typographiques** : harmonisation Notion (Logic blocks `Statut de l’objet`).
- **Refonte v2.0 de 4 templates secondaires** (Phase 6.5).
- **Migration au canon des manuels Twin v2 + WR-RD Twin v2** (Phases 4-5).
- **Nouveaux manuels Twin v2, taxos, notes de concept** : intégrés dans `Architecture data/...` (plus hors vault).
- **Glossaire** : refonte massive en cours via les phases canon ; ~50% Brouillon en cours de résorption.
