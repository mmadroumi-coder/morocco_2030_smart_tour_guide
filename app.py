import os
# Ligne de sécurité pour s'assurer que Keras lit bien les anciens formats .h5
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
import json

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Smart Tour Guide 🇲🇦",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. INJECTION CSS : FOND INTENSE ET UI ÉLÉGANTE
# ==========================================
st.markdown("""
<style>
    /* Ajout du drapeau marocain en fond avec un voile blanc réduit (0.65) pour plus d'intensité */
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.65), rgba(255, 255, 255, 0.65)), 
                          url("https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }

    /* Style du titre principal - Noir élégant avec un léger contour blanc pour la lisibilité */
    h1 {
        color: #1a1a1a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.9);
    }
    
    /* En-têtes des sections - Noir charbon */
    h2 {
        color: #222222 !important;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.9);
    }

    /* Boîtes de chat (très opaques et blanches pour compenser le fond plus intense) */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
    }

    /* CORRECTION CRITIQUE : Forcer tout le texte du chat en noir foncé */
    [data-testid="stChatMessage"] * {
        color: #111111 !important;
    }

    /* Bouton principal - Noir, avec un effet Rouge au survol */
    .stButton > button {
        background-color: #222222;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        border: 1px solid #000;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #C1272D;
        color: white;
        border-color: #C1272D;
        box-shadow: 0px 4px 10px rgba(193, 39, 45, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CONSTANTES ET INITIALISATION
# ==========================================
OLLAMA_API_URL = "http://localhost:11434/api/generate"
DOSSIER_COURANT = os.path.dirname(os.path.abspath(__file__))
CHEMIN_MODELE = os.path.join(DOSSIER_COURANT, "modele_monuments_robuste.h5")

CLASSES_MONUMENTS = [
    'Ait Ben Haddou', 'Bab Boujloud', 'Cap Spartel', 'Jemaa el fna', 
    'La Citerne portugaise El Jadida', 'La mosquee Koutoubia', 'Le Palais El Badi', 
    'Mausolee Mohammed V', 'Medersa Attarine', 'Medersa Ben Youssef', 
    'Mosquee Hassan 2', 'Palais Bahia', 'Tannerie Chouara', 'Tombeaux saadiens', 'Volubilis'
]

@st.cache_resource(show_spinner="Chargement du moteur de vision (MobileNetV2)...")
def charger_modele_vision():
    """Charge le modèle TF en mémoire vive une seule fois."""
    try:
        return tf.keras.models.load_model(CHEMIN_MODELE)
    except Exception as e:
        st.error(f"Erreur d'architecture : Impossible de charger {CHEMIN_MODELE}. {e}")
        return None

modele_cv = charger_modele_vision()

def interroger_guide_local(monument, question_utilisateur):
    """Envoie une requête POST au modèle Mistral local via Ollama."""
    prompt_systeme = f"""Tu es un guide touristique marocain expert et officiel pour la Coupe du Monde 2030. 
    Tu te trouves actuellement devant le monument suivant : {monument}. 
    Réponds de manière concise, chaleureuse, historique et factuelle. 
    Ne fais pas d'hallucinations. Si tu ne sais pas, dis-le."""

    prompt_complet = f"{prompt_systeme}\n\nTouriste : {question_utilisateur}\nGuide :"

    payload = {
        "model": "mistral",
        "prompt": prompt_complet,
        "stream": False
    }

    try:
        reponse = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        reponse.raise_for_status()
        return reponse.json().get("response", "Erreur de génération.")
    except requests.exceptions.RequestException as e:
        return f"Erreur de communication avec le LLM local. Ollama est-il démarré ? ({e})"

# ==========================================
# 4. INTERFACE UTILISATEUR : ACCUEIL
# ==========================================
st.title("🇲🇦 Bienvenue sur Smart Tour Guide")

# Paragraphe d'explication
st.markdown("""
<div style='background-color: rgba(255, 255, 255, 0.92); padding: 20px; border-radius: 10px; border-left: 5px solid #222222; margin-bottom: 30px; font-size: 1.1rem; color: #111; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);'>
    <strong>Découvrez le patrimoine marocain grâce à l'Intelligence Artificielle !</strong><br>
    Prenez en photo ou chargez l'image d'un monument historique. Notre système d'analyse visuelle l'identifiera instantanément. 
    Notre guide virtuel prendra ensuite le relais pour vous présenter son histoire et répondre à toutes vos questions en direct, afin d'enrichir votre expérience de la Coupe du Monde 2030.
</div>
""", unsafe_allow_html=True)


col_vision, col_nlp = st.columns([1, 1], gap="large")

with col_vision:
    st.header("📸 1. Identifier un monument")
    
    methode_upload = st.radio("Source de l'image :", ["📂 Fichier local", "📷 Caméra"], horizontal=True)
    fichier_image = None
    
    if methode_upload == "📷 Caméra":
        fichier_image = st.camera_input("Prenez une photo du monument")
    else:
        fichier_image = st.file_uploader("Charger une image (JPG/PNG)", type=["jpg", "jpeg", "png"])
    
    if fichier_image is not None:
        image_pil = Image.open(fichier_image).convert("RGB")
        st.image(image_pil, caption="Image à analyser", use_column_width=True)
        
        if st.button("Analyser l'image", type="primary"):
            if modele_cv is not None:
                with st.spinner("Analyse visuelle en cours..."):
                    # Prétraitement brut (la normalisation est déjà dans le .h5)
                    img_redimensionnee = image_pil.resize((224, 224))
                    img_array = tf.keras.preprocessing.image.img_to_array(img_redimensionnee)
                    img_array = tf.expand_dims(img_array, 0)

                    predictions = modele_cv.predict(img_array)
                    index_gagnant = np.argmax(predictions[0])
                    confiance = predictions[0][index_gagnant] * 100
                    
                    monument_detecte = CLASSES_MONUMENTS[index_gagnant]
                    
                    # Mise à jour de la session
                    st.session_state['monument_actuel'] = monument_detecte
                    
                    st.success(f"**Monument identifié : {monument_detecte}** (Fiabilité : {confiance:.1f}%)")
            else:
                st.error("Le moteur de vision est hors service.")

with col_nlp:
    st.header("🧠 2. Guide Interactif")
    
    if 'monument_actuel' in st.session_state:
        monument_cible = st.session_state['monument_actuel']
        
        # LOGIQUE D'AUTOMATISATION : Si c'est un nouveau monument, on réinitialise et on génère l'intro
        if st.session_state.get('dernier_monument') != monument_cible:
            st.session_state.messages = [] # On vide l'ancien chat
            st.session_state['dernier_monument'] = monument_cible # On met à jour la mémoire
            
            with st.spinner(f"Le guide prépare sa présentation pour {monument_cible}..."):
                prompt_intro = f"Fais une très brève présentation (3 phrases maximum) du monument '{monument_cible}' pour accueillir le touriste et donne-lui envie de te poser des questions."
                reponse_intro = interroger_guide_local(monument_cible, prompt_intro)
                st.session_state.messages.append({"role": "assistant", "content": reponse_intro})
        
        # Affichage de l'historique des messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Champ de texte pour les questions de l'utilisateur
        question = st.chat_input(f"Posez une question sur {monument_cible}...")
        
        if question:
            with st.chat_message("user"):
                st.markdown(question)
            st.session_state.messages.append({"role": "user", "content": question})

            with st.chat_message("assistant"):
                with st.spinner("Le guide réfléchit..."):
                    reponse_llm = interroger_guide_local(monument_cible, question)
                    st.markdown(reponse_llm)
            st.session_state.messages.append({"role": "assistant", "content": reponse_llm})
            
    else:
        st.info("👈 Chargez une image à gauche pour réveiller le guide touristique.")