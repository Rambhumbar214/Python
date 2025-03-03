def swap_and_combine(str1, str2):
    
    return str2[:2] + str1[2:] + str1[:2] + str2[2:]


str1 = input('enter a string')
str2 = input('enter a string')


result = swap_and_combine(str1, str2)


print(result)
