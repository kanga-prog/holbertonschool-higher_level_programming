#!/usr/bin/python3
"""
Script that lists all states with a name matching the user input from the
MySQL database hbtn_0e_0_usa. It takes four arguments: mysql username,
mysql password, database name, and state name to search for.
Results are sorted by states.id in ascending order.
"""

import sys
import MySQLdb


def connect_to_db(username, password, db_name):
    """
    Establishes a connection to the MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the database to connect to.

    Returns:
        connection: A MySQLdb connection object.
    """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
        return conn
    except MySQLdb.MySQLError as e:
        print(f"Error: {e}")
        sys.exit(1)


def fetch_states_by_name(cursor, state_name):
    """
    Fetches all states from the 'states' table where the name matches the given
    argument.

    Args:
        cursor (MySQLdb.cursor): The cursor object to execute queries.
        state_name (str): The name of the state to search for.

    Returns:
        list: A list of tuples representing the states that match the name.
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    return cursor.fetchall()


def main():
    """
    Main function to connect to the database, execute the query, and display states
    matching the user input for state name.
    """
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql username> <mysql password>"
              " <database name> <state name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    conn = connect_to_db(username, password, database)

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Fetch states matching the name
    states = fetch_states_by_name(cursor, state_name)

    # Print the states that match
    if states:
        for state in states:
            print(state)
    else:
        print(f"No state found matching: {state_name}")

    # Close the cursor and the connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
