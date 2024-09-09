



import psycopg2

# Define connection parameters
DB_NAME = 'your_dbname'
DB_USER = 'your_dbuser'
DB_PASS = 'your_dbpassword'
DB_HOST = 'your_dbhost'
DB_PORT = '5432'

# Method to establish a connection to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print('Connected to the database successfully')
        return conn
    except Exception as e:
        print('Database connection failed')
        print(e)
        return None



