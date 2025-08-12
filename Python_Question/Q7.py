'''Write a Python program to find the repeated items of a tuple.'''
from collections import Counter

# Define the tuple
my_tuple = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Count the occurrences of each element
element_counts = Counter(my_tuple)

# Identify elements that appear more than once
repeated_items = [item for item, count in element_counts.items() if count > 1]

# Display the repeated items
print(f"Repeated items: {repeated_items}")
