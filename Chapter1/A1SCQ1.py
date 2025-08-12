sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the element to search for: "))

index = -1
for i, element in enumerate(sorted_list):
    if element == target:
        index = i
        break

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
