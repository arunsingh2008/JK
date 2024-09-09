


import sqlite3

class Database:
    def __init__(self, db_name='books.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        self.conn.commit()

    def fetch_all_books(self):
        self.cursor.execute('SELECT * FROM books')
        rows = self.cursor.fetchall()
        return rows

    def __del__(self):
        self.conn.close()


