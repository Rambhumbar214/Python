''') Write a Python program to find set difference, union, intersection and symmetric 
difference.'''

# Define two sets
set_a = {1, 2, 3, 5, 7, 9}
set_b = {2, 4, 6, 7, 9, 0}

# Union of set_a and set_b
union_set = set_a | set_b
print(f"Union of set_a and set_b: {union_set}")

# Intersection of set_a and set_b
intersection_set = set_a & set_b
print(f"Intersection of set_a and set_b: {intersection_set}")

# Difference of set_a and set_b
difference_set = set_a - set_b
print(f"Difference of set_a and set_b (set_a - set_b): {difference_set}")

# Symmetric Difference of set_a and set_b
symmetric_difference_set = set_a ^ set_b
print(f"Symmetric Difference of set_a and set_b: {symmetric_difference_set}")
