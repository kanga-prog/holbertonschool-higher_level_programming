#!/usr/bin/python3
"""
Script qui recherche un état par son nom dans la base de données `hbtn_0e_6_usa`.
Utilise SQLAlchemy pour interagir avec la base de données.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def main():
    """
    Recherche un état par son nom et affiche son id si trouvé, sinon 'Not found'.

    Usage :
        ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name to search>

    Exemple :
        >>> import subprocess
        >>> subprocess.run(['./10-model_state_my_get.py', 'root', 'root', 'hbtn_0e_6_usa', 'Texas'])
        3
        >>> subprocess.run(['./10-model_state_my_get.py', 'root', 'root', 'hbtn_0e_6_usa', 'Illinois'])
        Not found
    """

    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name to search>")
        return

    # Extraction des arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Configuration de l'engine pour se connecter à la base de données
    engine = create_engine(
        f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'
    )

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état par son nom
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state:
        print(state.id)
    else:
        print("Not found")

    # Fermeture de la session
    session.close()

if __name__ == "__main__":
    main()
