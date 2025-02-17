def is_palindrome(input_string):
    
    cleaned_string = input_string.replace(" ", "").lower()
    
    
    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False


input_string = input("Enter a string: ")


if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
