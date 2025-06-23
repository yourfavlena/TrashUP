from PIL import Image
import numpy as np
import os
import cv2

def extract_features(image_path):
    features = {}
    # Taille du fichier
    features['file_size'] = os.path.getsize(image_path)
    # Ouverture de l'image
    img = Image.open(image_path)
    features['width'], features['height'] = img.size
    # Couleur moyenne
    arr = np.array(img)
    if arr.ndim == 3:
        features['avg_red'] = float(np.mean(arr[:,:,0]))
        features['avg_green'] = float(np.mean(arr[:,:,1]))
        features['avg_blue'] = float(np.mean(arr[:,:,2]))
    else:
        features['avg_red'] = features['avg_green'] = features['avg_blue'] = float(np.mean(arr))
    # Histogramme RVB
    features['histogram'] = img.histogram()
    # Contraste
    features['contrast'] = float(np.max(arr) - np.min(arr))
    # Détection de contours (Canny)
    img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img_cv, 100, 200)
    features['edges'] = edges.tolist()
    # Histogramme de luminance
    luminance = 0.2126*arr[:,:,0] + 0.7152*arr[:,:,1] + 0.0722*arr[:,:,2] if arr.ndim == 3 else arr
    features['luminance_hist'] = np.histogram(luminance, bins=16)[0].tolist()
    return features 