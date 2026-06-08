print("Welcome to the Email Username and Domain Extractor!")

email_address = input("Enter an email address: ").strip()

at_index = email_address.index("@")
username = email_address[:at_index]
domain = email_address[at_index + 1 :]

print(f"Username: {username}")
print(f"Domain: {domain}")
