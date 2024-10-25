# StatCraft-server

## Description

**StatCraft Server** est une application Streamlit permettant de visualiser en temps réel les statistiques des joueurs de Minecraft sur des serveur ayant installé Statcraft. Ce projet aide à analyser l'évolution des performances des joueurs en suivant des métriques telles que le score total, le nombre de blocs minés, les mobs tués, les objets craftés, et le temps de jeu.

## Fonctionnalités

- **Visualisation par Session** : Choisissez une session pour visualiser les performances des joueurs.
- **Graphiques d'Évolution** :
  - Score total
  - Nombre de blocs minés
  - Nombre de mobs tués
  - Nombre d'objets craftés
  - Temps de jeu
- **Interface Interactive** : Utilisation de Streamlit pour une expérience utilisateur intuitive et interactive.

Lien vers le GitHub : [StatCraft](https://github.com/Loutreee/StatCraft)

Lien vers le DockerHub : [StatCraft-Server DockerHub](https://hub.docker.com/r/loutreee/statcraft-server)

## Docker Minecraft-server

Je vous conseille d'utiliser l'image docker de [ITZG](https://hub.docker.com/r/itzg/minecraft-server) et d'incorporer dans le docker compose ceci :

```yml
statcraft-server:
        image: loutreee/statcraft-server
        ports: 
            - 81:8501
        volumes:
            - ./data:/app/data
```

### Tableau des étapes à venir pour l'interface et les graphiques

| **Étape**                                  | **Description**                                                                                                                                           | **Statut**            | **Commentaires**                                                                                                  |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------:|--------------------------------------------------------------------------------------------------------------------|
| **1. Génération des graphiques**           | Générer des graphiques comparant les joueurs individuellement et entre eux.                                                                                | 🟡 | Utilisation de Matplotlib ou Plotly pour créer les PNG des graphs.                                                |
| **2. Envoi des graphiques sur Discord**    | Automatiser l'envoi des PNG des graphiques dans un channel Discord.                                                                                        | 🔜 | Utiliser une bibliothèque Python comme discord.py pour l'envoi.                                                   |
| **3. Dashboard Streamlit**                 | Créer une interface Streamlit pour afficher les statistiques des joueurs, incluant un tableau de bord avec des informations détaillées et la DynMap.        | 🟡 | Streamlit en parallèle du serveur Minecraft pour un accès en temps réel aux stats.                                |
| **4. Intégration des statistiques en direct** | Envisager la récupération des statistiques en temps réel pendant le jeu, pour visualiser l'évolution des stats durant une session en cours.                 | 🔜 | Vérifier la faisabilité technique (accès aux stats via des API pendant le jeu).                                   |
| **5. Comparaison Joueurs & Stats Personnalisées** | Permettre des comparaisons poussées entre joueurs et créer des onglets spécifiques dans Streamlit pour les stats les plus intéressantes.                    | 🔜 | Définir les stats à comparer (ex : minerais minés, monstres tués) et les afficher dans des onglets dédiés.         |

✅ Terminé 🟡 En cours 🔜 À venir
