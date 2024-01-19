#!/usr/bin/node
/* let count = 0;
exports.logMe = function (item) { console.log(count++ + ':' + item); };
// console.log is executed with the current value of i then, is incremented by 1
*/

let i = 0;
exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
  // ++i; // in this case works the same as line above above
};

/* heads up: `i` is not a global variable in this context but rather belongs to the module or script scope.

In JavaScript, variables declared outside of a function, as i is in this case, maintain their value
between function calls. This is because i is defined in the same scope as the logMe function,
so it's accessible and modifiable within the function.

When you call the logMe function for the first time, i starts with a value of 0, which is incremented
after its current value is used (console.log(i + ': ' + item);). Then, i becomes 1.

The value of i persists because it is defined in the outer scope of the logMe function.
Therefore, each time you call logMe, i retains its incremented value from the previous call.
This allows you to keep track of how many times the logMe function has been called and maintain
a sequential count. */
