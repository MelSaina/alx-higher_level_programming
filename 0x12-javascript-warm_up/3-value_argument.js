#!/usr/bin/node

// Check if there is at least one argument (the first two elements in process.argv are node and the script name)
if (process.argv[2]) 
{
// Print the first argument
  console.log(process.argv[2]);
} 
else 
{
  // No arguments were passed
  console.log("No argument");
}
