from pathlib import Path

NOTES_FILE = Path(__file__).with_name("notes.txt")

print("Welcome to Notes App Using Text File!")

while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note_text = input("Enter note text: ")
        with NOTES_FILE.open("a", encoding="utf-8") as file:
            file.write(note_text + "\n")
        print("Note saved.")
    elif choice == "2":
        if NOTES_FILE.exists():
            with NOTES_FILE.open("r", encoding="utf-8") as file:
                content = file.read().strip()
            print(content if content else "No notes yet.")
        else:
            print("No notes yet.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
