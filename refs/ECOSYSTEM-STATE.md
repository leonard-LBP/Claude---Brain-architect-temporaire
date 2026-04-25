# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis a jour apres chaque changement.
> Derniere mise a jour : 2026-04-25 — Phase 5 batch C terminé (Notes concept + Glossaire double-indexés). Phase 5 indexation Notion COMPLÈTE.

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
| **Correction R-036 doublons A1+A2** | ✅ Terminé | 25 MAJ v1 (ressuscitation enrichie) + 25 v2 [DOUBLON] supprimées par Leonard | (à commit) |
| **A3 Taxonomies couche analytique** (INDIC, INS, ORG5D, PRA, PROC, SCALE) | ✅ Terminé | 23 MAJ enrichies + 2 créations (INDIC.TIMEROLE, SCALE.COVERAGE) + R-038 | (à commit) |
| **A4 Taxonomies Brain/transverse** (AGENT, BRICK, GLO, MET, META, MTG, OBJ, OPS, OUT, PLATFORM, PROMPT, SKILL, SRC) | ✅ Terminé | 24 MAJ enrichies + 1 création (MTG.EXEC_STATUS) + housekeeping ACT (1 MAJ ACT.CONSOLIDATION_TARGET + 1 archive ACT.CANDIDATE_TYPE) | (à commit) |
| **B1 Manuels socle structurel** | ✅ Terminé | 8 manuels (3 MAJ + 5 créations dont Actifs avec dette 7 relations comblée) | (à commit) |
| **B2 Manuels extraction factuelle** | ✅ Terminé | 2 MAJ (Actions détectées, Enjeux) | (à commit) |
| **B3 Manuels sémantique/mouvement/pivot/observation** | ✅ Terminé | 4 (2 MAJ Glossaire + Journal des signaux ; 2 créations Initiatives orga + Processus candidats) | (à commit) |
| **B4 Manuels couche analytique officielle** | ✅ Terminé | 8 (7 MAJ + 1 création Processus, migration "post-traitement" → "analytique officiel") | (à commit) |
| **B5 Manuels sandboxes** | ✅ Terminé | 6 créations (Type fonctionnel = "Digital Twin - sandbox") | (à commit) |
| **+ D-013 + modifs template + schéma Notion** | ✅ Terminé | template_version "v6.1.0" : ajout propriété Notion + ajout aux 28 frontmatters vault + 3 modifs template + maj manuel "Manuels de BDD" + 4 nouveaux types fonctionnels Notion + housekeeping (5 entrées) | (à commit) |
| **C Notes de concept + Glossaire** | ✅ Terminé | 152 actions Notion : 135 MAJ (67 cas A × 2 + 1 relation Template de brick) + 10 créations (5 cas D × 2) + 5 relations cas D + 2 archivages UO + 2 renommages (Référentiel 3P → 3P, Process → Processus) | (à commit) |

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
| 2026-04-25 | Batch A2 Taxonomies extraction + pivots (17 creations enrichies + 14 archives) + R-037 | (à commit) |
| 2026-04-25 | Correction R-036 doublons A1+A2 (25 MAJ v1 + 25 archives v2 [DOUBLON]) | (à commit) |
| 2026-04-25 | Capture R-038 (identifiant pivot par type d'objet : taxos = code, autres = nom) | (à commit) |
| 2026-04-25 | Batch A3 Taxonomies couche analytique (23 MAJ enrichies + 2 créations) | (à commit) |
| 2026-04-25 | Batch A4 Taxonomies Brain/transverse (24 MAJ enrichies + 1 création + housekeeping ACT.CANDIDATE_TYPE → ACT.CONSOLIDATION_TARGET) | (à commit) |
| 2026-04-25 | Capture D-013 (traçabilité de version de template d'instanciation) + modifs template Manuel de BDD + manuel "Manuels de BDD" | (à commit) |
| 2026-04-25 | Batch B Manuels Twin v2 (B1-B5 : 13 MAJ + 15 créations = 28 manuels) + 28 frontmatters vault avec template_version + housekeeping (5 entrées Notion) + 4 nouveaux types fonctionnels Notion | (à commit) |
| 2026-04-25 | Batch C Notes de concept + Glossaire (double indexation) : 152 actions Notion = 135 MAJ + 10 créations + 5 relations + 2 archivages + 2 renommages | (à commit) |
| 2026-04-25 | Capture R-039 (QA anti-artefacts IA dans tous les docs LBP) | (à commit) |

## Prochaines etapes

- **Commit unifié** des batchs A1+A2+A3+A4+B+C + R-038 + R-039 + D-013 + housekeeping
- **Anomalies QA** à corriger en source (vault) :
  - `concept - Repères communs.md` : artefact `:contentReference[oaicite:5]{index=5}` + texte tronqué dans summary frontmatter
  - `concept - Soft skill.md` : texte tronqué `décin collective` dans summary frontmatter
- **Phase 6** : Clefs de lecture (R-028)
- **Phase 7** : Prompts maitres et Logic blocks (refonte vers nouvelle archi Twin v2)
- **Enrichissement éditorial Phase 5bis** (option B) : remplir les champs avancés des fiches Glossaire LBP (Valeur ajoutée LBP, Usages IA potentiels, Règles d'usage et pièges, Équivalent langage courant) à partir du corps des notes de concept
