
const { Pool } = require('pg');

const pool = new Pool({
  user: 'dbuser',
  host: 'database.server.com',
  database: 'mydb',
  password: 'secretpassword',
  port: 5432,
  ssl: {
    rejectUnauthorized: false
  }
});

module.exports = pool;
