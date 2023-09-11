#!/usr/bin/node

// Define the factorial function recursively
function factorial(n) {
  // Base case: factorial of 0 is 1
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    // Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n - 1);
  }
}
// Get the first argument from process.argv
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Check if the argument is valid
if (!isNaN(num)) {
  // Call the factorial function and print the result
  console.log(factorial(num));
} else {
  console.log(1); // Factorial of NaN is 1
}
