#!/usr/bin/python3
""" script that lists first State objects from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_dbname = sys.argv[3]
    mysql_arg = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, mysql_dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    filteredTable = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)
    for row in filteredTable:
        print(f"{row.id}: {row.name}")
    session.close()
