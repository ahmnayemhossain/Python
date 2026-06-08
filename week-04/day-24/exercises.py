print("Day 24 practice exercises")


def greet(name):
    return f"Hello, {name}"


def total_values(data):
    return sum(data.values())


print("\nExercise 1: Function with dictionary")
prices = {"pen": 10, "book": 80}
print(total_values(prices))

print("\nExercise 2: Greeting function")
print(greet("Nayem"))

print("\nExercise 3: Dictionary update in function")


def add_item(data, key, value):
    data[key] = value
    return data


print(add_item(prices, "bag", 500))

print("\nExercise 4: Return dictionary value")


def get_price(data, key):
    return data.get(key, "Not found")


print(get_price(prices, "pen"))

print("\nExercise 5: User bid entry")
user_name = input("Enter bidder name: ")
user_bid = int(input("Enter bid amount: "))
print({user_name: user_bid})
