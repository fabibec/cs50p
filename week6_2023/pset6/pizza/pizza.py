import sys
import csv
from tabulate import tabulate

def main():
    # Validate input
    l = len(sys.argv)
    if l > 2:
        sys.exit("Too many command-line arguments")
    elif l < 2:
        sys.exit("Tow few command-line arguments")

    if sys.argv[1].rfind(".csv") == -1:
        sys.exit("Not a CSV file")

    # Store Menu Data in list
    menu = []

    # Read fieldnames for the CSV-File and check if file exits
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print the data using the tabulate function
    print(tabulate(menu, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()

