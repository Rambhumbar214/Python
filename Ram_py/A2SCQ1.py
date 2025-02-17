import string

def remove_special_symbols(input_string):
   
    cleaned_string = ''.join(char for char in input_string if char.isalnum() or char.isspace())
    return cleaned_string


str1 = "/*Sachin is @Cricketer & kind person"


cleaned_string = remove_special_symbols(str1)


final_string = cleaned_string.lower()


print(f"Expected output: '{final_string}'")
