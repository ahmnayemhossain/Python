print("Day 03 practice exercises")

print("\nExercise 1: Integer to string")
age = 25
print("Age: " + str(age))

print("\nExercise 2: Float formatting")
price = 99.5
print(f"Formatted price: {price:.2f}")

print("\nExercise 3: Basic type conversion")
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
sum_result = int(first_number) + int(second_number)
print(f"Sum: {sum_result}")

print("\nExercise 4: Simple f-string output")
user_name = input("Enter your name: ")
learning_goal = input("Enter your learning goal: ")
print(f"{user_name} wants to improve in {learning_goal}.")

print("\nExercise 5: Split bill practice")
snack_bill = input("Enter snack bill amount: ")
friend_count = input("Enter number of friends: ")
per_friend = float(snack_bill) / int(friend_count)
print(f"Each friend pays: {per_friend:.2f}")
