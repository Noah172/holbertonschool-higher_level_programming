#!/usr/bin/node
// only prints if is a number
const args = process.argv;
if (parseInt(args[2])) {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}
