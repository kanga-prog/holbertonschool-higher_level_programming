#!/usr/bin/python3
"""
Script that lists all states with a name starting\
      with 'N' from a MySQL database.
It takes three arguments: mysql username, mysql password, and database name.
The results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
                     host="localhost",
                     port=3306, user=username,
                     passwd='KKb', db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
