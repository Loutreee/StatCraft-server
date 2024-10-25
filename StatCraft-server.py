import streamlit as st

# Titre de l'application
st.title("Serveur Streamlit Simple")

# Texte de bienvenue
st.write("Bienvenue sur ce serveur Streamlit !")

# Saisie d'entrée utilisateur
name = st.text_input("Entrez votre nom", "")

# Affichage d'un message de bienvenue personnalisé
if name:
    st.write(f"Bonjour, {name} ! Ravi de vous voir ici.")

# Exemple d'un slider pour sélectionner un nombre
number = st.slider("Choisissez un nombre", 0, 100, 25)
st.write(f"Vous avez sélectionné le nombre : {number}")
