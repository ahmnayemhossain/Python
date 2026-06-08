import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expense_data.json")


def load_expenses():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=2)


print("Week 05 Exam - Expense Tracker Save and Load")

expenses = load_expenses()

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Save expenses")
    print("4. Reload expenses")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})
        print("Expense added.")
    elif choice == "2":
        if not expenses:
            print("No expenses available.")
        else:
            total_amount = 0
            for expense in expenses:
                print(f"{expense['category']}: {expense['amount']:.2f}")
                total_amount += expense["amount"]
            print(f"Total: {total_amount:.2f}")
    elif choice == "3":
        save_expenses(expenses)
        print("Expenses saved.")
    elif choice == "4":
        expenses = load_expenses()
        print("Expenses reloaded.")
    elif choice == "5":
        print("Exam complete.")
        break
    else:
        print("Invalid option.")
