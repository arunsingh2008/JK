

from flask import Blueprint, jsonify
from models.review_model import ReviewModel

reviews_bp = Blueprint('reviews_bp', __name__)

@reviews_bp.route('/reviews/<int:book_id>', methods=['GET'])
def get_reviews_by_book_id(book_id):
    reviews = ReviewModel.query.filter_by(book_id=book_id).all()
    reviews_list = [review.to_dict() for review in reviews]
    return jsonify(reviews_list)

