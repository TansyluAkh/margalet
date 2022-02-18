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


def new_user(chatid, letters, open, pos, r1, r2, r3, r4, r5):
    print('new')
    cur = con.cursor()

    cur.execute("INSERT INTO players (id, users, letters, open, pos, r1, r2, r3, r4, r5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (chatid,chatid,letters, open, pos, r1, r2, r3, r4, r5))
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
    cur.execute('SELECT r1 FROM players WHERE id={}'.format(str(chatid)))
    arr = cur.fetchone()
    print(arr)
    cur.close()
    return arr

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
# letters = ["⬜", "⬜","⬜","⬜","⬜","✅" ]
# pos = 0
# new_user(505303703, letters, open, pos, letters, letters, letters,  letters , letters,)
# get_user(505303703)