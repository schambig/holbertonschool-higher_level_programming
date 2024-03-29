#!/usr/bin/node
/* module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // the 2 lines bellow also can be represented by:
      // [this.width, this.height] = [w, h] (one liner)
      this.width = w;
      this.height = h;
    }
  }
};
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if ((h <= 0 || h === undefined) || (w <= 0 || w === undefined)) {
      // empty object
    } else {
      this.width = w;
      this.height = h;
      // also [this.width, this.height] = [w, h]
    }
  }
};
