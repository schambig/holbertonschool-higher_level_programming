#!/usr/bin/node
/* module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print(); // use print method from Rectangle class
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}; */

const SquareOne = require('./5-square');

module.exports = class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // just assing 'X' to c variable (look up line 5)
      }
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
};
