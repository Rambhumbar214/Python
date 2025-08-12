''' Write a Python program to count frequency of each character in a given string using user 
defined function.'''

# User-defined function to count frequency of each character
def count_char_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}

    # Iterate through each character in the string
    for char in input_string:
        if char in frequency_dict:
            # Increment the count if the character already exists in the dictionary
            frequency_dict[char] += 1
        else:
            # Add the character to the dictionary with count 1
            frequency_dict[char] = 1

    return frequency_dict

# Accept the string input from the user
input_string = input("Enter a string: ")

# Call the user-defined function to count character frequencies
result = count_char_frequency(input_string)

# Print the character frequencies
print("Character frequencies in the string:")
for char, frequency in result.items():
    print(f"'{char}': {frequency}")
