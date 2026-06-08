print("Welcome to Word Frequency Counter!")

sentence = input("Enter a sentence: ").lower()
words = sentence.split()
unique_words = sorted(set(words))

word_frequency = {word: words.count(word) for word in unique_words}

for word, count in word_frequency.items():
    print(f"{word}: {count}")
