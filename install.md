# 🛠️ Guide d'Installation et d'Accès à l'Application

Ce document est destiné aux utilisateurs souhaitant déployer, exécuter et tester l'application **Smart Tour Guide** sur leur machine locale. L'architecture reposant entièrement sur l'Edge AI, l'exécution des modèles de Vision et de NLP s'effectue à 100% en local et hors-ligne.

---

## 1. Prérequis Système

Avant de procéder à la configuration, assurez-vous que votre système dispose des spécifications suivantes :
* **Système d'exploitation** : Windows, macOS ou Linux.
* **Python** : Version 3.10 ou supérieure installée.
* **Ollama** : Le moteur d'inférence pour grands modèles de langage (LLM) doit être installé sur la machine. Vous pouvez le télécharger gratuitement sur [ollama.com](https://ollama.com/).
* **Ressources Matérielles** : Un minimum de 8 Go de RAM est requis (16 Go fortement recommandés pour une fluidité d'inférence optimale du LLM).

---

## 2. Récupération du Projet

Deux options s'offrent à vous pour récupérer l'intégralité du code source et des fichiers du projet :

### Option A : Téléchargement direct (Recommandé pour le Jury)
1. En haut à droite de cette page GitHub, cliquez sur le bouton vert **"Code"**.
2. Sélectionnez **"Download ZIP"**.
3. Extrayez l'archive téléchargée dans le dossier de votre choix sur votre ordinateur.
4. Ouvrez un terminal (ou invite de commande) et naviguez jusqu'à la racine de ce dossier extrait.

### Option B : Clonage via Git (Pour les développeurs)
Ouvrez votre terminal et exécutez la suite de commandes suivante :
git clone [https://github.com/votre-nom/morocco-2030-ai-guide.git](https://github.com/votre-nom/morocco-2030-ai-guide.git)
cd morocco-2030-ai-guide

---

## 3. Installation de l'Environnement et des Dépendances

Il est recommandé d'utiliser un environnement virtuel pour isoler les bibliothèques. À la racine du projet, exécutez la commande suivante pour installer l'ensemble des modules Python requis (TensorFlow, Streamlit, Ollama, Pillow, etc.) :

pip install -r requirements.txt

Ensuite, téléchargez le modèle linguistique français nécessaire au fonctionnement des fonctionnalités de traitement du langage naturel (NLP) via la bibliothèque spaCy :

python -m spacy download fr_core_news_sm

---

## 4. Procédure de Lancement (Double Processus)

L'application s'appuie sur une architecture multimodale qui nécessite l'exécution simultanée du moteur de génération textuelle (Backend LLM) et de l'interface graphique (Frontend Streamlit). Vous devez donc ouvrir **deux terminaux distincts**.

### 🟢 Étape 1 : Initialisation du moteur NLP (Terminal 1)
Dans le premier terminal, lancez le LLM local en exécutant la commande suivante. Laissez impérativement ce terminal ouvert en arrière-plan :

ollama run mistral

*(Note : Lors du tout premier lancement, Ollama téléchargera automatiquement les poids quantifiés du modèle Mistral, ce qui représente un téléchargement d'environ 4 Go).*

### 🔵 Étape 2 : Lancement de l'interface graphique (Terminal 2)
Ouvrez un second terminal, placez-vous à la racine du projet, puis démarrez le serveur applicatif Streamlit :

streamlit run app.py

---

## 🚀 Accès à l'Application

Une fois les deux étapes de lancement validées, le serveur Streamlit initialise le pipeline. L'application s'ouvre automatiquement dans votre navigateur web par défaut. 

Si ce n'est pas le cas, vous pouvez y accéder directement en copiant-collant l'adresse locale suivante dans la barre de recherche de votre navigateur :
👉 **http://localhost:8501**

Vous pouvez désormais téléverser une image de monument pour tester la détection visuelle et interagir en direct avec le guide touristique autonome.
