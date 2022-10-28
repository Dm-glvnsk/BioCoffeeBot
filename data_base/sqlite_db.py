import sqlite3 as sq
from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('cup.db')
    cur = base.cursor()
    if base:
        print('Data base connected!')
    base.execute('CREATE TABLE IF NOT EXISTS cup(id INT PRIMARY KEY, amount INT,  free_cups INT)')
    #base.execute('ALTER TABLE cup ALTER COLUMN amount SET DEFAULT "0"')
    #base.execute('ALTER TABLE cup ALTER COLUMN free_cups SET DEFAULT "0"')
    base.commit()