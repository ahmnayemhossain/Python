print("Welcome to Contact Book V1!")

contacts = {}

while True:
    print("\n1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print("Contact saved.")
    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "3":
        name = input("Enter contact name to search: ").strip()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
