def get_first_last_chars(s):
    return s[:2] + s[-2:] if len(s) >= 2 else ""


sample_string = input('enter a string')

print(get_first_last_chars(sample_string))
