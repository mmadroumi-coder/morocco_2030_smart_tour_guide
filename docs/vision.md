# 👁️ Module de Vision par Ordinateur (Computer Vision)

Le module de Vision par Ordinateur constitue le premier pilier de l'application **Smart Tour Guide**. Il agit comme les "yeux" du système, permettant à la machine de comprendre l'environnement de l'utilisateur en identifiant le monument photographié.

---

## 🏗️ L'Architecture du Modèle : MobileNetV2

Pour relever le défi d'une exécution 100% hors-ligne (Edge AI) sans sacrifier la précision, le choix de l'architecture du réseau de neurones convolutifs (CNN) s'est porté sur **MobileNetV2**.

### Pourquoi MobileNetV2 ?
Dans un contexte de déploiement local (sur des ordinateurs portables ou, à terme, des terminaux mobiles), les modèles massifs (comme VGG16 ou ResNet152) sont trop gourmands en mémoire vive et en puissance de calcul (GPU). 

MobileNetV2 contourne ce problème grâce à deux innovations mathématiques majeures :
1. **Les Convolutions Séparables en Profondeur (Depthwise Separable Convolutions) :** Elles séparent le filtrage spatial de la combinaison des canaux, ce qui réduit drastiquement le nombre de paramètres et les calculs nécessaires.
2. **Les Blocs Résiduels Inversés (Inverted Residuals) :** Ils permettent de compresser les données tout en préservant les informations essentielles pour la classification.

*Résultat :* Un modèle extrêmement léger et rapide, capable de réaliser des inférences en temps réel sur un simple CPU, idéal pour les contraintes du tourisme de masse lors de la Coupe du Monde 2030.

---

## 🏛️ Le Jeu de Données (Dataset)

Le modèle a été entraîné spécifiquement sur un jeu de données marocain pour reconnaître **15 classes distinctes** représentant la richesse du patrimoine national :

* **Patrimoine Historique & Médinas :** Ait Ben Haddou, Bab Boujloud, Jemaa el fna, Volubilis, Tannerie Chouara.
* **Édifices Religieux & Éducatifs :** Mosquée Hassan 2, Mosquée Koutoubia, Medersa Attarine, Medersa Ben Youssef.
* **Palais & Mausolées :** Palais Bahia, Palais El Badi, Mausolée Mohammed V, Tombeaux Saadiens.
* **Sites Côtiers :** Cap Spartel, La Citerne portugaise d'El Jadida.

---

## ⚙️ Le Pipeline d'Inférence (Prétraitement)

Pour qu'une image capturée par le touriste (via sa webcam ou son téléphone) soit comprise par le modèle, elle passe par un pipeline de prétraitement strict, intégré directement dans l'interface Streamlit :

1. **Capture et Instanciation :** L'image brute est convertie au format standard RGB via la bibliothèque `Pillow`.
2. **Redimensionnement (Resizing) :** Le tenseur d'entrée de MobileNetV2 exige une taille fixe. L'image est redimensionnée en `224x224 pixels`.
3. **Vectorisation (Array Conversion) :** L'image est transformée en une matrice mathématique (`img_to_array`) lisible par TensorFlow.
4. **Mise en Lot (Batching) :** Keras attend toujours un "lot" (batch) d'images. On ajoute donc une dimension artificielle (`expand_dims`) pour transformer la forme de `(224, 224, 3)` à `(1, 224, 224, 3)`.
5. **Inférence & Confiance :** Le modèle calcule les probabilités (Softmax) pour les 15 classes. La fonction `argmax` extrait la classe gagnante, et le score de probabilité est converti en pourcentage de fiabilité.

---

## ⚡ L'Avantage "Edge AI" dans le code

Pour garantir une expérience utilisateur fluide, le modèle `.h5` (sauvegardé sur le disque) est chargé **une seule fois** dans la mémoire cache (RAM) de l'application grâce au décorateur `@st.cache_resource` de Streamlit. 

Ainsi, lorsque l'utilisateur prend plusieurs photos d'affilée, le temps d'attente est quasi nul, car le système n'a pas besoin de recharger les poids du réseau de neurones à chaque prédiction.
