
from db import Database

class BooksRepository:
    def __init__(self, db_name='books.db'):
        self.db = Database(db_name)

    def get_all_books(self):
        query = 'SELECT * FROM books'
        books = self.db.query(query)
        return [{'id': book[0], 'title': book[1], 'author': book[2], 'year_published': book[3]} for book in books]

    def close_connection(self):
        self.db.close()
