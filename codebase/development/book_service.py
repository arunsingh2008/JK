


from sqlalchemy.orm import Session
from book_model import Book
from datetime import datetime
import json

def create_book(db_session: Session, book_data: dict) -> dict:
    # Validate input data
    if not ('title' in book_data and 'author' in book_data):
        raise ValueError('Missing title or author in book data')
    
    # Insert book into database
    new_book = Book(
        title=book_data['title'],
        author=book_data['author'],
        published_date=datetime.utcnow()
    )
    db_session.add(new_book)
    db_session.commit()
    
    # Return book details
    return json.dumps({
        'id': new_book.id,
        'title': new_book.title,
        'author': new_book.author,
        'published_date': new_book.published_date.isoformat()
    }, default=str)


