

from flask import request, jsonify\nfrom review_model import ReviewModel\n\ndef add_review():\n    data = request.json\n    book_id = data.get('book_id')\n    user_id = data.get('user_id')\n    rating = data.get('rating')\n    comment = data.get('comment')\n\n    if not all([book_id, user_id, rating, comment]):\n        return jsonify({'error': 'Missing data'}), 400\n\n    review_model = ReviewModel()\n    try:\n        review_id = review_model.insert_review(book_id, user_id, rating, comment)\n        review_model.update_book_rating(book_id)\n        return jsonify({'message': 'Review added successfully', 'review_id': review_id}), 201\n    except Exception as e:\n        return jsonify({'error': str(e)}), 500

