import random

print("Welcome to the Who Pays the Bill App!")

names_text = input("Enter names separated by commas: ")
names = [name.strip() for name in names_text.split(",") if name.strip()]

selected_name = random.choice(names)

print(f"{selected_name} will pay the bill today.")
