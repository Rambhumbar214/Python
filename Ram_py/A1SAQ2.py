def check_duplicates(numbers):
    
    if len(numbers) != len(set(numbers)):
        print("Duplicates")
    else:
        print("Unique")


numbers = []
for i in range(6):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)


check_duplicates(numbers)
