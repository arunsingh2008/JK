
from database import Database

def add_review(user_id, book_id, rating, review):
    db = Database('reviews.db')
    try:
        # Insert review data into reviews table
        insert_query = 'INSERT INTO reviews (user_id, book_id, rating, review) VALUES (?, ?, ?, ?)'
        db.execute_query(insert_query, (user_id, book_id, rating, review))

        # Update book rating
        update_query = '''
        UPDATE books
        SET rating = (
            SELECT AVG(rating)
            FROM reviews
            WHERE book_id = ?
        )
        WHERE id = ?
        '''
        db.execute_query(update_query, (book_id, book_id))

        # Commit transaction and close database connection
        db.commit_and_close()
    except Exception as e:
        print(f'An error occurred: {e}')
        db.connection.rollback()
        db.commit_and_close()
