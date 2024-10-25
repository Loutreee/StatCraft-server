# StatCraft-server

StatCraft-server est un interface web qui se lance en simultané d'un serveur Minecraft sur lequel le plugin StatCraft est installé. Il permet de faire un affichage dynamique des statistiques des joueurs en fonction de différents mode de jeu.

Lien vers le GitHub : [StatCraft](https://github.com/Loutreee/StatCraft)

### Tableau des étapes à venir pour l'interface et les graphiques

| **Étape**                                  | **Description**                                                                                                                                           | **Statut**            | **Commentaires**                                                                                                  |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------:|--------------------------------------------------------------------------------------------------------------------|
| **1. Génération des graphiques**           | Générer des graphiques comparant les joueurs individuellement et entre eux.                                                                                | 🟡 | Utilisation de Matplotlib ou Plotly pour créer les PNG des graphs.                                                |
| **2. Envoi des graphiques sur Discord**    | Automatiser l'envoi des PNG des graphiques dans un channel Discord.                                                                                        | 🔜 | Utiliser une bibliothèque Python comme discord.py pour l'envoi.                                                   |
| **3. Dashboard Streamlit**                 | Créer une interface Streamlit pour afficher les statistiques des joueurs, incluant un tableau de bord avec des informations détaillées et la DynMap.        | 🟡 | Streamlit en parallèle du serveur Minecraft pour un accès en temps réel aux stats.                                |
| **4. Intégration des statistiques en direct** | Envisager la récupération des statistiques en temps réel pendant le jeu, pour visualiser l'évolution des stats durant une session en cours.                 | 🔜 | Vérifier la faisabilité technique (accès aux stats via des API pendant le jeu).                                   |
| **5. Comparaison Joueurs & Stats Personnalisées** | Permettre des comparaisons poussées entre joueurs et créer des onglets spécifiques dans Streamlit pour les stats les plus intéressantes.                    | 🔜 | Définir les stats à comparer (ex : minerais minés, monstres tués) et les afficher dans des onglets dédiés.         |
✅ Terminé 🟡 En cours 🔜 À venir
