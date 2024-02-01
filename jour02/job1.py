import mysql.connector

#  Identifiants de connexion à la base de données
host = 'localhost'
user = 'mot'
password = 'mot'
database = 'LapLateforme'

# Se connecte à la base de données
connexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

#  Crée un curseur pour exécuter des requêtes SQL
curseur = connexion.cursor()

#  Exécute une requête pour récupérer tous les étudiants
requete_sql = "SELECT * FROM etudiant"
curseur.execute(requete_sql)

#   Récupère les résultats
resultats = curseur.fetchall()

#  Affiche les résultats en console
for resultat in resultats:
    print(resultat)

#  Ferme le curseur et la connexion
curseur.close()
connexion.close()