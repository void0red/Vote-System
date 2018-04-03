import sqlite3
from hashlib import md5


def get_md5(tar):
    return md5(bytes(str(tar), encoding='utf-8')).hexdigest()


class TP:
    def __init__(self, database, tp_hash=None):
        self.database = database
        self.tp_hash = tp_hash
        self.con = sqlite3.connect(database)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def add(self, title, title_hash, category, content, email):
        self.cur.execute('''insert into TP values (?, ?, ?, ?)''', (self.tp_hash, title, title_hash, category))
        content = content.split(',')
        args = []
        for x in content:
            args.append((title_hash, get_md5(email + x), x))
        self.cur.executemany('''insert into BALLOT values (?, ?, ?, 0)''', args)
        self.con.commit()

    def delete(self, title_hash):
        self.cur.execute('''delete from TP where TP_HASH = ? and TITLE_HASH = ?''', (self.tp_hash, title_hash))
        self.cur.execute('''delete from BALLOT where TITLE_HASH = ?''', (title_hash, ))
        self.con.commit()

    def get_info(self):
        re = self.cur.execute('''select TITLE, TITLE_HASH, CATEGORY from TP where TP_HASH = ?''', (self.tp_hash, )).fetchall()
        info = []
        for x in range(len(re)):
            info.append({'title': re[x][0], 'hash': re[x][1], 'category': re[x][2]})
        return info

    def get_single_info(self, title_hash):
        r1 = self.cur.execute('''select TITLE, CATEGORY from TP where TITLE_HASH = ?''', (title_hash, )).fetchall()
        li = {'title': r1[0][0], 'info': [], 'link': title_hash}
        if int(r1[0][1]) == 1:
            li['category'] = '单选'
        elif int(r1[0][1]) == 2:
            li['category'] = '多选'
        else:
            li['category'] = 'error'
        r2 = self.cur.execute('''select CONTENT, NUM from BALLOT where TITLE_HASH =?''', (title_hash, )).fetchall()
        sum = 0
        for x in range(len(r2)):
            li['info'].append({'content': r2[x][0], 'value': r2[x][1]})
            sum += int(r2[x][1])
        li['sum'] = sum
        li['num'] = len(r2)
        return li

    def get_share_info(self, title_hash):
        try:
            r1 = self.cur.execute('''select TITLE, CATEGORY from TP where TITLE_HASH = ?''', (title_hash,)).fetchall()
            li = {'title': r1[0][0], 'info': []}
            if int(r1[0][1]) == 1:
                category = 'radio'
            elif int(r1[0][1]) == 2:
                category = 'checkbox'
            else:
                category = 'error'
            r2 = self.cur.execute('''select CONTENT, ID from BALLOT where TITLE_HASH = ?''', (title_hash, )).fetchall()
            for x in r2:
                li['info'].append({'content': x[0], 'category': category, 'id': x[1]})
            return li
        except:
            return None

    def tp(self, id):
        try:
            id = id.split(',')
            re = []
            for x in id:
                re.append(self.cur.execute('''select NUM from BALLOT where ID = ?''', (x, )).fetchall()[0][0])
            args = []
            for x in range(len(id)):
                args.append((int(re[x]) + 1, id[x]))
            self.cur.executemany('''update BALLOT set NUM = ? where ID = ?''', args)
            self.con.commit()
        except:
            return None

