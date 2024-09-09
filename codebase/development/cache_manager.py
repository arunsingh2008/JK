



import redis
import json

class CacheManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def cache_recommendations(self, user_id, recommendations):
        try:
            self.r.set(user_id, json.dumps(recommendations))
            return True
        except Exception as e:
            print(f'Error caching recommendations: {e}')
            return False

    def get_recommendations(self, user_id):
        try:
            recommendations = self.r.get(user_id)
            if recommendations:
                return json.loads(recommendations)
            else:
                return []
        except Exception as e:
            print(f'Error retrieving recommendations: {e}')
            return []



