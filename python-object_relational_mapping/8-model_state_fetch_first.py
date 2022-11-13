#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import select

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, mysql_dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    table = session.query(State).all()

    for row in table:
        print(f"{row.id}: {row.name}")
