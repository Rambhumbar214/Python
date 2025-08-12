'''Write a Python program to sort (ascending and descending) a dictionary by value. '''

# Sample dictionary
sample_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

# Sort the dictionary by value in ascending order
ascending_order = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

# Sort the dictionary by value in descending order
descending_order = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

# Display the results
print("Original Dictionary:", sample_dict)
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)
