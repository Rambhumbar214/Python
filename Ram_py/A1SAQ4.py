def sum_of_digits(n):
   
    return sum(int(digit) for digit in str(n))


n = int(input("Enter a number: "))


result = sum_of_digits(n)
print(f"The sum of digits is: {result}")
