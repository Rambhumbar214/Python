from collections import Counter

s = input('Enter a string: ')
for char, freq in Counter(s).items():
    print("Character: {char}, Frequency: {freq}")
