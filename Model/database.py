import mysql.connector

class DatabaseManager:
    # Constructeur
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                                           host='localhost', database='users')
        self.cursor = self.cnx.cursor()

    # Destructeur
    def __del__(self):
        self.cnx.close()

    # Fermer la connexion à la DB
    def close_connection(self):
        self.cnx.close()

    # traitement de la requête
    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    # Retour des valeurs
    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()