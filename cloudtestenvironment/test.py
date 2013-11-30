from sqlite3 import connect
db=connect("cloudtestenvironment.db")
cursor=db.cursor()
print cursor.execute("SELECT * FROM customers").fetchall()
print cursor.execute("SELECT * FROM orders").fetchall()
print cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
