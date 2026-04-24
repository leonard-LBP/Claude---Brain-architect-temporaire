# Décisions architecturales

> Ce fichier trace les choix structurants qui ne sont pas des règles à appliquer, mais des décisions qui contextualisent l'écosystème.
> Chaque décision a un ID stable (D-XXX) et documente le *pourquoi* du choix, pas juste le *quoi*.
> Utile pour comprendre l'histoire de l'architecture et retracer les raisonnements.
> Dernière mise à jour : 2026-04-24 — ajout D-002 à D-009 (Panorama V2 v3) + D-010, D-011 (arborescence + conventions)

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

### D-010 : Arborescence cible d'Architecture data (v2)

- **Date** : 2026-04-24
- **Statut** : Adoptée (appliquée dans dossier temporaire ; migration vers vault à venir)
- **Portée** : Transverse (Brain + Twin)
- **Contexte** : La refonte Twin v2 produit ~200 nouveaux docs (22 manuels officiels + 6 sandboxes + ~74 notes de concept + ~96 taxonomies + 1 nouveau template). Il faut définir une arborescence cible évolutive avant migration vers le vault Architecture data, pour obtenir des URLs Drive stables avant indexation Notion.
- **Options envisagées** :
  - Indexer Notion d'abord puis ranger : double passe Notion (indexation sans URL, puis ajout URL).
  - Ranger d'abord puis indexer en une seule passe : URLs Drive disponibles dès l'indexation.
  - Structure détaillée par famille architecturale (sandboxes, BDD edge, analytique, etc.) : trop lourde pour 28 BDD.
  - Structure minimale (juste zone d'archives par dossier) : lisible, évolutive.
- **Choix retenu** :
  - Séquence en 4 étapes : (0) clarifier statut Notion, (1) définir arborescence, (2) appliquer arborescence + archiver anciens, (3) indexer Notion en une passe.
  - Arborescence :
    - `Manuels de BDD/Digital Twin/` : 22 manuels à plat + `Sandbox/` (6 sandboxes) + `archives/`
    - `Notes de Concept/` : notes à plat + `archives/`
    - `Taxonomies/` : taxonomies à plat + `archives/`
    - `Logic Blocks/` : sous-dossiers par BDD cible (dont nouveaux dossiers pour Actifs, Collectifs, Organisations, Postes, Initiatives, Relations inter-organisations) + `archives/` pour UO/Ressources/Rôles officiels
    - `Docs Méta LBP/` : templates à plat + `archives/`
  - Archivage **local par dossier thématique** (pas de grenier global).
- **Conséquences** :
  - ✅ URLs Drive disponibles dès la migration, indexation Notion en une passe
  - ✅ Sandboxes visuellement séparées des BDD officielles (renforce R-014)
  - ✅ Git garde l'historique complet des déplacements
  - ⚠️ Application en 2 temps : d'abord dossier temporaire `I:\AI\Claude Code\Nouveaux docs Brain\`, puis migration vers vault
- **Règles associées** : R-014 (sandboxes), R-025 (tableau maître), R-026 (archivage local), R-027 (nommage)

### D-012 : Séquence de migration Twin v2 vers Architecture data (7 phases)

- **Date** : 2026-04-24
- **Statut** : Adoptée
- **Portée** : Transverse (Brain + Twin + Mission Ops)
- **Contexte** : Après validation de l'arborescence cible (D-010) et des conventions de nommage (D-011), il fallait séquencer la migration de ~200 nouveaux docs + archivage de leurs v1 + refonte ciblée de l'arborescence existante. Objectif : avoir vault et Drive alignés AVANT l'indexation Notion (une seule passe avec URLs).
- **Options envisagées** :
  - Migration tout-en-un : risqué, pas de point de contrôle intermédiaire.
  - Par couche d'artefacts : OK mais mélange refonte arborescence et migration.
  - **Par phases avec refonte en amont** : plus rigoureux, chaque phase vérifiable.
- **Choix retenu** : Séquence en 7 phases, refonte arborescence d'abord :
  1. **Phase 1 — Refondre l'arborescence d'Architecture data** : renommer `Docs Méta LBP/` → `00 - Docs méta/` (avec sous-structure Templates + Doctrines), renommer `Core & Motor Brain/` → `Brain/`, créer `archives/` systématiques.
  2. **Phase 2 — Archiver les anciens docs v1** : tous les manuels Twin v1, toutes les notes de concept v1, toutes les taxonomies v1, ancien template. **Exception** : les logic blocks obsolètes ne sont PAS archivés maintenant (gardés comme inspiration pour la mise à jour future des nouveaux logic blocks Actifs, Collectifs, Organisations, Postes, Initiatives, Relations inter-organisations).
  3. **Phase 3 — Migrer les nouveaux docs** depuis dossier temporaire vers Architecture data (manuels Twin v2, notes de concept, taxonomies, nouveau template).
  4. **Phase 4 — Synchronisation Drive + vérification URLs**.
  5. **Phase 5 — Indexation Notion** : archiver les anciennes entrées Notion + indexer les nouveaux docs avec URLs Drive.
  6. **Phase 6 — Mise à jour des clefs de lecture** (R-028) : **templatiser d'abord** le doc "Instructions d'écriture & clefs de lecture" (améliorer le modèle), puis mettre à jour chaque doc dérivé.
  7. **Phase 7 — Chantier Prompts + Logic blocks** (séparé) : audit dossier Prompts actuel, mise à jour des prompts maîtres et logic blocks pour refléter Twin v2, rangement final.
- **Conséquences** :
  - ✅ Vault propre avant ingestion des nouveaux docs
  - ✅ Aucune indexation Notion sans URL Drive valide
  - ✅ Clair séparation entre "rangement" (phases 1-4), "gouvernance Notion" (phase 5), "dérivés docs" (phase 6), "mise à jour de contenu" (phase 7)
  - ✅ Logic blocks obsolètes conservés comme matière d'inspiration — ne pas les archiver trop tôt
- **Règles associées** : R-026 (archivage local), R-027 (nommage), R-028 (manuel=source de vérité)

### D-011 : Conventions de nommage des fichiers Brain/Twin

- **Date** : 2026-04-24
- **Statut** : Adoptée
- **Portée** : Transverse
- **Contexte** : Les anciens fichiers utilisaient différentes conventions (casse CAPITALES, tirets simples). Les nouveaux docs générés arrivaient avec tiret cadratin `—`. Il faut trancher pour éviter les disparités dans le vault.
- **Options envisagées** :
  - Tiret cadratin `—` (nouveaux) : élégant typographiquement, compliqué à taper.
  - Tiret simple `-` (anciens) : standard clavier, lisible.
  - Underscore `_` : plus technique, moins convivial pour Obsidian.
- **Choix retenu** :
  - **Séparateur** : tiret simple `-`
  - **Casse** : Title Case pour les manuels (`Manuel de BDD - Actifs.md`), minuscule pour les notes de concept (`concept - Actif.md`), code taxonomie pour les taxonomies (`ACT.IMPACT_DOMAIN.LBP.md`)
  - **Uniformisation rétroactive** : à faire au moment de la migration (renommer éventuellement les anciens fichiers CAPITALES `BDD - AGENTS LBP.md` → `Manuel de BDD - Agents LBP.md`, à décider au cas par cas)
- **Conséquences** :
  - ✅ Compatibilité clavier et interopérabilité avec tout outil
  - ✅ Homogénéité visuelle dans Obsidian
  - ⚠️ Les 28 nouveaux manuels Twin v2 ont été renommés (tiret cadratin → tiret simple) dans le dossier temporaire le 2026-04-24
- **Règles associées** : R-027

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
