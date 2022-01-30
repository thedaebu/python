## sqlite
import sqlite3

conn = sqlite3.connect(':memory:') # connection to sqlite database in memory

c = conn.cursor() # executor for database

## creating a table in a database
c.execute('''CREATE TABLE books 
    (title TEXT, pages INTEGER)''')

## inserting data into a table
c.execute('INSERT INTO books VALUES ("Hola", 72)')
conn.commit()
books = [ # inserting multiple data into table, must be in a list of tuples
    ('Hello', 12),
    ('Wassup', 123),
    ('Ahnnyoung', 412)
]
c.executemany('INSERT INTO books VALUES (?, ?)', books)
conn.commit()

## retrieving data from a table
c.execute('SELECT rowid, * FROM books WHERE title LIKE "Hello"') # rowid is the innate id of item in the table
data = c.fetchall()

## deleting data from a table
c.execute('DELETE FROM books WHERE rowid=1')
conn.commit()
c.execute('SELECT * FROM books')
data = c.fetchall()

## updating data from a table
c.execute('UPDATE books SET title="Yizzurd", pages=69 WHERE rowid=2')
conn.commit()
c.execute('SELECT * FROM books')
data = c.fetchall()