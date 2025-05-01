# README - Projet : Pipeline de traitement de données IoT avec Apache Airflow et Cassandra

## Table des matières

1. [Contexte](#contexte)
2. [Objectifs du projet](#objectifs-du-projet)
3. [Technologies utilisées](#technologies-utilisées)
4. [Étapes du projet](#étapes-du-projet)
5. [Défis à relever](#défis-à-relever)
6. [Installation et Configuration](#installation-et-configuration)
7. [Utilisation](#utilisation)
8. [Contributions](#contributions)
9. [Contact](#contact)

## Contexte

Une entreprise spécialisée dans les objets connectés (IoT) souhaite mettre en place un pipeline de collecte, transformation et stockage des données issues de ses capteurs industriels. Les données collectées en temps réel doivent être nettoyées, transformées et stockées efficacement pour une analyse ultérieure. Le pipeline doit être automatisé pour gérer la collecte des données provenant de différents dispositifs IoT et assurer un stockage performant et évolutif à l’aide d’Apache Cassandra.

## Objectifs du projet

- **Collecte des données IoT**
  - Récupérer les données des capteurs en temps réel via une API REST.
  - Gérer les flux entrants de données hétérogènes (température, humidité, pression, etc.).

- **Transformation et nettoyage des données**
  - Vérifier l’intégrité et la qualité des données reçues.
  - Normaliser les données (formatage de la date, gestion des valeurs manquantes).
  - Agréger les données pour des analyses futures.

- **Stockage dans Apache Cassandra**
  - Stocker les données de manière distribuée pour gérer de grands volumes en temps réel.
  - Assurer une disponibilité et une scalabilité maximales des données.
  - Structurer la base pour des analyses efficaces.

- **Orchestration du pipeline avec Airflow**
  - Automatiser la collecte, transformation et ingestion dans Cassandra.
  - Mettre en place des tâches planifiées pour vérifier l’intégrité des données.
  - Surveiller le pipeline et générer des alertes en cas d’erreur.

## Technologies utilisées

- **Apache Airflow**
- **Apache Cassandra**
- **Python**
- **Docker**
- **Grafana**

## Étapes du projet

1. **Définition de la source de données IoT**
   - Choisir une source de données IoT (via une API REST).
   - Configurer un simulateur de données IoT si aucune source réelle n’est disponible (ex. : [Mockaroo](https://www.mockaroo.com/)).

2. **Ingestion des données avec Apache Airflow**
3. **Nettoyage et transformation des données**
4. **Stockage dans Apache Cassandra**
5. **Orchestration avec Apache Airflow**
6. **Analyse des données stockées**

## Défis à relever

- Gérer les flux de données en temps réel.
- Nettoyer efficacement les données IoT.
- Optimiser les requêtes dans Cassandra.
- Assurer la fiabilité du pipeline.

## Installation et Configuration

### Prérequis

- Docker et Docker Compose installés
- Python 3.x

### Étapes d'installation

1. **Lancez les conteneurs** :
   ```bash
   docker-compose up -d
   ```

2. **Accédez à Grafana** :
   Ouvrez votre navigateur à l'adresse `http://localhost:3000` et connectez-vous avec les identifiants par défaut.

## Utilisation

1. **Configurer les sources de données dans Grafana**.
2. **Créer des tableaux de bord pour visualiser les données**.
3. **Utiliser Airflow pour orchestrer les tâches de collecte et de transformation**.

## Contributions

Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage (pull request) pour toute amélioration ou correction.

## Contact

Pour toute question ou suggestion, veuillez contacter :

- **Nom** : Keryl DJEUKOUA
- **Email** : keryljk@gmail.com

---
