import random

print("Day 09 practice exercises")

print("\nExercise 1: Random number")
print(random.randint(1, 10))

print("\nExercise 2: Coin toss")
print(random.choice(["Heads", "Tails"]))

print("\nExercise 3: Lucky color")
colors = ["Red", "Blue", "Green", "Yellow"]
print(random.choice(colors))

print("\nExercise 4: Dice roll twice")
print(random.randint(1, 6))
print(random.randint(1, 6))

print("\nExercise 5: Random yes or no")
print(random.choice(["Yes", "No"]))
