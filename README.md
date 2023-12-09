# Chatbot AI Assistant

## Description
Ce projet est un clone de ChatGPT, qui a été développé en utilisant l'API OpenAI et 
intégré dans une application web Flask.

## Objectif
L'objectif est de fournir une expérience interactive de chatbot, similaire à ChatGPT, pour aider les utilisateurs à 
obtenir des réponses à leurs questions, à explorer des sujets ou à obtenir de l'aide sur divers sujets.

## Fonctionnalités
Le bot peut répondre à des questions, générer du texte créatif, aider à la programmation, et plus encore.

## Technologies Utilisées
* Flask 
* OpenAI API
* Python
* TailwindCSS
* HTML
* CSS
* JavaScript

## Comment ça fonctionne ?
Les utilisateurs entrent leurs questions via l'interface web. Le front-end gère l'envoi des requêtes, la réception des 
réponses de l'API GPT et la mise à jour de l'interface utilisateur en conséquence. Ces requêtes sont envoyées au backend 
Flask, qui les transmet à l'API OpenAI. Les réponses générées sont ensuite renvoyées à l'utilisateur via l'interface web.

## Utilisation et Accès
Les utilisateurs peuvent accéder au chatbot via une URL web et commencer à interagir immédiatement. 
Il n'y a pas besoin de configuration ou d'installation supplémentaire.

## Installation

1. Clonez le dépôt Git
   ```sh
   git clone https://github.com/souleymanediallo/clonechatgpt
    ```
2. Créez un environnement virtuel :
   ```sh
   python -m venv venv
   ```
   ### Activez l'environnement virtuel :
   * Sur Windows :
   ```sh
   venv\Scripts\activate
   ```
    * Sur MacOS/Linux :
   ```sh
   source venv/bin/activate
   ```
   
4. Installez les dépendances :
* Assurez-vous que l'environnement virtuel est activé.
* Installez les dépendances requises en exécutant :
   ```sh
    pip install -r requirements.txt
    ```
5. Configurez la variable d'environnement :
   * Créez un fichier `.env` dans le répertoire principal du projet.
     ```sh
     touch .env
     ```
   * Ajoutez votre clé API OpenAI à ce fichier :
     ```sh
     OPENAI_API_KEY='votre_clé_api'
     ```
6. Lancez l'application Flask :
* Dans le terminal, assurez-vous d'être dans le répertoire du projet.
* Exécutez l'application en utilisant :
   ```sh
   python app.py
   ```
