
import json
from database import Database

def get_reviews_by_book_id(book_id):
    db = Database('books.db')
    reviews = db.query('SELECT * FROM reviews WHERE book_id = ?', (book_id,))
    db.close()
    reviews_list = [{'review_id': review[0], 'book_id': review[1], 'review_text': review[2], 'rating': review[3]} for review in reviews]
    return json.dumps(reviews_list, indent=4)

# Example usage
# print(get_reviews_by_book_id(1))
