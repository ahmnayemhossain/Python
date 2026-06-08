import csv
from pathlib import Path

practice_csv = Path(__file__).with_name("practice.csv")

print("Day 32 practice exercises")

print("\nExercise 1: Write CSV row")
with practice_csv.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["item", "price"])
    writer.writerow(["pen", "10"])
print("CSV file written.")

print("\nExercise 2: Read CSV rows")
with practice_csv.open("r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\nExercise 3: Append CSV row")
with practice_csv.open("a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["book", "80"])
print("Row appended.")

print("\nExercise 4: Count lines")
with practice_csv.open("r", newline="", encoding="utf-8") as file:
    print(len(list(csv.reader(file))))

print("\nExercise 5: User expense row")
category = input("Enter category: ")
amount = input("Enter amount: ")
with practice_csv.open("a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([category, amount])
print("User row added.")
