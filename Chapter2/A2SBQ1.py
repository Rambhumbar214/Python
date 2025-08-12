def is_palindrome(s):
    return s == s[::-1]


sample_string = input('enter a string')


if is_palindrome(sample_string):
    print(f"'{sample_string}' is a palindrome.")
else:
    print(f"'{sample_string}' is not a palindrome.")
