''' Write a Python program which finds sum of digits of a number. [20 M] 
Example n=130 then output is 4 (1+3+0). '''

# Accept an integer value from the user
n = int(input("Enter a number: "))

# Initialize sum to 0
sum_of_digits = 0

# Loop to extract digits and add them to the sum
while n > 0:
    digit = n % 10  # Get the last digit
    sum_of_digits += digit  # Add the digit to sum
    n //= 10  # Remove the last digit from the number

# Display the sum of digits
print(f"The sum of the digits is: {sum_of_digits}")
