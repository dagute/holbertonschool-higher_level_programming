#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  const sum = parseInt(arg);
  for (let i = 0; i < sum; i++) {
    console.log('X'.repeat(sum));
  }
}
