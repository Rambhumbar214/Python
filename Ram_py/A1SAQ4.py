n = int(input("Enter a number: "))  
sum_digits = sum(int(digit) for digit in str(n))  
print(f"The sum of digits is: {sum_digits}")  
