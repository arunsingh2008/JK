
import psycopg2


def setup_database_connection():
    connection_parameters = {
        'dbname': 'your_database_name',
        'user': 'your_database_user',
        'password': 'your_database_password',
        'host': 'your_database_host',
        'port': 'your_database_port'
    }
    try:
        connection = psycopg2.connect(**connection_parameters)
        print('Database connection established')
        return connection
    except Exception as error:
        print(f'Error connecting to the database: {error}')
        return None
