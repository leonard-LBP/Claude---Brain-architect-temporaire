#!/usr/bin/env python3
"""Refonte v3 des champs summary et purpose des 11 manuels Brain selon R-060 v3.

Mêmes principes que refonte_taxos_v3 :
- summary = phrase nominale autonome, sans citation d'objet voisin, sans énumération
  des familles, sans duplication frontmatter, ≤400 char
- purpose = verbe à l'infinitif + effet structurel direct, sans jargon backend
  (Notion, hub, miroir...), sans citation d'autres BDD, ≤400 char
"""

import re
from pathlib import Path

DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain")

MAPPING = {
    "Manuel de BDD - Manuels de BDD.md": (
        "Catalogue transverse des manuels de bases de connaissances de l’écosystème LBP, recensant pour chacun la base décrite, le document source et les métadonnées de gouvernance.",
        "Indexer les manuels de bases de connaissances de l’écosystème, pour rendre lisible la couverture documentaire et soutenir audit de cohérence, retrieval ciblé et propagation des évolutions de schéma.",
    ),
    "Manuel de BDD - Glossaire LBP.md": (
        "Lexique canonique des concepts, référentiels externes et produits-marques mobilisés dans l’écosystème LBP, présentant pour chaque terme une vue opératoire (définition courte, équivalent en langage courant, règles d’usage et pièges).",
        "Tenir le vocabulaire commun de l’écosystème LBP, pour harmoniser le langage entre productions et faciliter la désambiguïsation à la lecture comme au retrieval sémantique.",
    ),
    "Manuel de BDD - Registre des notes de concept.md": (
        "Registre pivot minimaliste des notes de concept canoniques de l’écosystème LBP, indexant chacune par son code stable, son statut de gouvernance et son document source.",
        "Indexer les notes de concept comme source de vérité d’un concept LBP, pour offrir un point d’autorité unique référencable depuis l’écosystème, sans dupliquer le contenu de la définition.",
    ),
    "Manuel de BDD - Registre des taxonomies.md": (
        "Inventaire des taxonomies de l’écosystème LBP, recensant pour chacune ses caractéristiques de structure (nature, niveaux, ouverture, sélection), son document source et les bases qui la consomment.",
        "Indexer le portefeuille de taxonomies LBP, pour offrir un point d’entrée unique vers les vocabulaires contrôlés et tracer leurs domaines d’usage à travers l’écosystème.",
    ),
    "Manuel de BDD - Registre des logic blocks.md": (
        "Registre des blocs de logique opérationnelle LBP, qualifiés par nature d’opération et cible d’application.",
        "Indexer les blocs de logique réutilisables, pour permettre une spécialisation locale des opérations sans duplication et rendre les natures d’opération comparables d’une cible à l’autre.",
    ),
    "Manuel de BDD - Prompts LBP.md": (
        "Hub orchestrateur du Brain LBP : référentiel gouverné des prompts, qualifiés par rôle architectural, type fonctionnel, statut de déploiement et environnements de la plateforme.",
        "Centraliser les prompts LBP comme point d’entrée unique de l’orchestration agentique, pour rendre lisibles leurs dépendances et tracer leurs statuts de déploiement de façon homogène.",
    ),
    "Manuel de BDD - Méthodes LBP.md": (
        "Référentiel des démarches internes réutilisables LBP, structurant le « comment faire » d’une démarche par ses entrées attendues, son déroulé, ses règles d’usage et ses sorties.",
        "Standardiser les démarches internes réutilisables, pour partager une lecture commune du « comment faire » entre missions et entre intervenants, sans imposer le format de rendu.",
    ),
    "Manuel de BDD - Templates de bricks.md": (
        "Référentiel des templates de bricks LBP définissant le format de sortie standardisé d’une brick de connaissance produite en mission.",
        "Normaliser les formats de sortie des bricks de connaissance, pour rendre les livrables intermédiaires et finaux comparables et fiabiliser leur production en mission.",
    ),
    "Manuel de BDD - Outils externes.md": (
        "Référentiel des outils logiciels et formats standards externes mobilisés par l’écosystème LBP pour produire ses outputs, distinguant pour chacun la nature, les entrées attendues, les sorties produites et le mode d’emploi.",
        "Inventorier les outils et formats externes mobilisés, pour rendre les outputs directement importables dans l’outil cible et adapter les rendus à leurs contraintes techniques sans tâtonnement.",
    ),
    "Manuel de BDD - Docs méta LBP.md": (
        "Référentiel transverse des doctrines, règles et garde-fous encadrant la production LBP, précisant pour chaque entrée les objets encadrés, le périmètre d’application et les déclencheurs d’usage.",
        "Tenir l’ancrage doctrinal de la production LBP, pour rendre les règles et conventions transverses lisibles, partagées et référencables au sein de l’écosystème.",
    ),
    "Manuel de BDD - Agents LBP.md": (
        "Référentiel des profils d’agents internes LBP, qualifiés par leur rôle dominant, leur périmètre, leurs exclusions, leurs garde-fous et leurs limites attendues.",
        "Tenir le casting d’agents internes LBP, pour rendre les rôles, périmètres et garde-fous comparables et faciliter le routage vers le bon agent dans l’écosystème.",
    ),
}


def replace_field(content, field, new_value):
    pat_block = re.compile(rf"^{field}: >[^\S\n]*\n((?:[ \t]+.*\n)+)", re.MULTILINE)
    pat_line = re.compile(rf'^{field}:[ \t]+.*$', re.MULTILINE)
    new_line = f'{field}: "{new_value}"'
    if pat_block.search(content):
        return pat_block.sub(new_line + "\n", content, count=1), True
    if pat_line.search(content):
        return pat_line.sub(new_line, content, count=1), True
    return content, False


def main():
    stats = []
    for fname, (sumv, purv) in MAPPING.items():
        p = DIR / fname
        if not p.exists():
            stats.append((fname, "MISSING"))
            continue
        if len(sumv) > 400:
            stats.append((fname, f"summary too long: {len(sumv)}"))
            continue
        if len(purv) > 400:
            stats.append((fname, f"purpose too long: {len(purv)}"))
            continue
        c = p.read_text(encoding="utf-8")
        c, sok = replace_field(c, "summary", sumv)
        c, pok = replace_field(c, "purpose", purv)
        if sok and pok:
            p.write_text(c, encoding="utf-8")
            stats.append((fname, f"OK (sum={len(sumv)}, pur={len(purv)})"))
        else:
            stats.append((fname, f"partial sum={sok} pur={pok}"))

    for n, s in stats:
        print(f"{n}: {s}")
    print()
    print(f"Total: {sum(1 for _, s in stats if s.startswith('OK'))}/{len(MAPPING)}")


if __name__ == "__main__":
    main()
