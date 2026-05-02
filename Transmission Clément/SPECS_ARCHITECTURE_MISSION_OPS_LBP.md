---
# === Identité ===
title: "Architecture de Mission Ops LBP"
doc_type: doc_meta
code: "CHRT_SPECS_MISSION_OPS_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
template_version: "1.0"
created_at: "30-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Modèle conceptuel des 4 BDDs Mission Ops (Sources d'informations, Meetings, Actions LBP, Bricks) : 6 principes structurants, tableau maître, cartographie objets, architecture logique en 4 couches sobres, articulation Twin↔MO via 3 ponts (Sources / Bricks / Actions), articulation Brain↔MO en lecture seule, stack technique Supabase cible (D-023)."
purpose: "Servir de référence canonique du modèle Mission Ops. Issu de la validation de la maquette Notion par le test Phase B (51 fiches Twin+MO sur scénario DeepSecAI v0, 30-04-2026)."
tags:
  - doc_meta
  - specs
  - architecture
  - mission_ops
  - bdd
  - bricks
  - sources_d_informations
  - lbp
---

# Architecture de Mission Ops LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> Référence canonique des **4 BDDs structurelles** du domaine Mission Ops, instancié à chaque mission consultant.
> Mission Ops est un domaine **co-égal** au Brain et au Digital Twin (cf. D-023), gouverné par 4 BDDs : `Sources d'informations`, `Meetings`, `Actions LBP`, `Bricks`.
> Les schémas détaillés (champs, propriétés, relations) vivent dans les **Manuels de BDD** sous `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Mission Ops\`. Ce fichier porte la vue d'ensemble structurante.
> Dernière mise à jour : 30-04-2026 - création post-Phase B test Twin+MO DeepSecAI v0 (51 fiches sur la maquette Notion).

---

## 1. Préambule - qu'est-ce que Mission Ops ?

**Mission Ops** est le domaine de **gouvernance opérationnelle des missions de conseil LBP**. Il porte la trace structurée de ce qui se passe pendant une mission (sources collectées, meetings tenus, actions exécutées par le consultant LBP, livrables produits).

### Frontières avec les 2 autres domaines

| Domaine | Rôle | Stack cible | Évolution pendant mission |
|---|---|---|---|
| **Brain** | Méta - référentiel doctrinal LBP (manuels, taxonomies, méthodes, templates, prompts, agents, outils). Stable, évolue **hors mission**. | Notion (à moyen terme) | ❌ Non (D-019, D-021) |
| **Digital Twin** | Représentation structurée d'**une organisation cliente** (objets ontologiques, relations, 5D). Instancié par mission. | Supabase (cible D-023) | ✅ Oui (peuplement progressif) |
| **Mission Ops** | Gouvernance opérationnelle de la **mission elle-même** (sources, meetings, actions consultant, livrables). | Supabase (cible D-023) | ✅ Oui (en flux continu) |

### Les 3 articulations doctrinales

1. **Brain → Mission Ops** : lecture seule. MO consomme les templates de bricks (`TPL_BRICK_*`), les méthodes (`METH_*`), les prompts (`PRMPT_*`), les agents (`AGT_*`) et les outils (`OUT_*`) du Brain. Aucune écriture ascendante (D-019, D-021).
2. **Mission Ops ↔ Digital Twin** : articulation **par les Bricks** (D-018). Une brick MO peut être la « note avancée » d'une fiche Twin (profil organisationnel, analyse, livrable). Les `Sources d'informations` MO sont l'**origine traçable** des fiches Twin (régime « extraction directe » C-018).
3. **Mission Ops ↔ Mission Ops** : intra-MO, les 4 BDDs ont des relations bidirectionnelles serrées (Meetings ↔ Actions ↔ Bricks ↔ Sources).

### Régime de connaissance

Mission Ops est de régime **opérationnel**, distinct du régime ontologique du Twin. Conséquences (D-022) :
- Frontmatter MO **plus mince** que Twin (pas de `ui_family`, `officiality_regime`, `has_advanced_note`, `aliases`)
- Pas de couche 5D (le 5D est un prisme Twin, pas MO)
- Pas de sandboxes MO (toutes les fiches sont opérationnelles par construction)
- Codification orientée occurrence : `MTG-XX-DATE`, `ACT-XX-NNN`, `BRK_<mission>_<brick>_<discriminant>_<rev>`

---

## 2. Principes structurants

Mission Ops est gouverné par **6 principes cardinaux** propres :

1. **Trace de mission, pas vérité organisationnelle** - MO documente ce qui s'est passé pendant la mission (qui a parlé, quoi a été fait, quels livrables ont été produits). La vérité organisationnelle vit dans le Twin.
2. **Sources = origine traçable de tout** - toute fiche MO ou Twin remontant à une mission doit pouvoir être reliée à au moins une `Source d'information` (R-001 transitif).
3. **Bricks = unité documentaire pivot** (D-018) - les bricks sont à la fois livrables MO et notes avancées Twin. Elles sont le **pont** structurel entre les deux domaines.
4. **Actions LBP = activité du consultant uniquement** - pas l'activité du client (qui se modélise via `Actions détectées` dans le Twin). Distinction stricte : `Actions LBP` = ce que LE CONSULTANT fait pendant la mission.
5. **Une mission = une instance MO complète** - chaque mission a son propre périmètre MO instancié (pas de fiches MO partagées entre missions, sauf cas exceptionnel à arbitrer).
6. **Régime opérationnel sobre** - MO n'a pas de couche analytique (5D, rollups complexes, chaînes de transformation). Son rôle est traçabilité + pilotage opérationnel, pas analyse organisationnelle.

---

## 3. Tableau maître canonique des 4 BDDs Mission Ops

| # | BDD | Objet principal | Rôle | Mode d'alimentation | Régime relationnel |
|---|---|---|---|---|---|
| 1 | `Sources d'informations` | Pièce documentaire / entretien / artefact | Satellite de traçabilité, pivot MO ↔ Twin | Curation consultant + import | Relations bidir vers presque toutes les BDDs Twin + bidir avec Bricks MO |
| 2 | `Meetings` | Rendez-vous tenu pendant la mission | Trace des interactions consultant ↔ client | Flux continu pendant la mission | Bidir avec Actions LBP + monodir vers Individus Twin |
| 3 | `Actions LBP` | Action du consultant pendant la mission | Pilotage opérationnel de la mission | Flux continu (backlog vivant) | Bidir avec Meetings + Bricks + auto-rel (Activité ↔ Action) + monodir vers Individus Twin |
| 4 | `Bricks` | Livrable / unité documentaire produite | Production documentaire de la mission | Flux continu (livrables itératifs) | Bidir avec Actions LBP + Sources d'informations |

### Détails par BDD

#### 3.1 Sources d'informations

**Rôle pivot** - c'est la BDD **la plus articulatoire** de Mission Ops. Elle est :
- L'**origine** de toutes les fiches Twin (chaîne d'extraction directe, C-018)
- La **preuve documentaire** de toutes les bricks MO (chaque brick est documentée par une ou plusieurs sources)
- Le **point d'entrée** d'une mission depuis l'extérieur (entretien transcrit, document client, export système, observation terrain)

**Champs caractéristiques** : `ID externe` (`SRC-XXX-NNN`), `Date de la source`, `Format d'origine`, `Provenance`, `Émetteur / Auteur`, `Confiance / solidité` (échelle 0-5), `Confidentialité`, `Cibles d'extraction recommandées` (multi-select : Individus / Collectifs / Postes / Actifs / Environnements / Événements / Actions détectées / Enjeux), `Notes du consultant`.

**Relations clés** : bidirectionnelles vers la quasi-totalité des BDDs Twin (`extrait (individus)`, `extrait (collectifs)`, `extrait (organisations)`, etc.) + bidir vers `Bricks` (`documente (bricks)`).

#### 3.2 Meetings

**Rôle** - trace structurée de chaque rendez-vous tenu pendant la mission (entretien individuel, atelier collaboratif, kickoff, comité, restitution, validation).

**Champs caractéristiques** : `Code` (`MTG-<TYPE>-<DISCRIMINANT>-<DATE-ISO>`), `Type de meeting` (taxo MTG.TYPE), `Format` (visio / présentiel / hybride), `Date/heure`, `Durée (min)`, `Lieu / outil`, `Lien calendrier (Google Calendar)`, `Objet du meeting`, `Agenda`, `Hypothèses / questions à clarifier`, `Résultats et décisions`, `Enregistrement (oui/non)`, `Statut d'exécution` (taxo OPS.STATUS).

**Relations clés** : bidir vers `Actions LBP` (3 régimes : `est préparé par`, `est exécuté avec`, `est suivi par`) + monodir vers `Individus` Twin (`réunit (individus)`).

**Note** : la relation vers `Individus` est **monodirectionnelle** vers le Twin pour ne pas polluer le Twin avec des traces de mission (R-013 transposée à MO).

#### 3.3 Actions LBP

**Rôle** - pilotage opérationnel des actions exécutées **par le consultant LBP** pendant la mission. Distinct de `Actions détectées` (Twin) qui modélise l'agir observé chez le client.

**Champs caractéristiques** : `Code` (`ACT-<DISCRIMINANT>-<NNN-ou-DATE>`), `Type d'entrée` (Activité = lot / Action = atomique), `Famille d'action` (taxo OPS.ACTION_FAMILY : préparation de meeting / animation en direct / coordination / collecte / analyse / synthèse / administratif), `Responsable principal` (Consultant LBP / Client / Mixte), `Échéance`, `Date de clôture`, `Description et critères de done`, `utilise aussi en inputs`, `Statut d'exécution`.

**Relations clés** : bidir vers `Meetings` (3 régimes : `prépare`, `se déroule pendant`, `assure le suivi de`) + bidir vers `Bricks` (`utilise` et `produit`) + auto-rel `appartient à (activité)` ↔ `contient (actions)` (structure macro/micro) + monodir vers `Individus` Twin (`est assignée à`).

**Couche calculée** : 3 rollups d'avancement (Nb actions, Nb actions terminées, Avancement %).

#### 3.4 Bricks

**Rôle pivot** - unité documentaire produite par la mission. Elles sont à la fois :
- Livrable MO (output d'une `Action LBP`, doit être traçable)
- Note avancée Twin (D-018) - peut détailler une fiche Twin (profil organisationnel, analyse 3P, etc.)

**Champs caractéristiques** : `Brick ID` (titre, format `BRK_<mission>_<brick>_<discriminant>_<rev>`), `Nom canonique` (humain), `Purpose`, `Famille de brick` (taxo BRICK.FAMILY : profil / meeting / compte-rendu / analyse / livrable / correspondance / sources / glossaire / socle client / socle mission), `Generated at`, `Version` (R01/R02/...), `mission_code`, `brick_code`, `Discriminant`, `rev`, `Lien drive`, `Utilise aussi en inputs`, `Statut d'exécution`.

**Relations clés** : bidir vers `Actions LBP` (`est produite par`, `est utilisée par`) + bidir vers `Sources d'informations` (`est documentée par`).

**Codification** (cf. CODIFICATION_LBP.md à venir) : grammaire stricte `BRK_<mission_code>_<brick_code>_<discriminant>_<rev>`, segments éclatés en 4 propriétés Notion séparées.

---

## 4. Cartographie des objets Mission Ops

Définitions canoniques et frontières (à ne pas confondre avec d'autres objets).

| Objet MO | Définition | Ne doit pas être confondu avec |
|---|---|---|
| **Source d'information** | Pièce documentaire / entretien / artefact servant de preuve primaire | Actif (Twin), Glossaire (Twin), Brick |
| **Meeting** | Rendez-vous tenu pendant la mission, daté et structuré | Événement (Twin) ; un meeting est une trace de mission, un événement Twin est un repère organisationnel |
| **Action LBP** | Activité ou action exécutée par le consultant LBP | Action détectée (Twin) - qui modélise l'agir observé chez le client |
| **Activité (Actions LBP)** | Lot de travail regroupant N actions atomiques | Initiative organisationnelle (Twin) - qui est un effort temporaire **chez le client** |
| **Brick** | Livrable documentaire produit ou utilisé par une action de mission | Note avancée d'objet Twin (rôle pivot, D-018) ; document Brain (template) |

---

## 5. Architecture logique d'une BDD Mission Ops (4 couches sobres)

Le régime MO est plus sobre que le régime Twin. Une BDD MO a typiquement 4 couches (au lieu des 5 du Twin) :

| Couche | Contenu | Question à laquelle elle répond |
|---|---|---|
| 1. Propriétés génériques | Nom/Code, Statut de l'objet, Notes du consultant, Created/Updated | Cette fiche est-elle claire et tracée ? |
| 2. Propriétés spécifiques | Champs propres à l'objet (Type, Format, Famille, Brick ID, etc.) | Qu'est-ce qui caractérise cette occurrence MO ? |
| 3. Relations + jumelles textes | Liens bidir intra-MO + monodir Twin + jumelles textes | À quoi cette fiche est-elle reliée dans la mission ? |
| 4. Couche pilotage opérationnel | `Statut d'exécution` (OPS.STATUS) | Où en est-on dans le cycle de vie opérationnel ? |
| 5. (Couche calculée - optionnelle) | Rollups d'avancement (Actions LBP uniquement) | Quel est le taux d'avancement d'une activité ? |

**Différences avec Twin** :
- ❌ Pas de couche 5D (le 5D est un prisme Twin)
- ❌ Pas de chaînes de transformation D-009 (le D-009 est un paradigme Twin)
- ❌ Pas de sandboxes (pas de besoin de qualification progressive en MO)
- ✅ Couche pilotage opérationnel (OPS.STATUS) propre à MO
- ✅ Codification orientée occurrence (codes datés, instanciés par mission)

---

## 6. Articulation Mission Ops ↔ Digital Twin

C'est l'articulation la plus dense. Elle se fait par **3 ponts** :

### 6.1 Pont par les Sources d'informations (origine traçable)

Toute fiche Twin issue d'une mission doit être reliée à au moins une `Source d'information` MO (régime « extraction directe » C-018, sauf BDDs analytiques en régime « consolidé/dérivé »).

```
Sources d'informations (MO)
    │
    └── extrait (individus) ─── Individus (Twin)
    └── extrait (collectifs) ── Collectifs (Twin)
    └── extrait (organisations) ── Organisations (Twin)
    └── extrait (postes) ───── Postes (Twin)
    └── ... (tous les objets Twin du socle structurel + observation)
```

Les BDDs Twin de **régime consolidé/dérivé** (Processus, Pratiques, Principes, Capacités, Modulateurs, Problématiques, OKR, Indicateurs) **n'ont pas** de relation directe vers Sources - leur traçabilité est transitive via les BDDs amont (C-018).

### 6.2 Pont par les Bricks (notes avancées, D-018)

Une brick MO peut servir de **note avancée** à une fiche Twin :
- Brick `Profil` → fiche `Organisations` ou `Collectifs` Twin (profil organisationnel synthétique)
- Brick `Analyse` → fiche analytique (Processus / Pratique / Capacité)
- Brick `Compte-rendu` → fiche `Meeting` MO (CR interne) - articulation intra-MO
- Brick `Livrable` → restitution multi-fiches Twin (note de synthèse client)

L'articulation se fait par le champ `Lien vers la note avancée` côté Twin (URL Drive de la brick) ou par référence textuelle dans la brick.

### 6.3 Pont par les Actions LBP (production)

Les Actions LBP **produisent** des bricks (`produit (bricks)`) qui peuvent **alimenter** ou **modifier** des fiches Twin. Exemple typique :
- Action « Produire profil organisationnel » → produit Brick `BRK_<mission>_PRF-ORG_<DISCRIMINANT>_R01` → la brick devient note avancée de la fiche `Organisations` Twin correspondante.

Cette articulation est **descendante** (MO produit, Twin reçoit). Le Twin ne « commande » jamais MO.

---

## 7. Articulation Brain ↔ Mission Ops (lecture seule)

Mission Ops consomme plusieurs objets Brain, mais **n'écrit jamais** dedans (D-019, D-021).

| Objet Brain consommé par MO | Usage en MO |
|---|---|
| `Templates de Bricks` (`TPL_BRICK_*`) | Structure des bricks instanciées (D-018) |
| `Méthodes LBP` (`METH_*`) | Cadre de conduite des actions (ex. méthode 3P) |
| `Prompts` (`PRMPT_*`) | Instructions agents pour exécution actions |
| `Agents LBP` (`AGT_*`) | KONTEXT pour orchestration mission (D-021) |
| `Outils externes` (`OUT_*`) | Outils mobilisés pendant les actions |
| `Logic blocks` (`LGBLK_*`) | Blocs de raisonnement réutilisables |
| `Glossaire LBP` + `Notes de concept` | Référentiel sémantique LBP |

**Mécanique de consommation** : la référence se fait par **code stable** (R-054) - pas par relation cross-stack. Au moment de l'instanciation MO (création d'une brick par exemple), le code template (`TPL_BRICK_PRF_ORG`) est inscrit en référence textuelle dans la fiche brick. La structure du template est **lue** depuis le Brain (lecture seule).

**Frontière infranchissable** : KONTEXT (l'agent MO) **ne peut pas** appeler Brain architect (D-021). Si une évolution Brain est nécessaire, elle est **flaggée** comme remontée hors mission.

---

## 8. Stack technique cible et maquette de validation

### 8.1 Stack cible (D-023)

- **Mission Ops = Supabase** (production cible)
- Volumes attendus : N fiches MO par mission × M missions actives = volumétrie potentiellement importante (centaines à milliers de fiches MO actives en parallèle).
- Performance : lecture/écriture critique pour le confort consultant.
- Schéma stable : validé via la maquette Notion test (Phase B 30-04-2026).

### 8.2 Maquette Notion (Phase B test, 30-04-2026)

La maquette Notion actuelle est une **fixture de validation de schéma**, pas une production. Elle a permis :
- Validation des 4 schémas BDDs MO (cf. test Phase B, 51 fiches sur 17 BDDs Twin+MO)
- Validation des relations bidir auto-propagées par Notion (Meetings ↔ Actions, Actions ↔ Bricks, Sources ↔ Bricks)
- Capitalisation des patterns de remplissage (cf. `TEST_TWIN_OPS_PLAYBOOK.md`)
- Identification des quirks techniques (apostrophes typographiques R-052, format expanded date, JSON multi-select)

**Référence** : page test `352e1a18653c8079b1b6edd1c456aaeb` (BDD test - 26-04-2026 - Digital Twin update).

### 8.3 Portage Supabase (chantier post-Phase C)

Le portage de la maquette Notion vers Supabase est un **chantier dédié** à cadrer après la Phase C (figement Brain). Périmètre prévu :
- Modélisation Postgres des 4 BDDs MO + relations (foreign keys)
- Migration des taxonomies LBP en tables de référence
- Préservation des patterns de codification (R-054 + grammaire bricks)
- Workflows d'instanciation par mission (création d'un schéma ou d'une partition par mission)
- Synchronisation avec le Brain (lecture seule des templates)

---

## 9. Liens vers la documentation détaillée

### Manuels de BDD (source de vérité, R-001)

Sous `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Mission Ops\` :
- `Manuel de BDD - Sources d'informations.md`
- `Manuel de BDD - Meetings.md`
- `Manuel de BDD - Actions LBP.md`
- `Manuel de BDD - Bricks.md`

### WR-RD (instructions champ par champ pour agents)

Sous `Manuels de BDD/Mission Ops/WR-RD/` :
- `WR-RD - Sources d'informations.md`
- `WR-RD - Meetings.md`
- `WR-RD - Actions LBP.md`
- `WR-RD - Bricks.md`

### Templates de bricks consommés par Mission Ops

Sous `Architecture data/Templates de bricks/` (Brain) - `TPL_BRICK_*`. Liste de référence dans la BDD Notion `Templates de bricks` du Brain.

### Apprentissages opérationnels

- `refs/TEST_TWIN_OPS_PLAYBOOK.md` - playbook stabilisé post-Phase B test (logiques de remplissage, patterns, anomalies, quirks techniques).

### Décisions et règles structurantes

- `refs/DECISIONS_LBP.md` - D-018 (bricks=notes avancées), D-019 (isolation Brain ↔ MO/Twin), D-021 (3 agents), D-022 (frontmatters Twin/MO différenciés), D-023 (MO co-égal + stack Notion/Supabase)
- `refs/RULES_LBP.md` - section dédiée Mission Ops (à enrichir au fur et à mesure)
- `refs/WORKFLOWS_LBP.md` - WF-008 (propagation d'impacts), futurs WF-MO-XXX à formaliser

---

## 10. Roadmap d'évolution (post bundle)

| Sujet | Statut | Cible |
|---|---|---|
| Portage Supabase Mission Ops | Chantier post-Phase C | À cadrer |
| Workflows MO dédiés (WF-MO-XXX) | À formaliser | Au fur et à mesure |
| Cogitation propriété « Régime de l'entité » | Backlog post-test | Phase C |
| Articulation 3 agents (D-021) avec MO en production | À cadrer | Post-Chantier P |
| Industrialisation pipeline d'instanciation MO depuis JSON | À cadrer | Post-Phase C |

---

> Dernière mise à jour : 30-04-2026 - création post-Phase B test Twin+MO DeepSecAI v0. Spécifications stabilisées sur la maquette Notion (51 fiches), prêtes pour portage Supabase ultérieur.
