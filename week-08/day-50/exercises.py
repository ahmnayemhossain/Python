from pathlib import Path

print("Day 50 practice exercises")

print("\nExercise 1: Show current folder")
print(Path(__file__).parent.name)

print("\nExercise 2: List starter files")
for path in sorted(Path(__file__).parent.iterdir()):
    print(path.name)

print("\nExercise 3: Check requirements file")
print((Path(__file__).parent / "requirements.txt").exists())

print("\nExercise 4: Check env example")
print((Path(__file__).parent / ".env.example").exists())

print("\nExercise 5: User package name")
package_name = input("Enter a package name: ")
print(f"Add '{package_name}' to requirements.txt later.")
