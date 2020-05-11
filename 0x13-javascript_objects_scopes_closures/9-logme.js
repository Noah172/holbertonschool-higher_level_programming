#!/usr/bin/node
let c = 0;
exports.logMe = function (i) {
  console.log(`${c}: ${i}`);
  c += 1;
};
