import random

print("Week 02 Exam - Password Generator and Shopping Cart Summary")

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*")

letter_count = int(input("How many letters? "))
symbol_count = int(input("How many symbols? "))
number_count = int(input("How many numbers? "))

password_chars = []

for _ in range(letter_count):
    password_chars.append(random.choice(letters))

for _ in range(symbol_count):
    password_chars.append(random.choice(symbols))

for _ in range(number_count):
    password_chars.append(random.choice(numbers))

random.shuffle(password_chars)
password = "".join(password_chars)

cart_items = []
item_count = int(input("How many cart items? "))

for index in range(item_count):
    item_name = input(f"Enter name for item {index + 1}: ")
    item_price = float(input(f"Enter price for item {index + 1}: "))
    cart_items.append([item_name, item_price])

total_price = 0
for item in cart_items:
    total_price += item[1]

print(f"Generated password: {password}")
print("Cart summary:")
for item in cart_items:
    print(f"- {item[0]}: {item[1]:.2f}")
print(f"Total: {total_price:.2f}")
