'''Write a Python program to remove special symbols/Punctuation from a given string'''

import string

# Accept the input string from the user
input_string = input("Enter a string: ")

# Remove punctuation and special symbols
output_string = ''.join(char for char in input_string if char not in string.punctuation)

# Display the result
print("String after removing punctuation and special symbols:")
print(output_string)
