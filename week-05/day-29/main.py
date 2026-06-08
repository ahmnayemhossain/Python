from toolbox_helpers import add_numbers, count_words, make_uppercase

print("Welcome to Mini Toolbox CLI!")

print("\n1. Add two numbers")
print("2. Count words")
print("3. Make uppercase")

choice = input("Choose a tool: ")

if choice == "1":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print(add_numbers(first_number, second_number))
elif choice == "2":
    text = input("Enter text: ")
    print(count_words(text))
elif choice == "3":
    text = input("Enter text: ")
    print(make_uppercase(text))
else:
    print("Invalid option.")
