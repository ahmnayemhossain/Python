class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"


print("Day 43 practice exercises")

print("\nExercise 1: Create object")
student = Student("Nayem")
print(student.name)

print("\nExercise 2: Call method")
print(student.greet())

print("\nExercise 3: Another object")
friend = Student("Jui")
print(friend.greet())

print("\nExercise 4: Object list")
students = [student, friend]
for learner in students:
    print(learner.name)

print("\nExercise 5: User object")
user_name = input("Enter a student name: ")
user_student = Student(user_name)
print(user_student.greet())
