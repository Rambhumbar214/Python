'''Write a Python program to sort the tuple T=(4,2,6.8,1.8,10) .'''
# Define the tuple
T = (4, 2, 6.8, 1.8, 10)

# Convert the tuple to a list
T_list = list(T)

# Sort the list in ascending order
T_list.sort()

# Convert the list back to a tuple
T_sorted = tuple(T_list)

# Display the sorted tuple
print("Sorted tuple:", T_sorted)
