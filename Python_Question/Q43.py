'''Write a Python program to create tuple of n numbers, print the first half values of tuple in 
one line and the last half values of tuple on next line. 
'''

# Accept input from the user for the number of elements
n = int(input("Enter the number of elements: "))

# Accept n numbers from the user and create a tuple
numbers = tuple(int(input(f"Enter number {i+1}: ")) for i in range(n))

# Calculate the middle index to split the tuple
mid_index = n // 2

# Print the first half of the tuple
print("First half of the tuple:")
print(numbers[:mid_index])

# Print the second half of the tuple
print("Second half of the tuple:")
print(numbers[mid_index:])
