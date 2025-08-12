"""write a program which finds sum of digits of a number
example n=130 then output is 4(1+3+0)"""

n = int(input("Enter a number: "))


sum_of_digits = 0


while n > 0:
    digit = n % 10  
    sum_of_digits += digit  
    n = n // 10  


print(f"The sum of digits is: {sum_of_digits}")
