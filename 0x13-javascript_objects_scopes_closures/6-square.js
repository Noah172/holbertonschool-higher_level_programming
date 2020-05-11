#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let he = 0; he < this.height; he++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
