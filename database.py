import sqlite3

conn = sqlite3.connect('shopping.db')

conn.execute('''CREATE TABLE Food
                    (id integer primary key autoincrement not null,
                    ingredient text,
                    category text,
                    quantity int)''')

conn.execute('''INSERT INTO Food values
                    (Beef, ?, ?)''')
conn.commit()
conn.close()



