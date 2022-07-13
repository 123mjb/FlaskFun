import sqlite3
cur = sqlite3.connect("./static/database.db").cursor()
cur.execute("INSERT INTO USERS (ID, USERNAME, INFO) \
    VALUES (NULL, 'hello', 'its me')")


