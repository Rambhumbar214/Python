str1 = input('Enter a string: ')
str2 = input('Enter a string: ')

result = str2[:2] + str1[2:] + str1[:2] + str2[2:]

print(result)
