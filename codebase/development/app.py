



from flask import Flask, jsonify
from database import get_db_connection

app = Flask(__name__)

@app.route('/book/<int:book_id>')
def get_book_by_id(book_id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(dict(book))



