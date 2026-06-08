import os
from pathlib import Path

print("Day 53 practice exercises")

print("\nExercise 1: Environment variable read")
print(os.getenv("API_KEY") is not None)

print("\nExercise 2: Secrets reminder")
print(".env should not be committed.")

print("\nExercise 3: Example env path")
print(Path(__file__).with_name(".env.example").name)

print("\nExercise 4: User env key name")
key_name = input("Enter a key name: ")
print(f"Keep {key_name} in .env")

print("\nExercise 5: Safe fallback")
print(os.getenv("MISSING_KEY", "demo-mode"))
