#!/usr/bin/python3
''' Script that changes the name of a State object from a given database '''
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

    up_state = session.query(State).filter_by(id=2).first()
    up_state.name = 'New Mexico'
    session.commit()
