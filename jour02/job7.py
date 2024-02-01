import mysql.connector

class Salarie:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.curseur = self.connexion.cursor()

    def creer_table_salarie(self):
        requete = """
            CREATE TABLE IF NOT EXISTS salarie (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                prenom VARCHAR(255),
                salaire DECIMAL(10, 2),
                id_service INT,
                FOREIGN KEY (id_service) REFERENCES service(id)
            )
        """
        self.curseur.execute(requete)
        self.connexion.commit()
        print("Table 'salarie' créée avec succès.")

    def creer_salarie(self, nom, prenom, salaire, id_service):
        requete = "INSERT INTO salarie (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print("Salarie créé avec succès.")

    def lire_salaries(self):
        requete = "SELECT * FROM salarie"
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()
        for resultat in resultats:
            print(resultat)

    def mettre_a_jour_salaire(self, salarie_id, nouveau_salaire):
        requete = "UPDATE salarie SET salaire = %s WHERE id = %s"
        valeurs = (nouveau_salaire, salarie_id)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print("Salaire mis à jour avec succès.")

    def supprimer_salarie(self, salarie_id):
        requete = "DELETE FROM salarie WHERE id = %s"
        valeurs = (salarie_id,)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()
        print("Salarie supprimé avec succès.")

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()
        print("Connexion à la base de données fermée.")

# Identifiants de connexion à la base de données
host = 'localhost'
user = 'mot1'
password = 'mot1'
database = 'employeMB'

# Se connecte à la base de données
connexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Crée un curseur pour exécuter des requêtes SQL
curseur = connexion.cursor()

# Exécuter la requête pour créer la table "salarie"
salarie_manager = Salarie(host, user, password, database)
salarie_manager.creer_table_salarie()

# Fermer le curseur et la connexion
curseur.close()
connexion.close()

# Continuer avec la classe Salarie

# Exemple d'utilisation de la classe Salarie
salarie_manager = Salarie(host, user, password, database)

# Créer un salarié
salarie_manager.creer_salarie('Doe', 'John', 50000.00, 1)

# Lire tous les salariés
print("\nListe des salariés avant mise à jour:")
salarie_manager.lire_salaries()

# Mettre à jour le salaire d'un salarié
salarie_manager.mettre_a_jour_salaire(1, 55000.00)

# Lire tous les salariés après mise à jour
print("\nListe des salariés après mise à jour:")
salarie_manager.lire_salaries()

# Supprimer un salarié
salarie_manager.supprimer_salarie(1)

# Lire tous les salariés après suppression
print("\nListe des salariés après suppression:")
salarie_manager.lire_salaries()

# Fermer la connexion
salarie_manager.fermer_connexion()