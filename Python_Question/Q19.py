''' Write a Python program to print average of all elements of sets.'''

# Define a set of numbers
numbers_set = {10, 20, 30, 40, 50}

# Calculate the sum of the elements
total_sum = sum(numbers_set)

# Count the number of elements
count = len(numbers_set)

# Compute the average
average = total_sum / count if count != 0 else 0  # Avoid division by zero

# Display the result
print(f"The average of the set elements is: {average}")
