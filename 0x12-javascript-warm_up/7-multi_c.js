#!/usr/bin/node

// Get the first argument from process.argv
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const num = parseInt(arg);

// Check if the argument is a valid number
if (!isNaN(num) && num > 0) 
{
  	for (let i = 0; i < num; i++) 
	{
   		console.log("C is fun");
	}
} 
else 
{
  console.log("Missing number of occurrences");
}
