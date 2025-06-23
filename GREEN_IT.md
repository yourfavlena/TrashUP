# Démarche Green IT & Évaluation des risques – TrashUP

## 1. Écoconception et bonnes pratiques
- Utilisation de technologies légères (Flask, SQLite) pour limiter la consommation de ressources serveur
- Stockage local des images, pas de cloud inutile
- Extraction de features optimisée (traitement à l'upload, pas de calculs redondants)
- Visualisation côté client (Leaflet, Chart.js possible) pour décharger le serveur
- Interface sobre, peu d'assets lourds, pas de vidéos ni de scripts superflus
- Possibilité de filtrer et supprimer les images pour limiter le stockage

## 2. Évaluation des impacts
- **Stockage** : limité par la taille des images et la base SQLite, possibilité de nettoyage régulier
- **Transport de données** : images compressées (JPG/PNG), pas de transfert massif ou de streaming
- **Traitement** : extraction de features simple, pas de machine learning lourd
- **Device utilisateur** : interface responsive, compatible mobile/tablette, pas de calculs lourds côté client

## 3. Questionnaire d'écoconception (synthèse)
- **Stratégie** : projet à impact environnemental positif (réduction des déchets sauvages)
- **Spécifications** : fonctionnalités limitées à l'essentiel, pas de sur-fonctionnalité
- **Architecture** : monolithique, simple, facile à héberger sur serveur mutualisé
- **UX/UI** : interface claire, accessible, peu énergivore
- **Contenus** : images compressées, pas de vidéos
- **Frontend/Backend** : frameworks légers, peu de dépendances
- **Hébergement** : possible sur serveur local ou mutualisé, faible empreinte
- **Algorithmie** : pas d'IA lourde, règles simples, extraction optimisée

## 4. Évaluation des risques
- **Sécurité** : vérification des formats d'images, pas d'exécution de code externe
- **Vie privée** : pas de collecte de données personnelles, géolocalisation optionnelle
- **Robustesse** : gestion des erreurs d'upload, vérification des entrées utilisateur
- **Scalabilité** : adapté à un usage local ou petite collectivité, peut évoluer vers du cloud si besoin

## 5. Améliorations possibles
- Compression automatique des images à l'upload
- Suppression automatique des images anciennes/non utilisées
- Ajout de filtres pour limiter l'affichage/traitement
- Hébergement sur serveur à énergie renouvelable

--- 