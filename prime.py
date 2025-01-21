"""write a program which accept an
integer value n and display all prime numbers till n"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("Enter an integer n: "))


print(f"Prime numbers up to {n}:")
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")
