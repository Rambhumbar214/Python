numbers = []  

for i in range(6):  
    num = int(input(f"Enter integer {i+1}: "))  
    numbers.append(num)  

# Check for duplicates  
if len(numbers) != len(set(numbers)):  
    print("Duplicates")  
else:  
    print("Unique")  
