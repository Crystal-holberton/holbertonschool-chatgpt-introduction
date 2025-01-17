#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given number n using recursion.
# It multiplies the number n by the factorial of n-1 until n reaches 0,
# where it returns 1 as the base case to terminate the recursion.

# Parameters:
# n (int): The integer input for which the factorial is to be calculated. 
#          The function assumes n is a non-negative integer.

# Returns:
# int: The factorial of the number n. 
#       For example, factorial(4) will return 24.

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case

f = factorial(int(sys.argv[1]))  # Convert the first command-line argument to an integer and pass it to the factorial function
print(f)  # Print the result
