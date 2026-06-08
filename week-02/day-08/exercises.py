print("Day 08 practice exercises")

print("\nExercise 1: Login check")
user_name = input("Enter username: ")
password = input("Enter password: ")
if user_name == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

print("\nExercise 2: Weather advice")
is_raining = input("Is it raining? yes/no: ").lower()
has_umbrella = input("Do you have an umbrella? yes/no: ").lower()
if is_raining == "yes" and has_umbrella == "yes":
    print("Go outside carefully")
elif is_raining == "yes":
    print("Stay inside or get an umbrella")
else:
    print("Enjoy the day")

print("\nExercise 3: Grade band")
marks = int(input("Enter marks: "))
if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("Needs improvement")

print("\nExercise 4: Access check")
age = int(input("Enter age: "))
member = input("Are you a member? yes/no: ").lower()
if age >= 18 or member == "yes":
    print("Access granted")
else:
    print("Access denied")

print("\nExercise 5: Nested decision")
time_of_day = input("Enter time (day/night): ").lower()
if time_of_day == "day":
    activity = input("Work or study? ").lower()
    if activity == "study":
        print("Open your notebook")
    else:
        print("Start your task")
else:
    print("Take some rest")
