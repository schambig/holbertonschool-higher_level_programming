#!/usr/bin/node
/* module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}; */

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
