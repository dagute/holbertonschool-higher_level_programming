#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.Connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4], ))
    l = []
    for row in cur.fetchall():
        l.append(row[1])
    print(", ".join(l))

    cur.close()
    db.close()
