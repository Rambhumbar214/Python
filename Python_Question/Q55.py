'''Write a Sequential search function which searches an item in a sorted list. The function 
should return the index of element to be searched in the list.'''

# Function to perform sequential search
def sequential_search(sorted_list, target):
    for index in range(len(sorted_list)):
        if sorted_list[index] == target:
            return index  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Sample sorted list
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]

# Accept the item to be searched from the user
target = int(input("Enter the number to search: "))

# Perform the search
index = sequential_search(sorted_list, target)

# Display the result
if index != -1:
    print(f"Item found at index {index}")
else:
    print("Item not found in the list.")
