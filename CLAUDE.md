# CLAUDE.md

## Regles absolues

- **Vault unique** : On ne travaille que sur le vault Obsidian **"Architecture data"**. Ne jamais toucher aux autres vaults.
- **Confirmation obligatoire** : Ne jamais effectuer de modification (creation, edition, suppression, renommage) sur le vault sans confirmation explicite de l'utilisateur. Toujours presenter le changement prevu et attendre la validation avant d'agir. Aucune exception.
- **Notion idem** : Meme regle pour les modifications Notion — toujours presenter et attendre validation.

## Conventions de travail

### Acces ecosysteme
- **Vault Obsidian** : `Architecture data` — accessible via Obsidian CLI (`Obsidian.exe`) et en lecture directe fichiers
- **Drive** : `H:\Drive partagés\LBP - shared\Architecture data\` (synchronise avec le vault)
- **Notion** : Page maitre Brain = `20be1a18653c8079aeb1e01047fddddd` — 11 BDD officielles (ignorer les BDD prefixees "XXX")
- **Repo git** : Ce dossier (`Claude - Brain architect temporaire`) — pour versionner le travail

### Documentation de reference
- `refs/ARCHITECTURE-DIGEST.md` — Synthese de l'architecture LBP (relire au debut de chaque conversation)
- `refs/RULES.md` — Regles de gestion de l'ecosysteme (consulter avant toute operation)
- `refs/WORKFLOWS.md` — Workflows documentes (suivre les etapes)
- `refs/ECOSYSTEM-STATE.md` — Etat courant (mettre a jour apres chaque changement)
- `SPECS_ARCHITECTURE_BRAIN.md` — Specs detaillees des 11 BDD Brain (schemas Notion)

### Habitudes de travail
- **TodoWrite** : Maintenir une liste de taches a jour pendant chaque session
- **Commits reguliers** : Suggerer un commit a chaque milestone (nouveau doc, mise a jour de regles, changement d'etat). Format : une ligne de resume + detail si necessaire + `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`
- **Memory** : Sauvegarder en memoire les decisions importantes, preferences utilisateur, et pointeurs de contexte
- **Relecture** : Avant de modifier un doc, toujours le lire d'abord. Avant de creer un doc, verifier qu'il n'existe pas deja.
- **Regles et workflows** : Quand on decouvre ou formalise une regle/workflow, la consigner immediatement dans refs/RULES.md ou refs/WORKFLOWS.md
