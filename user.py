import sqlite3
from hashlib import md5


def get_md5(tar):
    return md5(bytes(str(tar), encoding='utf-8')).hexdigest()


class User:
    def __init__(self, email, password, database):
        self.email = email
        self.password = password
        self.con = sqlite3.connect(database)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def check_user(self):
        re = self.cur.execute('''select * from user where EMAIL = ?''', (self.email,)).fetchall()
        if not re:
            return 1
        elif re[0][1] != self.password:
            return 2
        else:
            return 0

    def add_user(self):
        self.cur.execute('''insert into user (EMAIL, PASSWORD, CHECKED, TP_HASH) values (?, ?, 1, ?)''', (self.email, self.password, get_md5(self.email + self.password)))
        self.con.commit()

    def get_tp_hash(self):
        tp_hash = get_md5(self.email + self.password)
        return tp_hash