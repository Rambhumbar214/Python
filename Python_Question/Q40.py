'''Write a python program to check if a string is a Palindrome or not. '''

# Accept the input string from the user
input_string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for case-insensitive comparison
processed_string = input_string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if processed_string == processed_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
