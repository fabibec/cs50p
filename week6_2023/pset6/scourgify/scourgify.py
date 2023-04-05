import sys
import csv
from tabulate import tabulate

def main():
    # Validate input
    l = len(sys.argv)
    if l > 3:
        sys.exit("Too many command-line arguments")
    elif l < 3:
        sys.exit("Tow few command-line arguments")

    if sys.argv[1].rfind(".csv") == -1:
        sys.exit("Not a CSV file")

    data = []

    # Read Data from the CSV-File
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                data.append({"first":first, "last":last, "house":row["house"]})



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write Data into new File
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        # Header
        writer.writeheader()
        # Actual Data
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    main()
