#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL database running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query to retrieve states in ascending order by states.id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows and display them as they are in the example
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        db.close()
