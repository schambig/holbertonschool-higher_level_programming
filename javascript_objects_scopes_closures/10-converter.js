#!/usr/bin/Node
/* exports.converter = function (base) {
  return num => num.toString(base);
}; */

exports.converter = function (base) {
  function num (x) {
    return (parseInt(x, 10).toString(base));
  }
  return (num);
};
