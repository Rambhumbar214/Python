def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count


sample_string = input('enter a string')


print(string_length(sample_string))
