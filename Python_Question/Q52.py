'''Write a Python program to calculate the average of numbers in a given list. '''

# Accept a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the sum of all numbers in the list
total_sum = sum(numbers)

# Calculate the number of elements in the list
count = len(numbers)

# Calculate the average (sum divided by the number of elements)
if count > 0:
    average = total_sum / count
else:
    average = 0  # In case of an empty list

# Print the average
print(f"The average of the numbers is: {average}")
