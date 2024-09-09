

import requests
import unittest
from integration_test_config import IntegrationTestConfig

class TestAppIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up test environment
        cls.base_url = IntegrationTestConfig.TEST_SERVER_URL

    def test_home_page(self):
        # Test case for home page
        response = requests.get(f'{self.base_url}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome', response.text)

    def test_database_connection(self):
        # Test case for database connection
        response = requests.get(f'{self.base_url}/db-test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Database connection successful', response.text)

if __name__ == '__main__':
    unittest.main()


