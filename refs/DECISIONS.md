# Décisions architecturales

> Ce fichier trace les choix structurants qui ne sont pas des règles à appliquer, mais des décisions qui contextualisent l'écosystème.
> Chaque décision a un ID stable (D-XXX) et documente le *pourquoi* du choix, pas juste le *quoi*.
> Utile pour comprendre l'histoire de l'architecture et retracer les raisonnements.
> Dernière mise à jour : 2026-04-24

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

*(à remplir — notamment : scission UO→Organisation+Collectif, renommage ressources→actifs, renommage rôles officiels→postes, création Initiative organisationnelle)*

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
