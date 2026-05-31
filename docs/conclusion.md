# 🏁 Conclusion et Perspectives

Le projet **Smart Tour Guide** démontre avec succès la viabilité d'une architecture d'Intelligence Artificielle multimodale exécutée de bout en bout en local (Edge AI). 

En fusionnant la Vision par Ordinateur (MobileNetV2) et le Traitement du Langage Naturel (Mistral via Ollama) au sein d'une interface unifiée (Streamlit), ce Proof of Concept (PoC) apporte une réponse concrète aux défis d'infrastructure réseau et de confidentialité liés à l'organisation de la Coupe du Monde 2030.

---

## 📈 Bilan du Proof of Concept (PoC)

Les objectifs initiaux ont été atteints :
1. **Zéro Latence Réseau :** L'application fonctionne sans aucune connexion internet, garantissant son utilisabilité dans les médinas denses ou les stades saturés.
2. **Confidentialité Totale :** Les photos et les données conversationnelles des touristes ne quittent jamais leur appareil.
3. **Synergie Multimodale :** L'automatisation du transfert de contexte entre la vision (ce que l'utilisateur voit) et le LLM (ce dont le guide parle) offre une expérience utilisateur fluide et immersive.

---

## 🚀 Perspectives d'Évolution (Travaux Futurs)

Pour transformer ce prototype en une application grand public déployable à l'échelle nationale pour 2030, plusieurs axes d'amélioration ont été identifiés :

### 1. Scalabilité du Modèle de Vision
* **Extension du Dataset :** Passer de 15 classes à plus de 100 classes pour couvrir l'intégralité du patrimoine architectural marocain officiel.
* **Format Mobile :** Convertir le fichier `.h5` actuel au format **TensorFlow Lite (.tflite)** ou **ONNX** pour permettre un déploiement natif sur les puces (NPU) des smartphones Android et iOS.

### 2. Accessibilité et Multilinguisme
* **Synthèse Vocale (Text-to-Speech) :** Intégrer un module TTS local pour que le guide puisse "lire" ses réponses à voix haute. Le touriste pourrait ainsi écouter l'histoire du monument tout en continuant à le regarder, sans avoir les yeux rivés sur son écran.
* **Support Multilingue :** Profiter des capacités natives de Mistral pour détecter la langue de la question (Anglais, Espagnol, etc.) et répondre dans cette même langue, une nécessité absolue pour un événement international (co-organisé avec l'Espagne et le Portugal).

### 3. RAG (Retrieval-Augmented Generation)
* Pour éviter toute hallucination résiduelle, il serait pertinent de coupler Mistral à une base de données vectorielle locale (ChromaDB ou FAISS) contenant les archives officielles du Ministère du Tourisme. Ainsi, le modèle fonderait ses réponses exclusivement sur des documents certifiés.

---

*Projet conçu et développé par **Mohamed Madroumi**, élève-ingénieur en Intelligence Artificielle et Technologies de Données pour les Systèmes Industriels (IATDSI) à l'ENSAM de Meknès.*
