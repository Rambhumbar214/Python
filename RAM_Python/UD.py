def find_duplicates():
    
    values = []
    print("Enter 6 integer values:")
    for i in range(6):
        value = int(input(f"Enter value {i + 1}: "))
        values.append(value)
    
    duplicates = [value for value in set(values) if values.count(value) > 1]
    
    if duplicates:
        print(f"Duplicate values: {set(duplicates)}")
    else:
        print("All values are unique.")
        

find_duplicates()
