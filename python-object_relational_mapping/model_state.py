#!/usr/bin/python3
"""
Script that defines the State class and links \
    it to the `states` table in a MySQL database.
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Declare the Base class for all models
Base = declarative_base()


class State(Base):
    """
    State class that links to the `states` table in the MySQL database.
    It has an `id` column (primary key) and a `name` column.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":

    # Establish connection to MySQL using user credentials and database name
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    # Create the states table if it doesn't exist
    Base.metadata.create_all(engine)
