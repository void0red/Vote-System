import sqlite3
try:
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    try:
        cur.execute('''CREATE TABLE USER (EMAIL TEXT NOT NULL,
                                          PASSWORD TEXT NOT NULL,
                                          CHECKED INT NOT NULL,
                                          TP_HASH TEXT NOT NULL)''')
    finally:
        con.commit()
    try:
        cur.execute('''CREATE TABLE TP (TP_HASH TEXT NOT NULL,
                                        TITLE TEXT NOT NULL,
                                        TITLE_HASH TEXT NOT NULL,
                                        CATEGORY INT NOT NULL)''')
    finally:
        con.commit()
    try:
        cur.execute('''CREATE TABLE BALLOT (TITLE_HASH TEXT NOT NULL,
                                            ID TEXT NOT NULL,
                                            CONTENT TEXT NOT NULL,
                                            NUM TEXT NOT NULL)''')
    finally:
        con.commit()
except:
    pass