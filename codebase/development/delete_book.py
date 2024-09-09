



from database import get_db_connection

def delete_book(book_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    connection.commit()
    connection.close()

# Example usage (Uncomment the following line to use):
# delete_book(1)



