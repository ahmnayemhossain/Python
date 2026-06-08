print("Welcome to Number Filter Tool!")

numbers_text = input("Enter numbers separated by spaces: ")
numbers = [int(number) for number in numbers_text.split()]

even_numbers = [number for number in numbers if number % 2 == 0]
positive_numbers = [number for number in numbers if number > 0]
large_numbers = [number for number in numbers if number > 10]

print(f"Even numbers: {even_numbers}")
print(f"Positive numbers: {positive_numbers}")
print(f"Numbers greater than 10: {large_numbers}")
