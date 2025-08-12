'''Write a Python program to match key values in two dictionaries. [20 M] 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2} 
Expected output: key1: 1 is present in both x and y'''
# Define two dictionaries
dict_x = {'key1': 1, 'key2': 3, 'key3': 2}
dict_y = {'key1': 1, 'key2': 2}

# Iterate through items in dict_x
for key, value in dict_x.items():
    # Check if the key exists in dict_y and the values match
    if key in dict_y and dict_y[key] == value:
        print(f"{key}: {value} is present in both x and y")
