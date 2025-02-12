def sequential_search(sorted_list, item):
    
    for index in range(len(sorted_list)):
        
        if sorted_list[index] == item:
            return index
        
        elif sorted_list[index] > item:
            break
    return -1  


sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
item = int(input("Enter an item to search: "))
index = sequential_search(sorted_list, item)

if index != -1:
    print(f"Item found at index: {index}")
else:
    print("Item not found in the list.")
