import streamlit as st
import os
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Chemins des données et fichier de configuration
data_path = "./data/player_statistics"
server_mode_file = "./data/server_mode"

# Déterminer le mode du serveur (Hardcore ou Survie)
if os.path.exists(server_mode_file):
    with open(server_mode_file, "r") as file:
        server_mode = file.read().strip()
else:
    st.error("Fichier 'server_mode' introuvable. Veuillez vérifier.")
    st.stop()

is_hardcore = server_mode.lower() == "hardcore"

# Titre de l'application
st.title("Statistiques des joueurs - Minecraft Hardcore test")

if is_hardcore:
    # Afficher un message pour le mode Hardcore
    st.subheader("Mode Hardcore activé")
    # Charger les sessions disponibles
    sessions = [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]
    selected_session = st.selectbox("Sélectionnez une session", sessions)
else:
    # Mode Survie : prendre la session par défaut
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

    # Initialisation des listes pour chaque statistique
    dates, scores, blocks_mined, mobs_killed, items_crafted, play_time = [], [], [], [], [], []

    for xml_file in xml_files:
        file_path = os.path.join(player_path, xml_file)
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Récupérer la date du nom du fichier
        date = xml_file.replace(".xml", "")
        dates.append(date)

        # Extraire les différentes statistiques
        score_total = int(root.find("scoreTotal").text)
        total_blocks_mined = int(root.find("blocsMines/totalBlocsMines").text)
        total_mobs_killed = int(root.find("mobsTues/totalMobsTues").text)
        total_items_crafted = int(root.find("objetsCraftes/totalObjetsCraftes").text)
        total_play_time = int(root.find("tempsDeJeu").text)

        # Ajouter les statistiques aux listes
        scores.append(score_total)
        blocks_mined.append(total_blocks_mined)
        mobs_killed.append(total_mobs_killed)
        items_crafted.append(total_items_crafted)
        play_time.append(total_play_time)

    # Créer un DataFrame pour organiser les données
    df = pd.DataFrame({
        "Date": dates,
        "Score": scores,
        "Total Blocs Minés": blocks_mined,
        "Total Mobs Tués": mobs_killed,
        "Total Objets Craftés": items_crafted,
        "Temps de Jeu": play_time
    })
    # Convertir les dates en format date/heure avec le format spécifié
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d_%H-%M-%S")
    df = df.sort_values("Date")

    # Afficher les graphiques
    st.write(f"Statistiques pour le joueur {selected_player}")

    # Graphique pour le score
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Score"], marker="o", label="Score")
    ax.set_title(f"Évolution du score pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Score")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique pour le total des blocs minés
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Total Blocs Minés"], marker="o", color="orange", label="Total Blocs Minés")
    ax.set_title(f"Évolution des blocs minés pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Blocs Minés")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique pour le total des mobs tués
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Total Mobs Tués"], marker="o", color="red", label="Total Mobs Tués")
    ax.set_title(f"Évolution des mobs tués pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Mobs Tués")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique pour le total des objets craftés
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Total Objets Craftés"], marker="o", color="green", label="Total Objets Craftés")
    ax.set_title(f"Évolution des objets craftés pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Objets Craftés")
    ax.grid(True)
    st.pyplot(fig)

    # Graphique pour le temps de jeu
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Date"], df["Temps de Jeu"], marker="o", color="purple", label="Temps de Jeu")
    ax.set_title(f"Évolution du temps de jeu pour {selected_player}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temps de Jeu (minutes)")
    ax.grid(True)
    st.pyplot(fig)
