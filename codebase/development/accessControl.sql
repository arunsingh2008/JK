
-- Granting limited privileges to a new user

CREATE ROLE readonly_user WITH LOGIN PASSWORD 'readonlypassword';

-- Grant CONNECT to the database
GRANT CONNECT ON DATABASE mydb TO readonly_user;

-- Grant USAGE on schema
GRANT USAGE ON SCHEMA public TO readonly_user;

-- Grant SELECT on all tables in the public schema
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;

-- Make sure future tables are also accessible
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly_user;
