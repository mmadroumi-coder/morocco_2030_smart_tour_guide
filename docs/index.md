# 🇲🇦 Smart Tour Guide : L'IA au service du patrimoine

Bienvenue dans la documentation officielle du projet **Smart Tour Guide**, une application hybride d'Intelligence Artificielle développée pour enrichir l'expérience touristique au Maroc.

---

## 🌍 La Problématique : L'horizon de la Coupe du Monde 2030

En 2030, le Maroc co-organisera la Coupe du Monde de la FIFA, un événement historique qui attirera des millions de visiteurs internationaux. Cette affluence massive soulève un défi technologique majeur concernant l'accompagnement touristique :

1. **La barrière de l'information :** Comment fournir aux touristes une information historique fiable et instantanée sur les monuments qu'ils visitent ?
2. **La contrainte réseau :** Dans des zones à très forte densité de population (stades, médinas, places publiques), les réseaux mobiles sont souvent saturés. De plus, les frais d'itinérance (roaming) peuvent dissuader les visiteurs d'utiliser des applications cloud classiques.

---

## 💡 La Solution : Une approche "Edge AI"

Pour répondre à ces défis, j'ai conçu le **Smart Tour Guide**. Il s'agit d'un compagnon de voyage virtuel, intelligent et autonome, pensé spécifiquement pour le contexte marocain. 

La force majeure de cette architecture réside dans son déploiement en **Edge AI** (Intelligence Artificielle embarquée). Contrairement aux solutions traditionnelles qui envoient les données sur des serveurs distants, l'intégralité des calculs (reconnaissance visuelle et génération de texte) s'effectue **localement sur la machine de l'utilisateur**. 

Cela garantit une expérience 100% hors-ligne, sans temps de latence lié au réseau, et avec un respect total de la vie privée des touristes.

---

## ✨ Fonctionnalités Principales

L'application se divise en deux flux d'interaction fluides et automatisés :

* 👁️ **Scan et Reconnaissance Visuelle :** L'utilisateur prend une photo (ou charge une image) d'un site historique. L'application identifie instantanément le monument parmi 15 classes du patrimoine marocain (Koutoubia, Volubilis, Bab Boujloud, etc.).
* 🧠 **Guide Virtuel Interactif :** Dès que le monument est identifié, un agent conversationnel s'active de manière proactive pour présenter le lieu. Le touriste peut ensuite poser toutes ses questions en langage naturel et obtenir des réponses factuelles et historiques.

---

## 📸 Aperçu de l'Interface

L'interface graphique a été développée pour être intuitive, ergonomique, et rappeler visuellement la charte graphique marocaine.

> **1. Détection Visuelle**
> 
> *Le module de vision analyse l'image capturée et affiche le niveau de confiance de la prédiction.*
> 
<img width="949" height="775" alt="Screenshot 2026-05-31 161413" src="https://github.com/user-attachments/assets/f5c4af11-524f-4795-80ac-14c99523c283" />

> **2. Interaction avec le Guide**
> 
> *Le module linguistique prend le relais dans un format "chat" classique et interactif.*
> 
<img width="904" height="838" alt="Screenshot 2026-05-31 160143" src="https://github.com/user-attachments/assets/b04be4e7-03f5-470b-b523-41005fe1e1e9" />

---

*Dans les chapitres suivants, nous plongerons dans l'architecture technique de cette solution, en explorant d'abord le fonctionnement du modèle de Vision par Ordinateur, puis celui du moteur de Traitement du Langage Naturel.*
