''' Write a Python program to generate and print a dictionary that contains a number (between 
1 and n) in the form (x, x*x). 
Sample Dictionary (n = 5) 
Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25'''

# Accept input from the user for the value of n
n = int(input("Enter a number n: "))

# Generate and print the dictionary
square_dict = {x: x*x for x in range(1, n+1)}

# Display the generated dictionary
print("Generated Dictionary:", square_dict)
