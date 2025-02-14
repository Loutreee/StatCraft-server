import streamlit as st
import os
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Chemins des données et fichier de configuration
data_path = "./data/player_statistics"
server_mode_file = "./data/plugins/StatCraft/server_info/server_mode.xml"

# Déterminer le mode du serveur (Hardcore ou Survie)
if os.path.exists(server_mode_file):
    with open(server_mode_file, "r") as file:
        server_mode = file.read().strip()
else:
    st.error("Fichier 'server_mode' introuvable. Veuillez vérifier.")
    st.stop()

is_hardcore = server_mode.lower() == "hardcore"

# Titre de l'application
st.title("Statistiques des joueurs - Minecraft")

if is_hardcore:
    st.subheader("Mode Hardcore activé")
    # Charger les sessions disponibles
    sessions = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
    selected_session = st.selectbox("Sélectionnez une session", sessions)
else:
    st.subheader("Mode Survie activé")
    selected_session = "session0"
    session_path = os.path.join(data_path, selected_session)
    if not os.path.exists(session_path):
        st.error(f"La session par défaut '{selected_session}' est introuvable.")
        st.stop()

# Chargement des joueurs dans la session sélectionnée
session_path = os.path.join(data_path, selected_session)
players = [f for f in os.listdir(session_path) if os.path.isdir(os.path.join(session_path, f))]
selected_player = st.selectbox("Sélectionnez un joueur", players)

if selected_player:
    player_path = os.path.join(session_path, selected_player)
    xml_files = sorted([f for f in os.listdir(player_path) if f.endswith(".xml")])

    # Initialisation des listes pour chaque statistique de score
    dates, global_scores, blocks_scores, mobs_scores, crafts_scores = [], [], [], [], []

    for xml_file in xml_files:
        file_path = os.path.join(player_path, xml_file)
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Récupérer la date du nom du fichier
        date = xml_file.replace(".xml", "")
        dates.append(date)

        # Extraire les scores à partir des balises <score>
        score_total = int(root.find("scoreTotal").text)
        blocks_score = int(root.find("blocsMines/score").text)
        mobs_score = int(root.find("mobsTues/score").text)
        crafts_score = int(root.find("objetsCraftes/score").text)

        global_scores.append(score_total)
        blocks_scores.append(blocks_score)
        mobs_scores.append(mobs_score)
        crafts_scores.append(crafts_score)

    # Créer un DataFrame pour organiser les données
    df = pd.DataFrame({
        "Date": dates,
        "Score Global": global_scores,
        "Score Blocs": blocks_scores,
        "Score Mobs": mobs_scores,
        "Score Crafts": crafts_scores
    })

    # Conversion de la colonne Date en datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d_%H-%M-%S")
    df = df.sort_values("Date")

    st.write(f"Statistiques de score pour le joueur **{selected_player}**")

    # Graphique Score Global
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Score Global"], label="Score Global")
    ax.set_title(f"Évolution du Score Global pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score Global")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique Score Blocs
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Score Blocs"], color="orange", label="Score Blocs")
    ax.set_title(f"Évolution du Score Blocs pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score Blocs")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique Score Mobs
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Score Mobs"], color="red", label="Score Mobs")
    ax.set_title(f"Évolution du Score Mobs pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score Mobs")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique Score Crafts
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Score Crafts"], color="green", label="Score Crafts")
    ax.set_title(f"Évolution du Score Crafts pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score Crafts")
    ax.grid(True)
    st.pyplot(fig)
