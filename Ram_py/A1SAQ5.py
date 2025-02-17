def fibonacci_series(n):
   
    a, b = 0, 1
    series = []
    
    while a <= n:
        series.append(a)
        a, b = b, a + b
    
    return series


n = int(input("Enter a number: "))


series = fibonacci_series(n)
print(f"The Fibonacci series up to {n} is: {series}")
