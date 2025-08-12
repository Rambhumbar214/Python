'''Write a Python function to get a string made of the first 2 and the last 2 chars from a given 
string. If the string length is less than 2, it return empty string. 
Sample String: 'General12' Expected Result: 'Ge12' 
Sample String: 'Ka' Expected Result: 'KaKa' 
Sample String: ' K' Expected Result: Empty String '''

# Function to get the first 2 and last 2 characters
def get_substring(input_string):
    # Check if the string length is less than 2
    if len(input_string) < 2:
        return ""  # Return an empty string if length is less than 2
    else:
        # Extract the first 2 and last 2 characters
        return input_string[:2] + input_string[-2:]

# Test the function with different sample strings
sample_string1 = "General12"
sample_string2 = "Ka"
sample_string3 = " K"

# Display the results
print(get_substring(sample_string1))  # Expected: 'Ge12'
print(get_substring(sample_string2))  # Expected: 'KaKa'
print(get_substring(sample_string3))  # Expected: ''
