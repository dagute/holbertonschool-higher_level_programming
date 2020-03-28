#!/usr/bin/python3
"""changes the name of a State object from the database"""
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    change = session.query(State).filter_by(id=2).first()
    change.name = 'New Mexico'
    session.commit()

    session.close()
