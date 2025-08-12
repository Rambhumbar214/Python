''' Write a Python program to count the occurrences of each word in a given sentence.'''

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase to make the count case-insensitive
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word frequencies
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word frequencies
print("Word frequencies:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

