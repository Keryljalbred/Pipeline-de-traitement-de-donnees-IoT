FROM python:3.8

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste de votre code
COPY . .

# Commande par défaut
CMD ["python", "storage.py"]