from collections import Counter

sample_string = input('enter a string')

char_frequency = Counter(sample_string)


for char, freq in char_frequency.items():
    print(f"Character: {char}, Frequency: {freq}")
