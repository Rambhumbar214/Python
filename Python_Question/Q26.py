'''Write a Python program to create a dictionary from a string. 
Sample String: ’Hello all’ 
Expected output: {'e': 1, 'o': 1, 'a': 1, 'l': 4, 'H': 1} '''

from collections import Counter

# Sample string
sample_string = 'Hello all'

# Create a dictionary using Counter
char_count = dict(Counter(sample_string))

# Display the dictionary
print(char_count)
