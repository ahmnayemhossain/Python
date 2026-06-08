try:
    import requests
except ImportError:
    requests = None

print("Day 51 practice exercises")

print("\nExercise 1: Requests availability")
print(requests is not None)

print("\nExercise 2: Status code concept")
sample_status_code = 200
print(sample_status_code)

print("\nExercise 3: JSON-like dictionary")
sample_response = {"city": "Dhaka", "temp": 30}
print(sample_response["temp"])

print("\nExercise 4: User city echo")
city_name = input("Enter a city: ")
print(f"Checking city: {city_name}")

print("\nExercise 5: API success check")
status_code = int(input("Enter a status code: "))
print(status_code == 200)
