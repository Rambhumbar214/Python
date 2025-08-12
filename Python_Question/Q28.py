''' Write a Python program to accept the strings which contains all vowels.'''

# Accept input string from the user
input_string = input("Enter a string: ")

# Convert the string to lowercase to make the check case-insensitive
input_string = input_string.lower()

# Define the set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Check if all vowels are in the input string
if vowels.issubset(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
