#!/usr/bin/python3
""" script that lists all cities from the database  """
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
    args = (mysql_arg,)
    sqlParams = """SELECT cities.name
                FROM cities
                LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s;
                """
    cur.execute(sqlParams, args)

    stuff = cur.fetchall()

    string = ""
    for element in stuff:
        string += element[0]
        if (element != stuff[-1]):
            string += ", "
    print(string)

    db.close()
