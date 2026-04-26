const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

const staticDir = path.resolve(__dirname, '..', '..', 'frontend');

app.use(express.static(staticDir));

app.get('/', (req, res) => {
  res.sendFile(path.join(staticDir, 'html', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

