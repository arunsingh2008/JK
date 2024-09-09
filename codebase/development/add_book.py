

import json
from sqlalchemy.exc import SQLAlchemyError
from book_model import Book, Session

def create_book(title, author, year_published):
    session = Session()
    try:
        new_book = Book(title=title, author=author, year_published=year_published)
        session.add(new_book)
        session.commit()
        return json.dumps({'id': new_book.id})
    except SQLAlchemyError as e:
        session.rollback()
        return json.dumps({'error': str(e)})
    finally:
        session.close()


