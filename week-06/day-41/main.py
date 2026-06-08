from datetime import date


class ReminderValidationError(Exception):
    pass


def parse_due_date(date_text):
    try:
        due_date = date.fromisoformat(date_text)
    except ValueError as error:
        raise ReminderValidationError("Date must be in YYYY-MM-DD format.") from error

    if due_date < date.today():
        raise ReminderValidationError("Date cannot be in the past.")

    return due_date


print("Week 06 Exam - Robust Reminder CLI with Validation")

reminders = []

while True:
    print("\n1. Add reminder")
    print("2. View reminders")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter reminder title: ").strip()
        due_date_text = input("Enter due date (YYYY-MM-DD): ").strip()

        try:
            if not title:
                raise ReminderValidationError("Title is required.")
            due_date = parse_due_date(due_date_text)
        except ReminderValidationError as error:
            print(f"Validation error: {error}")
        else:
            reminders.append({"title": title, "due_date": due_date.isoformat()})
            print("Reminder added.")
    elif choice == "2":
        if not reminders:
            print("No reminders available.")
        else:
            upcoming = [reminder for reminder in reminders if reminder["due_date"] >= date.today().isoformat()]
            for reminder in upcoming:
                print(f"{reminder['title']} - {reminder['due_date']}")
    elif choice == "3":
        print("Exam complete.")
        break
    else:
        print("Invalid option.")
