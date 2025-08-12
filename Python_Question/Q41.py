'''Write a Sequential search function which searches an item in a sorted list. The function 
should return the index of element to be searched in the list. '''

def sequential_search(sorted_list, item):
    # Iterate through the list and check each element
    for index in range(len(sorted_list)):
        if sorted_list[index] == item:
            return index  # Return the index of the found item
    
    # Return -1 if the item is not found
    return -1

# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
item = int(input("Enter the item to search for: "))

index = sequential_search(sorted_list, item)

if index != -1:
    print(f"Item {item} found at index {index}.")
else:
    print(f"Item {item} not found in the list.")
