#!/usr/bin/node
/* module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    // Using destructuring assigment (no need of a temp variable)
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}; */

module.exports = class Rectangle {
  constructor (w, h) {
    if ((h <= 0 || h === undefined) || (w <= 0 || w === undefined)) {
      // empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    // using a tempral variable (FWIW look up line 12)
    let tmp = 0;
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
};
