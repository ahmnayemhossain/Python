print("Day 04 practice exercises")

print("\nExercise 1: Power operator")
square_number = 6
print(f"Square of {square_number}: {square_number ** 2}")

print("\nExercise 2: Division and rounding")
total_marks = 487
subject_count = 6
average_marks = total_marks / subject_count
print(f"Average marks: {average_marks:.2f}")

print("\nExercise 3: BMI number only")
practice_height = float(input("Enter practice height in meters: "))
practice_weight = float(input("Enter practice weight in kilograms: "))
practice_bmi = practice_weight / (practice_height ** 2)
print(f"Practice BMI: {practice_bmi:.2f}")

print("\nExercise 4: Simple remainder")
total_mangoes = 25
friends = 4
remaining_mangoes = total_mangoes % friends
print(f"Remaining mangoes: {remaining_mangoes}")

print("\nExercise 5: Rounded temperature")
temperature = float(input("Enter temperature in Celsius: "))
print(f"Rounded temperature: {round(temperature)}")
