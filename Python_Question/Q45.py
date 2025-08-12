''') Write a Python program to check if a given key already exists in a dictionary. If key exists 
replace with another key/value pair. '''

# Define a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accept the key and the new value from the user
key_to_check = input("Enter the key to check: ")
new_value = input("Enter the new value for the key: ")

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists. Replacing with new value...")
    my_dict[key_to_check] = new_value  # Replace the value for the existing key
else:
    print(f"Key '{key_to_check}' does not exist. Adding a new key-value pair...")
    my_dict[key_to_check] = new_value  # Add the new key-value pair to the dictionary

# Print the updated dictionary
print("Updated Dictionary:", my_dict)
