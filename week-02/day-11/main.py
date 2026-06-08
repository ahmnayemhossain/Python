print("Welcome to the Shopping Cart CLI!")

cart_items = []

while True:
    item_name = input("Enter item name or 'done': ")
    if item_name.lower() == "done":
        break

    item_price = float(input("Enter item price: "))
    cart_items.append([item_name, item_price])

total_price = 0

print("\nCart Summary:")
for item in cart_items:
    print(f"- {item[0]}: {item[1]:.2f}")
    total_price += item[1]

print(f"Total: {total_price:.2f}")
