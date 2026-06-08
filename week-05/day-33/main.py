import json
from pathlib import Path

VAULT_FILE = Path(__file__).with_name("vault.json")


def load_vault():
    if VAULT_FILE.exists():
        with VAULT_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_vault(vault_data):
    with VAULT_FILE.open("w", encoding="utf-8") as file:
        json.dump(vault_data, file, indent=2)


print("Welcome to Password Vault JSON V1!")

vault = load_vault()

while True:
    print("\n1. Add password")
    print("2. View all accounts")
    print("3. Search account")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account_name = input("Enter account name: ").strip()
        password = input("Enter password: ").strip()
        vault[account_name] = password
        save_vault(vault)
        print("Password saved.")
    elif choice == "2":
        if not vault:
            print("Vault is empty.")
        else:
            for account_name, password in vault.items():
                print(f"{account_name}: {password}")
    elif choice == "3":
        account_name = input("Enter account name to search: ").strip()
        print(vault.get(account_name, "Account not found."))
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
