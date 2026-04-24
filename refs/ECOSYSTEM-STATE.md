# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis a jour apres chaque changement.
> Derniere mise a jour : 2026-04-24 — Phase 5 mini-batch 0 effectue

## Phase actuelle

**Phase 5 de la migration Twin v2 — Indexation Notion en cours.**

Phases 1-4 terminees :
- Arborescence Architecture data refondue (D-010)
- Anciens docs v1 archives (20 manuels Twin + 69 notes concept + 68 taxonomies)
- Nouveaux docs v2 migres (22 manuels + 6 sandboxes + 72 notes concept + 96 taxonomies + 1 template)
- Sync Drive validee, URLs accessibles via WF-011

Phase 5 en cours : indexation Notion par mini-batchs avec dry-run par doc.

**Mini-batch 0 (calibration) terminé** :
- 4 creations : Manuel Actifs, Taxo ASSET.SUBTYPE, Registre concept Actif, Glossaire Actif
- 3 relations : Manuel → Taxo, Glossaire → Registre, Glossaire → Manuel
- 4 archivages v1 : Manuel Ressources, Taxo Type/sous-type ressource, Glossaire Ressource, Note concept Ressource
- Ajout option `Digital Twin - socle structurel` dans taxo Notion Type fonctionnel

## Etat du Brain (11 BDD)

| BDD | Etat | Commentaire |
|-----|------|-------------|
| Glossaire LBP | Actif Ressource → Archive ; +1 entree v2 (Actif) | +1 a chaque batch |
| Registre notes de concept | +1 entree v2 (Actif), +1 archive (Ressource) | +1 a chaque batch |
| Registre taxonomies | +1 entree v2 (ASSET.SUBTYPE), +1 archive | +1 a chaque batch |
| Manuels de BDD | +1 entree v2 (Actifs), +1 archive (Ressources), +1 option `socle structurel` | +1 a chaque batch |
| Docs meta LBP | Inchange | Pas de mise a jour prevue |
| Prompts LBP | Inchange (obsoletes vs Twin v2) | Phase 7 a venir |
| Logic blocks | Inchange (obsoletes vs Twin v2) | Phase 7 a venir |
| Methodes LBP | Inchange | A verifier |
| Templates de Bricks | Inchange | A verifier |
| Agents LBP | Inchange | A verifier |
| Outils externes | Inchange | A verifier |

## Etat de la migration Twin v2

### Docs migres dans le vault (phases 2-3) - 2026-04-24

| Dossier | Etat | Archives |
|---------|------|----------|
| Manuels de BDD/Digital Twin/ | 22 manuels + 6 sandboxes | 20 archives v1 |
| Notes de Concept/ | 72 notes | 69 archives v1 |
| Taxonomies/ | 96 taxos | 68 archives v1 |
| 00 - Docs meta/Templates d'instanciation/ | 11 + 1 nouveau | 2 archives |

### Indexation Notion (Phase 5) — progression

> Ordre ajuste suite a R-035 (ordonnancement inter-types) : Taxonomies (A) avant Manuels (B) avant Notes concept + Glossaire (C).

| Batch | Statut | Volume | Commit |
|---|---|---|---|
| **Mini-batch 0 (calibration : Actif)** | ✅ Terminé | 4 creations + 4 archives + 3 relations | fdaaabd |
| **A1 Taxonomies socle structurel** (ORG, COL, ASSET sauf SUBTYPE, JOB, ENV, EVT, ORG_REL, STAKEHOLDER) | ✅ Terminé + enrichissement descriptions | 29 creations + 17 archives + 29 MAJ enrichies | 9327200 + 2984dc6 |
| **A2 Taxonomies extraction + pivots** (ACT, SIG, ENJ, CAP, INIT, IMPACT, EMO, IND) | ✅ Terminé | 17 creations (R-037) + 14 archives | en cours |
| A3 Taxonomies couche analytique (PROC, PRA, INDIC, INS, SCALE, ORG5D) | A venir | ~30 | |
| A4 Taxonomies Brain/transverse (AGENT, BRICK, GLO, MET, META, MTG, OBJ, OPS, OUT, PLATFORM, PROMPT, SKILL, SRC) | A venir | ~22 | |
| B1 Manuels socle structurel (7 manuels — reprise Actifs pour ajouter les 7 relations taxo manquantes) | A venir | 7+1 | |
| B2 Manuels extraction factuelle | A venir | 3 | |
| B3 Manuels semantique/pivot/mouvement | A venir | 3 | |
| B4 Manuels couche analytique | A venir | 8 | |
| B5 Manuels sandboxes | A venir | 6 | |
| C Notes de concept + Glossaire | A venir | 72 notes = double indexation | |

## Anomalies a traiter

| # | Anomalie | Severite | Statut |
|---|----------|----------|--------|
| 1 | Glossaire : "est lie a (concepts)" en texte | Moyenne | Non traite |
| 2 | 3 relations Glossaire sans miroir | Faible | Non traite |
| 3 | Logic blocks : lien Drive en text | Faible | Non traite |
| 4 | Instructions ecriture / clefs lecture non indexees (Brain) | Moyenne | Non traite (Phase 6) |
| 5 | 6 BDD "XXX" a migrer | Moyenne | Non traite |
| 6 | ~50% Glossaire en Brouillon | Haute | En cours (refonte en masse via Phase 5) |
| 7 | Prompts maitres et logic blocks pointent vers ancienne archi Twin | Haute | Non traite (Phase 7) |
| 8 | Taxo `Type fonctionnel (BDD decrite)` sous-dimensionnee (socle structurel manquait) | Resolue | Option ajoutee 2026-04-24 |

## Modifications effectuees

| Date | Action | Commit |
|------|--------|--------|
| 2026-04-07 | Initialisation repo git + README | 970ccf4 |
| 2026-04-07 | Mise en place fondations de travail | a1ae7c1 |
| 2026-04-24 | Integration architecture Twin v2 (Panorama) dans refs/ | a411afa |
| 2026-04-24 | Phase 1 Twin v2 — refonte arborescence vault + D-012 | d8d9a3d |
| 2026-04-24 | Capture R-029 a R-034 (regles indexation Notion) | d7e21fa |
| 2026-04-24 | Phase 5 mini-batch 0 Actif | fdaaabd |
| 2026-04-24 | Capture R-035 (ordre d'indexation inter-types) + reseq | d7e21fa |
| 2026-04-24 | Batch A1 Taxonomies socle structurel (29 creations + 17 archives) + R-036 | (en cours) |

## Prochaines etapes

- Mini-batch 1a : socle structurel (7 manuels restants apres Actifs)
- Mini-batch 1b-1e
- Batch 2 : taxonomies
- Batch 3 : notes de concept + glossaire
