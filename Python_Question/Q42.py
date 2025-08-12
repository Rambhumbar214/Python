''' Write a Python program which finds sum of digits of a number. [20 M] 
Example n=135 then output is 9 (1+3+5).'''

# Accept input from the user
n = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Use a while loop to iterate through the digits of the number
while n > 0:
    # Get the last digit of the number
    digit = n % 10
    # Add the digit to the sum
    sum_of_digits += digit
    # Remove the last digit from the number
    n = n // 10

# Output the sum of digits
print("Sum of digits:", sum_of_digits)
