print("Day 54 practice exercises")

print("\nExercise 1: HTTP method names")
for method_name in ["GET", "POST", "PUT", "DELETE"]:
    print(method_name)

print("\nExercise 2: Sample payload")
payload = {"habit": "Reading", "status": "done"}
print(payload)

print("\nExercise 3: Update concept")
payload["status"] = "pending"
print(payload)

print("\nExercise 4: Delete concept")
deleted_id = input("Enter a habit id to delete: ")
print(f"Would send DELETE for {deleted_id}")

print("\nExercise 5: POST success status")
print(201)
