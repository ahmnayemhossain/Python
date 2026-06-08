print("Day 12 practice exercises")

print("\nExercise 1: Count with range")
for number in range(1, 6):
    print(number)

print("\nExercise 2: Accumulator")
total = 0
for value in range(1, 6):
    total += value
print(total)

print("\nExercise 3: Even numbers")
for value in range(2, 11, 2):
    print(value)

print("\nExercise 4: Word repeat")
word = input("Enter a word: ")
for _ in range(3):
    print(word)

print("\nExercise 5: Character counter")
name = input("Enter your name: ")
count = 0
for _ in name:
    count += 1
print(count)
