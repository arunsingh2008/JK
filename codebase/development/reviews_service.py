



from database import Database
import json

class ReviewsService:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def get_reviews_by_book_id(self, book_id):
        reviews = self.db.query('SELECT * FROM reviews WHERE book_id = ?', [book_id])
        self.db.close()
        return json.dumps([{"review_id": review[0], "book_id": review[1], "review_text": review[2], "rating": review[3]} for review in reviews])



