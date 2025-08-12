'''Write a Python program to print a dictionary where the keys are numbers between 1 and 
15 (both included) and the values are square of keys. 
Sample Dictionary: {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500} '''

# Create a dictionary using dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 16)}

# Print the resulting dictionary
print(squares_dict)
