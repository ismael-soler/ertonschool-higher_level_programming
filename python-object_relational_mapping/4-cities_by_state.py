#!/usr/bin/python3
""" script that lists all cities from the database  """
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
    cur.execute("""SELECT c.id, c.name, s.name
                FROM cities c
                LEFT JOIN states s
                ON c.state_id = s.id;
                """)
    stuff = cur.fetchall()
    for i in stuff:
        print(i)

    db.close()
