''' Write a Python program to unpack a tuple in several variables. Display type of each 
variable. '''

# Define a tuple
sample_tuple = (42, "Hello", 3.14, True)

# Unpack the tuple into variables
integer_var, string_var, float_var, bool_var = sample_tuple

# Display the value and type of each variable
print(f"integer_var = {integer_var}, type = {type(integer_var)}")
print(f"string_var = {string_var}, type = {type(string_var)}")
print(f"float_var = {float_var}, type = {type(float_var)}")
print(f"bool_var = {bool_var}, type = {type(bool_var)}")
