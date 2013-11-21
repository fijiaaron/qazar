from sqlite3 import connect
db=connect("cloudtestenvironment.db")
cursor=db.cursor()
print cursor.execute("SELECT * FROM order_items").fetchall()
print cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
