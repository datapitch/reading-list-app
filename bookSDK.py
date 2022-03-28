import sqlite3
from books import Book

def cursor():
    return sqlite3.connect('books.db').cursor()

def create_table(table_name):
    c = cursor()
    c.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)")
    c.connection.close()

def add_book(book):
    c = cursor()

    with c.connection:
        c.execute("INSERT INTO books VALUES (?, ?)", (book.title, book.pages))
    c.connection.close()
    return c.lastrowid
    

def get_book():
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
        c.execute('SELECT * FROM books WHERE title=?', (title, ))
    data = c.fetchone()
    c.connection.close()
    return data
    if not data:
        return None

def update_a_book(book, new_title, new_pages):
    c = cursor()
    with c.connection:
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?', (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(book.title)
    c.connection.close()
    return book


def delete_a_book(title):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=?', (title, ))
    rows = c.rowcount
    c.connection.close()
    return rows
  

    