#!/usr/bin/python3
"""Print the states.id of the State object with the specified name from the database."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
