import sqlite3
conn = sqlite3.connect("./static/database.db")

conn.execute("""CREATE TABLE USERS
        (ID INTEGER PRIMARY KEY,
        USERNAME TEXT NOT NULL,
        INFO TEXT
        );""")

conn.close()