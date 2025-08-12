'''Write a Python program to display occurrence of the elements in the tuple, which appears 
more than 2 times. ''' 
from collections import Counter

# Sample tuple
sample_tuple = ('a', 'b', 'c', 'a', 'b', 'a', 'd', 'e', 'b', 'a')

# Count the frequency of each element
element_counts = Counter(sample_tuple)

# Display elements that appear more than twice
for element, count in element_counts.items():
    if count > 2:
        print(f"Element '{element}' appears {count} times.")
