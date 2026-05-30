# Moroccan Smart Tour Guide — AI for Morocco 2030

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama)

---

## 🎯 Problématique & Vision

À l'horizon de la **Coupe du Monde 2030**, le Maroc s'apprête à accueillir des millions de visiteurs internationaux. Face à cet afflux massif, l'accès à une information culturelle et historique fiable présente trois défis majeurs :
* **La barrière linguistique et la saturation des guides physiques** sur les sites historiques.
* **La dépendance aux réseaux internet (Roaming/4G)**, souvent coûteuse, instable ou inexistante à l'intérieur de certains monuments (murs épais, zones reculées).
* **Le manque d'interactivité** des supports touristiques classiques (brochures, panneaux fixes).

**La solution :** `Smart Tour Guide` résout cette problématique en proposant un **compagnon de voyage multimodal fonctionnant à 100% en local (Edge AI)**. L'application combine la puissance de la vision par ordinateur et de l'IA générative locale pour transformer une simple photo prise par un touriste en une expérience éducative interactive et immédiate, sans aucune connexion internet requise.

---

## 🧠 Architecture Technique

Le projet repose sur l'intégration et la fusion de deux piliers majeurs de l'Intelligence Artificielle :

### 1. Pilier Computer Vision 
* **Architecture & Transfer Learning :** Utilisation du modèle `MobileNetV2`, optimisé pour l'inférence sur des appareils locaux.
* **Pipeline de Prétraitement Robuste :** Intégration de couches de normalisation (`Rescaling`) et de `Data Augmentation` directement au sein du graphe du modèle pour maximiser la robustesse face aux variations de luminosité et d'angle de vue.

### 2. Pilier Natural Language Processing (Génération Locale)
* **Inférence Edge-AI :** Déploiement du LLM `Mistral` en local via le moteur `Ollama`.
* **Prompt Engineering Avancé :** Structuration des directives système pour forcer le modèle à adopter un rôle d'historien expert, éliminer les risques d'hallucinations factuelles et calibrer les réponses selon le contexte de l'événement Maroc 2030.

### 3. Interface Utilisateur (UI/UX)
* Déploiement d'un tableau de bord réactif avec `Streamlit`, personnalisé aux couleurs de la charte nationale pour offrir une expérience immersive et fluide adaptée aux terminaux mobiles et ordinateurs portables.

---

## 🎬 Démonstration Visuelle

*(Glissez ici une capture d'écran de l'application Streamlit ou un GIF animé de démonstration)*
![Aperçu de l'application](https://images.unsplash.com/photo-1539667468225-eebb663053e6?auto=format&fit=crop&w=800&q=80)

---

## 🚀 Démarrage & Installation

Pour tester l'application sur votre machine (déploiement local), veuillez consulter le guide détaillé étape par étape :
👉 **[Lire le guide d'installation (INSTALL.md)](INSTALL.md)**

---

*Projet réalisé par **Mohammed Madroumi** dans le cadre du la premiére année du cycle d'ingénieur en 	Intelligence Artificielle et Technologies des Données : Systèmes Industriels (IATDSI) - ENSAM Meknès.*
