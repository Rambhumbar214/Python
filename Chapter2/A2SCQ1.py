str1 = "/*Sachin is @Cricketer & kind person"

# Remove non-alphanumeric characters except spaces
cleaned_string = ''.join(c for c in str1 if c.isalnum() or c.isspace())

# Convert the cleaned string to lowercase
final_string = cleaned_string.lower()

# Print the final result
print(f"Expected output: '{final_string}'")
