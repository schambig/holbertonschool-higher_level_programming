#!/usr/bin/node
/*
objects in js are mutable values that store `label:value` related data
that pais is also known as `property`, we can access properties through
dot notation
*/
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
