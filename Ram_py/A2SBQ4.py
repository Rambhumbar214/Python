def count_word_occurrences(sentence):
   
    words = sentence.split()
    
    
    word_count = {}
    
   
    for word in words:
       
        word = word.lower()
        
  
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count


sentence = input("Enter a sentence: ")


word_count = count_word_occurrences(sentence)


print("Word occurrences:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
