#!/usr/bin/python3

"""
Script qui liste tous les états dont le nom commence par 'N'
depuis une base de données MySQL, en utilisant SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Déclaration de la base
Base = declarative_base()

class State(Base):
    """
    Classe mappée à la table 'states' de la base de données.
    La table 'states' contient des colonnes 'id' et 'name'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    def __repr__(self):
        return f"({self.id}, '{self.name}')"

def main():
    """
    Fonction principale qui se connecte à la base de données
    et affiche tous les états dont le nom commence par 'N'.
    """
    # Vérification des arguments
    if len(sys.argv) != 4:
        return

    # Extraction des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création de l'URL de connexion
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}')
    
    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer les états dont le nom commence par 'N'
    states = session.query(State).filter(State.name.like('N%')).order_by(State.id).all()

    # Affichage des résultats
    for state in states:
        print(state)

    # Fermeture de la session
    session.close()

if __name__ == "__main__":
    main()

