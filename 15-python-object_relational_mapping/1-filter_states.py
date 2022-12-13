#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """
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
    cur.execute("""SELECT *
                FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC""")
    stuff = cur.fetchall()
    for i in stuff:
        print(i)

    db.close()
