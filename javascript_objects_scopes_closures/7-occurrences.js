#!/usr/bin/node
/* exports.nbOccurences = function (list, searchElement) {
  // filter return an array of the same element, use arrow function syntax
  return list.filter(element => element === searchElement).length;
}; */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) { ++count; }
  }

  return (count);
};
