


const express = require('express');
const https = require('https');
const fs = require('fs');
const bodyParser = require('body-parser');
const basicAuth = require('express-basic-auth');

const app = express();

app.use(bodyParser.json());

app.use(basicAuth({
    users: { 'admin': 'supersecret' }
}));

app.get('/api/data', (req, res) => {
    res.json({ message: 'Secure data accessed' });
});

https.createServer({
    key: fs.readFileSync('server.key'),
    cert: fs.readFileSync('server.cert')
}, app)
.listen(3000, () => {
    console.log('Listening on port 3000');
});


