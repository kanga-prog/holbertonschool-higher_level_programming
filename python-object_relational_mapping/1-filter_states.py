#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from a MySQL database.
It takes three arguments: mysql username, mysql password, and database name.
The results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def list_states_starting_with_n(username, password, database):
    """
    Connects to the MySQL database, retrieves all states whose names start
    with 'N', and returns them sorted by 'id' in ascending order.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): The name of the database.

    Returns:
        list: A list of tuples where each tuple contains the state id and name.
    """
    try:
        # Establish connection to MySQL server
        db = MySQLdb.connect(user=username, passwd=password, db=database)
    except MySQLdb.MySQLError as e:
        print(f"Error: {e}")
        return []

    with db.cursor() as cursor:
        # Execute the query to retrieve states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # Fetch all rows and return the results
        states = cursor.fetchall()

    db.close()
    return states


def print_states(states):
    """
    Prints the states fetched from the database.

    Args:
        states (list): A list of tuples containing state id and name.
    """
    for state in states:
        print(state)


if __name__ == "__main__":
    """
    Main function to fetch and display states starting with 'N' from the database.
    It expects three arguments: MySQL username, password, and database name.
    """
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Fetch the states starting with 'N'
    states = list_states_starting_with_n(username, password, database)

    # If we have states, print them
    if states:
        print_states(states)
    else:
        print("No states found.")
