#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Use a parameterized query to safely filter cities by state name
        query = "SELECT GROUP_CONCAT(name ORDER BY cities.id ASC) FROM cities \
                 JOIN states ON cities.state_id = states.id WHERE states.name=%s"
        cursor.execute(query, (state_name,))

        # Fetch the result and display it
        result = cursor.fetchone()
        if result and result[0]:
            print(result[0])

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        db.close()
