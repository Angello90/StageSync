# Flask API Project

## Description

Ce projet est une API REST construite avec Flask. Elle est organisée de manière modulaire pour être facilement extensible et maintenable. Elle expose plusieurs endpoints pour gérer des utilisateurs, des produits, et d'autres entités.

---

## Structure du Projet

```
my_flask_api/
├── app/
│   ├── __init__.py         # Initialisation de l'application Flask
│   ├── routes/             # Dossier contenant les routes
│   │   ├── __init__.py     # Enregistrement des routes
│   │   ├── user_routes.py  # Routes pour les utilisateurs
│   │   ├── product_routes.py # Routes pour les produits
│   │   ├── data_routes.py  # Route pour renvoyer un tableau JSON
│   ├── models/             # Modèles pour SQLAlchemy
│   │   ├── __init__.py     
│   │   ├── user_model.py   
│   ├── config.py           # Configuration de l'application
│   ├── extensions.py       # Extensions Flask
├── migrations/             # Migrations pour la base de données
├── tests/                  # Tests unitaires
├── run.py                  # Point d'entrée de l'application
├── requirements.txt        # Liste des dépendances
└── README.md               # Documentation du projet
```

---

## Installation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-projet.git
   cd nom-du-projet
   ```

2. **Créez un environnement virtuel :**
   ```bash
   python -m venv env
   source env/bin/activate   # macOS/Linux
   env\Scripts\activate      # Windows
   ```

3. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialisez la base de données (optionnel si vous utilisez SQLAlchemy) :**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

---

## Lancement du Projet

1. **Démarrez le serveur Flask :**
   ```bash
   flask --app run.py run
   ```

2. **Accédez à l'API via votre navigateur ou un outil comme Postman :**
   ```
   http://127.0.0.1:5000/
   ```

---

## Endpoints

### **Routes Utilisateurs**
- `GET /api/users/` : Retourne tous les utilisateurs.
- `GET /api/users/<id>` : Retourne les détails d'un utilisateur.

### **Routes Produits**
- `GET /api/products/` : Retourne tous les produits.
- `GET /api/products/<id>` : Retourne les détails d'un produit.

### **Exemple de Tableau JSON**
- `GET /api/data/get` : Retourne un tableau JSON simple :
  ```json
  [
      {"id": 1, "name": "Alice"},
      {"id": 2, "name": "Bob"},
      {"id": 3, "name": "Charlie"}
  ]
  ```

---

## Tests

Pour exécuter les tests unitaires :

```bash
pytest tests/
```

