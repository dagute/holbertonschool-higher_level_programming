#!/usr/bin/node
function sum (a, b) {
  let x1 = parseInt(a);
  let x2 = parseInt(b);
  console.log(x1 + x2);
}
sum(process.argv[2], process.argv[3]);
