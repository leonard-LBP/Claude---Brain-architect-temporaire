# Architecture Digest — Ecosysteme LBP

> Vue macro transverse de l'écosystème — à relire au début de chaque conversation pour re-contextualisation rapide.
> Pour le détail des BDD : voir `SPECS_ARCHITECTURE_BRAIN.md` (Brain) et `SPECS_ARCHITECTURE_TWIN.md` (Twin).
> Dernière mise à jour : 24-04-2026 — refonte après Panorama V2 v3 (nouvelle architecture Twin)

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

→ Détail : `refs/SPECS_ARCHITECTURE_BRAIN.md`

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

→ Détail, objets ontologiques, moteurs analytiques et chaînes de transformation : `refs/SPECS_ARCHITECTURE_TWIN.md`

### Mission Ops (4 BDD instanciées)
- Sources d'informations, Meetings, Actions LBP, Bricks

## 6. Changements v1 → v2 du Digital Twin

Cf. décisions D-002 à D-009 dans `refs/DECISIONS.md`.

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

## 7. Cycle de vie d'un doc Brain

```
Template (Docs méta) → instanciation (placeholders + @INSTR) → cleanup → doc MD final
→ validation humaine → indexation Notion (propriétés dérivées) → relations → propagation
```

## 8. Templates disponibles (dans Docs Méta LBP)

| Template | Génère |
|----------|--------|
| template-db-manual.md | Manuels de BDD (extraction directe + Brain) |
| template-db-manual-post_traitement.md | Manuels de BDD (post-traitement DT) |
| template-db-manual-mission_ops.md | Manuels de BDD (Mission Ops) |
| template-note_concept_lbp.md | Notes de concept |
| template-methode_lbp.md | Méthodes LBP |
| Template-prompt_lbp.md | Prompts LBP |
| template-prompt_maitre_lbp.md | Prompts maîtres |
| Template de system prompt.md | System prompts |
| template-meta_logic_block_lbp.md | Logic blocks |
| Template-Fiche_outil_LBP.md | Fiches Outils externes |
| Template méta de Brick.md | Templates de Bricks |
| template-taxonomie.md | Taxonomies |

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

### Héritées de v1 (non traitées)
1. Glossaire : ~50% des concepts en Brouillon, sans code unique
2. Glossaire : "est lié à (concepts)" est un champ texte, pas une relation
3. 3 relations Glossaire sans miroir exposé (vers Méthodes, Manuels, concepts)
4. Logic blocks : lien Drive en text au lieu d'url
5. Instructions d'écriture / clefs de lecture non indexées comme objets Brain
6. 6 BDD "XXX" à migrer (ancienne archi)
7. Pipeline : full rebuild uniquement (pas de sync incrémentale)
8. Brain Studio : 100% mock

### Nées de la refonte v2 du Twin
9. Prompts maîtres et logic blocks référencent encore l'ancienne architecture Twin (UO, Ressources, Rôles officiels) → obsolètes
10. Nouveaux manuels de BDD Twin v2 créés hors vault → à intégrer dans `Architecture data/Manuels de BDD/Digital Twin/`
11. Nouvelles taxonomies et notes de concept (Postes, Collectifs, Actifs, Initiatives) créées hors vault → à intégrer
12. BDD Notion du Twin actuelles désalignées avec la v2 → à régénérer à partir des nouveaux manuels
13. Archivage formel des anciens docs Twin (UO, Ressources, Rôles officiels) à prévoir
