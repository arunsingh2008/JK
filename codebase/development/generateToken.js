
const jwt = require('jsonwebtoken');
require('dotenv').config();

const generateAccessToken = (username) => {
  return jwt.sign(username, process.env.ACCESS_TOKEN_SECRET, { expiresIn: '1800s' });
};

module.exports = { generateAccessToken };
