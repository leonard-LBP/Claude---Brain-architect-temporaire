# Backlog des règles à formaliser

> Zone tampon pour les règles pressenties ou mentionnées en passant, qui ne sont pas encore prêtes à être formalisées dans `RULES.md`.
> Quand une règle du backlog est mûre, on la sort d'ici et on l'insère dans `RULES.md` avec un ID stable `R-XXX`.
> Dernière mise à jour : 27-04-2026 — ajout entrée Phase 6.5 : filtrer `category` vs `taxon` dans génération options select.

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

---

## Règles sorties du backlog (historique)

*Quand une règle est formalisée dans RULES.md, on la déplace ici avec une note rapide, pour tracer le cycle.*

*(vide pour l'instant)*
