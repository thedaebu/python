import sqlite3
from modules.book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c = cursor()

    with c.connection:
        c.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))

    c.connection.close()

    return c.lastrowid

def get_books():
    c = cursor()
    books = []

    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(Book(book[0], book[1]))

    c.connection.close()

    return books

def get_book_by_title(title):
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books WHERE title LIKE ?', (f'{title}',))
        data = c.fetchone()

    c.connection.close()

    if not data:
        return None
    else:
        return Book(data[0], data[1])

def update_book(book_title, new_title, new_pages):
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books WHERE title LIKE ?', (book_title,))
        data = c.fetchone()
        fetchedBook = Book(data[0], data[1])
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? and pages=?', (new_title, new_pages, fetchedBook.title, fetchedBook.pages))

    book = get_book_by_title(new_title)
    c.connection.close()

    return book

def delete_book(title):
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books WHERE title LIKE ?', (title,))
        data = c.fetchone()
        fetchedBook = Book(data[0], data[1])
        c.execute('DELETE FROM books WHERE title=? AND pages=?', (fetchedBook.title, fetchedBook.pages))
    
    rows = c.rowcount
    c.connection.close()
    return rows