import sqlite3

conn = sqlite3.connect("./static/database.db")
cursorObj = conn.cursor()

def two():
    subjects = [subject[0] for subject in cursorObj.execute("SELECT SUBJECT FROM SUBJECTS")]

    [conn.execute(f"""CREATE TABLE {subject}
            (ID INT PRIMARY KEY NOT NULL,
            QUESTION TEXT NOT NULL,
            Answer TEXT
            );""") for subject in subjects]

    conn.commit()
    conn.close()