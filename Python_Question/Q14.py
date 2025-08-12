''' Write a Python program to create and display all combinations of letters, selecting each 
letter from a different key in a dictionary. [20 M] 
Sample data: {'1':['a','b'], 2':['c','d']} 
Expected Output: 
ac 
ad 
bc 
bd '''
import itertools

# Sample dictionary
data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Generate all combinations
combinations = itertools.product(*data.values())

# Display each combination
for combination in combinations:
    print(''.join(combination))
