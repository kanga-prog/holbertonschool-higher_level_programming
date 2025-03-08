#!/usr/bin/python3

"""
Script that filters states by user input from the database.
It takes four arguments: mysql username, mysql password, database name, and state name to search for.
The results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function to connect to MySQL, execute the query, and list states
    that match the user input for state name.
    """
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query to get states that match the user input (state_name)
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))

    # Fetch all rows from the executed query
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

