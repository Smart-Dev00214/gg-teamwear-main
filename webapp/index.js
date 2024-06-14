import express from 'express';
import path from 'path';

const app = express();
const port = 5000;
const distFolder = "./dist";

//const webRoot = path.join(__dirname, distFolder);

app.use(express.static(distFolder));

app.listen(port);
