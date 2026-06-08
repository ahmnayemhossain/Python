print("Day 39 practice exercises")

print("\nExercise 1: Basic dictionary comprehension")
numbers = [1, 2, 3, 4]
square_map = {number: number * number for number in numbers}
print(square_map)

print("\nExercise 2: Word lengths")
words = ["python", "code", "learn"]
length_map = {word: len(word) for word in words}
print(length_map)

print("\nExercise 3: Filtered dictionary")
even_square_map = {number: number * number for number in numbers if number % 2 == 0}
print(even_square_map)

print("\nExercise 4: User word map")
user_words = input("Enter words separated by spaces: ").split()
user_map = {word: len(word) for word in user_words}
print(user_map)

print("\nExercise 5: Character count")
text = input("Enter a short text: ")
character_map = {character: text.count(character) for character in sorted(set(text))}
print(character_map)
