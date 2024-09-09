

const express = require('express');
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const swaggerDocument = YAML.load('./swagger.yaml');

const app = express();
const port = 3000;

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
app.get('/users', (req, res) => {
  res.json(['Alice', 'Bob']);
});
app.get('/users/:userId', (req, res) => {
  res.json({ id: req.params.userId, name: 'Alice' });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

