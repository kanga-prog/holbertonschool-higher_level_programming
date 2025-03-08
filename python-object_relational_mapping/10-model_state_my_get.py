#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name to search>")
        return

    # Extract arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Setup the engine to connect to the database
    engine = create_engine(f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state by name
    state = session.query(State).filter(State.name == state_name).first()

    # Check if state was found and print result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()

