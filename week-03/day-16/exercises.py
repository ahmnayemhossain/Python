print("Day 16 practice exercises")


def greet(name):
    print(f"Hello, {name}")


def square(number):
    return number * number


def is_even(number):
    return number % 2 == 0


print("\nExercise 1: Greeting function")
greet("Nayem")

print("\nExercise 2: Square function")
print(square(6))

print("\nExercise 3: Even check function")
print(is_even(10))

print("\nExercise 4: Parameter practice")
user_name = input("Enter your name: ")
greet(user_name)

print("\nExercise 5: Return value practice")
value = int(input("Enter a number: "))
print(square(value))
