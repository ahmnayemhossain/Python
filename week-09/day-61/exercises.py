print("Day 61 practice exercises")

print("\nExercise 1: Safety rule")
print("Do not automate actions too quickly.")

print("\nExercise 2: Rate limit idea")
print("Pause between repeated actions when needed.")

print("\nExercise 3: File extension group")
file_names = ["report.pdf", "photo.jpg", "notes.txt"]
for file_name in file_names:
    print(file_name.split(".")[-1])

print("\nExercise 4: User filename")
user_file = input("Enter a filename: ")
print(user_file.split(".")[-1] if "." in user_file else "no_extension")

print("\nExercise 5: Skip duplicate concept")
print("Do not overwrite files without checking first.")
