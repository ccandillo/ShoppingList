import sqlite3

conn = sqlite3.connect('shopping.db')

conn.execute('''
    CREATE TABLE Food(
        id integer primary key autoincrement,
        ingredient TEXT,
        category TEXT,
        quantity INTEGER
    )''')

conn.commit()
conn.close()



