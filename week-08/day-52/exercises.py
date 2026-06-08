from urllib.parse import urlencode

print("Day 52 practice exercises")

print("\nExercise 1: Query string build")
params = {"name": "bangladesh", "fullText": "true"}
print(urlencode(params))

print("\nExercise 2: Parameter dictionary")
api_params = {"country": "Japan", "lang": "en"}
print(api_params["country"])

print("\nExercise 3: URL join concept")
base_url = "https://example.com/search?"
print(base_url + urlencode(api_params))

print("\nExercise 4: User parameter")
user_country = input("Enter a country name: ")
print(urlencode({"country": user_country}))

print("\nExercise 5: Boolean-like parameter")
print(urlencode({"details": "true"}))
