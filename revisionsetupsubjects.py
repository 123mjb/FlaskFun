import sqlite3
conn = sqlite3.connect("./static/database.db")
cursorObj = conn.cursor()

def one():
    conn.execute("""CREATE TABLE SUBJECTS
            (SUBJECT TEXT PRIMARY KEY NOT NULL
            );""")

    [conn.execute(f"INSERT INTO SUBJECTS (SUBJECT) \
                    VALUES ('{subject}')") for subject in ['Maths','English','Geography','History','Music','Technology','Computing','French']]
    



    conn.commit()
    conn.close()