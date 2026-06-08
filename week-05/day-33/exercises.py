import json
from pathlib import Path

practice_json = Path(__file__).with_name("practice.json")

print("Day 33 practice exercises")

print("\nExercise 1: Write JSON")
data = {"name": "Nayem", "skill": "Python"}
with practice_json.open("w", encoding="utf-8") as file:
    json.dump(data, file)
print("JSON written.")

print("\nExercise 2: Read JSON")
with practice_json.open("r", encoding="utf-8") as file:
    print(json.load(file))

print("\nExercise 3: Update JSON")
data["level"] = "Beginner"
with practice_json.open("w", encoding="utf-8") as file:
    json.dump(data, file)
print("JSON updated.")

print("\nExercise 4: Load updated JSON")
with practice_json.open("r", encoding="utf-8") as file:
    print(json.load(file))

print("\nExercise 5: User JSON value")
favorite_tool = input("Enter favorite tool: ")
data["tool"] = favorite_tool
print(data)
