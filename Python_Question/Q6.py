'''Write a Python program to perform given operations on set. [20 M] 
a. check whether 2 sets are equal or not 
b. Symmetric difference 
c. Intersection of sets 
d. Find maximum and the minimum value in a set.'''
# Define two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# a. Check whether the two sets are equal
are_sets_equal = set1 == set2
print(f"Are set1 and set2 equal? {are_sets_equal}")

# b. Symmetric difference between set1 and set2
symmetric_diff = set1 ^ set2
print(f"Symmetric difference between set1 and set2: {symmetric_diff}")

# c. Intersection of set1 and set2
intersection = set1 & set2
print(f"Intersection of set1 and set2: {intersection}")

# d. Find maximum and minimum values in set1
max_value = max(set1)
min_value = min(set1)
print(f"Maximum value in set1: {max_value}")
print(f"Minimum value in set1: {min_value}")
