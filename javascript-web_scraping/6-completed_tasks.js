#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const completed = {};
    const todos = JSON.parse(body);
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
