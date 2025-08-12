''' Write a Python program to create a set with any 3 weekdays. Add single element to the set 
and print it. Add multiple elements and print the set. '''

# Create a set with three weekdays
weekdays = {"Monday", "Tuesday", "Wednesday"}

# Add a single element to the set
weekdays.add("Thursday")
print("After adding a single element:", weekdays)

# Add multiple elements to the set
weekdays.update(["Friday", "Saturday", "Sunday"])
print("After adding multiple elements:", weekdays)
