# 🧠 Module de Langage Naturel (NLP)

Une fois que le module de Vision par Ordinateur a identifié le monument, le relais est passé au module de Traitement du Langage Naturel (NLP). Ce système agit comme le "cerveau analytique" et la "voix" du guide, permettant une interaction fluide et naturelle avec le touriste.

---

## 🤖 Le Modèle : Mistral via Ollama

Dans le respect de notre contrainte architecturale **Edge AI** (100% local et hors-ligne), l'utilisation d'une API cloud tierce (comme OpenAI GPT-4) était exclue.

Le choix s'est donc porté sur le modèle **Mistral**, exécuté localement grâce au moteur d'inférence **Ollama**. 
* **Pourquoi Mistral ?** C'est un modèle de langage (LLM) extrêmement performant pour sa taille. Grâce à la quantification (réduction de la précision des poids du modèle pour économiser la mémoire), il peut générer du texte de haute qualité en temps réel sur une machine standard, sans nécessiter de GPU de centre de données.
* **Le rôle d'Ollama :** Ollama encapsule le modèle Mistral et l'expose comme une API web locale (`http://localhost:11434`), rendant la communication avec notre script Python extrêmement simple.

---

## 🛠️ Ingénierie de Prompt (Prompt Engineering)

La qualité des réponses d'un LLM dépend entièrement de la façon dont on le conditionne. Pour garantir que le modèle agit comme un véritable guide touristique fiable et non comme un simple robot de discussion, un **Prompt Système** strict a été mis en place.

Voici le cœur logique injecté à chaque requête :

> *"Tu es un guide touristique marocain expert et officiel pour la Coupe du Monde 2030. Tu te trouves actuellement devant le monument suivant : **{monument_detecte}**. Réponds de manière concise, chaleureuse, historique et factuelle. Ne fais pas d'hallucinations. Si tu ne sais pas, dis-le."*

**Points clés de ce prompt :**
1. **Persona & Contexte :** Définit le rôle (guide officiel) et l'événement (Coupe du Monde 2030).
2. **Injection Dynamique :** La variable `{monument_detecte}` est remplacée en temps réel par le résultat de la prédiction du modèle de vision (ex: *Bab Boujloud*). Le LLM "sait" ainsi exactement de quoi il doit
