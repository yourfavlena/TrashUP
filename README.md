# TrashUP – Plateforme intelligente de suivi des poubelles

## Objectif
Plateforme web pour :
- Collecter, annoter et visualiser des images de poubelles publiques (pleines/vides)
- Extraire automatiquement des caractéristiques visuelles simples
- Classifier les images via des règles conditionnelles (pas de machine learning)
- Visualiser les données (dashboard, carte interactive)
- Rechercher une poubelle par localisation ou ID
- Intégrer une démarche Green IT et une évaluation des risques

## Stack technique
- **Back-end** : Python (Flask, Flask-SQLAlchemy)
- **Gestion des images** : Pillow, OpenCV
- **Base de données** : SQLite
- **Front-end** : HTML/CSS, Bootstrap 5, Chart.js, Leaflet.js
- **Visualisation** : matplotlib (backend), Chart.js (frontend), Leaflet (carte)
- **Internationalisation** : Flask-Babel (prévu)

## Structure du projet
```
TrashUP/
│
├── app/
│   ├── static/
│   │   └── uploads/           # Images uploadées
│   ├── templates/             # Templates Jinja2 (HTML)
│   │   ├── base.html
│   │   ├── Header.html, Footer.html
│   │   ├── index.html, upload.html, dashboard.html, map.html, images.html, image_detail.html, search_results.html
│   ├── __init__.py            # Création de l'app Flask
│   ├── routes.py              # Toutes les routes Flask
│   ├── models.py              # Modèle TrashImage
│   ├── feature_extractor.py   # Extraction des features images
│   ├── rules.py               # Règles de classification
│   └── dashboard.py           # Statistiques et dashboard
│
├── extraction/                # Scripts d'extraction/classification (legacy)
├── php/                       # Scripts PHP (import, dashboard, etc.)
├── Guides/                    # Documentation Green IT, risques, grille d'impacts
├── site_dist/                 # Version statique du site (HTML)
├── requirements.txt           # Dépendances Python
├── package.json               # Dépendances JS (Chart.js, Parcel, etc.)
├── run.py                     # Lancement de l'app Flask
├── README.md                  # Ce fichier
└── ...
```

## Installation et démarrage
1. Cloner le dépôt et se placer dans le dossier TrashUP
2. Installer les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```
3. Installer les dépendances JS (optionnel, pour Chart.js/Parcel) :
   ```bash
   npm install
   ```
4. Lancer l'application Flask :
   ```bash
   python run.py
   ```
5. Accéder à la plateforme sur http://localhost:5000

## Fonctionnalités principales
- Upload et annotation d'images (pleine/vide)
- Extraction automatique de caractéristiques (taille, couleur, histogramme, contraste, etc.)
- Classification par règles conditionnelles
- Dashboard (statistiques, graphiques)
- Carte interactive (Leaflet) avec position des poubelles
- Recherche par localisation ou ID
- Internationalisation (FR/EN, en cours)
- Documentation Green IT et évaluation des risques

## Modèle principal (TrashImage)
- id, filename, upload_date, annotation, file_size, width, height, avg_red, avg_green, avg_blue, histogram, contrast, edges, luminance_hist, location, latitude, longitude

## Dépendances principales
### Python (requirements.txt)
- Flask, Flask_SQLAlchemy, Pillow, opencv-python, matplotlib, python-dotenv, Flask-Babel
### JS (package.json)
- chart.js, parcel, @cubejs-client/core

## Auteurs
- Anil BRAUN
- (Collaborateurs : à compléter)

## Notes
- Pour la géolocalisation automatique, activer la localisation dans le navigateur (HTTPS ou localhost recommandé).
- Un dossier `php/` existe pour des scripts d'import ou de dashboard legacy.
- Le dossier `site_dist/` contient une version statique HTML du site.
- Guides et documentation dans le dossier `Guides/`.
