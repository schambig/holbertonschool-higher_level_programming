#!/usr/bin/node
// function factorial (n) {
//   return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
// }
// console.log(factorial(Number(process.argv[2])));

function factorial (n) {
  return (n === 0 || Number.isNaN(n)) ? 1 : n * factorial(n - 1);
}
// const arg = parseInt(process.argv[2])
// const arg = Number(process.argv[2])
const arg = +process.argv[2]; // using unary operator '+'
const result = factorial(arg);

console.log(result);
