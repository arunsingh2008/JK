


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Assuming environment variables are used for credentials
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_CERT_PATH = os.getenv('DATABASE_CERT_PATH')

# Configure database engine with SSL
engine = create_engine(DATABASE_URL, connect_args={'sslmode': 'require', 'sslrootcert': DATABASE_CERT_PATH})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


