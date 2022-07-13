import sqlite3
con = sqlite3.connect("./static/database.db")
cur = con.cursor()
cur.execute("INSERT INTO USERS ( ID, USERNAME, INFO) VALUES ( NULL, 'hello', 'its me')")
con.commit()
con.close()


