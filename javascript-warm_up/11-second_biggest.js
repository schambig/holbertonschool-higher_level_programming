#!/usr/bin/node
if (isNaN(process.argv[2]) || parseInt(process.argv[2]) === 1) {
  console.log('0');
} else {
  const secBiggest = process.argv.slice(2).sort((a, b) => (b - a))[1];
  console.log(secBiggest);
}
