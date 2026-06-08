import csv
from pathlib import Path

CSV_FILE = Path(__file__).with_name("expenses.csv")

print("Welcome to Expense Tracker CSV!")

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: "))
        with CSV_FILE.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])
        print("Expense saved.")
    elif choice == "2":
        if not CSV_FILE.exists():
            print("No expenses yet.")
            continue

        total_amount = 0
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"{row[0]}: {float(row[1]):.2f}")
                    total_amount += float(row[1])
        print(f"Total: {total_amount:.2f}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
