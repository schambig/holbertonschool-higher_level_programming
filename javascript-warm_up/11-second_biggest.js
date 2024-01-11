#!/usr/bin/node
// if (isNaN(process.argv[2]) || process.argv.length === 3) {
//   console.log('0');
// } else {
//   // `sort((a, b) => b - a)` is the same as `sort(function(a ,b){return b -a})`
//   const secBiggest = process.argv.slice(2).sort((a, b) => b - a)[1];
//   console.log(secBiggest);
// }

// Number. only returns tru if the value is of type `number` and is `NaN`
// if (Number.isNaN(process.argv[2]) || process.argv.length === 3) {
if (isNaN(process.argv[2]) || process.argv.length === 3) {
  console.log('0');
} else {
  const numbers = process.argv.slice(2).map(Number); // Convert cli args to numbers
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sort numbers in cescending
  const secondLargest = sortedNumbers[1]; // Get the second largest number
  console.log(secondLargest);
}
