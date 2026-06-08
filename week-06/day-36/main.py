print("Welcome to Safe Calculator with Error Handling!")

try:
    first_number = float(input("Enter first number: "))
    operator = input("Choose operation (+, -, *, /): ")
    second_number = float(input("Enter second number: "))

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    else:
        raise ValueError("Invalid operator.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Result: {result}")
finally:
    print("Calculator session finished.")
