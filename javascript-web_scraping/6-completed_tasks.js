#!/usr/bin/node
const url = 'https://jsonplaceholder.typicode.com/todos' + '?completed=true';
const request = require('request');
request.get(url, (err, response, body) => {
  if (err) throw err;
  console.log(JSON.parse(body));
});
