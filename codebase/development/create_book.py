



from database import connect_db, close_db

def create_book(title, author, published_date):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books (title, author, published_date) VALUES (?, ?, ?)', (title, author, published_date))
    connection.commit()
    close_db(connection)



