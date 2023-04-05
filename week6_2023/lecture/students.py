import csv

names = []

with open("name.csv") as file:
    """
    for line in file:
        name, att = line.rstrip().split(",")
        names.append({"name":name, "att":att})
    """
    reader = csv.DictReader(file)
    for row in reader:
        names.append({"name": row["name"], "att": row["att"]})
"""
def get_name(student):
    return student["name"]
"""

for item in sorted(names, key=lambda student: student["name"], reverse=True):
    print(f"{item['name']} is a {item['att']}")