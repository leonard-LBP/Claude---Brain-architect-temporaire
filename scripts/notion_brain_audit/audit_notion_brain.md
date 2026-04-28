# Audit transverse Notion ↔ Manuels BDD Brain
> Date : 28-04-2026
> Périmètre : 11 BDDs Brain officielles vs leurs manuels Markdown sources de vérité.
> Méthode : pour chaque BDD, fetch du data source Notion (schéma de propriétés) + lecture de la section 4 / 3.2 du manuel, puis comparaison nom / type / options.

## Légende des écarts
- **Manuel-only** : prop spécifiée dans le manuel mais absente de Notion → à créer côté Notion.
- **Notion-only** : prop présente dans Notion mais non spécifiée dans le manuel → à documenter ou à supprimer.
- **Divergente** : nom OK mais type ou options diffèrent.
- 🟢 vert ≤ 1 écart mineur · 🟠 orange 2-4 écarts · 🔴 rouge ≥ 5 écarts ou écart structurant.

## Synthèse exécutive

| # | BDD | Score | Manuel-only | Notion-only | Divergentes | Action principale |
|---|---|---|---|---|---|---|
| 1 | Docs méta LBP | 🟢 | 0 | 0 | 0 | Conforme |
| 2 | Glossaire LBP | 🟠 | 0 | 1 (Notes) | 1 (Created/Last Updated en created_time/last_edited_time vs Date) | Documenter `Notes` ou supprimer |
| 3 | Registre des notes de concept | 🟢 | 0 | 0 | 0 | Conforme |
| 4 | Registre des taxonomies | 🟢 | 0 | 0 | 0 | Conforme |
| 5 | Prompts LBP | 🔴 | 1 (Domaine(s) d'usage : libellés) | 1 (`actif` checkbox) | 4 (Statut deploiement options vides, Environnement options vides, Version plateforme options vides, Domaine d'usage casse minuscule) | Sync taxos + supprimer `actif` |
| 6 | Registre des logic blocks | 🟠 | 0 | 0 | 1 (`Statut de l'objet` apostrophe ASCII vs typo manuel) | Aligner apostrophe (R-052) |
| 7 | Méthodes LBP | 🟠 | 1 (`Domaine(s) d'usage`) | 0 | 1 (rollups `Outils externes mobilisés` / `Templates de bricks mobilisés` typés `text` vs `rollup`) | Créer prop `Domaine(s) d'usage` + convertir rollups |
| 8 | Templates de bricks | 🟠 | 1 (`Domaine(s) d'usage`) | 0 | 1 (rollups `Méthodes (via Prompts)` / `Outils externes (via Prompts)` typés `text` vs `rollup`) | Créer prop `Domaine(s) d'usage` + convertir rollups |
| 9 | Agents LBP | 🔴 | 2 (`Domaine(s) d'usage`, `System prompt (lien source)`) | 0 | 4 rollups typés `text` vs `rollup` (Méthodes/Docs méta/Outils/Templates mobilisés) + 1 nom de relation côté Prompts (`utilise (Prompts LBP)` côté Agents avec miroir attendu `est utilisé par (Agents LBP)` côté Prompts → OK ; mais le manuel dit aussi parfois miroir `utilise (Agents LBP)` cf §7 — incohérence interne au manuel) | Créer 2 props + convertir 4 rollups |
| 10 | Outils externes | 🟠 | 1 (`Domaine(s) d'usage`) | 0 | 2 (rollups `Agents/Méthodes/Templates mobilisés` absents côté Notion ; Notion n'a aucun rollup) + 1 typo (`Valeur ajoutee LBP` / `Entrees attendues` ASCII vs accent manuel) | Créer prop + créer 3 rollups + corriger accents |
| 11 | Manuels de BDD | 🟢 | 0 | 0 | 1 (option taxo `OBJ.STATUT` du manuel vs option `OBJ.STATUT` côté Notion : OK / `Type fonctionnel` Notion comprend des options en plus du manuel : `Digital Twin - analytique officiel`, `Digital Twin - socle structurel`, `Digital Twin - mouvement transformation`, `Digital Twin - observation qualitative amont`, `Digital Twin - socle sémantique` → manuel à enrichir) | Compléter liste options Type fonctionnel dans manuel |

## Détail par BDD

### 1. Docs méta LBP (`64e99b5d-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : 22 / 22. Toutes les propriétés du manuel (Nom canonique, Code unique, Statut, Description, Valeur ajoutée LBP, Usages IA, Aliases, Famille, Mots-clés, Périmètre, Objets encadrés, Règles clés, Quand l'appliquer, Lien doc méta source, est utilisé dans (Prompts LBP), 4 rollups, Created/Last Updated) sont présentes côté Notion avec types et options conformes.
- **Manuel-only** : aucune.
- **Notion-only** : aucune.
- **Divergentes** : aucune. Options de `Famille (Doc méta)` et `Statut de l'objet` cohérentes.
- **Recommandation** : RAS. BDD pilote du canon, à utiliser comme référence.

### 2. Glossaire LBP (`349d8191-...`)
- **Manuel** : ✓ lu (v0.1)
- **Props alignées** : 21 / 22.
- **Manuel-only** : aucune.
- **Notion-only** : `Notes` (texte) — n'apparaît pas dans la section 3.2 du manuel.
- **Divergentes** : 
  - `Created Date` Notion = `created_time` ; manuel dit "Date" → cohérent en pratique (Notion type = created_time pour automatique).
  - `Last Updated Date` Notion = `last_edited_time` ; manuel dit "Date" mais précise "mettre à jour lors de changements" : incohérence sémantique (le manuel laisse penser éditable, alors que Notion l'a en last_edited_time auto). À clarifier dans le manuel.
- **Recommandation** : DOCUMENTER `Notes` dans le manuel ou DROP côté Notion ; CLARIFIER manuel sur Last Updated Date.

### 3. Registre des notes de concept (`4bd4e3a2-...`)
- **Manuel** : ✓ lu (v0.1)
- **Props alignées** : 8 / 8. Champs minimalistes conformes.
- **Manuel-only** : aucune.
- **Notion-only** : aucune.
- **Divergentes** : aucune.
- **Recommandation** : RAS.

### 4. Registre des taxonomies (`421c715c-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : 14 / 14.
- **Manuel-only** : aucune.
- **Notion-only** : aucune.
- **Divergentes** : aucune. Options `Ouverture` (ouverte/fermée), `Nature sémantique` (4 valeurs), `Niveaux autorisés` (3 valeurs), `Mode de sélection` (mono/multi), `Statut` toutes conformes.
- **Recommandation** : RAS.

### 5. Prompts LBP (`307c5df7-...`)
- **Manuel** : ✓ lu (v0.3)
- **Props alignées** : ~26 / 30.
- **Manuel-only** : 
  - aucune en termes de nom ; mais `Domaine(s) d'usage` Notion utilise libellés minuscules `core`, `motor`, `digital twin`, `mission ops` alors que le manuel attend les libellés capitalisés `Core; Motor; Digital Twin; Mission Ops` (cohérence transverse avec autres BDD).
- **Notion-only** : 
  - `actif` (checkbox) : explicitement supprimé en V3 du manuel (cf section 6, "le champ Actif est supprimé en V3 pour éviter le doublon avec Statut de déploiement"). À DROP.
- **Divergentes** :
  - `Statut de déploiement` : manuel attend taxo `PROMPT.DEPLOY_STATUS` avec valeurs (Déployé, Non déployé, Suspendu, Remplacé, Retiré) — Notion a `options: []` (aucune option configurée). À ALIMENTER.
  - `Environnement(s) de déploiement` : manuel attend `PLATFORM.ENV` (test, prod, …) — Notion a `options: []`. À ALIMENTER.
  - `Version(s) de plateforme` : manuel libre mais multi-select — Notion `options: []`. Acceptable au démarrage.
  - `Domaine(s) d'usage` : casse minuscules vs manuel capitalisé.
- **Recommandation** : DROP `actif` ; HARMONISER casse `Domaine(s) d'usage` ; CRÉER OPTIONS pour `Statut de déploiement` et `Environnement(s) de déploiement` (alimenter les taxos PROMPT.DEPLOY_STATUS et PLATFORM.ENV).

### 6. Registre des logic blocks (`101e108f-...`)
- **Manuel** : ✓ lu (v0.1)
- **Props alignées** : 15 / 16.
- **Manuel-only** : aucune.
- **Notion-only** : 
  - `est utilisé dans (Prompts LBP) [texte]` et `s'applique à (Manuels de BDD) [texte]` : ces "jumelles texte" existent côté Notion mais ne sont pas documentées dans la section 3.2 du manuel (qui interdit pourtant les "jumelles texte" en règle générale 3.1). Conflit doctrinal : à TRANCHER (suppression côté Notion ou ajout dans le manuel comme exception transitoire avec justification).
- **Divergentes** : 
  - Notion `Statut de l'objet` (apostrophe ASCII U+0027) ; manuel utilise `Statut de l'objet` (typographique U+2019). Violation R-052. À CORRIGER côté Notion en renommant la propriété.
- **Recommandation** : ALIGNER apostrophe (R-052) ; STATUER sur les jumelles texte.

### 7. Méthodes LBP (`df08a0a0-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : ~25 / 27.
- **Manuel-only** : 
  - `Domaine(s) d'usage` (multi-select Core/Motor/Digital Twin/Mission Ops) : présent dans le manuel (3.2), absent côté Notion. À CRÉER.
- **Notion-only** : aucune (sauf rollups divergents traités plus bas).
- **Divergentes** :
  - `Outils externes mobilisés (via prompts)` : Notion a type `text` ; manuel attend `rollup`. À CONVERTIR en rollup réel.
  - `Templates de bricks mobilisés (via prompts)` : idem, type `text` côté Notion vs `rollup` attendu. À CONVERTIR.
  - Les sous-champs `Entrées attendues - MUST/SHOULD/NICE` côté Notion ne sont pas documentés dans le manuel (qui parle d'un seul champ `Entrées attendues` structuré). Le manuel dit "1 champ avec structure imposée Indispensables/Recommandées/Bonus" alors que Notion a éclaté en 3 + 1 = 4 champs. Conflit structurel : à TRANCHER (manuel à mettre à jour OU Notion à consolider).
- **Recommandation** : CRÉER `Domaine(s) d'usage` ; CONVERTIR 2 champs text en rollups ; TRANCHER éclatement Entrées attendues.

### 8. Templates de bricks (`fefc8f39-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : 13 / 14.
- **Manuel-only** :
  - `Domaine(s) d'usage` (multi-select) : présent manuel, absent Notion. À CRÉER.
- **Notion-only** : aucune.
- **Divergentes** :
  - `Méthodes (via Prompts)` Notion type `text` vs `rollup` attendu.
  - `Outils externes (via Prompts)` Notion type `text` vs `rollup` attendu.
- **Recommandation** : CRÉER `Domaine(s) d'usage` ; CONVERTIR 2 champs en rollups réels.

### 9. Agents LBP (`82a8a779-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : ~16 / 21.
- **Manuel-only** :
  - `Domaine(s) d'usage` (multi-select) : présent manuel, absent Notion. À CRÉER.
  - `System prompt (lien source)` (URL) : présent manuel comme champ critique, ABSENT côté Notion. À CRÉER (priorité haute, critère validé).
- **Notion-only** : aucune.
- **Divergentes** :
  - 4 rollups typés `text` côté Notion vs `rollup` attendu : `Méthodes mobilisées (via prompts)`, `Docs méta mobilisés (via prompts)`, `Outils externes mobilisés (via prompts)`, `Templates de bricks mobilisés (via prompts)`. À CONVERTIR.
  - Nommage relation : Notion a `utilise (Prompts LBP)` côté Agents avec miroir Notion `est utilisé par (Agents LBP)` côté Prompts. Le manuel Agents (§3.2) dit la même chose. ✓ cohérent.
  - Mais la section 7 (Paramétrage Notion) du manuel Agents dit erronément "miroir utilise (Agents LBP)" : incohérence interne au manuel à corriger.
- **Recommandation** : CRÉER 2 props (`Domaine(s) d'usage`, `System prompt (lien source)`) ; CONVERTIR 4 rollups ; CORRIGER incohérence interne du manuel section 7.

### 10. Outils externes (`347a3db7-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : ~16 / 20.
- **Manuel-only** :
  - `Domaine(s) d'usage` (multi-select) : présent manuel, absent Notion. À CRÉER.
  - `Agents mobilisés (via prompts)` (rollup) : prévu manuel (§3.2 et §6), absent côté Notion. À CRÉER.
  - `Méthodes mobilisées (via prompts)` (rollup) : prévu manuel, absent Notion. À CRÉER.
  - `Templates de bricks mobilisés (via prompts)` (rollup) : prévu manuel, absent Notion. À CRÉER.
- **Notion-only** : aucune.
- **Divergentes** :
  - `Valeur ajoutee LBP` (Notion sans accent) vs `Valeur ajoutée LBP` (manuel). À RENOMMER côté Notion.
  - `Entrees attendues` (Notion sans accent) vs `Entrées attendues` (manuel). À RENOMMER.
  - Apostrophe `Mode d'emploi (IA)` Notion = ASCII U+0027 ; manuel utilise typographique U+2019. R-052.
- **Recommandation** : CRÉER 4 propriétés (1 multi-select + 3 rollups) ; RENOMMER 2 props avec accents corrects ; CORRIGER apostrophe.

### 11. Manuels de BDD (`4d8f54e7-...`)
- **Manuel** : ✓ lu (v0.2)
- **Props alignées** : 16 / 17.
- **Manuel-only** : aucune.
- **Notion-only** : aucune.
- **Divergentes** :
  - `Type fonctionnel (BDD décrite)` : Notion contient 13 options (Catalogue, Registre, Templates, et 9 variantes Digital Twin + Mission Ops) ; le manuel n'en liste explicitement que 8 (Catalogue, Registre, Templates, Mission Ops, Digital Twin - extraction directe, pivot, post-traitement, sandbox). Les 5 options manquantes côté manuel : `Digital Twin - analytique officiel`, `Digital Twin - socle structurel`, `Digital Twin - mouvement transformation`, `Digital Twin - observation qualitative amont`, `Digital Twin - socle sémantique`. À ALIMENTER dans la description ≤280 du manuel pour cohérence (ou DROP côté Notion si non utilisées).
- **Recommandation** : COMPLÉTER manuel section 3.2 avec les 5 options Digital Twin manquantes ; ou clarifier statut (canoniques vs legacy).

## Recommandations transverses

### Patterns récurrents observés

1. **Rollups typés `text` au lieu de `rollup` réel** (BDDs 7, 8, 9 — soit 4+2+2 = 8 champs) : généralisation d'un anti-pattern où la propriété rollup n'a pas été configurée comme rollup natif Notion mais saisie manuellement en texte. **Impact** : pas d'agrégation automatique, dette de maintenance forte. Action : **convertir tous ces champs en rollups natifs** (passe technique unique).

2. **Champ `Domaine(s) d'usage` manquant côté Notion** (BDDs 7, 8, 9, 10 — soit 4 BDDs Motor Brain) : ajout récent au canon manuel non encore propagé. Action : **batch creation** d'un multi-select identique sur les 4 BDDs (options : Core, Motor, Digital Twin, Mission Ops).

3. **Casse incohérente Domaine(s) d'usage** (BDD 5 Prompts LBP) : minuscules vs Capitalized ailleurs. Harmoniser sur la forme capitalisée du canon.

4. **Apostrophes ASCII U+0027 dans noms de propriétés Notion** (BDDs 6, 10 confirmées ; à scanner sur les autres) : violation R-052. Action : **scan + renommage en typographique U+2019**.

5. **Options de select vides côté Notion là où le manuel attend des taxos pleines** (BDD 5 Prompts : `Statut de déploiement`, `Environnement(s) de déploiement`) : à alimenter en se basant sur PROMPT.DEPLOY_STATUS et PLATFORM.ENV.

6. **"Jumelles texte" non documentées** (BDD 6 Logic blocks) : conflit doctrinal entre règle 3.1 ("pas de jumelles texte") et présence côté Notion. Statuer.

7. **Incohérence manuel ↔ Notion sur le typage de champs dates système** (Glossaire) : le manuel parle de "Date" mais Notion a `created_time` / `last_edited_time` ; à uniformiser le vocabulaire dans les manuels (utiliser explicitement les types Notion).

### Ordre d'attaque suggéré (par criticité × volume)

1. **Sprint 1 — Quick wins faible risque** : DROP `actif` côté Prompts LBP (1 champ, déjà acté en V3 du manuel). RAS sur BDDs 1/3/4 (déjà conformes).
2. **Sprint 2 — Création des `Domaine(s) d'usage` manquants** : 4 BDDs (Méthodes, Templates, Agents, Outils) — multi-select identique copiable.
3. **Sprint 3 — Création des rollups manquants ou mal typés** : 8 conversions text→rollup + 3 rollups absents (Outils externes). Passe technique cohérente.
4. **Sprint 4 — Création props critiques manquantes** : `System prompt (lien source)` Agents LBP (priorité haute car critère de validation des fiches Agents).
5. **Sprint 5 — Alimentation des options de taxos vides** : `Statut de déploiement` (PROMPT.DEPLOY_STATUS) et `Environnement(s) de déploiement` (PLATFORM.ENV) côté Prompts LBP.
6. **Sprint 6 — Harmonisation typographique R-052** : scan apostrophes ASCII et accents manquants (BDDs 6 et 10 confirmées, à étendre).
7. **Sprint 7 — Mise à jour manuels** : compléter options `Type fonctionnel` (Manuels de BDD), corriger incohérence interne manuel Agents §7, clarifier sort des jumelles texte (Logic blocks), documenter ou supprimer `Notes` (Glossaire), trancher éclatement `Entrées attendues` (Méthodes).

### Volume global d'écarts
- **Conformes (🟢)** : 4 BDDs (Docs méta, Notes de concept, Taxonomies, Manuels de BDD avec réserve options).
- **Orange (🟠)** : 5 BDDs (Glossaire, Logic blocks, Méthodes, Templates, Outils).
- **Rouge (🔴)** : 2 BDDs (Prompts LBP, Agents LBP) — concentrent les écarts les plus structurants.

Total estimé : **~20 actions Notion** (créations / conversions / renommages) + **~6 actions Manuels** (clarifications doctrinales).
