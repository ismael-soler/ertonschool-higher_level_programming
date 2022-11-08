#!/usr/bin/python3
""" This module selects all the states from a given db """
if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_dbname,
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    stuff = cur.fetchall()
    for i in stuff:
        print(i)

    cur.close()
    db.close()
