from pathlib import Path

print("Day 29 practice exercises")

print("\nExercise 1: Current file name")
current_file = Path(__file__).name
print(current_file)

print("\nExercise 2: Current folder")
current_folder = Path(__file__).parent.name
print(current_folder)

print("\nExercise 3: Join path")
sample_path = Path("notes") / "today.txt"
print(sample_path)

print("\nExercise 4: Check suffix")
print(sample_path.suffix)

print("\nExercise 5: User tool name")
tool_name = input("Enter a tool name: ")
print(f"Tool created: {tool_name}")
