# Flask API Project

## Description du projet

Ce projet consiste en la création d'un timer partagé synchronisé en réseau dans le but est l'utilisation en festival (SOLECTRO). Le projet s'articule en plusieurs parties. Ce repo Github est le code et le fonctionnement du server principal qui emet le timer. Il aura pour fonctionalté: 


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

