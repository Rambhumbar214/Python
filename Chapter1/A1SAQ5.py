n = int(input("Enter a number: "))  

a, b = 0, 1  
series = []  

while a <= n:  
    series.append(a)  
    a, b = b, a + b  

print(f"The Fibonacci series up to {n} is: {series}")  
