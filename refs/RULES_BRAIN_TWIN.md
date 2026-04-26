# Règles de gestion du Brain et du Digital Twin

> Ce fichier recense les règles **intrinsèques à l'écosystème LBP** (Brain + Twin + Mission Ops).
> Les règles contextuelles à notre collaboration (comportement de Claude, outillage) sont dans `CLAUDE.md` (IDs `C-XXX`).
> Chaque règle a un ID stable (`R-XXX`) qui ne change jamais, même si la règle déménage de section.
> Dernière mise à jour : 2026-04-25 — R-036 révisée + ajout R-038 (identifiant pivot par type d'objet)

---

## Format d'une règle

Chaque règle suit ce format pour homogénéité et lisibilité :

```markdown
### R-XXX : Titre court

- **Portée** : Brain / Twin / Mission Ops / Transverse
- **Statut** : Actif / En discussion / Archivé
- **Why** : Motivation (raison d'être, incident à l'origine)
- **How to apply** : Quand et comment appliquer concrètement
- **Exemples** : ✅ bon usage / ❌ mauvais usage
- **Découverte** : Date + contexte d'émergence
```

---

## Règles d'évolution de ce document (auto-restructuration)

Ces règles sont mes engagements pour maintenir la lisibilité du document à mesure qu'il grossit. Je les applique proactivement et je propose les restructurations — tu arbitres.

- **Stabilité des IDs** : l'ID `R-XXX` est immuable. On ne renumérote jamais, même si la règle déménage de section.
- **Déplacement** : si une règle change de section, on la déplace mais on garde l'ID. On note l'ancienne section dans le champ *Découverte* si utile.
- **Remplacement** : si une règle est supplantée, on marque l'ancienne `Archivé` (sans la supprimer) avec un pointeur vers la nouvelle.
- **Règle de scission** : si une sous-section dépasse ~8 règles, je propose de la scinder en sous-sous-sections thématiques.
- **Règle de promotion (inbox)** : dès que la section *À classer (inbox)* accumule 3+ entrées, je propose de les reclasser.
- **Règle de fusion / conflit** : si deux règles se chevauchent ou se contredisent, je le signale et je propose fusion, fusion partielle, ou révision avec archivage.
- **Housekeeping périodique** : à chaque milestone majeur (fin d'un gros chantier), je propose une revue structurelle du doc (ordre des sections, dénomination, détection de doublons).
- **Cohérence avec le backlog** : quand je promeus une règle du backlog vers ce doc, je laisse une trace dans le backlog (section historique).

---

## Sommaire

- [1. Règles transverses (gouvernance globale)](#1-règles-transverses)
- [2. Règles Brain](#2-règles-brain)
- [3. Règles Digital Twin](#3-règles-digital-twin)
- [4. Règles Mission Ops](#4-règles-mission-ops)
- [5. Règles de propagation d'impacts](#5-règles-de-propagation-dimpacts)
- [6. À classer (inbox)](#6-à-classer-inbox)

---

## 1. Règles transverses

*Règles qui s'appliquent à tout l'écosystème, indépendamment du domaine.*

### 1.1 Source de vérité et gouvernance

#### R-001 : Source de vérité = doc Markdown

- **Portée** : Transverse
- **Statut** : Actif
- **Why** : Éviter la divergence entre le contenu et son index. Le doc est portable, versionable, lisible IA ; Notion peut évoluer sans perte.
- **How to apply** : Pour modifier un objet, on modifie d'abord le doc MD, puis on aligne Notion. Jamais l'inverse.
- **Découverte** : Principe architectural originel.

> Les règles R-003 (confirmation humaine), R-009 (vault unique) et R-010 (git) ont été déplacées vers `CLAUDE.md` (IDs `C-001`, `C-002`, `C-003`) car elles relèvent de notre collaboration plutôt que de l'écosystème lui-même.

### 1.2 Zero contamination

#### R-002 : Zero donnée client dans Core / Motor

- **Portée** : Transverse (frontière Brain / Twin / MissOps)
- **Statut** : Actif
- **Why** : Le Brain est réutilisable entre missions. Contamination = perte de réutilisabilité.
- **How to apply** : Les domaines Core et Motor Brain ne contiennent jamais de données client. Seuls Digital Twin et Mission Ops sont instanciés par mission.
- **Exemples** : ✅ "Capacité Organisationnelle" dans Glossaire LBP / ❌ "Capacité Organisationnelle - Client X" dans Glossaire LBP
- **Découverte** : Principe architectural originel.

### 1.3 Qualité documentaire (QA)

#### R-039 : Aucun artefact de génération IA dans les docs LBP

- **Portée** : Transverse (tous les documents LBP : manuels, notes de concept, glossaire, taxonomies, prompts, méthodes, templates, frontmatters, contenus de fiches Notion, etc.)
- **Statut** : Actif
- **Why** : Les générateurs IA (notamment ChatGPT/o1 avec sources web) laissent parfois des artefacts de citation ou de balisage qui ne devraient jamais apparaître dans le doc final. Ces artefacts cassent la lisibilité, polluent l'extraction sémantique, et trahissent un défaut de relecture avant publication.
- **How to apply** : Avant de finaliser ou publier tout doc LBP (vault, Notion, Drive), faire une **passe QA anti-artefacts** qui détecte et supprime au minimum :
  - `:contentReference[oaicite:N]{index=N}` (citation OpenAI/Bing brute)
  - `【N†source】` ou `[N†source]` (citations OpenAI tournée)
  - `[citation:N]`, `[ref:N]`, `[1]`, `[2]`... isolés sans bibliographie
  - `<sup>N</sup>` orphelins
  - Caractères de remplacement Unicode (`�`, `\ufffd`)
  - Balises markdown brisées (`**...` ou `[...](` non fermés)
  - Fragments de placeholders non résolus (`[[NOM_OBJET]]`, `<INSTR>...</INSTR>`)
  - Texte tronqué visible (phrases coupées en milieu, comme "décin collective" au lieu de "décisions et de la performance collective")
- **Exemples détectés** :
  - ❌ Note vault `concept - Repères communs.md` : `Ils peuvent être symboliques [...] fonctionnels:contentReference[oaicite:5]{index=5}iguïtés en rendant visibles des attentes communes.` (artefact de citation + texte tronqué) — corrigé manuellement à l'indexation Notion (batch C, 2026-04-25)
  - ❌ Note vault `concept - Soft skill.md` : `qualité des interactions, des décin collective.` (texte tronqué)
- **Outillage suggéré** : grep de motifs avant publication, ou contrôle automatique dans pipeline d'indexation.
- **Conséquence si violation** : doc à corriger en source (vault) ET en cible (Notion) ; relire systématiquement la sortie de tout générateur IA avant intégration.
- **Découverte** : 2026-04-25, Leonard, après détection en batch C de 2 occurrences sur 72 notes de concept.

---

## 2. Règles Brain

*Règles spécifiques à la gouvernance du Brain (Core + Motor + Admin).*

### 2.1 Nommage et identification des objets

#### R-005 : Code unique stable

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Référencement stable entre BDD, résistance aux renommages.
- **How to apply** : Le code unique d'un objet Brain (ex: `CPT.GOV.LBP.SSOT`) ne change jamais, même si le nom canonique évolue.
- **Découverte** : Règle initiale.

*Sous-section à enrichir quand on formalisera les conventions de nommage des nouveaux objets (actif, poste, collectif, etc.).*

### 2.2 Templates et instanciation

#### R-004 : Template obligatoire pour tout nouveau doc Brain

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Homogénéité, gouvernance par les Docs méta, agents IA capables d'instancier.
- **How to apply** : Tout doc Brain est généré à partir d'un template (indexé dans Docs méta LBP). Cycle : Template → instanciation → cleanup → validation → indexation Notion.
- **Découverte** : Principe architectural originel.

#### R-040 : Toutes les instructions de génération vivent dans des blocs `@INSTR-*`

- **Portée** : Brain (templates d'instanciation)
- **Statut** : Actif
- **Why** : Un template définit la structure du doc final (sections numérotées `# 1)`, `# 2)`, etc.). Si une instruction de génération apparaît sous forme d'un titre Markdown numéroté (ex. `# 0) GUIDE D'INSTANTIATION`), elle se confond visuellement avec les vraies sections du doc final, crée un parasitage cognitif (la séquence `0,1,2,3...` laisse penser que `0)` est le début légitime de la structure), et augmente le risque que l'agent générateur oublie de la supprimer ou la prenne par mimétisme pour un modèle de section. Par construction, les instructions de génération ne doivent **jamais** ressembler à une section du doc final.
- **How to apply** :
  - Tout contenu qui guide la génération du doc (instructions, doctrine, exemples normatifs, paramétrages, vocabulaire contrôlé, guide d'instanciation, settings…) DOIT vivre **exclusivement** dans un bloc `<!-- @INSTR-START: NOM_BLOC ... @INSTR-END: NOM_BLOC -->`.
  - **Aucun titre Markdown numéroté** (`# 0)`, `## 0.1`, etc.) ne doit servir de wrapper à des instructions de génération.
  - Les blocs `@INSTR-*` sont **flottants** dans le template (placés là où c'est lisible pour l'auteur du template) et tous **systématiquement supprimés** à l'instanciation par la `cleanup_rules` standard `SUPPRIMER tous les commentaires HTML @INSTR-*`.
  - La `cleanup_rules` du template ne doit **jamais** contenir une règle ad hoc du type `SUPPRIMER la section 0) GUIDE D'INSTANTIATION` puisque cette section ne doit pas exister.
  - Les sections numérotées `# 1)`, `# 2)`, etc. sont **réservées à la structure du doc final** et ne contiennent jamais de contenu d'instruction de génération.
  - Une vraie section structurelle d'un doc final peut légitimement être numérotée `# 0)` si elle décrit du contenu métadata du doc (ex. `# 0) Meta de la brick` dans `Template méta de Brick.md` qui contient des sous-sections 0.1 Contexte & mandat, 0.2 Sources & procédé de production…). Le critère de discrimination : ce contenu apparaît-il dans le doc instancié final (oui = structure, à laisser) ou est-il supprimé à l'instanciation (oui = instruction, à wrapper dans `@INSTR-*`) ?
- **Exemples** :
  - ✅ `<!-- @INSTR-START: INSTANTIATION_GUIDE [contenu] @INSTR-END: INSTANTIATION_GUIDE -->` placé entre les autres blocs `@INSTR-*` du template.
  - ❌ `# 0) GUIDE D'INSTANTIATION — [INSTR-SECTION] (SUPPRIMER APRÈS USAGE)` suivi de sous-titres `## 0.1`, `## 0.2`…
  - ❌ `cleanup_rules: - SUPPRIMER la section 0) GUIDE D'INSTANTIATION` (témoigne d'une violation à corriger).
- **Conséquences** :
  - ✅ Structure du doc final sacrée et lisible (numérotation commence à `1`, jamais à `0` pour des instructions).
  - ✅ Une seule règle de cleanup suffit : `SUPPRIMER tous les commentaires HTML @INSTR-*`.
  - ✅ Pas de risque de contamination structurelle ni d'oubli de suppression.
- **Migration effectuée** : 2026-04-26 — 6 templates corrigés (Template Manuel de BDD - Digital Twin v6.1.0→v6.2.0 ; Template WR-RD - Digital Twin v1.0.0→v1.1.0 ; template-methode_lbp v1.0.0→v1.1.0 ; Template-prompt_lbp v1.0.0→v1.1.0 ; Template-Fiche_outil_LBP v1.0.0→v1.1.0 ; template-taxonomie). Le 7e cas (`# 0) Meta de la brick` dans `Template méta de Brick.md`) est conservé car c'est une vraie section structurelle du doc final.
- **Découverte** : 2026-04-26, Leonard, après revue des templates Manuel de BDD - Digital Twin v6.1.0 et WR-RD - Digital Twin v1.0.0.

### 2.3 Indexation Notion (doc → BDD)

#### R-006 : Descriptions Notion ≤280 caractères

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Lisibilité Notion, cohérence inter-BDD, utilisabilité par les agents.
- **How to apply** : Les descriptions de propriétés dans Notion commencent par un verbe à l'infinitif, restent en texte brut, ne dépassent pas 280 caractères. On les copie directement depuis le manuel de BDD.
- **Découverte** : Convention établie dans les templates de manuels de BDD.

#### R-029 : Le doc Markdown est source de vérité pour l'indexation Notion

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Éviter toute divergence entre le contenu du doc et ses propriétés Notion. Les propriétés sont dérivées, pas inventées.
- **How to apply** : Avant de créer ou mettre à jour une entrée Notion, l'agent doit **lire l'intégralité du doc Markdown correspondant**. Les propriétés sont dérivées du contenu. Si une propriété ne peut pas être dérivée du doc de façon non-ambiguë, laisser vide et signaler plutôt qu'inventer. Respecter les contraintes de format portées par **la description de chaque propriété Notion** (qui fait office d'instructions d'écriture).
- **Exemples** : ✅ `Définition` remplie avec 3-10 lignes extraites/synthétisées du doc (car la description Notion impose 3-10 lignes) / ❌ `Définition` générée de toutes pièces par l'agent
- **Découverte** : 2026-04-24, Leonard, avant indexation Twin v2

#### R-030 : Double indexation d'une note de concept

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Le Glossaire LBP est un hub sémantique qui n'a pas de lien source direct. Le lien vers le doc vit côté `Registre des notes de concept`. Le Glossaire porte la sémantique, le Registre porte la traçabilité.
- **How to apply** : Indexer une note de concept = créer **2 entrées Notion liées** :
  1. Une entrée dans `Registre des notes de concept` avec `Lien note concept (source) = URL Drive`
  2. Une entrée dans `Glossaire LBP` avec les propriétés sémantiques (Type concept, Domaine, Définition, Règles d'usage, etc.)
  3. Lier l'entrée Glossaire → Registre via la relation `est documenté par (notes de concept)`
  4. Si applicable, lier également Glossaire → Méthodes (`est mis en oeuvre par`) et/ou Glossaire → Manuels de BDD (`est modélisé par`)
- **Découverte** : 2026-04-24, Leonard, avant indexation Twin v2

#### R-031 : Alignement du code unique entre note de concept et glossaire

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Traçabilité stable et navigation cohérente. Un même concept doit avoir le **même code** dans les deux BDD.
- **How to apply** : Le `Code unique` d'une entrée dans `Registre des notes de concept` et l'entrée correspondante dans `Glossaire LBP` doivent être strictement identiques (ex: `CPT.CAP.LBP.ACTIF` dans les deux). Ce code provient du doc Markdown source (propriété ou convention du template).
- **Découverte** : 2026-04-24

#### R-033 : Les descriptions de propriétés Notion sont des mini-prompts de remplissage

- **Portée** : Brain (indexation)
- **Statut** : Actif (temporaire — à updater quand les BDD Brain auront leurs docs d'instructions d'écriture et clefs de lecture)
- **Why** : Pour les BDD du Brain, les **instructions d'écriture** ne vivent pas encore dans des docs séparés ; elles sont portées par les **descriptions de chaque propriété Notion**. Ignorer ces descriptions produit des contenus hors format.
- **How to apply** : Avant de remplir une propriété, **lire sa description Notion** (via `notion-fetch` sur la data source). Respecter scrupuleusement les contraintes :
  - Format imposé (ex: "3 à 10 lignes", "séparateur ';'", "MAJUSCULES")
  - Structure imposée (ex: "Bon usage: ... ; Mauvais usage: ...")
  - Valeurs strictes pour les select/multi-select (ex: "valeurs strictes: Core; Motor")
  - Interdictions (ex: "ne pas inclure de contenu client")
- **Exemples** : ✅ Pour `Code unique` d'une taxo, la description impose format `NAMESPACE.FAMILLE.LBP` MAJUSCULES alignée au mini-doc → valeur dérivée du nom de fichier .md / ❌ Inventer un code libre
- **Découverte** : 2026-04-24. À faire évoluer quand les docs d'instructions d'écriture dédiés existeront pour les BDD Brain (aujourd'hui seules les BDD Twin en ont, cf. `Clefs de lectures/TWIN - Instructions écriture + clefs de lecture/`).

#### R-035 : Ordre d'indexation inter-types (graphe de dépendances)

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Chaque type d'artefact Brain a des relations vers d'autres types. Pour éviter de créer une dette de relations (à rattraper dans des passes ultérieures), on indexe par ordre de dépendance : feuilles d'abord, types qui les consomment ensuite.
- **How to apply** : Respecter cet ordre pour une indexation Brain complète :
  1. **Taxonomies** (type feuille — aucune dépendance vers d'autres types Brain)
  2. **Manuels de BDD** (consomment les Taxonomies via `utilise (taxonomies)`)
  3. **Notes de concept + Glossaire** (Glossaire peut référencer Manuels via `est modélisé par`, Méthodes via `est mis en oeuvre par`)
  4. **Méthodes, Agents, Prompts, Logic blocks, Outils externes, Templates de bricks** (consomment Glossaire, Manuels, Docs méta)
- **Généralise R-034** : R-034 dit "créer puis relier" au sein d'un batch. R-035 étend à l'échelle inter-types.
- **Exemples** : ✅ Indexer ASSET.SUBTYPE → puis Manuel Actifs peut référencer ASSET.SUBTYPE dans sa création / ❌ Indexer Manuel Actifs d'abord avec relation vide vers ASSET.SUBTYPE, puis revenir plus tard (dette)
- **Découverte** : 2026-04-24, mini-batch 0 a créé une dette (Manuel Actifs sans ses 7 autres taxos non encore créées). Règle posée pour ne pas reproduire.

#### R-037 : Lecture complète du doc obligatoire avant indexation (pas de raccourci frontmatter)

- **Portée** : Brain (indexation) — **tous types de docs**
- **Statut** : Actif (renforce R-029)
- **Why** : Le frontmatter YAML résume les métadonnées structurelles (title, code, scale_kind, aliases). Les propriétés Notion narratives (Description source, Description courte, Définition, Règles d'usage, Valeur ajoutée...) exigent le contenu approfondi qui vit dans les **sections du corps du doc** (intention + règles d'usage + exclusions + "quoi choisir / quand" + distinctions + patrons d'arbitrage + exemples). Se limiter au frontmatter produit des descriptions pauvres et non-actionnables.
- **How to apply** : Pour indexer **tout doc Brain** (taxonomie, note de concept, manuel de BDD, méthode, prompt, etc.), **lire l'intégralité du doc** avant de remplir les propriétés narratives. Le frontmatter sert uniquement à extraire les champs structurés (title, code, type). Tout le reste doit venir de la lecture du corps :
  - **Taxonomie** : sections 1 (objet/but), 2 (détection du domaine), 5 (heuristique), 8 (exemples) → Description source + Description courte
  - **Note de concept** : sections 1 (résumé, définition, périmètre), 2 (rôle, valeur), 3 (caractéristiques, modules), 4 (relations), 7 (bonnes pratiques) → Définition + Règles d'usage + Valeur ajoutée + Usages IA
  - **Manuel de BDD** : sections 1 (identité), 2 (périmètre/frontières), 3 (rôle systémique), 4 (modèle de données) → Description + Valeur ajoutée + Usages IA
  - **Glossaire** (dérivé de note de concept via R-030) : lire la note de concept ET le doc auquel elle fait référence pour synthétiser
- **Exemples** : ✅ Lire `ORG.CONTEXTE.LBP.md` en entier pour en tirer une Description source qui mentionne "qualifie le contexte organisationnel d'un poste par niveau de périmètre ; règles : choisir 1 seule valeur, ne pas typer un collectif ou une organisation avec cette taxo" / ❌ Se contenter du `summary:` du frontmatter qui dit juste "Qualifie le contexte d'ancrage d'un poste"
- **Découverte** : 2026-04-24, Leonard, après batch A1 où raccourci frontmatter-only a produit des descriptions jugées pauvres

#### R-034 : Ordonnancement création puis relation (2 passes)

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Notion exige que les 2 entrées cibles d'une relation existent avant de pouvoir les lier. Lors d'une indexation par batch, créer d'abord toutes les entrées, puis créer les relations dans une seconde passe.
- **How to apply** :
  1. **Passe 1 — Créations** : créer toutes les entrées Notion sans établir leurs relations (ou seulement les relations vers des entrées déjà existantes)
  2. **Passe 2 — Relations** : établir les relations entre entrées créées dans la passe 1
  3. En pratique : regrouper les doc par "type sans dépendance" en premier (ex: taxonomies), puis types dépendants (ex: manuels qui référencent taxonomies), puis types couvrant le graphe (ex: glossaire qui pointe vers manuels)
- **Exemples** : ✅ Créer Manuel Actifs + Taxo ASSET.SUBTYPE → puis relier Manuel → Taxo / ❌ Tenter de créer le Manuel avec relation vers Taxo qui n'existe pas encore
- **Découverte** : 2026-04-24, lors du dry-run mini-batch 0

#### R-032 : Mise à jour plutôt que création pour une entrée existante

- **Portée** : Brain (indexation)
- **Statut** : Actif
- **Why** : Éviter les doublons Notion. Les entrées existantes portent peut-être des relations, des rollups, des références qu'on casserait en recréant.
- **How to apply** : Avant de créer une entrée Notion, vérifier qu'elle n'existe pas déjà (par `Code unique` d'abord, puis par `Nom canonique`). Si elle existe :
  - **Mettre à jour** toutes les propriétés en lisant le nouveau doc (cf. R-029)
  - **Mettre à jour le lien source** si le chemin Drive a changé
  - **Ne pas changer le `Code unique`** (stable par R-005)
  - Si le doc v2 porte un **nom ou code différent** de la v1, alors **archiver l'entrée v1** (Statut = Archivé) et **créer une nouvelle entrée v2** (R-036)
- **Découverte** : 2026-04-24

#### R-036 : Le Code unique est l'identité ; MAJ en place tant que le code est stable

- **Portée** : Brain (indexation)
- **Statut** : Actif (révisé 2026-04-25 par Leonard)
- **Why** : Le `Code unique` est l'identité stable de l'objet ; le `Nom canonique` n'est qu'un libellé éditable. Tant que le code est inchangé, l'entité est la même — seul son libellé / sa description / son URL évoluent. Préserver l'entrée existante préserve aussi ses relations Notion entrantes (rollups, références d'autres BDD), ses ID Notion stables, et évite de polluer le Registre avec des doublons archivés.
- **How to apply** :
  - **Code identique** (même si le nom canonique change, peu importe l'amplitude du changement) → **mise à jour en place** de l'entrée existante (Nom, Description, URL Drive, Aliases, etc.). Pas d'archivage.
  - **Code différent** (renommage de namespace, changement de TOKEN, scission/fusion d'objet) → archive de l'entrée v1 + création d'une nouvelle entrée v2.
- **Exemples** :
  - ✅ ORG.CONTEXTE.LBP : v1 "Contexte d'ancrage de rôle" → v2 "Contexte d'ancrage organisationnel d'un poste" (code stable) → **MAJ** de v1
  - ✅ ORG.DEP_LEVEL.LBP → COL.DEP_LEVEL.LBP (code change suite à scission UO→Orga+Collectif) → archive v1 + création v2
  - ✅ ACT.CANDIDATE_TYPE.LBP → ACT.CONSOLIDATION_TARGET.LBP (TOKEN change) → archive v1 + création v2
- **Conséquence** : Registre propre, IDs Notion stables, relations préservées. La trace des évolutions de libellés vit dans l'historique Notion (créé/last edited) et le journal git.
- **Note historique** : version initiale (2026-04-24) imposait archive+create dès que le nom changeait — révisée le 2026-04-25 après détection de 25 doublons inutiles dans batchs A1+A2 (correctifs appliqués).
- **Découverte / révision** : 2026-04-25, Leonard, après examen des batchs A1+A2

#### R-038 : Identifiant pivot par type d'objet (taxonomies = code, autres = nom)

- **Portée** : Brain (indexation, déduplication)
- **Statut** : Actif
- **Why** : R-036 (test de doublon par code unique) ne s'applique strictement qu'aux taxonomies. Pour les autres BDD Brain, le code n'est pas (encore) un identifiant fiable : il peut changer au cours d'updates, n'est pas systématiquement renseigné, ou n'est pas conçu comme pivot de déduplication. C'est le **Nom canonique** qui sert d'identifiant pivot pour ces objets. Confondre les deux logiques amène à créer des doublons (pour les taxos quand on dédoublonne par nom) ou à manquer des doublons (pour les manuels quand on dédoublonne par code).
- **How to apply** :
  - **Taxonomies** → identifiant pivot = `Code unique` (format `XXX.YYY.LBP`, immuable). Application stricte de R-036.
  - **Manuels de BDD, Notes de concept, Glossaire, autres BDD Brain** → identifiant pivot = `Nom canonique` (avec normalisation : trim, casse insensible, accents normalisés pour la comparaison). Le code éventuellement présent est informatif, pas pivot.
  - Lors d'une indexation Notion : avant toute création, requêter le registre cible avec le bon champ pivot. Si match → MAJ en place ; sinon → création.
- **Exemples** :
  - ✅ Taxo ORG.CONTEXTE.LBP : doublon détecté par code → MAJ v1
  - ✅ Manuel "Actifs" (anciennement "Ressources") : doublon détecté par nom (après normalisation) — pas par code, qui peut avoir changé
  - ❌ Tester un doublon de manuel uniquement par code : risque de rater une refonte de nom + code, ou de créer un faux doublon si le code a évolué
- **Conséquence** : R-036 reste valable mais son champ pivot dépend du type d'objet. Cette règle préfigure la procédure de réconciliation pour les batchs B (Manuels) et C (Notes concept + Glossaire).
- **Découverte** : 2026-04-25, Leonard, après correction des 25 doublons A1+A2 — précision donnée pour anticiper les batchs Manuels et Notes concept.

### 2.4 Gouvernance des taxonomies

#### R-007 : Taxonomies par codes

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Séparer le stockage lisible (libellés) du référencement stable (codes).
- **How to apply** : Les BDD stockent des libellés humains. Les codes taxonomiques (ex: `OBJ.STATUT.LBP`) apparaissent uniquement dans les descriptions ≤280 et dans la documentation. Pas de codes dans le corps des textes.
- **Découverte** : Convention établie dans les templates.

#### R-008 : Statuts harmonisés

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Uniformité de gouvernance à travers les 11 BDD Brain.
- **How to apply** : Toutes les BDD Brain utilisent la taxonomie `OBJ.STATUT.LBP` avec les valeurs `Brouillon`, `Validé`, `À revoir`, `Archivé`.
- **Découverte** : Convention établie.

### 2.5 Génération d'une BDD à partir d'un manuel

*Section à remplir quand on documentera le workflow "manuel de BDD → BDD Notion".*

### 2.6 Archivage des docs Brain

#### R-026 : Archivage local par dossier thématique

- **Portée** : Transverse (Brain + Twin)
- **Statut** : Actif
- **Why** : Éviter qu'un "grenier global" à la racine du vault gonfle sans fin et rende l'archivage illisible. Garder l'archive proche de son contexte thématique.
- **How to apply** : Chaque dossier thématique (`Manuels de BDD/Digital Twin/`, `Notes de Concept/`, `Taxonomies/`, `Logic Blocks/`, `Docs Méta LBP/`) a son propre sous-dossier `archives/`. Le git garde l'historique complet des déplacements — pas besoin de doublons dans le vault.
- **Exemples** : ✅ `Notes de Concept/archives/concept - Ressource.md` / ❌ `ARCHIVES/Notes de Concept/...`
- **Découverte** : 2026-04-24, conception arborescence cible pour refonte Twin v2 (D-010)

### 2.7 Conventions de nommage

#### R-027 : Conventions de nommage des fichiers Brain/Twin

- **Portée** : Transverse
- **Statut** : Actif
- **Why** : Homogénéité visuelle dans Obsidian, compatibilité clavier, interopérabilité inter-outils.
- **How to apply** :
  - **Séparateur** : tiret simple `-` (jamais tiret cadratin `—`, jamais underscore)
  - **Casse manuels de BDD** : Title Case, ex: `Manuel de BDD - Actifs.md`
  - **Casse notes de concept** : minuscule, ex: `concept - Actif.md`
  - **Casse taxonomies** : code canonique, ex: `ACT.IMPACT_DOMAIN.LBP.md`
  - **Accents et apostrophes typographiques autorisés** (Obsidian et Drive les gèrent)
  - **Préfixe** : pour les concepts, toujours `concept - `. Pour les manuels Twin v2, `Manuel de BDD - `.
- **Exemples** : ✅ `Manuel de BDD - Relations inter-organisations.md`, `concept - Poste.md`, `ORG_REL.TYPE.LBP.md` / ❌ `Manuel de BDD — Actifs.md` (cadratin), `Concept - Actif.md` (majuscule), `BDD_ACTIFS.md` (underscore)
- **Découverte** : 2026-04-24, standardisation lors de la migration Twin v2 (D-011)

### 2.7 Relations inter-BDD Brain

*Section à remplir quand on formalisera les règles de relations (hub-spoke, miroirs, bidirectionnalité...).*

### 2.8 Hiérarchies et héritage

*Section à remplir quand on clarifiera les patterns d'héritage (notes de concept ← glossaire, manuels ← taxonomies, etc.).*

---

## 3. Règles Digital Twin

*Règles spécifiques à la gouvernance des BDD instanciées du Digital Twin. Source principale : Panorama V2 v3 (2026-04-22).*

### 3.1 Ontologie des objets

#### R-011 : Frontières fortes entre objets canoniques

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Le Twin produit de la valeur à condition que ses objets restent conceptuellement nets. Sans frontières strictes, les relations deviennent incohérentes et les analyses inexploitables.
- **How to apply** : Maintenir les distinctions canoniques suivantes, qui ne doivent jamais être confondues :
  - une **Organisation** n'est pas un **Collectif** (institution juridique vs groupement humain opérant)
  - un **Poste** n'est pas un **Individu** (position formelle vs personne physique)
  - un **Actif** n'est pas un **Environnement** (support mobilisable vs cadre d'usage/contrainte)
  - une **Pratique** n'est pas un **Processus** (pattern opérant récurrent vs fonctionnement structuré)
  - une **Problématique** n'est pas un **Enjeu** (nœud diagnostique consolidé vs formulation structurée d'un besoin/tension)
  - un **Modulateur** n'est ni une **Capacité**, ni une **Pratique**, ni une **Problématique** (condition d'effectivité transversale)
  - un **Événement** n'est pas une **Initiative** (repère temporel vs effort intentionnel structuré)
  - une **Action détectée** n'est pas une **Pratique** (geste observé vs pattern récurrent consolidé)
- **Exemples** : ✅ Une équipe produit = Collectif ; SA TotalEnergies = Organisation / ❌ "Équipe ABC (SA)" dans Organisations
- **Découverte** : Panorama V2 v3, §3.2

#### R-012 : Séparation des 4 régimes de connaissance

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Éviter les glissements entre symptôme et diagnostic, la sur-interprétation du brut, la confusion entre vu/pensé/décidé.
- **How to apply** : Tout contenu du Twin relève d'un des 4 régimes, à ne jamais mélanger :
  1. **Preuve source** : observé, documenté, cité, transcrit
  2. **Qualification structurée** : typé, relié, mis en forme
  3. **Consolidation analytique** : stabilisé comme objet de lecture/diagnostic
  4. **Pilotage / action** : oriente, mesure, transforme
- **Découverte** : Panorama V2 v3, §3.1

### 3.2 Architecture des BDD

#### R-018 : Spécialisation des propriétés génériques à l'écriture

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Un socle générique commun ne garantit pas une grammaire de remplissage identique. Une description d'individu ne ressemble pas à une description d'actif.
- **How to apply** : Respecter les propriétés génériques communes (Description, Indices observés, Indices d'existence, Commentaires, Merge Notes, Logs) mais appliquer des **instructions d'écriture spécifiques à chaque objet**. Les manuels de BDD portent cette doctrine.
- **Exemples** : ✅ Description d'une problématique = nœud diagnostique consolidé + périmètre + logique centrale ; Description d'un actif = ce que c'est + à quoi il sert + pour qui / ❌ Description uniforme "texte libre 3-10 lignes"
- **Découverte** : Panorama V2 v3, §3.7 et §8.4

#### R-019 : Architecture en 5 couches d'une BDD bien spécifiée

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Homogénéité de design et lisibilité des fiches. Chaque couche répond à une question distincte.
- **How to apply** : Une BDD importante du Twin est pensée comme un empilement cohérent :
  1. **Propriétés génériques** (gouvernance, traçabilité)
  2. **Relations + jumelles textes** (graphe + formulation observée)
  3. **Propriétés spécifiques** (pouvoir explicatif propre)
  4. **Couche 5D** (traversabilité systémique)
  5. **Couche calculée** (rollups + formules)
- **Exemples** : Variantes d'intensité selon famille (registre, socle sémantique, extraction factuelle, socle structurel, post-traitement analytique) — cf. Panorama §9.2
- **Découverte** : Panorama V2 v3, §9.1

### 3.3 Doctrine relationnelle

#### R-013 : Sobriété relationnelle

- **Portée** : Twin
- **Statut** : Actif
- **Why** : La saturation relationnelle rend le graphe illisible et les rollups peu fiables. Les "edges décoratifs" détériorent la valeur analytique.
- **How to apply** : Une relation réelle n'est créée que si elle apporte un gain clair de : compréhension, traversée, consolidation, comparaison, ou diagnostic. Éviter les relations "au cas où" et les raffinements sans gain net.
- **Exemples** : ✅ `Organisation → comprend → Collectif` ; `OKR → est mesuré par → Indicateur` / ❌ Relation décorative "est mentionné par"
- **Découverte** : Panorama V2 v3, §3.3 et §8.1

#### R-014 : Règle absolue des sandboxes

- **Portée** : Twin
- **Statut** : Actif (absolue)
- **Why** : Les sandboxes servent à explorer et pré-consolider sans figer le graphe officiel. Y introduire des relations réelles transformerait la sandbox en BDD parallèle semi-officielle.
- **How to apply** : Une BDD sandbox n'a **jamais** de relations réelles avec les autres BDD du Twin, **à une seule exception** : la relation vers `Sources d'informations`. Les liens se matérialisent uniquement via jumelles textes.
- **Exemples** : ✅ Sandbox Pratiques → jumelle texte "est conduite par (collectifs) (texte)" / ❌ Sandbox Pratiques → relation réelle vers Collectifs
- **Découverte** : Panorama V2 v3, §3.4

#### R-015 : Jumelles textes systématiques

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Préserver la formulation observée dans les sources, permettre la consolidation progressive, garder un indice relationnel avant validation, servir de base de vérification pour humain ou agent.
- **How to apply** : Pour chaque relation réelle dans une BDD officielle, prévoir une **jumelle texte** qui conserve les formulations observées. Exemple : `est conduite par (collectifs) (texte)` accompagne `est conduite par (collectifs)`. Dans une sandbox, **seule la jumelle texte** existe.
- **Découverte** : Panorama V2 v3, §8.2

### 3.4 5D, rollups et formules

#### R-016 : La 5D est une matrice de lecture, jamais une preuve primaire

- **Portée** : Twin
- **Statut** : Actif
- **Why** : La 5D sert à rendre visibles des structures, comparer des objets hétérogènes, synthétiser des traversées. Elle ne remplace pas la preuve, qui reste portée par objets, relations, propriétés spécifiques, sources, indices.
- **How to apply** : Utiliser la 5D pour : contribution, exposition, dépendance, causalité/impact/risque, pilotage/mesure. Ne jamais l'utiliser pour reclassifier les objets ou fonder un diagnostic.
- **Découverte** : Panorama V2 v3, §3.5 et §8.5

#### R-017 : Sobriété des rollups et formules

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Les couches calculées ne sont pas là pour "faire riche". Elles doivent révéler un écart, un profil, une dépendance, une vulnérabilité, ou un état utile à la lecture.
- **How to apply** : Un rollup ou une formule n'est conservé que s'il améliore réellement l'intelligibilité. Jamais de formule décorative. Pas de rollup dans une sandbox sans relations réelles.
- **Exemples** : ✅ Formule `Vulnérabilité nette de l'actif`, rollup `Profils 5D agrégés d'exposition` / ❌ Formule "nombre total de relations"
- **Découverte** : Panorama V2 v3, §3.6, §8.6, §8.7

### 3.5 Traçabilité et gouvernance

#### R-020 : Traçabilité obligatoire des fiches importantes

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Un diagnostic ou une lecture doit toujours pouvoir être relu, questionné, justifié, recontextualisé.
- **How to apply** : Toute fiche importante doit rester **réauditable** via :
  - Sources (relation vers `Sources d'informations`)
  - Indices observés (journal structuré)
  - Indices d'existence de l'objet
  - Logs / Révisions LBP
  - Traces de merge si applicable
- **Découverte** : Panorama V2 v3, §13.2

#### R-023 : Progressivité du remplissage

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Le Twin n'est pas conçu pour être "plein" immédiatement mais densifié progressivement à mesure que la preuve augmente. Imposer une complétude uniforme génère du remplissage artificiel.
- **How to apply** : Toutes les BDD n'ont pas besoin du même niveau de densité au même moment. Ce qui compte : la qualité de ce qui est utile pour la question analytique du moment.
- **Découverte** : Panorama V2 v3, §13.5

#### R-025 : Tableau maître canonique obligatoirement tenu à jour

- **Portée** : Twin
- **Statut** : Actif (absolue)
- **Why** : Le tableau maître est la référence canonique du Twin. Sans lui, l'architecture dérive.
- **How to apply** :
  - Toute création de BDD doit être ajoutée au tableau maître
  - Toute suppression doit y être arbitrée
  - Tout changement de régime architectural doit y être explicité
  - Toute sandbox doit être distinguée de sa BDD officielle cible
- **Découverte** : Panorama V2 v3, §4.3. Tableau maître reproduit dans `refs/SPECS_ARCHITECTURE_TWIN.md`.

### 3.6 Lecture et traversées

#### R-024 : Lecture du Twin sur 3 niveaux simultanés

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Le Twin n'est pas un entrepôt mais une machine de lecture systémique. Séparer les 3 niveaux évite les lectures faussement sûres.
- **How to apply** : Toute traversée/analyse doit articuler :
  1. **Niveau 1 — ce qui existe** : objets, acteurs, supports, contextes, temps
  2. **Niveau 2 — ce qui se passe** : actions, pratiques, processus, signaux, enjeux, transformations
  3. **Niveau 3 — ce que cela signifie et ce qu'il faut en faire** : problématiques, capacités, principes, modulateurs, OKR, indicateurs
- **Découverte** : Panorama V2 v3, §14.3

---

## 4. Règles Mission Ops

*Règles spécifiques à la gouvernance de Mission Ops.*

### 4.1 Instanciation

*Section à remplir.*

### 4.2 Relations Twin ↔ Mission Ops

*Section à remplir — notamment la règle de monodirectionnalité Mission Ops → Twin sans miroir.*

---

## 5. Règles de propagation d'impacts

*Règles qui décrivent comment propager un changement à travers l'écosystème.*

### 5.1 Renommage d'un objet

*Section à remplir quand on traitera ressources→actifs, rôles officiels→postes, etc.*

### 5.2 Suppression / archivage d'une BDD

*Section à remplir quand on traitera l'archivage de l'ancienne UO.*

### 5.3 Modification d'une taxonomie

*Section à remplir.*

### 5.4 Mise à jour d'un template

*Section à remplir.*

### 5.5 Mise à jour d'un manuel de BDD

#### R-028 : Cohérence manuel ↔ doc clefs de lecture

- **Portée** : Brain (propagation vers docs dérivés)
- **Statut** : Actif
- **Why** : Le doc *Instructions d'écriture & clefs de lecture* d'une BDD est **dérivé** du manuel de BDD correspondant. Une asymétrie entre les deux produit des agents qui écrivent/lisent différemment de la spec, et des incohérences dans le Twin.
- **How to apply** : Le **manuel de BDD est source de vérité**. À chaque mise à jour d'un manuel :
  1. Identifier le doc clefs de lecture correspondant dans `Architecture data/Clefs de lectures/TWIN - Instructions écriture + clefs de lecture/`
  2. Vérifier la cohérence (champs, instructions d'écriture, clefs de lecture, taxonomies référencées)
  3. Mettre à jour le doc dérivé si asymétrie
  4. Consigner la MAJ dans les logs du doc dérivé
- **Exemples** : ✅ On renomme le champ "Rôles officiels" en "Postes" dans le manuel → on met à jour `écriture + lecture - Rôles officiels.md` (ou on le renomme/recrée en `Postes`) / ❌ On modifie un manuel sans vérifier le doc dérivé
- **Découverte** : 2026-04-24, confirmé par Leonard

### 5.6 Consolidation et promotion (sandbox → officielle)

#### R-021 : Distinction stricte fusionner / consolider / promouvoir

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Ces trois opérations sont fondamentalement différentes. Les confondre produit des décisions mal arbitrées et des graphes incohérents.
- **How to apply** : Distinguer systématiquement :
  - **Fusionner** : plusieurs fiches désignent réellement le même objet → merge (au sein d'une même BDD)
  - **Consolider** : plusieurs entrées amont convergent vers un objet plus structuré (signaux → enjeu, enjeux → problématique, actions → processus candidat, actions → pratique)
  - **Promouvoir** : une entrée sandbox devient une BDD officielle
- **Exemples** : ✅ "Fusion" dans Merge Notes d'une BDD ; "Consolidation" dans le passage Journal des signaux → Enjeux / ❌ Parler de "fusion" pour une promotion sandbox
- **Découverte** : Panorama V2 v3, §13.3

#### R-022 : Critères minimaux de promotion sandbox → BDD officielle

- **Portée** : Twin
- **Statut** : Actif
- **Why** : Éviter les promotions trop précoces qui polluent le graphe officiel.
- **How to apply** : Une promotion est autorisée uniquement si tous les critères suivants sont remplis :
  1. **Preuves suffisantes** (indices observés + indices d'existence)
  2. **Formulation stabilisée**
  3. **Absence de confusion majeure** avec un objet déjà existant
  4. **Valeur analytique nette** attendue après promotion
  5. **Cohérence avec la frontière conceptuelle** de la BDD cible
- **Découverte** : Panorama V2 v3, §13.4

---

## 6. À classer (inbox)

*Zone tampon pour les règles qui émergent mais dont la section définitive n'est pas encore évidente. À reclasser régulièrement.*

*(vide pour l'instant)*

---

## Annexe : règles archivées

*Règles qui ne sont plus actives, conservées pour traçabilité.*

*(vide pour l'instant)*
