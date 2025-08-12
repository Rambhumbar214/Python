'''Write a Python program which accepts 6 integer values and prints “DUPLICATES” if any 
of the values entered are duplicates otherwise it prints “ALL UNIQUE”. 
Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed.'''

# Accept 6 integer values from the user
numbers = []
for i in range(6):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

# Check for duplicates
if len(numbers) != len(set(numbers)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")
