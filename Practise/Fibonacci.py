"""write a program which finds sum of digits of a number"""

n = int(input("Enter a number: "))


n = abs(n)


sum_of_digits = sum(int(digit) for digit in str(n))


print(f"The sum of digits is: {sum_of_digits}")
