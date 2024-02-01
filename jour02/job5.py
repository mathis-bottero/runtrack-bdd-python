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

requete_sql = "SELECT SUM(superficie) AS superficie_totale FROM etage"
curseur.execute(requete_sql)

# Récupére le résultat
resultat = curseur.fetchone()

# Affiche le message avec la superficie totale
superficie_totale = resultat[0]
print(f"La superficie de La Plateforme est de: {superficie_totale} m2")

# Fermer le curseur et la connexion
curseur.close()
connexion.close()