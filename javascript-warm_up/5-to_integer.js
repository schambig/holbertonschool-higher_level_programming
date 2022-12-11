#!/usr/bin/node
// `isNaN(...) === true` also works, but it is redundant
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
