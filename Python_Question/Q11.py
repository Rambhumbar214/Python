'''Write a function to calculate the sum of numbers from 0 to n. '''

def sum_numbers(n):
    return sum(range(n + 1))

# Example usage:
n = 10
result = sum_numbers(n)
print(f"The sum of numbers from 0 to {n} is {result}")
