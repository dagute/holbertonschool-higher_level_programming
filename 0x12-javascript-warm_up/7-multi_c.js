#!/usr/bin/node
const n = process.argv[2];
if (isNaN(n, 10)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(n); i++) {
    console.log('C is fun');
  }
}
