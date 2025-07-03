import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm

def extraire_caracteristiques(chemin_image):
    image = cv2.imread(chemin_image)
    image_redimensionnee = cv2.resize(image, (256, 256))
    gris = cv2.cvtColor(image_redimensionnee, cv2.COLOR_BGR2GRAY)

    taille_ko = os.path.getsize(chemin_image) / 1024
    hauteur, largeur = image.shape[:2]
    moyenne_couleur = cv2.mean(image)[:3]
    histo_gris = cv2.calcHist([gris], [0], None, [256], [0, 256]).flatten()
    histo_gris = histo_gris / np.sum(histo_gris)
    ecart_type_histogramme = np.std(histo_gris)
    contraste = np.max(gris) - np.min(gris)
    contours_detectes = cv2.Canny(gris, 100, 200)
    densite_contours = np.sum(contours_detectes > 0) / contours_detectes.size
    contours, _ = cv2.findContours(contours_detectes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    aires = [cv2.contourArea(c) for c in contours if cv2.contourArea(c) > 0]
    taille_moyenne_par_contour = np.mean(aires) / contours_detectes.size if aires else 0

    return {
        "taille_fichier_Ko": taille_ko,
        "largeur": largeur,
        "hauteur": hauteur,
        "moyenne_R": moyenne_couleur[2],
        "moyenne_V": moyenne_couleur[1],
        "moyenne_B": moyenne_couleur[0],
        "luminosite": np.mean(gris),
        "ecart_type_gris": np.std(gris),
        "contraste": contraste,
        "ecart_type_histogramme": ecart_type_histogramme,
        "densite_contours": densite_contours,
        "taille_par_contours": taille_moyenne_par_contour
    }

def traiter_images_sans_labels(dossier_images):
    donnees = []
    for fichier in tqdm(os.listdir(dossier_images), desc="Analyse sans labels"):
        chemin = os.path.join(dossier_images, fichier)
        try:
            c = extraire_caracteristiques(chemin)
            c.update({"nom_fichier": fichier})
            donnees.append(c)
        except:
            print(f"❌ Erreur sur {chemin}")
    return pd.DataFrame(donnees)

if __name__ == "__main__":
    dossier = "Data/train/no_label"
    df = traiter_images_sans_labels(dossier)
    df.to_csv("resultats.csv", index=False)
    print("✅ Extraction terminée : resultats.csv généré")
