

import psycopg2

# Connect application to RDS
DB_NAME = 'mydatabase'
DB_USER = 'admin'
DB_PASSWORD = 'password'
DB_HOST = '<your-rds-endpoint>'
DB_PORT = '5432'

try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = connection.cursor()
    # Test query
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    print('Connected to:', db_version)
except Exception as e:
    print('Database connection failed due to', e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Database connection closed.')


