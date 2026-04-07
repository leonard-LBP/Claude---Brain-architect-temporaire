# Architecture Digest — Ecosysteme LBP

> Version condensee de l'architecture pour re-contextualisation rapide.
> Derniere mise a jour : 2026-04-07

## 1. Vue macro

LBP (Little Big Picture) est un cabinet de conseil qui construit des Digital Twins d'organisations pour diagnostiquer, decider et agir. L'ecosysteme repose sur 4 domaines :

| Domaine | Role | Permanent / Instancie |
|---------|------|-----------------------|
| **Core Brain** | Gouvernance : glossaire, taxonomies, notes de concept, docs meta | Permanent |
| **Motor Brain** | Bibliotheque operationnelle : prompts, agents, methodes, logic blocks, templates, outils | Permanent |
| **Digital Twin** | Representation structuree du client (23 BDD) | Instancie par mission |
| **Mission Ops** | Pilotage operationnel de mission (4 BDD) | Instancie par mission |

## 2. Principe fondamental

Le **doc Markdown (Architecture data / Drive) est la source de verite**. Notion indexe et relie, mais ne porte pas le contenu. Le trio Drive (cloud) + Obsidian (edition locale) + Git (versioning) assure stockage, ergonomie et reversibilite.

## 3. Pile d'orchestration Brain

```
1. System prompt          — identite stable de l'agent
2. Prompt maitre          — protocole general d'une operation
3. Logic block(s)         — logique locale operation x cible
4. Manuels / taxonomies   — verite metier (structure, sens, contraintes)
5. Instructions ecriture / clefs lecture — coherence champs
6. Template de sortie     — forme du rendu
```

Pas tous les prompts passent par toute la pile. Pattern privilegie pour les operations structurees.

## 4. Hub central : Prompts LBP

6 relations bidirectionnelles vers : Agents, Methodes, Logic blocks, Docs meta, Outils externes, Templates de bricks.

## 5. Structure des BDD

### Brain (11 BDD permanentes)
- **Admin** : Docs meta LBP
- **Core** : Glossaire LBP, Registre notes de concept, Registre taxonomies
- **Motor** : Prompts LBP (HUB), Logic blocks, Methodes, Templates de Bricks, Agents, Outils externes
- **Cross-zone** : Manuels de BDD

### Digital Twin (23 BDD instanciees)
- **Extraction directe** : Sources d'info, Individus, Evenements, Environnements, Ressources, UO, Actions detectees, Enjeux, Glossaire specifique
- **Post-traitement** : Capacites orga, Roles officiels, Pratiques, Principes, Process, Indicateurs, Modulateurs, Problematiques, OKR
- **Sandbox** : Insights, Journal des signaux, Process candidats

### Mission Ops (4 BDD instanciees)
- Sources d'informations, Meetings, Actions LBP, Bricks

## 6. Cycle de vie d'un doc Brain

```
Template (Docs meta) → instanciation (placeholders + @INSTR) → cleanup → doc MD final
→ validation humaine → indexation Notion (proprietes derivees) → relations → propagation
```

## 7. Templates disponibles (dans Docs Meta LBP)

| Template | Genere |
|----------|--------|
| template-db-manual.md | Manuels de BDD (extraction directe + Brain) |
| template-db-manual-post_traitement.md | Manuels de BDD (post-traitement DT) |
| template-db-manual-mission_ops.md | Manuels de BDD (Mission Ops) |
| template-note_concept_lbp.md | Notes de concept |
| template-methode_lbp.md | Methodes LBP |
| Template-prompt_lbp.md | Prompts LBP |
| template-prompt_maitre_lbp.md | Prompts maitres |
| Template de system prompt.md | System prompts |
| template-meta_logic_block_lbp.md | Logic blocks |
| Template-Fiche_outil_LBP.md | Fiches Outils externes |
| Template meta de Brick.md | Templates de Bricks |
| template-taxonomie.md | Taxonomies |

## 8. Chemins d'acces

| Ressource | Chemin |
|-----------|--------|
| Vault Obsidian | `Architecture data` (via Obsidian CLI) |
| Drive | `H:\Drive partages\LBP - shared\Architecture data\` |
| Notion Brain | Page `20be1a18653c8079aeb1e01047fddddd` |
| Docs Meta LBP (templates) | `H:\...\Architecture data\Docs Meta LBP\` |
| Manuels de BDD | `H:\...\Architecture data\Manuels de BDD\` |
| Notes de concept | `H:\...\Architecture data\Notes de Concept\` |
| Methodes | `H:\...\Architecture data\Methodes\` |
| Prompts | `H:\...\Architecture data\Prompts\` |
| Logic blocks | `H:\...\Architecture data\Logic Blocks\` |
| Taxonomies | `H:\...\Architecture data\Taxonomies\` |
| Templates de Bricks | `H:\...\Architecture data\Templates de Bricks\` |
| Clefs de lecture | `H:\...\Architecture data\Clefs de lectures\` |

## 9. Anomalies connues

1. Glossaire : ~50% des concepts en Brouillon, sans code unique
2. Glossaire : "est lie a (concepts)" est un champ texte, pas une relation
3. 3 relations Glossaire sans miroir expose (vers Methodes, Manuels, concepts)
4. Logic blocks : lien Drive en text au lieu d'url
5. Instructions d'ecriture / clefs de lecture non indexees comme objets Brain
6. 6 BDD "XXX" en attente de migration
7. Pipeline : full rebuild uniquement (pas de sync incrementale)
8. Brain Studio : 100% mock
