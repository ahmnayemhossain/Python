from pathlib import Path

print("Day 31 practice exercises")

print("\nExercise 1: Relative path")
relative_path = Path("sample.txt")
print(relative_path)

print("\nExercise 2: Absolute path")
print(relative_path.resolve())

print("\nExercise 3: Parent folder")
print(Path(__file__).parent)

print("\nExercise 4: File name and suffix")
example_file = Path("notes.txt")
print(example_file.name)
print(example_file.suffix)

print("\nExercise 5: User path check")
user_path = Path(input("Enter a path name: "))
print(user_path.is_absolute())
