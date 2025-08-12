"""write a sequential search function whcih searches
an item in a sorted list the function should
return the index of element to be searched in the list"""


sorted_list = [1, 3, 5, 7, 9, 11]
target = int(input("Enter the element to search: "))

index = -1


for i in range(len(sorted_list)):
    if sorted_list[i] == target:
        index = i
        break


if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
