



import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Parameters for database connection
params = {
    'database': 'your_database_name',
    'user': 'your_database_user',
    'password': 'your_database_password',
    'host': 'localhost',
    'port': '5432'
}

# Connect to PostgreSQL server
conn = psycopg2.connect(**params)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
# Create database
try:
    cursor.execute('CREATE DATABASE ' + params['database'])
except psycopg2.errors.DuplicateDatabase:
    print('Database already exists')

# Close connection to server
cursor.close()
conn.close()

# Connect to the newly created database
db_conn = psycopg2.connect(**params)
db_cursor = db_conn.cursor()

# Create tables
commands = (
    '''
    CREATE TABLE books (
        book_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        published_date DATE NOT NULL
    )
    ''',
    '''
    CREATE TABLE reviews (
        review_id SERIAL PRIMARY KEY,
        book_id INTEGER NOT NULL,
        review_text TEXT NOT NULL,
        rating INTEGER NOT NULL,
        FOREIGN KEY (book_id)
            REFERENCES books (book_id)
            ON UPDATE CASCADE ON DELETE CASCADE
    )
    '''
)

# Execute commands
for command in commands:
    db_cursor.execute(command)

db_conn.commit()

# Close communication with the database
db_cursor.close()
db_conn.close()




