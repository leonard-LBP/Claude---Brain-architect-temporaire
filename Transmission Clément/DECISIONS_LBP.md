---
# === Identité ===
title: "Décisions architecturales LBP"
doc_type: doc_meta
code: "CHRT_DECISIONS_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
template_version: "1.0"
created_at: "07-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Catalogue chronologique des 23 décisions architecturales (D-XXX) qui contextualisent l'écosystème LBP. Format standard par décision : Date / Statut / Portée / Contexte / Options envisagées / Choix retenu / Conséquences / Règles associées."
purpose: "Référence canonique pour comprendre POURQUOI tel choix architectural a été fait. Chaque D-XXX peut générer une ou plusieurs R-XXX (RULES_LBP) ou WF-XXX (WORKFLOWS_LBP)."
tags:
  - doc_meta
  - decisions
  - catalogue
  - architecture
  - brain
  - digital_twin
  - mission_ops
  - lbp
---

# Décisions architecturales LBP

> Ce fichier trace les choix structurants qui ne sont pas des règles à appliquer, mais des décisions qui contextualisent l'écosystème.
> Chaque décision a un ID stable (D-XXX) et documente le *pourquoi* du choix, pas juste le *quoi*.
> Utile pour comprendre l'histoire de l'architecture et retracer les raisonnements.
> Dernière mise à jour : 27-04-2026 - ajout D-018 (Bricks de connaissance comme Notes avancées des objets Twin, lien avec R-050)

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

- **Date** : 22-04-2026 (formalisée dans Panorama V2 v3)
- **Statut** : Adoptée (changements faits par Leonard, intégration dans le vault à venir)
- **Portée** : Twin
- **Contexte** : La BDD `Unités Organisationnelles` mélangeait deux natures d'objets ontologiquement distinctes - entités juridiques instituées et groupements humains opérants. Cette confusion produisait des analyses imprécises (ex: un "département" rangé au même niveau qu'une "SA").
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

- **Date** : 22-04-2026
- **Statut** : Adoptée
- **Portée** : Twin + Brain (propagation dans docs)
- **Contexte** : Le terme "Ressources" était ambigu - confondu avec "ressources humaines", "ressources financières", ou simple support. Il ne traduisait pas la nature gouvernable et administrable de l'objet.
- **Options envisagées** :
  - Garder "Ressources" + préciser dans la description : ne résout pas l'ambiguïté perçue.
  - Renommer en "Actifs" : terme plus précis, aligné sur une notion d'objet mobilisable/gouvernable.
  - Terme plus spécialisé (ex: "Moyens", "Supports") : moins générique, limitant.
- **Choix retenu** : "Actifs" - objet non humain gouvernable, mobilisable, administrable ou transformable.
- **Conséquences** :
  - ✅ Frontière clarifiée avec Environnements (cadre d'usage) et Sources (artefact de preuve)
  - ✅ Ouvre la voie à des propriétés spécifiques : type, criticité, substituabilité, cycle de vie
  - ⚠️ Mise à jour de tous les docs référençant "Ressources"
  - ⚠️ Mise à jour taxonomies, manuels, prompts maîtres, logic blocks
- **Règles associées** : R-011 (frontières fortes)

### D-004 : Renommage Rôles officiels → Postes

- **Date** : 22-04-2026
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Avec "Rôles officiels", un individu se retrouvait avec plusieurs rôles rattachés, générant du bruit et de la confusion entre fonction formelle et responsabilités multiples. Le terme "rôle" était aussi flou (officiel vs informel, formel vs opératoire).
- **Options envisagées** :
  - Garder "Rôles officiels" + règle "1 rôle principal par individu" : laisse la friction terminologique.
  - Renommer en "Postes" + règle 1 individu = 1 poste : plus net structurellement.
  - Renommer en "Fonctions" : terme trop lié aux Fonctions de direction/pilotage.
- **Choix retenu** : "Postes" - position formelle contextualisée, indépendante de son titulaire. **Règle associée** : un individu est rattaché à un seul poste (clarté et bruit réduit).
- **Conséquences** :
  - ✅ Charpente formelle du système plus lisible
  - ✅ Distinction claire avec Individu (personne physique) et Collectif (groupe)
  - ⚠️ Migration des entrées Rôles officiels existantes vers Postes
  - ⚠️ Si un individu avait plusieurs rôles, arbitrage humain nécessaire pour choisir le poste principal
- **Règles associées** : R-011 (frontières fortes)

### D-005 : Création de la BDD Initiatives organisationnelles

- **Date** : 22-04-2026
- **Statut** : Adoptée
- **Portée** : Twin
- **Contexte** : Le Twin ne portait pas explicitement les **efforts temporaires structurés** (projets, programmes, pilotes, chantiers). Ces objets finissaient dilués dans Événements, Actions détectées ou Processus - chacun étant une distorsion.
- **Options envisagées** :
  - Utiliser Événements pour les projets : confond repère temporel et effort intentionnel.
  - Utiliser Actions détectées : confond geste ponctuel et effort structuré.
  - Créer une BDD dédiée : porte correctement la nature "mouvement/transformation".
- **Choix retenu** : BDD `Initiatives organisationnelles` = effort intentionnel, temporaire et délimité, avec portage, sponsoring, jalons, état d'avancement, statuts temporels.
- **Conséquences** :
  - ✅ Chaîne de transformation `OKR → Initiatives` explicite (cf. Panorama §10.12)
  - ✅ Lecture de la transformation vivante du système (qui porte quoi, avec quels jalons)
  - ✅ Nouvelle famille architecturale "Mouvement / transformation"
  - ⚠️ Risque de confusion avec Événements (repère temporel) et Pratiques (récurrent) - à gérer via R-011
- **Règles associées** : R-011

### D-006 : Création de la BDD edge Relations inter-organisations

- **Date** : 22-04-2026
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
  - ⚠️ Seule BDD "edge" du Twin - singularité à documenter clairement
- **Règles associées** : R-011, R-013

### D-007 : Création de 6 sandboxes spécialisées

- **Date** : 22-04-2026
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

- **Date** : 22-04-2026
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
  - ✅ Création de `refs/SPECS_ARCHITECTURE_TWIN_LBP.md` qui reproduit le tableau
  - ⚠️ Discipline obligatoire : toute modification de l'archi doit être arbitrée à partir de la carte (R-025)
- **Règles associées** : R-025

### D-009 : Chaînes de transformation de la connaissance comme paradigme de lecture

- **Date** : 22-04-2026
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

- **Date** : 24-04-2026
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

- **Date** : 24-04-2026
- **Statut** : Adoptée
- **Portée** : Transverse (Brain + Twin + Mission Ops)
- **Contexte** : Après validation de l'arborescence cible (D-010) et des conventions de nommage (D-011), il fallait séquencer la migration de ~200 nouveaux docs + archivage de leurs v1 + refonte ciblée de l'arborescence existante. Objectif : avoir vault et Drive alignés AVANT l'indexation Notion (une seule passe avec URLs).
- **Options envisagées** :
  - Migration tout-en-un : risqué, pas de point de contrôle intermédiaire.
  - Par couche d'artefacts : OK mais mélange refonte arborescence et migration.
  - **Par phases avec refonte en amont** : plus rigoureux, chaque phase vérifiable.
- **Choix retenu** : Séquence en 7 phases, refonte arborescence d'abord :
  1. **Phase 1 - Refondre l'arborescence d'Architecture data** : renommer `Docs Méta LBP/` → `00 - Docs méta/` (avec sous-structure Templates + Doctrines), renommer `Core & Motor Brain/` → `Brain/`, créer `archives/` systématiques.
  2. **Phase 2 - Archiver les anciens docs v1** : tous les manuels Twin v1, toutes les notes de concept v1, toutes les taxonomies v1, ancien template. **Exception** : les logic blocks obsolètes ne sont PAS archivés maintenant (gardés comme inspiration pour la mise à jour future des nouveaux logic blocks Actifs, Collectifs, Organisations, Postes, Initiatives, Relations inter-organisations).
  3. **Phase 3 - Migrer les nouveaux docs** depuis dossier temporaire vers Architecture data (manuels Twin v2, notes de concept, taxonomies, nouveau template).
  4. **Phase 4 - Synchronisation Drive + vérification URLs**.
  5. **Phase 5 - Indexation Notion** : archiver les anciennes entrées Notion + indexer les nouveaux docs avec URLs Drive.
  6. **Phase 6 - Mise à jour des clefs de lecture** (R-028) : **templatiser d'abord** le doc "Instructions d'écriture & clefs de lecture" (améliorer le modèle), puis mettre à jour chaque doc dérivé.
  7. **Phase 7 - Chantier Prompts + Logic blocks** (séparé) : audit dossier Prompts actuel, mise à jour des prompts maîtres et logic blocks pour refléter Twin v2, rangement final.
- **Conséquences** :
  - ✅ Vault propre avant ingestion des nouveaux docs
  - ✅ Aucune indexation Notion sans URL Drive valide
  - ✅ Clair séparation entre "rangement" (phases 1-4), "gouvernance Notion" (phase 5), "dérivés docs" (phase 6), "mise à jour de contenu" (phase 7)
  - ✅ Logic blocks obsolètes conservés comme matière d'inspiration - ne pas les archiver trop tôt
- **Règles associées** : R-026 (archivage local), R-027 (nommage), R-028 (manuel=source de vérité)

### D-011 : Conventions de nommage des fichiers Brain/Twin

- **Date** : 24-04-2026
- **Statut** : Adoptée
- **Portée** : Transverse
- **Contexte** : Les anciens fichiers utilisaient différentes conventions (casse CAPITALES, tirets simples). Les nouveaux docs générés arrivaient avec tiret cadratin `-`. Il faut trancher pour éviter les disparités dans le vault.
- **Options envisagées** :
  - Tiret cadratin `-` (nouveaux) : élégant typographiquement, compliqué à taper.
  - Tiret simple `-` (anciens) : standard clavier, lisible.
  - Underscore `_` : plus technique, moins convivial pour Obsidian.
- **Choix retenu** :
  - **Séparateur** : tiret simple `-`
  - **Casse** : Title Case pour les manuels (`Manuel de BDD - Actifs.md`), minuscule pour les notes de concept (`concept - Actif.md`), code taxonomie pour les taxonomies (`ACT.IMPACT_DOMAIN.LBP.md`)
  - **Uniformisation rétroactive** : à faire au moment de la migration (renommer éventuellement les anciens fichiers CAPITALES `BDD - AGENTS LBP.md` → `Manuel de BDD - Agents LBP.md`, à décider au cas par cas)
- **Conséquences** :
  - ✅ Compatibilité clavier et interopérabilité avec tout outil
  - ✅ Homogénéité visuelle dans Obsidian
  - ⚠️ Les 28 nouveaux manuels Twin v2 ont été renommés (tiret cadratin → tiret simple) dans le dossier temporaire le 24-04-2026
- **Règles associées** : R-027

### D-013 : Traçabilité de version de template d'instanciation

- **Date** : 25-04-2026
- **Statut** : Adoptée
- **Portée** : Brain (Manuels de BDD ; étendable à Notes concept, Glossaire, Bricks ultérieurement)
- **Contexte** : Les templates d'instanciation LBP évoluent (template Manuel de BDD désormais en v6.1.0 = standard Twin v2). Les manuels générés via d'anciens templates restent valides mais structurellement différents (sections, frontmatter, vocabulaires). Sans traçabilité explicite, on ne peut pas distinguer les manuels conformes au standard courant des manuels legacy à migrer, ni piloter les migrations futures de templates.
- **Options envisagées** :
  - Pas de traçabilité : on suppose que tous les manuels suivent le standard courant. Casse dès qu'un template évolue.
  - Tag implicite via `tags` du frontmatter : non structuré, pas filtrable côté Notion.
  - **Champ dédié `template_version` (frontmatter vault + propriété Notion)** : explicite, filtrable, pérennise la traçabilité.
- **Choix retenu** :
  - **Côté template** : ajouter une instruction au bloc `FRONTMATTER_INSTANCE` du template pour que tout manuel instancié porte un champ `template_version` reflétant la valeur du champ `version` du template (actuellement "6.1.0").
  - **Côté vault** : ajouter `template_version: "6.1.0"` au frontmatter des manuels Twin v2 lors du batch B (rétro-fit).
  - **Côté Notion** : ajouter une propriété `Version du template` (Select, mono) à la BDD `Manuels de BDD` ; renseigner `v6.1.0` pour tous les manuels Twin lors du batch B ; laisser vide pour les manuels legacy.
  - **Convention** : champ vide = manuel legacy (template antérieur ou inconnu) ; à renseigner progressivement au fur et à mesure des migrations.
- **Conséquences** :
  - ✅ Distinction propre entre manuels v2 conformes et manuels legacy
  - ✅ Capacité à filtrer / piloter les migrations futures de templates
  - ✅ Pattern réutilisable pour les autres BDD à templates (Notes concept, Glossaire, Bricks)
  - ⚠️ Il faudra incrémenter `template_version` dans le manuel à chaque montée de version du template (à formaliser quand le 1er upgrade de template arrivera)
  - ⚠️ Les manuels Brain et Mission Ops anciennement indexés restent vides - la migration future demandera un audit
- **Règles associées** : à venir si on étend le pattern (potentielle R-039 sur "traçabilité de génération par template")

### D-014 : Colocalisation des docs WR-RD avec leurs manuels de BDD parents

- **Date** : 26-04-2026
- **Statut** : Adoptée (provisoire - naming "WR-RD" à reconfirmer après discussion sur leur rôle exact)
- **Portée** : Brain - organisation du vault Architecture data
- **Contexte** : Les docs « Instructions d'écriture + Clefs de lecture » (un par BDD du Brain/Twin/Mission Ops) étaient stockés dans un dossier global `Architecture data/Clefs de lectures/` à la racine du vault. Cette localisation détachait les docs WR-RD de leurs manuels parents, créait une asymétrie avec la nouvelle architecture par groupe (`Manuels de BDD/{Brain, Digital Twin, Mission Ops}/`), et rendait moins évidente la traçabilité « un manuel ↔ ses docs dérivés ». Suite à la refonte Twin v2, tous les docs WR-RD existants étaient désalignés avec les nouvelles specs et devaient être archivés.
- **Options envisagées** :
  - Conserver le dossier global `Clefs de lectures/` mais y créer une sous-structure par groupe : préserve le repère « zone WR-RD » mais perpétue la séparation manuel/WR-RD.
  - **Colocaliser** chaque WR-RD avec ses manuels parents dans un sous-dossier `WR-RD/` au sein de chaque dossier de groupe.
- **Choix retenu** :
  - Création d'un sous-dossier `WR-RD/` dans chaque groupe : `Manuels de BDD/Digital Twin/WR-RD/`, `Manuels de BDD/Brain/WR-RD/`, `Manuels de BDD/Mission Ops/WR-RD/`.
  - Chaque WR-RD a un `00 - archives/` pour ses propres anciennes versions (cohérent avec D-015).
  - Suppression du dossier `Clefs de lectures/` de la racine après migration.
  - Naming "WR-RD" provisoire : à rediscuter quand on précisera le rôle de ces docs (qui peut évoluer face aux nouveaux manuels Twin v2).
- **Migration effective (26-04-2026)** :
  - 39 docs Twin (anciens « Clefs de lecture » + plus récents « écriture + lecture ») archivés dans `Manuels de BDD/Digital Twin/WR-RD/00 - archives/` car désalignés avec les nouvelles specs Twin v2.
  - 2 docs Sources d'informations (Mission Ops) laissés ACTIFS dans `Manuels de BDD/Mission Ops/WR-RD/` car Mission Ops n'a pas encore été refondu.
  - `Manuels de BDD/Brain/WR-RD/` : créé vide pour la cohérence (les BDD Brain seront aussi manipulées par des agents et auront leurs WR-RD à terme).
  - Dossier racine `Architecture data/Clefs de lectures/` supprimé.
- **Conséquences** :
  - ✅ Proximité topologique entre un manuel et ses docs WR-RD (repérage facilité, navigation cohérente avec D-010).
  - ✅ Symétrie complète : chaque groupe BDD a son `WR-RD/` + son `00 - archives/`.
  - ✅ Aucun WR-RD obsolète n'est laissé en zone active.
  - ⚠ Naming "WR-RD" non finalisé - à reconsidérer après discussion sur le rôle réel de ces docs (extraction, lecture analytique, contrôle qualité, contrat de donnée…).
  - ⚠ Phase 6 = recréation des docs WR-RD pour les manuels Twin v2 actuels (à partir de zéro ou via dérivation depuis les manuels).

### D-015 : Convention de nommage `00 - archives/` pour les dossiers d'archives

- **Date** : 26-04-2026
- **Statut** : Adoptée
- **Portée** : Transverse - organisation visuelle de l'arborescence vault Architecture data
- **Contexte** : Le vault contient 12 dossiers `archives/` répartis dans toute l'arborescence (un par grand dossier de docs : Taxonomies, Méthodes, Notes de Concept, Manuels de BDD/{Brain,Digital Twin,Mission Ops}, etc.). En tri alphabétique standard, ces dossiers se mélangeaient avec les sous-dossiers actifs (parfois en milieu de liste), rendant moins immédiat le repérage de la zone "actuel vs historique" lors de la navigation.
- **Choix retenu** : préfixer tous les dossiers d'archives par `00 - ` → renommage `archives/` → `00 - archives/`. Le préfixe `00 - ` garantit que ces dossiers remontent en haut de chaque liste (tri alpha standard) sans confusion possible avec un dossier actif.
- **Migration effective (26-04-2026)** : 12 dossiers renommés en une passe :
  - `Taxonomies/00 - archives/`
  - `Méthodes/00 - archives/`
  - `Prompts/00 - archives/`
  - `Templates de Bricks/00 - archives/`
  - `Notes de Concept/00 - archives/`
  - `Logic Blocks/00 - archives/`
  - `00 - Docs méta/Templates d'instanciation/00 - archives/`
  - `00 - Docs méta/Doctrines & playbooks/00 - archives/`
  - `Manuels de BDD/00 - archives/`
  - `Manuels de BDD/Digital Twin/00 - archives/`
  - `Manuels de BDD/Mission Ops/00 - archives/`
  - `Manuels de BDD/Brain/00 - archives/`
  - + `Manuels de BDD/{Digital Twin, Brain, Mission Ops}/WR-RD/00 - archives/` (créés directement avec ce nommage)
- **Conséquences** :
  - ✅ Cohérent avec le pattern `00 - Docs méta/` déjà en racine du vault (préfixe `00 - ` = méta/transverse/historique remonté en haut).
  - ✅ Repérage visuel immédiat de la frontière "actuel vs historique".
  - ✅ Convention extensible : tout futur dossier d'archives doit suivre ce naming.
- **Règle implicite** : tout nouveau dossier d'archive vault → toujours `00 - archives/`, jamais `archives/`. À formaliser comme règle si besoin (R-XXX) au prochain ajout.

### D-016 : Rôle, contenu et format des docs WR-RD (Write Rules / Read Keys)

- **Date** : 26-04-2026
- **Statut** : Adoptée
- **Portée** : Brain (template d'instanciation) + Twin / Brain / Mission Ops (docs instanciés). Complète D-014 (colocalisation WR-RD avec leurs manuels parents).
- **Contexte** : Suite à la refonte Twin v2 (Phase 5), il fallait définir la place exacte des docs « Instructions d'écriture + Clefs de lecture » (renommés WR-RD) dans l'écosystème agentique LBP, où coexistent : system prompts (identité agent), prompts maîtres (par opération), logic blocks (par opération × BDD), manuels de BDD (référence design exhaustive), descriptions de propriétés Notion (mini-prompts inline). Le risque était soit de doublonner avec les logic blocks, soit de re-générer une doctrine déjà tenue par le manuel parent.
- **Constat préalable** : le template v6.1.0 du Manuel de BDD - Digital Twin prescrit déjà que les colonnes "Instructions d'écriture" (≤500 chars) et "Clefs de lecture" (≤400 chars) de la section 4 doivent être **autonomes** car elles seront "compilées vers les WR/RD". La doctrine du WR-RD était donc déjà en germe dans le manuel ; il restait à formaliser le format de sortie.
- **Options envisagées** :
  - **Option A - Statu quo discipliné** : maintenir un WR-RD éditorial avec sa propre doctrine et son contenu autonome.
  - **Option B - Fusion dans le manuel** : pas de WR-RD, l'agent charge le manuel complet à chaque opération.
  - **Option C - Fusion dans les logic blocks** : chaque logic block embarque les règles WR-RD nécessaires.
  - **Option D - WR-RD comme projection stricte du manuel parent** : extraction automatique d'un sous-ensemble de colonnes de la section 4 du manuel ; aucune doctrine ni contenu propre.
- **Choix retenu** : **Option D** - le WR-RD est une **projection stricte de la section 4 du manuel parent**, sans contenu propre.
  - **Rôle clarifié** : doc compact runtime pour les agents (twin architect en priorité, mais aussi tout agent opérant sur les BDD) qui doivent lire/écrire dans une BDD sans charger le manuel complet. Les Instructions d'écriture et Clefs de lecture étant autonomes par construction côté manuel, le WR-RD peut s'autosuffire ligne par ligne.
  - **Frontière nette avec les autres docs** :
    - System Prompt (agent) → identité, autorité, garde-fous globaux.
    - Prompt Maître (par opération) → mission, portée, garde-fous, hiérarchie d'autorité, format de sortie.
    - Logic Block (opération × BDD) → discernement, heuristiques d'opération, faux positifs, prudence, cas limites.
    - **WR-RD (par BDD) → tableau champ-par-champ : format d'écriture + sens de lecture (extraction stricte du manuel parent).**
    - Manuel de BDD (par BDD) → design conceptuel exhaustif, relations, gouvernance, narratif, invariants, traçabilité structurelle.
    - Description Notion ≤280 (par champ) → mini-prompt synthétique inline pour saisie rapide directement dans Notion.
  - **9 colonnes retenues du manuel parent** : Champ, Type, Taxonomie(s) - codes, Cardinalité / multiplicité, Forme logique attendue, Instructions d'écriture, Clefs de lecture, Utilité pour le Digital Twin, Exemples.
  - **3 colonnes du manuel NON reprises** : Portée (info de design), Nature de production (implicite dans Type), Prérequis Must/Should/Nice (stratégie de complétion, pas contrat strict).
  - **Révision 26-04-2026** : la colonne "Utilité pour le Digital Twin" a été réintégrée (initialement exclue v1.0.0 → réintroduite v1.2.0 du Template WR-RD). Argument : elle donne aux agents le sens opératoire de chaque champ (pourquoi ce champ existe, ce qu'il rend possible) sans bruit additionnel - un agent qui sait *pourquoi* écrit/lit mieux qu'un agent qui ne sait que *quoi*.
  - **5 sections cibles** miroir des sous-sections 4.1 à 4.5 du manuel : Génériques / Spécifiques / Relations + jumelles + rollups / 5D / Calculée. Sections 4 et 5 supprimées dans le doc instancié si la BDD n'a ni couche 5D ni couche calculée.
  - **Naming** : fichier `WR-RD - [Nom de la BDD].md` (miroir de `Manuel de BDD - [Nom de la BDD].md`) ; code unique `WRRD_[NOM_TOKEN]` (cohérent avec `DBMAN_[NOM_TOKEN]`).
  - **Frontmatter minimal** : `target_bdd_canonical_name`, `target_bdd_code`, `parent_manual`, `wr_rd_code`, `domain`, `version`, `template_version`, `created_at`, `tags`. Pas de `status` (géré hors document).
  - **Pas de section maintenance, ni doctrine, ni historique de version, ni articulation avec autres docs dans le doc instancié** : tout cela vit dans le manuel parent et relève du brain architect, pas du twin architect runtime.
- **Conséquences** :
  - ✅ Aucun risque de doublon avec logic blocks (qui parlent de discernement) ni avec le manuel (qui parle de design).
  - ✅ Source de vérité unique : la section 4 du manuel parent. Le WR-RD est une projection re-générable.
  - ✅ Doc compact, chargeable runtime par les agents, sans bruit pour le twin architect.
  - ✅ Extension future possible : générateur automatique manuel → WR-RD (script qui extrait les 8 colonnes des sous-sections 4.1 à 4.5 et émet le doc).
  - ⚠ Toute évolution du WR-RD doit passer par une évolution du manuel parent puis re-projection (pas de retouche directe du WR-RD).
  - ⚠ Naming "WR-RD" gardé (Write Rules / Read Keys) ; pourrait être reconsidéré si un meilleur nom émerge à l'usage.
- **Template créé** : `Template - WR-RD - Digital Twin.md` (v1.0.0) dans `00 - Docs méta/Templates d'instanciation/`. Reproduit le pattern du Template Manuel de BDD (cleanup_rules, blocs @INSTR, settings, FRONTMATTER_INSTANCE, COLUMN_DEFINITIONS, INSTANTIATION_GUIDE).
- **Implications à exécuter** :
  - 🔜 Notion : sur la BDD "Manuels de BDD", renommer la propriété URL existante "Lien vers le doc du manuel" → "Lien vers le manuel de BDD (.md)" ; ajouter une nouvelle propriété URL "Lien vers le doc WR-RD (.md)".
  - 🔜 Manuel parent "BDD - MANUELS DE BDD.md" : ajouter ces 2 propriétés dans la section 3.2 (champs) et la section 7 (propriétés spécifiques) avec instructions d'écriture / clefs de lecture autonomes.
  - 🔜 Phase 6 : générer 22 WR-RD à partir des 22 manuels Twin v2 actifs + 6 sandboxes (extraction automatique souhaitable).

---

### D-017 : Familles UI/UX comme prisme transverse de classification des BDD Twin

- **Date** : 27-04-2026
- **Statut** : Adoptée
- **Portée** : Twin (et propagation app LBP)
- **Contexte** : Les BDD du Twin disposent déjà de plusieurs prismes de classification techniques (`architecture_family` : socle_structurel, extraction_factuelle, analytique, sandbox, etc. ; `knowledge_regime` ; `officiality_regime`). Ces prismes sont utiles pour la gouvernance interne mais **opaques pour l'utilisateur final** de l'app LBP. Le besoin : disposer d'un prisme **orienté utilisateur** qui donne un sens narratif à l'organisation des BDD ("Qui existe", "Quels mots", "Quels cadres", "Ce qui met en mouvement", "Ce qui ancre durablement", "Comment on pilote", "Et des objets candidats pour court-circuiter la déduction quand la source les exprime déjà").
- **Options envisagées** :
  1. Réutiliser un prisme existant comme `architecture_family` côté UI → rejeté : trop technique, vocabulaire interne LBP.
  2. Créer un prisme dédié `ui_family` orthogonal aux autres → **retenu**.
  3. Mapping ad hoc dans le code app sans formalisation Brain → rejeté : risque de divergence app ↔ Brain, perte de cohérence sémantique.
- **Choix retenu** : Adopter une classification dédiée `ui_family` en **7 valeurs** :
  - **Langage** - *Les mots, termes métier, acronymes et définitions propres à l'organisation* (1 BDD : Glossaire spécifique)
  - **Structure** - *Qui existe, qui porte quoi, comment la structure humaine et institutionnelle est organisée* (5 BDD : Organisations, Relations inter-organisations, Collectifs, Individus, Postes)
  - **Cadres** - *Les cadres, supports, objets et situations qui conditionnent l'action* (3 BDD : Environnements, Actifs, Événements)
  - **Moteur** - *Ce qui met l'organisation en mouvement, produit, transforme et stabilise le fonctionnement réel* (5 BDD : Actions détectées, Processus candidats, Processus, Pratiques organisationnelles, Initiatives organisationnelles)
  - **Pilotage** - *Les sujets à traiter, les objectifs, les mesures et la trajectoire de pilotage* (5 BDD : Enjeux, Problématiques, OKR, Indicateurs, Journal des signaux)
  - **Ancrages** - *Ce qui oriente, soutient, amplifie ou freine durablement l'action organisationnelle* (3 BDD : Principes organisationnels, Capacités organisationnelles, Modulateurs)
  - **Objets candidats** - *Les objets organisationnels saisis directement quand la source les exprime explicitement, en complément des BDD-sas qui les déduisent par croisement (Enjeux → Problématiques+OKR ; Actions détectées → Pratiques+Initiatives+Processus candidats). Court-circuit opportuniste de la déduction.* (6 BDD sandbox)
- **Note typographique** : `Objets candidats` est intentionnellement en **2 mots** alors que les 6 autres familles sont en 1 mot. Cette dissonance typographique est **assumée** : elle signale visuellement que cette famille n'est pas un prisme de l'entreprise comme les autres, mais un statut d'objet (en cours de qualification). Le terme `Candidats` seul a été écarté car ambigu dans un contexte entreprise (pourrait évoquer des candidatures RH).

---

### D-018 : Bricks de connaissance comme Notes avancées des objets Twin

- **Date** : 27-04-2026
- **Statut** : Adoptée
- **Portée** : Twin + écosystème Bricks
- **Contexte** : Les fiches structurées du Twin (propriétés natives + relations + 5D) donnent une vue **quasi-tabulaire** d'un objet. Mais certains objets méritent une **profondeur narrative** : profil organisationnel d'une Organisation, profil détaillé d'un Individu, carte causale d'une Problématique, dossier complet d'un Actif critique, etc. Cette profondeur ne peut pas être portée par les propriétés structurées sans casser la lisibilité de la fiche. Or l'écosystème LBP dispose déjà d'un mécanisme adapté : les **Bricks** (livrables instanciés depuis des Templates de Bricks).
- **Options envisagées** :
  1. Ajouter des champs texte longs supplémentaires dans la fiche pour porter la profondeur → rejeté : alourdit la fiche, pas de format imposé, pas de réutilisabilité.
  2. Créer un nouvel objet "Note avancée" comme BDD séparée → rejeté : doublon avec les Bricks existants.
  3. **Réutiliser les Bricks** comme support des Notes avancées et lier la fiche Twin via une URL → **retenu**.
- **Choix retenu** : Une **Note avancée** d'un objet Twin = un **Brick de connaissance** instancié depuis un Template de Brick approprié (ex. `Template Brick - Profil organisationnel`, `Template Brick - Profil - Collectifs & Individus`). La fiche Twin de l'objet contient une propriété URL `Lien vers la note avancée` (R-050) qui pointe vers ce Brick. Les agents qui accompagnent le consultant peuvent consulter ces Bricks à la demande (focus contextuel).
- **Conséquences** :
  - ✅ Cohérence avec l'écosystème Bricks existant (pas de nouvel objet à inventer).
  - ✅ Profondeur narrative découplée de la fiche structurée (lisibilité préservée).
  - ✅ Réutilisation des Templates de Bricks pour homogénéiser les Notes avancées.
  - ⚠ Restriction : les Notes avancées ne sont produites **que pour des objets stabilisés** (cf. R-050 - exclusion sandbox, candidats, signaux, actions, indicateurs). On ne sur-documente pas un objet en cours de qualification.
  - 🔜 Identifier ou créer les Templates de Bricks "profil avancé" pour chaque type d'objet (Organisation, Collectif, Individu, Poste, Actif, Environnement, Événement, etc.).
- **Règles associées** : R-050 (déclaration de la propriété `Lien vers la note avancée`), R-047 v2.1 (position dans l'ordering).
- **Conséquences** :
  - ✅ Cohérence app ↔ Brain : la classification utilisée par l'app LBP est documentée dans le Brain, source de vérité.
  - ✅ Prisme **complémentaire** (non substitutif) aux autres : `architecture_family`, `knowledge_regime`, `officiality_regime` restent inchangés et servent la gouvernance technique.
  - ⚠ Charge de propagation : chaque manuel Twin doit recevoir un champ frontmatter `ui_family` (28 manuels à enrichir).
  - ⚠ Charge Notion : la BDD `Manuels de BDD` doit recevoir une propriété `Famille UI` (select) avec les 7 valeurs.
  - 🔜 La page Notion `BDD test - 26/04/2026 - Digital Twin update` utilise déjà cette classification (titres de groupes appliqués par Leonard 27-04-2026) - sert de référence visuelle.
- **Règles associées** : R-049 (déclaration obligatoire `ui_family` dans tout artefact Twin).

---

### D-019 : Brain = environnement documentaire en évolution (Core+Motor) ; isolation Brain ↔ Mission Ops/Twin

- **Date** : 28-04-2026
- **Statut** : Adoptée
- **Portée** : Brain (transverse à toutes ses BDDs) + frontière avec Mission Ops et Digital Twin
- **Contexte** : L'écosystème LBP distingue 4 grands environnements : `Core` (concepts, glossaire, taxonomies), `Motor` (méthodes, prompts, agents, templates, outils, logic blocks), `Digital Twin` (modélisation des organisations clients), `Mission Ops` (pilotage des missions et bricks produites). Les frontières Mission Ops ↔ Digital Twin sont nettes. En revanche, **côté Core et Motor, les contenus se mélangent en pratique** : la BDD Prompts LBP référence aussi bien des prompts qui manipulent le Twin d'un client que des prompts qui opèrent sur le Brain ; la BDD Manuels de BDD contient les manuels de toutes les BDDs (Brain + Twin + Mission Ops) ; la BDD Registre des taxonomies référence des taxos qui servent à toutes les BDDs. Tenter de cloisonner Core et Motor dans le modèle de données crée des sous-typages artificiels (cf. déséquilibre observé sur `Type fonctionnel` de la BDD Manuels de BDD : Digital Twin sur-subdivisé, Core/Motor/Mission Ops sans sous-familles).
- **Options envisagées** :
  1. Maintenir la distinction Core/Motor au niveau modèle de données (props `Type fonctionnel` ou équivalent par BDD) → rejeté : génère des sous-typages déséquilibrés et impose des arbitrages artificiels (un prompt qui génère une brick mission est-il Motor ou Mission Ops ?).
  2. Fusionner Core et Motor dans un "Brain" unifié au niveau modèle de données, en conservant la nuance Core/Motor au niveau **discours/documentation** uniquement → **retenu**.
  3. Mapping Core/Motor en taxo séparée à appliquer manuellement → rejeté : redondant avec `DBMAN.SCOPE` qui couvre déjà ce besoin pour les manuels.
- **Choix retenu** :
  1. **Brain = environnement documentaire en évolution** (les 11 BDDs Brain). Au niveau modèle de données, Core et Motor ne sont pas distingués : ce sont des **étiquettes de discours** utiles pour parler de l'écosystème, pas des prismes de classification structurels.
  2. **La nuance Core/Motor reste pertinente dans les `Domaine(s) d'usage`** des objets Motor Brain (Méthodes, Templates, Agents, Outils, Prompts) : un objet peut viser `Core`, `Motor`, `Digital Twin` ou `Mission Ops` selon ce qu'il sert. La taxo `DOMAIN.USAGE` (ou équivalent multi-select) reste à 4 valeurs.
  3. **Isolation stricte Brain ↔ Mission Ops/Twin** : aucune relation Notion entre une BDD Brain et une BDD Mission Ops ou Digital Twin. Justification : les BDDs Mission Ops et Digital Twin sont **instanciées à chaque mission** (espaces clients distincts), tandis que les BDDs Brain sont **uniques et persistantes** (l'écosystème documentaire LBP). Lier une BDD Brain à une instance MO/Twin créerait une dépendance impossible à matérialiser proprement.
- **Conséquences** :
  - ✅ Suppression de la propriété `Type fonctionnel` côté BDD Manuels de BDD (Notion + manuel).
  - ✅ La BDD Manuels de BDD ne porte plus de sous-typage par environnement (Core/Motor/Twin/MO) - le scope est déjà capturé par `DBMAN.SCOPE` (taxo créée Phase 1f).
  - ✅ Cohérence sur `Domaine(s) d'usage` : conservé sur les 5 BDDs Motor Brain (Méthodes, Templates, Agents, Outils, Prompts).
  - ⚠ Lorsqu'on parle "du Brain" en doctrine ou en règles, on parle de **l'environnement documentaire** (les 11 BDDs Brain + leurs docs) - pas des BDDs instanciées en mission.
  - ⚠ Les bricks produites en mission (BDD Bricks Mission Ops) ne sont **pas** des objets Brain malgré leur valeur cognitive - elles vivent dans l'instance Mission Ops.
- **Règles associées** : R-058 (interdiction jumelles texte sur Brain - corollaire de l'isolation et de la rigueur structurelle attendue côté Brain).

---

### D-020 : Propagation de la propriété `Version du template` à toutes les BDDs Brain

- **Date** : 28-04-2026
- **Statut** : Adoptée
- **Portée** : 11 BDDs Brain (transverse)
- **Contexte** : Aujourd'hui seule la BDD `Manuels de BDD` porte une propriété `Version du template` qui trace la version du template d'instanciation utilisé pour produire le manuel décrit (introduite avec D-018 / R-049 lors de la migration Twin v2). Or chaque BDD Brain indexe des docs qui sont eux aussi générés depuis un template (notes de concept ← `Template - Note de concept` ; taxos ← `Template - Taxonomie` ; méthodes ← `Template - Méthode LBP` ; templates de bricks ← `Template - Template de Brick` ; etc.). À chaque bump majeur d'un template, les docs générés depuis les versions précédentes deviennent stale et doivent être migrés (R-056). Sans propriété qui trace la lignée de génération, l'audit mécanique des docs stale est impossible.
- **Options envisagées** :
  1. Maintenir la propriété uniquement sur Manuels de BDD → rejeté : laisse les autres BDDs Brain sans audit possible de lignée.
  2. Étendre à toutes les 11 BDDs Brain → **retenu**.
  3. Stocker uniquement dans le frontmatter Markdown sans Notion → rejeté : Notion est l'interface principale de gouvernance, les vues filtrées par version doivent être possibles directement.
- **Choix retenu** : ajouter la propriété `Version du template` sur les **10 BDDs Brain** qui ne la portent pas encore (Docs méta LBP, Glossaire LBP, Registre des notes de concept, Registre des taxonomies, Méthodes LBP, Prompts LBP, Templates de bricks, Agents LBP, Outils externes, Registre des logic blocks). La BDD `Manuels de BDD` la porte déjà.
  - **Type** : `RICH_TEXT` (texte libre), pas `select`. Justification (Leonard 28-04-2026) : un select obligerait l'agent Brain architect à créer en permanence de nouvelles options à chaque bump de template, créant une accumulation illisible. Un texte libre suit la convention R-056 (`X.Y`) et peut être audité par regex sans pollution du schéma.
  - **Forme attendue** : `X.Y` (R-056), reflétant la valeur du frontmatter `template_version` du doc Markdown source.
  - **Mode de remplissage** : `consultant` ou `agent IA` lors de l'instanciation/mise à jour du doc. À défaut de connaissance, laisser vide (mieux que d'inventer).
- **Conséquences** :
  - ✅ Audit mécanique possible des docs stale lors de bumps majeurs de templates (filtrer Notion par `Version du template ≠ <version courante>`).
  - ✅ Cohérence transverse Brain - toutes les BDDs portent la même méta-info.
  - ✅ Convention R-056 (versioning X.Y) directement consommable côté Notion.
  - ⚠ Charge de propagation : 10 manuels Brain à enrichir + 11 WR-RD à propager (R-041/R-042).
  - ⚠ Charge de saisie : les ~310 entrées existantes des BDDs Brain devront être progressivement enrichies de leur version. Pour les nouveaux docs : la valeur est posée à la création.
  - ⚠ La BDD `Manuels de BDD` qui portait la propriété en `select` doit être convertie en `RICH_TEXT` pour cohérence transverse.
- **Règles associées** : R-055 (frontmatter canon), R-056 (versioning X.Y), R-049 (déclaration `template_version` dans le frontmatter).

---

### D-021 : Architecture des 3 agents LBP - Brain architect / Twin architect / KONTEXT

- **Date** : 28-04-2026
- **Statut** : Adoptée
- **Portée** : Transverse écosystème LBP (Brain + Twin + Mission Ops)
- **Contexte** : LBP a besoin d'une architecture d'agents claire pour distinguer (a) qui fait évoluer le Brain (méta-LBP, hors mission), (b) qui modélise/met à jour le Twin d'un client (peuplement, refactor), (c) qui pilote l'exécution d'une mission côté consultant utilisateur. Sans frontières d'isolation explicites, risque que des opérations de mission contaminent le Brain (modifications accidentelles pendant une prestation), ou que le Brain soit sur-utilisé comme outil de mission au lieu d'être consulté en lecture.
- **Options envisagées** :
  1. Un seul agent généraliste qui fait tout → rejeté : pas de séparation des responsabilités, risque de modifs Brain pendant une mission.
  2. Deux agents (Brain architect + agent mission unique) → rejeté : confond modélisation Twin et pilotage mission.
  3. **Trois agents avec frontières d'isolation explicites** → **retenu**.
- **Choix retenu** :
  1. **Brain architect** : opérations d'évolution sur le Brain (création/modif/refonte de manuels, taxos, méthodes, prompts, templates, agents, outils, logic blocks, docs méta). C'est l'agent méta-LBP - il fait évoluer l'écosystème documentaire.
  2. **Twin architect** : opérations sur le Twin d'un client (peuplement, refactor, dédoublonnage, complétion, mise à jour des objets Twin, génération de relations, qualification d'objets candidats).
  3. **KONTEXT** (nom provisoire) : agent central côté consultant utilisateur. Gère les Mission Ops : instanciation d'actions de mission, fixation de RDV, génération de livrables/bricks, mise à jour du Twin via délégation à Twin architect.
- **Frontière d'isolation infranchissable** : KONTEXT **ne peut pas** appeler Brain architect. Justification doctrinale : pendant une prestation, le Brain est **utilisé** (lecture des prompts, méthodes, outils, templates) mais **n'évolue pas**. L'évolution du Brain est une activité méta-LBP (gouvernance documentaire), pas une activité de mission. Cette frontière garantit la stabilité du Brain pendant les missions et évite les modifs accidentelles.
- **Délégations autorisées** :
  - KONTEXT → Twin architect : ✅ (mise à jour du Twin client = activité de mission légitime)
  - KONTEXT → Brain architect : ❌ (interdit)
  - Twin architect → Brain architect : à arbitrer ultérieurement (probable interdit pour la même raison ; à confirmer si le besoin émerge)
- **Conséquences** :
  - ✅ Stabilité du Brain pendant les missions.
  - ✅ Séparation claire des responsabilités (Brain = méta, Twin = client, Mission = exécution).
  - ✅ 3 agents = 3 fiches dans la BDD `Agents LBP` (à créer après Phase 7 bis / chantier P de tri Prompts+Logic blocks+Agents).
  - ⚠ Le nom `KONTEXT` est provisoire - à arbitrer avant publication finale.
  - ⚠ Cette doctrine bloque toute évolution du Brain en cours de mission. Si un agent identifie un besoin d'évolution Brain, il doit le **flagguer** comme remontée à traiter par Brain architect hors mission, pas le faire lui-même.
- **Règles associées** : à venir (R-XXX sur les frontières d'isolation des agents, à formaliser quand les 3 fiches Agents seront créées).

---

### D-022 : Différenciation assumée des frontmatters Twin et Mission Ops

- **Date** : 30-04-2026
- **Statut** : Active
- **Portée** : Architecture documentaire - Manuels de BDD Twin et Mission Ops
- **Contexte** : Backlog 27-04-2026 a remonté une **divergence des frontmatters** entre les manuels Twin (template v6.3.0) et Mission Ops (template v5.1.0). Le Twin embarque `ui_family`, `officiality_regime`, `has_advanced_note`, `aliases` ; Mission Ops ne les embarque pas. Pas d'arbitrage formel jusqu'ici → asymétrie silencieuse entre templates, source potentielle de confusion pour les futurs nouveaux docs MO.
- **Options envisagées** :
  1. **Harmoniser** : ajouter les 4 champs aussi côté MO pour permettre un audit transverse unifié.
  2. **Différencier explicitement** : assumer que Twin et MO ont des régimes de connaissance différents et que ces champs n'ont pas de sens en MO (statut **retenu**).
  3. **Laisser flou** : le statu quo, sans formalisation (rejeté - viole la doctrine de clarté C-008).
- **Choix retenu** : **Différenciation assumée**. Twin et MO sont deux domaines aux régimes de connaissance distincts :
  - Twin = **ontologique** (taxonomies, dimensions 5D, relations sémantiques, régime des objets organisationnels). Les champs Twin spécifiques (`ui_family`, `officiality_regime`, `has_advanced_note`, `aliases`) reflètent cette nature : prisme UX (D-017), distinction officiel/sandbox (R-014), bricks comme notes avancées (D-018), aliases pour le dédoublonnage de concepts.
  - Mission Ops = **opérationnel** (workflows de mission, livrables, traçabilité). Les champs Twin n'ont pas de pertinence en MO : pas de famille UI à classer, pas de régime officiel/sandbox (toutes les fiches MO sont opérationnelles par construction), pas de notes avancées (les bricks **sont** elles-mêmes des fiches MO), pas d'aliases (les noms d'occurrences MO sont uniques par construction - `MTG-XX-DATE`, `ACT-XX-NNN`).
  → Conséquence : le frontmatter MO est plus mince, par design, et c'est correct.
- **Conséquences** :
  - ✅ Pas de champ vide systématique côté MO (ce qui aurait été inélégant et faux-positif pour les audits de complétude).
  - ✅ Audit transverse à scope-aware : R-XXX et WF-XXX qui parlent du frontmatter doivent désormais préciser le scope (Brain / Twin / MO).
  - ⚠ Documentation requise dans `DOCTRINE_LBP.md` (à créer) pour expliciter la divergence de régime aux nouveaux contributeurs et à Clément.
  - ⚠ Si un nouveau champ doit être commun (ex. `code`, `version`, `created_at`, `updated_at`, `template_code`, `template_version`), il doit être présent **dans les deux** frontmatters et formalisé en R-XXX transverse.
- **Règles associées** : R-054 (codification), R-055 (frontmatter en 3 zones balisées Brain), R-056 (versioning X.Y), C-008 (séparation des scopes en `refs/`).

---

### D-023 : Mission Ops co-égal Brain/Twin + stack technique Notion (Brain) / Supabase (Twin + Mission Ops)

- **Date** : 30-04-2026
- **Statut** : Active
- **Portée** : Architecture transverse - gouvernance des 3 domaines + stack technique de production
- **Contexte** : Audit 30-04-2026 a révélé l'absence de décision fondatrice formalisant **Mission Ops comme domaine co-égal** au Brain et au Twin. Toutes les D-002→D-021 couvrent essentiellement le Twin (scission UO, sandboxes, chaînes D-009, bricks comme notes avancées) et le Brain (Core+Motor unifié D-019, agents D-021). Mission Ops a été instancié (4 BDDs, test Phase B 30-04-2026) sans formalisation doctrinale. Par ailleurs, la **stack technique de production** n'a jamais été formalisée : la maquette actuelle est sur Notion pour Brain et Twin/MO, mais le déploiement cible est différencié (Notion pour Brain, Supabase pour Twin + MO).
- **Options envisagées** :
  1. **MO sous-domaine du Twin** : intégrer les 4 BDDs MO comme extension du Twin (rejeté - viole la séparation des régimes de connaissance et l'isolation Brain ↔ MO/Twin de D-019).
  2. **MO co-égal Brain/Twin avec stack unifié Notion** : maquettage et production sur Notion (rejeté - Notion ne supporte pas les volumes de Mission Ops à grande échelle, ni les instanciations multi-mission par client, ni les performances de lecture/écriture nécessaires en production).
  3. **MO co-égal Brain/Twin avec stack différencié** : Notion pour Brain (gouvernance, lent, manuel), Supabase pour Twin + MO (volumes, performance, instanciation client) (statut **retenu**).
- **Choix retenu** :
  1. **Mission Ops est un domaine co-égal au Brain et au Twin**, gouverné par 4 BDDs structurelles : `Sources d'informations`, `Meetings`, `Actions LBP`, `Bricks`. Chaque mission consultant instancie son propre périmètre Twin + MO ; le Brain est partagé et stable (D-019).
  2. **Articulation entre les 3 domaines** :
     - Brain ↔ Twin : isolation stricte (D-019). Le Brain fournit les manuels, taxonomies, méthodes, templates, prompts, agents, outils. Il **n'évolue pas** pendant les missions (D-021).
     - Brain ↔ MO : isolation stricte (D-019). Le Brain fournit les templates de bricks (TPL_BRICK_*) que MO instancie en bricks de mission.
     - Twin ↔ MO : articulation via les **Bricks** (D-018) - les bricks MO documentent et alimentent les fiches Twin. Les `Sources d'informations` MO sont l'origine traçable des fiches Twin (régime « extraction directe » C-018).
  3. **Stack technique cible** :
     - **Brain = Notion** : volumétrie modérée (~200 docs Markdown actifs), gouvernance manuelle, navigation hypertexte, audit visuel. Notion suffit et apporte la richesse UX nécessaire à la gouvernance documentaire (relations, rollups, vues, filtres). Pas de migration prévue à court terme.
     - **Twin + Mission Ops = Supabase** : volumétrie potentiellement importante (instanciation par client, fiches Twin pouvant atteindre des milliers par mission, bricks et meetings nombreux), performance lecture/écriture critique, schéma stable car validé via la maquette Notion test (Phase B 30-04). La maquette Notion actuelle de Twin+MO sera **portée** vers Supabase une fois le schéma figé.
  4. **Pas de pont direct Brain ↔ Twin/MO** au niveau technique. Les seuls « ponts » conceptuels sont :
     - **Bricks instanciées à partir des Templates de Bricks Brain** (référence par code template, pas relation technique cross-stack)
     - **Templates de Bricks** lus depuis le Brain au moment de l'instanciation MO (lecture seule, snapshot conceptuel)
- **Conséquences** :
  - ✅ Mission Ops devient un domaine de premier niveau, avec sa propre doctrine, ses règles propres (à formaliser progressivement), et ses workflows propres (futurs WF-MO-XXX).
  - ✅ Stack technique cible cohérente avec la nature de chaque domaine : Notion pour la gouvernance, Supabase pour la production.
  - ✅ Le bundle de docs méta durables doit traiter les 3 domaines de façon symétrique : `SPECS_ARCHITECTURE_BRAIN_LBP.md` + `SPECS_ARCHITECTURE_TWIN_LBP.md` + `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md` (à créer).
  - ✅ Justifie la divergence assumée des frontmatters Twin/MO (D-022) - c'est un signe sain de différenciation des régimes.
  - ⚠ La maquette Notion Twin+MO devient une **fixture de validation de schéma**, pas une prod. À documenter clairement dans `MIGRATION_REPORT_2026-04` pour Clément.
  - ⚠ Le portage Twin+MO vers Supabase est un chantier ultérieur (post-Phase C) qui devra être cadré séparément (workflow dédié, gestion des migrations de données, gouvernance des schémas Supabase).
  - ⚠ Le Brain reste sur Notion à court/moyen terme. Toute future migration éventuelle (12-18 mois) sera elle aussi un chantier dédié.
  - ⚠ Pas de pont direct Brain↔Twin/MO : les agents (D-021) doivent intégrer cette frontière dans leur conception. KONTEXT lit le Brain (références conceptuelles : prompts, méthodes, templates) mais n'écrit pas dedans.
- **Règles associées** :
  - **R-014** : sandboxes Twin (relations dures uniquement avec Sources)
  - **D-009** : chaînes de transformation de la connaissance (chaînes Source → AD → Process → ... structurent l'articulation MO ↔ Twin)
  - **D-018** : bricks de connaissance comme notes avancées (articulation MO ↔ Twin)
  - **D-019** : Brain isolé de Twin/MO
  - **D-021** : 3 agents LBP avec frontières d'isolation
  - **C-018** : régime des BDDs (extraction directe vs consolidé)
  - À formaliser : R-XXX sur la stack technique de production (un par domaine si nécessaire).

---

## 3. Décisions de mise en œuvre

*Décisions techniques/pratiques (outillage, stockage, versioning).*

### D-001 : Trio Drive + Obsidian + Git comme stack documentaire

- **Date** : 07-04-2026
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
