''' Write a Python program to accept string and remove the characters which have odd index 
values of a given string using user defined function. '''

def remove_odd_index_characters(input_string):
    # Initialize an empty string to store the result
    result = ""
    # Iterate through the string by index
    for i in range(len(input_string)):
        # Check if the index is even
        if i % 2 == 0:
            result += input_string[i]
    return result

# Example usage
sample_string = "Hello, World!"
modified_string = remove_odd_index_characters(sample_string)
print(f"Original String: {sample_string}")
print(f"Modified String: {modified_string}")
