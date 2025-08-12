''') Write a Python function to multiply all the numbers in a list. [20 M] 
Sample-List: (8, 2, 3, -1, 7) 
Expected Output: -336 '''

def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Sample list
sample_list = [8, 2, 3, -1, 7]

# Function call and output
output = multiply_numbers(sample_list)
print(f"Expected Output: {output}")
