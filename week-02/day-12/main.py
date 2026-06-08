import random

print("Welcome to Password Generator V1!")

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*")

letter_count = int(input("How many letters would you like? "))
symbol_count = int(input("How many symbols would you like? "))
number_count = int(input("How many numbers would you like? "))

password_chars = []

for _ in range(letter_count):
    password_chars.append(random.choice(letters))

for _ in range(symbol_count):
    password_chars.append(random.choice(symbols))

for _ in range(number_count):
    password_chars.append(random.choice(numbers))

random.shuffle(password_chars)
password = "".join(password_chars)

print(f"Generated password: {password}")
