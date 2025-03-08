#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
using SQLAlchemy. The script takes 3 arguments: mysql username, mysql password,
and database name. It connects to a MySQL server running\
          on localhost at port 3306.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Get the arguments passed to the script
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:\
            {mysql_password}@localhost:3306/{database_name}", pool_pre_ping=True)

    # Create all tables in the database (if not already created)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to save the new state in the database
    session.commit()

    # Print the new state's id after creation
    print(new_state.id)

    # Close the session
    session.close()
