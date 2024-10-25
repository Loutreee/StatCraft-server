import streamlit as st
import os
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Définir le chemin des données
data_path = "./data/player_statistics"

# Charger les sessions disponibles
sessions = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]

st.title("Statistiques des joueurs - Minecraft Hardcore Party")

# Menu principal : Boutons pour chaque session
selected_session = st.selectbox("Sélectionnez une session", sessions)

if selected_session:
    session_path = os.path.join(data_path, selected_session)
    players = [f for f in os.listdir(session_path) if os.path.isdir(os.path.join(session_path, f))]

    # Boutons pour chaque joueur dans la session sélectionnée
    selected_player = st.selectbox("Sélectionnez un joueur", players)

    if selected_player:
        player_path = os.path.join(session_path, selected_player)
        xml_files = sorted([f for f in os.listdir(player_path) if f.endswith(".xml")])

        # Lire les fichiers XML et extraire les données de score et de date
        scores = []
        dates = []

        for xml_file in xml_files:
            file_path = os.path.join(player_path, xml_file)
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Récupérer la date du nom du fichier
            date = xml_file.replace(".xml", "")
            dates.append(date)
            
            # Extraire le score total
            score_total = int(root.find("scoreTotal").text)
            scores.append(score_total)

        # Créer un DataFrame pour organiser les données
        df = pd.DataFrame({"Date": dates, "Score": scores})
        # Convertir les dates en format date/heure avec le format spécifié
        df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d_%H-%M-%S")
        # Convertir en format date
        df = df.sort_values("Date")

        # Afficher le graphique d'évolution du score
        st.write(f"Évolution du score pour le joueur {selected_player}")
        plt.figure(figsize=(10, 5))
        plt.plot(df["Date"], df["Score"], marker="o")
        plt.title(f"Évolution du score pour {selected_player}")
        plt.xlabel("Date")
        plt.ylabel("Score")
        plt.grid(True)
        st.pyplot(plt)
