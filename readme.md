# 🇲🇦 Smart Tour Guide | Edge AI for Morocco 2030

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00.svg?logo=tensorflow)
![Ollama](https://img.shields.io/badge/Ollama-Mistral_Local-white.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?logo=streamlit)

> **Un compagnon de voyage autonome et 100% hors-ligne, propulsé par l'Intelligence Artificielle.**

## 🌍 Contexte : Coupe du Monde 2030
Dans le cadre de l'organisation de la Coupe du Monde de la FIFA 2030, le Maroc s'apprête à accueillir des millions de visiteurs. Le **Smart Tour Guide** est une preuve de concept (PoC) d'une application touristique intelligente. Conçue en **Edge AI** (traitement en local), elle permet aux touristes d'identifier instantanément le patrimoine marocain et d'interagir avec un guide virtuel, même sans connexion internet (idéal pour les zones denses ou le roaming coûteux).

---

## ✨ Fonctionnalités Principales

* 👁️ **Vision par Ordinateur (Reconnaissance en Temps Réel) :** Prenez une photo ou chargez l'image d'un monument. Le réseau de neurones l'analyse et l'identifie parmi 15 sites historiques marocains majeurs.
* 🧠 **Guide Interactif Autonome (NLP) :** Une fois le monument identifié, un agent conversationnel prend le relais. Il présente le site de manière proactive et répond aux questions de l'utilisateur avec des faits historiques précis.
* 🎨 **Interface Immersive (UI/UX) :** Un tableau de bord ergonomique et responsive, conçu aux couleurs de la charte nationale marocaine.
* 🔒 **100% Privacy & Offline :** Aucune donnée, photo ou conversation n'est envoyée sur le cloud. Tout est traité sur la machine physique.

---

## 🏗️ Architecture Technique (Pipeline Multimodal)

Le projet fusionne deux champs majeurs de l'Intelligence Artificielle :

1. **Moteur de Vision (MobileNetV2) :** * Modèle de classification d'images optimisé pour les terminaux légers.
   * Entraîné spécifiquement sur un dataset de monuments marocains (Koutoubia, Bab Boujloud, Volubilis, etc.).
   * *Format : `modele_monuments_robuste.h5` lu via TensorFlow/Keras (Legacy mode).*

2. **Moteur de Langage (LLM Local) :**
   * Modèle **Mistral** quantifié, exécuté en local via le serveur **Ollama**.
   * Prompt system strict pour garantir des réponses historiques factuelles (Zéro hallucination) et un ton chaleureux.

3. **Interface Utilisateur :**
   * Déployée en Python pur via **Streamlit**.
   * Injection CSS personnalisée pour le support de thèmes visuels avancés.

---

## 📸 Démonstration


<img width="1864" height="859" alt="dashbord" src="https://github.com/user-attachments/assets/de0bbf91-f78d-4513-ba29-8b3bd5e198fd" />


---

## 🚀 Installation & Déploiement

L'application nécessite une configuration spécifique pour garantir la compatibilité des moteurs C++ sous-jacents. 

👉 **Veuillez consulter le [Guide d'Installation Complet (install.md)](install.md) pour la procédure étape par étape.**

---

## 👨‍💻 Développé par
**Mohamed** Madroumi  
*Élève Ingénieur en Intelligence Artificielle et Technologies de Données pour les Systèmes Industriels (IATDSI) - ENSAM.*
