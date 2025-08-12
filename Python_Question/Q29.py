'''Write a Python program to reverse a given number.'''

# Accept input number from the user
num = int(input("Enter a number: "))

# Reverse the number
reversed_num = 0
while num > 0:
    digit = num % 10         # Get the last digit of the number
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num = num // 10          # Remove the last digit from the number

# Print the reversed number
print("Reversed number:", reversed_num)
