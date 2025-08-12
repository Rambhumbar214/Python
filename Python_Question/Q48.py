'''Write a Python program to display the following pattern (Floyd's triangle) 
For n=3 
1 
2 3 
4 5 6'''

# Accept the value of n from the user
n = int(input("Enter the number of rows for Floyd's triangle: "))

# Variable to keep track of the current number
current_number = 1

# Loop through the rows
for i in range(1, n+1):
    # Print numbers for the current row
    for j in range(i):
        print(current_number, end=" ")
        current_number += 1
    # Move to the next line after each row
    print()
