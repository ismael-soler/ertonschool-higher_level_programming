#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the
    argument. But this time, write one that is safe from MySQL
    injections! """
if __name__ == '__main__':
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_dbname = sys.argv[3]
    mysql_arg = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_dbname,
        port=3306
    )

    cur = db.cursor()
    cur.execute("""SELECT *
                FROM states
                WHERE name LIKE %s
                ORDER BY id ASC""", (mysql_arg,))
    stuff = cur.fetchall()
    for i in stuff:
        print(i)

    db.close()
