print("Welcome to the Age-Based Ticket Price App!")

age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age < 12:
    price = 200
elif age < 18:
    price = 350
elif age < 60:
    price = 500
else:
    price = 250

print(f"Your ticket price is: {price} BDT")
