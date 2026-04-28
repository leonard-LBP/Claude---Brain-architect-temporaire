# Backlog des règles à formaliser

> Zone tampon pour les règles pressenties ou mentionnées en passant, qui ne sont pas encore prêtes à être formalisées dans `RULES.md`.
> Quand une règle du backlog est mûre, on la sort d'ici et on l'insère dans `RULES.md` avec un ID stable `R-XXX`.
> Dernière mise à jour : 28-04-2026 — ajout 4 entrées : Chantier P (Prompts/Logic Blocks/Agents), Chantier M (réactualisation docs méta), convention "Statut vide = à créer", patterns techniques DDL Notion (multi-select JSON-encoded, CREATED_TIME/LAST_EDITED_TIME, statements séquentiels en API séparés).

---

## Format d'une entrée

```markdown
- [YYYY-MM-DD] Description concise de la règle pressentie.
  - **Contexte** : ce qui l'a fait émerger
  - **Portée potentielle** : Brain / Twin / Mission Ops / Transverse
  - **Bloquant à lever avant formalisation** : ce qui reste flou
```

---

## Règles en attente

- [27-04-2026] **Doctrine "manuels et templates de BDD agnostiques du backend"**
  - **Contexte** : Lors de la revue du nouveau template Mission Ops v5.1.0, Leonard a explicitement demandé qu'**aucune mention de Notion (ou tout autre backend spécifique) ne figure dans les templates et manuels de BDD**. Notion est un outil transitoire, pas durable. Les manuels doivent rester vrais quel que soit le backend (Notion aujourd'hui, autre demain). Application immédiate : suppression des `Libellé Notion ou libellé canonique unique` → `Libellé canonique unique` dans les 4 manuels Mission Ops + audit `purpose` du nouveau template (lui-même déjà conforme).
  - **Portée potentielle** : Transverse Brain + Twin + Mission Ops (toute la couche manuels et templates).
  - **À formaliser comme R-XXX** : possible règle "manuels et templates restent agnostiques du backend ; les conventions de typage parlent en termes structurels (`Sélection`, `Multi-sélection`, `Texte long`, `Relation bidirectionnelle`, etc.) sans référencer un outil particulier".
  - **Bloquant à lever** : auditer les manuels Twin et le template Twin pour vérifier qu'aucune mention de Notion ne traîne ; si oui, propager le nettoyage.

- [27-04-2026] **Divergence Twin / Mission Ops sur frontmatter — décision à expliciter**
  - **Contexte** : Le template Twin v6.3.0 inclut `ui_family` (R-049), `officiality_regime`, `has_advanced_note` (R-050), `aliases` dans son frontmatter. Le template Mission Ops v5.1.0 ne les inclut pas (décision Leonard 27-04-2026 : pas de convergence sur ces champs).
  - **Portée potentielle** : Transverse Brain (cohérence des frontmatter entre couches Brain / Twin / Mission Ops).
  - **À formaliser** : soit documenter explicitement pourquoi ces champs ne s'appliquent pas à Mission Ops (ex. pas d'UI dédiée, pas de notion de sandbox/pivot pour Mission Ops, pas de note avancée séparée), soit les ajouter avec valeurs par défaut sobres si la pratique le justifie un jour.
  - **Quand** : lors d'une revue cross-couches Brain/Twin/Mission Ops, après stabilisation de Mission Ops.

- [27-04-2026] **Idées créatives reportées — enrichissements template Mission Ops**
  - **Contexte** : Lors de la revue du nouveau template Mission Ops v5.1.0, 3 enrichissements ont été pressentis mais reportés au backlog (décision Leonard : "pas pour l'instant") :
    1. **Doctrine `knowledge_regime`** documentée dans le template avec critères de choix entre les 3 valeurs canoniques (`preuve_source`, `qualification_structuree`, `pilotage_action`). Actuellement les 4 manuels Mission Ops utilisent les 3 valeurs sans doctrine partagée explicite côté template — les règles existent mais peuvent gagner en clarté pédagogique.
    2. **Checklist d'intégrité finale** dans le template (5-10 items GO/NO-GO avant génération de la BDD : frontmatter complet, sections 1-8 présentes, miroirs relationnels cohérents, etc.). Substitut léger à la "Section 9 Checklist QA" supprimée volontairement du template.
    3. **Régressions volontaires v5.0.0+** (suppressions de Vues / Workflows / Paramétrage backend / Gouvernance opérationnelle / Checklist QA) : la doctrine "manuel = spec stable" suppose que des **playbooks et prompts** prennent le relais opérationnel. À auditer : ces playbooks/prompts existent-ils déjà ou faut-il les créer ?
  - **Portée potentielle** : Mission Ops (template) + écosystème playbooks.
  - **Quand** : après usage en condition réelle des 4 premiers manuels Mission Ops + génération des BDDs (Phase 6.5+).

- [27-04-2026] **Bug `extract_manifest.py` (Phase 6.5) — props natives manquantes + SELECT sans taxo mal typés**
  - **Contexte** : lors de la phase 6.5 de génération du Twin Notion, 4 rollups orphelins ont émergé après la création des propriétés natives via DDL. Diagnostic : le manifest produit par `scripts/phase6.5/extract_manifest.py` (i) **omettait 2 propriétés natives** de la BDD Individus — `Compétences hard dominantes` et `Compétences soft dominantes` (typées `Texte long` dans le manuel mais avec une taxo SKILL.HARD.LBP / SKILL.SOFT.LBP qui implique en fait un `multi_select` Notion), et (ii) **typait `Type d'usage de l'indicateur` (BDD Indicateurs) en `unknown`** parce que la propriété est un `select` sans taxonomie globale rattachée. Conséquence : 4 rollups (2 sur Postes vers Individus, 1 sur OKR vers Indicateurs, 1 sur Principes organisationnels vers Indicateurs) ont échoué car ils pointaient sur des propriétés source inexistantes dans Notion. Fix manuel appliqué le 27-04-2026 (ajout des 3 props + retry des 4 rollups).
  - **Portée potentielle** : Transverse (script de génération + doctrine de typage Notion à partir des manuels).
  - **Deux problèmes distincts à formaliser** :
    1. **Bug script** : le script doit (a) reconnaître qu'une propriété typée `Texte long` mais associée à une taxonomie codée se traduit en `multi_select` (ou `select` selon cardinalité) côté Notion ; (b) ne pas marquer en `unknown` les `select` sans taxo globale — détecter ce cas explicitement et journaliser pour arbitrage humain.
    2. **Doctrine SELECT sans taxo globale** : que faire des propriétés select dont les options ne sont pas couvertes par une taxonomie LBP (ex. `Type d'usage de l'indicateur` avec `officiel/proxy/potentiel/KR/alerte`, `Statut relationnel` côté Relations inter-orgas) ? Trois options : (i) créer des micro-taxos LBP dédiées (formalisation forte), (ii) accepter des conventions locales mission-by-mission documentées dans le manuel uniquement, (iii) hybride — taxo LBP pour les propriétés stables transverses, conventions locales pour les propriétés contextuelles. Choix à arbitrer avant la prochaine génération massive.
  - **Bloquant à lever avant formalisation** :
    - Recenser toutes les propriétés `select` / `multi_select` actuellement dans les manuels Twin sans taxo globale rattachée
    - Décider de la doctrine (taxos LBP vs conventions locales vs hybride)
    - Mettre à jour `extract_manifest.py` pour gérer correctement les deux cas (taxo référencée → multi_select; pas de taxo → demander arbitrage ou utiliser convention locale)
    - Vérifier qu'aucun autre manuel Twin ne contient de prop similaire encore non détectée

- [25-04-2026] **Logique unifiée des codes uniques pour tous les docs Brain / Motor**
  - **Contexte** : émerge des batchs A1-C de la Phase 5. On a aujourd'hui un patchwork de formats : taxonomies en `XXX.YYY.LBP` (3 segments points), notes de concept en `CPT.CAT.LBP.NOM` (4 segments points), quelques codes Notion historiques en `CPT_TOKEN_TOKEN` (underscores) ou `CPT-TOKEN` (tirets, format recommandé dans la description Notion mais peu appliqué). Manuels de BDD : `DBMAN_NOM`. Plus l'écosystème grossit, plus ce mélange devient illisible et coûteux à maintenir.
  - **Portée potentielle** : Transverse Brain (toutes les BDD : taxonomies, notes concept, glossaire, manuels, méthodes, agents, prompts, logic blocks, templates, sources, outils, etc.).
  - **Objectif** : définir une grammaire unique et lisible des codes — préfixe par type d'objet, séparateur stable, segments hiérarchiques (catégorie/domaine/leaf), règles de longueur/casse, règles d'évolution si renommage.
  - **Bloquant à lever avant formalisation** :
    - Recensement complet des formats existants par BDD (audit)
    - Décider si on harmonise rétroactivement (renommage massif des codes existants — risque sur R-005 stabilité) ou si on fixe la règle pour les nouveaux codes seulement
    - Articulation avec R-005 (code stable), R-036 (code = pivot taxos), R-038 (nom = pivot autres BDD)
    - Cohabitation avec codes externes éventuels (DBMAN_, etc.)
  - **Quand** : pas tout de suite — à programmer après Phases 6 et 7, ou en parallèle d'une refonte des taxonomies code/libellé.

- [27-04-2026] **Articulation des propriétés select de la BDD Notion `Manuels de BDD` pour cohérence transverse Brain / Twin / Mission Ops**
  - **Contexte** : la BDD `Manuels de BDD` (Brain) regroupe les manuels de **toutes** les couches (Brain Core/Motor/Admin + Digital Twin + Mission Ops). Or on a tendance à ajouter des propriétés select **spécifiques à un domaine** (ex. `Type fonctionnel (BDD décrite)` qui contient surtout des valeurs Twin : `Digital Twin - socle structurel`, `Digital Twin - sandbox`, etc., et pour les manuels Brain seulement quelques valeurs génériques `Catalogue`, `Registre`, `Templates`). De nouvelles propriétés candidates de classification (ex. `Famille UI` issue de D-017, qui n'a de valeurs canoniques que pour le Twin) accentueraient ce déséquilibre.
  - **Portée potentielle** : Transverse Brain (refonte ou clarification du schéma de la BDD `Manuels de BDD` Notion).
  - **Symptômes actuels** :
    - Propriétés select avec couverture partielle selon le domaine de chaque fiche.
    - Valeurs n/a ou laissées vides pour les manuels qui ne relèvent pas du domaine couvert par la propriété.
    - Risque de divergence entre propriétés "transverses" (s'appliquant à toutes les fiches) et propriétés "domain-specific" (Twin uniquement, Mission Ops uniquement, etc.).
  - **Pistes à examiner** :
    1. Soit créer **une propriété par domaine** (ex. `Type fonctionnel - Twin`, `Type fonctionnel - Brain`, `Type fonctionnel - Mission Ops`) et masquer celles qui ne s'appliquent pas via vues filtrées.
    2. Soit créer **une propriété "Domaine"** (déjà existante via `Domaine(s) d'usage`) et utiliser des **vues conditionnelles** par domaine pour piloter les colonnes affichées.
    3. Soit fusionner toutes les valeurs (Brain + Twin + Mission Ops) dans une seule propriété englobante (risque : explosion d'options, illisibilité).
  - **Pré-requis** : avoir d'abord **revu et structuré les manuels Brain et Mission Ops** (à ce jour seul le Twin a été refondu Twin v2). On ne peut pas trancher la doctrine d'articulation sans connaître les besoins de classification des autres domaines.
  - **Quand** : après refonte des manuels Brain et Mission Ops. À ce moment-là, traiter d'un coup : `Type fonctionnel`, `Famille UI` (D-017), et toute autre propriété select candidate.
  - **Lien** : D-017 (familles UI/UX), R-049 (déclaration `ui_family`), Phase 6.5 actuelle (les frontmatters Twin reçoivent `ui_family` mais la propagation Notion attend cette réflexion).

- [27-04-2026] **Nettoyage des libellés d'options taxonomiques pour compatibilité Notion DDL**
  - **Contexte** : la Phase 6.5 (création des 28 BDD Twin sur Notion via `update_data_source`) a révélé que **certains libellés d'options multi_select** dans les manuels de BDD Twin v2 contiennent des **virgules** (ex. `'SI, données & outillage'`, `'Risques, conformité & sécurité'`) ou des **apostrophes droites devant être échappées** (`d\'interface`). Ces libellés sont rejetés ou mal parsés par le DDL Notion (les virgules ferment les options ; les apostrophes échappées ne passent pas le parseur).
  - **Symptômes** : DDL bloqué, sub-agent qui a corrigé manuellement en remplaçant `,` → ` -` et `\'` → apostrophe typographique `'`. Concernées : `OKR`, `OKR sandbox`, `Problématiques`, `Problématiques sandbox`, `Pratiques organisationnelles`, `Pratiques organisationnelles sandbox`. Cf. `ECOSYSTEM-STATE.md` pour la liste exacte.
  - **Portée potentielle** : Transverse Twin (toutes les taxos référencées par les manuels Twin et utilisées comme select/multi_select sur Notion).
  - **Pistes** :
    1. Audit des taxos pour identifier toutes les options contenant `,` ou `'` droite. Renommer les options dans les `.md` de taxos + propager dans les manuels Twin + WR-RD (R-041 / R-042).
    2. Améliorer le script `build_phase3_ddl.py` pour échapper correctement les virgules (impossible côté DDL Notion) et les apostrophes (utiliser apostrophe typographique systématiquement).
    3. Décider d'une convention : pas de `,` dans les libellés d'options taxonomiques ; préférer ` - ` ou ` / `.
  - **Quand** : à traiter avant la prochaine génération massive de BDD ou avant tout export du bundle taxos vers d'autres outils.

- [27-04-2026] **Taxonomie `Statut relationnel` (Relations inter-organisations) à formaliser**
  - **Contexte** : la propriété `Statut relationnel` du manuel `Relations inter-organisations` est typée `Sélection` mais **aucune taxonomie n'est référencée** (le manifest a extrait `SELECT()` vide). En Phase 6.5 (création BDD Notion), cette propriété a été dégradée en `RICH_TEXT` provisoirement.
  - **Portée potentielle** : Twin (BDD Relations inter-organisations).
  - **Action requise** : définir la taxonomie `ORG_REL.STATUT.LBP` (ou équivalent) avec les valeurs canoniques (ex. `actif`, `en cours d'évaluation`, `interrompu`, `terminé`, etc.), créer le `.md` taxonomie, mettre à jour le manuel + WR-RD, puis re-typer la propriété Notion en SELECT.

- [27-04-2026] **Filtrer les nœuds `category` lors de la génération des options select Notion**
  - **Contexte** : la Phase 6.5 a révélé que `build_phase3_ddl.py` (et possiblement les scripts amont d'extraction) **aplatit la hiérarchie taxonomique** (`category` + `taxon`) en options Notion `SELECT/MULTI_SELECT`. Or les `category` sont des **familles parentes** non destinées à être sélectionnables comme valeur de fiche — seuls les `taxon` doivent l'être.
  - **Symptôme observé** : doublon `Autre` (category `ENJ.EXPRESSION.LBP.VALENCE_AUTRE`) vs `Autre type d'expression` (taxon `ENJ.EXPRESSION.LBP.AUTRE`) dans la BDD `Enjeux`. Corrigé manuellement par DROP de l'option `Autre` côté Notion.
  - **Portée potentielle** : Transverse Twin (toutes les BDD utilisant des taxos hiérarchiques category+taxon comme select/multi_select). Anomalie probablement isolée pour l'instant (audit des 28 BDD n'en a relevé qu'une), mais le script génère structurellement le risque.
  - **Action requise** :
    1. Auditer toutes les taxos pour identifier celles avec mélange `category` + `taxon`.
    2. Vérifier dans Notion si d'autres BDD ont des category leakées comme options.
    3. Mettre à jour `build_phase3_ddl.py` pour filtrer `Type de nœud == taxon` lors de la génération des options.
    4. Optionnel : ajouter une vérification au pre-commit / WR-RD pour signaler ce cas.
  - **Quand** : avant la prochaine génération massive de BDD ou lors d'un refactor du script DDL.

- [27-04-2026] **Doctrine `Indices observés` / `Indices d'existence de l'objet` réservés aux BDDs d'objets, pas aux containers d'indices**
  - **Contexte** : Leonard a retiré `Indices observés` et `Indices d'existence de l'objet` de la BDD `Sources d'informations` (Mission Ops) en faisant remarquer que les sources sont **les contenants** des indices, pas les objets que les indices décrivent. Demander des indices d'existence sur une fiche Source est circulaire (la source est sa propre preuve via `Lien vers document original`, `Nom du fichier original`, etc.). Ces 2 props ont sens pour les objets Twin (Actifs, Capacités, Enjeux, Problématiques…) où elles documentent comment on sait que l'objet existe et ce qu'on a observé à son sujet — mais pas pour Sources d'informations qui est elle-même la preuve.
  - **Portée potentielle** : pour l'instant identifié uniquement sur **Sources d'informations** (Mission Ops). À surveiller si la même logique s'applique à d'autres BDDs containers d'indices (ex. `Journal des signaux` Twin ? — à vérifier ; possiblement non car le Journal est consommateur des sources, pas un container natif).
  - **Décision Leonard (27-04-2026)** : ne **pas** capturer en règle R-XXX formelle pour l'instant, le cas ne concerne que Sources d'informations. Garder en backlog au cas où le pattern se généraliserait.
  - **Action immédiate effectuée** : suppression des 2 props sur Notion + propagation manuel + WR-RD (sections 4.1, 8.1, 8.2 + invariants 7.3 + références dans `Notes du consultant`). Doctrine émergente : *"Une BDD container d'indices/preuves n'a pas besoin de logguer ses propres indices d'existence."*

- [28-04-2026] **Self-relation Notion DDL : un seul `ADD COLUMN ... RELATION(self_ds, DUAL ...)` suffit (et NON deux croisés)**
  - **Contexte** : pendant Pass 2.3 Mission Ops (génération self-rel `appartient à (activité)` ↔ `contient (actions)` côté Actions LBP, et `est dérivée de` ↔ `a pour dérivés` côté Sources d'informations), le pattern initial du prompt était `2 ADD COLUMN avec DUAL croisés` (un par sens). Résultat : **4 colonnes créées au lieu de 2** car chaque ADD avec DUAL crée la prop ET son miroir auto.
  - **Règle empirique pressentie** : pour une self-relation Notion via DDL, **un seul `ADD COLUMN "PropA" RELATION(self_ds_id, DUAL 'PropMiroir' 'prop_miroir_internal')` suffit** — Notion auto-crée la prop miroir interne. Le pattern `2 ADD croisés` est faux pour ce moteur.
  - **À formaliser** : R-XXX dans `RULES_BRAIN_TWIN.md` section DDL Notion / phase 6.5 ou WF-014 (workflow de génération BDD) si confirmé sur d'autres self-rel. Documenter aussi dans le prompt-cadre de génération.
  - **Action effectuée** : pattern correctif appliqué (DROP des 4 colonnes parasites côté Actions LBP et côté Sources, recréation propre).

- [28-04-2026] **Convention v1.1 pour les futurs templates d'instanciation (pattern d'organisation des INSTR)**
  - **Contexte** : audit interne sur l'organisation des blocs `<!-- @INSTR-START: ... @INSTR-END -->` dans les templates Phase 1 a révélé deux patterns possibles :
    - **Pattern v1.0** (templates existants Phase 1) : multi-blocs INSTR successifs au début (SETTINGS, FRONTMATTER_INSTANCE, FRONTMATTER_CONTROLLED_VOCAB, FRONTMATTER_DECISION_RULES, FRONTMATTER_EXAMPLES, GLOBAL_DOCTRINE, WRITING_AND_READING_DOCTRINE, parfois COLUMN_DEFINITIONS, EXAMPLE_ROWS, etc.) puis `SECTION_X_GUIDE` avant chaque section H1. Pattern qui fonctionne et est éprouvé.
    - **Pattern v1.1** (Template Brain v1.1) : un seul bloc macro consolidé `<!-- @INSTR-START: TEMPLATE_USAGE_GUIDE -->` en tête (avec doctrine globale + vocabulaires contrôlés + frontmatter B + exemples + purge finale en sous-sections numérotées), puis `SECTION_X_GUIDE` court par section + tableaux **Modèle types de champs** + **Exemple simulé** dans des blocs INSTR pour les sections structurantes (§3.2 / §4 / §5).
  - **Décision Leonard (28-04-2026)** : adoption du pattern v1.1 **uniquement pour les futurs templates créés**. Les 5 templates Phase 1 existants (Manuel Twin v7.0, Manuel MO v6.0, WR-RD Twin v2.0, WR-RD MO v2.0, Note de concept v2.0, Taxonomie v2.0) sont **conservés en pattern v1.0** car ils fonctionnent et la refonte aurait un coût (~3-3h30) pour un gain marginal. Migration vers pattern v1.1 uniquement à l'occasion d'une refonte structurelle naturelle d'un de ces templates.
  - **Justification** :
    - Les LLM modernes (Claude Opus 4 = 1M tokens) ne perdent pas leurs instructions à 1000 lignes. La fragmentation des INSTR est plus théorique que pratique.
    - Les WR-RD sont des copies strictes du manuel parent (R-041/R-042) → pas besoin d'instructions élaborées dans leur template, c'est au manuel d'être rigoureux.
    - Les manuels existants servent eux-mêmes d'exemples vivants → moins besoin de mettre des exemples dans les templates.
    - Pragmatisme > perfection : ne pas refondre ce qui fonctionne pour aligner formellement.
  - **Convention pour les futurs templates** : pattern v1.1 = `TEMPLATE_USAGE_GUIDE` consolidé en tête + `SECTION_X_GUIDE` par section + tableaux **Modèle**/**Exemple simulé** dans les sections structurantes. Référence : `Template - Manuel de BDD - Brain.md` v1.1.
  - **Statut** : convention adoptée (pas formalisée comme R-XXX dure car c'est un guideline d'évolution, pas une contrainte). Si un futur template ne suit pas ce pattern, ce n'est pas une violation — juste une non-conformité à la convention recommandée.

---

- [28-04-2026] **Chantier P — Tri massif Prompts / Logic Blocks / Agents avant indexation Notion**
  - **Contexte** : Les dossiers `Prompts/` et `Logic Blocks/` du vault contiennent un mix non trié : (a) anciens system prompts / prompts maîtres / logic blocks que Leonard avait produits, (b) extraits du code de l'app LBP (prompts/chartes dispersés que l'agent dev a extraits en .md pour visibilité), (c) nouveaux docs de travail (system prompts / prompts maîtres / logic blocks destinés à Brain architect / Twin architect / KONTEXT). La BDD `Agents LBP` est vide (aucune fiche encore) et doit recevoir les 3 fiches agents (D-021).
  - **Portée** : Brain — BDDs `Prompts LBP`, `Registre des logic blocks`, `Agents LBP` (out of scope indexation court terme).
  - **Action requise** :
    1. Tri des dossiers `Prompts/` et `Logic Blocks/` : séparer (a) « image à un instant t » des prompts répartis dans le code app (à conserver comme référence ou archiver) (b) docs de travail nouveaux (à mettre au canon).
    2. Mise à jour des system prompts / prompts maîtres / logic blocks pour cohérence avec Twin v2, D-019 (Brain unifié), D-021 (3 agents).
    3. Création des 3 fiches `Agents LBP` (Brain architect, Twin architect, KONTEXT).
    4. Indexation Notion BDDs Prompts + Logic blocks + Agents.
  - **Quand** : après finalisation des autres BDDs Brain indexées.

- [28-04-2026] **Chantier M — Réactualisation des docs méta hors templates + réflexion bundle**
  - **Contexte** : (a) `PLAYBOOK — Macro-architecture v2` (dans `Architecture data > 00 - docs méta > doctrines & playbooks`, code `CHRT_PLAYBOOK_MACRO_ARCHI_LBP`, doc_type `DOC_META`) doit être réactualisé après les changements récents (Phases 4-7, R-053→R-059, D-019, D-020, D-021, sync Notion Brain, refonte 4 templates secondaires…). Il était à jour au 27-04-2026 mais beaucoup de doctrines ont évolué depuis. (b) La BDD Notion `Docs méta LBP` contient plusieurs entités indexées sans équivalent Markdown actuel dans `Architecture data` (ex : Bible des objets, etc.) — désuets et à réactualiser considérablement.
  - **Réflexion architecture bundle docs méta (Leonard 28-04-2026)** : plutôt que mettre à jour les bibles/doctrines/playbooks obsolètes existants, **produire un bundle de docs méta dédiés à chaque ensemble de doctrines/règles/chartes** avec un **périmètre bien défini par doc** (maintenable, améliorable). Objectif : architecture de la connaissance durable, facile à faire évoluer de façon cohérente à mesure que l'écosystème grandit.
  - **Portée** : Brain — Docs méta LBP.
  - **Action requise** :
    1. **Réflexion en amont** : recenser les ensembles thématiques de doctrines/règles/chartes (ex : architecture macro, conventions de codification, cycle de vie des docs, doctrine d'isolation des agents, gouvernance documentaire, etc.). Définir le périmètre net de chaque doc méta du futur bundle.
    2. **Production du bundle** : un doc méta par périmètre, au canon (R-055/056), avec articulation explicite entre eux (sans recouvrement).
    3. **Tri des entrées Notion `Docs méta LBP`** : pour chaque entrée actuelle sans Markdown actif → soit refondre dans un doc du nouveau bundle, soit archiver.
    4. **Indexation Notion** BDD Docs méta LBP avec le nouveau bundle.
  - **Quand** : après finalisation Phase A (indexation Brain restant) et Phase B (tests fonctionnels Twin + Mission Ops).

- [28-04-2026] **Convention "Statut de l'objet vide = à créer"**
  - **Contexte** : Leonard utilise la BDD `Méthodes LBP` Notion comme to-do/mémo : il y crée des entrées avec juste un nom et même pas de `Statut de l'objet`. Convention d'induction : statut vide = "à créer" (pas même brouillon). Origine : 28-04-2026 (calibration indexation Méthodes LBP).
  - **Portée potentielle** : transverse Brain (à vérifier avec autres BDDs si même convention applicable).
  - **À formaliser** : règle R-XXX si la convention est confirmée transverse, ou note doctrinale si reste spécifique à Méthodes LBP. Bloquant à lever : audit transverse pour voir si d'autres BDDs Brain ont des entrées sans statut.

- [28-04-2026] **Propriété "Maître" — figement d'une entité avérée comme entité d'accueil en cas de dédoublonnage**
  - **Contexte** : Leonard cogite sur une propriété qui permettrait de **figer** une entité Twin avérée comme « entité maître ». Exemple : si un individu (Jean Dupont) est confirmé comme salarié de l'entreprise focale d'une mission (même si ses propriétés ne sont pas toutes remplies), il devient une entité maître qui ne peut être ni archivée ni diluée dans une autre entité ultérieure. Si un second « Jean Dupont » apparaît par extraction d'une autre source, les agents de dédoublonnage proposeront de **fusionner la nouvelle entité dans la maître** (et non l'inverse) ; la maître devient l'entité d'accueil des contenus de la nouvelle ; la nouvelle est archivée après fusion.
  - **Portée potentielle** : Twin (toutes BDDs avec entités identifiables — Individus, Postes, Organisations, Collectifs, Actifs, etc.). Possiblement Mission Ops (Bricks ?). Pas Brain (les entrées Brain sont déjà gouvernées par `Statut de l'objet` et codes uniques).
  - **Pistes à explorer** :
    1. **Type de propriété** : checkbox booléenne (`Est maître : oui/non`) ou statut spécifique dans une nouvelle taxo (`OBJ.MASTERY` avec valeurs `non maître`, `maître`, `maître figé verrouillé`).
    2. **Précondition** : entité doit être au statut `Validé` (`OBJ.STATUT.VALIDE`) avant de pouvoir devenir maître.
    3. **Comportement attendu côté agents** :
       - Dédoublonnage : si conflit entre entité maître et entité non-maître → agent fusionne la non-maître dans la maître.
       - Refactor : la maître ne peut être ni archivée ni renommée sans validation explicite humaine.
       - Refactor : la maître accueille les enrichissements de propriétés issus des entités fusionnées.
    4. **Articulation avec OBJ.STATUT** : maître ⊂ Validé ; maître peut redevenir non-maître par décision explicite (rare).
    5. **Gouvernance** : qui peut figer une entité comme maître ? consultant uniquement ? ou agent IA avec validation ?
  - **À cogiter** : la propriété est-elle vraiment nécessaire ou un statut + une convention suffisent-ils ? Préciser le besoin par cas d'usage avant formalisation.
  - **Quand** : à inclure dans la Phase B (tests fonctionnels Twin + Mission Ops) — si on simule des fausses entités et qu'on rencontre des cas de dédoublonnage, cette réflexion mûrira concrètement.

- [28-04-2026] **Patterns techniques DDL Notion (à documenter dans WF-XXX)**
  - **Contexte** : plusieurs patterns techniques découverts pendant la sync DDL Notion qui méritent d'être documentés pour réutilisation.
  - **Patterns à formaliser** :
    1. **Multi-select via `update_page`** : passer la valeur en **string JSON-encoded** (`"property": "[\"value1\", \"value2\"]"`), pas en array natif. Notion retourne un array natif au fetch.
    2. **Types `CREATED_TIME` / `LAST_EDITED_TIME` en DDL** : fonctionnent (testé 28-04-2026 sur 5 BDDs Motor) bien que non documentés dans la liste des types simples de l'aide DDL Notion. Permettent de convertir une prop `date` (saisie manuelle) en prop système auto-remplie.
    3. **Statements multiples dans une même salve `update_data_source`** : ne s'exécutent **pas séquentiellement** quand un statement dépend du résultat du précédent (ex : `RENAME A→B; RENAME B→C` → 2e échoue car B n'existe pas en début de salve). Faire 2 calls API distincts pour les chaînes de dépendances.
  - **Portée** : Transverse — script de génération/sync Notion.
  - **À formaliser** : documenter dans `WORKFLOWS_LBP.md` WF-XXX (à enrichir WF-017 ou créer un WF-018 dédié aux patterns DDL Notion).

---

## Règles sorties du backlog (historique)

*Quand une règle est formalisée dans RULES.md, on la déplace ici avec une note rapide, pour tracer le cycle.*

- **[27-04-2026 → résolue 27-04-2026]** WR-RD Mission Ops à générer : ✅ Template `Template - WR-RD - Mission Ops.md` v1.0.0 créé + 4 WR-RD générés (Sources d'informations, Meetings, Actions LBP, Bricks). Doctrine agnostique backend respectée (0 mention Notion). Sortie du backlog avant même formalisation R-XXX (résolution rapide via délivrable concret).
