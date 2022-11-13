#!/usr/bin/python3
""" script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, mysql_dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id).all()

    for state, city in result:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.commit()
    session.close()
