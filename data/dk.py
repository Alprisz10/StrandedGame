import sqlite3

db = sqlite3.connect("data/data.db",check_same_thread=False)
cur = db.cursor()