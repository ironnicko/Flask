import sqlite3

db = sqlite3.connect("users.sqlite3")

cur = db.cursor()

try:
    cur.execute("SELECT * FROM users")
    [print(i) for i in cur]
except Exception as e:
    print(e)

finally:
    cur.close()
    db.close()
