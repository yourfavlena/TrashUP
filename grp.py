import pandas as pd

# Création de la matrice des risques
risk_matrix = pd.DataFrame({
    "Risque": [
        "R1 - Retard développement Android/iOS",
        "R2 - Problème API Google Calendar",
        "R3 - Non-conformité RGPD",
        "R4 - Cybersécurité (freelance partiel)",
        "R5 - Synchronisation équipe",
        "R6 - Réduction budgétaire à mi-parcours",
        "R7 - Retard UX/design",
        "R8 - Concurrence anticipée",
        "R9 - Tests utilisateurs insuffisants",
        "R10 - Acquisition utilisateurs difficile"
    ],
    "Impact (1-5)": [4, 3, 5, 5, 3, 4, 3, 4, 2, 3],
    "Probabilité (1-5)": [4, 5, 3, 2, 3, 4, 2, 3, 4, 3],
})

risk_matrix["Score"] = risk_matrix["Impact (1-5)"] * risk_matrix["Probabilité (1-5)"]
risk_matrix["Catégorie"] = risk_matrix["Score"].apply(
    lambda x: "🔴 Critique" if x >= 15 else ("🟠 Élevé" if x >= 10 else ("🟡 Moyen" if x >= 6 else "🟢 Faible"))
)

# Affichage de la matrice des risques
print("\nFiche Synthèse – Gestion des Risques\n" + "="*40)
print("\nMatrice des Risques\n" + "-"*40)
print(risk_matrix.to_string(index=False))

def fiche_detail(titre, sous_titre, causes, consequences, prevention, mitigation):
    print("\n" + "="*40)
    print(titre)
    print(sous_titre)
    print("\nCauses :\n" + causes)
    print("\nConséquences :\n" + consequences)
    print("\nPrévention :\n" + prevention)
    print("\nPlan de mitigation :\n" + mitigation)

fiche_detail(
    "Fiche Détail – Risque Critique 1",
    "R6 – Réduction budgétaire de 20% à mi-parcours",
    "- Changement de stratégie financière\n- Financement externe non sécurisé",
    "- Réduction de la portée fonctionnelle\n- Retards ou annulation de phases\n- Difficultés à maintenir la qualité",
    "- Prévoir un buffer budgétaire\n- Prioriser les fonctionnalités essentielles (MVP)\n- Rechercher des financements externes",
    "- Réduction temporaire des prestations externes\n- Réduction de périmètre ou qualité visuelle\n- Subventions publiques e-santé"
)

fiche_detail(
    "Fiche Détail – Risque Critique 2",
    "R2 – Problème API Google Calendar",
    "- Modification inattendue des API\n- Politiques internes de Google",
    "- Fonction de synchronisation inopérante\n- Re-développement à prévoir\n- Diminution de la valeur perçue",
    "- Veille technologique régulière\n- Connecteurs alternatifs prévus (iCal, Outlook)\n- Documentation complète dès la conception",
    "- Intégration d'une solution locale\n- Adaptation rapide grâce à documentation API\n- Contingence technique dans le code"
)

print("\nFin de la synthèse des risques.")
