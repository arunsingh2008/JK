


from review_aggregator import fetch_reviews, aggregate_reviews
from summary_generator import generate_summary_with_llama3

def generate_review_summary(book_id):
    reviews = fetch_reviews(book_id)
    aggregated_reviews = aggregate_reviews(reviews)
    summary = generate_summary_with_llama3(aggregated_reviews)
    return summary

# Example usage
# book_id = '123'
# print(generate_review_summary(book_id))


