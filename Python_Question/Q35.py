'''Write a Python program to accept a string and from a given string where all occurrences of 
its first character have been changed to '$', except the first char itself.'''

# Accept the string from the user
input_string = input("Enter a string: ")

# Get the first character of the string
first_char = input_string[0]

# Replace all occurrences of the first character with '$', except the first occurrence
modified_string = first_char + input_string[1:].replace(first_char, '$')

# Display the modified string
print("Modified string:", modified_string)
