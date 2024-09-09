



from database import get_db_connection

def update_book(book_id, title, author, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?', (title, author, year, book_id))
    conn.commit()
    conn.close()



