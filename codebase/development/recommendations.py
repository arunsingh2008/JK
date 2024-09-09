


from database import Database
import json

class BookRecommendations:
    def __init__(self):
        self.db = Database()

    def get_book_recommendations(self, preferences):
        books = self.db.get_books_by_preferences(preferences)
        recommendations = []
        for book in books:
            book_dict = {
                'id': book[0],
                'title': book[1],
                'author': book[2],
                'genre': book[3],
                'year_published': book[4]
            }
            recommendations.append(book_dict)
        return json.dumps(recommendations, indent=4)

if __name__ == '__main__':
    preferences = {'genre': 'Science Fiction', 'year_published': '2000'}
    rec = BookRecommendations()
    print(rec.get_book_recommendations(preferences))


