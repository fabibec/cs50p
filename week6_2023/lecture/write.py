import csv

name = input("What's your name? ")
age = input("What's your age? ")

with open("write.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","age"])
    writer.writerow({"name":name, "age": age})