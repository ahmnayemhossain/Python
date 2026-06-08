class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name!r})"

    def __str__(self):
        return f"Item: {self.name}"


print("Day 47 practice exercises")

print("\nExercise 1: __str__ demo")
item = Item("Laptop")
print(item)

print("\nExercise 2: __repr__ demo")
print(repr(item))

print("\nExercise 3: Object list printing")
items = [Item("Pen"), Item("Book")]
print(items)

print("\nExercise 4: Human-friendly output")
for thing in items:
    print(str(thing))

print("\nExercise 5: User item")
user_item = Item(input("Enter item name: "))
print(user_item)
