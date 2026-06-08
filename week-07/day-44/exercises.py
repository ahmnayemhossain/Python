class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def summary(self):
        return f"{self.title} has {self.pages} pages."


print("Day 44 practice exercises")

print("\nExercise 1: Create object with init")
book = Book("Python Basics", 120)
print(book.title)

print("\nExercise 2: Read attributes")
print(book.pages)

print("\nExercise 3: Call method")
print(book.summary())

print("\nExercise 4: Update attribute")
book.pages = 140
print(book.summary())

print("\nExercise 5: User object")
title = input("Enter a book title: ")
pages = int(input("Enter page count: "))
user_book = Book(title, pages)
print(user_book.summary())
