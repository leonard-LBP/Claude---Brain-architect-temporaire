# Décisions architecturales

> Ce fichier trace les choix structurants qui ne sont pas des règles à appliquer, mais des décisions qui contextualisent l'écosystème.
> Chaque décision a un ID stable (D-XXX) et documente le *pourquoi* du choix, pas juste le *quoi*.
> Utile pour comprendre l'histoire de l'architecture et retracer les raisonnements.
> Dernière mise à jour : 2026-04-24 — ajout D-002 à D-009 (Panorama V2 v3 du Twin)

---

## Format d'une décision

```markdown
### D-XXX : Titre de la décision

- **Date** : YYYY-MM-DD
- **Statut** : Proposée / Adoptée / Appliquée / Révisée / Abandonnée
- **Portée** : Brain / Twin / Mission Ops / Transverse
- **Contexte** : situation qui a appelé la décision
- **Options envisagées** : alternatives considérées
- **Choix retenu** : ce qu'on a décidé
- **Conséquences** : impacts (positifs, négatifs, ouverts)
- **Règles associées** : liens vers RULES.md si applicable
```

---

## Sommaire

- [1. Décisions structurantes (architecture)](#1-décisions-structurantes)
- [2. Décisions de gouvernance](#2-décisions-de-gouvernance)
- [3. Décisions de mise en œuvre](#3-décisions-de-mise-en-œuvre)

---

## 1. Décisions structurantes

*Décisions qui changent la forme de l'écosystème (nouveaux objets, nouvelles BDD, refontes).*

### D-002 : Scission UO → Organisation + Collectif

- **Date** : 2026-04-22 (formalisée dans Panorama V2 v3)
- **Statut** : Adoptée (changements faits par Leonard, intégration dans le vault à venir)
- **Portée** : Twin
- **Contexte** : La BDD `Unités Organisationnelles` mélangeait deux natures d'objets ontologiquement distinctes — entités juridiques instituées et groupements humains opérants. Cette confusion produisait des analyses imprécises (ex: un "département" rangé au même niveau qu'une "SA").
- **Options envisagées** :
  - Garder UO avec un champ "type" (juridique vs opérant) : simple mais laisse la confusion structurelle.
  - Scinder en deux BDD distinctes : plus rigoureux, permet des relations et propriétés spécifiques à chaque nature.
  - Créer une hiérarchie de sous-types : trop complexe pour le gain.
- **Choix retenu** : Scinder en deux BDD canoniques :
  - `Organisations` = acteur collectif institué, doté d'une existence juridique/institutionnelle
  - `Collectifs` = groupe humain opérant, stable ou temporaire, où du travail se coordonne
- **Conséquences** :
  - ✅ Frontières ontologiques nettes (cf. R-011)
  - ✅ Ouvre la voie à une BDD edge `Relations inter-organisations` (cf. D-006) et à des relations propres Organisation→Collectif
  - ⚠️ Archivage de l'ancienne UO + migration des entrées existantes à prévoir
  - ⚠️ Mise à jour des prompts maîtres et logic blocks qui référençaient UO
- **Règles associées** : R-011 (frontières fortes)

### D-003 : Renommage Ressources → Actifs

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin + Brain (propagation dans docs)
- **Contexte** : Le terme "Ressources" était ambigu — confondu avec "ressources humaines", "ressources financières", ou simple support. Il ne traduisait pas la nature gouvernable et administrable de l'objet.
- **Options envisagées** :
  - Garder "Ressources" + préciser dans la description : ne résout pas l'ambiguïté perçue.
  - Renommer en "Actifs" : terme plus précis, aligné sur une notion d'objet mobilisable/gouvernable.
  - Terme plus spécialisé (ex: "Moyens", "Supports") : moins générique, limitant.
- **Choix retenu** : "Actifs" — objet non humain gouvernable, mobilisable, administrable ou transformable.
- **Conséquences** :
  - ✅ Frontière clarifiée avec Environnements (cadre d'usage) et Sources (artefact de preuve)
  - ✅ Ouvre la voie à des propriétés spécifiques : type, criticité, substituabilité, cycle de vie
  - ⚠️ Mise à jour de tous les docs référençant "Ressources"
  - ⚠️ Mise à jour taxonomies, manuels, prompts maîtres, logic blocks
- **Règles associées** : R-011 (frontières fortes)

### D-004 : Renommage Rôles officiels → Postes

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Avec "Rôles officiels", un individu se retrouvait avec plusieurs rôles rattachés, générant du bruit et de la confusion entre fonction formelle et responsabilités multiples. Le terme "rôle" était aussi flou (officiel vs informel, formel vs opératoire).
- **Options envisagées** :
  - Garder "Rôles officiels" + règle "1 rôle principal par individu" : laisse la friction terminologique.
  - Renommer en "Postes" + règle 1 individu = 1 poste : plus net structurellement.
  - Renommer en "Fonctions" : terme trop lié aux Fonctions de direction/pilotage.
- **Choix retenu** : "Postes" — position formelle contextualisée, indépendante de son titulaire. **Règle associée** : un individu est rattaché à un seul poste (clarté et bruit réduit).
- **Conséquences** :
  - ✅ Charpente formelle du système plus lisible
  - ✅ Distinction claire avec Individu (personne physique) et Collectif (groupe)
  - ⚠️ Migration des entrées Rôles officiels existantes vers Postes
  - ⚠️ Si un individu avait plusieurs rôles, arbitrage humain nécessaire pour choisir le poste principal
- **Règles associées** : R-011 (frontières fortes)

### D-005 : Création de la BDD Initiatives organisationnelles

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Le Twin ne portait pas explicitement les **efforts temporaires structurés** (projets, programmes, pilotes, chantiers). Ces objets finissaient dilués dans Événements, Actions détectées ou Processus — chacun étant une distorsion.
- **Options envisagées** :
  - Utiliser Événements pour les projets : confond repère temporel et effort intentionnel.
  - Utiliser Actions détectées : confond geste ponctuel et effort structuré.
  - Créer une BDD dédiée : porte correctement la nature "mouvement/transformation".
- **Choix retenu** : BDD `Initiatives organisationnelles` = effort intentionnel, temporaire et délimité, avec portage, sponsoring, jalons, état d'avancement, statuts temporels.
- **Conséquences** :
  - ✅ Chaîne de transformation `OKR → Initiatives` explicite (cf. Panorama §10.12)
  - ✅ Lecture de la transformation vivante du système (qui porte quoi, avec quels jalons)
  - ✅ Nouvelle famille architecturale "Mouvement / transformation"
  - ⚠️ Risque de confusion avec Événements (repère temporel) et Pratiques (récurrent) — à gérer via R-011
- **Règles associées** : R-011

### D-006 : Création de la BDD edge Relations inter-organisations

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Avec la scission UO → Organisation + Collectif (D-002), les relations structurantes entre organisations (coopération, fourniture, dépendance, régulation, co-développement, fusion) nécessitaient un porteur dédié.
- **Options envisagées** :
  - Stocker les relations comme propriétés relations Notion sur Organisations : perd la richesse (nature, statut, ancienneté, réciprocité, événements associés).
  - Créer une BDD "edge" dédiée : le lien devient un objet first-class avec ses propres propriétés.
- **Choix retenu** : BDD `Relations inter-organisations` = lien structurant directionnel entre deux organisations, porte la nature, le statut, l'ancienneté, la réciprocité.
- **Conséquences** :
  - ✅ Cartographie de l'écosystème relationnel externe exploitable (traversée §12.3)
  - ✅ Profils 5D d'exposition/dépendance externe possibles
  - ⚠️ Seule BDD "edge" du Twin — singularité à documenter clairement
- **Règles associées** : R-011, R-013

### D-007 : Création de 6 sandboxes spécialisées

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Les consolidations précoces polluaient le graphe officiel. Il manquait des sas d'exploration pour tester hypothèses et formulations sans engager la couche officielle.
- **Options envisagées** :
  - Utiliser le statut `Brouillon` dans les BDD officielles : reste visible dans le graphe officiel, nuisible.
  - Une sandbox unique multi-objets : moins rigoureux, frontière confuse.
  - Une sandbox par BDD officielle cible : propre mais pour lesquelles BDD ?
- **Choix retenu** : 6 sandboxes spécialisées, chacune avec BDD officielle cible précise :
  - `Capacités métier candidates (sandbox)` → `Capacités organisationnelles`
  - `OKR (sandbox)` → `OKR`
  - `Pratiques organisationnelles (sandbox)` → `Pratiques organisationnelles`
  - `Principes organisationnels (sandbox)` → `Principes organisationnels`
  - `Problématiques (sandbox)` → `Problématiques`
  - `Processus candidats (sandbox)` → `Processus candidats`
- **Conséquences** :
  - ✅ Graphe officiel propre (hygiène)
  - ✅ Pré-consolidation réversible possible
  - ✅ Doctrine de promotion explicite (cf. R-022)
  - ⚠️ Règle absolue : pas de relations réelles sauf vers `Sources d'informations` (R-014)
  - ⚠️ Attention à ne pas laisser les sandboxes devenir des BDD parallèles durables
- **Règles associées** : R-014, R-021, R-022

### D-008 : Tableau maître canonique à 29 BDD

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : L'architecture du Twin avait évolué sans carte unique à jour. Il manquait un référentiel obligatoire auquel arbitrer toute création/modification/archivage de BDD.
- **Options envisagées** :
  - Tenir une carte informelle (wiki, doc hors refs) : non versionnée, dérive possible.
  - Faire du Panorama la carte canonique : trop doctrinal pour être consulté comme référence rapide.
  - Créer un SPECS_ARCHITECTURE_TWIN dédié, aligné sur SPECS_ARCHITECTURE_BRAIN : symétrie et scalabilité.
- **Choix retenu** : 29 BDD canoniques dans le Twin :
  - 1 satellite de traçabilité (`Sources d'informations`)
  - 1 socle sémantique (`Glossaire spécifique entreprise`)
  - 3 extraction factuelle (`Journal des signaux`, `Actions détectées`, `Enjeux`)
  - 8 socle structurel (`Organisations`, `Relations inter-organisations`, `Collectifs`, `Individus`, `Postes`, `Actifs`, `Environnements`, `Événements`)
  - 1 mouvement / transformation (`Initiatives organisationnelles`)
  - 1 pivot de qualification (`Processus candidats`)
  - 8 couche analytique officielle (`Processus`, `Pratiques organisationnelles`, `Principes organisationnels`, `Capacités organisationnelles`, `Problématiques`, `OKR`, `Indicateurs`, `Modulateurs`)
  - 6 sandboxes spécialisées
- **Conséquences** :
  - ✅ Référence unique pour la gouvernance
  - ✅ Création de `refs/SPECS_ARCHITECTURE_TWIN.md` qui reproduit le tableau
  - ⚠️ Discipline obligatoire : toute modification de l'archi doit être arbitrée à partir de la carte (R-025)
- **Règles associées** : R-025

### D-009 : Chaînes de transformation de la connaissance comme paradigme de lecture

- **Date** : 2026-04-22
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Le Twin était lu "table par table" ce qui masquait sa vraie valeur : la transformation progressive de la connaissance (preuve → qualification → consolidation → lecture → pilotage → action).
- **Options envisagées** :
  - Lecture par BDD isolées : simple mais occulte la chaîne de valeur.
  - Lecture par traversées : plus riche mais non guidée.
  - Lecture par chaînes de transformation : explicite le passage entre régimes de connaissance.
- **Choix retenu** : Adopter les **chaînes de transformation** comme paradigme de lecture principal. Exemples clés :
  - `Sources → objets documentés` (auditabilité)
  - `Journal des signaux → Enjeux → Problématiques → OKR → Indicateurs` (chaîne diagnostic → pilotage)
  - `Actions détectées → Processus candidats → Processus` (passage brut → structuré)
  - `Actions détectées → Pratiques organisationnelles` (geste → pattern)
  - `Pratiques → Capacités` (pattern → aptitude durable)
  - `Principes → Pratiques` (norme → incarnation, cœur de la lecture 3P)
  - `Modulateurs ↔ Pratiques ↔ Capacités` (conditions d'effectivité)
  - `sandbox → Sources d'informations → indices → BDD officielle cible` (promotion)
- **Conséquences** :
  - ✅ Twin pensé comme machine de lecture systémique, pas entrepôt
  - ✅ Séparation des 4 régimes de connaissance renforcée (R-012)
  - ✅ Chaînes exploratoires documentées (via sandboxes)
  - ⚠️ Les prompts maîtres et logic blocks doivent refléter ces chaînes
- **Règles associées** : R-012, R-021, R-022, R-024

---

## 2. Décisions de gouvernance

*Décisions sur comment on gère l'écosystème (workflows, responsabilités, fréquences).*

*(vide pour l'instant)*

---

## 3. Décisions de mise en œuvre

*Décisions techniques/pratiques (outillage, stockage, versioning).*

### D-001 : Trio Drive + Obsidian + Git comme stack documentaire

- **Date** : 2026-04-07
- **Statut** : Appliquée
- **Portée** : Transverse
- **Contexte** : Besoin de stockage cloud (partage équipe), d'édition locale ergonomique, et de versioning fiable.
- **Options envisagées** :
  - Tout sur Notion : simple mais pas de versioning fin, pas de portabilité.
  - Git + Markdown uniquement : portable mais pas de partage non-technique.
  - Drive + Obsidian + Git : combine les trois.
- **Choix retenu** : Drive synchronise, Obsidian édite en local, Git versionne.
- **Conséquences** :
  - ✅ Portabilité maximale, historique fin, graphe Obsidian navigable.
  - ⚠️ Risque de désync entre les trois (à gouverner).
- **Règles associées** : R-001, R-010

---

## Annexe : décisions révisées ou abandonnées

*(vide pour l'instant)*
