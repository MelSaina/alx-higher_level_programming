#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

try {
  const data1 = fs.readFileSync(file1Path, 'utf8');
  const data2 = fs.readFileSync(file2Path, 'utf8');
  const concatenatedData = data1 + data2;

  fs.writeFileSync(destinationPath, concatenatedData);
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
