print("Day 36 practice exercises")

print("\nExercise 1: Try-except integer input")
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid number.")

print("\nExercise 2: Division error handling")
try:
    print(10 / int(input("Enter a divisor: ")))
except ZeroDivisionError:
    print("Cannot divide by zero.")

print("\nExercise 3: Else block")
try:
    value = int(input("Enter another number: "))
except ValueError:
    print("Bad input.")
else:
    print(value + 5)

print("\nExercise 4: Finally block")
try:
    text = input("Enter any text: ")
    print(text)
finally:
    print("Input finished.")

print("\nExercise 5: Custom message")
try:
    float(input("Enter decimal number: "))
    print("Good input.")
except ValueError:
    print("Not a decimal number.")
