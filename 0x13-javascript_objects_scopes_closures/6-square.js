#!/usr/bin/node
const SquareA = require('./5-square.js');

class Square extends SquareA {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let height = 0; height < this.height; height++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
