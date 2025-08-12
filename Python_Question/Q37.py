''') Write a Python program to create a tuple of n numbers and print maximum, minimum, and 
sum of elements in a tuple.'''

# Accept input from the user for the number of elements
n = int(input("Enter the number of elements: "))

# Accept n numbers from the user and create a tuple
numbers = tuple(int(input(f"Enter number {i+1}: ")) for i in range(n))

# Calculate the maximum, minimum, and sum of the elements in the tuple
max_value = max(numbers)
min_value = min(numbers)
sum_value = sum(numbers)

# Print the results
print(f"Tuple: {numbers}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Sum of elements: {sum_value}")
