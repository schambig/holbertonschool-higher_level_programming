#!/usr/bin/node
/*
exporting a named function:
http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html
*/
// exports.add = function add (a, b) {
//   return a + b;
// };

const add = (a, b) => a + b;
module.exports = { add };
