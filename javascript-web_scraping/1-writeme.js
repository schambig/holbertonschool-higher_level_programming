#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error) => {
  console.log(erro);
});
