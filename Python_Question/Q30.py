''' Write a Python program to accept n numbers in list. Find average of list and sort it in 
descending order'''

# Accept the number of elements (n) in the list
n = int(input("Enter the number of elements in the list: "))

# Accept n numbers and store them in a list
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Calculate the average of the list
average = sum(numbers) / len(numbers)

# Sort the list in descending order
numbers.sort(reverse=True)

# Print the average and the sorted list
print(f"Average of the list: {average}")
print(f"Sorted list in descending order: {numbers}")

