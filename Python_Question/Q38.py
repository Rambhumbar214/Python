''' Write a Python program which accept an integer value ‘n’ and display all prime numbers 
till ‘n’. '''

# Accept input from the user
n = int(input("Enter an integer n: "))

# Display all prime numbers up to n
print(f"Prime numbers up to {n}:")

# Loop through numbers from 2 to n
for num in range(2, n + 1):
    is_prime = True  # Assume the number is prime
    
    # Check if num is divisible by any number between 2 and sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # If is_prime is still True, then the number is prime
    if is_prime:
        print(num, end=" ")
