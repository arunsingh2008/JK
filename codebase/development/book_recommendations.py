


from cache_config import cache
from functools import lru_cache

@lru_cache(maxsize=100)
def get_book_recommendations(user_id):
    # Simulate a time-consuming or resource-intensive operation
    # In a real scenario, this could be a call to a database or an external API
    print(f'Fetching recommendations for user {user_id}')
    return [f'Book {i}' for i in range(5)]

def cache_book_recommendations(user_id):
    if user_id in cache:
        return cache[user_id]
    else:
        recommendations = get_book_recommendations(user_id)
        cache[user_id] = recommendations
        return recommendations

def invalidate_cache(user_id):
    cache.pop(user_id, None)


