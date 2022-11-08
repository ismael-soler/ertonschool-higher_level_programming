#!/usr/bin/python3
""" takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument """
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
                WHERE name LIKE BINARY '{}'
                ORDER BY id ASC""".format(mysql_arg))
    stuff = cur.fetchall()
    for i in stuff:
        print(i)

    db.close()
