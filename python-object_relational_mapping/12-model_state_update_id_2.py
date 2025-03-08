#!/usr/bin/python3
"""
Script that changes the name of the State object with id = 2
from the database hbtn_0e_6_usa to "New Mexico".
Uses SQLAlchemy to interact with the database.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Ensure we get the arguments: mysql username, password, and db name
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the database
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}", pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the state with id = 2 exists
    if state_to_update:
        # Change the name of the state to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()  # Save the changes to the database
        print("State with id = 2 has been updated to:", state_to_update.name)
    else:
        print("State with id = 2 not found")

    # Close the session
    session.close()

