#!/usr/bin/node
function add(a, b) {
  let x1 = parseInt(a);
  let x2 = parseInt(b);
  console.log(x1 + x2);
}
add(process.argv[2], process.argv[3]);
