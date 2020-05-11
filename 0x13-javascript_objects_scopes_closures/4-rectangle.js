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

  rotate () {
    const hold = this.height;
    this.height = this.width;
    this.width = hold;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
