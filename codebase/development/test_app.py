


import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome', response.data.decode('utf-8'))

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('About', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()


