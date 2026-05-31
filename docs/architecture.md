# 🔄 Intégration et Architecture Globale

Le défi principal du **Smart Tour Guide** n'est pas seulement de faire fonctionner un modèle de Vision et un LLM isolément, mais de les faire communiquer de manière asynchrone et fluide au sein d'une même interface. 

Ce chapitre détaille l'orchestration logicielle du projet.

---

## 🏗️ Streamlit comme Chef d'Orchestre

L'interface utilisateur et la logique d'intégration sont gérées par **Streamlit**, un framework Python conçu spécifiquement pour le déploiement rapide d'applications de Machine Learning.

Streamlit a été choisi pour plusieurs raisons :
1. **Full-Python :** Il permet de concevoir le front-end et le back-end dans un seul et même langage, facilitant l'intégration directe des tenseurs TensorFlow.
2. **Réactivité (Responsive Design) :** L'interface s'adapte automatiquement aux écrans d'ordinateurs et de smartphones (grâce à la gestion en colonnes `st.columns`).
3. **Injections CSS :** Bien que natif en Python, Streamlit autorise l'injection de code CSS personnalisé (utilisé ici pour appliquer la charte graphique marocaine rouge, verte et noire de manière élégante).

---

## 🧠 Le Pont Multimodal : Le "Session State"

Comment le modèle de langage (à droite) sait-il ce que le modèle de vision (à gauche) vient de voir ? 
La réponse réside dans la gestion de l'état de l'application via le **`st.session_state`**.

Dans une application web classique, chaque rechargement de page efface les variables. Streamlit utilise le `session_state` pour conserver la mémoire des interactions de l'utilisateur.

**Le flux de données (Data Flow) s'opère ainsi :**
1. L'image passe dans `MobileNetV2`.
2. Le modèle retourne une chaîne de caractères (ex: `"Volubilis"`).
3. Cette donnée est immédiatement sauvegardée en mémoire globale : 
   `st.session_state['monument_actuel'] = "Volubilis"`
4. Le module NLP "écoute" en permanence cette variable. Dès qu'elle est mise à jour, la colonne de droite se débloque, génère le prompt système avec le nouveau monument, et initie la conversation de manière autonome.

---

## ⏳ Gestion de la Latence et UX Asynchrone

L'exécution de modèles d'Intelligence Artificielle en local (Edge AI) sollicite fortement le processeur (CPU). Pour éviter que l'application ne semble "figée" ou plantée pendant l'inférence :

* **Mise en cache du modèle lourd :** Le décorateur `@st.cache_resource` garantit que les poids du réseau de neurones (`modele_monuments_robuste.h5`) ne sont chargés dans la RAM qu'au tout premier lancement.
* **Retours Visuels (Feedback) :** L'utilisation de `st.spinner()` informe l'utilisateur en temps réel ("*Analyse visuelle en cours...*" ou "*Le guide réfléchit...*"), ce qui améliore considérablement l'expérience utilisateur (UX) pendant que TensorFlow ou Ollama calculent.

---

## 📊 Schéma Conceptuel du Pipeline

1. **Input Utilisateur** ➡️ (Image)
2. **Backend Vision** ➡️ (Prétraitement TF ➡️ Inférence MobileNetV2 ➡️ Extraction Classe)
3. **Mémoire Globale** ➡️ (Mise à jour du `session_state`)
4. **Backend NLP** ➡️ (Génération Prompt ➡️ Requête POST Ollama/Mistral ➡️ Réponse JSON)
5. **Output Utilisateur** ➡️ (Affichage de l'historique du Chat)
