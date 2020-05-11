#!/usr/bin/node
const args = process.argv.slice(2);
let fs = require('fs');
let first = fs.readFileSync('./' + args[0]);
let second = fs.readFileSync('./' + args[1]);
fs.writeFileSync(args[2], first + '\n' + second + '\n');
