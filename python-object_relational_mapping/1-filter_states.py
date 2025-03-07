#!/usr/bin/python3

"""
Script that connects to a MySQL database and displays all reports
whose name starts with 'N', sorted by ID.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Se connecter au serveur MySQL en localhost au port 3306
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )

    cursor = db.cursor()

    # Requête pour récupérer les états dont le nom commence par 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Récupérer et afficher les résultats
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Fermer le curseur et la connexion à la base de données
    cursor.close()
    db.close()
