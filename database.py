import psycopg2
import urllib.parse as urlparse
import os
from config import url
import config

url = urlparse.urlparse(url)
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
class User():
    def __init__(self, chatid,letters, open, pos, r1, r2, r3, r4, r5 ):
        self.id = chatid
        self.user = chatid
        self.letters = letters
        self.pos = pos
        self.open = open
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.r5 = r5

    pass

def new_user(chatid, letters, open, pos, r1, r2, r3, r4, r5):
    print('new')
    cur = con.cursor()
    s = cur.execute('SELECT 1 FROM players WHERE id={}'.format(str(chatid)))
    print(s)
    if s == None:
        print('INSERT')
        cur.execute("INSERT INTO players (id, users, letters,\
         open, pos, r1, r2, r3, r4, r5) VALUES (%s, %s, %s, %s, \
         %s, %s, %s, %s, %s, %s)", (chatid, chatid,letters, open, pos, r1, r2, r3, r4, r5))
    else:
        cur.execute('Update players set letters = %s where id = %s', (letters, chatid))
    con.commit()
    cur.close()
    return 'done'


def new_score(chatid, score):
    cur = con.cursor()
    s = cur.execute('SELECT 1 FROM users WHERE id={}'.format(str(chatid)))
    if s != 1:
        cur.execute('Update users set scores = %s where id = %s', (score, chatid))
        con.commit()
    cur.close()
    return 'created'


def get_user(chatid):
    cur = con.cursor()
    cur.execute('SELECT user, letters, open, pos, r1, r2, r3, r4, r5 FROM players WHERE id={}'.format(str(chatid)))
    arr = cur.fetchone()
    print(arr)
    if arr != None:
        info = User( *list(arr))
    else:
        info = []
    cur.close()
    return info

#
# cursor = con.cursor()
# #QL query to create a new table
# create_table_query = '''CREATE TABLE players
#       (id INT PRIMARY KEY NOT NULL,
#       users TEXT,
#       letters TEXT [],
#       open TEXT,
#       pos INT,
#       r1  TEXT [],
#       r2 TEXT [],
#       r3 TEXT [],
#       r4 TEXT [],
#       r5 TEXT []); '''
# #Execute a command: this creates a new table
# cursor.execute(create_table_query)
# con.commit()

# open = False
# gamekey = [config.b1, config.b2, config.b3, config.b4, config.b5, config.b6]
# btns = [config.b1, config.b2, config.b3, config.b4, config.b5, config.b6]
# letters = ["ppppp", "⬜","⬜","⬜","⬜","✅" ]
# pos = 0
#new_user(505303780, letters, open, pos, letters, letters, letters,  letters, letters)
# s = get_user(50530370)
# print(s.id, s.letters, s.pos, s.r3)
#
# cursor.execute("ROLLBACK")
# con.commit()
