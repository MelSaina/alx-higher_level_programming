#!/usr/bin/node

if (process.argv[2] && process.argv[3])
{
	// Print the two arguments in the specified format
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
else
{
	
	console.log('undefined is undefined');
}
