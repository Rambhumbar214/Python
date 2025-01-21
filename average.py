#write a python program to calculate the average of numbers in a given list
numbers=[10,20,30,40,50]
if len(numbers) == 0:
    print("The list is empty. No average to calculate.")
else:
    
    total = sum(numbers)
    average = total / len(numbers)
    print(f"The average of the list is: {average}")
