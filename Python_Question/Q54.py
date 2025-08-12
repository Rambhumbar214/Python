''') Write a program to display following pattern. [20 M] 
1 2 3 4 
1 2 3  
1 2   
1  '''

# Number of rows in the pattern
n = 4

# Loop through each row
for i in range(n, 0, -1):
    # Print numbers from 1 to i for each row
    for j in range(1, i+1):
        print(j, end=" ")
    # Move to the next line after each row
    print()
