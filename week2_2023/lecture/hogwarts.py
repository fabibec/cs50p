# Iteration with lists
"""
students = ["Harry","Ron","Hermione"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])
"""

# Dicts
"""
students_dict = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students_dict:
    print(student, students_dict[student], sep=" | ")
"""

# List of dicts
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=",")