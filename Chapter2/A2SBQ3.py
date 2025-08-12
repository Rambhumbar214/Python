input_string = input("Enter a string: ")

result = "".join(input_string[i] for i in range(len(input_string)) if i % 2 == 0)

print(f"String after removing characters with odd index values: {result}")
