'''Write a Python program to print the set difference and a symmetric difference of two sets. '''

# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Set Difference: Elements in set_a but not in set_b
difference_ab = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference_ab)

# Symmetric Difference: Elements in either set_a or set_b but not in both
symmetric_diff_ab = set_a.symmetric_difference(set_b)
print("Symmetric Difference (set_a ^ set_b):", symmetric_diff_ab)
