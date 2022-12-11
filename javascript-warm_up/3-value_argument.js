#!/usr/bin/node
if (process.argv[2] === undefined) {
// if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
