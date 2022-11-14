#!/usr/bin/python3
''' Script that deletes all State objects
with a name containing the letter 'a' from a given database '''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State):
        if 'a' in states.name:
            session.delete(states)
    session.commit()
