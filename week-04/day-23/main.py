print("Welcome to Student Result Management CLI!")

students = {
    "Rahim": {"marks": [78, 82, 90]},
    "Karim": {"marks": [65, 70, 68]},
    "Jui": {"marks": [88, 92, 85]},
}

for name, data in students.items():
    marks = data["marks"]
    average_mark = sum(marks) / len(marks)
    print(f"{name}: marks={marks}, average={average_mark:.2f}")
