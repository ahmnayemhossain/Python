from datetime import date, datetime, timedelta

print("Day 40 practice exercises")

print("\nExercise 1: Today's date")
print(date.today())

print("\nExercise 2: Current datetime")
print(datetime.now())

print("\nExercise 3: Add days")
future_date = date.today() + timedelta(days=7)
print(future_date)

print("\nExercise 4: Parse date")
user_date = input("Enter a date (YYYY-MM-DD): ")
print(date.fromisoformat(user_date))

print("\nExercise 5: Year and month")
today = date.today()
print(today.year)
print(today.month)
