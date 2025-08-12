'''Write an anonymous function to calculate area of square.'''

# Lambda function to calculate area of square
area_of_square = lambda side: side ** 2

# Accept the side length of the square from the user
side_length = float(input("Enter the side length of the square: "))

# Calculate the area and display the result
area = area_of_square(side_length)
print(f"The area of the square is: {area}")
