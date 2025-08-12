'''Write a program which prints Fibonacci series of a number. '''

# Number of terms
n = 10

# First two numbers in Fibonacci series
a, b = 0, 1

# Printing the Fibonacci series
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
