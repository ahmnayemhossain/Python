print("Day 11 practice exercises")

print("\nExercise 1: Nested list access")
products = [["Pen", 10], ["Book", 80]]
print(products[0][0])

print("\nExercise 2: Add nested item")
products.append(["Bag", 500])
print(products)

print("\nExercise 3: Update nested price")
products[1][1] = 90
print(products)

print("\nExercise 4: Count nested items")
print(len(products))

print("\nExercise 5: Print all items")
for product in products:
    print(f"{product[0]} - {product[1]}")
