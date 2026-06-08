print("Day 66 practice exercises")

print("\nExercise 1: Event concept")
print("A button click is an event.")

print("\nExercise 2: State variable")
running = False
print(running)

print("\nExercise 3: Time format")
seconds = 125
print(f"{seconds // 60:02d}:{seconds % 60:02d}")

print("\nExercise 4: Toggle state")
running = not running
print(running)

print("\nExercise 5: User timer value")
minutes = int(input("Enter minutes: "))
print(minutes * 60)
