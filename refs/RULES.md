# Regles de gestion de l'ecosysteme LBP

> Ce fichier recense les regles decouvertes et formalisees au fil du travail.
> Chaque regle a un ID stable pour reference.
> Derniere mise a jour : 2026-04-07

---

## R-001 : Source de verite = doc Markdown

Le document Markdown (Drive / Obsidian) est la source de verite. Les proprietes Notion sont toujours derivees du contenu du doc, jamais l'inverse.

**Consequence** : pour modifier un objet Brain, on modifie d'abord le doc MD, puis on met a jour Notion.

## R-002 : Zero donnee client dans Core / Motor

Les domaines Core et Motor Brain ne contiennent jamais de donnees client. Seuls le Digital Twin et Mission Ops sont instancies par mission/client.

## R-003 : Confirmation humaine obligatoire

Aucune modification (creation, edition, suppression, renommage) sur le vault Obsidian ou sur Notion sans confirmation explicite de l'utilisateur.

## R-004 : Template obligatoire pour tout nouveau doc Brain

Tout document Brain est genere a partir d'un template (indexes dans Docs meta LBP). Le cycle est : Template → instanciation → cleanup → validation → indexation Notion.

## R-005 : Code unique stable

Le code unique d'un objet Brain ne change jamais, meme si le nom canonique evolue. Il sert de reference stable dans tout l'ecosysteme.

## R-006 : Descriptions Notion ≤280 caracteres

Les descriptions de proprietes dans Notion commencent par un verbe a l'infinitif, restent en texte brut, et ne depassent pas 280 caracteres. Elles sont copiees directement depuis le manuel de BDD.

## R-007 : Taxonomies par codes

Les BDD stockent des libelles humains. Les codes taxonomiques (ex: OBJ.STATUT.LBP) apparaissent uniquement dans les descriptions ≤280 et dans la documentation. Pas de codes dans le corps des textes.

## R-008 : Statuts harmonises

Toutes les BDD Brain utilisent la meme taxonomie de statut : `Brouillon`, `Valide`, `A revoir`, `Archive` (OBJ.STATUT.LBP).

## R-009 : Vault unique = Architecture data

On ne travaille que sur le vault Obsidian "Architecture data". Les autres vaults ne sont pas dans le perimetre.

## R-010 : Git comme filet de securite

Chaque modification significative du vault ou des refs doit etre suivie d'un commit git. Le message de commit resume le changement et son motif.

---

*Regles a decouvrir : workflows de mise a jour, regles de propagation d'impacts, conventions de nommage des fichiers, regles de deduplication, etc.*
