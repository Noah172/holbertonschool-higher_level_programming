#!/usr/bin/python3
"""
script that takes in the name of a state as an
argument and lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) < 4:
        print('Usage: {} username \
               password database_name state_name'.format(argv[0]))
        exit(1)
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    stat = argv[4]
    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=passwd, db=db, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
                    FROM cities INNER JOIN states \
                    ON states.id = state_id \
                    WHERE states.name=%s", (stat,))

    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
