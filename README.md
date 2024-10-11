créer un environnement virtuel .venv
activer le avec la commande .\.venv\Scripts\activate
deactivate ; pour le désactiver
dans ce .venv, installer les dépendances (framwork et bibliothèques)
ex : pip install matplotlib
reprendre les dépendances dans une autre machine : pip install -r requirements.txt


1ère partie: Introduction et récupération des données des prix de la bourse (Tesla, Apple...)
Nous avons crée des variables de dates représentant le départ 1er janvier 2000 et de fin 31 décembre 2016
Puis nous avons récupérer des données de sociétés (Apple, Tesla) grâce à des API.
Nous les représentons par un graphique pour mieux les analyser

2ème partie: Gestion des données et conception des graphiques
Lecture des Données : Importation des données boursières de Tesla depuis un fichier CSV à l'aide de Pandas, avec les dates comme index pour faciliter l'analyse des séries temporelles.

Sélection de Colonnes Spécifiques : Affichage des 5 premières lignes des colonnes Open et High pour visualiser les prix d'ouverture et les prix les plus hauts.

Visualisation des Données : Utilisation de Matplotlib pour tracer un graphique de la colonne Adj Close (prix de clôture ajusté) et analyser l'évolution des actions de Tesla sur la période donnée.

Export et Réutilisation des Données : Sauvegarde du DataFrame modifié dans un fichier CSV pour une utilisation future et relecture des données pour de nouvelles analyses.

3ème partie : Analyse des données et visualisation avancée
Calcul de la Moyenne Mobile :
Application d'une moyenne mobile à 100 jours sur les prix de clôture ajustés pour analyser la tendance à long terme.

Visualisation Avancée :
Création de deux graphiques : un pour les prix et la moyenne mobile, un autre pour le volume des transactions, offrant une vue d'ensemble complète des mouvements du marché.

Nettoyage des Données :
Suppression des lignes avec des valeurs manquantes pour garantir l'intégrité des données.

4ème partie : Visualisation des données boursières avec des chandeliers et volume
Réinitialisation de l'index du DataFrame df_ohlc et converti les dates au format numérique pour les graphiques.
Deux sous-graphiques ont été créés : un pour afficher le graphique en chandeliers des prix de Tesla et l'autre pour afficher le volume des transactions.
Le graphique en chandeliers fournit une vue claire de l'évolution des prix, tandis que le graphique du volume permet d'évaluer l'intérêt du marché à différents moments.

5ème partie  : Récupération des tickers avec BeautifulSoup des sociétés faisant partie du S&P 500 puis stockage dans un fichier pickle pour réutilisation

Partie 6 : Téléchargement des données boursières
Tickers S&P 500 : Chargement depuis un fichier ou récupération depuis Wikipedia.
Dossier de stockage : Création d'un dossier pour les CSV.
Données Yahoo Finance : Téléchargement et sauvegarde des données historiques (2000-2016).
Optimisation : Évite de retélécharger si les fichiers existent déjà


Partie 7 : Compilation des données

Chargement des tickers du S&P 500 à partir du fichier pickle.
Lecture des données boursières stockées en CSV pour chaque société.
Renommage de la colonne 'Adj Close' par le ticker correspondant et suppression des colonnes inutiles.
Fusion des données de tous les tickers dans un seul DataFrame.
Export des données combinées dans un fichier CSV sp500_joined_closes.csv.

Partie 8 : 
Visualisation des Données : Lecture des prix de clôture ajustés du S&P 500 et tracé des prix d'Apple (AAPL).
Matrice de Corrélation : Calcul et affichage d'une heatmap représentant la corrélation entre les actions du S&P 500.


Partie 9 : 
Préparation des données pour les étiquettes :
Création de nouvelles colonnes représentant la variation du prix pour chaque jour futur sur une période donnée (7 jours).
Remplacement des valeurs manquantes par des zéros pour éviter les erreurs lors de l'analyse.

Partie 10:
Machine Learning pour prédire l'évolution du prix d'une action sur 7 jours
Préparation des données : Extraction des prix de clôture ajustés des actions du S&P 500 sur une période donnée et création de nouvelles colonnes pour les variations sur plusieurs jours.

Fonction de décision : Utilisation d'une fonction buy_sell_hold pour déterminer si un achat, une vente ou une conservation de l'action est nécessaire en fonction des variations des prix sur 7 jours.

Entraînement du modèle : Division des données en ensembles d'entraînement et de test, et entraînement d'un classificateur KNN pour prédire les mouvements boursiers.

Précision : Évaluation de la précision du modèle et affichage des prédictions sous forme de répartition des décisions (achat, vente, maintien).
