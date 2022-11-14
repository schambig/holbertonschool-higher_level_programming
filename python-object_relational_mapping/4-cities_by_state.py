#!/usr/bin/python3
''' Script to retrieve data from a database '''
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id")
    [print(cities) for cities in cur.fetchall()]
    cur.close()
    db.close()