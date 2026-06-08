print("Day 22 practice exercises")

print("\nExercise 1: Basic dictionary")
student = {"name": "Nayem", "age": 25}
print(student["name"])

print("\nExercise 2: Add key-value pair")
student["city"] = "Dhaka"
print(student)

print("\nExercise 3: Update value")
student["age"] = 26
print(student)

print("\nExercise 4: Loop through dictionary")
for key, value in student.items():
    print(f"{key}: {value}")

print("\nExercise 5: User dictionary")
favorite_color = input("Enter favorite color: ")
profile = {"color": favorite_color}
print(profile)
