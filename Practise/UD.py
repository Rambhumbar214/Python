"""write a program which accepts 6 intger values and prints
"Duplicates" if any of the values entered are duplicates
otherwise it prints "all Unique"
example let 5 integers are (32,10,45,90,45,6)
then output Duplicates to be printed"""

 
numbers = []
print("Enter 6 integers:")
for _ in range(6):
    num = int(input())
    numbers.append(num)

if len(numbers) != len(set(numbers)):
    print("Duplicates")
else:
    print("All Unique")
