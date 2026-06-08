print("Day 15 practice exercises")

print("\nExercise 1: Count down")
count = 5
while count > 0:
    print(count)
    count -= 1

print("\nExercise 2: Break demo")
number = 1
while True:
    print(number)
    if number == 3:
        break
    number += 1

print("\nExercise 3: Continue demo")
for value in range(1, 6):
    if value == 3:
        continue
    print(value)

print("\nExercise 4: Loop until yes")
answer = ""
while answer != "yes":
    answer = input("Type yes to stop: ").lower()

print("\nExercise 5: Sum with while")
index = 1
total = 0
while index <= 5:
    total += index
    index += 1
print(total)
