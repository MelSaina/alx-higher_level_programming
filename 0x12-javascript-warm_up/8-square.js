#!/usr/bin/node

// Get the size argument from process.argv
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const size = parseInt(arg);

// Check if the argument is a valid positive integer
if (!isNaN(size) && size > 0) 
{
  	for (let i = 0; i < size; i++) 
	{
		let line = '';
		for (let j = 0; j < size; j++) 
		{
			line += 'X';
		}
		console.log(line);
	}
} 
else 
{
  console.log("Missing size");
}
