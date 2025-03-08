#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
and their corresponding state names.
It takes three arguments: mysql username, mysql password, and database name.
Results are sorted in ascending order by cities.id.
"""

import sys
import MySQLdb


def main():
    """
    Main function to connect to the database, execute the query,
    and display cities with their corresponding state names.
    """
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> \
              <mysql password> <database name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Execute the query to get cities and their corresponding states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and print all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
