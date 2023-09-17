#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Extract command-line arguments
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    # Connect to the MySQL database running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Create and execute the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows and display them as specified
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
