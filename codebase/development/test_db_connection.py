


import unittest
from sqlalchemy.exc import SQLAlchemyError
from db_config import SessionLocal

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        """Test database connection security."""
        try:
            # Attempt to create a session and query the database
            db = SessionLocal()
            db.execute('SELECT 1')
            db.close()
        except SQLAlchemyError as e:
            self.fail(f'Database connection failed: {e}')

if __name__ == '__main__':
    unittest.main()


