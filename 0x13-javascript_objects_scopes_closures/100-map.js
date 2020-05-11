#!/usr/bin/node

const d = require('./100-data.js').list;
console.log(d);
console.log(d.map((i, j) => i * j));
