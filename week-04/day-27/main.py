print("Week 04 Exam - Contact Book with Search, Update, and Delete")

contacts = {}

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. View all")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        contacts[name] = phone
        print("Contact added.")
    elif choice == "2":
        name = input("Enter name to search: ").strip()
        print(contacts.get(name, "Contact not found."))
    elif choice == "3":
        name = input("Enter name to update: ").strip()
        if name in contacts:
            contacts[name] = input("Enter new phone: ").strip()
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "5":
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "6":
        print("Exam complete.")
        break
    else:
        print("Invalid option.")
