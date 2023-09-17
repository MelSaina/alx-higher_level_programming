#!/usr/bin/python3
"""List all State objects containing the letter 'a' from the database."""

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

    # Query State objects containing the letter 'a' in their name
    filtered_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results as specified
    for state in filtered_states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
