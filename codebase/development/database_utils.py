



import psycopg2


def disconnect_from_database(conn):
    try:
        conn.close()
        print('Database connection closed.')
    except Exception as e:
        print(f'Error closing connection: {e}')



