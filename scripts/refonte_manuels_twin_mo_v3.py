#!/usr/bin/env python3
"""Refonte v3 des champs summary et purpose des 32 manuels Twin + Mission Ops.

Constat avant refonte (audit 29-04-2026) :
- 32/32 ont summary vide.
- 32/32 ont un purpose boilerplate « Spécifier la BDD X du Digital Twin LBP / de
  Mission Ops LBP : périmètre, rôle systémique, modèle de données, ... » qui
  décrit le manuel et non la fonction de la BDD elle-même.

Refonte v3 :
- summary = phrase nominale autonome qui décrit l'objet de la BDD
  (Référentiel / Sandbox / Journal / Lexique / Pivot / Backlog / Index / Registre).
- purpose = verbe à l'infinitif en tête + effet structurel direct sur l'écosystème
  observé, sans citation d'autre BDD par son nom, sans énumération de valeurs,
  sans jargon backend, ≤400 caractères.
"""

import re
from pathlib import Path

ROOT = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD")

MAPPING: dict[tuple[str, str], tuple[str, str]] = {
    # (folder, filename) → (summary, purpose)
    ("Digital Twin", "Manuel de BDD - Actifs.md"): (
        "Référentiel du patrimoine non humain qui structure le fonctionnement, la production, la coordination, l’apprentissage, la protection ou la transformation d’un système observé.",
        "Indexer les actifs non humains réellement mobilisés dans une organisation, pour rendre lisibles dépendances, fragilités et leviers de transformation associés à ces objets.",
    ),
    ("Digital Twin", "Manuel de BDD - Actions détectées.md"): (
        "Sas de qualification des actions observées dans les sources d’une mission, en attente de consolidation aval vers pratiques, processus candidats ou initiatives organisationnelles.",
        "Capturer et qualifier les actions effectivement observées en sources, pour préparer leur consolidation aval sans préjuger de la cible finale d’agrégation.",
    ),
    ("Digital Twin", "Manuel de BDD - Capacités métier candidates sandbox.md"): (
        "Sandbox des capacités métier pressenties d’une organisation observée, en attente d’arbitrage avant migration éventuelle vers la couche officielle des capacités organisationnelles.",
        "Qualifier, comparer et tester des capacités métier candidates avant arbitrage de migration vers la couche officielle, pour éviter le figement prématuré dans le portefeuille consolidé.",
    ),
    ("Digital Twin", "Manuel de BDD - Capacités organisationnelles.md"): (
        "Référentiel des aptitudes collectives durables d’une organisation, qualifiées par leur famille (habilitante, motrice, générique, métier) et leur nature soft/hard.",
        "Cartographier ce qu’une organisation sait réellement produire ou maintenir de façon répétable, pour relier pratiques, contextes, problèmes, pilotage et transformation à la dynamique de capacités.",
    ),
    ("Digital Twin", "Manuel de BDD - Collectifs.md"): (
        "Référentiel des groupes humains opérants, identifiables et relativement stables qui structurent le travail réel d’une organisation, distincts des organisations instituées et des initiatives qu’ils peuvent porter.",
        "Rendre visible la trame réelle du travail, de la coopération et de l’apprentissage dans une organisation, pour analyser la dynamique des groupes humains opérants au-delà de l’arbre formel.",
    ),
    ("Digital Twin", "Manuel de BDD - Enjeux.md"): (
        "Référentiel des besoins, irritants, opportunités, craintes et objectifs pressentis remontés du terrain, en attente de consolidation éventuelle vers problématiques ou objectifs.",
        "Capturer largement les sujets exprimés du terrain, pour constituer un sas de qualification entre signaux faibles et couches aval de diagnostic et de pilotage.",
    ),
    ("Digital Twin", "Manuel de BDD - Environnements.md"): (
        "Référentiel des cadres contextuels — physiques, virtuels, relationnels ou macro — qui structurent l’activité, les contraintes, les opportunités et les transformations d’un système observé.",
        "Rendre visibles les cadres dans lesquels une organisation opère, pour comprendre comment l’environnement influence ses conditions d’action, ses risques et ses leviers.",
    ),
    ("Digital Twin", "Manuel de BDD - Glossaire spécifique.md"): (
        "Lexique des termes, expressions, acronymes et formulations propres à une organisation cliente ou à son secteur d’activité.",
        "Stabiliser le sens du vocabulaire local d’une organisation observée, pour réduire les ambiguïtés et fiabiliser l’analyse comme l’intelligibilité des productions de mission.",
    ),
    ("Digital Twin", "Manuel de BDD - Indicateurs.md"): (
        "Référentiel des mesures structurées, définies et reproductibles qui objectivent performance, risques, résultats, santé organisationnelle et écarts d’un système observé.",
        "Indexer les mesures pertinentes d’une organisation observée, pour rendre lisibles et comparables les phénomènes pilotés indépendamment de leur source et de leur granularité.",
    ),
    ("Digital Twin", "Manuel de BDD - Individus.md"): (
        "Référentiel des personnes qui comptent dans un système étudié, qualifiées par leurs rattachements, leurs rôles, leurs contributions, leurs expositions et leurs compétences.",
        "Rendre visibles les personnes significatives d’un écosystème observé, pour relier le fonctionnement réel aux décisions de diagnostic, de pilotage et de transformation.",
    ),
    ("Digital Twin", "Manuel de BDD - Initiatives organisationnelles.md"): (
        "Référentiel des efforts intentionnels, temporaires et délimités portés au sein ou entre une ou plusieurs organisations, distincts du fonctionnement courant.",
        "Suivre les transformations structurées dans le temps d’une organisation observée, pour les distinguer des groupes humains qui les portent comme des pratiques ou processus récurrents qu’elles modifient.",
    ),
    ("Digital Twin", "Manuel de BDD - Journal des signaux.md"): (
        "Journal d’observation amont des signaux faibles, perceptions, motifs récurrents, contradictions, émotions et anomalies relevés en sources d’une mission.",
        "Tracer la matière qualitative d’observation précoce d’un système, pour préparer la consolidation aval en enjeux, événements ou objets analytiques plus stables.",
    ),
    ("Digital Twin", "Manuel de BDD - Modulateurs.md"): (
        "Référentiel des conditions contextuelles qui accélèrent, freinent ou plafonnent l’effectivité réelle des pratiques d’une organisation.",
        "Remonter aux leviers racine d’effectivité des pratiques, pour expliquer pourquoi des pratiques existent mais plafonnent malgré leur présence et orienter les plans d’action.",
    ),
    ("Digital Twin", "Manuel de BDD - OKR.md"): (
        "Référentiel des objectifs pilotés et de leurs résultats-clés mesurables d’une organisation observée.",
        "Rendre lisibles les engagements de pilotage d’une organisation, pour articuler diagnostic, mesure et exécution sur des cibles partagées.",
    ),
    ("Digital Twin", "Manuel de BDD - OKR sandbox.md"): (
        "Sandbox des objectifs pilotés pressentis d’une organisation observée, en attente d’arbitrage avant migration éventuelle vers la couche officielle des OKR.",
        "Qualifier, comparer et tester des OKR candidats avant arbitrage de migration vers la couche officielle, pour éviter le figement prématuré du portefeuille piloté.",
    ),
    ("Digital Twin", "Manuel de BDD - Organisations.md"): (
        "Référentiel des acteurs collectifs institués d’un écosystème observé, qualifiés par leur forme institutionnelle, leurs frontières, leurs responsabilités et leurs emboîtements.",
        "Cartographier les acteurs institués d’un écosystème, pour soutenir les analyses de structure, de relations et de gouvernance sans confondre acteurs reconnus et collectifs humains qui les composent.",
    ),
    ("Digital Twin", "Manuel de BDD - Postes.md"): (
        "Référentiel des positions formelles contextualisées d’une organisation, définies indépendamment des personnes qui les occupent.",
        "Lire la structure attendue d’une organisation, pour analyser couverture réelle, responsabilités, interfaces et besoins en compétences indépendamment des personnes en poste.",
    ),
    ("Digital Twin", "Manuel de BDD - Pratiques organisationnelles.md"): (
        "Référentiel des patterns opérants récurrents qui structurent durablement le fonctionnement réel d’une organisation observée.",
        "Décrire le « réel » de ce qui est effectivement fait dans une organisation, pour relier le faire observable à la valeur durable, aux principes, aux capacités et aux modulateurs.",
    ),
    ("Digital Twin", "Manuel de BDD - Pratiques organisationnelles sandbox.md"): (
        "Sandbox des patterns opérants récurrents pressentis d’une organisation observée, en attente d’arbitrage avant migration éventuelle vers la couche officielle des pratiques.",
        "Qualifier, comparer et tester des pratiques candidates avant arbitrage de migration vers la couche officielle, pour ne pas figer trop tôt des patterns encore instables.",
    ),
    ("Digital Twin", "Manuel de BDD - Principes organisationnels.md"): (
        "Référentiel des intentions normatives stables qui guident durablement les arbitrages récurrents d’une organisation observée.",
        "Nommer ce qui doit être vrai dans une organisation au-delà des objectifs datés, pour analyser leur incarnation dans les pratiques, leurs tensions et leur cohérence systémique.",
    ),
    ("Digital Twin", "Manuel de BDD - Principes organisationnels sandbox.md"): (
        "Sandbox des intentions normatives stables pressenties d’une organisation observée, en attente d’arbitrage avant migration éventuelle vers la couche officielle des principes.",
        "Qualifier, comparer et tester des principes candidats avant arbitrage de migration vers la couche officielle, pour éviter le figement prématuré de la couche normative.",
    ),
    ("Digital Twin", "Manuel de BDD - Problématiques.md"): (
        "Référentiel des nœuds diagnostiques consolidés d’un système observé : difficultés, tensions et dysfonctionnements suffisamment structurés pour guider priorisation, transformation et pilotage.",
        "Consolider plusieurs enjeux proches en thèmes canoniques traçables, pour aligner la gouvernance autour de sujets priorisables avant formalisation en objectifs.",
    ),
    ("Digital Twin", "Manuel de BDD - Problématiques sandbox.md"): (
        "Sandbox des nœuds diagnostiques pressentis d’un système observé, en attente d’arbitrage avant migration éventuelle vers la couche officielle des problématiques.",
        "Qualifier, comparer et tester des problématiques candidates avant arbitrage de migration vers la couche officielle, pour ne pas figer trop tôt des diagnostics encore en construction.",
    ),
    ("Digital Twin", "Manuel de BDD - Processus.md"): (
        "Référentiel des fonctionnements structurés, stabilisés et relativement indépendants des personnes, qui transforment des entrées en sorties au sein d’une organisation observée.",
        "Rendre lisible la manière dont une organisation transforme inputs en outputs de façon répétable, pour analyser interfaces, qualité attendue et critères de terminé indépendamment des personnes.",
    ),
    ("Digital Twin", "Manuel de BDD - Processus candidats.md"): (
        "Pivot de qualification des regroupements fonctionnels plausibles d’actions observées, en attente de consolidation éventuelle dans la couche officielle des processus.",
        "Qualifier des regroupements fonctionnels plausibles d’actions, pour préparer leur consolidation éventuelle en processus sans précipiter la modélisation.",
    ),
    ("Digital Twin", "Manuel de BDD - Processus candidats sandbox.md"): (
        "Sandbox des regroupements fonctionnels pressentis d’actions observées, en attente d’arbitrage avant migration éventuelle vers la couche officielle des processus candidats.",
        "Qualifier, comparer et tester des regroupements d’actions candidats avant arbitrage de migration vers la couche officielle, pour ne pas figer trop tôt des regroupements encore exploratoires.",
    ),
    ("Digital Twin", "Manuel de BDD - Relations inter-organisations.md"): (
        "Référentiel des liens structurants entre organisations distinctes : échanges opérationnels, coopérations, contrôles, régulations, positionnements de marché et transformations structurelles.",
        "Rendre visible le tissu inter-organisationnel d’un écosystème observé, pour qualifier la nature des liens entre acteurs sans confondre lien et hiérarchie interne ni propriétés intrinsèques.",
    ),
    ("Digital Twin", "Manuel de BDD - Événements.md"): (
        "Journal des repères temporels structurants — jalons, épisodes, bascules, périodes, campagnes ou programmes — qui modifient, révèlent, rythment ou reconfigurent un système observé.",
        "Reconstituer une chronologie organisationnelle exploitable, pour relire dynamiques (structure, pratiques, capacités, résultats) et contextualiser enjeux, problématiques et indicateurs par des jalons concrets.",
    ),
    # MISSION OPS
    ("Mission Ops", "Manuel de BDD - Actions LBP.md"): (
        "Backlog opérationnel d’une mission LBP, structurant l’exécution en deux niveaux (Activité, Action) et reliant le « qui fait quoi pour quand » aux meetings et bricks de la mission.",
        "Piloter l’exécution opérationnelle d’une mission LBP, pour rendre visible et coordonné le qui fait quoi pour quand au fil de la mission.",
    ),
    ("Mission Ops", "Manuel de BDD - Bricks.md"): (
        "Index des productions Markdown d’une mission LBP, qualifiées, versionnées et reliées aux actions qui les produisent ou les utilisent.",
        "Tenir trace des productions documentaires d’une mission LBP, pour les retrouver, les versionner et piloter leur avancement documentaire en cohérence avec l’exécution.",
    ),
    ("Mission Ops", "Manuel de BDD - Meetings.md"): (
        "Journal opérationnel des rendez-vous datés d’une mission LBP : réunions, entretiens, ateliers, comités ou restitutions.",
        "Tenir le journal des occurrences de rendez-vous d’une mission, pour rendre visible la cadence d’interactions et la relier aux actions qui les préparent, s’y déroulent ou en assurent le suivi.",
    ),
    ("Mission Ops", "Manuel de BDD - Sources d’informations.md"): (
        "Registre de preuve d’une mission LBP indexant les supports, traces, fragments, documents, échanges et éléments observables ancrant les analyses et productions.",
        "Garantir la traçabilité des matières mobilisées au cours d’une mission, pour ancrer analyses, productions et décisions sur des supports identifiables et qualifiés.",
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
    ok = 0
    errors = []
    for (folder, fname), (sumv, purv) in MAPPING.items():
        p = ROOT / folder / fname
        if not p.exists():
            errors.append(f"MISSING: {fname}")
            continue
        if len(sumv) > 400:
            errors.append(f"sum>400 ({len(sumv)}): {fname}")
            continue
        if len(purv) > 400:
            errors.append(f"pur>400 ({len(purv)}): {fname}")
            continue
        c = p.read_text(encoding="utf-8")
        c, sok = replace_field(c, "summary", sumv)
        c, pok = replace_field(c, "purpose", purv)
        if sok and pok:
            p.write_text(c, encoding="utf-8")
            ok += 1
        else:
            errors.append(f"partial sum={sok} pur={pok}: {fname}")
    print(f"OK: {ok}/{len(MAPPING)}")
    if errors:
        print("Errors:")
        for e in errors: print(f"  {e}")


if __name__ == "__main__":
    main()
