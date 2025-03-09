#!/usr/bin/python3
"""Affiche toutes les villes de la base de données avec leur état"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
from model_state import Base

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer les villes avec leur état correspondant
    results = (
        session.query(State.name, City.id, City.name)
        .join(City)
        .order_by(City.id)
        .all()
    )

    # Affichage des résultats
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
