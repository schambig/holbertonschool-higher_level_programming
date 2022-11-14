#!/usr/bin/python3
''' Script that prints the State object with
the name passed as argument from a given database '''
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

    is_here = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print('{}'.format(state.id))
            is_here = True
            break
    if is_here is False:
        print('Not found')
