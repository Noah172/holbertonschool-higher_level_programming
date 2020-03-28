#!/usr/bin/python3
"""
Safe from injections
"""
if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], port=3306,
                         host="localhost", db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name=%s ORDER BY id ASC",
        (sys.argv[4],))
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    db.close()
