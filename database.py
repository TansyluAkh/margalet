import psycopg2
import urllib.parse as urlparse
import os
from config import url

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


def new_user(chatid, letters, open, pos, gamekey, btns):
    print('new')
    cur = con.cursor()
    s = cur.execute('SELECT id FROM players WHERE users={}'.format(str(chatid)))
    print(s)
    if s:
        cur.execute("INSERT INTO players (users, letters, open, pos, gamekey, btns) VALUES (%s, %s, %s)", (chatid, letters, open, pos, gamekey, btns))
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
    cur.execute('SELECT scores FROM users WHERE id={}'.format(str(chatid)))
    arr = cur.fetchone()
    print(arr)
    cur.close()
    return arr


# cursor = con.cursor()
# # SQL query to create a new table
# create_table_query = '''CREATE TABLE players
#       (id INT PRIMARY KEY NOT NULL,
#       users TEXT,
#       letters TEXT,
#       open TEXT,
#       pos INT,
#       gamekey  TEXT,
#       btns TEXT); '''
# # Execute a command: this creates a new table
# cursor.execute(create_table_query)
# con.commit()
