'''Write a Python program to define class to find validity of a string of parentheses, '(', ')', '{', 
'}', '[' and ']. These brackets must be in the correct order, for example "()" and "()[]{}" are valid 
but "[)", "({[)]" and "{{{" are invalid.'''

# Accept the input string from the user
input_string = input("Enter a string of parentheses: ")

# Initialize a stack to keep track of opening parentheses
stack = []

# Dictionary to match closing brackets with their opening counterparts
bracket_map = {')': '(', '}': '{', ']': '['}

# Variable to keep track of validity
is_valid = True

# Iterate over each character in the string
for char in input_string:
    if char in bracket_map:  # If the character is a closing bracket
        # Check if the stack is empty or if the top element of the stack doesn't match the current closing bracket
        if not stack or stack[-1] != bracket_map[char]:
            is_valid = False
            break
        else:
            stack.pop()  # Pop the opening bracket from the stack
    else:  # If it's an opening bracket
        stack.append(char)

# After the loop, check if the stack is empty (all brackets were matched)
if stack:
    is_valid = False

# Output the result based on validity
if is_valid:
    print("The string has valid parentheses.")
else:
    print("The string has invalid parentheses.")
