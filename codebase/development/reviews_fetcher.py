

import requests

def fetch_reviews(book_id):
    # Assuming there's an API to fetch reviews by book ID
    api_url = f'https://example.com/api/books/{book_id}/reviews'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to fetch reviews')

