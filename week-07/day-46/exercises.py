class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


print("Day 46 practice exercises")

print("\nExercise 1: Parent class")
animal = Animal()
print(animal.speak())

print("\nExercise 2: Child class")
dog = Dog()
print(dog.speak())

print("\nExercise 3: Another child class")
cat = Cat()
print(cat.speak())

print("\nExercise 4: Inherited list")
for pet in [dog, cat]:
    print(pet.speak())

print("\nExercise 5: User animal type")
animal_type = input("Enter dog or cat: ").lower()
chosen_pet = Dog() if animal_type == "dog" else Cat()
print(chosen_pet.speak())
