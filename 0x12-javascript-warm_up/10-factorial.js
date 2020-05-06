#!/usr/bin/node
const arg = Number(process.argv[2]);

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}

function factorial (n) {
  if (n === 1) {
    return n;
  }
  return n * factorial(n - 1);
}
