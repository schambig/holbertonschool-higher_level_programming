#!/usr/bin/node
const fs = require('fs');
/*
first argument in readFile function: path or the file you want to read
second argument: optional object in this case encoding utf-8
third argument: a callback function executed when the file is read,
  this callback function has two arguments: an error object and the
  data from teh file
*/
fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  console.log(error || content);
});
