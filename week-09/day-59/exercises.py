print("Day 59 practice exercises")

print("\nExercise 1: Table row concept")
row = ["Company", "Role"]
print(row)

print("\nExercise 2: Nested list")
jobs = [["Softnan", "Developer"], ["DataHub", "Analyst"]]
print(jobs[0][1])

print("\nExercise 3: Loop rows")
for job in jobs:
    print(job[0], "-", job[1])

print("\nExercise 4: User job entry")
company = input("Enter company: ")
role = input("Enter role: ")
print([company, role])

print("\nExercise 5: Header skip concept")
print("Skip the first row if it is a header.")
