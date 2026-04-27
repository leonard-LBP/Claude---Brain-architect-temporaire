"""
Casting ACME — scénario fictif PME industrielle pour peupler les 22 BDD non-sandbox.

Univers : ACME Industries, ~50 personnes, 3 BUs (Production, R&D, Commercial).
Partenaires externes : Fournisseur Alpha (matières), Client Beta (gros compte).

Pour chaque BDD : 3 entrées avec Nom + Description courte + Statut + 1-2 select
structurants (alimentent les rollups). PAS de relations (Passe relations à valider
manuellement avec Leonard).

Génère un JSON `simulation_acme_casting.json` consommable par le sub-agent
qui appellera notion-create-pages.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
REGISTRY = json.load(open(ROOT / "bdd_registry.json", encoding="utf-8"))


# Casting : nom_bdd → liste de 3 dicts {nom, description, props_extra}
# Les props_extra sont des couples (nom_prop_native, valeur) qui doivent matcher
# le schéma Notion. Le sub-agent vérifiera/échappera.
CASTING = {
    "Organisations": [
        {"nom": "ACME Industries", "description": "PME industrielle, ~50 personnes, 3 BUs (Production, R&D, Commercial). Cœur du scénario."},
        {"nom": "Fournisseur Alpha", "description": "Fournisseur historique de matières premières d'ACME. Hausse récente des prix de 15%."},
        {"nom": "Client Beta", "description": "Gros compte stratégique d'ACME. Contrat-cadre triennal."},
    ],
    "Collectifs": [
        {"nom": "Équipe Production ACME", "description": "BU Production : ligne d'assemblage A et atelier d'usinage. ~20 personnes."},
        {"nom": "Équipe R&D ACME", "description": "BU R&D : conception nouveaux produits, prototypage. ~10 personnes."},
        {"nom": "Comité de pilotage ACME", "description": "Instance hebdomadaire de coordination des 3 BUs. Direction + chefs de BU."},
    ],
    "Postes": [
        {"nom": "Directeur·rice Production ACME", "description": "Pilote la BU Production, animation équipe, KPIs qualité/flux."},
        {"nom": "Ingénieur·e R&D senior ACME", "description": "Conception produits, expertise technique, lien avec Production."},
        {"nom": "Commercial·e grands comptes ACME", "description": "Gestion portefeuille clients stratégiques, coordination avec Production."},
    ],
    "Individus": [
        {"nom": "Marie Dubois", "description": "Directrice Production ACME, en poste depuis 3 ans."},
        {"nom": "Karim Benali", "description": "Ingénieur R&D senior ACME, expert procédés."},
        {"nom": "Sophie Martin", "description": "Commerciale grands comptes ACME, gère le compte Client Beta."},
    ],
    "Environnements": [
        {"nom": "Atelier de production ACME", "description": "Site principal de production, lignes d'assemblage A et B."},
        {"nom": "Lab R&D ACME", "description": "Espace prototypage et tests, équipement de mesure."},
        {"nom": "Showroom client ACME", "description": "Espace de démonstration produits pour visites clients."},
    ],
    "Événements": [
        {"nom": "Lancement produit X (juin 2026)", "description": "Lancement commercial du nouveau produit X, point d'orgue du plan R&D 2026."},
        {"nom": "Audit qualité ISO 9001 (sept 2026)", "description": "Audit de renouvellement de certification ISO 9001."},
        {"nom": "Crise fournisseur Alpha (déc 2025)", "description": "Hausse de prix unilatérale 15% par Fournisseur Alpha, impact marge."},
    ],
    "Relations inter-organisations": [
        {"nom": "ACME ↔ Fournisseur Alpha — partenariat stratégique", "description": "Relation historique de fourniture matières premières, contrat-cadre."},
        {"nom": "ACME ↔ Client Beta — contrat-cadre", "description": "Contrat-cadre triennal, ~15% du CA ACME."},
        {"nom": "ACME ↔ Concurrent Gamma — veille concurrentielle", "description": "Veille passive, pas de relation commerciale directe."},
    ],
    "Actions détectées": [
        {"nom": "Refonte ligne assemblage A (mars 2026)", "description": "Décision en COPIL de refondre la ligne A pour réduire les défauts."},
        {"nom": "Mise en place CRM unifié (mai 2026)", "description": "Initiative pilotée par BU Commercial, remplacement CRM legacy."},
        {"nom": "Workshop innovation produit (juillet 2026)", "description": "Atelier 2 jours équipes R&D + Commercial pour idéation produits."},
    ],
    "Enjeux": [
        {"nom": "Réduire le time-to-market produit", "description": "Réduire le délai conception → mise en marché, levier compétitivité."},
        {"nom": "Risque dépendance fournisseur unique", "description": "Risque de rupture matière sur Fournisseur Alpha, exposition forte."},
        {"nom": "Besoin montée en compétence digitale", "description": "Besoin RH : monter en compétence sur outils digitaux (CRM, ERP, BI)."},
    ],
    "Journal des signaux": [
        {"nom": "Commerciaux perdent du temps à chercher l'info (Q1 2026)", "description": "Verbatim répété en réunion COPIL : irritation commerciaux sur accès info client."},
        {"nom": "Délais R&D s'allongent (Q2 2026)", "description": "Métrique : TTM moyen passé de 6 à 9 mois sur dernier semestre."},
        {"nom": "Fournisseur Alpha hausse prix +15% (Q1 2026)", "description": "Signal externe : courrier officiel Fournisseur Alpha annonçant hausse."},
    ],
    "Glossaire spécifique": [
        {"nom": "TTM (Time to Market)", "description": "Délai entre lancement projet R&D et mise en marché produit. KPI clé chez ACME."},
        {"nom": "BU (Business Unit)", "description": "Unité opérationnelle autonome chez ACME (Production, R&D, Commercial)."},
        {"nom": "DoD (Definition of Done)", "description": "Critères d'acceptation d'une livraison R&D (tests, doc, validation qualité)."},
    ],
    "Initiatives organisationnelles": [
        {"nom": "Initiative ACME Digital 2026", "description": "Programme transversal de transformation digitale (CRM, ERP, BI). 12 mois."},
        {"nom": "Initiative Excellence opérationnelle Production", "description": "Plan d'amélioration continue ligne A : réduction défauts -30%."},
        {"nom": "Initiative Diversification fournisseurs", "description": "Identification + qualification de 2 fournisseurs alternatifs à Alpha."},
    ],
    "Modulateurs": [
        {"nom": "Niveau de maturité data ACME", "description": "Modulateur SI : qualité et accessibilité des données opérationnelles."},
        {"nom": "Climat de confiance inter-équipes ACME", "description": "Modulateur culturel : qualité du travail entre Production, R&D et Commercial."},
        {"nom": "Disponibilité des outils digitaux ACME", "description": "Modulateur SI : couverture et stabilité des outils CRM, ERP, collaboration."},
    ],
    "Processus candidats": [
        {"nom": "Processus Onboarding nouveau client (candidat)", "description": "Esquisse de processus type pour intégrer un nouveau client grands comptes."},
        {"nom": "Processus Validation qualité produit (candidat)", "description": "Esquisse de processus formalisant les contrôles qualité produit fini."},
        {"nom": "Processus REX post-incident (candidat)", "description": "Esquisse de processus de retour d'expérience après incident production."},
    ],
    "Capacités organisationnelles": [
        {"nom": "Capacité Innovation produit", "description": "Capacité d'ACME à concevoir, prototyper et industrialiser de nouveaux produits."},
        {"nom": "Capacité Excellence opérationnelle", "description": "Capacité à produire en grande série avec maîtrise qualité/coût/délai."},
        {"nom": "Capacité Relation client", "description": "Capacité à gérer durablement les comptes stratégiques et fidéliser."},
    ],
    "Indicateurs": [
        {"nom": "TTM moyen (jours)", "description": "Time to Market moyen sur les projets R&D des 12 derniers mois."},
        {"nom": "Taux de défauts production (%)", "description": "Pourcentage de pièces rejetées en sortie ligne A par mois."},
        {"nom": "NPS client", "description": "Net Promoter Score moyen mesuré semestriellement auprès des grands comptes."},
    ],
    "OKR": [
        {"nom": "OKR Devenir leader européen (2026-2028)", "description": "Objectif: leader européen sur segment produit X. KR1: 30% PdM, KR2: NPS>50."},
        {"nom": "OKR Réduire délais R&D (2026)", "description": "Objectif: réduire TTM. KR1: -20% TTM moyen, KR2: 80% projets dans délai."},
        {"nom": "OKR Diversifier fournisseurs (2026)", "description": "Objectif: réduire dépendance Alpha. KR1: 3 fournisseurs validés, KR2: 0 dépendance >40%."},
    ],
    "Pratiques organisationnelles": [
        {"nom": "Pratique Stand-up quotidien R&D", "description": "Rituel quotidien 15 min équipe R&D : avancement, blocages, entraide."},
        {"nom": "Pratique Revue qualité hebdomadaire", "description": "Revue hebdo BU Production : analyse défauts, actions correctives."},
        {"nom": "Pratique REX trimestriel", "description": "Atelier REX trimestriel toutes BUs : retours d'expérience structurés."},
    ],
    "Principes organisationnels": [
        {"nom": "Principe : amélioration continue par le terrain", "description": "Les améliorations émergent du terrain, pas du sommet. Voix opérationnels valorisés."},
        {"nom": "Principe : décider au plus près de l'action", "description": "Subsidiarité : décisions prises au niveau le plus proche de l'exécution."},
        {"nom": "Principe : sécurité avant tout", "description": "Sécurité non négociable. Tout collaborateur peut stopper la production."},
    ],
    "Problématiques": [
        {"nom": "Problématique Silotage Production / R&D", "description": "Faible communication entre BUs Production et R&D, retours terrain peu remontés."},
        {"nom": "Problématique Dette technique CRM legacy", "description": "Le CRM actuel ne supporte plus les workflows commerciaux multi-canaux."},
        {"nom": "Problématique Manque visibilité chaîne de valeur", "description": "Pas de vue end-to-end commande → livraison, KPIs fragmentés."},
    ],
    "Processus": [
        {"nom": "Processus Production série standard", "description": "Processus stable et documenté de production de la gamme principale ACME."},
        {"nom": "Processus Développement nouveau produit", "description": "Processus R&D de la conception au transfert vers Production."},
        {"nom": "Processus Gestion commande client", "description": "Processus commercial de la prise de commande à la facturation."},
    ],
    "Actifs": [
        {"nom": "Machine d'usinage 5-axes", "description": "Équipement clé de la ligne A, machine d'usinage haute précision 5-axes."},
        {"nom": "ERP SAP ACME", "description": "ERP central, gestion finance/RH/production, déployé depuis 2018."},
        {"nom": "Brevet Formule X", "description": "Brevet déposé 2024 sur la formulation du produit X, actif immatériel stratégique."},
    ],
}


def main():
    # Validate: each BDD must exist in registry, must be non-sandbox, casting has 3 entries
    out = []
    for db_name, entries in CASTING.items():
        if db_name not in REGISTRY["databases"]:
            print(f"  ⚠ '{db_name}' absent du registry, skip.")
            continue
        if "sandbox" in db_name.lower():
            print(f"  ⚠ '{db_name}' est sandbox, skip.")
            continue
        if len(entries) != 3:
            print(f"  ⚠ '{db_name}' a {len(entries)} entrées (attendu 3).")
        ds_id = REGISTRY["databases"][db_name]["data_source_id"]
        out.append({
            "bdd_name": db_name,
            "data_source_id": ds_id,
            "entries": entries,
        })

    # Coverage check
    non_sandbox_in_registry = [n for n in REGISTRY["databases"] if "sandbox" not in n.lower()]
    casting_names = set(CASTING.keys())
    missing = [n for n in non_sandbox_in_registry if n not in casting_names]
    if missing:
        print(f"\n⚠ {len(missing)} BDD non-sandbox sans casting :")
        for n in missing:
            print(f"  - {n}")

    out_path = ROOT / "simulation_acme_casting.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    total_entries = sum(len(d["entries"]) for d in out)
    print(f"\n✓ Casting généré : {len(out)} BDD × ~3 entrées = {total_entries} pages.")
    print(f"  Output : {out_path}")


if __name__ == "__main__":
    main()
