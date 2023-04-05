import sys

def main():
    # Validate input
    l = len(sys.argv)
    if l > 2:
        sys.exit("Too many command-line arguments")
    elif l < 2:
        sys.exit("Tow few command-line arguments")

    if sys.argv[1].rfind(".py") == -1:
        sys.exit("Not a python file")

    lines = 0

    # Try to open file
    try:
        # Count lines, ignore comments and empty lines
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip() and not line.strip().startswith("#"):
                    lines += 1

        # Print the count
        print(lines)

    except FileNotFoundError:
        sys.exit("The file does not exist")

if __name__ == "__main__":
    main()
