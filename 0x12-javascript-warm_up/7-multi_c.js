#!/usr/bin/node
const args = process.argv;

if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let print = args[2]; print > 0; print--) {
    console.log('C is fun');
  }
}
