# TrashUP – Plateforme intelligente de suivi des poubelles

## Objectif
Développer une plateforme web pour :
- Collecter et annoter des images de poubelles (pleines/vides)
- Extraire automatiquement des caractéristiques visuelles simples
- Classifier les images via des règles conditionnelles (pas de machine learning)
- Visualiser les données et cartographier les zones à risque
- Intégrer une démarche Green IT et une évaluation des risques

## Stack technique
- **Back-end** : Python (Flask)
- **Gestion des images** : Pillow, OpenCV
- **Base de données** : SQLite (via SQLAlchemy)
- **Front-end** : HTML/CSS, Bootstrap, Chart.js
- **Visualisation** : matplotlib (backend), Chart.js (frontend)

## Structure du projet
```
TrashUP/
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── uploads/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── feature_extractor.py
│   ├── rules.py
│   └── dashboard.py
│
├── requirements.txt
├── README.md
├── eco_questionnaire.docx
├── impact_synthesis.xlsx
└── run.py
```

## Installation et démarrage
1. Cloner le dépôt et se placer dans le dossier TrashUP
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancer l'application :
   ```bash
   python run.py
   ```
4. Accéder à la plateforme sur http://localhost:5000

## Fonctionnalités principales
- Upload et annotation d'images
- Extraction automatique de caractéristiques
- Classification par règles conditionnelles
- Dashboard et visualisation
- Documentation Green IT et évaluation des risques

## Auteurs
- Anil BRAUN
- Wassim DJENANE
- Sean KAMGAING
- Jeremy BARDET
- Lena MAKRI
