class SmallValueError(Exception):
    pass


print("Day 37 practice exercises")

print("\nExercise 1: Raise custom error")
try:
    value = int(input("Enter a number greater than 5: "))
    if value <= 5:
        raise SmallValueError("Number is too small.")
    print("Accepted")
except SmallValueError as error:
    print(error)

print("\nExercise 2: Validate username")
username = input("Enter username: ")
if len(username) < 4:
    print("Invalid username")
else:
    print("Valid username")

print("\nExercise 3: Validate email format")
email = input("Enter email: ")
print("@" in email)

print("\nExercise 4: Catch ValueError")
try:
    int(input("Enter age: "))
    print("Valid number")
except ValueError:
    print("Invalid number")

print("\nExercise 5: Confirm non-empty field")
city = input("Enter city: ").strip()
if city:
    print("City accepted")
else:
    print("City required")
