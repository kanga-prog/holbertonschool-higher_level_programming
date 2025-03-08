#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument
and lists all cities of that state from the database hbtn_0e_4_usa.
It uses MySQLdb to prevent SQL injection.
"""
import sys
import MySQLdb


def main():
    """
    Connects to the database and lists cities from the state.
    """
    if len(sys.argv) != 4:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password>"
              " <database name> <state name>")
        sys.exit(1)

    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Query to get cities from a state, safely using parameterized queries
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the query with the state name as parameter to avoid SQL injection
    cursor.execute(query, (state_name,))

    # Fetch all results
    cities = cursor.fetchall()

    # If cities are found, print them as comma-separated values
    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print()

    # Close the cursor and the connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

