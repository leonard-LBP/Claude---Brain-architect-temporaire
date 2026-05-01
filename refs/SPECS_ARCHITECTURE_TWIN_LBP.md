---
# === Identité ===
title: "Specs Architecture Digital Twin LBP - Modèle conceptuel des 28 BDDs Twin"
doc_type: doc_meta
code: "CHRT_SPECS_TWIN_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
created_at: "24-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Modèle conceptuel des 28 BDDs Digital Twin v2 (22 officielles + 6 sandboxes) : 8 principes cardinaux, tableau maître canonique, cartographie objets ontologiques, architecture logique en 5 couches, chaînes de transformation D-009, 11 moteurs analytiques, 11 traversées à forte valeur."
purpose: "Servir de référence canonique du modèle Twin. Pour la doctrine narrative détaillée (régimes de structuration, gouvernance, merge/consolidation/promotion) voir DOCTRINE_TWIN_LBP."
tags:
  - doc_meta
  - specs
  - architecture
  - digital_twin
  - bdd
  - 5d
  - sandboxes
  - lbp
---

# SPECS - Architecture Digital Twin LBP

> Référence canonique des **28 BDD** du Digital Twin v2 (22 officielles + 6 sandboxes).
> Source doctrinale : `Panorama V2 - Macro-architecture, chaînes de valeur et logique analytique du Digital Twin LBP v3`.
> **Note** : `Sources d'informations` n'est PAS une BDD Twin mais une BDD **Mission Ops** (comme `Meetings`, `Actions LBP`, `Bricks`). Le Panorama l'inclut dans son tableau maître parce qu'elle joue un rôle de satellite de traçabilité pour les objets Twin, mais son instance opérationnelle vit en Mission Ops.
> Les schémas Notion détaillés (champs, propriétés, relations) vivent dans les **Manuels de BDD** (vault Architecture data). Ce fichier porte la vue d'ensemble structurante.
> Dernière mise à jour : 24-04-2026 - retrait de Sources d'informations (Mission Ops)

---

## 1. Principes structurants

Le Digital Twin LBP est une **architecture de représentation structurée d'une organisation**, qui transforme preuves / observations / objets / relations en lectures systémiques exploitables pour diagnostic, pilotage et transformation.

Les 8 principes cardinaux (cf. Panorama §3) :

1. **Séparer preuve, qualification, consolidation et action** (R-012)
2. **Frontières fortes entre objets** (R-011)
3. **Relations réelles uniquement si gain analytique clair** (R-013)
4. **Sandboxes sans relations réelles sauf vers Sources** (R-014)
5. **5D = matrice de lecture, jamais preuve primaire** (R-016)
6. **Rollups et formules sobres, révélateurs** (R-017)
7. **Socle générique commun, grammaire d'écriture spécifique** (R-018)
8. **Tableau maître canonique tenu à jour** (R-025)

---

## 2. Tableau maître canonique des 28 BDD Twin

> Pour mémoire : `Sources d'informations` est Mission Ops (satellite de traçabilité transverse), cf. note en tête de document.

| # | BDD | Objet principal | Famille architecturale | Mode d'alimentation | Régime relationnel | Valeur systémique dominante |
|---|---|---|---|---|---|---|
| 1 | `Glossaire spécifique entreprise` | Terme / expression située | Socle sémantique | Curation / clarification | Relations réelles + jumelles textes | Stabiliser le langage client |
| 2 | `Journal des signaux` | Signal faible ou indice qualitatif | Observation qualitative amont | Extraction / lecture qualitative | Relations réelles + jumelles textes | Capter les indices faibles avant consolidation |
| 3 | `Actions détectées` | Action observée ou dite | Extraction factuelle | Extraction IA + revue | Relations réelles + jumelles textes | Matière brute du faire réel |
| 4 | `Enjeux` | Enjeu formulé | Extraction factuelle stratégique | Extraction IA + revue | Relations réelles + jumelles textes | Remonter besoins, tensions, objectifs, opportunités, craintes |
| 5 | `Organisations` | Organisation | Socle structurel institutionnel | Curation / structuration | Relations réelles + jumelles textes | Décrire les acteurs institués |
| 6 | `Relations inter-organisations` | Relation directionnelle entre deux organisations | BDD edge structurelle | Curation / structuration | Relations réelles + jumelles textes | Cartographier l'écosystème relationnel externe |
| 7 | `Collectifs` | Collectif opérant | Socle structurel social | Curation / structuration | Relations réelles + jumelles textes | Décrire les groupes humains où le travail se coordonne |
| 8 | `Individus` | Individu | Socle structurel humain | Extraction + curation | Relations réelles + jumelles textes | Rendre visibles les personnes significatives |
| 9 | `Postes` | Poste | Structure formelle | Curation / structuration | Relations réelles + jumelles textes | Décrire la charpente formelle des fonctions |
| 10 | `Actifs` | Actif | Supports / moyens | Curation / structuration | Relations réelles + jumelles textes | Rendre visibles supports, dépendances, vulnérabilités |
| 11 | `Environnements` | Environnement | Contextes / contraintes | Curation / structuration | Relations réelles + jumelles textes | Expliciter les cadres d'usage, d'exposition, de contrainte |
| 12 | `Événements` | Événement | Temps / trajectoire | Curation / structuration | Relations réelles + jumelles textes | Donner les jalons, bascules, épisodes structurants |
| 13 | `Initiatives organisationnelles` | Initiative organisationnelle | Mouvement / transformation | Curation / pilotage | Relations réelles + jumelles textes | Décrire les efforts temporaires structurés de transformation |
| 14 | `Processus candidats` | Processus candidat | Pivot de qualification | Analyse / consultant | Relations réelles + jumelles textes | Préparer la consolidation des fonctionnements |
| 15 | `Processus` | Processus | Fonctionnement consolidé | Analyse / consultant | Relations réelles + jumelles textes | Modéliser les fonctionnements structurés stabilisés |
| 16 | `Pratiques organisationnelles` | Pratique organisationnelle | Réel opérant consolidé | Analyse / consultant | Relations réelles + jumelles textes | Rendre visibles les patterns opérants récurrents |
| 17 | `Principes organisationnels` | Principe organisationnel | Couche normative | Analyse / consultant | Relations réelles + jumelles textes | Formaliser la couche normative du système |
| 18 | `Capacités organisationnelles` | Capacité organisationnelle | Couche capacitaire | Analyse / consultant | Relations réelles + jumelles textes | Rendre visibles les aptitudes collectives durables |
| 19 | `Problématiques` | Problématique | Couche diagnostique | Analyse / consultant | Relations réelles + jumelles textes | Produire les nœuds diagnostiques consolidés |
| 20 | `OKR` | OKR | Couche de pilotage | Analyse / consultant | Relations réelles + jumelles textes | Relier diagnostic, pilotage, transformation |
| 21 | `Indicateurs` | Indicateur | Couche de mesure | Analyse / consultant | Relations réelles + jumelles textes | Objectiver la performance, les écarts, la progression |
| 22 | `Modulateurs` | Modulateur | Couche d'effectivité | Référentiel préchargé + évaluation consultant | Relations réelles + jumelles textes | Expliquer les conditions d'effectivité, les plafonds |
| 23 | `Capacités métier candidates (sandbox)` | Capacité métier candidate | Sandbox d'exploration | Extraction / analyse exploratoire | Jumelles textes + relation à `Sources d'informations` | Tester des capacités pressenties |
| 24 | `OKR (sandbox)` | OKR exploratoire | Sandbox d'exploration | Analyse exploratoire | Jumelles textes + relation à `Sources d'informations` | Tester des objectifs avant promotion |
| 25 | `Pratiques organisationnelles (sandbox)` | Pratique exploratoire | Sandbox d'exploration | Extraction / analyse exploratoire | Jumelles textes + relation à `Sources d'informations` | Tester des pratiques pressenties |
| 26 | `Principes organisationnels (sandbox)` | Principe exploratoire | Sandbox d'exploration | Analyse exploratoire | Jumelles textes + relation à `Sources d'informations` | Tester des principes pressentis |
| 27 | `Problématiques (sandbox)` | Problématique exploratoire | Sandbox d'exploration | Analyse exploratoire / consolidation initiale | Jumelles textes + relation à `Sources d'informations` | Tester des formulations diagnostiques instables |
| 28 | `Processus candidats (sandbox)` | Processus candidat exploratoire | Sandbox d'exploration | Extraction / analyse exploratoire | Jumelles textes + relation à `Sources d'informations` | Tester des regroupements fonctionnels pressentis |

---

## 3. Familles architecturales (regroupement par régime)

| Famille | BDD concernées | Fonction architecturale |
|---------|----------------|-------------------------|
| **Socle sémantique** | Glossaire spécifique entreprise | Stabiliser vocabulaire et expressions du client |
| **Extraction factuelle** | Journal des signaux, Actions détectées, Enjeux | Capter la matière amont |
| **Socle structurel** | Organisations, Relations inter-organisations, Collectifs, Individus, Postes, Actifs, Environnements, Événements | Charpente structurelle du Twin |
| **Mouvement / transformation** | Initiatives organisationnelles | Relier au changement en cours |
| **Pivot de qualification** | Processus candidats | Sas de qualification fonctionnelle |
| **Couche analytique officielle** | Processus, Pratiques, Principes, Capacités, Problématiques, OKR, Indicateurs, Modulateurs | Couche analytique, explicative, pilotable, actionnable |
| **Sandboxes exploratoires** | 6 sandboxes spécialisées | Sas d'exploration sans relations réelles |

---

## 4. Cartographie des objets ontologiques

Définitions canoniques et frontières (cf. R-011). Chaque objet ne doit pas être confondu avec ses voisins.

| Objet | Définition architecturale | Ne doit pas être confondu avec |
|-------|---------------------------|-------------------------------|
| **Source d'information** | Pièce documentaire, entretien, note, support, transcript ou artefact servant de preuve primaire | Actif, glossaire, événement |
| **Terme de glossaire** | Unité sémantique stabilisée dans le contexte client | Principe, capacité, actif, nom de projet |
| **Signal** | Indice faible ou qualitatif encore peu consolidé | Enjeu, problématique, événement |
| **Organisation** | Acteur collectif institué, doté d'une existence institutionnelle ou juridique | Collectif, poste, relation inter-organisations |
| **Relation inter-organisations** | Lien structurant directionnel entre deux organisations distinctes | Hiérarchie institutionnelle, simple mention de partenaire |
| **Collectif** | Groupe humain opérant, stable ou temporaire, où du travail se coordonne | Organisation, poste, initiative |
| **Individu** | Personne physique significative dans le système étudié | Poste, collectif |
| **Poste** | Position formelle contextualisée, indépendante de son titulaire | Individu, rôle informel, collectif |
| **Actif** | Objet non humain gouvernable, mobilisable, administrable ou transformable | Environnement, source, pratique |
| **Environnement** | Cadre d'usage, d'exposition ou de contrainte | Actif, événement |
| **Événement** | Repère temporel daté ou datable, ponctuel ou borné | Initiative, action, simple contexte |
| **Initiative organisationnelle** | Effort intentionnel, temporaire et délimité | Événement, collectif, pratique |
| **Action détectée** | Unité minimale de faire observé ou dit | Pratique, processus |
| **Enjeu** | Formulation structurée d'un besoin, tension, opportunité, objectif ou crainte | Problématique consolidée, signal faible |
| **Processus candidat** | Regroupement plausible d'actions avant consolidation | Processus consolidé, simple suite d'actions sans cohérence |
| **Processus** | Fonctionnement structuré, stabilisé, doté d'une logique de transformation | Pratique, initiative |
| **Pratique organisationnelle** | Pattern opérant récurrent produisant une valeur durable | Action isolée, processus, principe |
| **Principe organisationnel** | Intention normative stable guidant des arbitrages récurrents | Valeur décorative, règle locale, pratique |
| **Capacité organisationnelle** | Aptitude collective durable que le système possède ou doit renforcer | Pratique, projet, poste |
| **Problématique** | Nœud diagnostique consolidé et structurant | Enjeu, signal, symptôme isolé |
| **OKR** | Objectif piloté et structuré, orienté résultats | Initiative, indicateur, principe |
| **Indicateur** | Mesure, proxy ou dispositif de suivi | Objectif, problème, actif |
| **Modulateur** | Condition d'effectivité transversale influençant fortement pratiques et capacités | Capacité, pratique, problématique |

---

## 5. Architecture logique d'une BDD (5 couches)

Cf. R-019. Une BDD importante du Twin est pensée comme un empilement cohérent :

| Couche | Contenu | Question à laquelle elle répond |
|--------|---------|----------------------------------|
| 1. Propriétés génériques | Nom, statut, aliases, description, indices, logs, traces de merge | Cette fiche est-elle claire, traçable et gouvernable ? |
| 2. Relations + jumelles textes | Liens officiels et formulations observées | À quels autres objets est-elle liée, et comment ces liens ont-ils été observés ? |
| 3. Propriétés spécifiques | Champs qui donnent à chaque objet sa valeur analytique propre | Qu'est-ce qui fait la singularité analytique de cet objet ? |
| 4. Couche 5D | Contribution / exposition / dépendance / causalité-impact-risque / pilotage-mesure | Où cet objet agit-il, dépend-il, expose-t-il ou mesure-t-il le système ? |
| 5. Couche calculée | Rollups + formules | Que faut-il voir rapidement sans relire toute la fiche ? |

**Variantes d'intensité par famille** :
- **Registre / satellite** : peu de 5D, peu de calculée (cf. Sources d'informations)
- **Socle sémantique** : forte générique et spécifique, peu de 5D/calculée (cf. Glossaire)
- **Extraction factuelle** : relations et jumelles textes très importantes, 5D comme orientation
- **Socle structurel** : relations nombreuses, propriétés spécifiques de portée/criticité/temporalité, rollups très utiles
- **Pivots / couche analytique** : forte intensité sur propriétés spécifiques, 5D et formules très utiles

---

## 6. Chaînes de transformation de la connaissance

Cf. D-009. Le Twin produit de la valeur parce qu'il organise des chaînes de passage entre régimes :

```
Sources ─────────────────► toutes les BDD documentées        [auditabilité]
Glossaire ────────────────► meilleure extraction/consolidation [clarté sémantique]
Journal signaux → Enjeux                                      [signal → stratégique]
Enjeux → Problématiques                                       [besoin → diagnostic]
Actions → Processus candidats → Processus                     [brut → structuré]
Actions → Pratiques organisationnelles                        [geste → pattern]
Actions → Initiatives organisationnelles                      [effort détecté]
Pratiques → Capacités                                         [pattern → aptitude durable]
Principes → Pratiques                                         [norme → incarnation, cœur 3P]
Problématiques → OKR → Indicateurs                            [diagnostic → pilotage → mesure]
OKR → Initiatives                                             [pilotage → action]
Modulateurs ↔ Pratiques ↔ Capacités                           [conditions d'effectivité]
sandbox → Sources → indices → BDD officielle cible            [exploration → promotion]
```

---

## 7. Moteurs analytiques (11 lectures)

Le Twin peut être lu selon 11 moteurs complémentaires, chacun répondant à une famille de questions :

| Moteur | BDD noyau | Question typique |
|--------|-----------|------------------|
| Lecture structurelle | Organisations, Collectifs, Individus, Postes, Actifs | Qui existe, avec quelle structure ? |
| Lecture du fonctionnement réel | Actions, Processus candidats, Processus, Pratiques | Comment cela fonctionne-t-il réellement ? |
| Lecture diagnostique | Journal des signaux, Enjeux, Problématiques | Qu'est-ce qui bloque, se tend, inquiète ? |
| Lecture normative (3P) | Principes, Pratiques | Ce que dit l'orga se retrouve-t-il dans le réel ? |
| Lecture capacitaire | Capacités, Pratiques, Initiatives, Indicateurs | Que sait durablement faire le système ? |
| Lecture contextuelle et temporelle | Environnements, Événements, Relations inter-organisations | Dans quel cadre et à quel moment ? |
| Lecture de pilotage | OKR, Initiatives organisationnelles | Que le système vise-t-il à transformer ? |
| Lecture de mesure | Indicateurs + liés | Qu'est-ce qui est réellement objectivé ? |
| Lecture 5D | Presque toutes | Où cet objet agit-il, dépend-il, expose-t-il ? |
| Lecture des conditions d'effectivité | Modulateurs + Pratiques/Capacités/Actifs/Organisations | Pourquoi ça tient ou ça plafonne ? |
| Lecture calculée | Rollups, formules | Quelles synthèses sans relire toutes les fiches ? |

---

## 8. Traversées analytiques à forte valeur

Cf. Panorama §12. Le Twin devient puissant quand on l'interroge par traversées :

1. **Structure formelle et vivante** : `Organisation → Collectif → Poste → Individu`
2. **Dépendances de fonctionnement** : `Collectif/Processus/Pratique → Actif → Environnement`
3. **Écosystème externe** : `Organisation → Relation inter-organisations → Organisation`
4. **Transformation vivante** : `Organisation/Collectif/Poste/Individu → Initiative → Événement`
5. **Passage du brut à l'analytique** : `Actions détectées → Processus candidats / Pratiques / Initiatives`
6. **Chaîne diagnostic → pilotage** : `Journal des signaux → Enjeux → Problématiques → OKR → Indicateurs`
7. **Qui porte réellement le système ?** : `Collectifs ↔ Individus ↔ Postes ↔ Initiatives ↔ Pratiques`
8. **Angles morts de mesure** : `Problématiques/Capacités/Pratiques/Processus/OKR → Indicateurs`
9. **Où agir en priorité ?** : `Problématiques → Collectifs/Organisations affectés → Capacités en écart → OKR/Initiatives/Indicateurs`
10. **Quelles pratiques pour faire monter une capacité ?** : `Capacités → Pratiques → Modulateurs → Initiatives → Indicateurs`
11. **Une hypothèse doit-elle sortir du sandbox ?** : `sandbox → Sources → indices → BDD officielle cible`

---

## 9. Liens vers la documentation détaillée

Les schémas Notion complets (champs, relations, rollups, formules) sont portés par les **Manuels de BDD** dans le vault "Architecture data". Une fois les nouveaux manuels intégrés au vault, cette section listera les liens.

- Source doctrinale complète : `Panorama V2 v3` (non encore intégré au vault)
- **Doctrine détaillée Twin** (régimes de structuration des données, 15 chaînes de transformation détaillées, gouvernance Twin, doctrine merge/consolidation/promotion, critères sandbox→officiel) : `refs/DOCTRINE_TWIN_LBP.md` (v4.0 - refonte du Panorama V2 v3 du 22-04-2026, mise à jour 01-05-2026)
- Manuels de BDD : à intégrer dans `Architecture data/Manuels de BDD/Digital Twin/`
- Règles gouvernant l'architecture : `refs/RULES_LBP.md` section 3
- Décisions structurantes : `refs/DECISIONS_LBP.md` D-002 à D-009
