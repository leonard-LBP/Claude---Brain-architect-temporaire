# Backlog des règles à formaliser

> Zone tampon pour les règles pressenties ou mentionnées en passant, qui ne sont pas encore prêtes à être formalisées dans `RULES.md`.
> Quand une règle du backlog est mûre, on la sort d'ici et on l'insère dans `RULES.md` avec un ID stable `R-XXX`.
> Dernière mise à jour : 2026-04-25

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

- [2026-04-25] **Logique unifiée des codes uniques pour tous les docs Brain / Motor**
  - **Contexte** : émerge des batchs A1-C de la Phase 5. On a aujourd'hui un patchwork de formats : taxonomies en `XXX.YYY.LBP` (3 segments points), notes de concept en `CPT.CAT.LBP.NOM` (4 segments points), quelques codes Notion historiques en `CPT_TOKEN_TOKEN` (underscores) ou `CPT-TOKEN` (tirets, format recommandé dans la description Notion mais peu appliqué). Manuels de BDD : `DBMAN_NOM`. Plus l'écosystème grossit, plus ce mélange devient illisible et coûteux à maintenir.
  - **Portée potentielle** : Transverse Brain (toutes les BDD : taxonomies, notes concept, glossaire, manuels, méthodes, agents, prompts, logic blocks, templates, sources, outils, etc.).
  - **Objectif** : définir une grammaire unique et lisible des codes — préfixe par type d'objet, séparateur stable, segments hiérarchiques (catégorie/domaine/leaf), règles de longueur/casse, règles d'évolution si renommage.
  - **Bloquant à lever avant formalisation** :
    - Recensement complet des formats existants par BDD (audit)
    - Décider si on harmonise rétroactivement (renommage massif des codes existants — risque sur R-005 stabilité) ou si on fixe la règle pour les nouveaux codes seulement
    - Articulation avec R-005 (code stable), R-036 (code = pivot taxos), R-038 (nom = pivot autres BDD)
    - Cohabitation avec codes externes éventuels (DBMAN_, etc.)
  - **Quand** : pas tout de suite — à programmer après Phases 6 et 7, ou en parallèle d'une refonte des taxonomies code/libellé.

---

## Règles sorties du backlog (historique)

*Quand une règle est formalisée dans RULES.md, on la déplace ici avec une note rapide, pour tracer le cycle.*

*(vide pour l'instant)*
