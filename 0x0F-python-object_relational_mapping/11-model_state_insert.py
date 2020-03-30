#!/usr/bin/python3
"""
script that inserts a new state in a db
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

    session = sessionmaker(bind=eng)()
    lu = State(name="Louisiana")
    session.add(lu)
    session.commit()
    print(lu.id)
    session.close()
