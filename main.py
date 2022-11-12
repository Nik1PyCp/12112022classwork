import sqlite3

connection = sqlite3.connect('itstepDB.sl3', 5)
cur = connection.cursor()

# cur.execute('CREATE TABLE users (name TEXT, login TEXT, password TEXT)')
# connection.commit()

#cur.execute('INSERT INTO users (name, login, password) VALUES("Veronika", "login12", "256847")')
#connection.commit()

#cur.execute('UPDATE users SET name = "Nika" WHERE rowid = 1')
#connection.commit()

#cur.execute('DELETE FROM users WHERE rowid = 3')
#connection.commit()

cur.execute('SELECT rowid, name, login, password FROM users')
connection.commit()
res = cur.fetchall()
print(res)

connection.close()