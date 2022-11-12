import sqlite3

connection = sqlite3.connect('itstepDB.sl3', 5)
cur = connection.cursor()

cur.execute('CREATE TABLE users (name TEXT, login TEXT, password TEXT)')
connection.commit()



connection.close()