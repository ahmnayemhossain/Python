def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Cannot divide by zero"
    return first_number / second_number


print("Welcome to Calculator Functions!")

first_number = float(input("Enter first number: "))
operator = input("Choose operation (+, -, *, /): ")
second_number = float(input("Enter second number: "))

if operator == "+":
    result = add(first_number, second_number)
elif operator == "-":
    result = subtract(first_number, second_number)
elif operator == "*":
    result = multiply(first_number, second_number)
else:
    result = divide(first_number, second_number)

print(f"Result: {result}")
