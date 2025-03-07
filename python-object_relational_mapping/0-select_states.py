#!/usr/bin/python3

import MySQLdb
import sys

'''
 module  to lists all states from the database hbtn_0e_0_usa
'''

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                                user=username, passwd=password, db=db_name)
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    # Execute the SQL query to fetch all states, ordered by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    # Fetch all the results
    states = cursor.fetchall()
    # Print each state in the format (id, name)
    for state in states:
        print(state)
    # Close the cursor and database connection
    cursor.close()
    db.close()
