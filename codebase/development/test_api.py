

import unittest
from app import create_app, db
from app.models import User
from config import TestConfig

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_endpoint(self):
        # Add a test user
        user = User(username='testuser')
        db.session.add(user)
        db.session.commit()

        # Test GET request
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', response.get_json()['users'])

if __name__ == '__main__':
    unittest.main()

