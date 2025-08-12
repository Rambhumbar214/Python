''' Write a Python program to count frequency of each character in a given string using user 
defined function. '''

def count_char_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}

    # Iterate over each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

# Sample string
sample_string = 'Hello all'

# Call the function and store the result
char_frequencies = count_char_frequency(sample_string)

# Display the character frequencies
print(char_frequencies)
