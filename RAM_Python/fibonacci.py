
n = int(input("Enter a number: "))


a, b = 0, 1


print("Fibonacci series:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b  
