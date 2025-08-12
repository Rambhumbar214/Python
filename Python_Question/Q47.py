'''Write a Python program which accepts an integer value ‘n’ and display all prime 
numbers till ‘n’.'''

# Accept an integer input from the user
n = int(input("Enter a number: "))

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print all prime numbers up to n
print(f"Prime numbers up to {n}:")
for number in range(2, n+1):
    if is_prime(number):
        print(number, end=" ")
