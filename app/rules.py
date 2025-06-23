def classify_image(features):
    # Exemple de règle : couleur moyenne < 100 ET taille > 200Ko => pleine
    seuil_couleur = 100
    seuil_taille = 200 * 1024  # 200 Ko
    avg_color = (features.get('avg_red',0) + features.get('avg_green',0) + features.get('avg_blue',0)) / 3
    if avg_color < seuil_couleur and features.get('file_size',0) > seuil_taille:
        return 'pleine'
    else:
        return 'vide' 