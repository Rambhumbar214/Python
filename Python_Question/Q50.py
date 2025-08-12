''' Write a Python program to accept n elements in a set and find the length of a set, maximum, 
minimum value and the sum of values in a set. (Don’t use built-in function'''


# Accept input for the number of elements
n = int(input("Enter the number of elements: "))

# Create an empty set
my_set = set()

# Accept n elements and add them to the set
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_set.add(element)

# Calculating the length of the set manually
length = 0
for _ in my_set:
    length += 1

# Calculating the maximum value manually
max_value = None
for value in my_set:
    if max_value is None or value > max_value:
        max_value = value

# Calculating the minimum value manually
min_value = None
for value in my_set:
    if min_value is None or value < min_value:
        min_value = value

# Calculating the sum manually
total_sum = 0
for value in my_set:
    total_sum += value

# Output the results
print(f"Length of the set: {length}")
print(f"Maximum value in the set: {max_value}")
print(f"Minimum value in the set: {min_value}")
print(f"Sum of the values in the set: {total_sum}")
