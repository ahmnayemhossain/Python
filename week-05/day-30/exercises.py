from pathlib import Path

practice_file = Path(__file__).with_name("practice.txt")

print("Day 30 practice exercises")

print("\nExercise 1: Write text file")
with practice_file.open("w", encoding="utf-8") as file:
    file.write("Python practice\n")
print("File written.")

print("\nExercise 2: Read text file")
with practice_file.open("r", encoding="utf-8") as file:
    print(file.read().strip())

print("\nExercise 3: Append text")
with practice_file.open("a", encoding="utf-8") as file:
    file.write("More practice\n")
print("Text appended.")

print("\nExercise 4: Read all lines")
with practice_file.open("r", encoding="utf-8") as file:
    print(file.readlines())

print("\nExercise 5: User note")
user_note = input("Enter a short note: ")
with practice_file.open("a", encoding="utf-8") as file:
    file.write(user_note + "\n")
print("User note saved.")
