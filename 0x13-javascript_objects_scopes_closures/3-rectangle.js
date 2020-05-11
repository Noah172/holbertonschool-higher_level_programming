#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let he = 0; he < this.height; he++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
