#!/usr/bin/python3
"""
Script that lists all states with a name starting
with 'N' from a MySQL database.
It takes three arguments: mysql username, mysql password, and database name.
The results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function to connect to MySQL, execute the query and list states
    starting with 'N' ordered by their id.
    """
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the query to get states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows from the executed query
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
