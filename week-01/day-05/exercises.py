print("Day 05 practice exercises")

print("\nExercise 1: Voting check")
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

print("\nExercise 2: Number comparison")
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

print("\nExercise 3: Exam result")
marks = int(input("Enter your marks: "))
if marks >= 33:
    print("Pass")
else:
    print("Fail")

print("\nExercise 4: Age group")
person_age = int(input("Enter another age: "))
if person_age < 13:
    print("Child")
elif person_age < 20:
    print("Teenager")
else:
    print("Adult")

print("\nExercise 5: Password length check")
password = input("Enter a password: ")
if len(password) >= 8:
    print("Strong enough for practice")
else:
    print("Too short")
