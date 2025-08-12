''') Write a Python program which prints fibonacci series of a number.'''

# Accept the input from the user for the number of terms in the Fibonacci series
n = int(input("Enter a number to generate Fibonacci series up to: "))

# Initialize the first two numbers of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci series:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
