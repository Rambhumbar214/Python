''' Write a Python program to create a dictionary from two lists without losing duplicate 
values. 
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3] 
 
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': 
 
{3}, 'Class-V': {1}}) '''

from collections import defaultdict

# Sample lists
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]

# Initialize a defaultdict with set as the default factory
class_dict = defaultdict(set)

# Iterate over both lists simultaneously
for class_name, class_id in zip(class_list, id_list):
    class_dict[class_name].add(class_id)

# Display the resulting dictionary
print(class_dict)
