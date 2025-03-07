#!/usr/bin/python3
import MySQLdb
import sys

""" 
lists all states starting with N from the database
"""

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch all the results
    states = cursor.fetchall()

    # Print each result
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
