print("Day 67 practice exercises")

print("\nExercise 1: JSON key concept")
record = {"website": {"email": "a@example.com", "password": "123"}}
print(record["website"]["email"])

print("\nExercise 2: GUI field names")
print(["website", "email", "password"])

print("\nExercise 3: Save concept")
print("Store data as JSON text.")

print("\nExercise 4: User website")
website = input("Enter website name: ")
print(website)

print("\nExercise 5: Dictionary update")
record["github"] = {"email": "b@example.com", "password": "xyz"}
print(record)
