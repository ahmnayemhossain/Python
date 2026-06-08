print("Day 23 practice exercises")

print("\nExercise 1: Nested dictionary")
school = {"student": {"name": "Nayem", "marks": [80, 90, 85]}}
print(school["student"]["name"])

print("\nExercise 2: Access nested list")
print(school["student"]["marks"][1])

print("\nExercise 3: Add nested value")
school["student"]["city"] = "Dhaka"
print(school)

print("\nExercise 4: Loop through nested data")
for key, value in school["student"].items():
    print(f"{key}: {value}")

print("\nExercise 5: User result entry")
user_name = input("Enter student name: ")
user_marks = [int(input("Enter mark 1: ")), int(input("Enter mark 2: "))]
record = {user_name: {"marks": user_marks}}
print(record)
