#!/usr/bin/node

// Get the first argument from process.argv
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const num = parseInt(arg);

// Check if the result is a valid number
if (!isNaN(num)) 
{
  console.log(`My number: ${num}`);
} 
else 
{
  console.log('Not a number');
}
