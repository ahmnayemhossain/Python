print("Day 38 practice exercises")

print("\nExercise 1: Square list")
numbers = [1, 2, 3, 4]
squares = [number * number for number in numbers]
print(squares)

print("\nExercise 2: Uppercase words")
words = ["python", "code", "learn"]
upper_words = [word.upper() for word in words]
print(upper_words)

print("\nExercise 3: Filter odd numbers")
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)

print("\nExercise 4: User numbers")
values = input("Enter numbers separated by spaces: ").split()
converted_values = [int(value) for value in values]
print(converted_values)

print("\nExercise 5: Lengths of words")
lengths = [len(word) for word in words]
print(lengths)
