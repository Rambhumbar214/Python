'''Write a Python program to find the length of a string without using built-in function'''

def string_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

# Example usage
sample_string = "Hello, World!"
length = string_length(sample_string)
print(f"The length of the string is: {length}")
