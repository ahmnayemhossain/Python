print("Day 25 practice exercises")

print("\nExercise 1: Print debugging")
value = 5
print(f"DEBUG: value = {value}")
print(value * 2)

print("\nExercise 2: Track loop values")
for number in range(3):
    print(f"DEBUG: number = {number}")

print("\nExercise 3: Debug input")
user_number = int(input("Enter a number: "))
print(f"DEBUG: user_number = {user_number}")
print(user_number + 10)

print("\nExercise 4: Check condition path")
marks = int(input("Enter marks: "))
print(f"DEBUG: marks = {marks}")
if marks >= 33:
    print("Pass")
else:
    print("Fail")

print("\nExercise 5: Track list changes")
items = ["pen"]
print(f"DEBUG: before append = {items}")
items.append("book")
print(f"DEBUG: after append = {items}")
