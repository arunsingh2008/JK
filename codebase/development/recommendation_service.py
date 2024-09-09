



from cache_manager import CacheManager

class RecommendationService:
    def __init__(self):
        self.cache_manager = CacheManager(host='your-elasticache-host', port=6379, db=0)

    def store_recommendations(self, user_id, book_recommendations):
        if self.cache_manager.cache_recommendations(user_id, book_recommendations):
            print('Recommendations cached successfully.')
        else:
            print('Failed to cache recommendations.')

    def retrieve_recommendations(self, user_id):
        recommendations = self.cache_manager.get_recommendations(user_id)
        if recommendations:
            print('Recommendations retrieved from cache.')
        else:
            print('No recommendations found in cache.')
        return recommendations



