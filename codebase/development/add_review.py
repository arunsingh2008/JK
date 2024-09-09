



from database import connect_db, close_db

def add_review(book_id, review_details):
    connection = connect_db()
    cursor = connection.cursor()
    
    try:
        cursor.execute('INSERT INTO reviews (book_id, review_text) VALUES (?, ?)', (book_id, review_details))
        connection.commit()
    except Exception as e:
        print(f'An error occurred: {e}')
        connection.rollback()
    finally:
        close_db(connection)



