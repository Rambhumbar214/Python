'''Write a Python program to accept and convert string in uppercase or vice versa. '''

# Accept input from the user
input_string = input("Enter a string: ")

# Ask the user for their choice of conversion
conversion_choice = input("Enter 'U' to convert to uppercase or 'L' to convert to lowercase: ")

# Check the user's choice and perform the conversion
if conversion_choice.upper() == 'U':
    # Convert the string to uppercase
    converted_string = input_string.upper()
    print("Converted string in uppercase:", converted_string)
elif conversion_choice.upper() == 'L':
    # Convert the string to lowercase
    converted_string = input_string.lower()
    print("Converted string in lowercase:", converted_string)
else:
    print("Invalid choice! Please enter 'U' for uppercase or 'L' for lowercase.")
