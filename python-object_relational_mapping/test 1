#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
Uses SQLAlchemy to interact with the database.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Ensure we get the arguments: mysql username, password, and db name
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py "
              "<mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}",
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all states where the name contains the letter 'a'
    states_to_delete = session.query(State).\
        filter(State.name.like('%a%')).all()

    # Delete the states found
    for state in states_to_delete:
        session.delete(state)

    session.commit()  # Commit the deletion to the database
    print(f"{len(states_to_delete)} state(s) deleted")

    # Close the session
    session.close()
