'''Write a Python program to match key values in two dictionaries. [20 M] 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2} 
Expected output: key1: 1 is present in both x and y'''

# Define two dictionaries
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

# Iterate through the first dictionary
for key, value in x.items():
    # Check if the key exists in the second dictionary with the same value
    if key in y and y[key] == value:
        print(f"{key}: {value} is present in both x and y")
