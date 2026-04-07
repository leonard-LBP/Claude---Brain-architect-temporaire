# Workflows documentes — Ecosysteme LBP

> Ce fichier recense les workflows formalises au fil du travail.
> Chaque workflow a un ID stable pour reference.
> Derniere mise a jour : 2026-04-07

---

## Index

| ID | Workflow | Statut |
|----|----------|--------|
| WF-001 | Creer un nouveau doc Brain | A formaliser |
| WF-002 | Mettre a jour un doc Brain existant | A formaliser |
| WF-003 | Indexer un doc dans Notion | A formaliser |
| WF-004 | Mettre a jour les proprietes Notion | A formaliser |
| WF-005 | Creer une nouvelle note de concept | A formaliser |
| WF-006 | Mettre a jour une note de concept | A formaliser |
| WF-007 | Creer/mettre a jour une taxonomie | A formaliser |
| WF-008 | Propagation d'impacts apres modification | A formaliser |
| WF-009 | Migration d'une BDD XXX | A formaliser |
| WF-010 | Demarrage de session Claude (re-contextualisation) | A formaliser |

---

## WF-010 : Demarrage de session Claude

**Statut** : Actif (premier workflow formalise)

### Etapes

1. CLAUDE.md est lu automatiquement
2. memory/ est lu automatiquement
3. Si reprise de travail en cours → lire `refs/ECOSYSTEM-STATE.md`
4. Si besoin de contexte architecture → lire `refs/ARCHITECTURE-DIGEST.md`
5. Si operation prevue → consulter `refs/RULES.md` et `refs/WORKFLOWS.md`
6. Initialiser TodoWrite si taches multiples

### Declencheur
Debut de chaque nouvelle conversation.

---

*Les autres workflows seront formalises au fur et a mesure qu'on les pratiquera.*
