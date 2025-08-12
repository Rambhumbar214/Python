'''Write a Python program to accept n numbers in list and remove duplicates from a list.'''

# Accept the number of elements (n) in the list
n = int(input("Enter the number of elements in the list: "))

# Accept n numbers and store them in a list
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Remove duplicates by converting the list to a set, then back to a list
unique_numbers = list(set(numbers))

# Print the list after removing duplicates
print(f"List after removing duplicates: {unique_numbers}")
