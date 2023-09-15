#!/usr/bin/python3
"""Add the State object "Louisiana" to the database and print its states.id."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for "Louisiana"
    louisiana = State(name="Louisiana")

    # Add the new State object to the database
    session.add(louisiana)
    session.commit()

    # Print the new states.id after creation
    print(louisiana.id)

    # Close the session
    session.close()
