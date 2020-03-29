#!/usr/bin/python3
"""

"""
if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) < 4:
        print('Usage: {} username \
               password database_name'.format(argv[0]))
        exit(1)
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                        passwd, db))
    session = sessionmaker(bind=eng)
    States = session().query(State).all()

    for row in States:
        print("{}: {}".format(row.id, row.name))

    session.close()
